#!/usr/bin/python
# 
# 2017-01-19
# Tyler Mazaika
# 
# Copy a given version of an M4L (.amxd) device into position for use in Ableton Live.

# TODO: --prod vs. --dev
# --dev should, for the incremental build, replace a device with "-DEV" suffix, used for testing and development.

import os          # filesytem operations
import subprocess
import argparse    # parse arguments / options
import datetime    # for logging history of versions moved
import re

# External to Live's search path.  Holds individually-named build versions.
SOURCE_DIR=os.path.expanduser("~/build/m4l_amxd")

# External to Live's search path.  Devices copied from SOURCE_DIR to here with a 
# uniform name (so the same set can be used with newer device versions as they are made.)
DEVELOPMENT_DEPLOY_DIR=os.path.expanduser("~/build/m4l_DEVELOPMENT")
DEVELOPMENT_DEVICE_SUFFIX="-DEV"

# In Live's search path.
PRODUCTION_DEPLOY_DIR=os.path.expanduser("~/Music/Ableton/User Library/M4L Toolkit v1") # in live search path


for folder in ( SOURCE_DIR, PRODUCTION_DEPLOY_DIR, DEVELOPMENT_DEPLOY_DIR ):
	assert os.path.exists( folder ), "Required directory does not exist.\n{}".format( folder )

assert os.path.exists( SOURCE_DIR )
HISTORY_FILE=os.path.expanduser("~/Music/Ableton/User Library/m4l_deploy_amxd_history.log")
#print SOURCE_DIR


parser = argparse.ArgumentParser(prefix_chars="--", add_help=True, description="""

Copy a .amxd file from the source directory into the deploy directory.  Differentiates between production and development directories

EXAMPLE USAGE:

1) Copy the most recent build of device 'ClipTargeter' from the source directory into the development directory (with suffix -DEV).

  deploy_amxd -n ClipTargeter --development --latest
  
2) Copy the most recent build of device 'ClipTargeter' from the source directory into the production directory directory.

  deploy_amxd -n ClipTargeter -p -l

3) Display history.

  deploy_amxd --history

  
""", formatter_class=argparse.RawTextHelpFormatter, epilog="""
Default Directories:

  SOURCE DIRECTORY       : {}
  PRODUCTION_DEPLOY_DIR  : {}
  DEVELOPMENT_DEPLOY_DIR : {}
""".format( SOURCE_DIR, PRODUCTION_DEPLOY_DIR, DEVELOPMENT_DEPLOY_DIR))

base_mode = parser.add_mutually_exclusive_group(required=True)
base_mode.add_argument("-n", "--source_file_name", \
	help="The base name of the device you wish to copy.")
mode = parser.add_mutually_exclusive_group()
mode.add_argument("-d", "--development", action="store_true", \
	help="Copy the most recent build into the development directory with the '{}' suffix.".format(DEVELOPMENT_DEVICE_SUFFIX))
mode.add_argument("-p", "--production", action="store_true", \
	help="Use the production directory.")
parser.add_argument("-l", "--latest", action="store_true", \
	help="If set, automatically get the most recently created version of the device from the source directory.")
parser.add_argument("-f", "--file_name", \
	help="If set, use the specific .amxd filename provided as the source for deployment.")
parser.add_argument("--no-prompt", action="store_true", \
	help="If set, do not prompt when overwriting existing .amxd files in the deploy directory.")
base_mode.add_argument("--history", action="store_true", \
	help="Display the last 50 lines of history and exit.")
parser.add_argument("-v", "--verbose", action="store_true", \
	help="Print history verbosely (includes full file paths).")

args = parser.parse_args()


# Make sure the log file is open.  Read history if we're in history mode.
if args.history:
	log_file = open(HISTORY_FILE, "r")
	print
	print "{:26}  {:30}    {:30}".format("Date", "Original File", "Deploy File")
	print "{:26}  {:30}    {:30}".format("="*26, "="*30, "="*30)
	ln_count = 0
	for ln in log_file.readlines()[-100:]:
		# print ln[:120]
		if (ln_count % 2) == 0:
			print "{:95}".format(ln[:-1]),
		else:
			if args.verbose:
				# Print out the file movement, in original format
				print ln, 
			else:
				# Don't print anything about the actual file names
				print " "
		ln_count += 1
	log_file.close()
	exit(0)
log_file = open(HISTORY_FILE, "a")


# Parse the file/path name arguments.
source_file_full_path = ""
file_name_trunk = args.source_file_name
log_label_string = "[PROD]"
if args.development:
	# Development
	log_label_string = "[DEV]"
	target_file_full_path = DEVELOPMENT_DEPLOY_DIR + "/" + file_name_trunk + DEVELOPMENT_DEVICE_SUFFIX + ".amxd"
else:
	# Production
	target_file_full_path = PRODUCTION_DEPLOY_DIR + "/" + file_name_trunk + ".amxd"


# Automatically detect the latest version
if args.latest:
	print
	print "Finding most recent version of {}".format( args.source_file_name )
	command = subprocess.Popen( ["ls", "-t1", SOURCE_DIR], stdout=subprocess.PIPE )
	stdout, stderr = command.communicate()

	# If the device name trunk includes special regexp characters we need to escape them
	escaped_file_name_trunk = ""
	for c in file_name_trunk:
		# print c
		if c in ["+", "*", "[", "]"]:
			escaped_file_name_trunk += "\\" + c
		else:
			escaped_file_name_trunk += c
	# print escaped_file_name_trunk

	# Iterate through the 'ls -t1' result and grep to find the first matched file.
	found_file = ""
	for file_name in stdout.split("\n"):
		# print file_name
		if re.match("{}(\-[\w\.\d]+)\.amxd".format( escaped_file_name_trunk ), file_name):
			found_file = file_name
			break
	if not found_file:
		print ">>> No matching .amxd file found for file_name_trunk = '{}'".format(file_name_trunk)
		exit(1)
	source_file_full_path = SOURCE_DIR + "/" + found_file
elif args.file_name:
	print
	source_file_full_path = SOURCE_DIR + "/" + args.file_name

print "\t" + source_file_full_path

# Confirm replacement
if os.path.exists( target_file_full_path ):
	# confirm we want to replace.
	if not args.no_prompt and not args.development:
		print
		print "Device already exists at [production] path:\n\t" + target_file_full_path
		confirmation = raw_input("Replace existing device? (y/n): ".strip() )
		if confirmation.lower() != "y":
			print "Cancelled by user. Exiting."
			exit(1)

# Copy the file into place
info_string = '{:19} {:6} {:30} --> {:30}  \n  ("{}" --> "{}")'.format( str(datetime.datetime.now())[:-7], log_label_string, source_file_full_path.split("/")[-1], target_file_full_path.split("/")[-1], source_file_full_path, target_file_full_path)
print
print info_string
print

subprocess.check_call( ["cp", source_file_full_path, target_file_full_path] )
log_file.write( info_string + "\n")
log_file.close()

# Remove any tags associated with a file.  But this does still leave the color/label on it.
# find "/Users/tyler/Max for Live Device Projects/Max for Live Devices" -xattrname com.apple.metadata:_kMDItemUserTags -name "*.maxproj" -print0 | xargs -I{} -0 xattr -d com.apple.metadata:_kMDItemUserTags {}
cmd = 'find "/Users/tyler/Max for Live Device Projects/Max for Live Devices" -xattrname com.apple.metadata:_kMDItemUserTags -name "*.maxproj" -print0 | xargs -I\{\} -0 xattr -d com.apple.metadata:_kMDItemUserTags \{\}'
ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print output


