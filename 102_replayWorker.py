#!/usr/bin/python
import os
import timeit
import subprocess
from subprocess import call
from concurrent import futures
import datetime
import itertools
import time

#INPUT :  Called by 001_replay_merges.py
#OUTPUT:  output 

#path git directory
pwd = "./"
#git directory
gd = "Sources"
merge_output= "./output/"
data_output= "./data/"
WORKERS=4  #number of processes

#functions
def console(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return (p.returncode, out, err)

def iterCommits (n, cmt,listcgd):
	file_out=open(merge_output + str(n) + ".txt",'w')
	list_parents= cmt.split(" ")
	cmd= "cd "+ listcgd +"; git checkout -b branch" +str(n) + " "+ str(list_parents[1])+ "; git merge "
	for x in list_parents[2::] :
		cmd=cmd + " " + str(x)

	file_out.write("\n" +cmt +"\n")
	file_out.write(cmd +"\n")
	output = subprocess.check_output("cd "+ listcgd +"; git cat-file -p " + str(list_parents[0]),shell=True);
	tree=output.split("\n")[0]
	file_out.write(tree +"\n")
	file_out.write(output +"\n")
	file_out.write("simpleResolution=")
	for x in list_parents[1::] :
		output1 = subprocess.check_output("cd "+ listcgd +"; git cat-file -p " + str(x),shell=True);
		tree1=output1.split("\n")[0]
		if tree==tree1:
			file_out.write("True")
			break
	
	
	call(cmd,shell=True, stdout=file_out,stderr=file_out)
	file_out.close()
	call("cd "+ listcgd +"; git reset --hard HEAD", shell=True)
	return

print "\n######################## CONTINUES REPLAYING THE MERGES ######################"
start = timeit.default_timer()
commit_parents = open(data_output+ "001_commit_parents.txt", 'r')
cmdline= "cd "+ gd +";git log --min-parents=2 --oneline | wc -l"
output = subprocess.check_output(cmdline,shell=True);
numOfMerges= int(output)
LIMIT1 = int(numOfMerges/WORKERS)
LIMIT2 = LIMIT1*2
LIMIT3 = LIMIT1*3
ENUMS2= list(enumerate(commit_parents))[LIMIT1:LIMIT2]
for count,line in ENUMS2:
	iterCommits(count,line,"ws2")

stop = timeit.default_timer()
print "\n>>>>> "+ str(LIMIT2-LIMIT1) + " merges were replayed in: " + str(stop - start)
#clean...
call("rm -rf ws2",shell=True);
#===============================================================================================
