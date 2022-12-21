# Issue 3792: fix Sage build when there is a broken systemwide freetype library

Issue created by migration from Trac.

Original creator: certik

Original creation time: 2008-08-08 20:05:52

Assignee: mabshoff

The problem and fix is in this thread:

http://groups.google.com/group/sage-support/browse_thread/thread/d1c8996964802ab1


what remains to be done is to extract this fix, create a patch and new spkgs.


---

Comment by certik created at 2008-08-18 12:21:49

Here are the fixed spkg:

http://sage.math.washington.edu/home/ondrej/spkg/matplotlib-0.91.1.p5.spkg
http://sage.math.washington.edu/home/ondrej/spkg/gd-2.0.33.p5.spkg

Please don't just copy them, you need to extract it and copy the sage-install script. With matplotlib, that's all that is needed, with gd, you need to get a new gd-2.0.35 from:

http://www.libgd.org/releases/

and copy it to the src.


---

Comment by mabshoff created at 2008-08-27 09:26:47

Review:

 * matplotlib-0.91.1.p5.spkg: this is the right fix and I will forward port it to the matplotlib-0.98.spkg.
 * gd-2.0.33.p5.spkg: this is also the correct fix and I will port it to the current gd-2.0.35.spkg

Aside from that everything else for a properly upgraded spkg is wrong, but I guess since nobody ever taught you you did not know :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 09:30:39

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-27 09:30:39

Resolution: fixed


---

Comment by certik created at 2008-08-27 09:42:47

Yes, I know, it was a quick hack to get things working, but just to be sure you don't just copy the spkg, I wrote literally, please don't copy it, extract it. :)

Thanks Michael!
