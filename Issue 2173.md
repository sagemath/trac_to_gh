# Issue 2173: [with patch; needs review] SAGE setup.py should run cython as "python2.5 cython"

Issue created by migration from https://trac.sagemath.org/ticket/2173

Original creator: tabbott

Original creation time: 2008-02-16 01:06:23

Assignee: tabbott

the cython in debian runs as #!/usr/bin/python, and /usr/bin/python is python2.4 by default in Debian.  Thus, the SAGE setup.py should explicitly run "python2.5 cython" to get python2.5.

I'm submitting in non-mercurial format since I get the following error when I try to:

[tabbott`@`mega-man sage$] hg diff
abort: index 00changelog.i invalid format 2!
[tabbott`@`mega-man sage$] cat .hg/00changelog.i ; echo
� dummy changelog to prevent using the old repo layout



---

Attachment

The patch doesn't work as is for the non-Debianized build:

```
Building sage/matrix/matrix_dense.c because it depends on sage/matrix/matrix_dense.pyx.
python2.5 cython --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/devel/sage-main -o sage/matrix/matrix_dense.c sage/matrix/matrix_dense.pyx
python2.5: can't open file 'cython': [Errno 2] No such file or directory
sage: Error running cython.
sage: There was an error installing modified sage library code.
```

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 01:30:39

I guess it is a patch issue: `python2.5 `which cython`` works. We could just do something analog like the other places in setup.py and introduce a special case for the Debianized build.

Cheers,

Michael


---

Comment by tabbott created at 2008-02-16 01:38:21

Yeah, python2.5 `which cython` is what I'd intended; for non-debian builds, SAGE_LOCAL/bin should be in PATH, and for Debian builds, /usr/bin/cython will be in PATH, so I think that's best.


---

Comment by tabbott created at 2008-03-29 22:01:52

I'm attaching a new patch that includes the python2.5 `which cython` change and also the other things that were needed to get SAGE 2.10.4 to build on Debian.

I think the changeset can be cleaned up to just create a symlink 'python' in SAGE_LOCAL/bin that goes to the working python2.5 and then one would not have to do as many changes that replace 'python' with 'python2.5' in the build process.


---

Attachment

sage-spkg-debian.patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-29 23:05:03

Merged in Sage 2.11.rc0


---

Comment by mabshoff created at 2008-03-29 23:05:03

Resolution: fixed
