# Issue 7518: flint -- hangs computing certain degenerate case xgcd's

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-23 07:00:21

Assignee: AlexGhitza

CC:  david.kirkby@onetel.net

Observe:


```
sage: Q.<x> = ZZ[]
sage: gcd(Q(2),x^2)
1
sage: xgcd(Q(2),x^2)
<hang forever!>
```


whereas


```
sage: Q.<x> = PolynomialRing(ZZ,implementation="NTL")
sage: type(x)
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
sage: gcd(Q(2),x^2)
1
sage: xgcd(Q(2),x^2)
(4, 2, 0)
```


works fine.



---

Comment by drkirkby created at 2009-12-24 03:45:32

The 'Report Upstream:' field is set to N/A. Is that appropiate, or should it be reported to the flint developers?


---

Comment by was created at 2009-12-24 20:28:22

That Report Upstream button is *annoying*.  I just reported it upstream, and the only option I can select to change from "Not yet reported" is "Reported; little feedback".  Huh?   I want to change it "Reported upstream".  Of course there is no feedback, since I reported it seconds ago.


---

Comment by was created at 2009-12-25 08:33:31


```
from	Bill Hart <goodwillhart`@`googlemail.com>
to	William Stein <wstein`@`gmail.com>
date	Thu, Dec 24, 2009 at 5:23 PM
subject	Re: flint bug maybe
	
hide details 5:23 PM (7 hours ago)
	
Yes, it is a (fairly trivial) flint bug. I'll try and issue a fix later today.

Thanks.

Bill.
```



---

Comment by drkirkby created at 2009-12-25 15:39:49

I don't see why the 'Reported; little feedback' should be annoying. The fact you have reported it is acknowldeged, the fact you have got no feedback is true. 

Once you get some feedback, then update it. It this case, I would have updated it to 'Preported Upstream. Developers acknowldge it's a bug', since at this point in time, there is no fix. 

What I think would be usefully added is 'Reported upstream. Useful feedback'. Sometimes it takes quite a bit of discussion to decide whether its a Sage bug or a bug in the upstream code.


---

Comment by was created at 2009-12-25 18:13:30


```
OK, I persisted with the very slow machine and got flint-1.5.1
released, which fixes this bug. All the test code passes, including
the test function I wrote for the case reported.
-- Bill Hart
```



---

Comment by drkirkby created at 2010-08-23 20:51:42

Is anyone looking up updating the flint package in Sage to cure this bug? According to this ticket, flint 1.5.1 was released 8 months ago. 

Dave


---

Comment by leif created at 2011-09-01 22:46:39

Changing component from basic arithmetic to packages.


---

Comment by leif created at 2011-09-01 22:46:39

Changing assignee from AlexGhitza to tbd.


---

Comment by leif created at 2011-09-01 22:46:39

Replying to [comment:7 drkirkby]:
> Is anyone looking up updating the flint package in Sage to cure this bug? According to this ticket, flint 1.5.1 was released 8 months ago. 
> 
> Dave 

I'm upgrading FLINT to 1.5.2 (not 1.6, at least for the moment, nor 2.x) for a couple of reasons (e.g. failing to build the test suite with MPIR 2.x, cf. #9858, #8664; ARM support, cf. #10328). I had an almost ready spkg last year, but now have to rebase my changes since the p5 has meanwhile become a p9. (There's a lot wrong with this spkg, especially the `makefile`, but also `spkg-install` and even `SPKG.txt`.)

I so far can confirm that the failing example given above works with FLINT 1.5.2, so this ticket can most probably be closed when a new FLINT spkg has been merged.

Stay tuned on #9858.


---

Comment by leif created at 2011-09-01 22:46:39

Changing priority from major to critical.


---

Comment by jdemeyer created at 2013-05-16 08:02:02

Works now.


---

Comment by jdemeyer created at 2013-05-16 08:02:02

Resolution: worksforme
