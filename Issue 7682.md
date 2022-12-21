# Issue 7682: Customize printing of real numbers

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-12-14 20:29:00

Assignee: AlexGhitza

CC:  robertwb jkantor was kcrisman egourgoulhon

From http://groups.google.com/group/sage-support/browse_thread/thread/06756df51d828bf4


```
we probably ought to make this easier to just print the 
first n digits after the decimal by default for RR numbers, or to not 
print out the trailing zeros.  I can't imagine telling my students, for 
example, that they need to do '%.3f'%num every time they come across a 
number, especially since they just want to display the equation, not 
format it as a string.

What do people think about this interface?

sage: RR.print_digits=3
sage: 3.09384
3.094
sage: RR.print_trailing_zeros=False
sage: RR.print_digits=None
sage: 3.09384
3.09384

Make it something like the RR.scientific_notation flag that is currently 
in use.
```


Additionally, and more flexibly, we could just have something like:


```

sage: RR.set_print_format('%.3f')
sage: RR(pi)
3.142
```


or more pythonically


```
sage: RR.print_format = '%.3f'
sage: RR(pi)
3.142
```



---

Comment by jason created at 2009-12-14 20:29:37

Note that these extra zeros were introduced in the printing by the switch to pynac.  They were eliminated a while ago in maxima by #4572.


---

Comment by was created at 2009-12-24 07:07:39

I'm declaring a total feature freeze on sage-4.3.


---

Comment by jason created at 2010-01-25 13:43:01

Here is a first cut of a print_options model for RealField that lets you specify default printing options for any RealField, all RealFields, and still lets you override the defaults when you actually print the numbers.

It mostly works.  Docs need to be updated, deprecation warnings need to be added, and the interface for scientific notation needs to be revamped (no_sci and sci_not are confusing and inconsistent keyword choices!).


---

Comment by jason created at 2010-01-25 13:43:01

Changing status from new to needs_work.


---

Comment by jason created at 2010-01-25 13:43:27

Changing component from basic arithmetic to numerical.


---

Comment by jason created at 2010-01-26 05:50:36

