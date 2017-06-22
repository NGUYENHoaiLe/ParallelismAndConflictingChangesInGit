#!/usr/bin/python
import os
import timeit
import subprocess
#call shell command from python code
from subprocess import call

start = timeit.default_timer()

rd_output= "./RD_output/"
name_list ={
"rails-B8W-V3.1",
"rails-B4W-V3.1",
"rails-B3W-V3.1",
"rails-B2W-V3.1",
"rails-B1W-V3.1",
"rails-A1W-V3.1",
"rails-A2W-V3.1",
"rails-A3W-V3.1",
"rails-A4W-V3.1",
"rails-A8W-V3.1",

"rails-B8W-V3.2",
"rails-B4W-V3.2",
"rails-B3W-V3.2",
"rails-B2W-V3.2",
"rails-B1W-V3.2",
"rails-A1W-V3.2",
"rails-A2W-V3.2",
"rails-A3W-V3.2",
"rails-A4W-V3.2",
"rails-A8W-V3.2",

"rails-B8W-V4.0",
"rails-B4W-V4.0",
"rails-B3W-V4.0",
"rails-B2W-V4.0",
"rails-B1W-V4.0",
"rails-A1W-V4.0",
"rails-A2W-V4.0",
"rails-A3W-V4.0",
"rails-A4W-V4.0",
"rails-A8W-V4.0",

"rails-B8W-V4.1",
"rails-B4W-V4.1",
"rails-B3W-V4.1",
"rails-B2W-V4.1",
"rails-B1W-V4.1",
"rails-A1W-V4.1",
"rails-A2W-V4.1",
"rails-A3W-V4.1",
"rails-A4W-V4.1",
"rails-A8W-V4.1",

"rails-B8W-V4.2",
"rails-B4W-V4.2",
"rails-B3W-V4.2",
"rails-B2W-V4.2",
"rails-B1W-V4.2",
"rails-A1W-V4.2",
"rails-A2W-V4.2",
"rails-A3W-V4.2",
"rails-A4W-V4.2",
"rails-A8W-V4.2"}

for name in name_list:
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


