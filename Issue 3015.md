# Issue 3015: introspecting Cryto.DES using DES?? should throw an error message instead of displaying binary junk

Issue created by migration from https://trac.sagemath.org/ticket/3015

Original creator: yi

Original creation time: 2008-04-24 03:54:06

Assignee: was

In sage-3.0 on OSX and linux (sage.math.washington.edu) if you do the following:

  sage: from Crypto.Cipher import DES
  sage: DES??

You get a bunch of binary garbage on your screen. I tried the same thing in vanilla ipython and it correctly told me that it could not open the source file.


---

Comment by mhansen created at 2013-07-22 16:11:46

Resolution: invalid


---

Comment by mhansen created at 2013-07-22 16:11:46

I get an error now instead of binary junk.  I think this was probably fixed with the new IPython update.
