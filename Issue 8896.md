# Issue 8896: 0.0000000000000000000000000000 is parsed completely differently than 1.0000000000000000000000000000 for no good reason

Issue created by migration from https://trac.sagemath.org/ticket/8896

Original creator: was

Original creation time: 2010-05-05 20:17:53

Assignee: AlexGhitza

CC:  jason

In Sage 0.0 and 0.00000000000000000000000000000000000000 should not denote the same thing, though sadly they do.  Note, however, that 1.0 and 1.00000000000000000000000000000000000000 are different in Sage (as I expect):

```
sage: 0.0
0.000000000000000
sage: 0.00000000000000000000000000000000000000
0.000000000000000
sage: parent(0.00000000000000000000000000000000000000)
Real Field with 53 bits of precision
sage: 1.00000000000000000000000000000000000000
1.0000000000000000000000000000000000000
sage: 1.0
1.00000000000000
sage: parent(1.00000000000000000000000000000000000000)
Real Field with 130 bits of precision
sage: parent(1.0)
Real Field with 53 bits of precision
```

I consider the above inconsistency a bug.


---

Comment by robertwb created at 2010-05-05 22:53:47

This is because 0.00000000000000000000000000000000005 is not considered to have "high precision." We should special-case 0.


---

Comment by leif created at 2010-05-06 01:06:33

Btw, Sage does not distinguish +0.0 and -0.0 (and 0.0).

Nice how trac interprets long decimal fractions of floats. :D


---

Attachment


---

Comment by robertwb created at 2010-05-15 22:36:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-05-26 18:02:42

Looks okay in general, but the last block 

```
else: 
        # Must be 0.00000000000000...0 
        sigfigs = len(mantissa) 
```

needs to be indented, n'est pas?

In the tests, there should be (brief) words to the effect that the first two have the default minimum precision and that is what is being tested for, while in the new tests we are testing for getting high precision.


---

Comment by kcrisman created at 2010-05-26 18:02:42

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-05-27 13:59:08

Replying to [comment:5 kcrisman]:
> Looks okay in general, but the last block 
> {{{
> else: 
>         # Must be 0.00000000000000...0 
>         sigfigs = len(mantissa) 
> }}}
> needs to be indented, n'est pas?

No, the `else` belongs to the `for` statement.
But currently, _leading_ zeros contribute to the precision, too: :)

```
sage: RealNumber(0.000000000000000000).prec()
67
sage: RealNumber(00.000000000000000000).prec()
70
sage: RealNumber(.000000000000000000).prec()
64
```

I'm not sure if this is intentional, it's at least uncommon.
(And a leading `+` also increases the precision.)

It looks as if a decimal point is counted as a significant digit.

And, sorry, the code is extremely ugly (not due to the patch) and inefficient.
Examples and parameter description can be improved as well.

I'm not quite sure what kind of strings actually get in (i.e., where/if illegal syntax is catched, it seems all is left to `RealNumber._set()` if not already handled by the parser), this should perhaps be documented, too.


---

Comment by leif created at 2010-05-27 15:03:06

Also, is it intentional that the exponent is ignored when computing the required precision?
E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.


---

Comment by leif created at 2010-05-27 16:01:29

`sage.rings.complex_number.create_ComplexNumber()` also needs work.

(It doesn't "strip" trailing/fractional zeros, but also doesn't treat a given exponent correctly. Bases (other than 10) aren't supported; perhaps it should just call `create_RealNumber()` or use the same code to compute the necessary precision once this operates as desired.)


---

Comment by robertwb created at 2010-05-27 18:48:51

apply on top of previous


---

Comment by robertwb created at 2010-05-27 18:51:01

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:6 leif]:
> No, the `else` belongs to the `for` statement.

Exactly. 

> But currently, _leading_ zeros contribute to the precision, too: :)
> {{{
> sage: RealNumber(0.000000000000000000).prec()
> 67
> sage: RealNumber(00.000000000000000000).prec()
> 70
> sage: RealNumber(.000000000000000000).prec()
> 64
> }}}
> I'm not sure if this is intentional, it's at least uncommon.

That's the point of this ticket. For 0, all zeros are leading. 

> (And a leading `+` also increases the precision.)
> 
> It looks as if a decimal point is counted as a significant digit.

Good catch, fixed. That required some adjustment to keep the input/str in sync. 

