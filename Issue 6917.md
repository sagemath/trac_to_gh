# Issue 6917: [with patch] Minkowsky sum sould work with polyhedra and not only with polytopes

Issue created by migration from https://trac.sagemath.org/ticket/6917

Original creator: sbarthelemy

Original creation time: 2009-09-10 12:48:39

Assignee: mhampton

The attached patch makes Minkowsky sum handle unbounded polyhedra.

However, as a side effect, it makes bug #6915 blatant, thus doctests don't pass anymore.


---

Attachment


---

Comment by mvngu created at 2009-09-10 18:06:42

Is this ready for review? If so, please change the summary to "[with patch, needs review]".


---

Comment by mhampton created at 2010-04-03 14:43:09

I believe this patch is unnecessary because of #7109, which fixed a lot of related problems.


---

Comment by mhampton created at 2010-04-03 14:43:09

Resolution: fixed
