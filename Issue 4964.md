# Issue 4964: Add Weil pairing to Sage

Issue created by migration from Trac.

Original creator: dmhansen

Original creation time: 2009-01-11 17:54:28

Assignee: mollerhansen

Keywords: pairing, elliptic curve

Add at first (mollerhansen's) Weil pairing implementation on EC points and in this way laying out a framework for pairings in general. 

In future: 
* this Weil pairing implementation should be replaced by a more effective implementation.
* other pairings could be implemented/wrapped using same framework.


---

Comment by dmhansen created at 2009-01-25 16:50:06

Have checked in patch for elliptic_points.py.
Don't know how much of a framework there is yet.


---

Comment by dmhansen created at 2009-01-25 16:50:06

Resolution: fixed


---

Comment by cremona created at 2009-01-25 17:35:12

How can this ticket be closed when there is no patch here?  Is there a patch somewhere else?  If so, where?!


---

Comment by cremona created at 2009-01-25 18:25:09

I am reopening this since David wrongly thought that committing his changes was all that was needed.  He will upload a patch sometime soon.


---

Comment by cremona created at 2009-01-25 18:25:09

Resolution changed from fixed to 


---

Comment by cremona created at 2009-01-25 18:25:09

Changing status from closed to reopened.


---

Comment by cremona created at 2009-01-25 22:26:33

This looks pretty good to me though I have not done any detailed testing, I only looked at the code.

I have one suggestion which should speed this up whenever the actual orders of P or Q are strictly less than n:  find the orders of P and Q, say m1 and m2.  (The generic function order_from_multiple might be useful here.)   Let d=gcd(m1,m2).  Then it is clear that the result is a d'th root of unity, and it can be computed by taking the pairing of (m1/d)*P and (m2/d)*Q.  [Proof: exercise.]  This would save a lot when d is much less than n.

I also have a question: rather than wait for a division by zero error to catch dependent input, why not do a discrete log calculation to test this?  Maybe that's much slower for large n;  it would be nice to have this decision justified.

Sorry, that's all I have time for just now.


---

Comment by dmhansen created at 2009-01-25 22:47:28

> I have one suggestion which should speed this up whenever the actual orders of P or Q are strictly less than n:  find the orders of P and Q, say m1 and m2.  (The generic function order_from_multiple might be useful here.)   Let d=gcd(m1,m2).  Then it is clear that the result is a d'th root of unity, and it can be computed by taking the pairing of (m1/d)*P and (m2/d)*Q.  [Proof: exercise.]  This would save a lot when d is much less than n.

Yes, I agree - for now the only thing implemented is for points of order n, I check that they both are of order n, which actually will take some time for large n. There is definitely room for improvement here! 

> I also have a question: rather than wait for a division by zero error to catch dependent input, why not do a discrete log calculation to test this?  Maybe that's much slower for large n;  it would be nice to have this decision justified.

Well, it is much slower for large n to do discrete log computations. Wrt. to time complexity then I do not think we can do better since the miller algorithm runs in linear time in the number of bits in the input n.

You're right the above argument should be noted in the code.

Replying to [comment:6 cremona]:
> This looks pretty good to me though I have not done any detailed testing, I only looked at the code.
> 
> I have one suggestion which should speed this up whenever the actual orders of P or Q are strictly less than n:  find the orders of P and Q, say m1 and m2.  (The generic function order_from_multiple might be useful here.)   Let d=gcd(m1,m2).  Then it is clear that the result is a d'th root of unity, and it can be computed by taking the pairing of (m1/d)*P and (m2/d)*Q.  [Proof: exercise.]  This would save a lot when d is much less than n.
> 
> I also have a question: rather than wait for a division by zero error to catch dependent input, why not do a discrete log calculation to test this?  Maybe that's much slower for large n;  it would be nice to have this decision justified.
> 
> Sorry, that's all I have time for just now.


---

Comment by cremona created at 2009-02-01 18:25:04

I succesfully applied the patch to 3.3.alpha3 and the doctests pass.  But the first example I tried crashed:

```
sage: F.<a>=GF(19^4)
sage: E=EllipticCurve(F,[-1,0])
sage: P,Q=E.gens()
sage: P.order(), Q.order()
(360, 360)
# Check that P and Q really are independent:
sage: linear_relation(P,Q,'+')
(0, 360)
sage: P.weil_pairing(Q,360)
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)
...
PariError: impossible inverse modulo:  (36)
```

So pari (which does the underlying field arithmetic) has tried to divide by zero.

The comments in the code suggest that (1) run-time errors only happen when the points are independent, and (2) these are caught.  So here is a counterexample to both.

Is there a typo in the code perhaps?


---

Comment by dmhansen created at 2009-02-01 19:21:48

> Is there a typo in the code perhaps?

Well, I kinda hope that there is, since otherwise it would be a larger problem. 
Debugging time! I'll try to figure it out, then i'll put up a new patch and notify you. Thanks for your review.


---

Comment by cremona created at 2009-02-01 20:31:15

Replying to [comment:9 dmhansen]:
> > Is there a typo in the code perhaps?
> 
> Well, I kinda hope that there is, since otherwise it would be a larger problem. 
> Debugging time! I'll try to figure it out, then i'll put up a new patch and notify you. Thanks for your review.

I cannot see the problem myself.  The _line_() code looks fine.  _miller_() looks good, and when the points are independent I don't see how you would ever get 0 from one of the _line() calls.  [One piece of debugging would be to make sure that _line_() never returns zero, perhaps).

Two more comments:  in _miller_(), you should perhaps initialize t to self.base_ring()(1) and not just 1.  Secondly, this code would apply just as well to points of finite order over any field, so you should move the whole block of code so that the functions are members of EllipticCurvePoint_field and not of the sub-class EllipticCurvePoint_finite_field.


---

Comment by dmhansen created at 2009-02-06 10:19:04

> I cannot see the problem myself.  The _line_() code looks fine.  _miller_() looks good, and when the points are independent I don't see how you would ever get 0 from one of the _line() calls.  [One piece of debugging would be to make sure that _line_() never returns zero, perhaps).

There was definetly a zero division when computing the slope in case P=Q\neqO in the _line_ function. Problem was that after refactoring my own code and putting it nicely into sage I forgot the subcase P=Q\neqO x1=x2. So the zero came from the vertical slope not being handled seperatly.

I then tried your test and I wondered why 

```
sage: P.weil_pairing(Q,360).multiplicative_order()
181
sage: P.order()
360
sage: 180*P
(0 : 0 : 1)
```

I will make a bug report on it. 

> Two more comments:  in _miller_(), you should perhaps initialize t to self.base_ring()(1) and not just 1.  Secondly, this code would apply just as well to points of finite order over any field, so you should move the whole block of code so that the functions are members of EllipticCurvePoint_field and not of the sub-class EllipticCurvePoint_finite_field.

I think I will do this in the next iteration together with your suggestion on saving time by precomputing the d=gcd(m1,m2) and doing the pairing of (m1/d)*P and (m2/d)*Q. I'm a bit pressured on time this month and I think that the next iteration will require some more extensive tests.


---

Comment by dmhansen created at 2009-02-06 10:28:54

> I will make a bug report on it. 

No I won't. The sage output is ok. 
Sorry it's a bit early in the morning. weil pairing result must then be wrong.. Think it's a bit to early in the morning to be doing this.


---

Comment by cremona created at 2009-02-06 10:31:23

Replying to [comment:12 dmhansen]:
> > I will make a bug report on it. 
> 
> No I won't. The sage output is ok. 
> Sorry it's a bit early in the morning. weil pairing result must then be wrong.. Think it's a bit to early in the morning to be doing this.

Agreed: (0:0:1) has order 2, so that's consistent!  john


---

Attachment

Sage Version 3.2.3, Release Date: 2009-01-05


---

Comment by dmhansen created at 2009-02-06 14:21:53

New patch is up. I kept the pairing down in the ElliptiCurvePoint_finite_field class. In future this should be moved up into more general class with possible improvements noted in the above comments. Also the Modified Tate pairing, should be fairly straight forward to implement now.


---

Attachment

The revised patch fixes the bug.  I have taken the liberty of adding my patch trac_4964a.patch (to be applied after trac_4964.patch) which does the following:

   1. Adds a doctest to show that the bug I reported is fixed.
   2.  Moves the functions to the class EllipticCurvePoint_field, as I originally suggested, since this works perfectly well!
   3. Illustrate my point in 2 by adding a docest computing a 5th order Weil pairing over the 5th cyclotomic field.
   4. Edited the documentation about the implementation only applying when both points have the same order n, since in fact the only condition is that n*P=n*Q=0, i.e. that they are both in E[n], so the function could be applied to any two torsion points provided that n is a common multiple of their orders.

If dmhansen is happy with these adjustments then I am happy with the (combined) patch, so I am optimistically giving it a positive review.  Ideally, a 3rd party would take a look too.


---

Comment by dmhansen created at 2009-02-07 16:02:13

>    1. Adds a doctest to show that the bug I reported is fixed.

- Great! I also made a similar doc test using your example to test the _miller_ unction implementation, so now we should be covered.

>    2.  Moves the functions to the class EllipticCurvePoint_field, as I originally suggested, since this works perfectly well!
>    3. Illustrate my point in 2 by adding a docest computing a 5th order Weil pairing over the 5th cyclotomic field.

- This is really good. Thank you a lot, really cool that it just generalizes without any problems. 

>    4. Edited the documentation about the implementation only applying when both points have the same order n, since in fact the only condition is that n*P=n*Q=0, i.e. that they are both in E[n], so the function could be applied to any two torsion points provided that n is a common multiple of their orders.

- I agree. That's an important point to include. 

> If dmhansen is happy with these adjustments then I am happy with the (combined) patch, so I am optimistically giving it a positive review.  Ideally, a 3rd party would take a look too.

I am very happy with the changes and yes it would be nice to get a 3rd party review.


---

Attachment

Apply after previous two.


---

Comment by cremona created at 2009-02-07 17:17:49

Thanks.  Encouraged, I added the other thing which I suggested earlier, which ensures that the hard computation (of the Miller functions) is only done to order gcd(|P|,|Q|).  In case the orders of P and Q are not known, it computes the order using the information that it divides n (otherwise it would use the group order, but that might be a lot larger than n).  Some testing showed that this did speed up the function.

I'm asking for a new reviewer on sage-nt now.


---

Comment by mabshoff created at 2009-02-08 02:00:54

Merged all three patches in Sage 3.3.alpha6. Doctests do pass, but if another reviewer looks at this again it would be good.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 02:00:54

Resolution: fixed


---

Comment by cremona created at 2009-02-08 10:16:41

Replying to [comment:20 mabshoff]:
> Merged all three patches in Sage 3.3.alpha6. Doctests do pass, but if another reviewer looks at this again it would be good.
> 
> Cheers,
> 
> Michael

Thanks, Michael!  John
