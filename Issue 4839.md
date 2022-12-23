# Issue 4839: update desolve_laplace like #4285 did for desolve

Issue created by migration from https://trac.sagemath.org/ticket/4839

Original creator: jason

Original creation time: 2008-12-20 20:12:20

Assignee: burcin

CC:  mhansen jdemeyer

Make it so that the following works:


```
sage: var('t')
t
sage: x=function('x', t)
sage: soln=desolve_laplace(diff(x,t)+x==1, x, ics=[0,2]) 
sage: soln(3) 
e^-3 + 1
```




---

Comment by wdj created at 2008-12-20 20:39:13

This would be awesome! 

BTW, ICs used with desolve really does not work: from the docstring, you see


```
           sage: x = var('x')
            sage: y = function('y', x)
            sage: de = diff(y,x,2) - y == x
            sage: desolve(de, y)
            k1*e^x + k2*e^(-x) - x
            sage: f = desolve(de, y, [10,2,1]); f
            (e^10*y(10) + 8*e^10)*e^(-x)/2 + (y(10) +12)*e^(x - 10)/2 - x
```

so for some reason 2 is not plugged in for y(10).


---

Comment by AlexGhitza created at 2009-01-22 18:22:49

Changing type from defect to enhancement.


---

Comment by robert.marik created at 2009-10-06 20:02:09

Replying to [comment:1 wdj]:
> BTW, ICs used with desolve really does not work: from the docstring, 

has been fixed in http://trac.sagemath.org/sage_trac/ticket/6479


---

Comment by robert.marik created at 2009-11-08 00:10:39

The desolve_laplace has been fixed together with other things in http://trac.sagemath.org/sage_trac/ticket/6479 and got positive review. Can be closed now as a duplicate.


---

Comment by robert.marik created at 2009-11-08 00:10:39

Changing status from new to needs_info.


---

Comment by kcrisman created at 2009-11-18 18:16:41

To release manager: please see previous comment.


---

Comment by kcrisman created at 2009-12-24 03:28:54

Replying to [comment:5 kcrisman]:
> To release manager: please see previous comment.

Bump; please close.


---

Comment by kcrisman created at 2010-11-04 18:37:26

Bump again - release manager, please close :)


---

Comment by mhansen created at 2010-11-04 19:30:45

Resolution: duplicate


---

Comment by mhansen created at 2010-11-04 19:30:45

Fixed by #6479.


---

Comment by jdemeyer created at 2010-11-04 19:48:27

Replying to [comment:7 kcrisman]:
> Bump again - release manager, please close :)
Next time, just make the ticket reviewed (put it to needs_review asking somebody to confirm to close the ticket).

This way we have a peer-reviewed proposal to close and the release manager will see that the ticket has positive_review.


---

Comment by kcrisman created at 2010-11-04 20:12:09

Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.

Anyway, no problem - but in that case let me change the reviewer!  (I can't do the diacritical mark in Robert's name, though.)


---

Comment by jdemeyer created at 2010-11-04 20:20:21

Replying to [comment:10 kcrisman]:
> Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.
Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager.  I also think it is good to review the fact that the bug is indeed invalid.

> I can't do the diacritical mark in Robert's name, though.
Copy and paste from [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames) :-)


---

Comment by kcrisman created at 2010-11-04 20:28:44

> > Okay, that's different from how we've handled closing of duplicates in the past.   After all, there is nothing to review in this case.
> Well, I myself have gotten complaints about closing tickets (for whatever reason) when not being a release manager. 
Yes, as have I; I think that only having release managers (or possibly experienced non-current release managers like Mike and Minh) actually close the tickets is wise.  

But in this case, you *are* the release manager!   As Robin Williams says in 'Aladdin', "Phenomenal cosmic powers! Itty bitty living space."

> I also think it is good to review the fact that the bug is indeed invalid.

Of course, one should review that a bug is invalid, but in this case it is the duplicate status that is at issue, which is more of a release issue.  Anyway, I don't mind Robert getting more props!
