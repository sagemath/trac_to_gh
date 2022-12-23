# Issue 7935: local_data for elliptic curves over number fields

Issue created by migration from https://trac.sagemath.org/ticket/7935

Original creator: wuthrich

Original creation time: 2010-01-15 13:41:18

Assignee: cremona

CC:  cremona robertwb

Keywords: elliptic curve, number fields, local data, tamagawa

First of all, I spotted the following bug:


```
K.<a> = NumberField(x^2-38)
E = EllipticCurve([a,1/2])
E.global_integral_model()
```


which yields

```
AssertionError: bug in global_integral_model: [0, 0, 0, 4/361*a, 4/6859]
```


and that is easy to fix. But I also wish to add a `tamagawa_product` and improve the documentation.

I will post a patch later today.


---

Comment by wuthrich created at 2010-01-15 13:42:52

Before I get complains, I'd better add that tamagawa_product will not be the product of tamagawa numbers, but rather it envolves also the changes to the local minimal model. It will be the term that appears in BSD. Something I always wanted to add.


---

Comment by cremona created at 2010-01-15 13:50:53

Thanks, I'll review it as soon as possible (I wrote the function so it is my fault!)


---

Attachment

exported against 4.3.alpha1


---

Comment by wuthrich created at 2010-01-15 15:21:23

I am not sure whether it is a good idea to have a definition of tamagawa_product for number fields that differs from the one for Q; but it is the only sensible definition. An option whould be to change the definition over Q; it would affect only non-minimal equation, but still it might break a lot of compatibility.

The very last thing in the patch, line 1024 in the new ell_number_field.py, is strange. It yields now a different global minimal model (yes they differ by a weierstrass-change with u a unit in K). If one computes this outside of this file one gets the old result. This may be linked to #7930, I don't know.


---

Comment by wuthrich created at 2010-01-15 15:21:30

Changing status from new to needs_review.


---

Comment by cremona created at 2010-01-15 16:52:41

Thanks for all the excellent documentation!

About the bug:  I am puzzled by this, as I still don't see how either my original code failed or how the change (of uniformiser) works best.  Here was my thinking:  if val(a_i)<0 for some i, then find the minimal e such that e*i+valuation(a_i) is >=0 for i in [1,2,3,4,6] and then replace a_i by `a_i/pi^(e*i)`.  The point about using the "negative" flag on the uniformiser was so ensure that dividing by a power of pi maintained integrality at all other primes.  Your new code will not do that.

Would this be better:

```
        D = self.discriminant()
        for P in D.prime_factors():
            if not all([a.valuation(P)>=0 for a in ai]):
                   pi=K.uniformizer(P,'negative')
                   e  = min([(ai[i].valuation(P)/[1,2,3,4,6][i]) for i in range(5)]).floor()
                   ai = [ai[i]/pi**(e*[1,2,3,4,6][i]) for i in range(5)]
```

? 

I have not looked at your last point yet.  I am not so keen on tamagawa_product() not giving the product of the Tamagawa numbers.  Are you sure that over Q when an equation is non-minimal at p that the number returned by tamagawa_number() is not the index for the minimal model?  I thought that was what Tate's algorithm would give.  I'll need to look at it more closely.


I am leaving this as "needs review" as I have not actually tested it yet!


---

Comment by wuthrich created at 2010-01-15 17:07:54

Maybe you make a little sign error ? In the bug-example, the valuation of a6 at P = (a) is -2. So e is -1. So you are really multiplying the ais by pi<sup>+i</sup>. So pi should be integral away from P.

As to your comment on `tamagawa_product()`, we have


```
sage: E = EllipticCurve('11a2')
sage: E.tamagawa_product()
1

sage: E2 = E.change_weierstrass_model([1/11,0,0,1])
sage: E2
Elliptic Curve defined by y^2 + 3993*y = x^3 - 121*x^2 - 114492620*x - 466951591502 over Rational Field
sage: E2.tamagawa_product()
1
```


So it is defined to be the product of the Tamagawa numbers (i.e. the index of E<sup>0</sup> (K_v)) on the minimal model.

My definition (and that is the only sensible over number fields) of `tamagawa_product()` changes as one changes the chosen invariant differential in such a way that the product of it with the periods is invariant under this choice. In particular it is not the product of the Tamagawa numbers despite the name.


---

Comment by cremona created at 2010-01-15 17:33:29

