# Issue 9057: Supporting elliptic curves over function fields and their L-functions

Issue created by migration from Trac.

Original creator: salmanhb

Original creation time: 2010-05-26 21:10:31

Assignee: cremona

Keywords: elliptic curves, L-functions, function fields

Sage currently cannot compute L-functions of elliptic curves over function fields. Chris Hall and I have developed Cython code so that Sage can make use of our ELLFF (elliptic curve L-functions over function fields) library (written in C++ with NTL). The next step is to patch this into Sage.


---

Comment by salmanhb created at 2010-05-26 22:54:53

Installed ellff.pyx. This will allow you to compute L-functions of elliptic curves over F_q(t).

WARNING: the interface is surely to change, especially in light of the following ticket:

     [http://trac.sagemath.org/sage_trac/ticket/9054](http://trac.sagemath.org/sage_trac/ticket/9054)


---

Comment by salmanhb created at 2010-05-26 22:54:53

Changing status from new to needs_work.


---

Attachment

Initial patch


---

Attachment

ELLFF now uses FunctionField in #9054


---

Comment by salmanhb created at 2010-05-28 04:34:09

merges initial file with FunctionField functionality


---

Attachment


---

Comment by salmanhb created at 2010-05-28 20:50:52

trac_9057_ellff-part2.patch adds doctests and resolves some bugs with the previous patches.


---

Comment by salmanhb created at 2010-06-03 18:04:28

The requisite SPKG can be found here:

http://sage.math.washington.edu/home/sbutt/ellff/ellff-0.1.spkg


---

Comment by was created at 2010-10-26 22:51:41

This is now in PSAGE: http://code.google.com/p/purplesage/source/checkout
