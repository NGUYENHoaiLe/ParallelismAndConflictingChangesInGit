#!/usr/bin/python
import os
import time
import timeit
import datetime
import subprocess
from subprocess import call
#from concurrent import futures
import itertools

#INPUT :  git projects folder named "Sources"
#OUTPUT:  data/001_commit_parents.txt  <== git log --min-parents=2 --pretty=format:"%H %P"
#         output/*  <==   merges output 

#path git directory
pwd = "./"
#git directory
gd = "Sources"
merge_output= "./output/"
data_output= "./data/"
WORKERS=4  #number of processes

#using 16 clones for 4 workers
#def run_multithreading(Executor):
#	with Executor(max_workers=WORKERS) as executor:
#        	{executor.submit(iterCommits, count,line,"ws"+str(count%16 +1)): (count,line) for count,line in ENUMS}
#run_multithreading(futures.ProcessPoolExecutor)


print "\n######################## REPLAY THE MERGES ######################"
print "\n This program will create 4 workers which running in 4 different terminals."
print "\n Please waiting for all workers to finish his job then you can run the next script (002_...)"
#clean...
call("rm -rf ws1",shell=True);
call("rm -rf ws2",shell=True);
call("rm -rf ws3",shell=True);
call("rm -rf ws4",shell=True);
call("rm -rf "+ merge_output,shell=True);
call("rm -rf "+ data_output,shell=True);
# init...
call("git clone "+ gd + " ws1",shell=True);
call("git clone "+ gd + " ws2",shell=True);
call("git clone "+ gd + " ws3",shell=True);
call("git clone "+ gd + " ws4",shell=True);
call("mkdir "+ merge_output,shell=True);
call("mkdir "+ data_output,shell=True);
call("cd "+ gd +";git log --min-parents=2 --pretty=format:\"%H %P\" >> ../data/001_commit_parents.txt", shell=True)

subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./101_replay.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./102_replay.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./103_replay.sh'])
subprocess.Popen(['gnome-terminal', '-e', 'bash --rcfile  ./104_replay.sh'])

#call("exit",shell=True);
#===============================================================================================
