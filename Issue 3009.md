# Issue 3009: remove spaces after continuation characters "\"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-04-23 20:45:37

Assignee: tba

*	John H Palmieri reports:

In the section of the tutorial on 3d plotting,

  <http://sagemath.org/doc/html/tut/node22.html>

the continuation characters "\" all have spaces after them, which
messes up cutting and pasting.  Also in the section on Maxima,

  <http://sagemath.org/doc/html/tut/node54.html>

two of the backslashes have spaces after them (in the Mobius strip and
the Klein bottle examples).

The same thing happens half a dozen times in "SAGE Constructions".

I've only searched the tutorial and the constructions documentation
for this issue (by searching the files "tut.tex" and "const.tex"); I
haven't looked at the rest of the documentation. 


---

Attachment


---

Comment by jwmerrill created at 2008-09-14 06:10:20

I did a regex search on all the tex documentation and all the docstrings for the pattern "\\[\ ]+$" and replaced all the appropriate matches (filtered by eye).  The changes are separated into patches for the docstrings and patches for the tex documentation.  If this is accepted, both patches should be applied.


---

Comment by jwmerrill created at 2008-09-14 06:10:20

Changing assignee from tba to jwmerrill.


---

Comment by mabshoff created at 2008-09-14 11:33:21

Patches look good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 11:53:18

Merged in Sage 3.1.2.rc3


---

Comment by mabshoff created at 2008-09-14 11:53:18

Resolution: fixed
