# Issue 7262: Have multiplcation_by_m() return an EllipticCurveIsogeny object

archive/issues_007262.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @JohnCremona @williamstein @robertwb\n\nKeywords: elliptic curves, isogeny,\n\nCurrently sage returns a pair of rational functions when asked \n\n\n```\nE = EllipticCurve('11a1')\nE.multiplication_by_n(7)\n```\n\n\nI would be better if this creates a EllipticCurveIsogeny object from E to E.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7262\n\n",
    "created_at": "2009-10-21T09:26:49Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Have multiplcation_by_m() return an EllipticCurveIsogeny object",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7262",
    "user": "https://github.com/categorie"
}
```
Assignee: @loefflerd

CC:  @JohnCremona @williamstein @robertwb

Keywords: elliptic curves, isogeny,

Currently sage returns a pair of rational functions when asked 


```
E = EllipticCurve('11a1')
E.multiplication_by_n(7)
```


I would be better if this creates a EllipticCurveIsogeny object from E to E.

Issue created by migration from https://trac.sagemath.org/ticket/7262





---

archive/issue_comments_060197.json:
```json
{
    "body": "moving an email discussion forward, John said :\n\n> So, do we want to allow any (separable) isogeny to be created from the\n> full x-coordinate rational map (or from its numerator and\n> denominator)?  That soulds like a good idea _provided_ that (1) we can\n> do it, more cheaply that discarding the numerator and calling existing\n> code, and also perhaps (2) we have a way of checking the validity.\n\nI would send both coordinates to the constructor. Your code of constructing them is faster than what the generic isogeny-code will do. \n\n> As a first step, suppose we only allow this when the codomain is also\n> specified (as we can do in this case).  Then checking validity is\n> quite easy (you get the y-coordinate by differentiating and scaling\n> appropriately and then plug into the equation of the codomain -- I can\n> write this out properly if you do not follow me.)\n\nYes, that is what I will do. I do not think that we will need this option of specifying an isogeny when the codomain is not known. One could always send the denominator as a kernel_polynomial which will create the codomain.\n\nOf course there is an obvious extension that should be added here. Complex multiplication, like multiplication_by_n(2*i+3). Also we could make automorphisms into a group and create a endomorphism ring... oh but I am dreaming some steps ahead of what I will do about this ticket.\n\nChris.",
    "created_at": "2009-10-21T09:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60197",
    "user": "https://github.com/categorie"
}
```

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

archive/issue_comments_060198.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T10:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60198",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060199.json:
```json
{
    "body": "I've got a prototype patch ready that I'm going to post now, but I'd like some opinions before I finish it off. \n\nFirst, here's what I did: it'd be nice if we could make `multiplication_by_m` return an `EllipticCurveIsogeny` object without breaking any old code. This is no problem: I added a `__getitem__` and `__iter__` method to `EllipticCurveIsogeny` objects, so that statements like ` x, y = E.multiplication_by_m(7) ` still work just as before. However, it's not all sunshine and roses ...\n\nHere are some questions:\n\n* It's **significantly** slower to do it this way. This is because isogeny objects compute a whole bunch of other information about themselves, which has to happen to create one. (We could do a lot more work to make all those attributes lazy, which would possibly alleviate some of the issue.) This isn't just \"oh, it's a few percent slower\" -- here's an example with the old code:\n  {{{\nsage: E = EllipticCurve('11a1')\nsage: %time x,y = E.multiplication_by_m(17)\nCPU times: user 0.73 s, sys: 0.02 s, total: 0.75 s\nWall time: 0.87 s\n  }}}\n  I ran the new version of the code on the same example when I **started** this ticket, and it's still running. And no, I don't type at 4000 WPM. `:)` So that's definitely a huge speed penalty. A _very_ cursory glance suggests that at least part of this time is getting lost in some polynomial arithmetic; I'm happy to look into that if no one beats me to it. \n\n* The `x_only` argument also creates an issue. Before, the function would return either a rational function or a tuple of two of them, which is unfortunate -- in general, the rule of thumb is that we prefer for functions to have a single return type, no matter what flags are passed. So we could still do the same thing, but it somehow feels even more egregious to have the function return either a rational function or an isogeny object.\n\nI'm not sure what the best plan is -- I'm guessing people aren't willing to accept that speed hit in general. We could also have a separate function, maybe `multiplication_by_m_isogeny` or somesuch?\n\nI'm attaching a patch anyway, in case people want to play around with it. Don't be frightened by the size of the patch file -- I got a little carried away using `\\C-t` in emacs, and reformatted all the documentation to be at most 80 characters wide. I also changed some statements of the form `x == None` to `x is None,` mostly out of habit. (It's faster, and arguably more sensible -- after all, `None` is a unique object.) So even if we decide on a completely different plan for this ticket, I'd still like to extract the doc cleanup changes and submit those.\n\nSince I'm mostly looking for comments, I'm adding one or two people on the cc list ...",
    "created_at": "2010-01-20T10:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60199",
    "user": "https://github.com/craigcitro"
}
```

I've got a prototype patch ready that I'm going to post now, but I'd like some opinions before I finish it off. 

First, here's what I did: it'd be nice if we could make `multiplication_by_m` return an `EllipticCurveIsogeny` object without breaking any old code. This is no problem: I added a `__getitem__` and `__iter__` method to `EllipticCurveIsogeny` objects, so that statements like ` x, y = E.multiplication_by_m(7) ` still work just as before. However, it's not all sunshine and roses ...

Here are some questions:

* It's **significantly** slower to do it this way. This is because isogeny objects compute a whole bunch of other information about themselves, which has to happen to create one. (We could do a lot more work to make all those attributes lazy, which would possibly alleviate some of the issue.) This isn't just "oh, it's a few percent slower" -- here's an example with the old code:
  {{{
sage: E = EllipticCurve('11a1')
sage: %time x,y = E.multiplication_by_m(17)
CPU times: user 0.73 s, sys: 0.02 s, total: 0.75 s
Wall time: 0.87 s
  }}}
  I ran the new version of the code on the same example when I **started** this ticket, and it's still running. And no, I don't type at 4000 WPM. `:)` So that's definitely a huge speed penalty. A _very_ cursory glance suggests that at least part of this time is getting lost in some polynomial arithmetic; I'm happy to look into that if no one beats me to it. 

* The `x_only` argument also creates an issue. Before, the function would return either a rational function or a tuple of two of them, which is unfortunate -- in general, the rule of thumb is that we prefer for functions to have a single return type, no matter what flags are passed. So we could still do the same thing, but it somehow feels even more egregious to have the function return either a rational function or an isogeny object.

I'm not sure what the best plan is -- I'm guessing people aren't willing to accept that speed hit in general. We could also have a separate function, maybe `multiplication_by_m_isogeny` or somesuch?

I'm attaching a patch anyway, in case people want to play around with it. Don't be frightened by the size of the patch file -- I got a little carried away using `\C-t` in emacs, and reformatted all the documentation to be at most 80 characters wide. I also changed some statements of the form `x == None` to `x is None,` mostly out of habit. (It's faster, and arguably more sensible -- after all, `None` is a unique object.) So even if we decide on a completely different plan for this ticket, I'd still like to extract the doc cleanup changes and submit those.

Since I'm mostly looking for comments, I'm adding one or two people on the cc list ...



---

archive/issue_comments_060200.json:
```json
{
    "body": "(Shame that I am sitting in my office, marking exams, when all this action happens on bugs.)\n\nI fear that speed is an issue, so I am in favour of having both options, `multiplication_by_m_isogeny` sounds like a good idea.\n\nIn a more long-term vision, you might want to look at #7368. For instance, I am not sure yet, how one should design isogenies in general. Probably they should internally remember their factorisation if they came with one. Like a seperable \\circ non-seperable isogeny. Even for the isogeny [m], it might be much faster if we treat it as \\phi \\circ \\hat\\phi when there is a factorisation like that. etc etc.\n\nBut any progress on this is very welcome and the big philiosophical questions can be looked at later.\n\nProbably you are aware of the related ticket #6413.",
    "created_at": "2010-01-20T10:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60200",
    "user": "https://github.com/categorie"
}
```

(Shame that I am sitting in my office, marking exams, when all this action happens on bugs.)

I fear that speed is an issue, so I am in favour of having both options, `multiplication_by_m_isogeny` sounds like a good idea.

In a more long-term vision, you might want to look at #7368. For instance, I am not sure yet, how one should design isogenies in general. Probably they should internally remember their factorisation if they came with one. Like a seperable \circ non-seperable isogeny. Even for the isogeny [m], it might be much faster if we treat it as \phi \circ \hat\phi when there is a factorisation like that. etc etc.

But any progress on this is very welcome and the big philiosophical questions can be looked at later.

Probably you are aware of the related ticket #6413.



---

archive/issue_comments_060201.json:
```json
{
    "body": "Quick comment: let's allow the old version to remain, with a different name.  And let's keep the x-only version (again with a different name if it must) since that is used a lot, e.g. for dividing points by  m.\n\nMust run -- not marking exams but defining the group law on elliptic curves in 10 mins!",
    "created_at": "2010-01-20T11:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60201",
    "user": "https://github.com/JohnCremona"
}
```

Quick comment: let's allow the old version to remain, with a different name.  And let's keep the x-only version (again with a different name if it must) since that is used a lot, e.g. for dividing points by  m.

Must run -- not marking exams but defining the group law on elliptic curves in 10 mins!



---

archive/issue_comments_060202.json:
```json
{
    "body": "Ok, new ticket created for making isogenies faster to create at #8014. Also, I'm posting a new patch (within the next two minutes, just double-checking there's no cruft in it) that breaks this out into a `multiplication_by_m_isogeny` method, which should at least be a start on the request from this ticket. Is everyone happy with reviewing this one and pushing further work to #8014?",
    "created_at": "2010-01-20T19:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60202",
    "user": "https://github.com/craigcitro"
}
```

Ok, new ticket created for making isogenies faster to create at #8014. Also, I'm posting a new patch (within the next two minutes, just double-checking there's no cruft in it) that breaks this out into a `multiplication_by_m_isogeny` method, which should at least be a start on the request from this ticket. Is everyone happy with reviewing this one and pushing further work to #8014?



---

archive/issue_comments_060203.json:
```json
{
    "body": "Apparently I never posted the other patch? Weird. \n\nAnyway, as I mentioned above: the patch is big, but it's basically me hitting `\\C-t` in emacs a whole bunch to fix widths in the documentation. (It was actually fairly unreadable from the command line.) All the \"action\" is in `ell_generic.py`, where I'm just adding one new method.",
    "created_at": "2010-01-20T19:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60203",
    "user": "https://github.com/craigcitro"
}
```

Apparently I never posted the other patch? Weird. 

Anyway, as I mentioned above: the patch is big, but it's basically me hitting `\C-t` in emacs a whole bunch to fix widths in the documentation. (It was actually fairly unreadable from the command line.) All the "action" is in `ell_generic.py`, where I'm just adding one new method.



---

archive/issue_comments_060204.json:
```json
{
    "body": "I have read through the patch, but not started testing yet.  I think this is a summary of what it contains:\n\n1. A lot of cosmetic changes to the docstrings\n2. Several minor changes such as \"is None\" for \"None == \"\n3. The new ability to construct an isogeny with the maps in hand, not just the kernel poly.\n4. A new function in ell_generic which creates a multiplcation-by-m map as an isogeny (in the separable case) by using the existing code to get the maps and then calling the new constructor.\n\nHave I missed anything?  I do think that this is a good start, and will go on to test.",
    "created_at": "2010-01-20T20:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60204",
    "user": "https://github.com/JohnCremona"
}
```

I have read through the patch, but not started testing yet.  I think this is a summary of what it contains:

1. A lot of cosmetic changes to the docstrings
2. Several minor changes such as "is None" for "None == "
3. The new ability to construct an isogeny with the maps in hand, not just the kernel poly.
4. A new function in ell_generic which creates a multiplcation-by-m map as an isogeny (in the separable case) by using the existing code to get the maps and then calling the new constructor.

Have I missed anything?  I do think that this is a good start, and will go on to test.



---

archive/issue_comments_060205.json:
```json
{
    "body": "Yep, that's exactly what's in the patch.",
    "created_at": "2010-01-20T20:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60205",
    "user": "https://github.com/craigcitro"
}
```

Yep, that's exactly what's in the patch.



---

archive/issue_comments_060206.json:
```json
{
    "body": "Am I doing something stupid here?  The patch applies fine but when I run the test I get\nthis from ell_generic.py:\n\n```\n    sage: E.multiplication_by_m_isogeny(7)\n    AttributeError: 'EllipticCurve_rational_field' object has no attribute 'multiplication_by_m_isogeny'\n```\n\nwhich makes no sense since E has type `EllipticCurve_rational_field` which derived from `EllipticCurve_generic`, which is where multiplication_by_m_isogeny() is defined.",
    "created_at": "2010-01-20T20:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60206",
    "user": "https://github.com/JohnCremona"
}
```

Am I doing something stupid here?  The patch applies fine but when I run the test I get
this from ell_generic.py:

```
    sage: E.multiplication_by_m_isogeny(7)
    AttributeError: 'EllipticCurve_rational_field' object has no attribute 'multiplication_by_m_isogeny'
