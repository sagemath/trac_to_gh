# Issue 9850: sage -pkg may hang if there are many uncommitted changes in the package

Issue created by migration from https://trac.sagemath.org/ticket/9851

Original creator: SimonKing

Original creation time: 2010-09-03 09:51:51

Assignee: tbd

CC:  mpatel

Keywords: sage-pkg, stderr hangs

At [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c008a74ae2b3af95), I reported the following problem.

 - Take a folder with many uncommitted changes in a Mercurial repository. [Example](http://www.google.com/url?sa=D&q=http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.alpha0.tar.gz&usg=AFQjCNE362g2kL77GzI-7T5RaOBx92X0KQ).
 - Run `sage -pkg` on it.
 - It will hang forever while it is attempted to read from `stderr` of a subprocess.

Mitesh Patel pointed to the solution: One should use `communicate` rather than stdout/stdin/stderr!

I don't know how to doctest the issue; but I have a patch that solves the problem.


---

Comment by SimonKing created at 2010-09-03 09:55:55

Replace p.stderr.read()/p.stdout.read() by p.communicate() in the sage-pkg script


---

Comment by SimonKing created at 2010-09-03 09:57:23

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-09-03 23:07:01

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-03 23:07:01

Thanks for tracking this down and fixing it!


---

Comment by mpatel created at 2010-09-15 11:13:07

Resolution: fixed
