# Issue 3871: crap in SAGE_ROOT; extending #3759

Issue created by migration from https://trac.sagemath.org/ticket/3871

Original creator: was

Original creation time: 2008-08-15 10:04:25

Assignee: mabshoff

These are still left in SAGE_ROOT after testlong:

`sage.png, sage0.png, sage1.png, sage2.png, sage3.png, sage4.png, sage5.png and sage6.png`

See #3759


---

Comment by boothby created at 2009-01-22 18:55:31

I didn't testlong, but I did a full test, and found that /rings/polynomial/polynomial_element.pyx creates two images around line 228


```
        EXAMPLES:
            sage: x = polygen(GF(389))
            sage: plot(x^2 + 1, rgbcolor=(0,0,1)).save()
            sage: x = polygen(QQ)
            sage: plot(x^2 + 1, rgbcolor=(1,0,0)).save()
```



---

Attachment

The attached patches just fix all the cases of saving images to a file that I could find using search_src('...').  I applied it and ran --long doctests, and everything passes.


---

Attachment


---

Comment by mabshoff created at 2009-01-24 12:27:48

Positive review. Hopefully this will be the last of the annoying code that dumps pngs into $SAGE_ROOT.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 12:33:25

Note that the last hunk from the second patch in sage/schemes/elliptic_curves/lseries_ell.py is also in the first patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 13:16:23

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 13:16:23

Resolution: fixed
