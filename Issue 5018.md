# Issue 5018: lrs optional package improvements

Issue created by migration from https://trac.sagemath.org/ticket/5018

Original creator: mhampton

Original creation time: 2009-01-18 20:22:03

Assignee: mabshoff

Keywords: lrs, polyhedra, polytopes

In order to move the lrs package closer to being included as a standard package, I have added a couple of tests to the makefile.


---

Comment by mhampton created at 2009-01-18 20:23:05

My current candidate is at:
http://sage.math.washington.edu/home/mhampton/lrs-4.2b.p1.spkg


---

Comment by mabshoff created at 2009-01-19 01:31:58

A couple remarks:

 * the spkg is missing an hg repo. Please check in everything but src
 * SPKG.txt does not conform to the standard - see the SpkgTemplate in the wiki 
 * spkg-install needs to be executable
 * spkg-check is missing, when you add it please run `make check` with it
 * for the make check target: create foo.expected and direct the result from test foo into foo.result. Then diff, i.e. do not create the expected result in the script
 * the makefile should have a make install target
 * the makefile still uses `gcc -O3 -static` - this should be set via CC and CFLAGS for example

Not all of the above have to be fixed to get a positive review from me, but it would be nice to get those all fixed. The missing hg repo and an updated SPKG.txt should *really* be done.

Cheers,

Michael


---

Comment by mhampton created at 2009-01-19 04:17:02

I think I have addressed the concerns above, except that I did not add the CC and CFLAGS macros, because I was not sure how to do that for all the compilation cases in the makefile.  The updated version is that the same link as before.


---

Comment by mabshoff created at 2009-02-02 06:31:36

This spkg is enough of an improvement to warrant a positive review. Much remains to be done, but this can be addressed via subsequent spkgs.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 06:32:47

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 06:32:47

Uploaded in the optional spkg repo in Sage 3.3.alpha4.

Cheers,

Michael
