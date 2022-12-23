# Issue 7160: comparison with quadratic number field elements needs work

Issue created by migration from https://trac.sagemath.org/ticket/7160

Original creator: mhansen

Original creation time: 2009-10-08 18:38:28

Assignee: davidloeffler

CC:  vdelecroix


```
sage: I^2
-1
sage: bool(I^2 < 0)
True
sage: bool(I^2 > 0)
True
```



---

Comment by mhansen created at 2009-10-08 18:41:58

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-10-08 19:23:54

This is basically the same as #6132.


---

Comment by cremona created at 2009-10-29 21:30:58

I think this is confusing:  you have an ordering of elements of a real or imaginary quadratic field which is based on some kind of lexicographic ordering on the representation of the elements rather than anything mathematical.  Presumably this is so lists, etc, can be sorted in a pythonic way.  But I find this bizarre:

```
sage: K.<i> = QuadraticField(-1)
sage: i>0
True
```

and this raises a strange error:

```
sage: K.<a> = NumberField(x^2+x-10)
sage: a < -a
---------------------------------------------------------------------------
SystemError                               Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/790/_home_john__sage_init_sage_0.py in <module>()

SystemError: error return without exception set
sage: Type(K)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/790/_home_john__sage_init_sage_0.py in <module>()

NameError: name 'Type' is not defined
sage: type(K)
<class 'sage.rings.number_field.number_field.NumberField_quadratic'>
```



---

Comment by cremona created at 2009-10-29 21:30:58

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-02-07 15:43:47

Apparently related to #6132 and #10064, see [this sage-devel discussion](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/01168722573ff736).


---

Comment by mhansen created at 2011-12-19 10:32:31

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2011-12-19 10:32:31

I've put up a new patch which is minimally invasive and fixes the issue.


---

Comment by kcrisman created at 2011-12-19 15:02:45

Does this result in any interesting speed regressions when doing things with I?


---

Comment by was created at 2011-12-20 06:47:51

1. Typo: " comparision" in sage/rings/number_field/number_field_element_quadratic.pyx. 

2. This code raises a big red flag for me:

```
        1704	                from sage.rings.all import RR 
 	1705	                r = RR(right) 
 	1706	                l = RR(embedding(left)) 
 	1707	                return cmp(l, r) 
```

My concern is that you're comparing to double (=53 bits) precision, which is totally arbitrary.  What if there is an embedding and cmp(left, right) requires 54 bits of precision to sort out?  I could probably with some work construct a nasty example of this, where the above code just gives totally the wrong answer.   I guess we need to (1) compute to precision of the embedding, and (2) if cmp(l,r)==0, then check something more?

3. Where is "self._element_class" actually used?  I guess by the coercion model, but it's hard to see how from this patch, exactly. 

4. I feel like this is too much code that gets around a fundamental problem or bug in number field elements in the case of the reported problem, but leaves the underlying bug unfixed.  Note that *before* applying your patch:

```
sage: bool(I^2 < 0)
True
sage: (I^2).pyobject() < 0
False
```


It seems to me that the output of both lines above should be the same, right, but I bet pynac is evaluating the first comparison and not even going to the pyobject level. Similarly:


```
sage: bool(I^2 < SR(0))
True
sage: (I^2).pyobject() < SR(0).pyobject()
False
```


This is because in Sage we currently have:

```
sage: K.<I> = QuadraticField(-1)
sage: I^2 < 0
False
sage: I^2
-1
```

This is, as Cremona pointed out, due to the arbitrary lexicographic ordering rather than using the one we get on the intersection of K and R inside embedding(K). 

So... it seems to me that the real problem is that the arbitrary ordering is lame.   What you've done is implemented a natural fix in one very, very special case.  Maybe that's the intention, and maybe you had something more general before?  I don't know, since you changed the patch. 

I'm guessing your more general patch changed comparison for all elements to:
  (1) check if there is an embedding of the parent(s), and (2) if so, use that to induce an embedding on *the* real subfield of the field(s).   That would be natural. 

