#!/usr/bin/python
import os
import timeit
import subprocess
#call shell command from python code
from subprocess import call

start = timeit.default_timer()

rd_output= "./RD_output/"

name_list = {"samba-B8W-V3.2"
,"samba-B4W-V3.2"
,"samba-B3W-V3.2"
,"samba-B2W-V3.2"
,"samba-B1W-V3.2"
,"samba-A1W-V3.2"
,"samba-A2W-V3.2"
,"samba-A3W-V3.2"
,"samba-A4W-V3.2"
,"samba-A8W-V3.2"

,"samba-B8W-V3.3"
,"samba-B4W-V3.3"
,"samba-B3W-V3.3"
,"samba-B2W-V3.3"
,"samba-B1W-V3.3"
,"samba-A1W-V3.3"
,"samba-A2W-V3.3"
,"samba-A3W-V3.3"
,"samba-A4W-V3.3"
,"samba-A8W-V3.3"

,"samba-B8W-V3.6"
,"samba-B4W-V3.6"
,"samba-B3W-V3.6"
,"samba-B2W-V3.6"
,"samba-B1W-V3.6"
,"samba-A1W-V3.6"
,"samba-A2W-V3.6"
,"samba-A3W-V3.6"
,"samba-A4W-V3.6"
,"samba-A8W-V3.6"}
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

