#!/usr/bin/python
import os
import timeit
import subprocess
#call shell command from python code
from subprocess import call

start = timeit.default_timer()

rd_output= "./RD_output/"

name_list = { 
 "linux-B4W-V2.6.39"
,"linux-B2W-V2.6.39"
,"linux-B3W-V2.6.39"
,"linux-B1W-V2.6.39"
,"linux-A1W-V2.6.39"
,"linux-A2W-V2.6.39"
,"linux-A3W-V2.6.39"
,"linux-A4W-V2.6.39"

,"linux-B4W-V3.0"
,"linux-B3W-V3.0"
,"linux-B2W-V3.0"
,"linux-B1W-V3.0"
,"linux-A1W-V3.0"
,"linux-A2W-V3.0"
,"linux-A3W-V3.0"
,"linux-A4W-V3.0"

,"linux-B4W-V3.1"
,"linux-B3W-V3.1"
,"linux-B2W-V3.1"
,"linux-B1W-V3.1"
,"linux-A1W-V3.1"
,"linux-A2W-V3.1"
,"linux-A3W-V3.1"
,"linux-A4W-V3.1"

,"linux-B4W-V3.19"
,"linux-B3W-V3.19"
,"linux-B2W-V3.19"
,"linux-B1W-V3.19"
,"linux-A1W-V3.19"
,"linux-A2W-V3.19"
,"linux-A3W-V3.19"
,"linux-A4W-V3.19"

,"linux-B4W-V4.0"
,"linux-B3W-V4.0"
,"linux-B2W-V4.0"
,"linux-B1W-V4.0"
,"linux-A1W-V4.0"
,"linux-A2W-V4.0"
,"linux-A3W-V4.0"
,"linux-A4W-V4.0"

,"linux-B4W-V4.1"
,"linux-B3W-V4.1"
,"linux-B2W-V4.1"
,"linux-B1W-V4.1"
,"linux-A1W-V4.1"
,"linux-A2W-V4.1"
,"linux-A3W-V4.1"
,"linux-A4W-V4.1"}

for name in name_list:
	call("rm -r "+ rd_output+name ,shell=True)
	call("mkdir "+ rd_output+name,shell=True)
	octopus=""
	ocp = open("./"+name +".txt", 'r')
	for count, line in enumerate(ocp) :
		if line <> "" and line <> "\n" :
			command = "cp "+line.replace("\n","") +" " +rd_output+ name +"/" +line.split("/")[2] 
			#print command
			call(command,shell=True)

stop = timeit.default_timer()
print "Running time: " + str(stop - start)

