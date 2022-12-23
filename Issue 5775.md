# Issue 5775: Building the documentation after -bdisting is broken

Issue created by migration from https://trac.sagemath.org/ticket/5775

Original creator: mabshoff

Original creation time: 2009-04-13 07:51:55

Assignee: mhansen

This is a tree that was bdisted from 3.4.1.rc2:

```
sphinx-build -b html -d /scratch/mabshoff/sage-3.4.1.rc3/devel
/sage/doc/output/doctrees/en/tutorial   .  /scratch/mabshoff/sage-
3.4.1.rc3/devel/sage/doc/output/html/en/tutorial
Build finished.  The built documents can be found in /scratch
/mabshoff/sage-3.4.1.rc3/devel/sage/doc/output/html/en/tutorial
sphinx-build -b html -d /scratch/mabshoff/sage-3.4.1.rc3/devel
/sage/doc/output/doctrees/en/website   .  /scratch/mabshoff/sage-
3.4.1.rc3/devel/sage/doc/output/html/en/website
Build finished.  The built documents can be found in /scratch
/mabshoff/sage-3.4.1.rc3/devel/sage/doc/output/html/en/website
Traceback (most recent call last): 
 File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 668, in <module>
    getattr(get_builder(name), type)()
  File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 258, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 348, in _wrapper
    for module_name in self.get_modified_modules():
  File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/doc/common
/builder.py", line 415, in get_modified_modules
    added, changed, removed = env.get_outdated_files(False)
  File "/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python2.5/site-
packages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py", line 400, in get_outdated_files
    newmtime = path.getmtime(self.doc2path(docname))
  File "/scratch/mabshoff/sage-3.4.1.rc3/local/lib/python
/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: '/scratch/mabshoff
/sage-3.4.1.rc2/devel/sage-main/doc/en/reference/sage/combinat/word/
morphism.rst'
```



---

Comment by mabshoff created at 2009-04-13 08:24:43

To reproduce this: *-bdist*, unpack in some other place, run *make* -> *boom*.

Note that deleting the output directory and restarting *make* gets past this problem.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-17 22:54:12

I don't care too much about this, so I am bumping it to 3.4.2 for now.

Cheers,

Michael


---

Comment by mvngu created at 2010-02-02 23:50:16

I don't see this problem any more. The process of "-bdist", unpack at a different directory, then run "make" works for me with Sage 4.3.2.alpha1. I'm closing this as fixed.


---

Comment by mvngu created at 2010-02-02 23:50:16

Resolution: fixed
