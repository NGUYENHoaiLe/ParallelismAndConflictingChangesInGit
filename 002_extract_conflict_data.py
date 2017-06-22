#!/usr/bin/python
import os
import timeit
import subprocess
from subprocess import call

#PRECONDITION: 001_replay_merges.py has been run
#OUTPUT:  002_extract_conflicts_data.txt


#path git directory
pwd = "./"
#git directory
gd = "Sources"
merge_output= "./output/"
data_output= "./data/"
try:
	call("mkdir "+data_output,shell=True)
except:
	pass

cmdline= "cd "+ gd +";git log --min-parents=2 --oneline | wc -l"
output = subprocess.check_output(cmdline,shell=True);
numOfMerges= int(output)

print "\n######################## EXTRACTING DATA ########################"
print "(Data is written to 002_extract_conflicts_data.txt)"
call("rm -rf "+ data_output+"002_extract_conflicts_data.txt",shell=True);
file_out=open(data_output+"002_extract_conflicts_data.txt",'w')

#print  "No of AUTHOR EMAILs: + 1 "
#cmdline= "cd "+ gd +";git log --pretty=format:\"%ae\" | sort -u | wc -l"
#call(cmdline,shell=True);
#print  "No of EXISTING files, including deleted files that are not committed : "
#cmdline= "cd "+ gd +";git ls-tree -r master | wc -l"
#call(cmdline,shell=True);

cmdline= "cd "+ gd +";git log --pretty=format:\"%an\" | sort -u | wc -l"
_author_name= int(subprocess.check_output(cmdline,shell=True)) -1;#one empty line
cmdline= "cd "+ gd +";git ls-files | wc -l"  
_existing_files= int(subprocess.check_output(cmdline,shell=True));
cmdline= "cd "+ gd +";git log --pretty=format: --name-status | cut -f2- | sort -u |wc -l"
_created_files= int(subprocess.check_output(cmdline,shell=True))-1;#one empty line
cmdline= "cd "+ gd +";git log --min-parents=2 --oneline | wc -l"
_merges= int(subprocess.check_output(cmdline,shell=True));
cmdline= "cd "+ gd +";git log --min-parents=3 --oneline | wc -l"
_octopus_merges= int(subprocess.check_output(cmdline,shell=True));
_simple_merges= _merges-_octopus_merges

#conflict data
cmdline= "grep -e \"Automatic merge failed\" -e\"Merge with strategy octopus failed\" ./output/*.txt |cut -d':' -f1|sort -u| wc -l"
_automerge_failed =int(subprocess.check_output(cmdline,shell=True));
cmdline= "grep -e \"ERROR: content\" -e \"Not handling case\" ./output/*.txt|cut -d':' -f1|sort -u|wc -l"
_automerge_failed_octopus =int(subprocess.check_output(cmdline,shell=True));		
_automerge_failed_simple = _automerge_failed - _automerge_failed_octopus

cmdline= "grep -e \"Auto-merging\" ./output/*.txt | cut -d':' -f2 | sort -u | wc -l"
_automerge_concurrent_files =int(subprocess.check_output(cmdline,shell=True));

cmdline="grep -e\"CONFLICT (\" ./output/*.txt |  cut -d':' -f3 |sort -u |wc -l"
_file_with_conflits_simple =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"ERROR: content\" -e \"Not handling case\" ./output/*.txt | cut -d':' -f3|sort -u| wc -l"
_file_with_conflits_octopus =int(subprocess.check_output(cmdline,shell=True));

cmdline="grep -e\"CONFLICT (\" ./output/*.txt | wc -l"
_conflicts_simple =int(subprocess.check_output(cmdline,shell=True));
cmdline= "grep -e \"ERROR: content\" -e \"Not handling case\" ./output/*.txt|wc -l"
_conflicts_octopus =int(subprocess.check_output(cmdline,shell=True));

#typesConflict
# simple conflict
cmdline="grep -e \"CONFLICT (content)\" ./output/*.txt | wc -l"
_cflsimple_content =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (cowarning: \" ./output/*.txt | wc -l"
_cflsimple_cowarning_content =int(subprocess.check_output(cmdline,shell=True));
_cflsimple_content=_cflsimple_content+_cflsimple_cowarning_content
cmdline="grep -e \"CONFLICT (modify/delete)\" ./output/*.txt | wc -l"
_cflsimple_modify_delete =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/modify)\" ./output/*.txt | wc -l"
_cflsimple_rename_modify =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/delete)\" ./output/*.txt | wc -l"
_cflsimple_rename_delete =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/rename)\" ./output/*.txt | wc -l"
_cflsimple_rename_rename =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/add)\" ./output/*.txt | wc -l"
_cflsimple_rename_add =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (add/add)\" ./output/*.txt | wc -l"
_cflsimple_add_add =int(subprocess.check_output(cmdline,shell=True));