I refreshed the patch which a much more comprehensive patch.  This patch fixes all doctests in rings/*.pyx (running long doctests now).  Documentation still needs to be updated, though, and some new doctests to test the new functionality.


---

Comment by jason created at 2010-01-26 06:16:16

Okay, patch passes all (non-long) doctests in Sage.


---

Comment by robertwb created at 2010-01-26 06:26:07

Usually rings are supposed to be immutable, but I think this general idea is worth it. As for the interface, setting attributes on RR directly isn't very consistent with the way we do things in Sage--it's probably be better to have a RR.print_options(...) that takes keywords. (This way it could have a nice docstring as well.)


---

Comment by robertwb created at 2010-01-26 06:26:07

Changing status from needs_work to needs_info.


---

Comment by jason created at 2010-01-26 06:41:30

Thanks for the style review.  Okay, I can change print_options to a function, though I don't think it's "better", maybe just more consistent and slightly worse (i.e., unpythonic and more typing)

On another note, I just changed the latexing of a real field to indicate the precision and rounding, so that RealField(100,rnd='RNDD') prints as \Bold{R}^{-}_{100}.  The subscript is the precision, the superscript is '+' for RNDU, '-' for RNDD, 0 for RNDZ, and nothing for RNDN.  What do you think?  It mirrors better the textual description of the field that indicates precision and rounding.


---

Comment by jason created at 2010-01-26 06:44:34

As for immutability; what if we don't consider the printing options as part of the ring (i.e., it's not part of the hash for the cache, like it is now)?  Then a user can temporarily change the ring's printing operations, but none of the printing options are considered in testing for equality, stored in pickles, etc.


---

Comment by jason created at 2010-01-26 07:38:30

Replying to [comment:8 robertwb]:
> it's probably be better to have a RR.print_options(...) that takes keywords. (This way it could have a nice docstring as well.) 

Yes, but how do you get the value of a specific option (as opposed to setting it).


---

Comment by jason created at 2010-01-26 07:44:20

Replying to [comment:8 robertwb]:
> (This way it could have a nice docstring as well.) 

The Cython "property" construct can also take a nice docstring.  Is anything ever done with this docstring?


---

Attachment

Okay, this is getting big now.  I went through real_mpfr.pyx and added a lot of doctests and documentation.

There are four doctests failing right now because I'm not sure if they are bugs or if they are right.  Here they are:


```
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3343:
    sage: RR('nan').is_real() # fail until we decide what it should be
Expected nothing
Got:
    True
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3344:
    sage: RR('inf').is_real() # fail until we decide what it should be
Expected nothing
Got:
    True
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3360:
    sage: RR('nan').__nonzero__() # fail until we decide what it should be
Expected nothing
Got:
    False
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3397:
    sage: RR('nan')==RR('nan') # Fail until we decide what it should be
Expected nothing
Got:
    True
**********************************************************************
File "/home/grout/sage-4.3.1/devel/sage-main/sage/rings/real_mpfr.pyx", line 3419:
    sage: RR('nan')==RR('nan') # fail until we decide what it should be
Expected nothing
Got:
    True
```


Are those four answers right (the "Got:" parts)?  See #8074 for more corner cases.


---

Comment by jason created at 2010-02-27 22:34:21

I rebased this patch to apply to 4.3.3 (it conflicted with a big rewrite by was and a small patch by robertwb).  The patch touches a lot of areas (and adds lots of doctests!), so a quick review would help avoid having to rebase it again.


---

Attachment

apply instead of previous patch.  Rebased to Sage 4.3.3


---

Comment by jason created at 2010-02-28 05:00:02

I uploaded a new patch which corrects several doctests; all doctests in Sage now seem to pass with this patch applied.


---

Comment by jason created at 2010-03-17 05:13:24

Changing type from defect to enhancement.


---

Comment by jason created at 2010-03-17 05:13:51

Changing status from needs_info to needs_review.


---

Comment by jason created at 2010-05-14 17:06:15

rebase to 4.4.1, apply only this patch


---

Attachment

I removed a bunch of fixes unrelated to the printing option change and put them on other tickets.  I also fixed at least one accidental code removal.  In 4.4.1, Sage won't start after this patch is applied, due to


```
----------------------------------------------------------------------
----------------------------------------------------------------------
init2.c:52: MPFR assertion failed: p >= 2 && p <= ((mpfr_prec_t)((mpfr_prec_t)(~(mpfr_prec_t)0)>>1))
/Users/grout/sage/local/bin/sage-sage: line 206: 16842 Abort trap              sage-ipython "$`@`" -i
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |
```



---

Comment by jason created at 2010-05-14 17:07:52

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-05-14 18:20:04

rebase to 4.4.1, fix startup bug,  apply only this patch


---

Attachment

rebase to 4.4.1, fix startup bug,  fix one doctest to test for the startup bug; apply only this patch


---

Comment by leif created at 2010-05-28 01:34:26

Slightly OT: Regarding the thread that started this, in finance you don't need less/limited precision, but _fixed_-point numbers. ;-)


---

Comment by jason created at 2010-05-28 02:16:45

Replying to [comment:19 leif]:
> Slightly OT: Regarding the thread that started this, in finance you don't need less/limited precision, but _fixed_-point numbers. ;-)
> 

Of course, then you would probably use the python Decimal module :).


---

Comment by jason created at 2010-05-28 02:17:48

My reason for initially working on this was for a numerical analysis class, where we wanted to see *all* the digits of the real number, and not just have the last few digits rounded off.


---

Comment by jason created at 2010-06-18 16:03:13

#9261 asks for one of the features implemented in this patch (setting the printing style for real interval fields).


---

Comment by jason created at 2010-06-18 16:22:17

After experimenting for a few minutes, it looks like something like #9261 is almost implemented in this patch, but not quite.


---

Comment by jason created at 2010-06-18 17:32:53

apply on top of previous patch


---

Attachment

I added a patch which implements the feature wanted in #9261:


```
sage: R=RealIntervalField(print_options=dict(style='brackets'))
sage: R.print_options
{'style': 'brackets', 'error_digits': 0}
sage: R(1,2)
[1.0000000000000000 .. 2.0000000000000000]
```


Doctests and documentation still needs to be written for this.  And maybe convenience functions for setting these two options (i.e., make the syntax in #9261 work).


---

Comment by zimmerma created at 2010-06-19 09:19:05

Jason,

sorry, I was not aware of this ticket. I see you have invested a lot of time in it. However I am
not in favour of removing trailing zeroes by default. Those zeroes are quite helpful to give an
idea of the accuracy of the computation.

About reducing or increasing the number of printed zeroes with respect to the internal precision,
I don't see why this could be desirable. If we reduce the number of printed zeroes, then if we
copy/paste the number, we will loose some accuracy (because of the decimal<->binary conversion).
If we increase the number of printed zeroes, the user will see more significant digits (due to
the internal binary representation) and this will lead to more user questions:

```
sage: a=n(pi); a
3.14159265358979
sage: print '%.3f'%a
3.142
sage: b=3.142; a-b
-0.000407346410206788
sage: print '%.30f'%a
3.141592653589793115997963468544
```


In addition I don't understand how you achieve this:

```
sage: RR.print_trailing_zeros=False
sage: RR.print_digits=None
sage: 3.09384
3.09384
```

What happens with `RR.print_digits=16`?

Also, what happens with numbers with tiny or huge exponent, say `3.09384e-100` or
`3.09384e+100`?

Just my 2 cents.

Paul

PS: however, the patch for #9261 looks very nice. Can't you make it independent of that ticket?


---

Comment by jason created at 2010-06-19 12:24:51

Replying to [comment:25 zimmerma]:
> Jason,
> 
> sorry, I was not aware of this ticket. I see you have invested a lot of time in it. However I am
> not in favour of removing trailing zeroes by default. Those zeroes are quite helpful to give an
> idea of the accuracy of the computation.

I agree. That's the default in Sage now, though (and led to this patch, as it was hiding too much in my numerical analysis class!)

So changing it should probably be a different ticket, and after this patch, should just be a one liner change to the defaults.


> 
> About reducing or increasing the number of printed zeroes with respect to the internal precision,
> I don't see why this could be desirable. If we reduce the number of printed zeroes, then if we
> copy/paste the number, we will loose some accuracy (because of the decimal<->binary conversion).
> If we increase the number of printed zeroes, the user will see more significant digits (due to
> the internal binary representation) and this will lead to more user questions:
> {{{
> sage: a=n(pi); a
> 3.14159265358979
> sage: print '%.3f'%a
> 3.142
> sage: b=3.142; a-b
> -0.000407346410206788
> sage: print '%.30f'%a
> 3.141592653589793115997963468544
> }}}
> 
> In addition I don't understand how you achieve this:
> {{{
> sage: RR.print_trailing_zeros=False
> sage: RR.print_digits=None
> sage: 3.09384
> 3.09384
> }}}
> What happens with `RR.print_digits=16`?
> 
> Also, what happens with numbers with tiny or huge exponent, say `3.09384e-100` or
> `3.09384e+100`?

Good questions.  It's been a while since I worked with this patch (other than the rough patch from yesterday).  I'll try to see what changes are changes I made, as opposed to what things were already in Sage.  The things that were already in Sage can be dealt with on another ticket.


> 
> Just my 2 cents.
> 
> Paul
> 
> PS: however, the patch for #9261 looks very nice. Can't you make it independent of that ticket?

Yes, though it's easier to build on top of the framework here, and I hope better in the long run.


---

Comment by jason created at 2010-07-11 06:51:54

Applying these patches to 4.4.2 gives several doctest errors like this:


```
sage -t  "4.4.2-test3/devel/sage-main/sage/rings/rational_field.py"
**********************************************************************
File "/Users/grout/sage-4.4.2-test3/devel/sage-main/sage/rings/rational_field.py", line 26:
    sage: QQ(RealField(9).pi())
Exception raised:
    Traceback (most recent call last):
      File "/Users/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        QQ(RealField(Integer(9)).pi())###line 26:
    sage: QQ(RealField(9).pi())
      File "parent.pyx", line 854, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
      File "rational.pyx", line 367, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)
        self.__set_value(x, base)
      File "rational.pyx", line 455, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:6223)
        set_from_Rational(self, x.simplest_rational())
      File "real_mpfr.pyx", line 2762, in sage.rings.real_mpfr.RealNumber.simplest_rational (sage/rings/real_mpfr.c:17811)
        return hp_intv.simplest_rational(low_open=odd, high_open=odd)
      File "real_mpfi.pyx", line 2742, in sage.rings.real_mpfi.RealIntervalFieldElement.simplest_rational (sage/rings/real_mpfi.c:14640)
        highprec = RealIntervalField_class(int(self.prec() * 1.2))(self)
      File "real_mpfi.pyx", line 472, in sage.rings.real_mpfi.RealIntervalField_class.__init__ (sage/rings/real_mpfi.c:3522)
        for key,val in print_options.items():
    AttributeError: 'NoneType' object has no attribute 'items'

```



---

Comment by jason created at 2010-07-11 06:57:44

It appears that the problem above occurs with just the last patch.


---

Comment by jason created at 2010-07-11 07:12:42

Paul: I think I understand your comment now.  I did not implement the original suggestion, but instead provided a framework for field-wide printing options and just wrapped what Sage currently provides.  You bring up some good questions about the design which are out of scope for the current patch attached.  Given this, I think it would be best to either change the scope of the ticket to reflect what the patch actually does, or make a new ticket for the patch and keep this ticket around for a design discussion of how (or whether it is desirable!) to implement the features described in the description.


---

Comment by zimmerma created at 2010-07-11 16:41:08

Replying to [comment:29 jason]:
> it would be best to either change the scope of the ticket to reflect what the patch actually does
I would prefer this.

Paul


---

Comment by cwitty created at 2010-07-11 19:30:02

I actually dislike the goal of this patch: I don't think it's a good idea to have `RealNumber` printing varied per-parent, and certainly not if the printing is mutable.  Consider:

Somebody wants to know what 128 bits of $\pi$ prints as in scientific notation:


```
sage: RR128 = RealField(128)
sage: RR128.print_options['scientific_notation'] = 'always'
sage: RR128(pi)
3.1415926535897932384626433832795028842e0
```


Then, days later (but in the same Sage session) they're playing around with the internals of AA/QQbar:


```
sage: rt2 = AA(sqrt(2))
sage: rt2._value.center()
1.41421356237309505
sage: RealIntervalField(100)(rt2)
1.414213562373095048801688724210?
sage: rt2._value.center()
1.4142135623730950488016887242096980786e0
```


Why is that last number printed in scientific notation?  Oh yes, it's because we changed RR128 days ago.

I realize that you're just extending a design that's been in Sage for years (since before I started working on Sage), but IMHO it's a bad design, and this just makes it worse.

I can think of two ways to fix this:

1) Get rid of per-field printing options altogether; only have a single global setting that affects all `RealField`s.

2) Make the print options immutable, so that creating RR128scientific_notation doesn't affect anybody else who might create RR128 without scientific notation.

My vote would be for option 1, but I could live with either option.


---

Comment by jason created at 2010-07-12 14:40:56

Replying to [comment:32 cwitty]:
> I actually dislike the goal of this patch: I don't think it's a good idea to have `RealNumber` printing varied per-parent, and certainly not if the printing is mutable.  Consider:
> 
> Somebody wants to know what 128 bits of $\pi$ prints as in scientific notation:
> 
> {{{
> sage: RR128 = RealField(128)
> sage: RR128.print_options['scientific_notation'] = 'always'
> sage: RR128(pi)
> 3.1415926535897932384626433832795028842e0
> }}}
> 
> Then, days later (but in the same Sage session) they're playing around with the internals of AA/QQbar:
> 
> {{{
> sage: rt2 = AA(sqrt(2))
> sage: rt2._value.center()
> 1.41421356237309505
> sage: RealIntervalField(100)(rt2)
> 1.414213562373095048801688724210?
> sage: rt2._value.center()
> 1.4142135623730950488016887242096980786e0
> }}}
> 
> Why is that last number printed in scientific notation?  Oh yes, it's because we changed RR128 days ago.
> 
> I realize that you're just extending a design that's been in Sage for years (since before I started working on Sage), but IMHO it's a bad design, and this just makes it worse.
> 
> I can think of two ways to fix this:
> 
> 1) Get rid of per-field printing options altogether; only have a single global setting that affects all `RealField`s.
> 
> 2) Make the print options immutable, so that creating RR128scientific_notation doesn't affect anybody else who might create RR128 without scientific notation.
> 
> My vote would be for option 1, but I could live with either option.


I agree.  Another reason to add to your argument above is that Sage does coercing between different realfield precisions, so you might have a number that is printed one way, then Sage automatically coerces to a different precision for an operation and your result is printed a different way.  I think (1) is a better option, given the caching strategy used.

For my use-case (teaching numerical analysis), option (1) is better than the patch on this ticket.

So do you propose eliminating the sci_not options to RealField?  Do you propose eliminating the arguments to the str function?

Note that I think your suggestion will be relatively straightforward to accommodate on this patch, since the patch defines module-level defaults.  We should be able to just remove the code that overrides the module-level defaults and stores a user value.  Note that this patch also unifies several different options for scientific notation that were scattered in different places in the code, so I think it is better to build (or cut things out) on this patch rather than throw it away altogether.


---

Comment by cwitty created at 2010-07-12 16:25:01

So do you propose eliminating the sci_not options to RealField?? Do you propose eliminating the arguments to the str function? 

Yes, my vote would be to eliminate sci_not in `RealField`.  No, I don't see any reason to eliminate the arguments to str(); if you want to convert a single number to a string in some special way (with scientific notation, say), then it's a lot easier to call .str(scientific_notation='always') than to type something like:


```
  old = sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation']
  sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation'] = 'always'
  foostr = foo.str()
  sage.rings.real_mpfr._PRINT_OPTIONS['scientific_notation'] = old
```


Further comments:

I haven't really reviewed the actual patch, but I did just notice that the new docstring for .str() has no doctests for no_sci.  I think it should end with something like:


```
TESTS:

Here we test the deprecated no_sci argument to .str()::
```


followed by the tests for no_sci that used to be there (assuming there were some, I haven't actually checked).


---

Comment by leif created at 2011-07-22 09:34:11

ping (?)


---

Comment by jason created at 2011-07-22 14:55:56

pong.  I would love to see this ticket resolved, but as you can see, there is another major rewrite needed before it is ready.


---

Comment by nbruin created at 2018-05-20 06:28:27

How lovely to revive an 8 year old ticket ...

In the mean time, python has grown a new string formatting method. If we implement a `__format__` method on our mpfr wrapper, one could just do something like

```
sage: a=RealField(200)(2).sqrt()
sage: "{:.20e}".format(a)
'1.414213562373095049e0'
```

No need to fuss with global state ... if people want more control over the typesetting of their floats, they can just use the standard python tools (or the tools already available on `str`).

It might be a nice beginner's exercise to write the appropriate `__format__`.


---

Comment by @sheerluck created at 2019-04-14 09:21:25

I wanted to have fun with `e` to the power of `π√163`

I expected Sage would print me `262537412640768743.99999999999925`

```
sage: R = RealField(1500)
sage: a = R(e) ** (R(pi) * R(163).sqrt())
sage: a.n(digits=33)
2.62537412640768743999999999999250e17
sage: "{:.70f}".format(a)
TypeError: unsupported format string passed to sage.rings.real_mpfr.RealNumber.__format__
```

is there a way to print `2.62537412640768743999999999999250e17` as `262537412640768743.99999999999925`?


---

Comment by egourgoulhon created at 2019-04-14 09:56:48

Replying to [comment:44 gh-sheerluck]:
> I wanted to have fun with `e` to the power of `π√163`
> 
> I expected Sage would print me `262537412640768743.99999999999925`
> {{{
> sage: R = RealField(1500)
> sage: a = R(e) ** (R(pi) * R(163).sqrt())
> sage: a.n(digits=33)
> 2.62537412640768743999999999999250e17
> sage: "{:.70f}".format(a)
> TypeError: unsupported format string passed to sage.rings.real_mpfr.RealNumber.__format__
> }}}
> is there a way to print `2.62537412640768743999999999999250e17` as `262537412640768743.99999999999925`?

A solution is:

```
sage: n(exp(pi*sqrt(163)), digits=33).str(no_sci=2)
'262537412640768743.999999999999249212'
```



---

Comment by @sheerluck created at 2019-04-14 10:13:40

Replying to [comment:45 egourgoulhon]:
> 
> A solution is:
> {{{
> sage: n(exp(pi*sqrt(163)), digits=33).str(no_sci=2)
> '262537412640768743.999999999999249212'
> }}}
Thank you!
