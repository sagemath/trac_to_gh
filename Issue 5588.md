# Issue 5588: [with patch, needs review] developer's guide: more information about docstrings

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-23 04:35:58

Assignee: jhpalmieri

Keywords: developer

The attachment does the following things:

1. It says that the Sage style for typesetting the standard rings (ZZ, CC, etc.) is to use mathbf, not mathbb.

2. It discusses trying to achieve a balance between the appearance of the docstring in interactive help vs. in the reference manual.

3. In the paragraph starting "Finally", it mentions some nonstandard macros available for use in docstrings.  This part depends on #5555.

4. It mentions that methods which start with an underscore don't appear in the reference manual, and this should be taken into consideration when writing documentation. The example in this part depends on #5529.



---

Comment by malb created at 2009-03-23 10:02:39

Replying to [ticket:5588 jhpalmieri]:
> 1. It says that the Sage style for typesetting the standard rings (ZZ, CC, etc.) is to use mathbf, not mathbb.

I wonder if that was a conscious decision or whether it is just as it is (I personally prefer mathbb over mathbf).


---

Comment by jhpalmieri created at 2009-03-24 16:50:20

I happen to prefer mathbf, but I was basing this on the latex methods for ZZ, RR, etc., and also on the contents of the file SAGE_ROOT/sage/doc/common/macros.tex, which (in the old version of the documentation) was available for use in the docs.  The consistency among ZZ, RR, etc., led me to believe that it was a conscious decision, but I don't know this for a fact.  Of course, both mathbb and mathbf are used in the code many times...

Let's see what people on sage-devel think.


---

Comment by jhpalmieri created at 2009-03-25 23:36:34

Let's delay this one for a while.  If #5610 gets in, then I'll need to revise the stuff about mathbf anyway...


---

Attachment

Now that #5610 is in (as of 3.4.2.alpha0), here's a version of the patch which is ready for review.


---

Comment by cremona created at 2009-04-29 11:57:57

The patch applies fine to 3.4.2.alpha0 and the docs build and read well.


---

Comment by mabshoff created at 2009-04-30 00:59:35

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 00:59:35

Resolution: fixed
