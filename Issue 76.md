# Issue 76: No doc for 'attach'

Issue created by migration from https://trac.sagemath.org/ticket/76

Original creator: Justin Walker (justin@mac.com)

Original creation time: 2006-09-22 22:28:05

Assignee: somebody

sage: attach?
Object `attach` not found.

This means that 'attach' is not a first-class citizen of SAGE-land.



---

Comment by was created at 2006-09-23 00:59:34

I fixed this.  I did it by adding a file attach.py that defines a class
Attach and an instance attach of that class.  Then tab completion and
help work (since I wrote lots of help for that class).  Also, I made 
attach('foo') give a helpful error message.  The result is in the
hg repository, and here's the standard unifieid diff patch below...



```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1158972475 25200
# Node ID 6c5558645b6c76646cbc8edac64d12617ed36535
# Parent dd4a75ae77f673d39f3371fe3339966bfdd2287e
No docs or tab completion for "attach" -- Addressed trac tickets #76 and 77

Justin Walker complains that attach is not a first-class citizen
of SAGE-land, and this patch fixes that problem.  Also, it improves
the documentation for load.

--- a/sage/ext/sage_object.pyx	Fri Sep 22 14:13:45 2006 -0700
+++ b/sage/ext/sage_object.pyx	Fri Sep 22 17:47:55 2006 -0700
@@ -445,6 +445,13 @@ def load(filename, compress=True, verbos
     Load \sage object from the file with name filename, which will
     have an .sobj extension added if it doesn't have one.
 
+    NOTE: There is also a special SAGE command (that is not
+    available in Python) called load that you use by typing
+                sage.: load filename.sage
+    The documentation below is not for that command.  The documentation
+    for load is almost identical to that for attach.  Type attach? for
+    help on attach.
+
     This also loads a ".sobj" file over a network by specifying the full URL.
     (Setting "verbose = False" suppresses the loading progress indicator.)    
 
--- a/sage/misc/all.py	Fri Sep 22 14:13:45 2006 -0700
+++ b/sage/misc/all.py	Fri Sep 22 17:47:55 2006 -0700
@@ -6,6 +6,8 @@ from misc import (alarm, srange, xsrange
                   repr_lincomb, tmp_dir, tmp_filename,
                   DOT_SAGE, SAGE_ROOT, SAGE_URL, SAGE_DB, SAGE_TMP,
                   is_32_bit, is_64_bit, newton_method_sizes)
+
+from attach import attach
 
 from profiler import Profiler
 
--- /dev/null	Thu Jan 01 00:00:00 1970 +0000
+++ b/sage/misc/attach.py	Fri Sep 22 17:47:55 2006 -0700
@@ -0,0 +1,41 @@
+class Attach:
+    r"""
+    Attach a file to a running instance of SAGE.
+
+    attach is *not* a function and is not part of the Python language.
+    You attach a file, e.g., foo.sage or foo.py or foo.spyx, to a
+    running SAGE session by typing
+    
+        sage.: attach foo.sage   # or foo.py   or foo.spyx
+
+    The contents of the file are then loaded, which means they are
+    read into the running SAGE session.  For example, if foo.sage
+    contains 'x=5', after attaching foo.sage the variable x will be
+    set to 5.  Moreover, any time you change foo.sage, the attached
+    file will be re-read automatically (with no intervention on your
+    part).
+
+    INPUT: attach file1 file2 ...
+        -- space-separated list of .py, .spyx, and .sage files.
+
+    EFFECT:
+        -- Each file is read in and added to an internal list of watched files.
+           The meaning of reading a file in depends on the file type:
+               .py   -- read in with no preparsing (so, e.g., 2^3 is 2 bit-or 3),
+               .sage -- preparsed then the result is read in
+               .spyx -- *not* preparsed.  Compiled to a module m then "from m import *"
+                        is executed.
+
+    Type \code{attached_files()} for a list of all currently attached files.
+    You can remove files from this list to stop them from being watched. 
+
+    NOTE: attach is exactly the same as load, except it keeps track of the
+    loaded file and automatically reloads it when it changes. 
+    """
+    def __repr__(self):
+        return self.__doc__
+
+    def __call__(self, *args, **kwds):
+        raise RuntimeError, "Use 'attach filename' instead, where filename is a .py, .sage, or .spyx file."
+
+attach = Attach()
```



---

Comment by was created at 2006-09-23 00:59:49

Resolution: fixed


---

Comment by was created at 2006-09-23 00:59:49

And, of course, this closes the bug.
