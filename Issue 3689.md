# Issue 3689: trivial problems in the examples spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-07-21 05:48:56

Assignee: mabshoff

# Scripts missing #!/bin/sh lines in examples-3.0.5.spkg:

```
programming/standalone_scripts/python/test
```


# Empty directories in examples-3.0.5.spkg

```
examples/misc/
```


# Scripts that use #!sage or #!sage.bin as their interpreter in examples-3.0.5.spkg
# You want to use #!/usr/bin/env sage

```
programming/standalone_scripts/python/binom 
programming/standalone_scripts/python/factor 
programming/standalone_scripts/sage/factor.sage 
programming/standalone_scripts/sage/simple.sage
```



---

Attachment


---

Comment by tabbott created at 2009-04-26 05:24:45

Oops, tried to update the wrong patch.  You just want the examples-shebang.patch.
Along with applying that patch, one should run

```
rmdir misc
```

from the root of the examples spkg.  The /usr/bin/env/sage issues have already been fixed.


---

Comment by awebb created at 2009-07-22 06:01:14

I applied the patch and ran the rmdir command as suggested above.

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.


---

Comment by mvngu created at 2009-07-23 09:48:39

Resolution: fixed
