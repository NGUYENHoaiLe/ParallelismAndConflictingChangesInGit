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
#cmdline= "cd "+ gd +";git log --min-parents=2 --oneline | wc -l"
#output = subprocess.check_output(cmdline,shell=True);
#numOfMerges= int(output)

print "\n################ EXTRACTING DATA ##################"
#print "(Data is written to Rd_extract_conflicts_data.txt)"


#V3.1, _day ="2011-08-31"
_day ="2011-08-31"
dictB={
"2011-08-24":"rails-B1W-V3.1",
"2011-08-17":"rails-B2W-V3.1",
"2011-08-10":"rails-B3W-V3.1",
"2011-08-03":"rails-B4W-V3.1",
"2011-07-06":"rails-B8W-V3.1"}

dictA={
"2011-09-07":"rails-A1W-V3.1",
"2011-09-14":"rails-A2W-V3.1",
"2011-09-21":"rails-A3W-V3.1",
"2011-09-28":"rails-A4W-V3.1",
"2011-10-26":"rails-A8W-V3.1"}

"""

#V3.2, _day ="2012-01-20"
_day ="2012-01-20"
dictB={
"2012-01-13":"rails-B1W-V3.2",
"2012-01-06":"rails-B2W-V3.2",
"2011-12-30":"rails-B3W-V3.2",
"2011-12-23":"rails-B4W-V3.2",
"2011-11-25":"rails-B8W-V3.2"}

dictA={
"2012-01-27":"rails-A1W-V3.2",
"2012-02-03":"rails-A2W-V3.2",
"2012-02-10":"rails-A3W-V3.2",
"2012-02-17":"rails-A4W-V3.2",
"2012-03-16":"rails-A8W-V3.2"}



#V4.0, _day ="2013-06-25"
_day ="2013-06-25"
dictB={
"2013-06-18":"rails-B1W-V4.0",
"2013-06-11":"rails-B2W-V4.0",
"2013-06-04":"rails-B3W-V4.0",
"2013-05-28":"rails-B4W-V4.0",
"2013-04-30":"rails-B8W-V4.0"}


dictA={
"2013-07-02":"rails-A1W-V4.0",
"2013-07-09":"rails-A2W-V4.0",
"2013-07-16":"rails-A3W-V4.0",
"2013-07-23":"rails-A4W-V4.0",
"2013-08-20":"rails-A8W-V4.0"}


#V4.1, _day ="2014-04-08"
_day ="2014-04-08"
dictB={
"2014-04-01":"rails-B1W-V4.1",
"2014-03-25":"rails-B2W-V4.1",
"2014-03-18":"rails-B3W-V4.1",
"2014-03-11":"rails-B4W-V4.1",
"2014-02-11":"rails-B8W-V4.1"}

dictA={
"2014-04-15":"rails-A1W-V4.1",
"2014-04-22":"rails-A2W-V4.1",
"2014-04-29":"rails-A3W-V4.1",
"2014-05-05":"rails-A4W-V4.1",
"2014-06-02":"rails-A8W-V4.1"}



#V4.2, _day ="2014-08-20"
_day ="2014-08-20"
dictB={
"2014-08-13":"rails-B1W-V4.2",
"2014-08-06":"rails-B2W-V4.2",
"2014-07-30":"rails-B3W-V4.2",
"2014-07-23":"rails-B4W-V4.2",
"2014-06-25":"rails-B8W-V4.2"}
dictA={
"2014-08-27":"rails-A1W-V4.2",
"2014-09-03":"rails-A2W-V4.2",
"2014-09-10":"rails-A3W-V4.2",
"2014-09-17":"rails-A4W-V4.2",
"2014-10-15":"rails-A8W-V4.2"}
"""


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



