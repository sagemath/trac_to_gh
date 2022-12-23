# Issue 3687: trivial problems in the sage_scripts spkg

Issue created by migration from https://trac.sagemath.org/ticket/3687

Original creator: tabbott

Original creation time: 2008-07-21 05:46:02

Assignee: mabshoff

Below is a list trivial problems in the sage_scripts spkg that were found by Debian's automatic package quality checking tools:

# Scripts missing #!/bin/sh lines in sage_scripts-3.0.5.spkg:
sage-pull
sage-push
sage-mirror
sage-mirror-darcs-scripts
sage-osx-open

# Scripts missing #!/usr/bin/python lines in sage_scripts-3.0.5.dpkg:
sage-startuptime.py
sage-gdb-pythonstartup
dsage_setup.py

# Files unnecessarily marked as executable in sage_scripts-3.0.5.spkg
sage-banner
sage-gdb-commands
sage-maxima.lisp

# Scripts that use #!sage or #!sage.bin as their interpreter in sage_scripts-3.0.5.spkg
# You want to use #!/usr/bin/env sage
sage-ipython 
sage-location
sage-preparse
sage-run 
sage-run2

# Weird files in sage_scripts-3.0.5.spkg marked executable
sage-README-osx.txt (duplicate of file of the same name in the root of the sage distribution)
sage-verify-pyc (this one is just weird)



---

Comment by tabbott created at 2008-07-21 05:52:43

Let's try that again with proper formatting:

# Scripts missing #!/bin/sh lines in sage_scripts-3.0.5.spkg:

```
sage-pull
sage-push
sage-mirror
sage-mirror-darcs-scripts
sage-osx-open
```


# Scripts missing #!/usr/bin/python lines in sage_scripts-3.0.5.dpkg:

```
sage-startuptime.py
sage-gdb-pythonstartup
dsage_setup.py
```


# Files unnecessarily marked as executable in sage_scripts-3.0.5.spkg

```
sage-banner
sage-gdb-commands
sage-maxima.lisp
```


# Scripts that use #!sage or #!sage.bin as their interpreter in sage_scripts-3.0.5.spkg
# You want to use #!/usr/bin/env sage

```
sage-ipython 
sage-location
sage-preparse
sage-run 
sage-run2
```


# Weird files in sage_scripts-3.0.5.spkg marked executable

```
sage-README-osx.txt (duplicate of file of the same name in the root of the sage distribution)
sage-verify-pyc (this one is just weird)
```



---

Attachment


---

Comment by tabbott created at 2009-04-26 05:27:58

Along with applying the attached patch, one should run

```
chmod -x sage-banner sage-gdb-commands sage-maxima.lisp sage-README-osx.txt sage-verify-pyc
```



---

Comment by awebb created at 2009-07-22 06:01:04

I applied the patch and ran the chmod command as suggested above.

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.


---

Comment by mvngu created at 2009-07-23 09:42:35

Resolution: fixed


---

Comment by mvngu created at 2009-07-26 06:51:32

See #6625 for a follow up to this ticket.