```

which makes no sense since E has type `EllipticCurve_rational_field` which derived from `EllipticCurve_generic`, which is where multiplication_by_m_isogeny() is defined.



---

archive/issue_comments_060207.json:
```json
{
    "body": "Replying to [comment:10 cremona]:\n> Am I doing something stupid here?  \n\nApologies, I patched a clone but ran the main branch.  Stupid!\n\nTests do pass.  Positive review soon, I expect!",
    "created_at": "2010-01-20T20:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60207",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:10 cremona]:
> Am I doing something stupid here?  

Apologies, I patched a clone but ran the main branch.  Stupid!

Tests do pass.  Positive review soon, I expect!



---

archive/issue_comments_060208.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T20:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60208",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060209.json:
```json
{
    "body": "Looks good to me.  I wanted to do more tests (over number fields and finite fields) but have to go.",
    "created_at": "2010-01-20T20:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60209",
    "user": "https://github.com/JohnCremona"
}
```

Looks good to me.  I wanted to do more tests (over number fields and finite fields) but have to go.



---

archive/issue_comments_060210.json:
```json
{
    "body": "Oops.  \n\n```\nsage: E = EllipticCurve('11a1')\nsage: E.multiplication_by_m_isogeny(4)\n```\n\nBoom.",
    "created_at": "2010-01-20T21:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60210",
    "user": "https://github.com/JohnCremona"
}
```

