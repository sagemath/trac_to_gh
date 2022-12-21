# Issue 6605: sage -docbuild DOC FORMAT should do better error checking on DOC

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-07-23 17:48:39

Assignee: tba

If I run `sage -docbuild hello html`, then a directory "hello" is created in `SAGE_ROOT/devel/sage/doc/en`.  Then if I run `sage -docbuild -help`, "hello" is listed as one of the options.

Error-checking should be done on the "document" argument of `sage -docbuild` to make sure this doesn't happen.



---

Comment by jhpalmieri created at 2009-07-23 19:58:39

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-07-23 19:58:39

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-07-23 19:58:39

As written, this depends on #6187 (although it would be easy enough to modify it to avoid this).   The new OMIT variable is for situations such as the one introduced by #5653, where there is a subdirectory "introspect" of SAGE_ROOT/doc/en/, which is not a document to be processed by "sage -docbuild", and so should be omitted from the list of all such documents.  (This patch doesn't depend on #5653, but it will be compatible with it, should #5653 be merged.)


---

Comment by mpatel created at 2009-07-24 09:31:56

The patch works for me.  I think a non-zero exit value is the UNIX convention for an error.  I can make an updated patch.  Or I can wait for more feedback on #6187. 

Notes for other potential tickets:

 * We could also print a similar message in the less severe case of an invalid format.
 * Instead of using [sys.exit()](http://docs.python.org/library/sys.html#sys.exit), we could raise (and catch) some exception, so that the builder can loop over documents, formats, and commands, printing warnings as necessary.  At the moment, though, this feature is not implemented.


---

Attachment

This patch is identical, except it uses sys.exit(1) instead of sys.exit(0).


---

Comment by mvngu created at 2009-07-24 22:35:27

Resolution: fixed


---

Comment by mvngu created at 2009-07-26 23:32:54

The patch applies but with fuzz:

```
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6605/trac_6605-docbuild-check.patch && hg qpush
adding trac_6605-docbuild-check.patch to series file
applying trac_6605-docbuild-check.patch
patching file doc/common/builder.py
Hunk #3 succeeded at 614 with fuzz 1 (offset -44 lines).
Now at: trac_6605-docbuild-check.patch
```



---

Comment by mvngu created at 2009-07-27 05:24:22

The patch `trac_6605-docbuild-check.patch` is buggy when it comes to (re)building the documentation of a new release. Assume you have applied this patch to Sage 4.1.1.alpha0, then build a source release with

```
sage -sdist <version>
```

or a binary release with

```
sage -bdist <version>
```

After that, upgrade a previous release to this new release and rebuild the documentation. You then get this error message:

```
[mvngu`@`sage sage-4.1.1.alpha1-test-x86_64-Linux]$ ./sage -docbuild tutorial htmlTraceback (most recent call last):
  File "/scratch/mvngu/sage-4.1.1.alpha1-test-x86_64-Linux/devel/sage/doc/common/builder.py", line 673, in <module>
    getattr(get_builder(name), type)()
  File "/scratch/mvngu/sage-4.1.1.alpha1-test-x86_64-Linux/devel/sage/doc/common/builder.py", line 616, in get_builder
    elif name in get_documents() or name in AllBuilder().get_all_documents():
NameError: global name 'get_documents' is not defined
```

The same error is raised if you rebuild the documentation of the binary version of the new release. I'm reopening this ticket and marking it as needs work.


---

Comment by mvngu created at 2009-07-27 05:24:22

Resolution changed from fixed to 


---

Comment by mvngu created at 2009-07-27 05:24:22

Changing status from closed to reopened.


---

Comment by jhpalmieri created at 2009-07-27 05:55:18

It doesn't need work.  As I mentioned in the first comment, it depends on #6187.  That's where "get_documents" is defined.

Please wait for #6187 to merge.


---

Comment by mhansen created at 2009-10-15 16:34:36

Resolution: fixed
