# Issue 5632: [with spkg; needs review] doc fixes for quaternion algebra element

Issue created by migration from https://trac.sagemath.org/ticket/5632

Original creator: jhpalmieri

Original creation time: 2009-03-29 15:39:54

Assignee: tbd

Along the lines of #5541, here are some doc fixes for quaternion_algebra_element.pyx.


---

Comment by jhpalmieri created at 2009-03-29 16:15:55

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-03-29 16:15:55

Changing assignee from tbd to jhpalmieri.


---

Comment by mvngu created at 2009-03-30 06:45:41

jhpalmieri: Can you please provide a link to the spkg you mentioned above? I seem to not find a link or the spkg anywhere on this ticket. Sorry if I've missed anything.


---

Comment by jhpalmieri created at 2009-03-30 13:55:37

Sorry, should have said "with patch", not "with spkg".


---

Comment by mvngu created at 2009-03-31 05:37:36

Looks good, applies OK against Sage 3.4.1.alpha0, all doctests passed. Positive review.


---

Comment by mabshoff created at 2009-03-31 07:53:42

Due to #5520 this patch needs to be rebased:

```
sage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5632_quaternion.patch 
patching file sage/algebras/quatalg/quaternion_algebra_element.pyx
Hunk #1 succeeded at 171 (offset 4 lines).
Hunk #2 succeeded at 354 (offset 140 lines).
Hunk #3 succeeded at 398 (offset 140 lines).
Hunk #4 succeeded at 410 (offset 140 lines).
Hunk #5 succeeded at 422 (offset 140 lines).
Hunk #6 succeeded at 437 (offset 140 lines).
Hunk #7 succeeded at 496 (offset 140 lines).
Hunk #8 succeeded at 537 (offset 167 lines).
Hunk #9 succeeded at 685 (offset 167 lines).
Hunk #10 succeeded at 712 (offset 167 lines).
Hunk #11 succeeded at 797 (offset 224 lines).
Hunk #12 succeeded at 1149 (offset 261 lines).
Hunk #13 succeeded at 1219 (offset 260 lines).
Hunk #14 succeeded at 1244 (offset 260 lines).
Hunk #15 succeeded at 1494 (offset 441 lines).
Hunk #16 succeeded at 1854 (offset 441 lines).
Hunk #17 FAILED at 1912.
1 out of 17 hunks FAILED -- saving rejects to file sage/algebras/quatalg/quaternion_algebra_element.pyx.rej
```


Cheers,

Michael


---

Comment by jhpalmieri created at 2009-03-31 15:37:24

Here's a rebased version.  Since the previous one had a positive review, I assume this one does, too.

However, I think we also need something like the attached 'quatalg-reference.patch' to process the moved files for inclusion into the reference manual, but when I apply it and try to build the docs, I get error messages like

```
Traceback (most recent call last):
  File "/Applications/sage/devel/sage/doc/common/builder.py", line 668, in <module>
    getattr(get_builder(name), type)()
  File "/Applications/sage/devel/sage/doc/common/builder.py", line 348, in _wrapper
    for module_name in self.get_modified_modules():
  File "/Applications/sage/devel/sage/doc/common/builder.py", line 415, in get_modified_modules
    added, changed, removed = env.get_outdated_files(False)
  File "/Applications/sage_builds/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/Sphinx-0.5.1-py2.5.egg/sphinx/environment.py", line 400, in get_outdated_files
    newmtime = path.getmtime(self.doc2path(docname))
  File "/Applications/sage_builds/sage-3.4.1.alpha0/local/lib/python2.5/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: '/Applications/sage_builds/sage-3.4.1.alpha0/devel/sage-main/doc/en/reference/sage/algebras/quaternion_algebra.rst'
```

(This fix should have been part of #5520, I think.)


---

Attachment

rebased post #5520, positive review for this patch


---

Attachment

For the record: positive review quatalg-reference.patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 20:08:49

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 20:08:49

Resolution: fixed
