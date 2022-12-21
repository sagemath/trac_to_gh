# Issue 1130: [with patch] point counting for elliptic curves over non-prime finite fields

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-08 22:16:45

Assignee: malb

The user has three new options of finite extension fields:
 1. "legendre" - as the name implies: using Legendre symbols

```
sage: k.<a> = GF(3^10)
sage: E = EllipticCurve(k,[k.random_element() for _ in range(5)])
sage: time E.cardinality('legendre')
CPU times: user 0.39 s, sys: 0.05 s, total: 0.44 s
Wall time: 0.44
58997
```


 1. "bsgs" - using the Baby-Step Giant-Step algorithm

```
sage: time E.cardinality('bsgs')
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
58997
```


 1. "heuristic" - use "legendre" if q<100 (as in mwrank) and "bsgs" else

```
sage: time E.cardinality()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02
58997
```


Neither of these will win any speed records but it is *much* better than the naive algorithm used before.


---

Attachment


---

Comment by robertwb created at 2007-11-18 09:11:09

This seems to rely on an earlier patch. (#1120?) Couldn't apply, but mostly looks good. 

One concern I have that the use of the hasse bound may not be enough for extremely small cardinality (maybe I haven't thought this through enough). It isn't used there by default of course. Very clean implementation of the algorithm though!


---

Comment by malb created at 2007-11-18 15:45:35

David Harvey on [sage-devel]:

```
I'm very concerned about this patch. It is not the case that the LCM
of the orders of all elements of E(GF(q)) will equal the order of E 
(GF(q)). I haven't tried the code, but if I understand the code
correctly, it will go into an infinite loop on such cases, and it may
well give incorrect results in other cases.
```



---

Comment by malb created at 2007-11-18 15:47:26

my reply:

```
Yes, it should not go in, my bad, sorry. I quickly hacked to together
the algorithm in "Elliptic Curves" by Lawrence Washington and 
apparently screwed up badly on the way. He writes:

"""
7. If we are looking for the #E(F_q), then repeat steps (1)-(6)  
[finding the order of a point, malb] with randomly chosen points 
in E(F_q) until the greatest common multiple of the orders divides
only one integer N with q + 1 -2*sqrt(q) <= N <= q + 1 + 2*sqrt(q). 
Then N = #E(F_q).
"""

Apparently I overread the 'divides' part. Also, what is a 
'greatest common divisor'?
```



---

Comment by malb created at 2007-11-18 15:47:58

and David again:


```
I still don't believe this algorithm.

Look at this example:

sage: K.<a> = GF(3^4)
sage: K.polynomial()
a^4 + 2*a^3 + 2
sage: E = EllipticCurve(K, [2*a^2 + 2*a + 2, 2*a^3 + 2*a + 1])
sage: points = E.points()
sage: len(points)
100
sage: LCM([P.order() for P in points])
10

The hasse bound says the the number of points must be in [64, 100].  
But if the best we can do is show divisibility by 10, that's not  
enough information: it could be 70, 80, 90, or 100.

Does Washington place any other restrictions on the finite field or  
on the curve?
```



---

Comment by cremona created at 2007-11-20 18:36:35

David is right that the lcm of the orders of the points does not give the group order, it only gives the exponent of the group.  But that's not what the algorithm described above (by malb) said!  The algorithm says that the group order is the only multiple of that lcm which lies in the Hasse interval.  I believe that to be the case, with a finite number of exceptional fields F_q, as in my posting to sage-devel of 2007-11-20.

jec


---

Comment by was created at 2007-12-21 09:21:21


```

> What's the latest on
>
> http://trac.sagemath.org/sage_trac/ticket/1130
>
> It looks to me like David Harvey pointed out that the algorithm was
> maybe wrong.  It's unclear if
> something needs to be done or not after quickly looking at the
> comments.    Is all that needs to
> happen for malb to make another patch that incorporates the table the
> John mentions in his last
> comment?

Since the code in question was only determining the group
order, not structure, as long as the table of exceptions is dealt with
properly the basic algorithm should work.

By the way, Larry Washington is currently preparing a second edition
of his book and he is planning to incorporate this correction,
attributing it to me and David Harvey.

John
```



---

Comment by cremona created at 2008-02-15 09:44:34

extra functionality for e.c.s over non-prime finite fields


---

Attachment

New patch fixes this and other issues (#1120, #262, even #29), providing full support for elliptic curves over non-prime finite fields, including intelligent point-counting (including over extension fields), group structure, disctrete log, and more.  All functions fully doctested.


---

Comment by ncalexan created at 2008-02-16 18:47:05

The attached ncalexan-1 bundle fixes a few small issues and formats docstrings as per the Sage standard.  Still to come: removing debug output.


---

Attachment


---

Attachment

addition minor fixes


---

Comment by cremona created at 2008-02-16 20:27:41

Thanks to Nick for tidying up my patch.

Only one comment:  while I approve of separating out the point counting for j=0 and j=1728 as done here, I don't think that the name "supersingular j invariant" is right here.  Curves are supersingular iff the cardinality is coprime to the characteristic (with many many equivalent definitions), which is not the same thing.

Hence I would suggest changing the name of that function.

I have added a new patch 8312.patch which is to applied along with all the previous ones, and fixes a few rather minor things.


---

Attachment

This bundle should apply to a clean sage-2.10.2.alpha0 and supersedes everything but malb's bsgs code, which is not ready for application.


---

Attachment


---

Comment by mabshoff created at 2008-02-16 21:52:06

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 21:52:06

Merged 1130-jcremona-ncalexan-final.patch in Sage 2.10.2.alpha1 - credit in the official log did get screwed up, so my apologies to John & Nick.

Cheers,

Michael