OK, I agree that there was a sign error...   The value of e in the code is always negative (since we skip if a is integral, hence at least one of the fractions (which are rounded down by the "/" operator) is negative.  Hence we divide by a negative power of pi, i.e. multiply by a positive power, so haveing pi integral is exactly what you want.  You win! 

Sorry, it's 5.30 on a Friday after the first week of term.

On the T. products, can we come up with a different name for one of the functions since they don't agree?  Either that, of have an optional parameter in the case over Q to give the same value as if Q were treated as a number field?


---

Comment by cremona created at 2010-01-15 20:30:13

Positive review:  applies fine to 4.3.1.alpha2, all tests in sage/schemes/elliptic_curves pass, docs build well (there's a lot of useful extra documentation in the patch), and I agree with the design decisions made.

Thanks for fixing the bug in my code (and more!)


---

Comment by cremona created at 2010-01-15 20:30:13

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 00:01:21


```
File "sage/schemes/elliptic_curves/ell_number_field.py", line 1026:
    sage: E2
Expected:
    Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (12289755603565800754*a-75759141535687466985)*x + (51556320144761417221790307379*a-317814501841918807353201512829) over Number Field in a with defining polynomial x^2 - 38
Got:
    Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (368258520200522046806318444*a-2270097978636731786720859345)*x + (8456608930173478039472018047583706316424*a-52130038506793883217874390501829588391299) over Number Field in a with defining polynomial x^2 - 38
**********************************************************************
```



---

Comment by rlm created at 2010-01-19 00:01:21

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-01-19 14:08:06

This is very strange.  For that curve E2, I sometimes get

```
Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (12289755603565800754*a-75759141535687466985)*x + (51556320144761417221790307379*a-317814501841918807353201512829) over Number Field in a with defining polynomial x^2 - 38
```

but sometimes I get

```
Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (368258520200522046806318444*a-2270097978636731786720859345)*x + (8456608930173478039472018047583706316424*a-52130038506793883217874390501829588391299) over Number Field in a with defining polynomial x^2 - 38
```

on the same machine.  (Note that both are valid, since both are models with a unit Discriminant so are certainly global minimal models.)

The only way round this I can see in the short term is to remove the line in the doctest which displays E2 itself.  What do people think?


---

Comment by wuthrich created at 2010-01-19 14:20:05

I was afraid that this would happen. I strongly believe that this is the same bug as #7930.
Both answers are valid global minimal models (as mentionned earlier), I could propose that we put a #random behind it and wait for #7930 to be solved.


---

Comment by wuthrich created at 2010-01-19 14:21:24

As we are back to review: What about another name for `tamagawa_product`. It seems not a bad name for what it is, but I admit that John objection is a fair one. What other names could we give it ?


---

Comment by cremona created at 2010-01-19 15:06:56

Replying to [comment:11 wuthrich]:
> I was afraid that this would happen. I strongly believe that this is the same bug as #7930.
> Both answers are valid global minimal models (as mentionned earlier), I could propose that we put a #random behind it and wait for #7930 to be solved. 

I'll go with that.  I'll even put in a comment after the #random saying (minimal model is not unique).


---

Comment by cremona created at 2010-01-19 15:07:45

Replying to [comment:12 wuthrich]:
> As we are back to review: What about another name for `tamagawa_product`. It seems not a bad name for what it is, but I admit that John objection is a fair one. What other names could we give it ?

Howe about bsd_tamagawa_product() or minimal_tamagawa_product()?


---

Comment by cremona created at 2010-01-19 15:18:13

Patch trac_7935b.patch adds the #random tag.


---

Comment by wuthrich created at 2010-01-19 15:30:56

> How about bsd_tamagawa_product() or minimal_tamagawa_product()?

the first one would be ok, the second is missleading as it is not minimal.

tamagawa_product_bsd or tamagawa_product_as_in_bsd so that the tab still
completes it as before.


---

Attachment

Apply after previous


---

Comment by cremona created at 2010-01-19 15:43:31

The new version of trac_7935b.patch changes the name to tamagawa_product_bsd .

Chris, if you are happy with this second patch now you can give it a positive review.


---

Comment by cremona created at 2010-01-19 15:43:31

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2010-01-20 23:26:57

Sorry, John, I could not apply your patch, the last hunk failed. Maybe because I did not upgrade yet. I try again later.


---

Comment by cremona created at 2010-01-21 11:30:50

I will rebase it.  Something else must have merged since which messed up line numbers or something.


---

Comment by wuthrich created at 2010-01-21 13:05:05

second patch to be applied after the first patch, exported against 4.3.1


---

Attachment

I have rebased it.


---

Comment by cremona created at 2010-01-31 17:16:11

Sorry for the delay.  Apply the first and third patches to 4.3.1 -- all works.


---

Comment by cremona created at 2010-01-31 17:16:11

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:11:15

Please update the Author and Reviewer fields, if they're wrong.


---

Comment by mpatel created at 2010-02-11 15:11:15

Resolution: fixed


---

Comment by cremona created at 2010-02-11 15:24:52

I think we can leave it as it is although 99% of the work is by Chris.
