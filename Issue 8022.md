# Issue 8022: ref manual for 4.3.1: fix warning about misc/attach.rst

Issue created by migration from https://trac.sagemath.org/ticket/8022

Original creator: jhpalmieri

Original creation time: 2010-01-21 06:31:45

Assignee: mvngu

When building the reference manual, I get this warning (among others):

```
.../devel/sage/doc/en/reference/sage/misc/attach.rst:: WARNING: document isn't included in any toctree
```

The fix is easy: delete (by hand) the file `SAGE_ROOT/devel/sage/doc/en/reference/sage/misc/attach.rst`.  (This file is not under revision control, so can't be removed by a patch.)


---

Comment by jhpalmieri created at 2010-01-21 06:31:52

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-31 01:30:39

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-31 01:45:18

Also, `polytope.rst`?  To be sure, do `rm -rf SAGE_DOC/en/reference/sage*` and rebuild...


---

Comment by jhpalmieri created at 2010-01-31 06:26:16

Replying to [comment:3 mpatel]:
> Also, `polytope.rst`?  To be sure, do `rm -rf SAGE_DOC/en/reference/sage*` and rebuild...

Yes, it looks like polytope.rst was removed from the reference manual in #7109.  Let's delete that file, too; I'll change the description of this ticket to reflect this.


---

Comment by mvngu created at 2010-02-01 22:31:49

There are no patches to merge, so I "merged" as follows:

 * `rm -rf SAGE_ROOT/devel/sage-main/doc/en/reference/sage`

For Sage 4.3.2.alpha1, originally the number of warnings for building the reference manual was 157. After following the above deletion step, the total number of warnings dropped down to 155.


---

Comment by mvngu created at 2010-02-01 22:31:49

Resolution: fixed


---

Comment by mvngu created at 2010-02-04 01:36:06

*Correction:* I only removed the file `polytope.rst`:

 * `rm SAGE_ROOT/devel/sage-main/doc/en/reference/sage/geometry/polytope.rst`
