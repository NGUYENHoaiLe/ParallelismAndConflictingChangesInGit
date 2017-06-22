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

rd_output= "./RD_output/"
merge_output= ""
data_output= "./RD_data/"
"""
try:
	call("mkdir "+data_output,shell=True)
except:
	pass
"""
cmdline= "cd "+ gd +";git log --min-parents=2 --oneline | wc -l"
output = subprocess.check_output(cmdline,shell=True);
numOfMerges= int(output)

print "\n######################## EXTRACTING DATA ########################"
#print "(Data is written to Rd_extract_conflicts_data.txt)"


#V3.0, _day ="2008-12-31"
_day ="2008-12-31"

#_before ="2008-12-24"; _name="iki-B1W-V3.0";
#_before ="2008-12-17"; _name="iki-B2W-V3.0";
#_before = "2008-12-10"; _name="iki-B3W-V3.0";
#_before ="2008-12-03"; _name="iki-B4W-V3.0";
#_before ="2008-11-05"; _name="iki-B8W-V3.0";

#_after ="2009-01-07"; _name="iki-A1W-V3.0";
#_after ="2009-01-14"; _name="iki-A2W-V3.0";
_after ="2009-01-21"; _name="iki-A3W-V3.0";
#_after ="2009-01-28"; _name="iki-A4W-V3.0";
#_after ="2009-02-25"; _name="iki-A8W-V3.0";

#before
"""
cmdline= "cd "+ gd +";git log --after=\""+_before+"\" --before=\""+_day+"\"  --oneline |wc -l"
_commits= int(subprocess.check_output(cmdline,shell=True));
_created_files= int(subprocess.check_output(cmdline,shell=True))-1;#one empty line
cmdline= "cd "+ gd +";git log --after=\""+_before+"\" --before=\""+_day+"\"   --pretty=format: --name-status | cut -f2- | sort -u |wc -l"
_created_files= int(subprocess.check_output(cmdline,shell=True))-1;#one empty line
cmdline= "cd "+ gd +";git log --after=\""+_before+"\" --before=\""+_day+"\"   --min-parents=2 --oneline | wc -l"
_merges= int(subprocess.check_output(cmdline,shell=True));



#after
"""
cmdline= "cd "+ gd +";git log --after=\""+_day+"\" --before=\""+_after+"\"  --oneline |wc -l"
_commits= int(subprocess.check_output(cmdline,shell=True));
_created_files= int(subprocess.check_output(cmdline,shell=True))-1;#one empty line
cmdline= "cd "+ gd +";git log --after=\""+_day+"\" --before=\""+_after+"\"  --pretty=format: --name-status | cut -f2- | sort -u |wc -l"
_created_files= int(subprocess.check_output(cmdline,shell=True))-1;#one empty line
cmdline= "cd "+ gd +";git log --after=\""+_day+"\" --before=\""+_after+"\"  --min-parents=2 --oneline | wc -l"
_merges= int(subprocess.check_output(cmdline,shell=True));


merge_output= rd_output+ _name;

#conflict data
cmdline= "grep -e \"Automatic merge failed\" -e\"Merge with strategy octopus failed\" "+ merge_output + "/*.txt |cut -d':' -f1|sort -u| wc -l"
_automerge_failed =int(subprocess.check_output(cmdline,shell=True));
cmdline= "grep -e \"ERROR: content\" -e \"Not handling case\"  "+ merge_output + "/*.txt|cut -d':' -f1|sort -u|wc -l"
_automerge_failed_octopus =int(subprocess.check_output(cmdline,shell=True));		
_automerge_failed_simple = _automerge_failed - _automerge_failed_octopus

#cmdline= "grep -e \"Auto-merging\"  "+ merge_output + "/*.txt | cut -d':' -f2 | sort -u | wc -l"
cmdline= "grep -e \"Auto-merging\"  "+ merge_output + "/*.txt | wc -l"
_automerge_concurrent_files =int(subprocess.check_output(cmdline,shell=True));



