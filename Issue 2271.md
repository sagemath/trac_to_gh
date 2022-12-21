# Issue 2271: Include Antti Ajanki's DLX library

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-02-22 23:27:49

Assignee: mhansen

The Dancing Links algorithm (DLX) is sweet.  It solves the Exact Cover problem with the quickness.

Arguments for including Ajanki's code:
    1) It's the only Python implementation of DLX I've seen.
    2) I emailed the author, who happily added the "or later" bit after the GPL2
    3) With my Sage Matrix -> DLXMatrix code (plus docstrings to everything I
added), the file dlx.py is only 8kB!
    4) It will resolve tickets #1311 and #1313


---

Comment by boothby created at 2008-02-22 23:27:56

Changing type from defect to enhancement.


---

Attachment


---

Comment by was created at 2008-02-22 23:33:49

+1 to include this in Sage.

I haven't formally refereed it.

You should just attach a single plain text patch instead of an hg bundle.


---

Comment by boothby created at 2008-02-23 20:52:09

Oops, I forgot to add the functions to all.py, so the tests fail.  New patch up in a few.


---

Attachment

This patch (although awesome) doesn't quite obey the new doctest-for-every-function rule, since the following functions do not have doctests:

 1. `walknodes`
 1. `constructmatrix`
 1. `covercolumn`
 1. `uncovercolumn`
 1. `dosearch`
 1. `solve`


---

Attachment


---

Comment by boothby created at 2008-02-25 20:07:42

2271_doctests.patch implements world peace, washes your dishes, and makes coffee before your alarm goes off in the morning.  It's truly amazing.  Also, it contains doctests for everything in sight, reworks the DLXMatrix class to be a real python generator class, and implements an iterative formulation of DLX.

In the creation of these doctests, I have discovered a wondrous resolution of P vs. NP, but the proof was too long to justify appending to the patch.


---

Comment by rlm created at 2008-02-25 20:12:22

As well as a round of applause.


---

Comment by mabshoff created at 2008-02-25 20:32:53

Replying to [comment:7 boothby]:
> 2271_doctests.patch implements world peace, washes your dishes, and makes coffee before your alarm goes off in the morning.  It's truly amazing.  Also, it contains doctests for everything in sight, reworks the DLXMatrix class to be a real python generator class, and implements an iterative formulation of DLX.
> 
> In the creation of these doctests, I have discovered a wondrous resolution of P vs. NP, but the proof was too long to justify appending to the patch.
> 

I guess you should have written it in the margins :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-25 20:35:35

Resolution: fixed


---

Comment by mabshoff created at 2008-02-25 20:35:35

Merged 2271_adds_DLX.patch and 2271_doctests.patch in Sage 2.10.3.alpha0 - w00t
