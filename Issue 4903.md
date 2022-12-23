# Issue 4903: convert sage.calculus.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4903

Original creator: mhansen

Original creation time: 2009-01-01 22:46:01

Assignee: tba




---

Comment by mhansen created at 2009-01-02 03:02:50

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2009-01-02 03:02:50

Patch at http://sage.math.washington.edu/home/mhansen/trac_4903.patch


---

Comment by mhansen created at 2009-01-02 03:02:50

Changing status from new to assigned.


---

Comment by wdj created at 2009-01-02 12:11:12

* In minpoly (around line 1659)


```
+        ``self`` and use PARI's algdep to get a candidate
+        minpoly `f`. If `f(``self``)`,
+        evaluated to a higher precision, is close enough to 0 then evaluate
+        `f(``self``)` symbolically, attempting to prove
+        vanishing. If this fails, and ``epsilon`` is non-zero,
+        return `f` if and only if
+        `f(``self``) < ``epsilon```.
```

is not parsing correctly. See

```
http://sage.math.washington.edu/home/mhansen/sage-3.2.3-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/sage/calculus/calculus.html
```

I guess sphinx is having trouble with the nested quotes?

Another problem with the html conversion is that the footer (in ubuntu seamonkey) in that file is
not offset as blue. (Eg, the next link at the bottom of the page does not appear as it is overwritten by the white page background, but it is there if you mose over it.) It does render correctly in epiphany however. Does anyone but me even use seamonkey?


---

Attachment

I attached a patch which fixes the problem with the nested quotes.

I'm not seeing the problem that you are in Firefox 3.0.


---

Attachment


---

Attachment

I've posted a tiny fix to make doctests pass in sage.calculus.* after sphinxification.


---

Comment by wdj created at 2009-02-22 12:13:31

I looked through 

```
http://sage.math.washington.edu/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/devel/sage/doc/output/html/en/reference/calculus.html
```

and this looks good to me.


---

Comment by mabshoff created at 2009-02-24 17:58:00

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 17:58:00

Merged sage.calculus-final.patch in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 20:15:50

Merged trac4903-tiny-fix.patch in Sage 3.4.alpha0 to fix a doctest failure not in Mike's patch.

Cheers,

Michael
