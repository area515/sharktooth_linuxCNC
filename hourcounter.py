#!/usr/bin/python
import hal,time
import datetime
import os
import pickle

h = hal.component("hourcounter")
h.newpin("running", hal.HAL_BIT, hal.HAL_IN)
h.newpin('running_ack', hal.HAL_BIT, hal.HAL_OUT)
h.newpin("total_day", hal.HAL_U32, hal.HAL_OUT)
h.newpin("total_hour", hal.HAL_U32, hal.HAL_OUT)
h.newpin("total_minutes", hal.HAL_U32, hal.HAL_OUT)
h.newpin("total_seconds", hal.HAL_U32, hal.HAL_OUT)
h.newpin('counter', hal.HAL_U32, hal.HAL_OUT)

LASER_TIME_FILENAME = 'LaserTimeCount'

def logTimeIncrement(totalTime, startTime):
	endTime = datetime.datetime.now()
	delta = endTime - startTime
	totalTime += delta
	with open(LASER_TIME_FILENAME, 'w') as timeFile:
		pickle.dump(totalTime, timeFile)
	return totalTime, endTime

if os.path.exists(LASER_TIME_FILENAME):
	with open(LASER_TIME_FILENAME, 'r') as timeFile:
		totalTime = pickle.load(timeFile)
else:
	totalTime = datetime.timedelta()
	

h.ready()

count = 0
isRunning = False
try:
	while 1:
		count += 1
		h['counter'] = count
		time.sleep(1)
		h['running_ack'] = h['running']
		if h['running'] and not isRunning:
			startTime = datetime.datetime.now()
			isRunning = True
		if not h['running'] and isRunning:
			isRunning = False
		if isRunning:
			totalTime, startTime = logTimeIncrement(totalTime, startTime)
		h['total_day'] = totalTime.days
		h['total_hour'] = totalTime.seconds / (60*60)
		h['total_minutes'] = (totalTime.seconds / 60) % 60
		h['total_seconds'] = totalTime.seconds % 60
		
except KeyboardInterrupt:
	if isRunning:
		logTimeIncrement(totalTime, startTime)
	
	raise SystemExit


