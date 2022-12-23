# Issue 8799: Bring doctests for mwrank.pyx up to 100% (from 3%)

Issue created by migration from https://trac.sagemath.org/ticket/8799

Original creator: cremona

Original creation time: 2010-04-28 08:11:56

Assignee: mvngu

CC:  rlm

Keywords: mwrank

Improve documentation for this:

```
sage/libs/mwrank/mwrank.pyx:  3% (1 of 30)
```



---

Comment by cremona created at 2010-04-28 20:36:14

I am working on this (started 2010-04-28) -- John


---

Comment by cremona created at 2010-05-02 19:59:57

The patch provides 100% doctests to sage/libs/mwrank (both files mwrank.pyx and interface.py), as well as adding them to the reference manual.

This is 95% in the docstrings, but I did find a few fairly minor bugs (mainly in the documentation not saying what various parameters did precisely).

Patch up very soon -- just doing final testing.


---

Comment by cremona created at 2010-05-02 20:00:29

Applies to 4.4


---

Attachment

I am flagging this as "needs review", while still testing.  Not expecting any surprises since the patch is almost entirely in docstrings.  (I did also test the building of the docs).


---

Comment by cremona created at 2010-05-02 20:01:50

Changing status from new to needs_review.


---

Comment by cremona created at 2010-05-09 21:25:13

Replying to [comment:3 cremona]:
> I am flagging this as "needs review", while still testing.  Not expecting any surprises since the patch is almost entirely in docstrings.  (I did also test the building of the docs).

Just in case anyone reading the above thinks that this is not ready for testing & reviewing -- it is!


---

Attachment

based on Sage 4.4.2.alpha0


---

Comment by mvngu created at 2010-05-10 11:39:09

With the patch [trac_8799-mwrank-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-mwrank-doctest.patch), I got the following failures on sage.math:


```
[mvngu@sage sage-4.4.2.alpha0-8799-mwrank-doctest]$ ./sage -t -long devel/sage-main/sage/libs/mwrank/mwrank.pyx
sage -t -long "devel/sage-main/sage/libs/mwrank/mwrank.pyx" 
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8799-mwrank-doctest/devel/sage-main/sage/libs/mwrank/mwrank.pyx", line 428:
    sage: E.discriminant()
Expected:
    -1269581104000000L
Got:
    -1269581104000000
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-8799-mwrank-doctest/devel/sage-main/sage/libs/mwrank/mwrank.pyx", line 455:
    sage: E.conductor()
Expected:
    126958110400L
Got:
    126958110400
P1 = [0:1:0]	 is torsion point, order 1
P1 = [-3:0:1]	  is generator number 1
saturating up to 20...Checking 2-saturation 

<output truncated>

Searching for points (bound = 8)...done:
  found points of rank 3
  and regulator 0.41714355875838396981711954461809339674981010609846
Processing points found during 2-descent...done:
  now regulator = 0.41714355875838396981711954461809339674981010609846
No saturation being done
```


The reviewer patch fix this issue and a bunch of typos. What we need now is someone to review the technical aspect of John's patch. Unfortunately, I'm not at all familiar with elliptic curves.


---

Comment by cremona created at 2010-05-10 16:41:33

Many thanks for the reviewer patch, and many many apologies for all those typose & other things which I missed converting from old-style docstring format to ReST.

For info:  the removal of the trailing L on those output constants is correct:  I converted various integers in the output to Sage integers (they were python ints).

I CC'd rlm, hoping that he'll be able to look at this too.


---

Comment by leif created at 2010-05-10 17:04:17

Hmm, what's the convention for typesetting numbers, isolated or e.g. in _2-descent_?

Math mode looks very ugly (and isn't consistently used).

Also, _Python_ should be uppercase, and _Sha_ should be _SHA_ I guess.

There are also some (non-)references e.g. to _2-descent_ where I guess `:meth:`two_descent`` should be used.

Btw, both patches work for 4.4.1.rc0 (which is almost 4.4.1), too, and doctests pass.
I only get an error when building PDF documentation, due to some reference with an underscore(?), haven't yet closely looked at that.

-Leif


---

Comment by leif created at 2010-05-10 17:11:10

Replying to [comment:7 leif]:
> I only get an error when building PDF documentation, due to some reference with an underscore(?), haven't yet closely looked at that.

Sorry, perhaps completely unrelated to _this_ patch/ticket.


---

Comment by leif created at 2010-05-10 17:37:10

Replying to [comment:7 leif]:
> Also, ..[...] _Sha_ should be _SHA_ I guess.

Ouch, it's actually the cyrillic Sha. :)

Sorry again.


---

Comment by cremona created at 2010-05-10 17:53:26

Replying to [comment:9 leif]:
> Replying to [comment:7 leif]:
> > Also, ..[...] _Sha_ should be _SHA_ I guess.
> 
> Ouch, it's actually the cyrillic Sha. :)

That's right.  I don't know if we can access such fonts in the docs.  I think the other inconsistencies have been dealt with by Minh.

   John

> Sorry again.


---

Comment by leif created at 2010-05-10 18:35:27

Replying to [comment:10 cremona]:
> I think the other inconsistencies have been dealt with by Minh.
No, not really. Minh introduced _some_ math-typeset numbers - isolated and within words (but did not change all occurrences), and did not "change" all method references.

There's also some reference to Python's (deprecated) `long`.

The typesetting of Python (variable) names (and e.g. _true_ instead of `True`) is not fully consistent, too.

(The return value descriptions use both passive and imperative form, too. ;-) )

