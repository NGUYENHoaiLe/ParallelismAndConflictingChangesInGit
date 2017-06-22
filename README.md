# ParallelismAndConflictingChangeInGit
Parallelism and conflicting changes in Git version control systems

Please follow below steps to run your analysis

001.CONFIG GIT
	git config --global user.email="your@email.com"
	git config --global user.name ="Your name"
	git config --global log.date iso
	git config --global merge.conflictstyle diff3
	git config --global merge.tool kdiff3
	git config --diff.tool kdiff3
	
002. CLONE GIT REPOSITORY TO ./Sources FOLDER
	git clone <repository_link>  ./Sources
		
003. RUN SCRIPTS IN THE ORDER OF THEIR NAMES 
	python 001_replay_merges.py
	python 002_extract_conflicts_data.py
	python 003_list_author_merge_conflict_resolution.py
	python 004_revert_detector.py
	python 005_diff_content.py
	python 006_adjacemtline_detector.py
	python 007_revert_data.py
	python 008_diff_content_potential_conflicts.py
	python 009_adjacemtline_potential_conflicts.py
	
004. OUTPUT DATA FOLDER: ./data/*.txt
	002_extract_conflicts_data.txt
	003_list_author_merge_conflict_resolution.txt
	004_revert_data.txt
	006_adjacent_line_data.txt
	009_adjacent_line_potential_data.txt
	
  