So all of the above, is just me understanding why you are doing what you're doing.  It might make sense to add something like this to the documentation.


---

Comment by was created at 2011-12-20 07:22:26

Note: With sage-4.8.alpha5 and this patch, all tests in devel/sage/sage pass.


---

Comment by davidloeffler created at 2011-12-20 09:40:24

Replying to [comment:7 was]:
> 2. This code raises a big red flag for me:

```
	1704	                from sage.rings.all import RR 
	1705	                r = RR(right) 
	1706	                l = RR(embedding(left)) 
	1707	                return cmp(l, r) 
```

> My concern is that you're comparing to double (=53 bits) precision, which is totally arbitrary. What if there is an embedding and cmp(left, right) requires 54 bits of precision to sort out?  I could probably with some work construct a nasty example of this, where the above code just gives totally the wrong answer.   I guess we need to (1) compute to precision of the embedding, and (2) if cmp(l,r)==0, then check something more?

Isn't this what we have the QQbar class for?


---

Attachment


---

Comment by mhansen created at 2011-12-20 10:10:47

I've added a new patch which should be better.  It turns out just using the embedding directly should be fine.


---

Comment by mhansen created at 2011-12-20 12:32:49

Changing keywords from "" to "sd35".


---

Attachment

Replying to [comment:7 was]:
> 4. I feel like this is too much code that gets around a fundamental problem or bug in number field elements in the case of the reported problem, but leaves the underlying bug unfixed.  Note that *before* applying your patch:
 {{{
 sage: bool(I^2 < 0)
 True
 sage: (I^2).pyobject() < 0
 False
 }}}
> 
> It seems to me that the output of both lines above should be the same, right, but I bet pynac is evaluating the first comparison and not even going to the pyobject level.

The first comparison is done in the `test_relation()` method of `sage.symbolic.expression.Expression`. This converts both sides of the relation to `CIF` and performs the comparison there.

> Similarly:
> 
> {{{
> sage: bool(I^2 < SR(0))
> True
> sage: (I^2).pyobject() < SR(0).pyobject()
> False
> }}}
> 
> This is because in Sage we currently have:
> {{{
> sage: K.<I> = QuadraticField(-1)
> sage: I^2 < 0
> False
> sage: I^2
> -1
> }}}
> This is, as Cremona pointed out, due to the arbitrary lexicographic ordering rather than using the one we get on the intersection of K and R inside embedding(K). 
> 
> So... it seems to me that the real problem is that the arbitrary ordering is lame.   What you've done is implemented a natural fix in one very, very special case.  Maybe that's the intention, and maybe you had something more general before?  I don't know, since you changed the patch. 

Note that this lame ordering is causing problems all over symbolics since `is_positive()` checks fail. See #10849, #10062, #10064 for examples.

> I'm guessing your more general patch changed comparison for all elements to:
>   (1) check if there is an embedding of the parent(s), and (2) if so, use that to induce an embedding on *the* real subfield of the field(s).   That would be natural. 

I attached a new patch at attachment:trac_7160-quadratic_number_field_element_comparison.patch, based on Mike's last patch attachment:trac_7160.patch. This changes the comparison function of quadratic number field elements to always use the embedding into `CC`.

Timings with the patch:


```
sage: K.<sqrt2> = QuadraticField(2)
sage: t = K.random_element(); t
-2*sqrt2 - 35
sage: u = K.random_element(); u
-1
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 659 µs per loop
sage: u = K.random_element(); u
-2*sqrt2 - 1
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 807 µs per loop
```


Without the patch:


```
sage: K.<sqrt2> = QuadraticField(2)
sage: t = -2*sqrt2 - 35
sage: u = K(-1)
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 419 ns per loop
sage: u = -2*sqrt2 - 1
sage: %timeit res = cmp(t,u)
625 loops, best of 3: 419 ns per loop
```


