# Issue 8659: another broken square root simplification

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-04-08 10:10:49

Assignee: burcin

CC:  kcrisman

Reported by Alex Raichev on sage-support:


```
On Wed, 7 Apr 2010 16:56:01 -0700 (PDT)
Alex Raichev <tortoise.said`@`gmail.com> wrote:

> What the?
> 
> ----------------------------------------------------------------------
> | Sage Version 4.3.5, Release Date: 2010-03-28                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant(); a
> 8
> sage: a^(-1/2)
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call
> last)
> 
> /Users/arai021/Dropbox/sage_work/<ipython console> in <module>()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> expression.so in sage.symbolic.expression.Expression.__pow__ (sage/
> symbolic/expression.cpp:11892)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/rings/
> number_field/number_field_element.so in
> sage.rings.number_field.number_field_element.NumberFieldElement.__pow__
> (sage/rings/number_field/number_field_element.cpp:10038)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> power_helper.so in sage.symbolic.power_helper.try_symbolic_power
> (sage/ symbolic/power_helper.cpp:633)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> power_helper.so in sage.symbolic.power_helper.try_symbolic_power
> (sage/ symbolic/power_helper.cpp:509)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/
> expression.so in sage.symbolic.expression.Expression.__pow__ (sage/
> symbolic/expression.cpp:11892)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/rings/
> rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/
> rational.c:15609)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/structure/
> element.so in sage.structure.element.RingElement.__mul__ (sage/
> structure/element.c:11337)()
> 
> /Applications/sage/local/lib/python2.6/site-packages/sage/structure/
> coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op
> (sage/structure/coerce.c:6994)()
> 
> TypeError: unsupported operand parent(s) for '*': 'Rational Field' and
> '<type 'NoneType'>'

```


Here is the thread:

http://groups.google.com/group/sage-support/t/3e8ae9f6b7c44e7c

This looks similar to #8540, though it is a long standing issue, not caused by that ticket:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant(); a
8
sage: a^(-1/2)
<boom>
```



---

Comment by jason created at 2010-04-08 14:46:52

This problem might not be in symbolics, but in number fields:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();
sage: a
8
sage: type(a.pyobject())
<type 'sage.rings.number_field.number_field_element_quadratic.NumberFieldElement_quadratic'>
sage: b=a.pyobject()
sage: b
8
sage: parent(b)
Number Field in I with defining polynomial x^2 + 1
sage: sqrt(b)
2*sqrt(2)
sage: 1/sqrt(b)
1/4*sqrt(2)
sage: b^(-1/2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.4, Release Date: 2010-03-19                       |
| Type notebook() for the GUI, and license() for information.        |
/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.NumberFieldElement.__pow__ (sage/rings/number_field/number_field_element.cpp:10038)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:633)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:509)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11892)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15609)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()

TypeError: unsupported operand parent(s) for '*': 'Rational Field' and '<type 'NoneType'>'
```



---

Comment by jason created at 2010-04-08 14:51:38

Interestingly, these all work (starting from the above example in my post):


```
sage: b^(1/3)
2
sage: b^(1/4)
8^(1/4)
sage: b^(-1/4)
1/8*8^(3/4)
```


So it seems that b^(1/2) is the only problem?


---

Comment by jason created at 2010-04-08 15:27:29

On the other hand, it seems like the problem is in try_symbolic_power.  When I change that function to:


```
    global __pynac_pow
    print "entering try_symbolic_power: ", obj, p, "; __pynac_pow is ", __pynac_pow
    if __pynac_pow:
        __pynac_pow = False
        print "    set __pynac_pow to False and return None"
        return None
    else:
        try:
            __pynac_pow = True
            print "    Try SR powers: ", ring.SR(obj), ring.SR(p)
            return ring.SR(obj)**ring.SR(p)
        finally:
            print "        and then set __pynac_pow to False"
            __pynac_pow = False
```


then I get:


```
sage: b^(1/2)
entering try_symbolic_power:  8 1/2 ; __pynac_pow is  False
    Try SR powers:  8 1/2
entering try_symbolic_power:  2 1/2 ; __pynac_pow is  True
    set __pynac_pow to False and return None
        and then set __pynac_pow to False
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/number_field/number_field_element.so in sage.rings.number_field.number_field_element.NumberFieldElement.__pow__ (sage/rings/number_field/number_field_element.cpp:10065)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:755)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/power_helper.so in sage.symbolic.power_helper.try_symbolic_power (sage/symbolic/power_helper.cpp:614)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__pow__ (sage/symbolic/expression.cpp:11892)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.__pow__ (sage/rings/rational.c:15609)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()

TypeError: unsupported operand parent(s) for '*': 'Rational Field' and '<type 'NoneType'>'
sage: b^(1/4)
entering try_symbolic_power:  8 1/4 ; __pynac_pow is  False
    Try SR powers:  8 1/4
entering try_symbolic_power:  8 1/4 ; __pynac_pow is  True
    set __pynac_pow to False and return None
        and then set __pynac_pow to False
8^(1/4)

```



---

Comment by jason created at 2010-04-08 16:00:32

Unsurprisingly, I get the same error traceback if I do `(b*b)^(1/4)`


---

Comment by burcin created at 2010-09-25 23:24:24