cmdline="grep -e\"CONFLICT (\"  "+ merge_output + "/*.txt |  cut -d':' -f3 |sort -u |wc -l"
_file_with_conflits_simple =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"ERROR: content\" -e \"Not handling case\"  "+ merge_output + "/*.txt | cut -d':' -f3|sort -u| wc -l"
_file_with_conflits_octopus =int(subprocess.check_output(cmdline,shell=True));

cmdline="grep -e\"CONFLICT (\"  "+ merge_output + "/*.txt | wc -l"
_conflicts_simple =int(subprocess.check_output(cmdline,shell=True));
cmdline= "grep -e \"ERROR: content\" -e \"Not handling case\"  "+ merge_output + "/*.txt|wc -l"
_conflicts_octopus =int(subprocess.check_output(cmdline,shell=True));

#typesConflict
# simple conflict
cmdline="grep -e \"CONFLICT (content)\" "+ merge_output + "/*.txt | wc -l"
_cflsimple_content =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (cowarning: \"  "+ merge_output + "/*.txt | wc -l"
_cflsimple_cowarning_content =int(subprocess.check_output(cmdline,shell=True));
_cflsimple_content=_cflsimple_content+_cflsimple_cowarning_content
cmdline="grep -e \"CONFLICT (modify/delete)\"  "+ merge_output + "/*.txt | wc -l"
_cflsimple_modify_delete =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/modify)\"  "+ merge_output + "/*.txt | wc -l"
_cflsimple_rename_modify =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/delete)\"  "+ merge_output + "/*.txt | wc -l"
_cflsimple_rename_delete =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/rename)\"  "+ merge_output + "/*.txt | wc -l"
_cflsimple_rename_rename =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (rename/add)\"  "+ merge_output + "/*.txt | wc -l"
_cflsimple_rename_add =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"CONFLICT (add/add)\"  "+ merge_output + "/*.txt | wc -l"
_cflsimple_add_add =int(subprocess.check_output(cmdline,shell=True));

#octopus
cmdline="grep -e \"ERROR: content\"  "+ merge_output + "/*.txt | wc -l"
_cfloctopus_content =int(subprocess.check_output(cmdline,shell=True));
cmdline="grep -e \"Not handling case\"  "+ merge_output + "/*.txt | wc -l"
_clfoctopus_update_remove =int(subprocess.check_output(cmdline,shell=True));

#Simple resolutions (roll back)
cmdline ="grep -e\"CONFLICT (\" -e \"ERROR: content\"  -e \"Not handling case\" -e\"simpleResolution=True\"  "+ merge_output + "/*.txt | cut -d' ' -f1 | sort -u | cut -d':' -f1| uniq -c |grep -e\"2 \"|wc -l"
_simple_resolution =int(subprocess.check_output(cmdline,shell=True));

print "No of Commits:" +str(_commits)
print "No of Created files:" +str(_created_files)
print  "No of Concurrent modified files:" + str(_automerge_concurrent_files)
print "No of Merges:" +str(_merges)
print "No of merges resulted in conflicts:" + str(_automerge_failed)
print "No of Simple merges resulted in conflict:" +str(_automerge_failed_simple)
print "No of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus)
#print "No of Files with conflicts in Simple merges:" +str(_file_with_conflits_simple)
#print "No of Files with conflicts in Octopus merges: " +str(_file_with_conflits_octopus)
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

call("rm -rf "+ data_output+ _name +"_data.txt",shell=True);
file_out=open(data_output+_name +"_data.txt",'w')
file_out.write( "\nNo of Commits:" +str(_commits))
file_out.write( "\nNo of Created files:" +str(_created_files))
file_out.write( "\nNo of Concurrent modified files:" + str(_automerge_concurrent_files))
file_out.write( "\nNo of Merges:" +str(_merges))
file_out.write( "\nNo of merges resulted in conflicts:" + str(_automerge_failed))
file_out.write( "\nNo of Simple merges resulted in conflict:" +str(_automerge_failed_simple))
file_out.write( "\nNo of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus))
#file_out.write( "\nNo of Files with conflicts in Simple merges:" +str(_file_with_conflits_simple))
#file_out.write( "\nNo of Files with conflicts in Octopus merges: " +str(_file_with_conflits_octopus))
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



