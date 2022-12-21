# Issue 8942: failing calculation with limit

Issue created by migration from Trac.

Original creator: casamayou

Original creation time: 2010-05-10 09:32:39

Assignee: burcin

CC:  jason mvngu mhansen

Keywords: limit

In all three calculations below, the first result is false, whereas in a previous version of Sage, he returned Und what is the correct answer.


```
sage:f(x) = (cos(pi/4-x) - tan(x)) / (1 - sin(pi/4+x))
sage:limit(f(x), x = pi/4) 
+Infinity
sage: limit(f(x), x = pi/4, dir='plus')            
-Infinity
sage: limit(f(x), x = pi/4, dir='minus')           
+Infinity
```



---

Comment by kcrisman created at 2010-05-26 20:13:48

This was fixed when we improved our recognition of Maxima's unsigned infinity.

```
sage: sage: limit(f(x), x = pi/4, dir='minus')           
+Infinity
sage: sage: limit(f(x), x = pi/4, dir='plus')            
-Infinity
sage: sage:limit(f(x), x = pi/4) 
Infinity
```

So I guess this can be closed?  Or should we whip up a patch to document this...?


---

Comment by casamayou created at 2010-05-27 15:49:02

Resolution: fixed


---

Comment by casamayou created at 2010-05-27 15:49:02

Replying to [comment:1 kcrisman]:
> This was fixed when we improved our recognition of Maxima's unsigned infinity.
> {{{
> sage: sage: limit(f(x), x = pi/4, dir='minus')           
> +Infinity
> sage: sage: limit(f(x), x = pi/4, dir='plus')            
> -Infinity
> sage: sage:limit(f(x), x = pi/4) 
> Infinity
> }}}
> So I guess this can be closed?  Or should we whip up a patch to document this...?

This can be closed. Thanks a lot !


---

Comment by kcrisman created at 2010-05-27 15:55:06

Changing status from closed to new.


---

Comment by kcrisman created at 2010-05-27 15:55:06

Resolution changed from fixed to 


---

Comment by kcrisman created at 2010-05-27 15:55:06

Thanks.  One thing to point out is [http://www.sagemath.org/doc/developer/trac.html#closing-tickets](http://www.sagemath.org/doc/developer/trac.html#closing-tickets), so that in theory only the release manager should close a ticket.  For instance, we might want to document this somewhere (which is what I was really asking about).  

I will now violate that same web page by re-opening it; since it hasn't actually been merged (nothing to merge) hopefully that is ok, Minh or Mike :)


---

Attachment

Based on 4.4.2


---

Comment by kcrisman created at 2010-05-27 16:05:46

If we want more documentation that we have fixed this, here it is.  Ready for review.


---

Comment by kcrisman created at 2010-05-27 16:05:46

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-07-12 12:43:27

positive review (I've checked that all doctests still pass).

A small comment: maybe the documentation could say more explicitly that the output `Infinity`
indicates a complex infinity, whereas `+Infinity` means plus infinity.

By the way, there is a problem since Sage parses `Infinity` as `+Infinity`:

```
sage: Infinity
+Infinity
sage: Infinity == +Infinity
True
sage: a=limit(1/x, x=0)
sage: a == +Infinity
True
```

but this could be in a different ticket.


---

Comment by zimmerma created at 2010-07-12 12:43:27

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-07-12 12:49:44

> but this could be in a different ticket. 

see #9480


---

Comment by mpatel created at 2010-07-20 10:04:03

Resolution: fixed
