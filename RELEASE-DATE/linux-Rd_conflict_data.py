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


"""
#V2.6.39, _day ="2011-05-18"
_day ="2011-05-18"
dictB={
"2011-05-11":"linux-B1W-V2.6.39"
,"2011-05-04":"linux-B2W-V2.6.39"
,"2011-04-27":"linux-B3W-V2.6.39"
,"2011-04-20":"linux-B4W-V2.6.39"}
dictA={
"2011-05-25":"linux-A1W-V2.6.39"
,"2011-06-01":"linux-A2W-V2.6.39"
,"2011-06-08":"linux-A3W-V2.6.39"
,"2011-06-15":"linux-A4W-V2.6.39"}


#V3.0, _day ="2011-07-21"
_day ="2011-07-21"
dictB={
"2011-07-14":"linux-B1W-V3.0"
,"2011-07-07":"linux-B2W-V3.0"
,"2011-07-01":"linux-B3W-V3.0"
,"2011-06-23":"linux-B4W-V3.0"}
dictA={
"2011-07-28":"linux-A1W-V3.0"
,"2011-08-04":"linux-A2W-V3.0"
,"2011-08-11":"linux-A3W-V3.0"
,"2011-08-18":"linux-A4W-V3.0"}


#V3.1, _day ="2011-10-24"
_day ="2011-10-24"
dictB={
"2011-10-17":"linux-B1W-V3.1"
,"2011-10-10":"linux-B2W-V3.1"
,"2011-10-03":"linux-B3W-V3.1"
,"2011-09-26":"linux-B4W-V3.1"}
dictA={
"2011-10-31":"linux-A1W-V3.1"
,"2011-11-07":"linux-A2W-V3.1"
,"2011-11-14":"linux-A3W-V3.1"
,"2011-11-21":"linux-A4W-V3.1"}


#V3.19, _day ="2015-02-08"
_day ="2015-02-08"
dictB={
"2015-02-01":"linux-B1W-V3.19"
,"2015-01-25":"linux-B2W-V3.19"
,"2015-01-18":"linux-B3W-V3.19"
,"2015-01-11":"linux-B4W-V3.19"}
dictA={
"2015-02-15":"linux-A1W-V3.19"
,"2015-02-22":"linux-A2W-V3.19"
,"2015-03-01":"linux-A3W-V3.19"
,"2015-03-08":"linux-A4W-V3.19"}


#V4.0, _day ="2015-04-12"
_day ="2015-04-12"
dictB={
"2015-04-05":"linux-B1W-V4.0"
,"2015-03-29":"linux-B2W-V4.0"
,"2015-03-22":"linux-B3W-V4.0"
,"2015-03-15":"linux-B4W-V4.0"}
dictA={
"2015-04-19":"linux-A1W-V4.0"
,"2015-04-26":"linux-A2W-V4.0"
,"2015-05-03":"linux-A3W-V4.0"
,"2015-05-10":"linux-A4W-V4.0"}

"""
#V4.1, _day ="2015-06-21"
_day ="2015-06-21"
dictB={
"2015-06-14":"linux-B1W-V4.1"
,"2015-06-07":"linux-B2W-V4.1"
,"2015-05-31":"linux-B3W-V4.1"
,"2015-05-24":"linux-B4W-V4.1"}
dictA={
"2015-06-28":"linux-A1W-V4.1"
,"2015-07-05":"linux-A2W-V4.1"
,"2015-07-12":"linux-A3W-V4.1"
,"2015-07-19":"linux-A4W-V4.1"}




#before
for _before, _name in dictB.iteritems():
	cmdline= "cd "+ gd +";git log --after=\""+_before+"\" --before=\""+_day+"\"  --oneline |wc -l"
	_commits= int(subprocess.check_output(cmdline,shell=True));
	_created_files= int(subprocess.check_output(cmdline,shell=True))-1;#one empty line
	cmdline= "cd "+ gd +";git log --after=\""+_before+"\" --before=\""+_day+"\"   --pretty=format: --name-status | cut -f2- | sort -u |wc -l"
	_created_files= int(subprocess.check_output(cmdline,shell=True))-1;#one empty line
	cmdline= "cd "+ gd +";git log --after=\""+_before+"\" --before=\""+_day+"\"   --min-parents=2 --oneline | wc -l"
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
	print "\n ###### "   + _name
	print "No of Commits:" +str(_commits)
	print "No of Merges:" +str(_merges)
	print "No of merges resulted in conflicts:" + str(_automerge_failed)

	print "No of Modified files:" +str(_created_files)
	print  "No of Concurrent modified files:" + str(_automerge_concurrent_files)
	#print "No of Simple merges resulted in conflict:" +str(_automerge_failed_simple)
	#print "No of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus)
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
	file_out.write( "\nNo of Merges:" +str(_merges))
	file_out.write( "\nNo of merges resulted in conflicts:" + str(_automerge_failed))

	file_out.write( "\nNo of Modified  files:" +str(_created_files))
	file_out.write( "\nNo of Concurrent modified files:" + str(_automerge_concurrent_files))
	
	#file_out.write( "\nNo of Simple merges resulted in conflict:" +str(_automerge_failed_simple))
	#file_out.write( "\nNo of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus))
	#file_out.write( "\nNo of Files with conflicts in Simple merges:" +str(_file_with_conflits_simple))
	#file_out.write( "\nNo of Files with conflicts in Octopus merges: " +str(_file_with_conflits_octopus))
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


#after
for _after, _name in dictA.iteritems():
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

	print "\n ###### "   + _name
	print "No of Commits:" +str(_commits)
	print "No of Merges:" +str(_merges)
	print "No of merges resulted in conflicts:" + str(_automerge_failed)

	print "No of Modified files:" +str(_created_files)
	print  "No of Concurrent modified files:" + str(_automerge_concurrent_files)
	#print "No of Simple merges resulted in conflict:" +str(_automerge_failed_simple)
	#print "No of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus)
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
	file_out.write( "\nNo of Merges:" +str(_merges))
	file_out.write( "\nNo of merges resulted in conflicts:" + str(_automerge_failed))

	file_out.write( "\nNo of Modified  files:" +str(_created_files))
	file_out.write( "\nNo of Concurrent modified files:" + str(_automerge_concurrent_files))
	
	#file_out.write( "\nNo of Simple merges resulted in conflict:" +str(_automerge_failed_simple))
	#file_out.write( "\nNo of Octopus merges resulted in conflicts:" +str(_automerge_failed_octopus))
	#file_out.write( "\nNo of Files with conflicts in Simple merges:" +str(_file_with_conflits_simple))
	#file_out.write( "\nNo of Files with conflicts in Octopus merges: " +str(_file_with_conflits_octopus))
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


