# Issue 3000: Some packages don't respect the CXX environment variable

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-22 16:43:16

Assignee: mabshoff

CC:  mjo

Packages which seem not to honor CXX environment variable (they use "g++")

```
polybori-0.3.1.p1
rubiks-20070912.p5
sage-3.0.rc1
gfan-0.3.p3
flintqs-20070817.p3
```



---

Comment by PolyBoRi created at 2008-04-22 21:19:55

See #2999 for PolyBoRi,

Regards,
  Alexander


---

Comment by mabshoff created at 2008-04-26 10:45:58

Changing status from new to assigned.


---

Comment by mjo created at 2012-02-27 15:09:57

Changing status from new to needs_review.


---

Comment by mjo created at 2012-02-27 15:09:57

These are fixed or have their own tickets:

 * flintqs: #12428
 * gfan: #7820
 * rubiks: #7036
 * sage: #12443

As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.


---

Comment by ohanar created at 2012-02-27 18:04:58

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-04 21:25:49

Resolution: duplicate


---

Comment by leif created at 2012-03-17 02:12:19

Replying to [comment:3 mjo]:
> These are fixed or have their own tickets:
> 
>  * flintqs: #12428
>  * gfan: #7820
>  * rubiks: #7036
>  * sage: #12443
> 
> As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.

I wouldn't have closed this ticket.  There's at least still Lcalc with its ugly `Makefile`, using `CC` and `CCFLAGS`[sic] for compiling C as well as C++, hardcoding `CC` to `g++`, and even Singular apparently has an instance of a hardcoded `g++`.


---

Comment by leif created at 2012-03-17 11:12:19

Replying to [comment:7 leif]:
> Replying to [comment:3 mjo]:
> > These are fixed or have their own tickets:
> > 
> >  * flintqs: #12428
> >  * gfan: #7820
> >  * rubiks: #7036
> >  * sage: #12443
> > 
> > As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.
> 
> I wouldn't have closed this ticket.  There's at least still Lcalc with its ugly `Makefile`, using `CC` and `CCFLAGS`[sic] for compiling C as well as C++, hardcoding `CC` to `g++`, and even Singular apparently has an instance of a hardcoded `g++`.

Singular (3-1-3-3) is now #12680 (*needs review*).

I've also fixed the Lcalc spkg, but haven't yet opened a ticket for that.


---

Comment by leif created at 2012-03-17 11:30:48

Replying to [comment:8 leif]:
> I've also fixed the Lcalc spkg, but haven't yet opened a ticket for that.

This is now #12681 (soon *needing review*).
