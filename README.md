max-utilities
============

Scripts used for developing in Max and Max for Live devices.

This will hold scripts or configuration information which have been useful over the years during extensive development in Max.

Shell Scripts
-------------

#### max_styles_cleanup.py

(1) Do an in-place cleanup of my_maxpat.maxpat:

    max_styles_cleanup.py -f my_maxpat.maxpat -i

(2) In-place cleanup of all children in the current directory:

	find "$(pwd)" | grep .maxpat | xargs -I{} max_styles_cleanup.py -f {} -i

#### deploy_m4l_amxd.py

Deploy the most recent .amxd with name matching 'ClipTargeter' to your configured Development folder, with the name "ClipTarget-DEV.amxd".  Overwrites the existing version there if one exists.  This can be used to update a version currently used in a Live set(s).

    deploy_m4l_amxd.py -n ClipTargeter --development --latest



#### export_m4l

Calls AppleScript ("Export M4L.scpt") for exporting and deploying an Max for Live Device file

    $1 = Project Name Base
    $2 = stem name for appending to project name
    $3 = automatically deploy (bool) via deploy_m4l_amxd.py

    export_m4l $1 $2 $3




AppleScript
-------------

#### Export M4L.scpt

Automates the "Export Max for Live Device..." workflow in Max to export an .amxd file.