> And, sorry, the code is extremely ugly (not due to the patch) and inefficient.
> Examples and parameter description can be improved as well.
> 
> I'm not quite sure what kind of strings actually get in (i.e., where/if illegal syntax is catched, it seems all is left to `RealNumber._set()` if not already handled by the parser), this should perhaps be documented, too. 

Updated the docstring a bit. This is mostly for use by the preparser, though of course it gets used directly as well.


---

Comment by robertwb created at 2010-05-27 18:52:59

Replying to [comment:7 leif]:
> Also, is it intentional that the exponent is ignored when computing the required precision?
> E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.

Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures. I made create_ComplexNumber defer to create_RealNumber as well.


---

Comment by kcrisman created at 2010-05-27 19:29:04

> > No, the `else` belongs to the `for` statement.
> 
> Exactly. 

[Here](http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) is the reference for this - I hadn't seen that before.  Thanks for the additional docstring.


---

Comment by leif created at 2010-05-27 23:00:20

Just took a first glance:

 * `create_ComplexNumber()` now looks nice
 * in the above function, it's `len<15` instead of `len<=15`
 * `min_prec` can be smaller than 53 (if specified)
 * `pad` should be (tested to be) non-negative
 * (`min_prec` perhaps too, or `min_prec+pad>=0`) 
 * compare against `min_prec+pad` rather than individually for the "common" case
 * `rnd` description in `create_RealNumber()` is slightly messed up
 * IMHO leading zeros *left to the decimal point* should be stripped/ignored

More to come... ;-)

(I've only looked at the patch to the patch.)


---

Comment by leif created at 2010-05-27 23:26:56

Replying to [comment:9 robertwb]:
> Replying to [comment:6 leif]:
> > But currently, _leading_ zeros contribute to the precision, too: :)
> > {{{
> > sage: RealNumber(0.000000000000000000).prec()
> > 67
> > sage: RealNumber(00.000000000000000000).prec()
> > 70
> > sage: RealNumber(.000000000000000000).prec()
> > 64
> > }}}
> > I'm not sure if this is intentional, it's at least uncommon.
> 
> That's the point of this ticket. For 0, all zeros are leading. 

Not really. We were (only I think) considering zeros of the *fractional* part.

Truncation only makes sense from the right; and you don't express precision by padding zeros to the left. Stating that the earth's diameter is about 013 million meters doesn't give more information than stating it is about 13 million meters.

> Updated the docstring a bit. This is mostly for use by the preparser, though of course it gets used directly as well. 

I was thinking of scientific notation syntax, too. (Also the examples do not contain that form.)


---

Comment by leif created at 2010-05-27 23:40:39

Replying to [comment:13 leif]:
> Not really. We were (only I think) considering zeros of the *fractional* part.

To be more precise, 0.0 and 00.0 denote the same "thing", i.e. have the same meaning, while 0.0 and 0.00 do not.


---

Comment by jason created at 2010-05-28 00:14:36

For those interested in printing real numbers in general, I'll just plug #7682, which could use just a bit of polishing work, I believe, and makes printing real/complex numbers much more consistent and easy to adjust.


---

Comment by leif created at 2010-05-28 01:00:13

Replying to [comment:10 robertwb]:
> Replying to [comment:7 leif]:
> > Also, is it intentional that the exponent is ignored when computing the required precision?
> > E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.
> 
> Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures.

I don't agree either. If the "effective" exponent (the one in normalized form) exceeds the maximum, one should either increase `prec` accordingly or - more practical - raise an exception.

If not, this could be a pitfall. But *I* don't mind... ;-)


---

Comment by robertwb created at 2010-05-28 06:24:27

Replying to [comment:13 leif]:
> Replying to [comment:9 robertwb]:
> > That's the point of this ticket. For 0, all zeros are leading. 
> 
> Not really. We were (only I think) considering zeros of the *fractional* part.
> 
> Truncation only makes sense from the right; and you don't express precision by padding zeros to the left. Stating that the earth's diameter is about 013 million meters doesn't give more information than stating it is about 13 million meters.

Which has the same information as saying the Earth's diameter is about 0.000013 trillion meters. Whether or not a digit is significant is not a function of whether it is on the left or right of the decimal. 

Would you then say that `0.00e9` and `00.0e8` and `.000e10` have different precisions?


---

Comment by robertwb created at 2010-05-28 06:33:26

Replying to [comment:12 leif]:
> Just took a first glance:
> 
>  * `create_ComplexNumber()` now looks nice
>  * in the above function, it's `len<15` instead of `len<=15`

