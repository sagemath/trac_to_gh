# Issue 7262: Have multiplcation_by_m() return an EllipticCurveIsogeny object

Issue created by migration from https://trac.sagemath.org/ticket/7262

Original creator: wuthrich

Original creation time: 2009-10-21 09:26:49

Assignee: davidloeffler

CC:  cremona was robertwb

Keywords: elliptic curves, isogeny,

Currently sage returns a pair of rational functions when asked 


```
E = EllipticCurve('11a1')
E.multiplication_by_n(7)
```


I would be better if this creates a EllipticCurveIsogeny object from E to E.


---

Comment by wuthrich created at 2009-10-21 09:33:58

moving an email discussion forward, John said :

> So, do we want to allow any (separable) isogeny to be created from the
> full x-coordinate rational map (or from its numerator and
> denominator)?  That soulds like a good idea _provided_ that (1) we can
> do it, more cheaply that discarding the numerator and calling existing
> code, and also perhaps (2) we have a way of checking the validity.

I would send both coordinates to the constructor. Your code of constructing them is faster than what the generic isogeny-code will do. 

> As a first step, suppose we only allow this when the codomain is also
> specified (as we can do in this case).  Then checking validity is
> quite easy (you get the y-coordinate by differentiating and scaling
> appropriately and then plug into the equation of the codomain -- I can
> write this out properly if you do not follow me.)

Yes, that is what I will do. I do not think that we will need this option of specifying an isogeny when the codomain is not known. One could always send the denominator as a kernel_polynomial which will create the codomain.

Of course there is an obvious extension that should be added here. Complex multiplication, like multiplication_by_n(2*i+3). Also we could make automorphisms into a group and create a endomorphism ring... oh but I am dreaming some steps ahead of what I will do about this ticket.

Chris.


---

Comment by craigcitro created at 2010-01-20 10:40:14

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-01-20 10:40:14

I've got a prototype patch ready that I'm going to post now, but I'd like some opinions before I finish it off. 

First, here's what I did: it'd be nice if we could make `multiplication_by_m` return an `EllipticCurveIsogeny` object without breaking any old code. This is no problem: I added a `__getitem__` and `__iter__` method to `EllipticCurveIsogeny` objects, so that statements like ` x, y = E.multiplication_by_m(7) ` still work just as before. However, it's not all sunshine and roses ...

Here are some questions:

 * It's *significantly* slower to do it this way. This is because isogeny objects compute a whole bunch of other information about themselves, which has to happen to create one. (We could do a lot more work to make all those attributes lazy, which would possibly alleviate some of the issue.) This isn't just "oh, it's a few percent slower" -- here's an example with the old code:
  {{{
sage: E = EllipticCurve('11a1')
sage: %time x,y = E.multiplication_by_m(17)
CPU times: user 0.73 s, sys: 0.02 s, total: 0.75 s
Wall time: 0.87 s
  }}}
  I ran the new version of the code on the same example when I *started* this ticket, and it's still running. And no, I don't type at 4000 WPM. `:)` So that's definitely a huge speed penalty. A _very_ cursory glance suggests that at least part of this time is getting lost in some polynomial arithmetic; I'm happy to look into that if no one beats me to it. 

 * The `x_only` argument also creates an issue. Before, the function would return either a rational function or a tuple of two of them, which is unfortunate -- in general, the rule of thumb is that we prefer for functions to have a single return type, no matter what flags are passed. So we could still do the same thing, but it somehow feels even more egregious to have the function return either a rational function or an isogeny object.

I'm not sure what the best plan is -- I'm guessing people aren't willing to accept that speed hit in general. We could also have a separate function, maybe `multiplication_by_m_isogeny` or somesuch?

