# Issue 1033: new biopython optional package

Issue created by migration from https://trac.sagemath.org/ticket/1033

Original creator: mhampton

Original creation time: 2007-10-30 01:04:22

Assignee: was

Keywords: biopython

Biopython 1.44 has been released.  An spkg is available at:
http://www.d.umn.edu/~mhampton/biopython-1.44.spkg


---

Comment by was created at 2007-11-01 02:59:51

Mabshoff and I made some changes to this package:
   * got rid of the stupid "have to hit return thing" (by hacking setup.py)
   * shrunk the package from 21MB to 3.7MB by deleting some pdfs and using compression.
   * added an .hg repository as per the package spec. 

Anyway, this is now posted.


---

Comment by was created at 2007-11-01 02:59:56

Resolution: fixed
