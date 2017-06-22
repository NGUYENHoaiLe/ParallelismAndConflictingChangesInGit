#!/usr/bin/python
import os
import timeit
import subprocess
from subprocess import call
from subprocess import Popen, PIPE


pwd = "./"
gd = "Sources"
cgd= "ws1adjacentline"
call("rm -rf "+ cgd,shell=True);
call("git clone "+ gd + " "+ cgd,shell=True);

def console(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return (p.returncode, out, err)

def isContains(listline,line1,line2):
	index1=-1
	index2=-1
	for l in range(len(listline)):
		if listline[l]==line1:
			change1=True
			index1=l
			if index2!=-1 and abs(index1-index2) <=2 :
				return 3
		elif listline[l] == line2: 
			change2=True
			index2=l
			if index1!=-1 and abs(index1-index2) <=2 :
				return 3
	if index1!=-1 and index2!=-1:	
		return abs(index1-index2)
	elif index1!=-1:
		return 1
	elif index2!=-1:
		return 2
	return 0
#functions
def iterFile (f):
	fileAdLn=open(f,'r').readlines()
	for n in range(len(fileAdLn)) :
		if fileAdLn[n] =="ADJACENT-LINE\n":
			cmd= "cd "+ cgd +"; git checkout -b check"+f   + str(n) + " " + fileAdLn[n+1]
			call(cmd,shell=True)
			try:
				file_temp= open(cgd +"/"+fileAdLn[n+2].replace("\n",""),'r').readlines()
				print fileAdLn[n+1].replace("\n","")," ===============>>> ",fileAdLn[n+2].replace("\n","")	
				file_out.write("\n"+fileAdLn[n+1].replace("\n","")+" ===============>>> "+fileAdLn[n+2].replace("\n",""))
				if fileAdLn[n+3] =="" or fileAdLn[n+4]=="":
					print "ADJACENT-LINE note: 1 side is a empty line"
					file_out.write("\nADJACENT-LINE note: 1 side is a empty line"	)
				recode= isContains(file_temp , fileAdLn[n+3],fileAdLn[n+4])
				if recode==1:
					print "ADJACENT-LINE resolution: applied CHANGE_1"
					file_out.write("\nADJACENT-LINE resolution: applied CHANGE_1")
				elif recode==2:
					print "ADJACENT-LINE resolution: applied CHANGE_2"
					file_out.write("\nADJACENT-LINE resolution: applied CHANGE_2")
				elif recode==3:
	 				print "ADJACENT-LINE resolution: applied CHANGE_BOTH"
	 				file_out.write("\nADJACENT-LINE resolution: applied CHANGE_BOTH")
				elif recode==0:
					print "ADJACENT-LINE resolution: NOT APPLIED"	
					file_out.write("\nADJACENT-LINE resolution: NOT APPLIED")	
				else:
					print "ADJACENT-LINE resolution: applied CHANGE_1SIDE",recode	
					file_out.write("\nADJACENT-LINE resolution: applied CHANGE_1SIDE"+str(recode))	
			except IOError as (errno, strerror):
			    print "I/O error({0}): {1}".format(errno, strerror)
			    file_out.write("\n"+"I/O error({0}): {1}".format(errno, strerror))
		elif fileAdLn[n] =="NORMAL-CONFLICT\n":
			cmd= "cd "+ cgd +"; git checkout -b check"+f   + str(n) + " " + fileAdLn[n+1]
			call(cmd,shell=True)
			try:
				file_temp= open(cgd +"/"+fileAdLn[n+2].replace("\n",""),'r').readlines()
				print fileAdLn[n+1].replace("\n","")," ===============>>> ",fileAdLn[n+2].replace("\n","")	
				file_out.write("\n"+ fileAdLn[n+1].replace("\n","")+" ===============>>> "+fileAdLn[n+2].replace("\n",""))	
				if fileAdLn[n+3] =="" or fileAdLn[n+4]=="":
					print "NORMAL-CONFLICT note: 1 side is a empty line"
					file_out.write("\nNORMAL-CONFLICT note: 1 side is a empty line"	)	
				recode= isContains(file_temp , fileAdLn[n+3],fileAdLn[n+4])
				if recode==1:
					print "NORMAL-CONFLICT resolution: applied CHANGE_1"
					file_out.write("\nNORMAL-CONFLICT resolution: applied CHANGE_1")
				elif recode==2:
					print "NORMAL-CONFLICT resolution: applied CHANGE_2"
					file_out.write("\nNORMAL-CONFLICT resolution: applied CHANGE_2")
				elif recode==3:
	 				print "NORMAL-CONFLICT resolution: applied CHANGE_BOTH"
	 				file_out.write("\nNORMAL-CONFLICT resolution: applied CHANGE_BOTH")
				elif recode==0:
					print "NORMAL-CONFLICT resolution: NOT APPLIED"	
					file_out.write("\nNORMAL-CONFLICT resolution: NOT APPLIED")	
				else:
					print "NORMAL-CONFLICT resolution: applied CHANGE_1SIDE",recode		
					file_out.write("\nNORMAL-CONFLICT resolution: applied CHANGE_1SIDE" +str(recode))		
			except IOError as (errno, strerror):
			    print "I/O error({0}): {1}".format(errno, strerror)	
			    file_out.write("\n"+"I/O error({0}): {1}".format(errno, strerror)	)
	return



start = timeit.default_timer()
call("rm -rf ./data/006_adjacent_line_conflict.txt",shell=True);
call("rm -rf ./data/006_adjacent_line_data.txt",shell=True);
output = subprocess.check_output( "grep -e'ADJACENT-LINE' -e'NORMAL-CONFLICT' ./adjlineoutput/*.txt | cut -d\":\" -f1 | sort -u",shell=True)
listAdLnFile=output.split("\n")

file_out=open("./data/006_adjacent_line_conflict.txt" ,'a')
for f in listAdLnFile:
	if f !="":
		print f	
		iterFile(f)
call("rm -rf "+ cgd,shell=True);
file_out.close()

normal_change1= int(subprocess.check_output("grep -e\"NORMAL-CONFLICT resolution: applied CHANGE_1\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
normal_change2= int(subprocess.check_output("grep -e\"NORMAL-CONFLICT resolution: applied CHANGE_2\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
normal_change1side= int(subprocess.check_output("grep -e\"NORMAL-CONFLICT resolution: applied CHANGE_1SIDE\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
normal_change_both= int(subprocess.check_output("grep -e\"NORMAL-CONFLICT resolution: applied CHANGE_BOTH\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
normal_notapplied= int(subprocess.check_output("grep -e\"NORMAL-CONFLICT resolution: NOT APPLIED\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
normal_IOerror= int(subprocess.check_output("grep -e\"I/O error(2): No such file or directory\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
adjline_change1= int(subprocess.check_output("grep -e\"ADJACENT-LINE resolution: applied CHANGE_1\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
adjline_change2= int(subprocess.check_output("grep -e\"ADJACENT-LINE resolution: applied CHANGE_2\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
adjline_change1side= int(subprocess.check_output("grep -e\"ADJACENT-LINE resolution: applied CHANGE_1SIDE\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
adjline_change_both= int(subprocess.check_output("grep -e\"ADJACENT-LINE resolution: applied CHANGE_BOTH\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))
adjline_notapplied= int(subprocess.check_output("grep -e\"ADJACENT-LINE resolution: NOT APPLIED\" ./data/006_adjacent_line_conflict.txt| wc -l",shell=True))

print "\n############################################"
print "\nNo of total ADJACENT-LINE conflicts:" + str(adjline_change_both+adjline_change1+adjline_change2+adjline_notapplied)
print "\nNo of ADJACENT-LINE applied both sides:" + str(adjline_change_both)
print "\nNo of ADJACENT-LINE  applied 1 sides:"+ str(adjline_change1+adjline_change2)
print "\nNo of ADJACENT-LINE  other cases:"+ str(adjline_notapplied)
print "\nNo of total NORMAL-CONFLICT conflicts:"+ str(normal_change_both+normal_change1+normal_change2+ normal_notapplied+normal_IOerror)
print "\nNo of NORMAL-CONFLICT  applied both sides:"+ str(normal_change_both)
print "\nNo of NORMAL-CONFLICT  applied 1 sides:"+ str(normal_change1+normal_change2 )
print "\nNo of NORMAL-LINE  other cases:"+ str(normal_notapplied+normal_IOerror)

file_out=open("./data/006_adjacent_line_data.txt" ,'a')
file_out.write("No of total ADJACENT-LINE conflicts:" + str(adjline_change_both+adjline_change1+adjline_change2+adjline_notapplied))
file_out.write("\nNo of ADJACENT-LINE applied both sides:" + str(adjline_change_both))
file_out.write("\nNo of ADJACENT-LINE  applied 1 sides:"+ str(adjline_change1+adjline_change2))
file_out.write("\nNo of ADJACENT-LINE  other cases:"+ str(adjline_notapplied))
file_out.write("\nNo of total NORMAL-CONFLICT conflicts:"+ str(normal_change_both+normal_change1+normal_change2+ normal_notapplied+normal_IOerror))
file_out.write("\nNo of NORMAL-CONFLICT  applied both sides:"+ str(normal_change_both))
file_out.write("\nNo of NORMAL-CONFLICT  applied 1 sides:"+ str(normal_change1+normal_change2))
file_out.write("\nNo of NORMAL-LINE  other cases:"+ str(normal_notapplied+normal_IOerror))
file_out.close()

stop = timeit.default_timer()
print "Running time: " + str(stop - start)