So there is a significant slow down.

There are two failing doctests I need help with:


```
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py
**********************************************************************
File "/home/burcin/sage/sage-5.0.prealpha0/devel/sage-main/sage/schemes/elliptic_curves/ell_curve_isogeny.py", line 4361:
    sage: _[0].rational_maps()
Expected:
    (((-4/25*i - 3/25)*x^5 + (-4/5*i + 2/5)*x^3 + x)/(x^4 + (-4/5*i + 2/5)*x^2 + (-4/25*i - 3/25)),
    ((2/125*i - 11/125)*x^6*y + (64/125*i + 23/125)*x^4*y + (162/125*i - 141/125)*x^2*y + (-4/25*i - 3/25)*y)/(x^6 + (-6/5*i + 3/5)*x^4 + (-12/25*i - 9/25)*x^2 + (2/125*i - 11/125)))
Got:
    (((4/25*i + 3/25)*x^5 + (4/5*i - 2/5)*x^3 - x)/(x^4 + (-4/5*i + 2/5)*x^2 + (-4/25*i - 3/25)), ((11/125*i + 2/125)*x^6*y + (-23/125*i + 64/125)*x^4*y + (141/125*i + 162/125)*x^2*y + (3/25*i - 4/25)*y)/(x^6 + (-6/5*i + 3/5)*x^4 + (-12/25*i - 9/25)*x^2 + (2/125*i - 11/125)))
**********************************************************************
File "/home/burcin/sage/sage-5.0.prealpha0/devel/sage-main/sage/schemes/elliptic_curves/ell_curve_isogeny.py", line 4622:
    sage: isogenies_13_0(E)[0].rational_maps()
Expected:
    (((-4/169*r - 11/169)*x^13 + (-128/13*r - 456/13)*x^10 + (-1224/13*r - 2664/13)*x^7 + (-2208/13*r + 5472/13)*x^4 + (1152/13*r - 8064/13)*x)/(x^12 + (4*r - 36)*x^9 + (-1080/13*r + 3816/13)*x^6 + (2112/13*r + 5184/13)*x^3 + (17280/169*r - 1152/169)), ((18/2197*r - 35/2197)*x^18*y + (-23142/2197*r + 35478/2197)*x^15*y + (-1127520/2197*r + 1559664/2197)*x^12*y + (87744/2197*r + 5992704/2197)*x^9*y + (-6625152/2197*r + 9085824/2197)*x^6*y + (28919808/2197*r - 2239488/2197)*x^3*y + (-1990656/2197*r + 3870720/2197)*y)/(x^18 + (6*r - 54)*x^15 + (-3024/13*r + 11808/13)*x^12 + (31296/13*r - 51840/13)*x^9 + (-487296/169*r - 2070144/169)*x^6 + (-940032/169*r - 248832/169)*x^3 + (-1990656/2197*r + 3870720/2197)))
Got:
    (((7/338*r + 23/338)*x^13 + (-164/13*r - 420/13)*x^10 + (720/13*r + 3168/13)*x^7 + (3840/13*r - 576/13)*x^4 + (4608/13*r + 2304/13)*x)/(x^12 + (4*r + 36)*x^9 + (1080/13*r + 3816/13)*x^6 + (2112/13*r - 5184/13)*x^3 + (-17280/169*r - 1152/169)), ((18/2197*r + 35/2197)*x^18*y + (23142/2197*r + 35478/2197)*x^15*y + (-1127520/2197*r - 1559664/2197)*x^12*y + (-87744/2197*r + 5992704/2197)*x^9*y + (-6625152/2197*r - 9085824/2197)*x^6*y + (-28919808/2197*r - 2239488/2197)*x^3*y + (-1990656/2197*r - 3870720/2197)*y)/(x^18 + (6*r + 54)*x^15 + (3024/13*r + 11808/13)*x^12 + (31296/13*r + 51840/13)*x^9 + (487296/169*r - 2070144/169)*x^6 + (-940032/169*r + 248832/169)*x^3 + (1990656/2197*r + 3870720/2197)))
```



