# Issue 2079: /= does not work for univariate polynomials

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-02-07 05:24:30

Assignee: somebody

CC:  robertwb


```
sage: R.<x> = QQ[]
sage: a = 2*x^2+2; a
2*x^2 + 2
sage: a /= 2
sage: a
2*x^2 + 2
```



---

Comment by mhansen created at 2008-02-07 10:22:14

Changing priority from major to critical.


---

Comment by cremona created at 2008-02-18 11:27:42

Lines 938-946 of polynomial_element.pyx seem to be at fault.  This might help:


```
sage: R.<x> = QQ[]
sage: a = 2*x^2+2; a
2*x^2 + 2
sage: a/=2; a
2*x^2 + 2
sage: a/=Integer(2); a
2*x^2 + 2
sage: a/=QQ(2); a
x^2 + 1
```


I note the comment there:

```
        Be careful about coercions (this used to be broken):
            sage: R.<x> = ZZ['x']
            sage: f = x / Mod(2,5); f
            3*x
            sage: f.parent()
            Univariate Polynomial Ring in x over Ring of integers modulo 5
```


Personally I would prefer that to be broken than to allow division of a ZZ polynomial by an integer mod 5.  I think the coercion model which says "if there is anything conceivable which could be done to make sense of the input, the do it, even if it makes little or no mathematical sense", has something wrong with it.

But someone with more knowledge of the coercion code will have to deal with this one, which is certainly very serious.


---

Comment by was created at 2008-02-19 00:18:01

> I think the coercion model which says "if there is anything 
> conceivable which could be done to make sense of the input, 
> the do it, even if it makes little or no mathematical sense",
> has something wrong with it.

That (=PARI, Mathematica, etc) is definitely *not* supposed 
to be Sage's coercion model.

That said, dividing a ZZ poly by an integer mod 5 does make perfectz
sense in the coercion model.  There is a natural map from ZZ to ZZ/5ZZ,
hence a natural map `ZZ[x] --> (ZZ/5ZZ)[x]`.  The poly is mapped
to (ZZ/5ZZ)[x] and then the division takes place.  It is well defined,
natural, canonical, and certainly not ad hoc.

William


---

Comment by was created at 2008-02-19 00:58:51

Changing priority from critical to blocker.


---

Comment by was created at 2008-02-19 00:58:51

This is a really really serious bug somewhere in the actions part of the coercion model.  I've promoted it to a blocker.


---

Comment by was created at 2008-02-19 01:29:38

The problem is around line 869 of coerce.pyx, where if we put:

```
        if self.connecting is not None:
            print "g before = ", g
            g = self.connecting._call_c(g)
            print "g after = ", g
```


then run the sample code:

```
sage: R.<x> = QQ[]; a = 2*x^2+2
sage: a /= 2
g before =  1/2
g after =  1
3 2*x^2 + 2 1
```


you see that self.connecting._call_c is somehow replacing 1/2 by 1.  Not good.


---

Comment by was created at 2008-02-19 01:49:28

I'm about to attach a patch that adds several functions related to making the coercion model a little more user friendly (for debugging), fixes/adds more documentation, and MOST IMPORTANTLY, re-enables some disabled type checking that lead to some potentially seriously bugs in the basic arithmetic in Sage.   I also put some commented out code that doesn't look right to me that would fix the above problem.  I hope that Robert will: 

  1. look at the above patch;
 
  2. Make some changes to genuinely fixes the action.pyx file;

  3. Make a patch over the above patch that incorporates those fixes, and probably disables the type checking that I enabled. 

Anyway, again, the core root cause of this problem is that InverseAction in action.pyx is not implemented correctly and/or makes invalid assumptions, and ends up calling this bit of code in rational.pyx with an x that is of type Rational:


```
    cdef Element _call_c_impl(self, Element x):
        cdef Rational rat
        rat = <Rational> PY_NEW(Rational)
        mpq_set_z(rat.value, (<integer.Integer>x).value)
        return rat
```


The result is wrong answers. 

William


---

Comment by was created at 2008-02-19 01:50:51

fixes the problem, but needs an additional patch from Robert.


---

Attachment

I figured out what the issue is. I will post a fix tonight (after making sure it breaks nothing else, and adding more doctests/consistency checks.)


---

Comment by cremona created at 2008-02-19 09:21:26

Replying to [comment:3 was]:
> > I think the coercion model which says "if there is anything 
> > conceivable which could be done to make sense of the input, 
> > the do it, even if it makes little or no mathematical sense",
> > has something wrong with it.
> 
> That (=PARI, Mathematica, etc) is definitely *not* supposed 
> to be Sage's coercion model.
> 
> That said, dividing a ZZ poly by an integer mod 5 does make perfectz
> sense in the coercion model.  There is a natural map from ZZ to ZZ/5ZZ,
> hence a natural map `ZZ[x] --> (ZZ/5ZZ)[x]`.  The poly is mapped
> to (ZZ/5ZZ)[x] and then the division takes place.  It is well defined,
> natural, canonical, and certainly not ad hoc.
> 
> William
> 

 OK, I admit that this does make sense.  Just after posting that I realised that for many years,  in pari, if I ever wanted to input a polynomial mod 5 I would type something like 

```
f = (x^2+1) * Mod(1,5)
```

 which -- apart from being a multiplication and not a division -- shows that I do know that this makes sense.

 Trying to understand what was going wrong in this case got me into very deep water in the coercion mode;  I look forward to seeing the patches which make that easier to understand what is going on.  The notes at http://wiki.sagemath.org/days7/coercion will be very helpful.  ARe they a description of what is currently in place, or a wish list for what should be, or somewhere between the two?


---

Attachment


---

Attachment


---

Comment by robertwb created at 2008-02-19 10:47:58

This code now works correctly instead of giving invalid results (really bad) or throwing an error (undesirable). I have also added code to verify any actions created in the coercion model conform to the expected specifications, to forestall something like this from coming up again (and had to fix things in a couple of other places, though nothing else that gave erroneous results). 

In response to the question above, the Sage Days 7 wiki page is a wishlist and guide for how things should and will be, some of which has already been implemented in a (still very broken) branch. Most of what is there concerns how the user/developer will interact with the coercion model, rather than how the model itself works.


---

Comment by was created at 2008-02-19 14:36:54

REFEREE REPORT: 

I've read through and tested the code and it (1) looks good, and (2) fixes a critical bug in basic arithmetic in Sage that would lead to basic wrong answers.  The code looks good and adds a lot of nice documentation.  Thus this should definitely be applied!

I really think documenting the heck out of all the coercion model related files should be the absolute number one priority in all the coercion model stuff you guys are doing.  If that code were documented and the coercion model itself were way friendly wrt introspection (i.e., understanding it interactively from the command line and/or graphically), then people would be VASTLY more likely to dive in and help with revamping things according to your vision.  At least, I would be.   The value of knowing you can dive into the core and understand it yourself when the going gets rough is not to be underestimated, and is why we all like open source so much.


---

Comment by was created at 2008-02-19 14:37:58

One more comment: ALL the patches attached to this ticket should be applied in order.


---

Comment by mabshoff created at 2008-02-19 14:56:10

All four patches merge in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-19 14:56:10

Resolution: fixed
