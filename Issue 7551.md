# Issue 7551: Remove all Fortran binary compilers except OS X.

Issue created by migration from https://trac.sagemath.org/ticket/7551

Original creator: drkirkby

Original creation time: 2009-11-28 22:22:58

Assignee: was

CC:  was

The package fortran-20071120.p9 has Fortran compilers for various systems. William Stein said:

http://groups.google.com/group/sage-devel/msg/b4cf0f10ed040d5d?hl=en

_"I think in sage-4.3 on, we should *only* include fortran compilers for OS X, and *nothing* else."_

I've looked at the fortran package, with a view to removing these, but it looks an quite a complex spkg-install, and since William is listed as the maintainer, I've assigned this to him. Feel free to unassign yourself William, but I think you are probably the best person for this. 

Dave 


---

Comment by GeorgSWeber created at 2009-12-01 21:22:44

This ticket looks like a doublette to

#7485:
make fortran a prerequisite on all platforms except OS X. Remove g95 binaries from Sage


---

Comment by drkirkby created at 2009-12-06 10:44:51

Hi George, 

you are correct, this ticket is identical to William's "make fortran a prerequisite on all platforms except OS X. Remove g95 binaries from Sage" #7485 which he has in fact marked as "critical". It's best if William resolves this, as he has a better understanding of this Fortran issue. I've cc'ed William, and closed this as a duplicate of #7485.


---

Comment by drkirkby created at 2009-12-06 10:44:51

Resolution: duplicate


---

Comment by was created at 2009-12-06 15:34:57

> It's best if William resolves this, as he has a better understanding 
> of this Fortran issue. 

It's best if anybody does this.  Don't assign it to me, since I might never find time to actually do it.    In fact, it's best if somebody else does this, since then the number of people that have an understanding of the Fortran issue increases. :-)

William