Oops.  

```
sage: E = EllipticCurve('11a1')
sage: E.multiplication_by_m_isogeny(4)
```

Boom.



---

archive/issue_comments_060211.json:
```json
{
    "body": "Well, the error that pops up in that case is just an exception being raised by the `EllipticCurveIsogeny` code, saying that it can't create an isogeny in this case. What would you rather see? (Other than an implementation of isogenies in that case. `:)` )",
    "created_at": "2010-01-20T21:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60211",
    "user": "https://github.com/craigcitro"
}
```

Well, the error that pops up in that case is just an exception being raised by the `EllipticCurveIsogeny` code, saying that it can't create an isogeny in this case. What would you rather see? (Other than an implementation of isogenies in that case. `:)` )



---

archive/issue_comments_060212.json:
```json
{
    "body": "I also add that the following problem with the documentation should be adjusted, too...\n\n\n```\n/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_generic.py:docstring of sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic.multiplication_by_m_isogeny:19: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n```\n\n\nBy the way, is it considered \"good coding\" to cut lines at 80 characters ? I never thought about this and I am happy to follow that rule, if others desire that.",
    "created_at": "2010-01-20T21:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60212",
    "user": "https://github.com/categorie"
}
```

I also add that the following problem with the documentation should be adjusted, too...


