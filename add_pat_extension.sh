#!/bin/bash

# make sure a directory has been entered.
if [[ ! $1 ]]
then
	echo -n "enter directory for operation: "
	read DIR
else
	DIR=$1
fi

# go to the selected directory.
cd $DIR
DIR=`pwd`
echo $DIR

ls
#for every directory including the current
for current_dir in `ls` .
do
	if [[ -d "$current_dir" ]]
	then
		# go to that directory and list the files
		cd $current_dir
		echo ; echo; pwd
		ls
		echo
		for filename in `ls`
		do
			# if the file is just a file and does not end with '.pat'
			if [[ -f $filename ]] # && [[ ! `grep .pat $filename` ]]
			then
				# add '.pat' as file extension to the name and report.
				mv $filename ${filename}.pat
				echo "$filename ---> ${filename}.pat"
			fi
		done
		cd $DIR #move back to initial directory
	fi
done

