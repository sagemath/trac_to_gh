# Issue 3926: [with spkg, needs review] fix Macaulay2 building

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-22 12:29:12

Assignee: mabshoff

I've uploaded a new SPKG for M2 to:

  http://sage.math.washington.edu/home/malb/spkgs/macaulay2-1.1-r7210.p1.spkg

which fixes a couple of compilation problems:

 * UNAME might not be defined
 * some standard headers are not included in `overflow.hpp`


---

Comment by mabshoff created at 2008-08-25 04:58:37

Positive review. A couple remarks:

 * The fixes malb did should go upstream.
 * I fixed the boehm_gc and gdbm detection code since it only works for default spkgs and not optional ones - my bad.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 04:59:40

Oops, I forgot to mention that the updated spkg is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/macaulay2-1.1-r7210.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 04:59:53

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-25 04:59:53

Resolution: fixed
