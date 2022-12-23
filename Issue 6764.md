# Issue 6764: [with patch, needs review]  Independent Set of Reresentatives (uses Linear Programming)

Issue created by migration from https://trac.sagemath.org/ticket/6764

Original creator: ncohen

Original creation time: 2009-08-16 17:06:55

Assignee: rlm

See http://groups.google.com/group/sage-devel/browse_thread/thread/9d9b09274f1eab83/79938a2139ba25d9?lnk=gst&q=isr#79938a2139ba25d9

This patch add the ISR() function for graphs. The Independent Set of Representatives is a generalisation of graph coloring and list coloring, but goes way further ! I tried to take care of the documentation, so you will find some more informations in the docstrings if you need it ! ;-)

This patch uses Linear Programming, so you will have to first install GLPK (just type sage -i glpk 4.38), then the patch AllMIP at #6502 ;-)


---

Comment by ncohen created at 2009-08-31 15:55:32

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann


---

Comment by ncohen created at 2009-09-06 16:32:56

Just updated, everything is ready for review :-)

Thanks again for your help !

Nathann


---

Comment by rlm created at 2009-12-15 16:22:23

rebased for 4.3.rc1


---

Comment by rlm created at 2009-12-15 16:38:01

Changing status from needs_review to needs_work.


---

Attachment

1. The doctest needs to be marked as optional.

2. There should be more examples.

3. Whether or not GLPK is installed, the import `from sage.numerical.mip import MIP` fails. I suppose this is a rather old patch, should `MIP` be `MixedIntegerLinearProgram`?

4. "rebased for 4.3.rc1" means 4.3.rc0 + #7640 + #7674 + #7673, all of which are merged in rc1.


---

Comment by ncohen created at 2009-12-15 16:53:24

This is a rather old patch. I'll update it immediately !


---

Comment by ncohen created at 2009-12-15 18:56:50

Updated !


---

Comment by ncohen created at 2009-12-15 18:56:50

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-15 19:03:54

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-15 19:03:54

You haven't really addressed #2.


---

Comment by rlm created at 2009-12-15 19:04:13

(item 2 not ticket # 2)


---

Comment by ncohen created at 2009-12-16 00:26:56

This one should be better then :-)


---

Comment by ncohen created at 2009-12-16 00:26:56

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by rlm created at 2009-12-16 02:42:33

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-20 07:26:57

Resolution: fixed
