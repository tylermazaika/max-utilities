#!/bin/bash

BUILD_DIR=~/build/m4l_DEVELOPMENT
TEST_DIR=/Users/Shared/_max_for_live_sample_distributions

cd "$BUILD_DIR"
for AMXD in $@;
do
	echo "copying $AMXD"
	ls -t | grep $AMXD | xargs -I {} cp {} /Users/Shared/_max_for_live_sample_distributions ;
done