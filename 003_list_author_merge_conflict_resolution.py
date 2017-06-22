#!/usr/bin/python
import os
import subprocess
from subprocess import call


author_commit= dict()
#generating authors.txt: 
data_output= "./data/"
call("rm -rf authors.txt",shell=True)
call("rm -rf "+data_output+"003_list_author_merge_conflict_resolution.txt",shell=True)
call("grep -e \"committer \" ./output*/*.txt >>authors.txt",shell=True)
authors = open("./authors.txt", 'r')

for count, line in enumerate(authors) :
	au=(line.split(' ')[1] + " " +line.split(' ')[2]).split('<')[0]
	if author_commit.has_key(au):
		author_commit[au] = author_commit[au] +" " + line.split(':')[0]
	else:
		author_commit[au] = line.split(':')[0]

amcsr_output= open(data_output+"003_list_author_merge_conflict_resolution.txt",'w')
amcsr_output.write("Author"+", NoMerges"+", NoMergesResultedInConflict"+", NoConflicts" + ", NoSimpleResolutions"+"\n")
print "No-Author-That-Had-Merges:" + str(len(author_commit))
print "Author"+", NoMerges"+", NoMergesResultedInConflict"+", NoConflicts" + ", NoSimpleResolutions"

for k,v in author_commit.items():
	noMerges= len(v.split(' '))
	if noMerges >10000:
		call("rm -rf temp"+str(noMerges),shell=True)
		call("mkdir temp"+str(noMerges),shell=True)	
		for f in v.split(' '):
			call("cp "+ f + " temp"+str(noMerges),shell=True)
		noCflMerges = int(subprocess.check_output("grep -e \"Automatic merge failed\" -e\"Merge with strategy octopus failed\" ./temp"+str(noMerges) + "/*.txt | wc -l",shell=True));
		noCfls =  int(subprocess.check_output("grep -e \"CONFLICT (\" -e \"ERROR: content\" -e \"Not handling case\"  ./temp"+str(noMerges) + "/*.txt | wc -l",shell=True));
		noSpRes = int(subprocess.check_output("grep -e \"CONFLICT (\" -e \"ERROR: content\" -e \"Not handling case\" -e\"simpleResolution=True\" ./temp"+str(noMerges) + "/*.txt  | cut -d' ' -f1 | sort -u | cut -d':' -f1| uniq -c |grep -e\"2 \"|wc -l",shell=True));
		call("rm -rf temp"+str(noMerges),shell=True)
		amcsr_output.write(str(k)+", "+str(noMerges)+", "+str(noCflMerges)+","+ str(noCfls) + ","+str(noSpRes)+"\n")
		print str(k)+", "+str(noMerges)+", "+ str(noCflMerges)+", "+str(noCfls)+", "+str(noSpRes)
		
	else:
		noCflMerges = int(subprocess.check_output("grep -e \"Automatic merge failed\"  -e\"Merge with strategy octopus failed\" "+ str(v) + " | wc -l",shell=True));	
		noCfls =  int(subprocess.check_output("grep -e\"CONFLICT (\" -e \"ERROR: content\" -e \"Not handling case\" "+ str(v) + " | wc -l",shell=True));
		noSpRes = int(subprocess.check_output("grep -e\"CONFLICT (\" -e \"ERROR: content\" -e \"Not handling case\" -e\"simpleResolution=True\" "+ str(v) + " | cut -d' ' -f1 | sort -u | cut -d':' -f1| uniq -c |grep -e\"2 \"|wc -l",shell=True));
		amcsr_output.write(str(k)+", "+str(noMerges)+", "+ str(noCflMerges)+", "+str(noCfls)+", "+str(noSpRes)+"\n")
		print str(k)+", "+str(noMerges)+", "+ str(noCflMerges)+", "+str(noCfls)+", "+str(noSpRes)

authors.close()
amcsr_output.close()
call("rm -rf authors.txt",shell=True)
	
