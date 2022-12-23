# Issue 9950: Missing package init file 'sage/tests/french_book/__init__.py'

Issue created by migration from https://trac.sagemath.org/ticket/9951

Original creator: mpatel

Original creation time: 2010-09-19 21:36:49

Assignee: jason

CC:  ylchapuy zimmerma

Running `sage -b` with 4.6.alpha1 gives:

```
[...]
running build_py
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
running build_ext
[...]
```

The solution is to add an "empty" `__init__.py` file.  Mercurial may complain if the file is truly empty.  We can use 

 # This comment is here so the file is non-empty (so Mercurial will check it in).

say, instead.

This is a follow-up to #9395.


---

Comment by drkirkby created at 2010-09-19 21:53:15

I made the mistake the other day of creating an empty file. Mercruial checked it in OK.


---

Comment by leif created at 2010-09-20 03:32:33

Replying to [comment:2 drkirkby]:
> I made the mistake the other day of creating an empty file. Mercruial checked it in OK. 

Yeah, it is properly checked it, but exporting it gives

```
# HG changeset patch
# User Leif Leonhardy <not.really@online.de>
# Date 1284952693 -7200
# Node ID eb739c32247985cc9923bb8dbdebf1f7eb404666
# Parent  81b3de2e81408620d6d68f022cd7d834880fa029
#9951 Add (empty) sage/tests/french_book/__init__.py file to avoid warnings.

# HG changeset patch
# User Leif Leonhardy <not.really@online.de>
# Date 1284953161 -7200
# Node ID 87a65b1dbf4f7fc9dd0e468724924363e0d9072c
# Parent  eb739c32247985cc9923bb8dbdebf1f7eb404666
#9951 ... and fill it such that Mercurial will produce a proper patch :/

diff -r eb739c322479 -r 87a65b1dbf4f sage/tests/french_book/__init__.py
--- a/sage/tests/french_book/__init__.py	Mon Sep 20 05:18:13 2010 +0200
+++ b/sage/tests/french_book/__init__.py	Mon Sep 20 05:26:01 2010 +0200
@@ -0,0 +1,1 @@
+# This comment is here so the file is non-empty (so Mercurial will check it in).
```

(I.e., the patch(es) won't apply properly.) :/


---

Comment by leif created at 2010-09-20 03:41:20

Apply to Sage library


---

Attachment

_Non-empty_ patch is up.


---

Comment by leif created at 2010-09-20 03:44:02

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-09-20 07:09:46

sorry, I don't know how to review this patch. On my side, `sage -b` works with the vanilla
sage-4.6.alpha1.


---

Comment by leif created at 2010-09-20 12:41:45

Replying to [comment:5 zimmerma]:
> sorry, I don't know how to review this patch. On my side, `sage -b` works with the vanilla
> sage-4.6.alpha1.

If it wouldn't *work*, the priority of this ticket would be _blocker_ rather than _minor_. ;-)

The patch just avoids potentially annoying or confusing warning messages.
 
To see the difference, do for example:

```sh
~/Sage/sage-4.6.alpha1/devel/sage-main$ touch sage/tests/french_book/numbertheory.py 
~/Sage/sage-4.6.alpha1/devel/sage-main$ ../../sage -b     
----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Execute 0 commands (using 0 threads)
Time to execute 0 commands: 0.0640869140625 seconds
Finished compiling Cython code (time = 0.421274900436 seconds)
running install
running build
running build_py
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
copying sage/tests/french_book/numbertheory.py -> build/lib.linux-x86_64-2.6/sage/tests/french_book
package init file 'sage/tests/french_book/__init__.py' not found (or not a regular file)
running build_ext
Total time spent compiling C/C++ extensions:  0.0187819004059 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/tests/french_book/numbertheory.py -> /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book
byte-compiling /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book/numbertheory.py to numbertheory.pyc
running install_egg_info
Removing /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /home/leif/Sage/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m1.590s
user	0m1.110s
sys	0m0.300s
```


Then apply the patch and retry it. (In fact, you should not even have to touch the file, the messages should be there regardless of files being modified or not.)


---

Comment by zimmerma created at 2010-09-21 07:09:31

with the patch, I get:

```
tarte% ../../sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 1.09672546387e-05 seconds
Finished compiling Cython code (time = 0.345225095749 seconds)
running install
running build
running build_py
copying sage/tests/french_book/__init__.py -> build/lib.linux-x86_64-2.6/sage/tests/french_book
running build_ext
Total time spent compiling C/C++ extensions:  0.017902135849 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/tests/french_book/__init__.py -> /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book
byte-compiling /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/tests/french_book/__init__.py to __init__.pyc
running install_egg_info
Removing /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /tmp/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real    0m1.459s
user    0m1.145s
sys     0m0.233s
```

thus a positive review.

Paul


---

Comment by zimmerma created at 2010-09-21 07:09:31

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 09:11:03

Resolution: fixed
