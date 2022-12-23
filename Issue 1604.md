# Issue 1604: more locale problems with python exposed by matplotlib

Issue created by migration from https://trac.sagemath.org/ticket/1604

Original creator: was

Original creation time: 2007-12-27 02:12:30

Assignee: was

On a linux box the function setlocale in locale.py sometimes files for some weird locals, which breaks matplotlib.   We patch the python spkg so instead of giving an error in that case, it just uses the default locale.


---

Comment by was created at 2007-12-27 02:16:26

The updated spkg is at 

  http://sagemath.org/packages/standard/python-2.5.1.p11.spkg

If you just do "sage -upgrade" before making the next version of Sage,
you'll get this fixed package.


---

Comment by mabshoff created at 2007-12-29 17:32:23

The promised patch is missing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 06:31:43

The updated spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/python-2.5.1.p12.spkg

contains this fix.


---

Comment by mabshoff created at 2008-01-21 06:31:57

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 06:31:57

Resolution: fixed
