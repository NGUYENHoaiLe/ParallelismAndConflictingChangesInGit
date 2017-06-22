#!/usr/bin/python
import os
import timeit
import subprocess
#call shell command from python code
from subprocess import call

start = timeit.default_timer()

rd_output= "./RD_output/"

#name ="iki-B8W-V3.0"
#name ="iki-B4W-V3.0"
#name ="iki-B3W-V3.0"
#name ="iki-B2W-V3.0"
#name ="iki-B1W-V3.0"
#name ="iki-A1W-V3.0"
#name ="iki-A2W-V3.0"
name ="iki-A3W-V3.0"
#name ="iki-A4W-V3.0"
#name ="iki-A8W-V3.0"


call("rm -r "+ rd_output+name ,shell=True)
call("mkdir "+ rd_output+name,shell=True)
ocp = open("./"+name +".txt", 'r')
for count, line in enumerate(ocp) :
	if line <> "" and line <> "\n" :
		command = "cp "+line.replace("\n","") +" " +rd_output+ name +"/" +line.split("/")[2] 
		#print command
		call(command,shell=True)

stop = timeit.default_timer()
print "Running time: " + str(stop - start)
