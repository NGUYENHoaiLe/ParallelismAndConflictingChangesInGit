#!/usr/bin/python
import os
import timeit
import subprocess
from subprocess import call

pwd = "./"
gd = "Sources"
merge_output= "./output/"
data_output= "./data/"

print "\n######################## REVERT DETECTING ######################"
print "\n This program will create 4 workers which running in 4 different terminals."
print "\n Please waiting for all workers to finish his job then you can run the next script (005_...)"

#clean...
call("rm -rf ws1",shell=True);
call("rm -rf ws2",shell=True);
call("rm -rf ws3",shell=True);
call("rm -rf ws4",shell=True);
call("rm -rf "+data_output+"004_merge-children-parents.txt",shell=True);
call("rm -rf "+ data_output+"004_revert_checking.txt",shell=True);
# init...
call("git clone "+ gd + " ws1",shell=True);
call("git clone "+ gd + " ws2",shell=True);
call("git clone "+ gd + " ws3",shell=True);
call("git clone "+ gd + " ws4",shell=True);
cmdline = "cd "+gd +"; git log  --min-parents=2 --children | awk '/^commit|^Merge:/ {print}' >> ../data/004_merge-children-parents.txt"
call(cmdline,shell=True);

subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./401_revert.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./402_revert.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./403_revert.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./404_revert.sh'])

###################################################################333