Ah, oops.

>  * `min_prec` can be smaller than 53 (if specified)

Yes, but I'm not following what you're trying to say here. 

>  * `pad` should be (tested to be) non-negative
>  * (`min_prec` perhaps too, or `min_prec+pad>=0`) 
>  * compare against `min_prec+pad` rather than individually for the "common" case

I don't care if pad is negative (I'll fix the docstring). Same with min_prec, I just pass whatever I get onto the RealField constructor which will raise a perfectly fine exception if the precision is not valid (as defined by MPFR_MIN_PREC and MPFR_MAX_PREC).

>  * `rnd` description in `create_RealNumber()` is slightly messed up

Ah, I'll fix that. 


> > > E.g., `1.0e-1000000000` as well as `1.0e-10000000000` evaluate to zero, because of only 53 bits precision.
> > 
> > Yes, of course. The size of the exponent is completely orthogonal to the number of significant figures.
> 
> I don't agree either. If the "effective" exponent (the one in normalized form) exceeds the maximum, one should either increase `prec` accordingly or - more practical - raise an exception.
> 
> If not, this could be a pitfall. But *I* don't mind... ;-)

Well, I'd say the above has only two significant digits of precision, no matter what the exponent, which is all this function tries to deduce. The fact that it's subnormal is outside of the scope of this ticket--if an exception should be raise it's not here. (And in this case you can't raise the precision enough, due to memory/library limitations.)


---

Comment by leif created at 2010-05-28 09:28:00

Replying to [comment:18 robertwb]:
> Replying to [comment:12 leif]:
> >  * `min_prec` can be smaller than 53 (if specified)
> 
> Yes, but I'm not following what you're trying to say here. 
> 
> >  * `pad` should be (tested to be) non-negative
> >  * (`min_prec` perhaps too, or `min_prec+pad>=0`) 
> >  * compare against `min_prec+pad` rather than individually for the "common" case
> 
> I don't care if pad is negative (I'll fix the docstring). Same with min_prec, I just pass whatever I get onto the RealField constructor which will raise a perfectly fine exception if the precision is not valid (as defined by MPFR_MIN_PREC and MPFR_MAX_PREC).

If you test for `min_prec+pad==53 and ...`, more inputs fall into the simple common case (`RR`).
(Using `RR`, i.e. 53 bit mantissa, if the sum is _less_ than 53 is perhaps not desired.)


---

Comment by leif created at 2010-05-28 12:47:02

Replying to [comment:19 leif]:
> (Using `RR`, i.e. 53 bit mantissa, if the sum is _less_ than 53 is perhaps not desired.)
> 

Must have been some spot on the screen that covered `min_`... ;-)

Of course it's pretty ok to return `RR` in that case, too. (If someone really wants _less_ precision, he can use `RealField(prec)("...")` directly.)


---

Attachment

Doctest fixes for 4.6.1.


---

Comment by robertwb created at 2011-05-31 07:03:39

Folded and rebased on 4.7. Apply only this patch.


---

Comment by mariah created at 2011-06-06 17:38:28

Changing status from needs_review to positive_review.


---

Attachment

Patch fixes problem.  Ran 'make testlong'.  All tests passed.  Positive review!


---

Comment by robertwb created at 2011-06-06 17:47:41

Thanks!


---

Comment by jdemeyer created at 2011-06-08 07:32:18

Changing status from positive_review to needs_info.


---

Comment by jdemeyer created at 2011-06-08 07:32:18

In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 *should* be treated differently than 0.0000000000000.

I really think the current behaviour of Sage is what makes the most sense (mathematically) so I am not in favour of this ticket.  Of course, if the majority thinks this patch is a good idea then I'm all for it.

One thing about the patch which is very unclear is why zero is treated differently from other numbers.  Consider::

```
sage: (0.0).prec()
53
sage: (0.1).prec()
53
sage: (000000000000000000000.0).prec()
77
sage: (000000000000000000000.1).prec()
53
sage: (0.000000000000000000000).prec()
77
sage: (0.000000000000000000001).prec()
53
```



---

Comment by robertwb created at 2011-06-08 15:41:09

Replying to [comment:25 jdemeyer]:
> In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 *should* be treated differently than 0.0000000000000.

It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. 

> I really think the current behaviour of Sage is what makes the most sense (mathematically) so I am not in favour of this ticket.  Of course, if the majority thinks this patch is a good idea then I'm all for it.
> 
> One thing about the patch which is very unclear is why zero is treated differently from other numbers.  

Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). 

