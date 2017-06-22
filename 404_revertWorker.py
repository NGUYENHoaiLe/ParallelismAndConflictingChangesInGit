#!/usr/bin/python
import os
import timeit
import subprocess
from subprocess import call
from concurrent import futures
import datetime
import itertools
import time

#INPUT :  Called by 004_revert_detector.py
#OUTPUT:   ./data/revert_checking.txt    

pwd = "./"
gd = "Sources"
data_output= "./data/"
max_level=4
WORKERS=4  #number of processes
reverted= {}
children = {}
parents  = {}
tree_child = {}
curr_commit = {}


#functions
def console(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return (p.returncode, out, err)

def revertingCheck(children, parents,level):
	for k,v  in children.items() : 
		for kp,vp in parents.items() : 
			if v == vp:
				reverted[k.replace("\n","")] =str(kp).replace("\n","") + ", Level: " + str(level)
				return True
	return False	

def iterCommits (n, cmt, listcgd):
	global children, parents, reverted, tree_child, curr_commit
 	list_element = cmt.split(" ") 
	
	if list_element[0] == "commit" :
		children.clear()
		curr_commit.clear()
		output = subprocess.check_output("cd "+ listcgd +"; git cat-file -p " + str(list_element[1]),shell=True);
		curr_commit[list_element[1]]=output.split("\n")[0]

		for i  in range(2,len(list_element)) :
			output = subprocess.check_output("cd "+ listcgd +"; git cat-file -p " + str(list_element[i]),shell=True);
			children[list_element[i]]= output.split("\n")[0]
			
        elif list_element[0]== "Merge:" :
		parents.clear()
		for i  in range(1,len(list_element)):
			 output = subprocess.check_output("cd "+ listcgd +"; git cat-file -p " + str(list_element[i]),shell=True);
			 parents[list_element[i]]= output.split("\n")[0]
		
		# Level 0: reverting the merge commit 	
		level=0	
 		is_reverted=revertingCheck(curr_commit, parents,level)
		
		# Level 1->... : reverting after the merge commit
		if is_reverted ==False :
			level= level + 1
			is_reverted=revertingCheck(children, parents,level)	
		        while is_reverted ==False and level <max_level:
				level=level+1
				for k,v  in children.items() : 
					output = subprocess.check_output("cd "+ listcgd +"; git log --children | grep ^\"commit " + str(k).replace("\n","") +"\"",shell=True); 
					next_elements= output.split(" ")
					tree_child.clear()		
					for i  in range(2,len(next_elements)) :
						output = subprocess.check_output("cd "+ listcgd +"; git cat-file -p " + str(next_elements[i]),shell=True);
						tree_child[next_elements[i]]= output.split("\n")[0]	
					is_reverted=revertingCheck(tree_child, parents,level)
					if is_reverted == True:
						break
				
				children=dict(tree_child)
	return


print "\n######################## CONTINUES REVERT CHECKING ######################"

start = timeit.default_timer()
commit_parents = open(data_output+"004_merge-children-parents.txt", 'r')
cmdline= "cd "+ gd +";git log --min-parents=2 --oneline | wc -l"
output = subprocess.check_output(cmdline,shell=True);
numOfMerges= int(output)
LIMIT1 = int(numOfMerges/WORKERS) *2
LIMIT2 = LIMIT1*2
LIMIT3 = LIMIT1*3
ENUMS4= list(enumerate(commit_parents))[LIMIT3:]

for count,line in ENUMS4:
	print count,line
	iterCommits(count,line,"ws4")

print "######################## REVERT DETECTED ######################"
file_out=open(data_output+"004_revert_checking.txt",'a')
for k,v  in reverted.items() : 
	print  k + " was reverted to " + v
	file_out.write(k + " was reverted to " + v+"\n")
file_out.close()
stop = timeit.default_timer()
print "\nRevert checking in: " + str(stop - start)


#clean...
call("rm -rf ws4",shell=True);
#===============================================================================================
