# Issue 5849: Update MPIR to 1.1.1

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-22 03:56:58

Assignee: mabshoff

MPIR 1.1.1 is about to be released fixing a couple small issues that in rare circumstances can cause trouble, i.e. when a pathscale compiler is installed on x86-64. 

While we are at it: Make sure to select generic x86-64 code since right now we build code using lahf on sage.math that some early P4s did not have as mentioned on #5284. Use the SAGE_SIMD_FLAG flag to decide what to do.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 03:57:03

Changing status from new to assigned.


---

Comment by mhampton created at 2009-04-24 12:54:50

Changing priority from major to critical.


---

Comment by mhampton created at 2009-04-24 12:54:50

I would like to add that this is extremely important for me, since I cannot build sage-3.4.1 on my laptop, which is what I usually develop on.


---

Comment by mabshoff created at 2009-04-30 07:47:18

The spkg is at 

   http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/rc0/gmp-mpir-1.1.1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 09:42:51

Ok, bumping back to 3.4.2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 09:42:51

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2009-05-01 00:41:20

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-01 00:41:20

Resolution: fixed
