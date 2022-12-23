# Issue 2641: replace guava 3.1 by guava 3.3

Issue created by migration from https://trac.sagemath.org/ticket/2641

Original creator: wdj

Original creation time: 2008-03-22 01:29:55

Assignee: rlm

There is a significantly improved version of GUAVA (a GAP package) available.
The new tarball is at
http://sage.math.washington.edu/home/wdj/guava/guava3.3.tar.gz
This new version has a new C code function for (quickly) computing the
minimum distance of binary and ternary codes (accessed via the new GUAVA function MinimumWeight), and also includes Brouwer's patch which (I'm told) fixes some or all the memory problems which Leon's code suffered. The GUAVA part also has many new functions, especially new code constructions.



---

Comment by wdj created at 2008-03-30 16:02:20

This new gap version has been posted to
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.p3.spkg
It loads fine on sage 2.10.4 (using sage -f) and passes sage -testall


---

Comment by rlm created at 2008-03-30 17:38:45

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-03-31 14:04:45

David: the spkg looks good. The only thing you didn't do was checking in the changed spkg-install and SPKG.txt into the repo. I did that and that spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha0/gap-4.4.10.p3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-31 14:06:31

Resolution: fixed


---

Comment by mabshoff created at 2008-03-31 14:06:31

Merged in Sage 3.0.alpha0
