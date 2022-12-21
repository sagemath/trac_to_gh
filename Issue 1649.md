# Issue 1649: Updated eclib.spkg to  eclib-20071231.p0.spkg  or later

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-31 23:59:03

Assignee: mabshoff

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/eclib-20071231.p0.spkg

Changelog:
eclib-20071231.p0 (Michael Abshoff)
 * added Cygwin support
 * add spkg-check
 * install headers into $SAGE_LOCAL/eclib
 * delete $SAGE_LOCAL/include/cremona
 * chown $SAGE_LOCAL/include/eclib and files underneath

eclib-20071231 (John Cremona):
 * renamed to eclib
 * allows elliptic curves as input with rational (as opposed to just integer) coefficients.

This spkg still needs fixes to `mwrank.pyx` [expect a patch shortly] and is related to #1058.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-01 00:00:16

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-01 02:15:03

I misunderstood John and the old interface no longer works. I had assumed that we needed to enhance the interface to take advantage of the new capabilities:

```
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
sage/libs/mwrank/wrap.cc: In function ‘char* two_descent_getbasis(two_descent*)’:
sage/libs/mwrank/wrap.cc:246: error: invalid initialization of reference of type ‘const std::vector<Point, std::allocator<Point> >&’ from expression of type ‘std::vector<P2Point, std::allocator<P2Point> >’
sage/libs/mwrank/wrap.cc:159: error: in passing argument 1 of ‘char* point_vector_to_str(const std::vector<Point, std::allocator<Point> >&)’
error: command 'gcc' failed with exit status 1
```


I haven't investigated how much effort it will be to fix this, but since there are more pressing bugs to fix for me I will step back and hope that somebody else will fix this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-04 12:02:48

In http://groups.google.com/group/sage-devel/t/1b3e097ee29e7cf6 John has posted a link to an updated eclib.spkg at

http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20071231.p1.spkg

To quote:

```
This version, which builds on mabshoff's eclib-20071231.p0.spkg,
handles the interface with NTL's ZZ_p class better (using a cached
list of ZZ_pContext's for those who know NTL) which should certailny
be a lot more efficient, and might even solve the problems people had
trying to compile this with gcc-4.3 (which I do not have).

Since other parts of Sage use the ZZ_p class it might be worth using
what I did here (in src/procs/gf.{h,cc}) elsewhere too.  I have a
global object of type map<ZZ,ZZ_pContext> consisting of an in
initially empty list of pairs [p,c] where p is a prime and c is a
ZZ_pContext which stores the internal NTL data for working mod p.
When I need to switch to a new modulus, instead of just calling
ZZ_p::init() each time (which was happening a lot of times for the
same p in programs such as mwrank), I look to see if that p has a
saved context and if so just restore it.  If not, is do ZZ_p::init and
then save the context.  So each prime only gets init'ed once.

It is possible that this will have solved other mysterious problems,
since the NTL documention (see http://www.shoup.net/ntl/doc/ZZ_p.txt)
says

"One should also not presume that things will work properly
if the modulus is changed, but its value happens to be the same---
one should restore the same "context", from either a ZZ_pBak
or a ZZ_pContext object."

Up to now I *had* been making such a presumption.

It is still true that this spkg will not build correctly in Sage 2.9.1
(or even 2.9.2) since there is a small change to the interface which
requires a similar small change to the wrapping code, but this has
been put off at least until after the AMS meeting.  But it should
build fine as a stand-alone package.

John 
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 03:20:11

This spkg should also fix #1650.


---

Comment by mabshoff created at 2008-01-27 18:55:55

Note that an updated spkg by William is at #1650 that fixes the OSX build issue I introduced by fixing the Cygwin build :(

Cheers,

Michael


---

Attachment


---

Comment by was created at 2008-01-27 19:17:17

I wrote "needs review", but I've run the doctests and all pass, and Cremona and
I just worked on this together, so it's had two eyes.


---

Comment by mabshoff created at 2008-01-27 19:56:53

Patch looks good to me. The spkg from #1650 was merged.


---

Attachment


---

Comment by mabshoff created at 2008-01-27 20:16:01

The second patch looks good to me, too. I am doing a `sage -ba` to make sure everything still compiles.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-27 20:20:33

Merged in Sage 2.10.1.rc2


---

Comment by mabshoff created at 2008-01-27 20:20:33

Resolution: fixed