```
/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_generic.py:docstring of sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic.multiplication_by_m_isogeny:19: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
```


By the way, is it considered "good coding" to cut lines at 80 characters ? I never thought about this and I am happy to follow that rule, if others desire that.



---

archive/issue_comments_060213.json:
```json
{
    "body": "I posted a new patch fixing the newline in docstring issue. (I was bad and didn't even try building the docs.)\n\nAs to 80 character line widths: while lots of people use wider terminals nowadays, 80 has always been the standard width from days of yore. For the neanderthals like me who still prefer the command-line over the terminal, and in particular keep to 80 characters, it's a big mess when things are wider. So in short, yes, at least some people prefer 80 character line widths -- but no one's going to start rejecting patches if you forget. \n\nChris, what're your thoughts on the exception John ran into? What would you like to see happen?",
    "created_at": "2010-01-20T21:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60213",
    "user": "https://github.com/craigcitro"
}
```

I posted a new patch fixing the newline in docstring issue. (I was bad and didn't even try building the docs.)

As to 80 character line widths: while lots of people use wider terminals nowadays, 80 has always been the standard width from days of yore. For the neanderthals like me who still prefer the command-line over the terminal, and in particular keep to 80 characters, it's a big mess when things are wider. So in short, yes, at least some people prefer 80 character line widths -- but no one's going to start rejecting patches if you forget. 

Chris, what're your thoughts on the exception John ran into? What would you like to see happen?



---

archive/issue_comments_060214.json:
```json
{
    "body": "Looking at the code, I see that this is not doing exactly what my original idea was when I opened this trac. The reason this is so slow is that a lot of computations will be done several times. I thought that one should create the isogeny without running through the current init of the object. I think all data is known easily once the division polynomial is computed.\n\nOf course, we can leave it like that by now, but I would suggest to open a further ticket to improve this.\n\nAnother ugly thing is\n\n```\nsage: phi.codomain() == phi.domain()\nFalse\n```\n\n\nOne should set the post_isomorphism correctly.\n\nAs to the 4-isogeny, this is indeed not implemented since it is a bit more complicated. The best would be to have the composition of morphisms defined and then to defined by iterating [2]. We can leave it like that by now. It is a shame though.",
    "created_at": "2010-01-20T21:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60214",
    "user": "https://github.com/categorie"
}
```

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

archive/issue_comments_060215.json:
```json
{
    "body": "For now why don't we limit this function to prime m?\n\nI agree with setting domain=codomain.  I did that a lot with the l-isogeny code when I knew I had an endomorphism.  One day we'll have endomorphisms as a proper class.\n\nSorry I did not check docbuilding as I was called away...",
    "created_at": "2010-01-20T21:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60215",
    "user": "https://github.com/JohnCremona"
}
```

For now why don't we limit this function to prime m?

I agree with setting domain=codomain.  I did that a lot with the l-isogeny code when I knew I had an endomorphism.  One day we'll have endomorphisms as a proper class.

Sorry I did not check docbuilding as I was called away...



---

archive/issue_comments_060216.json:
```json
{
    "body": "We have to limit (actually the current code does that already) that the only even m which works is m=2. But m=9 is fine.",
    "created_at": "2010-01-20T22:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60216",
    "user": "https://github.com/categorie"
}
```

We have to limit (actually the current code does that already) that the only even m which works is m=2. But m=9 is fine.



---

archive/issue_comments_060217.json:
```json
{
    "body": "Okay, good point about the codomain -- I'm going to attach a new patch with that fix. I should mention that I've never actually used the isogeny **or** multiplication by m code myself -- I volunteered for this while we were triaging during the bug days. So if you don't think the patch is helpful, feel free to say so ... I won't take it personally. `:)`\n\nI agree that something more sophisticated is definitely called for. I happened to email Dan Shumow about this, and he had much the same opinion as you and John: it would be nice to have an endomorphism class that inherits from isogeny, and then possibly even a multiplication-by-m class that inherits from that, each avoiding more and more computation. I was thinking that the first step would be to make things get calculated lazily in `EllipticCurveIsogeny`, and then people could pick and choose as they needed things or knew enough to set them up themselves. (This is what I was thinking in #8014.) Maybe it's a better idea to just make new classes from the get-go? In any event, you're right, more work is needed ...",
    "created_at": "2010-01-20T22:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60217",
    "user": "https://github.com/craigcitro"
}
```

