#!/usr/bin/env python

# shadowbox dpi=45 speed=300 power=80 on_time=1.5

import os, sys, time, glob
from math import ceil, floor
from subprocess import *
from itertools import *
from PIL import Image
import optparse

DEFAULT_SPEED=250
DEFAULT_ACCEL=40
DEFAULT_LASER_POWER=100
DEFAULT_LASER_ON_TIME=0.3
DEFAULT_BIDIRECTIONAL_RASTER=True
DEFAULT_ORIGIN_X=0
DEFAULT_ORIGIN_Y=0
DEFAULT_ORIGIN_LOC='bottom_left'
DEFAULT_MIRROR_X=False
DEFAULT_MIRROR_Y=False
DEFAULT_KEEP_ASPECT_RATIO=True
DEFAULT_RASTER_W=-1
DEFAULT_RASTER_H=-1
DEFAULT_XDPI=200
DEFAULT_YDPI=200

def main(image_name, outputObject, SPEED=DEFAULT_SPEED, ACCEL=DEFAULT_ACCEL, laser_power=DEFAULT_LASER_POWER, laser_on_time=DEFAULT_LASER_ON_TIME, bidirectional_raster=DEFAULT_BIDIRECTIONAL_RASTER, origin_x=DEFAULT_ORIGIN_X, origin_y=DEFAULT_ORIGIN_Y, origin_loc=DEFAULT_ORIGIN_LOC, mirror_x=DEFAULT_MIRROR_X, mirror_y=DEFAULT_MIRROR_Y, keep_aspect_ratio=DEFAULT_KEEP_ASPECT_RATIO, raster_w=DEFAULT_RASTER_W, raster_h=DEFAULT_RASTER_H, XDPI=DEFAULT_XDPI, YDPI=DEFAULT_YDPI, air_assist=True, is_metric=False, pause_on_every_line=True):

	outputObject.write('%\n')
	outputObject.write( '(image = %s)\n' % image_name)

	image = Image.open(image_name)

	(img_w,img_h) = image.size
	outputObject.write('(image size w=%u,h=%u)\n' % (img_w,img_h))

	# system parameters
	output_optional_border = False
	distribute_bits_in_floats = False
	MAX_BPF = 53

	# calc lead in + 100% fudge
	leadIn = (1.0*SPEED*SPEED/3600)/ACCEL

	outputObject.write( '(raster requested size w=%f, h=%f)\n' % (raster_w,raster_h))

	# adjust to aspect ratio
	raster_w_scaled_to_h = raster_h*float(img_w)/img_h
	raster_h_scaled_to_w = raster_w*float(img_h)/img_w

	if raster_w < 0 and raster_h < 0:
	    # set size to be exactly input image
	    raster_w = img_w/float(XDPI)
	    raster_h = img_h/float(YDPI)
	    pix_w = img_w
	    pix_h = img_h
	    W = raster_w
	    H = raster_h
	else:
	    if raster_w < 0:
		raster_w = raster_w_scaled_to_h
	    elif raster_h < 0:
		raster_h = raster_h_scaled_to_w
	    elif keep_aspect_ratio:
		if raster_w < raster_w_scaled_to_h:
		    raster_h = raster_h_scaled_to_w
		    outputObject.write( '(keep aspect ratio scaling h down to %f)\n' % (raster_h))
		elif raster_h < raster_h_scaled_to_w:
		    raster_w = raster_w_scaled_to_h
		    outputObject.write( '(keep aspect ratio scaling w down to %f)\n' % (raster_w))

	    # calc image raster size
	    pix_w = int(raster_w * XDPI)
	    pix_h = int(raster_h * YDPI)
	    W = float(pix_w) / XDPI
	    H = float(pix_h) / YDPI

	# handle origin offsetting
	if ( origin_loc == 'center' ):
	    X = origin_x - W/2.0
	    Y = origin_y + H/2.0
	else:
	    if ( 'top' in origin_loc ):
		Y = origin_y
	    elif ( 'bottom' in origin_loc ):
		Y = origin_y + H
	    elif ( 'middle' in origin_loc ):
		Y = origin_y + H/2.0
	    else:
		outputObject.write('unknown origin_loc='+origin_loc+'\n')
		sys.exit()

	    if ( 'left' in origin_loc ):
		X = origin_x
	    elif ( 'center' in origin_loc ):
		X = origin_x - W/2.0
	    elif ( 'right' in origin_loc ):
		X = origin_x - W
	    else:
		outputObject.write('unknown origin_loc='+origin_loc+'\n')
		sys.exit()

	outputObject.write( '(raster upper right corner x=%f,y=%f)\n' % (X,Y))
	outputObject.write( '(raster calculated size w=%f,h=%f)\n' % (W,H))

	if img_w != pix_w or img_h != pix_h:
	    outputObject.write( '(rescaling image to %u,%u pixels)\n' % (pix_w, pix_h))
	    image = image.resize((pix_w, pix_h), Image.BICUBIC)
	else:
	    outputObject.write( '(keeping image size %u,%u pixels)\n' % (pix_w, pix_h))
	image = image.convert('1')

	if mirror_x:
	    outputObject.write( '(flip image left to right)\n')
	    image = image.transpose(Image.FLIP_LEFT_RIGHT)
	if mirror_y:
	    outputObject.write( '(flip image top to bottom)\n')
	    image = image.transpose(Image.FLIP_TOP_BOTTOM)

	image.save('actual.png')

	pix = list(image.getdata())

	# gcode header
	if is_metric:
	    outputObject.write('G21\n')
	else:
	    outputObject.write('G20\n')
	outputObject.write('M101 P%d\n' % laser_power)
	outputObject.write('M63 P0 (turn off laser dout)\n')
	outputObject.write('G0 Z0 (turn off magic z)\n')
	outputObject.write('G64 P0.0001 Q0.0001 (minimal path blending)\n')
	outputObject.write('M68 E0 Q35.000 (set laser power level)\n')
	outputObject.write('M3 S1 (master laser power on)\n')
	if air_assist:
	    outputObject.write('M7 (air assist on)\n')
	outputObject.write('#<raster_speed> = %0.3f\n' % SPEED)
	outputObject.write('F[#<raster_speed>]\n')

	# gcode skip lines that show raster image run box
	if output_optional_border:
	    outputObject.write('/ G0 X%0.4f Y%0.4f\n' % (X,Y))
	    outputObject.write('/ G1 X%0.4f Y%0.4f\n' % (X+W,Y))
	    outputObject.write('/ G1 X%0.4f Y%0.4f\n' % (X+W,Y-H))
	    outputObject.write('/ G1 X%0.4f Y%0.4f\n' % (X,Y-H))
	    outputObject.write('/ G1 X%0.4f Y%0.4f\n' % (X,Y))
	    outputObject.write('/ M2\n')

	outputObject.write('o100 sub\n')
	outputObject.write('  M68 E2 Q[#2]\n')
	outputObject.write('  M68 E1 Q[#1]\n')
	outputObject.write('o100 endsub\n')

	forward = True
	first_output = True

	for y in xrange(0,pix_h):
	    offset_y = Y - 1/float(YDPI)/2 - float(y)/YDPI

	    row = pix[y * pix_w:(y + 1) * pix_w]

	    if not forward:
		row.reverse()

	    first_non_zero = -1
	    last_non_zero = -1
	    for index, pixel in enumerate(row):
		if (pixel <= 127):
		    if (first_non_zero == -1):
			first_non_zero = index
		    last_non_zero = index

	    # debug raster
	    #first_non_zero, last_non_zero = (0,len(row)-1)

	    # some data to output
	    if (first_non_zero >= 0):
		outputObject.write('(raster line %d)\n' % y)

		if distribute_bits_in_floats:
		    # figure out how many max bpf floats to hold the data and
		    # then evenly distribute the bits
		    total_bits = last_non_zero - first_non_zero + 1;
		    BPF = ceil(total_bits / (ceil(float(total_bits) / MAX_BPF)))
		else:
		    # just pack the floats at max
		    BPF = MAX_BPF

		bits = []
		i=0
		bitval=0
		for v in row[first_non_zero:last_non_zero+1]:
		    if (v <= 127):
			bitval += (1<<i)
		    i += 1
		    if (i >= BPF):
			bits.append(bitval);
			bitval = 0
			i = 0
		if (i > 0):
		    bits.append(bitval);

		# forward offsets are:
		#   X where we start
		#     + half a dpi to center the dots
		#     + offset to first bit to not waste time scanning air
		#     - lead in to make sure we are at full speed before output
		if forward:
		    offset_start = X + (1/float(XDPI)/2 + float(first_non_zero)/XDPI - leadIn)
		    offset_end = X + (1/float(XDPI)/2 + float(last_non_zero)/XDPI + leadIn)
		else:
		    offset_start = X + (W - 1/float(XDPI)/2 - float(first_non_zero)/XDPI + leadIn)
		    offset_end = X + (W - 1/float(XDPI)/2 - float(last_non_zero)/XDPI - leadIn)

		outputObject.write('G0 X%0.4f Y%0.4f\n' % (offset_start,offset_y))
		outputObject.write('M68 E1 Q-1 (start new line)\n')
		if first_output:
		    # only have to send this on the first line output
		    outputObject.write('o100 call [-2] [%d] (gcode is metric 0=no,1=yes)\n' % (1 if is_metric else 0))
		    outputObject.write('o100 call [-3] [#<raster_speed>] (speed, in/min or mm/min)\n')
		outputObject.write('o100 call [-4] [%d] (direction)\n' % (1 if forward else -1))
		if first_output:
		    outputObject.write('o100 call [-5] [%0.3f] (dpi)\n' % XDPI)
		if distribute_bits_in_floats or first_output:
		    outputObject.write('o100 call [-6] [%u] (bits per float)\n' % BPF)
		if first_output:
		    outputObject.write('o100 call [-7] [%d] (laser on time, ns)\n' % (laser_on_time*1000000))
		# have to send last parameters as this triggers the line init
		outputObject.write('o100 call [-8] [%0.4f] (lead in)\n' % leadIn)
		outputObject.write('(raster data start)\n')

		first_output = False

		bits_length = len(bits)
		for index, bitval in enumerate(bits):
		    if bitval != 0 or index == bits_length-1:
			# we can skip zeros unless it is the last float
			outputObject.write('o100 call [%u] [%u]\n' % (index+1, bitval))

		outputObject.write('G1 X%0.4f\n' % offset_end)
		if pause_on_every_line:
			outputObject.write('M1\n')

	    if bidirectional_raster:
		# next line is reverse direction
		forward = not forward

	outputObject.write('M68 E1 Q0 (end raster)\n')

	outputObject.write('G0 X%0.4f Y%0.4f (go to start)\n' % (X,Y))
	outputObject.write('M2\n')
	outputObject.write('%\n')

