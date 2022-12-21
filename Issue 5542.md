# Issue 5542: more docstring fixes for permgroup.py

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-03-17 05:45:48

Assignee: tba

Keywords: permgroup.py, docstring

While reviewing the patch on ticket #5536, I noticed that there are more formatting issues in `sage/groups/perm_gps/permgroup.py`. This is a follow up to that ticket.


---

Attachment

The patch *trac_5542-docstring-fixes.patch* fixes formatting problems I found while reviewing ticket #5536. This patch depends on #5536, and the patch at #5536 should be applied first.


---

Comment by jhpalmieri created at 2009-03-17 16:52:26

Looks good, mostly.  I'm attaching a new patch to fix a few issues; positive review for everything else.  (So if my new patch is okay, the whole thing gets a positive review.)


---

Comment by mvngu created at 2009-03-18 09:52:07

For the patch *5542-referee.patch*, everything looks good except for this line:

```
2017	        The normal subgroups of `H = PSL(2,7) \times PSL(2,7)` are
```

The LaTeX macro `\times` is meant to render as a multiplication symbol that looks like this "x". But after applying *5542-referee.patch* on top of *trac_5542-docstring-fixes.patch* and rebuilding the HTML version of the reference manual, the said macro doesn't render as expected; see the rebuilt ref manual at



http://sage.math.washington.edu/home/mvngu/scratch/sage-3.4/devel/sage-5542/doc/output/html/en/reference/sage/groups/perm_gps/permgroup.html#sage.groups.perm_gps.permgroup.PermutationGroup_generic.normal_subgroups



to see what it's rendered as.


---

Comment by jhpalmieri created at 2009-03-18 16:22:20

Should have been `\\times` instead.  Here's a replacement patch.


---

Attachment

OK, the (new) patch *5542-referee.patch* applies fine against Sage 3.4, all doctests passed, the HTML version of the reference manual builds without problems, and the macro `\\times` now renders as expected. The HTML manual page for `sage/groups/perm_gps/permgroup.py` now looks ridiculously beautiful :-)  Positive review.


---

Comment by mvngu created at 2009-03-18 23:33:08

For the record, here's the order in which patches should be applied:
 1. First apply the patch on ticket #5536.
 1. Then apply `trac_5542-docstring-fixes.patch`.
 1. And finally, apply `5542-referee.patch`.


---

Comment by mabshoff created at 2009-03-20 21:20:04

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-20 21:20:04

Resolution: fixed
