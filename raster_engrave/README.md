To develop on this you need to do the following:
```
sudo apt-get isntall python-pip
sudo pip install sniffer
sudo apt-get isntall python-qt4 python-qt4-dev qt4-designer pyqt4-dev-tools
```

Qt Designer can be used to modify the GUI
To regenerate the python file from the ui file, run:
```
pyuic4 -o mainDialogUI.py mainDialog.ui
```
