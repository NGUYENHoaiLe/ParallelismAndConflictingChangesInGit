#!/usr/bin/python
import os
import timeit
import subprocess
from subprocess import call
from subprocess import Popen, PIPE

pwd = "./"
gd = "Sources"
adjlineoutput= "./potentialoutput/"
data_output= "./data/"
WORKERS=4  #number of processes

def console(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return (p.returncode, out, err)

def iterCommits (n, cmt, listcdg):
	list_parents= cmt.split(" ")
	cmd= "cd "+ listcdg +"; git checkout -b branch" +str(n) + " "+ str(list_parents[1])+ "; git merge "
	for x in list_parents[2::] :
		cmd=cmd + " " + str(x)
	output1= console(cmd)
	output2=output1[1]
	if output1[2] !=None:
		output2= output1[2]
	if output2.find("CONFLICT (content): ")!=-1 or output2.find("ERROR: content")!=-1:
		file_out=open(adjlineoutput + str(n) + ".txt",'w')
		file_out.write(cmd +"\n")
		file_out.write(output2)
		output = subprocess.check_output( "cd "+ listcdg +"; git checkout branch" +str(n)+ "; git difftool",shell=True)
		file_out.write(output)
		listdiff=output.split("\n")
		
		outputline=""
		diff_file=""
		begin_c1=-1
		end_c1=-1
		begin_com=-1
		end_com=-1
		begin_c2=-1
		end_c2=-1
		change_case=-1
		check=True
		for i in range(len(listdiff)):
			
			if listdiff[i].startswith("diff --cc"):
				diff_file= listdiff[i].split(" ")[2]
				if diff_file.endswith(".pdf") or diff_file.endswith(".html") or diff_file.startswith("source3/configure"): #do not process PDF files	
					check=False
				else:
					check=True
								
			elif check and listdiff[i].startswith("++<<<<<<<"):
				begin_c1=i+1
			elif check and listdiff[i].startswith("++|||||||"):
				end_c1=i-1	
				begin_com=i+1
			elif check and listdiff[i].startswith("++======="):
				end_com=i-1
				begin_c2=i+1
			elif check and listdiff[i].startswith("++>>>>>>>"):
				end_c2=i-1
				#########################################
				if end_com>begin_com and end_c1>begin_c1 and end_c2>begin_c2 and (begin_c1!=-1 and begin_com!=-1 and end_com !=-1):
					for cm in range(begin_com,end_com +1):
						if (begin_c2+cm-begin_com)>=len(listdiff) or (begin_c1+cm-begin_com)>end_c1:
							break
						if change_case==-1 :  #INIT CASE or line(i-1): V|V or line(i-1) X|X
							if listdiff[cm][2:] == 	listdiff[begin_c1+cm-begin_com][2:] :  #equal to c1  ...
								if listdiff[cm][2:] != listdiff[begin_c2+cm-begin_com][2:]: #... but not equal c2
									change_case=1
							elif listdiff[cm][2:] == listdiff[begin_c2+cm-begin_com][2:] : 	#not equal to c1 but equal to c2
									change_case=2
							else: # not equal to c1 neither c2 ==> changed both sides (normal conflict), not adjacent-line case
								outputline="\nNORMAL-CONFLICT\n"+str(list_parents[0]) +"\n"+ diff_file+"\n"+ listdiff[begin_c1+cm-begin_com][2:] +"\n"+ listdiff[begin_c2+cm-begin_com][2:]  +"\n"
								file_out.write(outputline)
								#change_case=-1
								#break
						
						#CASE_1 : line(i-1):  V||X
						elif change_case==1:
							if listdiff[cm][2:] != 	listdiff[begin_c1+cm-begin_com][2:] : 
								#       Change1 || Change2          #  V= not changed, X= changed  
								#line(i-1)  V   ||    X            (1) Normal-content conflict  
								#line( i ) [X]  || X(1)|V(2)       (2) Adjacent-line  conflict  
								if listdiff[cm][2:] != listdiff[begin_c2+cm-begin_com][2:]: #1
									outputline="\nNORMAL-CONFLICT\n"+str(list_parents[0]) +"\n"+ diff_file+"\n"+ listdiff[begin_c1+cm-begin_com][2:] +"\n"+ listdiff[begin_c2+cm-begin_com][2:]  +"\n"
									file_out.write(outputline)
									chang_case=-1
									#break
								else: #2 #elif listdiff[cm][2:] == listdiff[begin_c2+cm-begin_com][2:] and  listdiff[cm-1][2:] != listdiff[begin_c2+cm-begin_com -1][2:] :
									outputline="\nADJACENT-LINE\n"+str(list_parents[0]) +"\n"+ diff_file+"\n"+ listdiff[begin_c2+cm-begin_com-1][2:] +"\n"+ listdiff[begin_c1+cm-begin_com][2:]  +"\n"
									file_out.write(outputline)
									change_case=2
									#break 
							elif listdiff[cm][2:] == listdiff[begin_c2+cm-begin_com][2:]:
								change_case =-1
							#else: change_case =1
 
						#CASE_2 : line(i-1):  X|V			
						else: # change_case ==2  
							if listdiff[cm][2:] != 	listdiff[begin_c2+cm-begin_com][2:] : 	
								#           Change1  || Change2           
								#line(i-1)    X      ||    V         (1) Normal-content conflict  
								#line( i ) X(1)|V(2) ||   [X]        (2) Adjacent-line  conflict  
								if listdiff[cm][2:] != listdiff[begin_c1+cm-begin_com][2:]: #1
									outputline="\nNORMAL-CONFLICT\n"+str(list_parents[0]) +"\n"+ diff_file+"\n"+ listdiff[begin_c1+cm-begin_com][2:] +"\n"+ listdiff[begin_c2+cm-begin_com][2:]  +"\n"
									file_out.write(outputline)
									chang_case=-1
									#break
								else: #elif listdiff[cm][2:] == listdiff[begin_c1+cm-begin_com][2:] and  listdiff[cm-1][2:] != listdiff[begin_c1+cm-begin_com -1][2:] :
									outputline="\nADJACENT-LINE\n"+str(list_parents[0]) +"\n"+ diff_file+"\n"+ listdiff[begin_c1+cm-begin_com-1][2:] +"\n"+ listdiff[begin_c2+cm-begin_com][2:]  +"\n"
									file_out.write(outputline)
									change_case= 1
									#break 
							elif listdiff[cm][2:] == listdiff[begin_c1+cm-begin_com][2:]:	
								change_case= -11   
							#else: change_case = 2
					#end for
				#end if					
				#########################################
				begin_c1=-1
				end_c1=-1
				begin_com=-1
				end_com=-1
				begin_c2=-1
				end_c2=-1
				change_case=-1
			#end elif (detection of end_c2)
		#end for	
		file_out.close()
	call("cd "+ listcdg +"; git reset --hard HEAD", shell=True)
	return


print "\n######################## CONTINUES REPLAYING DIFF CONTENT ######################"
start = timeit.default_timer()
commit_parents = open(data_output+ "001_commit_parents.txt", 'r')
cmdline= "cd "+ gd +";git log --min-parents=2 --oneline | wc -l"
output = subprocess.check_output(cmdline,shell=True);
numOfMerges= int(output)
LIMIT1 = int(numOfMerges/WORKERS)
LIMIT2 = LIMIT1*2
LIMIT3 = LIMIT1*3
ENUMS1= list(enumerate(commit_parents))[:LIMIT1]

for count,line in ENUMS1:
	iterCommits(count,line,"ws1")

stop = timeit.default_timer()
print "\n>>>>> "+ str(LIMIT1) + " DIFF were replayed in: " + str(stop - start)

#clean...
call("rm -rf ws1",shell=True);

