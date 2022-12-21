# Issue 3422: Minor typo in docs for zeta_zeros()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-13 23:40:55

Assignee: tba

Michael Yurko reported in http://groups.google.com/group/sage-devel/t/9300a4480eafd679

```
In the reference manual (13.7 Tables of zeros of the Riemann-Zeta
function) it states that zeta_zeros() gives a list of the "first 10000
imaginary parts." However, it should say "first 100000 imaginary
parts" (add a zero to read 100,000). Also, it might serve to mention
that this is an optional package that doesn't come by default.
```




---

Comment by jwmerrill created at 2008-09-14 03:08:18

Changing assignee from tba to jwmerrill.


---

Attachment

This patch fixes the doc to reflect that there is info about 100,000 zeros, but I do not understand how to install this optional package, so can't write documentation regarding that.


---

Attachment

The second patch adds instructions for installing the optional package necessary to make zeta_zeros() work.  I also changed the unusual seealso section into a REFERENCES: section.  If this is accepted, both patches should be applied.


---

Comment by mabshoff created at 2008-09-14 11:29:46

Nice work. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 11:53:32

Merged in Sage 3.1.2.rc3


---

Comment by mabshoff created at 2008-09-14 11:53:32

Resolution: fixed