Okay, good point about the codomain -- I'm going to attach a new patch with that fix. I should mention that I've never actually used the isogeny **or** multiplication by m code myself -- I volunteered for this while we were triaging during the bug days. So if you don't think the patch is helpful, feel free to say so ... I won't take it personally. `:)`

I agree that something more sophisticated is definitely called for. I happened to email Dan Shumow about this, and he had much the same opinion as you and John: it would be nice to have an endomorphism class that inherits from isogeny, and then possibly even a multiplication-by-m class that inherits from that, each avoiding more and more computation. I was thinking that the first step would be to make things get calculated lazily in `EllipticCurveIsogeny`, and then people could pick and choose as they needed things or knew enough to set them up themselves. (This is what I was thinking in #8014.) Maybe it's a better idea to just make new classes from the get-go? In any event, you're right, more work is needed ...



---

archive/issue_comments_060218.json:
```json
{
    "body": "Attachment [trac_7262.patch](tarball://root/attachments/some-uuid/ticket7262/trac_7262.patch) by @craigcitro created at 2010-01-20 22:57:37",
    "created_at": "2010-01-20T22:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60218",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_7262.patch](tarball://root/attachments/some-uuid/ticket7262/trac_7262.patch) by @craigcitro created at 2010-01-20 22:57:37



---

archive/issue_comments_060219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T21:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7262#issuecomment-60219",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