But I don't want to grumble to much...


---

Comment by cremona created at 2010-05-10 19:02:18

Feel free to add a second reviewer's patch!


---

Attachment

A (rough) second reviewer patch based on Minh's.


---

Comment by leif created at 2010-05-10 23:20:04

Better first look at the diff (before applying the patch); I've changed various things (including a typo in the actual code), but haven't reverted anything Minh changed (at least I think so), i.e. math-typeset numbers etc. still look ugly. ;-)

I've (yet) changed little in `mwrank.pyx`, because I can't find documentation generated from anything but the two pure Python functions... ;-)

-Leif

P.S.: Minh, the prev/next topic for me doesn't work as expected... 8|


---

Comment by leif created at 2010-05-10 23:33:42

P.P.S.: John, I've also added some `TODO`s. Btw, do we initialise or initialize? ;-)


---

Attachment

I have made some more changes to the docstring of `interface.py` and `mwrank.pyx`. My second reviewer patch [trac_8799-reviewer-part3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-part3.patch) includes changes in addition to the original reviewer patch and leif's patch. With many patches to apply, it can be confusing to see what changes the reviewers propose. So I have folded the reviewers' patches into one mega patch called [trac_8799-reviewer-total.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-total.patch).



Also notice that I move documentation for constructor methods, i.e. `__init__`, into the docstring of a class. The main reason is that, currently the docstring of `__init__` don't show up on the reference manual once you built it. 



To rebuild the whole reference manual, you could do the following from `SAGE_ROOT`, assuming you applied the patches to the branch main:


```sh
./sage -b main
./sage -docbuild reference html
```


If you want to be thorough and want to check that the new documentation build OK, do:


```sh
rm -rf devel/sage-main/doc/output/
./sage -b main
./sage -docbuild reference html
```



---

Comment by leif created at 2010-05-11 02:24:56

4th reviewer patch on top of Minh' second (-part3). Fixes 1 doctest failure, too.


---

Attachment

Sorry, yet another patch. (It also fixes a doctest failure *introduced by me*. 8/ )

Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)

Shouldn't we replace

```
 - foo (bool) -- ...
 - bar (int, default 12) -- ...
```

by

```
 - foo (:class:`bool`) -- ...
 - bar (:class:`int`, default 12) -- ...
```

too?

-Leif

P.S.: Note that despite the ticket title, my patches also change the code.


---

Comment by mvngu created at 2010-05-11 03:43:58

cumulative of all reviewers' patches


---

Attachment

Replying to [comment:16 leif]:
> Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)

I'm not particularly picky about this issue. What you proposed in your patches are OK by me. I have folded all our reviewer patches into one cumulative patch. Even your second reviewer patch has been folded into [trac_8799-reviewer-total.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8799/trac_8799-reviewer-total.patch).




> Shouldn't we replace

```
- foo (bool) -- ...
- bar (int, default 12) -- ...
```

> by

```
- foo (:class:`bool`) -- ...
- bar (:class:`int`, default 12) -- ...
```

> too?

That is OK by me. But I would prefer something like "boolean", "integer", "real number", etc. Something as "meaningful" as possible, without recourse to type information. We now need someone to review the technical (mathematical) aspect of John's patch, and a sign off on my review patch. I'm OK with your patches. That is, someone other than myself need to look over the cumulative reviewer patch.


---

Comment by leif created at 2010-05-11 04:29:50

