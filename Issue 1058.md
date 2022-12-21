# Issue 1058: the mwrank interface barfs on bad input

Issue created by migration from Trac.

Original creator: moretti

Original creation time: 2007-11-02 00:17:02

Assignee: was

Keywords: mwrank

If give mwrank any invalid input, the running process quits, and you get a pexpect error, since Sage never restarts mwrank:

# the a-list needs to be all integers
sage: E = EllipticCurve( [0, 0, 0, 0, -675/4])
sage: E.rank()
Exception (click to the left for traceback):
...
# this should be valid
sage: F = EllipticCurve( [0, 0, 1, 0, -169])
# ... but calling mwrank again makes everything fail
sage: F.rank()
Exception (click to the left for traceback):
...


---

Comment by moretti created at 2007-11-02 00:17:49

Changing assignee from was to moretti.


---

Comment by cremona created at 2007-11-21 10:56:35

Changing assignee from moretti to cremona.


---

Comment by cremona created at 2007-11-21 10:56:35

There are two separate things here.

First:  it would be entirely reasonable to expect mwrank to allow rational input and not just integer.  At the moment (2007-11-21) that is not supported, but it could be, and I hope to add that functionality when sorting out the more serious #1233.

Second:  The wrapper which sends elliptic curves to mwrank attempts to coerce the coefficients to ints.  (This is what causes the above examples to fail).  But it also seems to have some silly (though documented) side-effects, such as 

```
mwrank_EllipticCurve([1.2,3.4])
y^2 = x^3 + x + 3
```

where the floating point inputs have been rounded down.  This behaviour has no conceivable use, so I would suggest changing the wrapper to require the inputs to be rational.


---

Comment by cremona created at 2007-12-31 16:20:27

eclib-20071231.spkg  is an updated version of cremona*.spkg which allows elliptic curves as input with rational (as opposed to just integer) coefficients.

The Sage interface to the library functions for mwrank (etc) will need to be adapted to handle this.  I expect that is best done as part of the complete rewrite of the Sage-mwrank interface which WAS recently mentioned as desirable.

The new package may be downloaded from http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20071231.spkg

John Cremona


---

Comment by mabshoff created at 2007-12-31 17:44:30

I am looking into this. The upgrade will be non-trivial since we potentially need to delete old headers, fix some includes in the interface and so on. But I think it will be merged in 2.9.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-01 00:00:09

An updated eclib.spkg can be found at:

http://sage.math.washington.edu/home/mabshoff/eclib-20071231.p0.spkg

Changelog:

 * added Cygwin support
 * add spkg-check
 * install headers into $SAGE_LOCAL/eclib
 * delete $SAGE_LOCAL/include/cremona
 * chown $SAGE_LOCAL/include/eclib and files underneath

This spkg breaks compilation of `mwrank.pyx` for now, expect a patch shortly. Since the Sage interface needs updates I split the spkg update off to #1649. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-02 08:33:22

Ok, I tried fixing the interface problems, but it isn't as simple as I thought.

Giving up for now, I need to fix other, more urgent bugs for this release cycle.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-27 20:19:06

Patch passes doctests. Note that the patch needs the updated eclib.spkg and the patches from #1649 to work. Second Positive review.


---

Comment by mabshoff created at 2008-01-27 20:19:24

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 20:19:24

Merged in Sage 2.10.1.rc2
