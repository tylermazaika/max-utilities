#!/usr/bin/python
# 
# max_styles_cleanup.py
#
# Remove all unused styles from a .maxpat file.
#
# 2020-01-23
# Tyler Mazaika
# 


import os          # filesytem operations
import argparse    # parse arguments / options
import re
import json


##### Argument Parsing
parser = argparse.ArgumentParser(prefix_chars="--", add_help=True, description="""

Remove all unused object style information in a Max patcher file (-f).  

Use with -i (--in_place) to rewrite the file (-f) in its current location. 

Without -i, files are written to /tmp/max_styles_cleanup/.  This allows you to open the file to preview/verify that the style removal has behaved correctly and with no unintended side effects.

EXAMPLES:

 (1) Do an in-place cleanup of my_maxpat.maxpat:
	
	max_styles_cleanup.py -f my_maxpat.maxpat -i


 (2) In-place cleanup of all children in the current directory:

	find "$(pwd)" | grep .maxpat | xargs -I{} /Users/tyler/dev/max-utilities/max_styles_cleanup.py -f {} -i

 (3) Do a cleanup of my_maxpat.maxpat, writing the new file to /tmp/max_styles_cleanup.

    max_styles_cleanup.py -f my_maxpat.maxpat
  
""", formatter_class=argparse.RawTextHelpFormatter, epilog="""

(c) Tyler Mazaika, 2020

""" )
parser.add_argument("-f", "--file_name", required=True, \
	help="The full path of the argument to process.")
parser.add_argument("-i", "--in_place", action="store_true", \
	help="Replace text in place.")
parser.add_argument("-v", "--verbose", action="store_true", \
	help="Verbose style output (of used styles).")
args = parser.parse_args()



# Build the list of all style names used by boxes/patchers in the file.
source_file_full_path = args.file_name


styles_found = 0
patchers_found = 0


def clear_unused_styles_in_file( source_file_full_path ):

	# Build used_style_names. Read the file and look for all places where a style is explicity assigned.
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

	# Store the text of ALL style definitions.
	with open(source_file_full_path) as original_file:
		# Get all the found style definitions
		unused_style_names = []
		file_text = original_file.read()

		# Make a list of matches of the style dictionary pattern
		style_definiton = re.findall(r'''(^,\s{3,})(\{\s^\s+"name" : "([^\"]+)"[^\}]+[^\{]+"multi" : 0\s+\})''', file_text, re.MULTILINE)
		
		if style_definiton:
			# Iterate the list to get the 
			for s in style_definiton:
				# s[2] is the name of the style.  s[1] is the style data
				if s[2] in used_style_names:
					# It's possible we will be defining and then re-defining the style over and over again here.  Maybe we'd only want to add the data the first time through?
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



	'''
	Styles are stored as an array/list in JSON. So initialize a new list for the styles and then add _only_ the known used styles to it.  We will then replace the "styles" indexes with this data in the future.
	'''
	json_styles_replacement = []
	if args.verbose:
		print "Known style values:"
	for k in styles_dictionary:
		if args.verbose:
			print "Style name: ", k
			print styles_dictionary[k]
		json_styles_replacement.append( json.JSONDecoder().decode( styles_dictionary[k]) )
	# print json_styles_replacement


	# -------------------
	global styles_found
	global patchers_found
	styles_found = 0
	patchers_found = 0

	# Recursively churn in the file and replace style definitions with our style dict
	def styles_replacement( json_obj ):
		global styles_found
		global patchers_found
		# nonlocal patchers_found
		# nonlocal styles_found

		# Keep track of styles used at this patcher level
		styles_used_by_boxes_in_this_patcher = []

		# Only patcher objects define a "boxes" key
		if "boxes" in json_obj:
			for b in json_obj["boxes"]:

				
				# If a box uses a style, make sure we note that style as required in this patcher level.
				if "style" in b["box"]:
					# print "BOX HAD Style", b["box"]["style"], styles_used_by_boxes_in_this_patcher
					styles_used_by_boxes_in_this_patcher.append( b["box"]["style"] )
				# print
				# print "\n"*5
				if "patcher" in b["box"]:
					# print b["box"]
					styles_replacement( b["box"] ) # Recurse and do it again

		# Only patcher objects define a "styles" key
		if "styles" in json_obj.keys(): 
			# print 'found style'
			styles_found += 1
			# print json_obj["styles"]

			# Add this patchers style to the used styles in this patcher.
			if json_obj["style"] not in styles_used_by_boxes_in_this_patcher:
				styles_used_by_boxes_in_this_patcher.append( json_obj["style"] )

			# Set the json styles dict to be only the known used styles.
			json_obj["styles"] = [ s for s in json_styles_replacement if s["name"] in styles_used_by_boxes_in_this_patcher ]


		
		if "patcher" in json_obj:
			patchers_found += 1
			styles_replacement( json_obj["patcher"] ) # Recurse and do it again


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

		new_file_path = "/tmp/max_styles_cleanup/{}".format(source_file_full_path.split("/")[-1])
		if not os.path.exists("/tmp/max_styles_cleanup"):
			os.mkdir("/tmp/max_styles_cleanup")
		with open(new_file_path, "w") as tmp:
			tmp.write( json.JSONEncoder().encode( js ) )
		print " ->", new_file_path

	print "Replaced {} styles dictionaries in {} subpatchers.".format( styles_found, patchers_found )
	print

clear_unused_styles_in_file( args.file_name )



"""
DEVELOPMENT NOTES


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