Now that we have the `hold()` function for symbolic expressions (#9879), we don't need `sage.symbolic.power_helper`. attachment:trac_8659-hold_powers.patch removes this module, and fixes the problem described.

This ticket depends on #9879.


---

Comment by burcin created at 2010-09-25 23:24:24

Changing status from new to needs_review.


---

Attachment

At first I thought I minded this discrepancy, but I think that maybe that's okay, given they really do live in different places.  At the same time, in theory then we should be holding anything that might ever be multivalued.  Like a square root.

```
sage: 8^(1/2)
2*sqrt(2)
sage: I.pyobject().parent()
Number Field in I with defining polynomial x^2 + 1
sage: I.pyobject().parent()(8)^(1/2)
sqrt(8)
```

In particular, what do we want here?

```
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();
sage: b = a.pyobject()
sage: b^(-1/2); a^(-1/2)
1/sqrt(8)
1/8*sqrt(8)
```



---

Comment by kcrisman created at 2011-04-25 17:02:33

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2011-04-25 19:53:24

Also, is 

```
sage: (t^2)^(1/4) 
64^(1/4) 
```

intended to test

```
return SR(nbase).power(nexp*exp, hold=True)
```

But the powers weren't multiplied, because `SR(base)` already is just 64.  

Similarly, 

```
sage: 8^(-1/5) 
```

can't be to test the change in that file, because 8 isn't rational.  

Or am I missing something?   Sorry if I've misinterpreted something; otherwise this is a good fix, it seems.


---

Attachment


---

Comment by burcin created at 2011-05-30 22:32:36

Changing status from needs_info to needs_review.


---

Comment by burcin created at 2011-05-30 22:32:36

attachment:trac_8659-hold_powers.take2.patch should address the issues in comment:7 at the cost of magically changing the type of the coefficients to rational.

The test

```
sage: 8^(-1/5)
```

does test the `__pow__` method of rationals, since the `__pow__` method of `Integer` casts the base to a rational and calls pow again.


---

Comment by kcrisman created at 2011-06-16 04:37:40

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2012-02-15 15:46:31

I uploaded a new patch which should finally fix this. Please review.


---

Comment by burcin created at 2012-02-15 15:46:31

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2012-02-15 15:59:50

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-02-15 15:59:50

[[[
infite loops
}}}


---

Comment by kcrisman created at 2012-02-15 16:14:56

Hmm, that didn't format right.  I meant to say, there are two occurrences of 

```
infite loops
```


I think it would be helpful to have a doctest or two for each branch of the number field code.  Some are no doubt already in there, but all?  For instance, I would have thought that `(t<sup>2)</sup>(1/4)` is testing `return nbase.power(pexp * exp, hold=True) `, but it doesn't give `8^(1/2)` like I would have thought from that (so it must be from the `if not SR` branch); so it would be good to have one for that branch.

Also, can you think of a place where putting the rational power in the denominator could cause something to break?    Is that standard practice in this kind of computer algebra?  For instance, Maxima does not do this.

```
(%i3) 2^(-1/2);
(%o3) 1/sqrt(2)
```


Sorry if these are dumb questions.


---

Attachment


---

Comment by burcin created at 2012-02-15 17:05:32

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2012-02-15 17:05:32

Replying to [comment:13 kcrisman]:
> Hmm, that didn't format right.  I meant to say, there are two occurrences of 
> {{{
> infite loops
> }}}

I updated the patch to fix the typos.

> I think it would be helpful to have a doctest or two for each branch of the number field code.  Some are no doubt already in there, but all?  For instance, I would have thought that `(t<sup>2)</sup>(1/4)` is testing `return nbase.power(pexp * exp, hold=True) `, but it doesn't give `8^(1/2)` like I would have thought from that (so it must be from the `if not SR` branch); so it would be good to have one for that branch.

That branch is tested by these:


```
            sage: sqrt2^(1/5)
            2^(1/10)
            sage: sqrt2^sqrt2
            2^(1/2*sqrt(2))
```


> Also, can you think of a place where putting the rational power in the denominator could cause something to break?    Is that standard practice in this kind of computer algebra?  For instance, Maxima does not do this.
> {{{
> (%i3) 2^(-1/2);
> (%o3) 1/sqrt(2)
> }}}

AFAICT, GiNaC assumes this normal form.


On another note... IMHO, a simple typo in comments within source code, or not documenting which doctest corresponds to which branch in the code is justification to switch a ticket to `needs_work`. You might not be satisfied with the work, but it is possible that someone else will give a positive review, especially since this is a `critical` ticket.


---

Comment by kcrisman created at 2012-02-15 17:52:47

> On another note... IMHO, a simple typo in comments within source code, or not documenting which doctest corresponds to which branch in the code is justification to switch a ticket to `needs_work`. You might not be satisfied with the work, but it is 

Fair enough!  Though I do think typos are 'needs work', often I can update them on a refresh.  The doctest thing was just wanting to check that we *did* check all branches.  Maybe 'needs info' is better?  The point is that I want to make sure the comment gets seen; a lot of times I see questions on 'needs review' that are then never actually addressed.  I don't really care what the status itself is.

> possible that someone else will give a positive review, especially since this is a `critical` ticket.

Well, it's apparently been `critical` for nearly two years, so perhaps that is less convincing of an argument on this ticket than others.  But point taken in general!


---

Comment by kcrisman created at 2012-02-15 20:22:14

Okay, I now get all the branches, and it makes sense.  Thanks for hanging in there with me!  Also, good catch and test on the powers less than -1.

I'm not putting 'needs work' :) but also not yet positive review.   In comment:7, we see the equivalent of this inconsistency: 

```
sage: a= matrix([[2,2,I],[2,2,-I],[I,-I,0]]).determinant();
sage: a; type(a)
8
<type 'sage.symbolic.expression.Expression'>
sage: b = SR(8)
sage: type(b)
<type 'sage.symbolic.expression.Expression'>
sage: a.operands(); a.operator()
[]
sage: b.operands(); b.operator()
[]
sage: b^(-1/2)
1/4*sqrt(2)
sage: a^(-1/2)
1/8*sqrt(8)
sage: a^(1/2)
sqrt(8)
sage: b^(1/2)
2*sqrt(2)
```


I thought that maybe this was because (for reasons unclear to me) we had entered 

```

        if not PY_TYPE_CHECK(self, Rational):
```

but 

```
sage: isinstance(b,Rational)
False
sage: isinstance(a,Rational)
False
```

so I must be missing something obvious.  Anyway, I can't see why these should return different things, and we still have the switch to rational that should take care of this:

```
                res = QQ(base)**exp 
```




Also, the documentation in rational.pyx still says

```

    def __pow__(self, n, dummy):
        """
        Raise self to the integer power n.
        
```

though I think this code has been used for non-integer powers for quite a while.

But perhaps another reviewer will see what is going on in these cases, my apologies if I'm wasting time.


---

Comment by davidloeffler created at 2012-03-10 10:53:09

Apply trac_8659-hold_powers.take3.patch

(for the patchbot, which is trying to apply all three patches simultaneously)


---

Comment by davidloeffler created at 2012-03-11 14:32:19

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-11 14:32:19

Patch does not apply (either to 5.0.beta7, or to 4.8 with #12511 installed).


---

Attachment


---

Comment by burcin created at 2012-05-24 09:50:55

I rebased the patch to 5.0. Apply only attachment:trac_8659-hold_powers.take4.patch.


---

Comment by burcin created at 2012-05-24 09:50:55

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2012-05-28 20:53:57

For the patchbot, apply trac_8659-hold_powers.take4.patch


---

Comment by mhansen created at 2012-05-28 21:09:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2012-05-28 21:09:03

Changing keywords from "" to "sd40.5".


---

Comment by mhansen created at 2012-05-28 21:09:03

Looks good to me.


---

Comment by jdemeyer created at 2012-06-18 10:21:48

Resolution: fixed