#octopus
cmdline="grep -e \"ERROR: content\" ./output/*.txt | wc -l"
_cfloctopus_content =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"Not handling case\" ./output/*.txt | wc -l"
_clfoctopus_update_remove =int(subprocess.check_output(cmdline,shell=True));

#Simple resolutions (roll back)
cmdline ="grep -e\"CONFLICT (\" -e \"ERROR: content\"  -e \"Not handling case\" -e\"simpleResolution=True\" ./output/*.txt | cut -d' ' -f1 | sort -u | cut -d':' -f1| uniq -c |grep -e\"2 \"|wc -l"
_simple_resolution =int(subprocess.check_output(cmdline,shell=True));

print "No of Author names:" +str(_author_name)
print "No of Existing files:" + str(_existing_files)
print "No of Created files:" +str(_created_files)
print  "No of Concurrent modified files:" + str(_automerge_concurrent_files)
print "No of Merges:" +str(_merges)
print "No of merges resulted in conflicts:" + str(_automerge_failed)
print "No of Simple merges:" +str(_simple_merges)
print "No of Octopus merges:" +str(_octopus_merges)
print "No of Simple merges resulted in conflict:" +str(_automerge_failed_simple)
print "No of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus)
print "No of Files with conflicts in Simple merges:" +str(_file_with_conflits_simple)
print "No of Files with conflicts in Octopus merges: " +str(_file_with_conflits_octopus)
print "No of Conflicts in Simple merges: "  +str(_conflicts_simple)
print "No of Conflicts in Octopus merges:" +str(_conflicts_octopus)
print "CONFLICT (content):"+str(_cflsimple_content)
print "CONFLICT (modify/delete):"+str(_cflsimple_modify_delete)
print "CONFLICT (rename/modify):"+str(_cflsimple_rename_modify)
print "CONFLICT (rename/delete):"+str(_cflsimple_rename_delete)
print "CONFLICT (rename/rename):"+str(_cflsimple_rename_rename)
print "CONFLICT (rename/add):"+str(_cflsimple_rename_add)
print "CONFLICT (add/add):"+str(_cflsimple_add_add)
print "Octopus-content:"+str(_cfloctopus_content) # ERROR: content
print "Octopus update/remove:"+str(_clfoctopus_update_remove)  # Not handling case
print "No of Simple resolution:"+str(_simple_resolution) 

file_out.write( "No of Author names:" +str(_author_name))
file_out.write( "\nNo of Existing files:" + str(_existing_files))
file_out.write( "\nNo of Created files:" +str(_created_files))
file_out.write( "\nNo of Concurrent modified files:" + str(_automerge_concurrent_files))
file_out.write( "\nNo of Merges:" +str(_merges))
file_out.write( "\nNo of merges resulted in conflicts:" + str(_automerge_failed))
file_out.write( "\nNo of Simple merges:" +str(_simple_merges))
file_out.write( "\nNo of Octopus merges:" +str(_octopus_merges))
file_out.write( "\nNo of Simple merges resulted in conflict:" +str(_automerge_failed_simple))
file_out.write( "\nNo of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus))
file_out.write( "\nNo of Files with conflicts in Simple merges:" +str(_file_with_conflits_simple))
file_out.write( "\nNo of Files with conflicts in Octopus merges: " +str(_file_with_conflits_octopus))
file_out.write( "\nNo of Conflicts in Simple merges: "  +str(_conflicts_simple))
file_out.write( "\nNo of Conflicts in Octopus merges:" +str(_conflicts_octopus))
file_out.write( "\nCONFLICT (content):"+str(_cflsimple_content))
file_out.write( "\nCONFLICT (modify/delete):"+str(_cflsimple_modify_delete))
file_out.write( "\nCONFLICT (rename/modify):"+str(_cflsimple_rename_modify))
file_out.write( "\nCONFLICT (rename/delete):"+str(_cflsimple_rename_delete))
file_out.write( "\nCONFLICT (rename/rename):"+str(_cflsimple_rename_rename))
file_out.write( "\nCONFLICT (rename/add):"+str(_cflsimple_rename_add))
file_out.write( "\nCONFLICT (add/add):"+str(_cflsimple_add_add))
file_out.write( "\nOctopus-content:"+str(_cfloctopus_content)) # ERROR: content
file_out.write( "\nOctopus update/remove:"+str(_clfoctopus_update_remove) ) # Not handling case
file_out.write( "\nNo of Simple resolution:"+str(_simple_resolution))
#close file_out
file_out.close()
#=================================================================================	



