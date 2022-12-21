# Issue 8237: Sage does not recognize Maxima's complex ininity

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-02-11 17:09:35

Assignee: burcin

CC:  robert.marik

As subject says:

```
sage: maxima('inf').sage()
+Infinity
sage: maxima('infinity').sage()
+Infinity
```


From Maxima manual

```
Constant: inf
    inf represents real positive infinity.

Constant: infinity
    infinity represents complex infinity.

Constant: minf
    minf represents real minus (i.e., negative) infinity. 
```

As a cosequence, Sage fails to evaluate limit of 1/x at x=0. Maxima gives correct result (complex infinity)

```
sage: maxima('limit(1/x,x,0)')
infinity
sage: maxima('limit(1/x,x,0)').sage()
+Infinity
sage: limit(1/x,x=0)
+Infinity
sage: maxima('limit(1/x,x,0,plus)')
inf
sage: maxima('limit(1/x,x,0,plus)').sage()
+Infinity
```



---

Comment by robert.marik created at 2010-02-11 17:16:31

reported on [sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/350697c3650a3b76)


---

Comment by robert.marik created at 2010-02-11 18:22:17

Changing assignee from burcin to robert.marik.


---

Comment by robert.marik created at 2010-02-11 18:22:45

Changing assignee from robert.marik to burcin.


---

Comment by kcrisman created at 2010-02-11 19:51:52

Right now, there doesn't seem to be a lot of distinction in Sage between unsigned and signed infinity, though of course as you point out there should be.  From sage.rings.infinity.py:

```
    Note: the shorthand oo is predefined in Sage to be the same as
    +Infinity in the infinity ring. It is considered equal to, but not
    the same as Infinity in the UnsignedInfinityRing::
    
        sage: oo
        +Infinity
        sage: oo is InfinityRing.0
        True
        sage: oo is UnsignedInfinityRing.0
        False
        sage: oo == UnsignedInfinityRing.0
        True
    
```

There is unsigned_infinity, but the following seems problematic:

```
sage: unsigned_infinity
Infinity
sage: Infinity
+Infinity
```

What the heck?


---

Attachment

fix conversion of different infinities back from maxima


---

Comment by burcin created at 2010-02-11 22:02:17

Changing status from new to needs_review.


---

Comment by burcin created at 2010-02-11 22:02:17

I uploaded a patch, please review.


---

Comment by kcrisman created at 2010-02-12 02:38:21

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-02-12 02:38:21

Looks good, but does it duplicate some of lines 1841ff of sage/calculus/calculus.py?

```
from sage.rings.infinity import infinity, minus_infinity
register_symbol(infinity, dict(maxima='inf'))
register_symbol(minus_infinity, dict(maxima='minf'))
```

Since 

```
sage: type(infinity)
<class 'sage.rings.infinity.PlusInfinity'>
sage: type(SR(infinity))
<type 'sage.symbolic.expression.Expression'>
```

my guess is that, at least for completeness, calculus.py should also import unsigned_infinity and have a line added with 

```
register_symbol(unsigned_infinity, dict(maxima='infinity'))
```


Also, my taste in doctests is to also include the original example, not (only) the underlying cause:

```
sage: limit(1/x,x=0)
Infinity
sage: limit(1/x,x=0,dir='above')
+Infinity
sage: limit(1/x,x=0,dir='below')
-Infinity
```

which of course works great now.  These are very minor quibbles, of course, but might as well be done.

Also, in doctesting it doesn't like sage: sage: as the prefix (though one could argue this is a bug itself), and 

```
devel/sage/sage/calculus/functional.py", line 313:
    sage: lim(1/x, x=0)
Expected:
    +Infinity
Got:
    Infinity
```



---

Comment by burcin created at 2010-02-20 14:30:17

apply only this patch


---

Attachment

I was trying to get the first patch out quickly, so it ended up being too sloppy. I hope attachment:trac_8237-maxima_infinity.take2.patch is cleaner. :)

I think it's more natural to put the maxima conversions for different infinities in `sage/symbolic/constants.py` where all the other constants are declared, so I removed the lines in `calculus.py`. I also added doctests with `limit(1/x, ...)`.


---

Comment by burcin created at 2010-02-20 14:36:11

Changing status from needs_work to needs_review.


---

