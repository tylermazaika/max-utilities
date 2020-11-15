#!/usr/bin/python
# 
# max_styles_cleanup.py
#
# Remove all unused styles from a .maxpat file
#
# 2020-01-23
# Tyler Mazaika
# 

"""

purging styles regexp
(\,\s{3,})\{\s+"name" : "(sand|pattr|testing_objects|camo|steel)(-\d+)+"[^\}]+[^\{]+"multi" : 0\s+\}

This doesn't work with some styles (which might lack some additional keys).  Copy-paste into sublime


^(\,\s{3,})\{\s^(\s+)"name" : "(sand|pattr|testing_objects|camo|charcoal|heat|steel)(-\d+)+"[^\}]+[^\{]+\2"multi" : []\s+\}\s


how do we find styles which are not used in the file in which they are associated?
^(\,\s{3,})\{\s^(\s+)"name" : "(\w+)"[^\}]+[^\{]+\2"multi" : [01]\s+\}\s
When used in a box, a style name would appear as:   "style" : "<stylemame>"


Overall Logic Flow:
1. Get list of all styles names referenced in the file
2. Figure out which one is the primary document style.  Remove this from the list.
3. Figure out which (if any) of the other style definitions are actually referenced from this file.
4. In the list of initial definitions, remove anything which was neither (a) the primary style nor (b) used anywhere else in this file.
"""


import os          # filesytem operations
import subprocess
import argparse    # parse arguments / options
import datetime    # for logging history of versions moved
import re
import json




##### Argument Parsing
parser = argparse.ArgumentParser(prefix_chars="--", add_help=True, description="""

Remove all unused object style information in a Max patcher.

EXAMPLES:

 (1) Do an in-place cleanup of my_maxpat.maxpat:
	
	max_styles_cleanup.py -f my_maxpat.maxpat -i


 (2) In-place cleanup of all children in the current directory:

	find "$(pwd)" | grep .maxpat | xargs -I{} /Users/tyler/dev/max-utilities/max_styles_cleanup.py -f {} -i
  
""", formatter_class=argparse.RawTextHelpFormatter, epilog="""

(c) Tyler Mazaika, 2020

""" )
parser.add_argument("-f", "--file_name", required=True, \
	help="The full path of the argument to process.")
parser.add_argument("-i", "--in_place", action="store_true", \
	help="Replace text in place.")
args = parser.parse_args()



# Build the list of all style names used by boxes/patchers in the file.
source_file_full_path = args.file_name


styles_found = 0
patchers_found = 0


def clear_unused_styles_in_file( source_file_full_path ):
	with open(source_file_full_path) as original_file:
		
		used_style_names = []
		for line in original_file:
			# print line
			match = re.match('''\t+"style"\s:\s"(.+)".+''', line)
			if match and match.group(1) not in used_style_names:	# style line
				used_style_names.append( match.group(1) )

	print source_file_full_path

	# Keep a list of the used styles.  We will use this to replace instances of the "styles" dictionary in all the subpatchers later
	styles_dictionary = {} # name : settings

	# Get all the found style definitions themselves
	with open(source_file_full_path) as original_file:
		# Get all the found style definitions
		unused_style_names = []
		file_text = original_file.read()

		style_definiton = re.findall(r'''(^,\s{3,})(\{\s^\s+"name" : "([^\"]+)"[^\}]+[^\{]+"multi" : 0\s+\})''', file_text, re.MULTILINE)
		
		if style_definiton:
			for s in style_definiton:
				if s[2] in used_style_names:
					styles_dictionary[s[2]] = s[1]
				elif s[2] not in unused_style_names:
					unused_style_names.append( s[2] )


	# If there are no unused styles, just return.
	if not len(unused_style_names):
		print "No unused styles."
		print
		return

	# Printing info
	# print unused_style_names
	print "\n", len(unused_style_names), "Unused styles:"
	for s in unused_style_names: print s
	print "\n", len(used_style_names), "Used styles:"
	for s in used_style_names: print s


	print
	json_styles_replacement = []
	print "Known style values:"
	for k in styles_dictionary:
		print "Style name: ", k
		print styles_dictionary[k]
		json_styles_replacement.append( json.JSONDecoder().decode( styles_dictionary[k]) )
	# print json_styles_replacement


	# -------------------
	global styles_found
	global patchers_found
	styles_found = 0
	patchers_found = 0

	def styles_replacement( json_obj ):
		global styles_found
		global patchers_found
		# nonlocal patchers_found
		# nonlocal styles_found
		if "styles" in json_obj.keys():
			# print 'found style'
			styles_found += 1
			# print json_obj["styles"]
			json_obj["styles"] = json_styles_replacement
		
		if "boxes" in json_obj:
			for b in json_obj["boxes"]:
				# print
				# print "\n"*5
				if "patcher" in b["box"]:
					# print b["box"]
					styles_replacement( b["box"] )
		
		if "patcher" in json_obj:
			patchers_found += 1
			styles_replacement( json_obj["patcher"] )


	### Read the original file
	js = False

	with open(source_file_full_path, "r") as original_file:
		js = json.loads( original_file.read() )
		styles_replacement( js )

	### Write the file. Either write it over the original or to a tmp file
	if args.in_place:
		# print "skipping WRITE"
		with open(source_file_full_path, "w") as original_file:
			original_file.write( json.JSONEncoder().encode( js ))
	else:
		with open("/tmp/max_styles_cleanup_tmp.maxpat", "w") as tmp:
			tmp.write( json.JSONEncoder().encode( js ) )

	# print styles_found
	# print patchers_found
	print "Replaced {} styles dictionaries in {} subpatchers.".format( styles_found, patchers_found )
	print

clear_unused_styles_in_file( args.file_name )