---

Comment by davidloeffler created at 2012-03-29 17:21:36

This patch doesn't apply to 5.0.beta11 -- see patchbot logs.


---

Comment by davidloeffler created at 2012-03-29 17:21:36

Changing status from needs_review to needs_work.


---

Attachment

apply only this patch


---

Comment by mhansen created at 2012-03-29 20:23:56

I rebased the patch to beta11.


---

Comment by mjo created at 2012-04-15 02:34:45

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2012-04-15 02:34:45

This applies cleanly on beta13, I believe it needs review again?


---

Comment by dsm created at 2012-05-25 04:44:53

This ticket applies against cleanly against 5.1.beta0 but still has the two doctest failures.  This patch would get rid of several other problems -- #10064 and #10849 -- so it'd be nice to get in.


---

Comment by mjo created at 2012-05-29 19:32:12

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2012-07-09 07:45:53

Hi,

I made a sort of duplicate with #13213. My aim was to use the natural order of RR in the case of real embedding. For quadratic field it is quite easy and fast. In the same patch, I aim to implement other functions related to the real embedding (is_positive, floor, ceil, abs, ...).

On the other hand, the difference of timings with my patch have an order of magnitude of x10 and not of x1000.

Should I close my ticket ? What to do with my patch ?


---

Comment by burcin created at 2012-07-10 15:57:40

Hi Vincent,

thanks a lot for taking a look at this long standing problem.

Replying to [comment:18 vdelecroix]:
> I made a sort of duplicate with #13213. My aim was to use the natural order of RR in the case of real embedding. For quadratic field it is quite easy and fast. In the same patch, I aim to implement other functions related to the real embedding (is_positive, floor, ceil, abs, ...).

Fixing the comparison of quadratic number fields elements and implementing `floor`, `ceil`, etc. should be in separate patches.

> On the other hand, the difference of timings with my patch have an order of magnitude of x10 and not of x1000.
> 
> Should I close my ticket ? What to do with my patch ?

Since your patch performs much better, we can move ahead using that. I will try to review your patch on #13213.

Once the patches in this ticket are rebased on your patch, we can close this as a duplicate.


---

Comment by vdelecroix created at 2013-05-15 17:13:49

Now #13213 is in positive review (and performances much better than what I expected at the begining)! Should we add a doctest related to the example in the description of the ticket or do we simply close it as a duplicate ?


---

Comment by kcrisman created at 2013-05-15 18:08:58

> Now #13213 is in positive review (and performances much better than what I expected at the begining)! Should we add a doctest related to the example in the description of the ticket or do we simply close it as a duplicate ?
If there are nearly identical examples to these in #13213, then I think that's okay; if there is nothing like this there, we should add a trivial patch. to check it's improved.   I'm not going to look through that whole patch to find ones like this but presumably you know whether there is one like that, as the author :)


---

Attachment


---

Comment by vdelecroix created at 2013-05-15 20:36:59

There are no example which deals with the symbolic ring... that's why I suggested to add some doctest here. See the proposition in the patch. Nevertheless, I found stupid the following behavior (or at least confusing)

```
sage: I**2 == -1
-1 == -1
sage: (I+4)**4 > 0
-4 > 0
```


apply trac_7160-doctest.patch


---

Comment by vdelecroix created at 2013-05-15 20:36:59

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2013-05-31 22:15:44

Now #13213 is positive review. I guess we may close that ticket ?


---

Attachment

fix commit message, and sphinx trac link


---

Comment by burcin created at 2013-06-03 13:56:25

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2013-06-03 13:56:25

I attached a new patch which fixes the commit message and missing `:` before the trac link in the documentation. This is good to go.

Thanks!


---

Comment by jdemeyer created at 2013-06-06 12:31:18

Resolution: fixed
