# Issue 2772: Update Singular to 3-0-4-2

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-02 15:33:08

Assignee: malb

This version has GCC 4.3 support.


---

Comment by malb created at 2008-04-04 13:54:45

A new SPKG is available at:

  http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080404.spkg

However, this is not ready for inclusion yet, because of some problem with the GCD. It works correctly from Singular but not correctly via the libSingular interface. I'm working on it.


---

Attachment


---

Comment by malb created at 2008-04-05 16:37:37

A new SPKG is available at:

   http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080405.spkg

which in combination with the attached patch should pass all doctests.


---

Comment by mabshoff created at 2008-04-06 02:18:48

The patch applies cleanly, the spkg compiles cleanly for me on OSX and Linux. Doctests pass. I did find two small issues:

 * I removed spkg-install.orig from the spkg
 * I also removed the comment that SPKG.txt is deprecated from that file.

In total: positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 02:19:03

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 02:19:03

Merged in Sage 3.0.alpha2
