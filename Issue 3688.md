# Issue 3688: trivial problems in the sage spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-07-21 05:48:09

Assignee: mabshoff

# Scripts missing #!/bin/sh lines in sage-3.0.5.spkg:

```
pull
install
```


# Scripts missing #!/usr/bin/python lines in sage-3.0.5.dpkg:

```
sage/dsage/misc/hostinfo.py
sage/dsage/scripts/dsage_setup.py
```


# Files unnecessarily marked as executable in sage-3.0.5.spkg

```
sage/graphs/planarity/graphEmbed.c
sage/graphs/planarity/graphIO.c
sage/graphs/planarity/graphIsolator.c
sage/graphs/planarity/graphNonplanar.c
sage/graphs/planarity/graphPreprocess.c
sage/graphs/planarity/graphStructure.c
sage/graphs/planarity/graphTests.c
sage/graphs/planarity/listcoll.c
sage/graphs/planarity/planarity.c
sage/graphs/planarity/stack.c
```


# Other files unnecessarily marked as executable

```
sage-README-osx.txt (in the root of the sage distribution)
```




---

Attachment


---

Comment by tabbott created at 2009-04-26 05:18:41

I realized this should probably be marked as having a patch, since it does.  You'll want to apply the patch that is attached and run

```
   chmod -x sage/graphs/planarity/*.c
```

from the root of the Sage spkg.


---

Comment by awebb created at 2009-07-21 16:40:58

I don't see a sage/dsage directory in sage-4.1.spkg. Has this been moved/removed?


---

Comment by awebb created at 2009-07-22 06:04:36

I applied the patch and ran the chmod command as suggested above. The patch failed due to missing files but I continued anyway.

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1. 

Assuming that the change in dsage is fine then I would give this a positive review.


---

Comment by awebb created at 2009-07-22 06:05:38

skip dsage files


---

Comment by mvngu created at 2009-07-24 09:11:34

Resolution: fixed


---

Attachment

dsage has been moved into its own package. You can find it under `SAGE_ROOT/spkg/standard/`.
