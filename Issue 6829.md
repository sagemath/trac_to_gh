# Issue 6829: Implement Manin symbols over number fields

Issue created by migration from https://trac.sagemath.org/ticket/6829

Original creator: cremona

Original creation time: 2009-08-26 21:47:59

Assignee: craigcitro

CC:  mtaranes

Keywords: modular manin symbols

Manin symbols over number fields (related to modular symbols) are used for computing modular forms over those fields.  An implementation valid for general number fields is in prepration by Maite Aranes.

This will be part of a larger project to implement modular forms over number fields in Sage.


---

Attachment


---

Comment by mtaranes created at 2009-08-27 12:59:12

The patch is based on 4.1.1


---

Comment by GeorgSWeber created at 2009-09-21 22:51:20

Just my two cents.

Mathematically: Both the normalization (lines 415 - 455) and the list creation (lines 993 - 1018) look good to me, forming the heart of the module. Index-looking up is done by list searching, well. The other internal functions lift_to_sl2_Ok, make_coprime, psi also look good.

Non-mathematically: This is how more Sage library code should look like. If this applies cleanly to the newest Sage alpha, doctests all pass and have 100% coverage, and the ReST documentation compiles OK (I didn't check, but I'd be surprised if there was any issue), then I'd vote to let this in.


---

Comment by mvngu created at 2009-09-23 01:20:05

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:43:42

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