def add_int_param(parser,param, dest, default):
	parser.add_option(*param, action='store', type='int', dest=dest, default=default)

def add_float_param(parser, param, dest, default):
	parser.add_option(*param, action='store', type='float', dest=dest, default=default)

def add_boolean_param(parser, param, dest, default):
	if default:
		parser.add_option(*param, action='store_false', dest=dest, default=default)
	else:
		parser.add_option(*param, action='store_true', dest=dest, default=default)

def add_string_param(parser, param, dest, default):
	parser.add_option(*param, action='store', type='string', dest=dest, default=default)

if __name__ == '__main__':


	parser = optparse.OptionParser()

	add_int_param(parser, ['--speed'], 'speed', DEFAULT_SPEED)
	add_int_param(parser, ['--accel'], 'accel', DEFAULT_ACCEL)
	add_int_param(parser, ['--laser_power'], 'laser_power', DEFAULT_LASER_POWER)
	add_float_param(parser, ['--laser_on_time'], 'laser_on_time', DEFAULT_LASER_ON_TIME)
	add_boolean_param(parser, ['--unidirectional_raster'], 'bidirectional_raster', DEFAULT_BIDIRECTIONAL_RASTER)
	add_float_param(parser, ['--origin_x'], 'origin_x', DEFAULT_ORIGIN_X)
	add_float_param(parser, ['--origin_y'], 'origin_y', DEFAULT_ORIGIN_Y)
	add_string_param(parser, ['--origin_loc'], 'origin_loc', DEFAULT_ORIGIN_LOC)
	add_boolean_param(parser, ['--mirror_x'], 'mirror_x', DEFAULT_MIRROR_X)
	add_boolean_param(parser, ['--mirror_y'], 'mirror_y', DEFAULT_MIRROR_Y)
	add_boolean_param(parser, ['--ignore_aspect_ratio'], 'keep_aspect_ratio', DEFAULT_KEEP_ASPECT_RATIO)
	add_float_param(parser, ['--raster_w'], 'raster_w', DEFAULT_RASTER_W)
	add_float_param(parser, ['--raster_h'], 'raster_h', DEFAULT_RASTER_H)
	add_int_param(parser, ['--xdpi'], 'xdpi', DEFAULT_XDPI)
	add_int_param(parser, ['--ydpi'], 'ydpi', DEFAULT_YDPI)
	add_string_param(parser, ['-o', '--output'], 'outputFile', None)

	(options, args) = parser.parse_args()
	if ( len(args) > 0 and os.path.exists(args[0]) ):
	    image_name = args[0]
	else:
	    image_name = image_not_found()
	if options.outputFile is None:
		outputObject = sys.stdout
		main(image_name, SPEED=options.speed, ACCEL=options.accel, laser_power=options.laser_power, laser_on_time=options.laser_on_time, bidirectional_raster=options.bidirectional_raster, origin_x=options.origin_x, origin_y=options.origin_y, origin_loc=options.origin_loc, mirror_x=options.mirror_x, mirror_y=options.mirror_y, keep_aspect_ratio=options.keep_aspect_ratio, raster_w=options.raster_w, raster_h=options.raster_h, XDPI=options.xdpi, YDPI=options.ydpi, outputObject=outputObject)
	else:
		with open(options.outputFile, 'w') as outputObject:
			main(image_name, SPEED=options.speed, ACCEL=options.accel, laser_power=options.laser_power, laser_on_time=options.laser_on_time, bidirectional_raster=options.bidirectional_raster, origin_x=options.origin_x, origin_y=options.origin_y, origin_loc=options.origin_loc, mirror_x=options.mirror_x, mirror_y=options.mirror_y, keep_aspect_ratio=options.keep_aspect_ratio, raster_w=options.raster_w, raster_h=options.raster_h, XDPI=options.xdpi, YDPI=options.ydpi, outputObject=outputObject)

	#main(image_name, SPEED=options.speed, ACCEL=options.accel, laser_power=options.laser_power, laser_on_time=options.laser_on_time, bidirectional_raster=options.bidirectional_raster, origin_x=options.origin_x, origin_y=options.origin_y, origin_loc=options.origin_loc, mirror_x=options.mirror_x, mirror_y=options.mirror_y, keep_aspect_ratio=options.keep_aspect_ratio, raster_w=options.raster_w, raster_h=options.raster_h, XDPI=options.xdpi, YDPI=options.ydpi, outputObject=outputObject)
