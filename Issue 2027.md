# Issue 2027: PolyBoRi.spkg: add one line patch to fix memleak

Issue created by migration from https://trac.sagemath.org/ticket/2027

Original creator: mabshoff

Original creation time: 2008-02-02 03:36:26

Assignee: mabshoff

RPW applied Michael Brickenstein's patch to

http://coderpunks.org/tmp/polybori-0.1-r7.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 03:51:23

To be more precise about the changelog:

 * pulled in changes from PolyBoRi's SF CVS repo for a memleak fix in nf.cc
 * fixes to the comments. claims about potential patents were removed by PolyBoRi authors.

Unfortunately this increased the spkg size by 2 mb. Once we update to PolyBoRi 2.0 we should consider resetting the hg changelog. I also checked in some outstanding small changes in `spkg-install`.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-02 05:20:07

Spkg compiles and passes `-testall` on OSX and Linux.


---

Comment by mabshoff created at 2008-02-02 05:20:50

Merged in Sage 2.10.1.rc5


---

Comment by mabshoff created at 2008-02-02 05:20:50

Resolution: fixed