> Consider::
> {{{
> sage: (0.0).prec()
> 53
> sage: (0.1).prec()
> 53
> sage: (000000000000000000000.0).prec()
> 77
> sage: (000000000000000000000.1).prec()
> 53
> sage: (0.000000000000000000000).prec()
> 77
> sage: (0.000000000000000000001).prec()
> 53
> }}}


---

Comment by kcrisman created at 2011-06-08 15:56:54

Another argument is that the BDFL suggested this change fairly strongly when opening this ticket :)

More seriously, I do have a question here.
Robert's reasoning seems sound in the following example - we want a high-precision zero, and this is the best way to acquire it.

```
> sage: (0.000000000000000000000).prec()
> 77
> sage: (0.000000000000000000001).prec()
> 53
```

But I agree with Jeroen that the following seems problematic.  Didn't you say yourself (robertwb) that leading zeros _before_ the decimal point shouldn't make a difference?  So in the case here maybe we should have the default precision...

```
> sage: (000000000000000000000.0).prec()
> 77
> sage: (000000000000000000000.1).prec()
> 53
```

Keeping in mind that I have very little invested in either outcome for now, so take these only as observations.


---

Comment by jdemeyer created at 2011-06-08 16:01:57

Replying to [comment:26 robertwb]:
> Replying to [comment:25 jdemeyer]:
> > In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 *should* be treated differently than 0.0000000000000.
> 
> It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. 
It is absolutely _not the same_ because with non-zero numbers only digits *after* a non-zero digit contribute to the precision.  Indeed, `0.437` and `0.00000000000437` have exactly the same precision.

> Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). 
Well, you can always do:

```
sage: zero = RealField(1000)(0)
sage: zero.prec()
1000
```


An other way to demonstrate the problem with this patch is that truncating decimal numbers (i.e. removing digits from the right) can _increase_ the precision, which is very unlogical::

```
sage: (0.000000000000000000001234567890123456789).prec()
67
sage: (0.00000000000000000000123456789012345678).prec()
64
sage: (0.000000000000000000001).prec()
53
sage: (0.00000000000000000000).prec()
74
```



---

Comment by robertwb created at 2011-06-08 16:19:58

Replying to [comment:28 jdemeyer]:
> Replying to [comment:26 robertwb]:
> > Replying to [comment:25 jdemeyer]:
> > > In my opinion, this ticket is a huge can of worms and a bad idea.  I don't see any mathematically consistent reason who 0.0 *should* be treated differently than 0.0000000000000.
> > 
> > It's exactly the same reason that 1.0 is treated differently than 1.0000000000000000000000. The (value-preserving) trailing zeros indicate higher precision. 
> It is absolutely _not the same_ because with non-zero numbers only digits *after* a non-zero digit contribute to the precision.  Indeed, `0.437` and `0.00000000000437` have exactly the same precision.

This hinges on the ambiguity of the term "trialing zero." Sage interprets trailing zeros after the decimal point as additional precision. To me, trailing zeros are those that are not followed by a non-zero digit, to you trailing zeros must also follow a non-zero digit. 

> > Because otherwise there's now way to write a high-precision zero (in fact I can't think of any other interpretation of a large number of trailing zeros). 
> Well, you can always do:
> {{{
> sage: zero = RealField(1000)(0)
> sage: zero.prec()
> 1000
> }}}

Yeah, but that's a pain, but to me the fact that 0.00000000000000000000000000000000 is not high precision is more surprising, as it has many significant digits. 

> An other way to demonstrate the problem with this patch is that truncating decimal numbers (i.e. removing digits from the right) can _increase_ the precision, which is very unlogical::
> {{{
> sage: (0.000000000000000000001234567890123456789).prec()
> 67
> sage: (0.00000000000000000000123456789012345678).prec()
> 64
> sage: (0.000000000000000000001).prec()
> 53
> sage: (0.00000000000000000000).prec()
> 74
> }}}

It also changes the relative value by a huge amount :) 

Is it worth taking this discussion to sage-devel?


---

Comment by jdemeyer created at 2011-06-08 19:07:45

Replying to [comment:29 robertwb]:
> to me the fact that 0.00000000000000000000000000000000 is not high precision is more surprising, as it has many significant digits.
I would say that it does have a lot of _digits_ but that none of them is a _significant digit_.


---

Comment by was created at 2011-08-24 23:43:21

Changing keywords from "" to "sd32".