Comment by rossk created at 2010-02-24 12:40:10

By exercising a number of arithmetic use cases, viz. 

```
for k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):
    print k, k + Infinity , k + +Infinity, k + -Infinity

for k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):
    print k, Infinity -k , +Infinity -k, -Infinity -k

for k in (1, 1.0, 1/2, x, 1+I, -1, -1.0, -1/2, -x, -1-I):
    print k, k / Infinity , k / +Infinity, k / -Infinity

for k in (1, 1.0, 1/2, x, -1, -1.0, -1/2, -x):
    print k, k * Infinity , k * +Infinity, k * -Infinity
```

there were a small number of things to note


(a) the same answer resulted, regardless of whether (unsigned) Infinity or +Infinity was used. Query: Just to make sure we are getting the results we designed for...  Currently +Infinity (or -Infinity) is being returned regardless of whether a signed or unsigned infinity is used. Should (unsigned) Infinity be returned when (unsigned) Infinity is used?


(b) what seems to be an inconsistency occurs when mixing Infinity with complex numbers (same thing holds when we replace Infinity with +Infinity or with -Infinity)

```
# the following combinations of complex and infinity are ok
I + Infinity # +Infinity
I - Infinity # -Infinity
I / Infinity # 0

# the following crash with Arithmetic Error 
Infinity / I  
Infinity * I
I * Infinity

# isnt I+Infinity (for example) just as meaningful/less as I*Infinity ? 
```


(c) Im curious about the following expressions

```
x * Infinity
-x * Infinity
```

These return `+Infinity` and `-Infinity` respectively. But what if x is negative real? (should be opposite answers). The following tries to demonstrate this for two vars (z and x), both declared real in two different ways

```
sage: var('z',domain='real')
z
sage: assume(x,'real',x<0,z<0)
sage: assumptions()
[x is real, x < 0, z < 0]
sage: x*+Infinity
+Infinity
sage: z*+Infinity
+Infinity
```

(is this another ticket "make Infinity work with assumptions/declarations"?)


---

Comment by burcin created at 2010-02-24 16:51:02

Hi Ross,

It's likely that there are inconsistencies in the way infinity is handled by pynac. For instance it definitely doesn't handle interactions with the complex `I` well. I implemented support for infinity in pynac to provide a basis for better series expansions and limit computations. However, I didn't have time to actually use it for anything later.

I suggest we keep this issue focused on the conversion problem in the maxima interface so it can be reviewed and merged quickly. You can open separate tickets for the problems in pynac related to infinity. The fact that assumptions are not passed on to pynac should be yet another ticket.

BTW, this article might help decide what behavior we expect w.r.t. arithmetic involving infinity.

http://dx.doi.org/10.1016/j.jsc.2004.12.002


---

Comment by rossk created at 2010-02-25 07:53:32

Burcin.


I *did* think it unlikely all these issues would be addressed in one ticket ;-) I guess I was trying to be diligent in reviewing (and Im interested in getting involved in "symbolics" development some time, so the extended exercising of the symbolics module is part of my familiarization process - I even started looking at the code!)


The tests I did above (plus others involving limits) warrant a positive review vote from me. Ill let Karl-Dieter sign it off when he wants, as he has reviewed the code as well.


---

Comment by burcin created at 2010-04-12 08:33:08

apply only this patch


---

Attachment

I rebased the patch so that it applies cleanly after #7661.

This ticket depends on #7661. Only attachment:trac_8237-maxima_infinity.take3.patch should be applied.


---

Comment by kcrisman created at 2010-04-23 16:30:35

This looks wonderful to me, but unfortunately I don't have a current build of the alphas for 4.4, so I can't actually test it.  I'd give is a positive review if I could!


---

Comment by robert.marik created at 2010-04-29 06:05:47

Works for me, long tests passed on 4.4.rc0.

Since also kcrisman wrote "This looks wonderful to me .... I'd give is a positive review if I could!" I think that the ticket deserves positive review.

Positive review. Apply only trac_8237-maxima_infinity.take3.patch


---

Comment by robert.marik created at 2010-04-29 06:05:47

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 22:09:54

Merged [trac_8237-maxima_infinity.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8237/trac_8237-maxima_infinity.take3.patch).


---

Comment by mvngu created at 2010-05-08 22:09:54

Resolution: fixed
