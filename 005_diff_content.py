#!/usr/bin/python
import os
import subprocess
from subprocess import call
from subprocess import Popen, PIPE

#INPUT :  git projects folder named "Sources", data/001_commit_parents.txt
#OUTPUT:  adjlineoutput/*.txt
pwd = "./"
gd = "Sources"
adjlineoutput= "./adjlineoutput/"
WORKERS=4  #number of processes

print "\n######################## REPLAY DIFF CONTENT ######################"
print "\n This program will create 4 workers which running in 4 different terminals."
print "\n Please waiting for all workers to finish his job then you can run the next script (006_...)"
#clean...
call("rm -rf ws1",shell=True);
call("rm -rf ws2",shell=True);
call("rm -rf ws3",shell=True);
call("rm -rf ws4",shell=True);
call("rm -rf "+ adjlineoutput,shell=True);
# init...
call("git clone "+ gd + " ws1",shell=True);
call("git clone "+ gd + " ws2",shell=True);
call("git clone "+ gd + " ws3",shell=True);
call("git clone "+ gd + " ws4",shell=True);
call("mkdir "+ adjlineoutput,shell=True);

subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./501_diff.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./502_diff.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./503_diff.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./504_diff.sh'])
