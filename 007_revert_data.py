#!/usr/bin/python
import os
import timeit
import subprocess
from subprocess import call
from subprocess import Popen, PIPE


pwd = "./"
gd = "Sources"

start = timeit.default_timer()
call("rm -rf ./data/004_revert_data.txt",shell=True);

file_out=open("./data/004_revert_data.txt" ,'a')


level0= int(subprocess.check_output("grep -e\", Level: 0\" ./data/004_revert_checking.txt| wc -l",shell=True))
level1= int(subprocess.check_output("grep -e\", Level: 1\" ./data/004_revert_checking.txt| wc -l",shell=True))
level2= int(subprocess.check_output("grep -e\", Level: 2\" ./data/004_revert_checking.txt| wc -l",shell=True))
level3= int(subprocess.check_output("grep -e\", Level: 3\" ./data/004_revert_checking.txt| wc -l",shell=True))
level4= int(subprocess.check_output("grep -e\", Level: 4\" ./data/004_revert_checking.txt| wc -l",shell=True))

print "No of total revert:" + str(level0+level1+level2+level3+level4)
print "No of revert level 0:" + str(level0)
print "No of revert level 1:" + str(level1)
print "No of revert level 2:" + str(level2)
print "No of revert level 3:" + str(level3)
print "No of revert level 4:" + str(level4)
file_out.write("No of total revert:" + str(level0+level1+level2+level3+level4))
file_out.write("\nNo of revert level 0:" + str(level0))
file_out.write("\nNo of revert level 1:" + str(level1))
file_out.write("\nNo of revert level 1:" + str(level2))
file_out.write("\nNo of revert level 1:" + str(level3))
file_out.write("\nNo of revert level 1:" + str(level4))

file_out.close()
stop = timeit.default_timer()
print "Running time: " + str(stop - start)