I'm attaching a patch anyway, in case people want to play around with it. Don't be frightened by the size of the patch file -- I got a little carried away using `\C-t` in emacs, and reformatted all the documentation to be at most 80 characters wide. I also changed some statements of the form `x == None` to `x is None,` mostly out of habit. (It's faster, and arguably more sensible -- after all, `None` is a unique object.) So even if we decide on a completely different plan for this ticket, I'd still like to extract the doc cleanup changes and submit those.

Since I'm mostly looking for comments, I'm adding one or two people on the cc list ...


---

Comment by wuthrich created at 2010-01-20 10:52:53

(Shame that I am sitting in my office, marking exams, when all this action happens on bugs.)

I fear that speed is an issue, so I am in favour of having both options, `multiplication_by_m_isogeny` sounds like a good idea.

In a more long-term vision, you might want to look at #7368. For instance, I am not sure yet, how one should design isogenies in general. Probably they should internally remember their factorisation if they came with one. Like a seperable \circ non-seperable isogeny. Even for the isogeny [m], it might be much faster if we treat it as \phi \circ \hat\phi when there is a factorisation like that. etc etc.

But any progress on this is very welcome and the big philiosophical questions can be looked at later.

Probably you are aware of the related ticket #6413.


---

Comment by cremona created at 2010-01-20 11:51:21

Quick comment: let's allow the old version to remain, with a different name.  And let's keep the x-only version (again with a different name if it must) since that is used a lot, e.g. for dividing points by  m.

Must run -- not marking exams but defining the group law on elliptic curves in 10 mins!


---

Comment by craigcitro created at 2010-01-20 19:23:00

Ok, new ticket created for making isogenies faster to create at #8014. Also, I'm posting a new patch (within the next two minutes, just double-checking there's no cruft in it) that breaks this out into a `multiplication_by_m_isogeny` method, which should at least be a start on the request from this ticket. Is everyone happy with reviewing this one and pushing further work to #8014?


---

Comment by craigcitro created at 2010-01-20 19:26:46

Apparently I never posted the other patch? Weird. 

Anyway, as I mentioned above: the patch is big, but it's basically me hitting `\C-t` in emacs a whole bunch to fix widths in the documentation. (It was actually fairly unreadable from the command line.) All the "action" is in `ell_generic.py`, where I'm just adding one new method.


---

Comment by cremona created at 2010-01-20 20:25:47

I have read through the patch, but not started testing yet.  I think this is a summary of what it contains:

    1. A lot of cosmetic changes to the docstrings
    2. Several minor changes such as "is None" for "None == "
    3. The new ability to construct an isogeny with the maps in hand, not just the kernel poly.
    4. A new function in ell_generic which creates a multiplcation-by-m map as an isogeny (in the separable case) by using the existing code to get the maps and then calling the new constructor.

Have I missed anything?  I do think that this is a good start, and will go on to test.


---

Comment by craigcitro created at 2010-01-20 20:27:02

Yep, that's exactly what's in the patch.


---

Comment by cremona created at 2010-01-20 20:48:55

Am I doing something stupid here?  The patch applies fine but when I run the test I get
this from ell_generic.py:

```
    sage: E.multiplication_by_m_isogeny(7)
    AttributeError: 'EllipticCurve_rational_field' object has no attribute 'multiplication_by_m_isogeny'
```

which makes no sense since E has type `EllipticCurve_rational_field` which derived from `EllipticCurve_generic`, which is where multiplication_by_m_isogeny() is defined.


---

Comment by cremona created at 2010-01-20 20:52:51

Replying to [comment:10 cremona]:
> Am I doing something stupid here?  

Apologies, I patched a clone but ran the main branch.  Stupid!

Tests do pass.  Positive review soon, I expect!


---

Comment by cremona created at 2010-01-20 20:58:48

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-20 20:58:48

Looks good to me.  I wanted to do more tests (over number fields and finite fields) but have to go.


---

Comment by cremona created at 2010-01-20 21:01:08

Oops.  

```
sage: E = EllipticCurve('11a1')
sage: E.multiplication_by_m_isogeny(4)
```

Boom.


---

Comment by craigcitro created at 2010-01-20 21:33:55

Well, the error that pops up in that case is just an exception being raised by the `EllipticCurveIsogeny` code, saying that it can't create an isogeny in this case. What would you rather see? (Other than an implementation of isogenies in that case. `:)` )


---

Comment by wuthrich created at 2010-01-20 21:37:44

I also add that the following problem with the documentation should be adjusted, too...


```
/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_generic.py:docstring of sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic.multiplication_by_m_isogeny:19: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
```


By the way, is it considered "good coding" to cut lines at 80 characters ? I never thought about this and I am happy to follow that rule, if others desire that.


---

Comment by craigcitro created at 2010-01-20 21:44:48

I posted a new patch fixing the newline in docstring issue. (I was bad and didn't even try building the docs.)

As to 80 character line widths: while lots of people use wider terminals nowadays, 80 has always been the standard width from days of yore. For the neanderthals like me who still prefer the command-line over the terminal, and in particular keep to 80 characters, it's a big mess when things are wider. So in short, yes, at least some people prefer 80 character line widths -- but no one's going to start rejecting patches if you forget. 

Chris, what're your thoughts on the exception John ran into? What would you like to see happen?


---

Comment by wuthrich created at 2010-01-20 21:51:54

Looking at the code, I see that this is not doing exactly what my original idea was when I opened this trac. The reason this is so slow is that a lot of computations will be done several times. I thought that one should create the isogeny without running through the current init of the object. I think all data is known easily once the division polynomial is computed.

Of course, we can leave it like that by now, but I would suggest to open a further ticket to improve this.

Another ugly thing is

```
sage: phi.codomain() == phi.domain()
False
```


One should set the post_isomorphism correctly.

As to the 4-isogeny, this is indeed not implemented since it is a bit more complicated. The best would be to have the composition of morphisms defined and then to defined by iterating [2]. We can leave it like that by now. It is a shame though.


---

Comment by cremona created at 2010-01-20 21:55:26

For now why don't we limit this function to prime m?

I agree with setting domain=codomain.  I did that a lot with the l-isogeny code when I knew I had an endomorphism.  One day we'll have endomorphisms as a proper class.

Sorry I did not check docbuilding as I was called away...


---

Comment by wuthrich created at 2010-01-20 22:11:00

We have to limit (actually the current code does that already) that the only even m which works is m=2. But m=9 is fine.


---

Comment by craigcitro created at 2010-01-20 22:28:15

Okay, good point about the codomain -- I'm going to attach a new patch with that fix. I should mention that I've never actually used the isogeny *or* multiplication by m code myself -- I volunteered for this while we were triaging during the bug days. So if you don't think the patch is helpful, feel free to say so ... I won't take it personally. `:)`

I agree that something more sophisticated is definitely called for. I happened to email Dan Shumow about this, and he had much the same opinion as you and John: it would be nice to have an endomorphism class that inherits from isogeny, and then possibly even a multiplication-by-m class that inherits from that, each avoiding more and more computation. I was thinking that the first step would be to make things get calculated lazily in `EllipticCurveIsogeny`, and then people could pick and choose as they needed things or knew enough to set them up themselves. (This is what I was thinking in #8014.) Maybe it's a better idea to just make new classes from the get-go? In any event, you're right, more work is needed ...


---

Attachment


---

Comment by mvngu created at 2010-01-23 21:27:45

Resolution: fixed