Replying to [comment:17 mvngu]:
> Replying to [comment:16 leif]:
> > Minh, you vote in favour of math-typeset numbers? (I don't like e.g. ``L`-functions` either...)
> 
> I'm not particularly picky about this issue. What you proposed in your patches are OK by me.
Well, I haven't reverted your changes of e.g. `1` to ``1``; the HTML output is not very nice...

> I have folded all our reviewer patches into one cumulative patch.
Yes, of course noticed that.

> I would prefer something like "boolean", "integer", "real number", etc. Something as "meaningful" as possible, without recourse to type information.
This might not sound pythonic, but I'd prefer documenting the concrete type if the function actually expects some Python type (rather than a duck).

> We now need someone to review the technical (mathematical) aspect of John's patch,
rlm?

> and a sign off on my review patch.
I've positively reviewed _your_ changes... :)

So unfortunately someone else (other than John and us) has to review the cumulative reviewer patch to avoid mutual peer-reviewing on the same ticket (some people seem to have no problems with this, I do).


---

Comment by cremona created at 2010-05-11 08:23:13

Changing assignee from mvngu to cremona.


---

Comment by cremona created at 2010-05-11 08:23:13

For what it's worth, thanks again to both, and I am quite happy with the combined reviewer patch (trac_8799-reviewer-total.patch).

I did not see the typo in the code which Leif mentioned.  Is it where we test height_bound > 21.4 and not 21.48?  In that place, it is true that this could be approximately doubled on 64-bit machines (I guess that when this code was first written the person doing it did not know how to test that) but in practice using bounds > 21 will take a very very long time.

So we still need an independent reviewer... and some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?


---

Comment by leif created at 2010-05-12 17:18:53

Replying to [comment:19 cremona]:
> I did not see the typo in the code which Leif mentioned.  Is it where we test height_bound > 21.4 and not 21.48?
No. I meant:

```
-        verbose == bool(verbose)
+        verbose = bool(verbose)
```

> In that place, it is true that this could be approximately doubled on 64-bit machines (I guess that when this code was first written the person doing it did not know how to test that) but in practice using bounds > 21 will take a very very long time.
It's just that the implementation doesn't meet the documentation:

```
        - ``height_limit`` (float, default: 18) -- search up to this
          logarithmic height.

        .. note::
        
          On 32-bit machines, this *must* be < 21.48 else
          `\exp(h_{\text{lim}}) > 2^{31}` and overflows.  On 64-bit machines, it
          must be *at most* 43.668.  However, this bound is a logarithmic
          bound and increasing it by just 1 increases the running time
          by (roughly) `\exp(1.5)=4.5`, so searching up to even 20
          takes a very long time.
```

(We could add here that larger heights for 64-bit code currently aren't implemented in the Python interface.) 

```
        height_limit = float(height_limit)
        if height_limit >= 21.4:	# TODO: docstring says 21.48 (for 32-bit machines; what about 64-bit...?)
            raise ValueError, "The height limit must be < 21.4."
```

Also, if the docstring says `21.48`, the code should use the same value.

(Note that the code should check for what machine the code/`mwrank` was compiled for, not what machine Sage is currently running on...)

But that (change of the implementation, and perhaps other TODOs, like in `mwrank_EllipticCurve.__repr__()`) should be fixed on another ticket.



> [...] some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?
Definitely. :)

-Leif


---

Comment by leif created at 2010-05-12 23:15:21

Replying to [comment:19 cremona]:
> [...] some of the points raised on this ticket deserve a wider audience, possibly additional sentences in the developers guide?

I've opened a ticket for that at http://trac.sagemath.org/sage_trac/ticket/8958.


---

Comment by cremona created at 2010-05-15 17:25:23

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-05-15 17:25:23

I just checked that the patches apply fine to 4.4.2.rc0 (they do) and did a full make ptest.

This reveals a small problem in sage/libs/mwrank.pyx:  The reviewer patch removes two L suffixes from the output of E.discriminant() and E.conductor(), on long python ints.  I think this must be 32/64-bit dependent.  The best soution (surely) is to make those functions return Sage integers in the first place.  I will add that.

In the mean time I have put this back to "need work", realising that it has missged the boat for 4.4.2 anyway...


---

Comment by leif created at 2010-05-15 17:34:19

Replying to [comment:22 cremona]:
> In the mean time I have put this back to "need work", realising that it has missged the boat for 4.4.2 anyway...

mvngu wrote:
> From hereon, only critical fixes would be merged. *Fixes for documentation could also be merged.*

;-)


---

Comment by cremona created at 2010-05-15 19:35:48

Replying to [comment:23 leif]:
> Replying to [comment:22 cremona]:
> > In the mean time I have put this back to "need work", realising that it has missged the boat for 4.4.2 anyway...
> 
> mvngu wrote:
> > From hereon, only critical fixes would be merged. *Fixes for documentation could also be merged.*
> 
> ;-)

I know (and with that in mind I asked a couple of people of they would step in) but now I am suggesting a non-docstring change...


---

Attachment

Additional small fixes


---

Comment by cremona created at 2010-05-15 19:54:13

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-05-15 19:54:13

The final patch trac_8799-extra.patch fixes the issues raised by returning python ints (which display differently on 32 and 64 bit machines): the return types are Sage Integers, which is better anyway.


---

Comment by davidloeffler created at 2010-05-16 12:38:13

The code looks fine, the patch applies and builds fine, the reference manual builds with no warnings, and all doctests pass. Positive review.


---

Comment by davidloeffler created at 2010-05-16 12:38:13

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 08:41:56

Resolution: fixed
