# Issue 7742: add a compose function to sage

archive/issues_007742.json:
```json
{
    "body": "Assignee: @aghitza\n\n\n```\n\ndef compose(f, n, a):\n    \"\"\"\n    Return f(f(...f(a)...)), where the composition occurs n times.\n    \n    INPUT:\n        - `f` -- anything that is callable\n        - `n` -- a nonnegative integer\n        - `a` -- any input for `f`\n\n    OUTPUT:\n        result of composing `f` with itself `n` times and applying to `a`.\n\n    EXAMPLES::\n\n        sage: def f(x): return x^2 + 1\n        sage: x = var('x')\n        sage: compose(f, 3, x)\n        ((x^2 + 1)^2 + 1)^2 + 1\n    \"\"\"\n    n = Integer(n)\n    if n <= 0: return a\n    a = f(a)\n    for i in range(n-1): a = f(a)\n    return a\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7742\n\n",
    "created_at": "2009-12-19T20:15:55Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "add a compose function to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7742",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza


```

def compose(f, n, a):
    """
    Return f(f(...f(a)...)), where the composition occurs n times.
    
    INPUT:
        - `f` -- anything that is callable
        - `n` -- a nonnegative integer
        - `a` -- any input for `f`

    OUTPUT:
        result of composing `f` with itself `n` times and applying to `a`.

    EXAMPLES::

        sage: def f(x): return x^2 + 1
        sage: x = var('x')
        sage: compose(f, 3, x)
        ((x^2 + 1)^2 + 1)^2 + 1
    """
    n = Integer(n)
    if n <= 0: return a
    a = f(a)
    for i in range(n-1): a = f(a)
    return a

```


Issue created by migration from https://trac.sagemath.org/ticket/7742





---

archive/issue_comments_066426.json:
```json
{
    "body": "Replying to [ticket:7742 was]:\n>     n = Integer(n)\n\nConverting to int should be sufficient... Or the implementation below should'nt be very useful :-).\n\n>     if n <= 0: return a\n\nI'd rather sage to raise a `ValueError` if `n < 0` than returning silently a wrong value...\n\nFlorent",
    "created_at": "2009-12-19T22:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66426",
    "user": "https://github.com/hivert"
}
```

Replying to [ticket:7742 was]:
>     n = Integer(n)

Converting to int should be sufficient... Or the implementation below should'nt be very useful :-).

>     if n <= 0: return a

I'd rather sage to raise a `ValueError` if `n < 0` than returning silently a wrong value...

Florent



---

archive/issue_comments_066427.json:
```json
{
    "body": "Replying to [comment:1 hivert]:\n> Replying to [ticket:7742 was]:\n> >     n = Integer(n)\n> \n> Converting to int should be sufficient... Or the implementation below should'nt be very useful :-).\n> \n> >     if n <= 0: return a\n> \n> I'd rather sage to raise a `ValueError` if `n < 0` than returning silently a wrong value...\n> \n> Florent\n\nWe probably want to return an inverse function, if possible, when n<0... I'm also wondering if there is a generalisation of this to all real numbers.",
    "created_at": "2009-12-20T16:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66427",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

Replying to [comment:1 hivert]:
> Replying to [ticket:7742 was]:
> >     n = Integer(n)
> 
> Converting to int should be sufficient... Or the implementation below should'nt be very useful :-).
> 
> >     if n <= 0: return a
> 
> I'd rather sage to raise a `ValueError` if `n < 0` than returning silently a wrong value...
> 
> Florent

We probably want to return an inverse function, if possible, when n<0... I'm also wondering if there is a generalisation of this to all real numbers.



---

archive/issue_comments_066428.json:
```json
{
    "body": "\n```\nHi,\n\nThere is a function in Mathematica that does exactly what you want and it's called Nest. I've reimplemented it in python as general effort to port some functional tools that I like to python. Please check this link if you are interested on it:\n\nhttp://bitbucket.org/juliusc/functional/src/tip/functional/functional_mathematica.py\n\nHope this helps,\nCarlos\n```\n",
    "created_at": "2009-12-20T21:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66428",
    "user": "https://github.com/williamstein"
}
```


```
Hi,

There is a function in Mathematica that does exactly what you want and it's called Nest. I've reimplemented it in python as general effort to port some functional tools that I like to python. Please check this link if you are interested on it:

http://bitbucket.org/juliusc/functional/src/tip/functional/functional_mathematica.py

Hope this helps,
Carlos
```




---

archive/issue_comments_066429.json:
```json
{
    "body": "Hi,\n\nThere is a function in Mathematica that does exactly what you want and it's called Nest. I've reimplemented it in python as general effort to port some functional tools that I like to python. Please check this link if you are interested on it:\n\nhttp://bitbucket.org/juliusc/functional/src/tip/functional/functional_mathematica.py\n\nHope this helps,\nCarlos",
    "created_at": "2009-12-20T21:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66429",
    "user": "https://github.com/williamstein"
}
```

Hi,

There is a function in Mathematica that does exactly what you want and it's called Nest. I've reimplemented it in python as general effort to port some functional tools that I like to python. Please check this link if you are interested on it:

http://bitbucket.org/juliusc/functional/src/tip/functional/functional_mathematica.py

Hope this helps,
Carlos



---

archive/issue_comments_066430.json:
```json
{
    "body": "> We probably want to return an inverse function, if possible, when n<0..\n\nNote that usually the inverse isn't available.",
    "created_at": "2009-12-20T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66430",
    "user": "https://github.com/williamstein"
}
```

> We probably want to return an inverse function, if possible, when n<0..

Note that usually the inverse isn't available.



---

archive/issue_comments_066431.json:
```json
{
    "body": "What about doing it in log(n) compositions, like when you try to compute x^12 ? :-)\n\nNathann",
    "created_at": "2009-12-21T07:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66431",
    "user": "https://github.com/nathanncohen"
}
```

What about doing it in log(n) compositions, like when you try to compute x^12 ? :-)

Nathann



---

archive/issue_comments_066432.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> What about doing it in log(n) compositions, like when you try to compute x^12 ? :-)\n\nThat's an interesting idea.  For a Python function that will make absolutely no difference.  For a symbolic callable expression it would make a noticeable difference though.   So we should definitely think about it. \n\nI think the most important thing though is to implement something with a clear interface and definition now and get it into sage. Then we can make it faster whenever we want.",
    "created_at": "2009-12-21T08:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66432",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:6 ncohen]:
> What about doing it in log(n) compositions, like when you try to compute x^12 ? :-)

That's an interesting idea.  For a Python function that will make absolutely no difference.  For a symbolic callable expression it would make a noticeable difference though.   So we should definitely think about it. 

I think the most important thing though is to implement something with a clear interface and definition now and get it into sage. Then we can make it faster whenever we want.



---

archive/issue_comments_066433.json:
```json
{
    "body": "I completely agree ! That's what we are doing in graph theory : first implement, then try to think about how to optimize it :-)\n\nI this case it should not be too different from these few lines ( if I make none of my usual mistakes )\n\n\n```\nif n==0:\n    return \"identity function\"( no idea how it is called in Sage )\n\nif n%2 == 1:\n    ff = compose(f, (n-1)/2, a)\n    return f(ff(ff(a)))\nelse:\n    ff = compose(f, n/2, a)\n    return ff(ff(a))\n```\n\n\nBut perhaps the function \"compose\" should be a method of these symbolic callable expressions you mentionned, which would be called by this \"compose\" function : it may be interesting to compute symbolically the n^th composed of a function without evaluating it  :-)",
    "created_at": "2009-12-21T08:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66433",
    "user": "https://github.com/nathanncohen"
}
```

I completely agree ! That's what we are doing in graph theory : first implement, then try to think about how to optimize it :-)

I this case it should not be too different from these few lines ( if I make none of my usual mistakes )


```
if n==0:
    return "identity function"( no idea how it is called in Sage )

if n%2 == 1:
    ff = compose(f, (n-1)/2, a)
    return f(ff(ff(a)))
else:
    ff = compose(f, n/2, a)
    return ff(ff(a))
```


But perhaps the function "compose" should be a method of these symbolic callable expressions you mentionned, which would be called by this "compose" function : it may be interesting to compute symbolically the n^th composed of a function without evaluating it  :-)



---

archive/issue_comments_066434.json:
```json
{
    "body": "Attachment [compose.patch](tarball://root/attachments/some-uuid/ticket7742/compose.patch) by colah created at 2010-03-14 04:00:29\n\nAdds the compose function.",
    "created_at": "2010-03-14T04:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66434",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

Attachment [compose.patch](tarball://root/attachments/some-uuid/ticket7742/compose.patch) by colah created at 2010-03-14 04:00:29

Adds the compose function.



---

archive/issue_comments_066435.json:
```json
{
    "body": "I ran into some problems producing the patch. On mhansen's suggestion, I added     \n{{from sage.rings.integer import Integer}}\nat the beginning of the function instead of the beginning of misc.py and it worked... But I don't know why and am concerned that it adds unnecessary overhead...",
    "created_at": "2010-03-14T04:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66435",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

I ran into some problems producing the patch. On mhansen's suggestion, I added     
{{from sage.rings.integer import Integer}}
at the beginning of the function instead of the beginning of misc.py and it worked... But I don't know why and am concerned that it adds unnecessary overhead...



---

archive/issue_comments_066436.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-14T04:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66436",
    "user": "https://trac.sagemath.org/admin/accounts/users/colah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066437.json:
```json
{
    "body": "I have two comments: (1) the patch contains twice the new function, and (2) it would be nice to\nbe able to write `compose(f,x,n)` for a symbolic variable n (or any expression). Only when\nn is an integer would the \"nesting\" be evaluated. Comment (1) needs more work, comment (2) could\nbe a separate ticket, but if easy it would be nice to do it.\n\nAdditional comment: please rename the patch as trac_7742.patch.",
    "created_at": "2010-03-14T18:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66437",
    "user": "https://github.com/zimmermann6"
}
```

I have two comments: (1) the patch contains twice the new function, and (2) it would be nice to
be able to write `compose(f,x,n)` for a symbolic variable n (or any expression). Only when
n is an integer would the "nesting" be evaluated. Comment (1) needs more work, comment (2) could
be a separate ticket, but if easy it would be nice to do it.

Additional comment: please rename the patch as trac_7742.patch.



---

archive/issue_comments_066438.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-14T18:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66438",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066439.json:
```json
{
    "body": "The new patch addresses many of the above concerns (other than symbolic n), and splits the functionality into three functions:\n\n* compose(f,g) which composes functions such that compose(f,g)(x) = f(g(x))\n\n* self_compose(f, n) which composes a function with itself such that self_compose(f,n)(x) = f(...(f(x))...)\n\n* nest(f, n, a) which effectively self_composes and evaluates (but does it slightly faster than a self_compose)\n\nQuestions:\n\n* compose(f,g)(x) = f(g(x)) - is this the most common convention among mathematicians? or should the RHS be g(f(x))?\n\n* Is (f, n, a) or (f, a, n) the best order of parameters for nest?\n\n* Is there somewhere more suitable than misc/misc.py for these functions?",
    "created_at": "2010-11-04T13:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66439",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

The new patch addresses many of the above concerns (other than symbolic n), and splits the functionality into three functions:

* compose(f,g) which composes functions such that compose(f,g)(x) = f(g(x))

* self_compose(f, n) which composes a function with itself such that self_compose(f,n)(x) = f(...(f(x))...)

* nest(f, n, a) which effectively self_composes and evaluates (but does it slightly faster than a self_compose)

Questions:

* compose(f,g)(x) = f(g(x)) - is this the most common convention among mathematicians? or should the RHS be g(f(x))?

* Is (f, n, a) or (f, a, n) the best order of parameters for nest?

* Is there somewhere more suitable than misc/misc.py for these functions?



---

archive/issue_comments_066440.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-04T13:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66440",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066441.json:
```json
{
    "body": "What version of Sage are you targeting?  I tried applying both of these (individually) to 4.6.0 and to 4.5.3 and couldn't apply them.",
    "created_at": "2010-11-16T22:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66441",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

What version of Sage are you targeting?  I tried applying both of these (individually) to 4.6.0 and to 4.5.3 and couldn't apply them.



---

archive/issue_comments_066442.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-16T22:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66442",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066443.json:
```json
{
    "body": "Attachment [trac_7742-add-compose-etc.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc.patch) by flawrence created at 2010-11-17 04:40:32\n\nadds compose, self_compose and nest functions. actually replaces previous patch this time",
    "created_at": "2010-11-17T04:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66443",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac_7742-add-compose-etc.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc.patch) by flawrence created at 2010-11-17 04:40:32

adds compose, self_compose and nest functions. actually replaces previous patch this time



---

archive/issue_comments_066444.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-17T04:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66444",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066445.json:
```json
{
    "body": "Sorry, the second patch accidentally relied on the first (which needed rebasing).  I've fixed it and the second patch should now apply and work for both 4.6.0 and 4.6.1alpha0.",
    "created_at": "2010-11-17T04:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66445",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Sorry, the second patch accidentally relied on the first (which needed rebasing).  I've fixed it and the second patch should now apply and work for both 4.6.0 and 4.6.1alpha0.



---

archive/issue_comments_066446.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-17T11:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66446",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066447.json:
```json
{
    "body": "This needs more work, since the function `self_compose` fails for n=0:\n\n```\nsage: function('f');\nsage: h=self_compose(f,0)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/localdisk/tmp/sage-4.6/<ipython console> in <module>()\n\n/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)\n    890     # all necessary powers of two (f, f^2, f^4), storing them in a list\n    891     fs = [f]\n--> 892     for i in xrange(int(floor(log(n, 2)))):\n    893         fs.append(compose(fs[i], fs[i]))\n    894     \n\nValueError: math domain error\n```\n\nPaul",
    "created_at": "2010-11-17T11:51:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66447",
    "user": "https://github.com/zimmermann6"
}
```

This needs more work, since the function `self_compose` fails for n=0:

```
sage: function('f');
sage: h=self_compose(f,0)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/localdisk/tmp/sage-4.6/<ipython console> in <module>()

/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)
    890     # all necessary powers of two (f, f^2, f^4), storing them in a list
    891     fs = [f]
--> 892     for i in xrange(int(floor(log(n, 2)))):
    893         fs.append(compose(fs[i], fs[i]))
    894     

ValueError: math domain error
```

Paul



---

archive/issue_comments_066448.json:
```json
{
    "body": "Replying to [comment:12 flawrence]:\n\n> * compose(f,g)(x) = f(g(x)) - is this the most common convention among mathematicians? or should the RHS be g(f(x))?\n\ncompose(f,g) seems good to me.\n\n> * Is (f, n, a) or (f, a, n) the best order of parameters for nest?\n\nI prefer (f,n,a) since this is coherent with `self_compose(f,n)`.\n\n> * Is there somewhere more suitable than misc/misc.py for these functions?\n\nI don't know.\n\nAlso if a symbolic n is not allowed (yet) in `self_compose`, some type-checking\nshould be done:\n\n```\nsage: function('f')\nsage: var('m')\nsage: self_compose(f,m)(x)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/localdisk/tmp/sage-4.6/<ipython console> in <module>()\n\n/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)\n    890     # all necessary powers of two (f, f^2, f^4), storing them in a list\n    891     fs = [f]\n--> 892     for i in xrange(int(floor(log(n, 2)))):\n    893         fs.append(compose(fs[i], fs[i]))\n    894     \n\n/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5398)()\n\nTypeError: unable to simplify to float approximation\n```\n\n\nPaul",
    "created_at": "2010-11-17T11:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66448",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:12 flawrence]:

> * compose(f,g)(x) = f(g(x)) - is this the most common convention among mathematicians? or should the RHS be g(f(x))?

compose(f,g) seems good to me.

> * Is (f, n, a) or (f, a, n) the best order of parameters for nest?

I prefer (f,n,a) since this is coherent with `self_compose(f,n)`.

> * Is there somewhere more suitable than misc/misc.py for these functions?

I don't know.

Also if a symbolic n is not allowed (yet) in `self_compose`, some type-checking
should be done:

```
sage: function('f')
sage: var('m')
sage: self_compose(f,m)(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/localdisk/tmp/sage-4.6/<ipython console> in <module>()

/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)
    890     # all necessary powers of two (f, f^2, f^4), storing them in a list
    891     fs = [f]
--> 892     for i in xrange(int(floor(log(n, 2)))):
    893         fs.append(compose(fs[i], fs[i]))
    894     

/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5398)()

TypeError: unable to simplify to float approximation
```


Paul



---

archive/issue_comments_066449.json:
```json
{
    "body": "At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.",
    "created_at": "2010-11-18T01:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66449",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.



---

archive/issue_comments_066450.json:
```json
{
    "body": "Replying to [comment:17 jrp]:\n> At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.\n\nGiven that symbolic functions have named variables, is this the correct behavior?\n\n\nsage: f(x) = x+1\nsage: g(y) = y+1\nsage: compose(f,g)\ny + 2\nsage: compose(g,f)\nx + 2",
    "created_at": "2010-11-18T01:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66450",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Replying to [comment:17 jrp]:
> At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.

Given that symbolic functions have named variables, is this the correct behavior?


sage: f(x) = x+1
sage: g(y) = y+1
sage: compose(f,g)
y + 2
sage: compose(g,f)
x + 2



---

archive/issue_comments_066451.json:
```json
{
    "body": "Replying to [comment:18 jrp]:\n> Replying to [comment:17 jrp]:\n> > At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.\n> \n> Given that symbolic functions have named variables, is this the correct behavior?\n> \n> \n> sage: f(x) = x+1\n> sage: g(y) = y+1\n> sage: compose(f,g)\n> y + 2\n> sage: compose(g,f)\n> x + 2\nI don't actually know anything about symbolic functions in Sage.  As such, all doctests and examples in the patch are for regular python functions not symbolic functions.  The compose functions in the patch use lambda functions, which may or may not break symbolic functions.\n\nWith normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using \"timeit\").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).  But I don't know if anyone is interested in large n cases.",
    "created_at": "2010-11-18T03:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66451",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Replying to [comment:18 jrp]:
> Replying to [comment:17 jrp]:
> > At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.
> 
> Given that symbolic functions have named variables, is this the correct behavior?
> 
> 
> sage: f(x) = x+1
> sage: g(y) = y+1
> sage: compose(f,g)
> y + 2
> sage: compose(g,f)
> x + 2
I don't actually know anything about symbolic functions in Sage.  As such, all doctests and examples in the patch are for regular python functions not symbolic functions.  The compose functions in the patch use lambda functions, which may or may not break symbolic functions.

With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using "timeit").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).  But I don't know if anyone is interested in large n cases.



---

archive/issue_comments_066452.json:
```json
{
    "body": "Replying to [comment:19 flawrence]:\n\n> With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using \"timeit\").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).\n\nI ran the following:\n\n```\nsage: def f(x):\n....:     return x + 1\n....: \nsage: g = self_compose(f,10000)\nsage: g\n<function <lambda> at 0xb0aa80c>\nsage: timeit('g(0)')\n25 loops, best of 3: 9.41 ms per loop\nsage: timeit('nest(f,10000,0)')\n125 loops, best of 3: 6.35 ms per loop\n```\n\nSince nest just loops through xrange and doesn't use powers of two, maybe the slowdown before was due to the recursion.  But in any case, it definitely helps with the symbolic ones.\n\n> The compose functions in the patch use lambda functions, which may or may not break symbolic functions.\n\nI'm attaching a patch to check for symbolic functions and (hopefully) do the right thing.  I also make self_compose(f,0) return the identity.",
    "created_at": "2010-11-18T07:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66452",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Replying to [comment:19 flawrence]:

> With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using "timeit").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).

I ran the following:

```
sage: def f(x):
....:     return x + 1
....: 
sage: g = self_compose(f,10000)
sage: g
<function <lambda> at 0xb0aa80c>
sage: timeit('g(0)')
25 loops, best of 3: 9.41 ms per loop
sage: timeit('nest(f,10000,0)')
125 loops, best of 3: 6.35 ms per loop
```

Since nest just loops through xrange and doesn't use powers of two, maybe the slowdown before was due to the recursion.  But in any case, it definitely helps with the symbolic ones.

> The compose functions in the patch use lambda functions, which may or may not break symbolic functions.

I'm attaching a patch to check for symbolic functions and (hopefully) do the right thing.  I also make self_compose(f,0) return the identity.



---

archive/issue_comments_066453.json:
```json
{
    "body": "> Given that symbolic functions have named variables, is this the correct behavior?\n\n```\nsage: f(x) = x+1\nsage: g(y) = y+1\nsage: compose(f,g)\ny + 2\nsage: compose(g,f)\nx + 2\n```\n\n\n[please use { { { and } } } to quote Sage examples]\n\nI can't reproduce this. I get with the patch from Felix:\n\n```\nsage: f(x) = x+1\nsage: g(y) = y+1\nsage: compose(f,g)\n<function <lambda> at 0x1787c80>\nsage: compose(f,g)(x)\nx + 2\n```\n\nwhich seems ok to me.\n\nPaul",
    "created_at": "2010-11-18T07:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66453",
    "user": "https://github.com/zimmermann6"
}
```

> Given that symbolic functions have named variables, is this the correct behavior?

```
sage: f(x) = x+1
sage: g(y) = y+1
sage: compose(f,g)
y + 2
sage: compose(g,f)
x + 2
```


[please use { { { and } } } to quote Sage examples]

I can't reproduce this. I get with the patch from Felix:

```
sage: f(x) = x+1
sage: g(y) = y+1
sage: compose(f,g)
<function <lambda> at 0x1787c80>
sage: compose(f,g)(x)
x + 2
```

which seems ok to me.

Paul



---

archive/issue_comments_066454.json:
```json
{
    "body": "Special treatment of symbolic functions.",
    "created_at": "2010-11-18T19:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66454",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Special treatment of symbolic functions.



---

archive/issue_comments_066455.json:
```json
{
    "body": "Attachment [trac_7742-symbolics.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-symbolics.patch) by jrp created at 2010-11-18 19:11:30\n\nI realized that what really matters is the type of the first function in the composition - i.e., the type of g in compose(f,g).",
    "created_at": "2010-11-18T19:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66455",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Attachment [trac_7742-symbolics.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-symbolics.patch) by jrp created at 2010-11-18 19:11:30

I realized that what really matters is the type of the first function in the composition - i.e., the type of g in compose(f,g).



---

archive/issue_comments_066456.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-18T19:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66456",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066457.json:
```json
{
    "body": "jrp, you didn't answer comment 21. What was wrong with Felix patch?\n\nPaul",
    "created_at": "2010-11-18T19:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66457",
    "user": "https://github.com/zimmermann6"
}
```

jrp, you didn't answer comment 21. What was wrong with Felix patch?

Paul



---

archive/issue_comments_066458.json:
```json
{
    "body": "Paul - I wanted it to automatically do the right thing when g is a symbolic function.  I agree that this isn't very important since we can already just call compose(f,g)(x).  More important is that with symbolics, now the powers-of-two optimization will work.  (I don't think it did before, but will think more on this).",
    "created_at": "2010-11-18T19:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66458",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Paul - I wanted it to automatically do the right thing when g is a symbolic function.  I agree that this isn't very important since we can already just call compose(f,g)(x).  More important is that with symbolics, now the powers-of-two optimization will work.  (I don't think it did before, but will think more on this).



---

archive/issue_comments_066459.json:
```json
{
    "body": "I am not very happy with the fact that when f is an expression, the code assumes it has exactly\none symbolic variable:\n\n```\nsage: f = 2\nsage: self_compose(f,0)\n<function <lambda> at 0x41031b8>\nsage: self_compose(f,1)\n2\nsage: self_compose(f,2)\n<function <lambda> at 0x7fa8ac2b0d70>\n```\n\nor\n\n```\nsage: f = x+y\nsage: self_compose(f,0)\nx\nsage: self_compose(f,1)\nx + y\nsage: self_compose(f,2)\nx + 2*y\n```\n\nConsider also:\n\n```\nsage: f = pi+1\nsage: self_compose(f,0)\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/tmp/cado-nfs-1.0-rc1/<ipython console> in <module>()\n\n/usr/local/sage-4.6/sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)\n    911     if n == 0:\n    912         if type(f) == sage.symbolic.expression.Expression:\n--> 913             return f.parent()(f.variables()[0])\n    914         else:\n    915             return lambda x: x\n\nIndexError: tuple index out of range\n```\n\n\nI would prefer that symbolic expressions such as `f=x+1` are not allowed,\nand we should write instead `f(x)=x+1` or `f = lambda x : x+1`.\n\nPaul",
    "created_at": "2010-11-18T20:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66459",
    "user": "https://github.com/zimmermann6"
}
```

I am not very happy with the fact that when f is an expression, the code assumes it has exactly
one symbolic variable:

```
sage: f = 2
sage: self_compose(f,0)
<function <lambda> at 0x41031b8>
sage: self_compose(f,1)
2
sage: self_compose(f,2)
<function <lambda> at 0x7fa8ac2b0d70>
```

or

```
sage: f = x+y
sage: self_compose(f,0)
x
sage: self_compose(f,1)
x + y
sage: self_compose(f,2)
x + 2*y
```

Consider also:

```
sage: f = pi+1
sage: self_compose(f,0)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/tmp/cado-nfs-1.0-rc1/<ipython console> in <module>()

/usr/local/sage-4.6/sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)
    911     if n == 0:
    912         if type(f) == sage.symbolic.expression.Expression:
--> 913             return f.parent()(f.variables()[0])
    914         else:
    915             return lambda x: x

IndexError: tuple index out of range
```


I would prefer that symbolic expressions such as `f=x+1` are not allowed,
and we should write instead `f(x)=x+1` or `f = lambda x : x+1`.

Paul



---

archive/issue_comments_066460.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-18T20:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66460",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066461.json:
```json
{
    "body": "Replying to [comment:25 zimmerma]:\n> I would prefer that symbolic expressions such as `f=x+1` are not allowed,\n> and we should write instead `f(x)=x+1` or `f = lambda x : x+1`.\n\nI now think it's best to leave compose,self_compose, and nest agnostic to the type of f; the user can supply anything callable and we won't attempt to turn it back into a symbolic function.\n\nThen as a separate issue, symbolic functions can grow an f.self_compose(n) function that plays nice with types.",
    "created_at": "2010-11-22T20:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66461",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Replying to [comment:25 zimmerma]:
> I would prefer that symbolic expressions such as `f=x+1` are not allowed,
> and we should write instead `f(x)=x+1` or `f = lambda x : x+1`.

I now think it's best to leave compose,self_compose, and nest agnostic to the type of f; the user can supply anything callable and we won't attempt to turn it back into a symbolic function.

Then as a separate issue, symbolic functions can grow an f.self_compose(n) function that plays nice with types.



---

archive/issue_comments_066462.json:
```json
{
    "body": "Replying to [comment:19 flawrence]:\n> With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using \"timeit\").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).  But I don't know if anyone is interested in large n cases.\n\nWith normal python functions, I don't think there is any gain from powers of two.\n\nWith the self_compose from adds-compose-etc.patch:\n\n\n```\nsage: f = lambda x: x + 1\nsage: g = x + 1\nsage: f1 = self_compose(f,10000)\nsage: g1 = self_compose(g,10000)\nsage: timeit('self_compose(f,10000)')\n625 loops, best of 3: 66.6 \u00b5s per loop\nsage: timeit('self_compose(g,10000)')\n625 loops, best of 3: 66.9 \u00b5s per loop\nsage: timeit('f1(0)')                \n25 loops, best of 3: 9.32 ms per loop\nsage: timeit('g1(0)')\n5 loops, best of 3: 375 ms per loop\nsage: timeit('nest(f,10000,0)')\n125 loops, best of 3: 6.46 ms per loop\nsage: timeit('nest(g,10000,0)')\n5 loops, best of 3: 379 ms per loop\nsage: def new_self_compose(f,n):\n....:     return lambda a: nest(f,n,a)\n....: \nsage: timeit('new_self_compose(f,10000)')\n625 loops, best of 3: 1.17 \u00b5s per loop\nsage: timeit('new_self_compose(g,10000)')\n625 loops, best of 3: 2.68 \u00b5s per loop\n```\n\n\nSince self_compose is implemented via `lambda x: f(g(x))`, we have to eventually pass the argument through `f` the correct number of times.\n\nLet's move the powers of two, and the symbolics handling, into a method of symbolic functions.  Then the compose tools for python functions can have fast, dirt-simple implementations.",
    "created_at": "2010-11-22T20:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66462",
    "user": "https://trac.sagemath.org/admin/accounts/users/jrp"
}
```

Replying to [comment:19 flawrence]:
> With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using "timeit").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).  But I don't know if anyone is interested in large n cases.

With normal python functions, I don't think there is any gain from powers of two.

With the self_compose from adds-compose-etc.patch:


```
sage: f = lambda x: x + 1
sage: g = x + 1
sage: f1 = self_compose(f,10000)
sage: g1 = self_compose(g,10000)
sage: timeit('self_compose(f,10000)')
625 loops, best of 3: 66.6 µs per loop
sage: timeit('self_compose(g,10000)')
625 loops, best of 3: 66.9 µs per loop
sage: timeit('f1(0)')                
25 loops, best of 3: 9.32 ms per loop
sage: timeit('g1(0)')
5 loops, best of 3: 375 ms per loop
sage: timeit('nest(f,10000,0)')
125 loops, best of 3: 6.46 ms per loop
sage: timeit('nest(g,10000,0)')
5 loops, best of 3: 379 ms per loop
sage: def new_self_compose(f,n):
....:     return lambda a: nest(f,n,a)
....: 
sage: timeit('new_self_compose(f,10000)')
625 loops, best of 3: 1.17 µs per loop
sage: timeit('new_self_compose(g,10000)')
625 loops, best of 3: 2.68 µs per loop
```


Since self_compose is implemented via `lambda x: f(g(x))`, we have to eventually pass the argument through `f` the correct number of times.

Let's move the powers of two, and the symbolics handling, into a method of symbolic functions.  Then the compose tools for python functions can have fast, dirt-simple implementations.



---

archive/issue_comments_066463.json:
```json
{
    "body": "Attachment [trac_7742-add-compose-etc_v2.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc_v2.patch) by flawrence created at 2010-11-23 04:57:51\n\nadds compose, self_compose and nest functions. self_compose is a wrapper for nest.  a self-contained patch.",
    "created_at": "2010-11-23T04:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66463",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac_7742-add-compose-etc_v2.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc_v2.patch) by flawrence created at 2010-11-23 04:57:51

adds compose, self_compose and nest functions. self_compose is a wrapper for nest.  a self-contained patch.



---

archive/issue_comments_066464.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-23T05:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66464",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066465.json:
```json
{
    "body": "Changing component from basic arithmetic to misc.",
    "created_at": "2010-11-23T05:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66465",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing component from basic arithmetic to misc.



---

archive/issue_comments_066466.json:
```json
{
    "body": "Replying to [comment:27 jrp]:\n> With normal python functions, I don't think there is any gain from powers of two.\n> \n> With the self_compose from adds-compose-etc.patch:\n(snip)\n> Since self_compose is implemented via `lambda x: f(g(x))`, we have to eventually pass the argument through `f` the correct number of times.\n\nYes, `nest` is always faster than `self_compose` if you actually want to evaluate the function.  However the functions do different things: `nest` isn't really a compose function, since it returns f^n(x) not f^n.  `self_compose` is more useful than `nest` if you want to forget about f and only want to apply `f^n`.  In hindsight, `self_compose` should actually look like this, which I agree would be faster to construct and to evaluate than the powers of two method:\n\n```\n\ndef self_compose(f,n):\n    return lambda x: nest(f,n,x)\n```\n \n> Let's move the powers of two, and the symbolics handling, into a method of symbolic functions.  Then the compose tools for python functions can have fast, dirt-simple implementations.\nI agree that we should scrap the powers of two, and not go out of our way to support symbolics in this ticket.  I'm uploading a patch that makes the change detailed above.  I'm not going to have any more time to work on this for at least a month, so someone else will have to finish the ticket if further changes are required.\n\nThe new patch works for n = 0, but still does not check whether n is symbolic.  I don't think this is the worst thing in the world: the documentation does state that n should be a nonnegative integer, and if it is symbolic then the error raised is appropriate IMO:\n\n```\n\nsage: _ = var('x y')\nsage: nest(sin,x,y)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Applications/sage/devel/sage-dev/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in nest(f, n, x)\n    939     \n    940     \"\"\"\n--> 941     for i in xrange(n):\n    942         x = f(x)\n    943     return x\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__int__ (sage/symbolic/expression.cpp:4375)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17185)()\n\nTypeError: cannot evaluate symbolic expression numerically\n```\n",
    "created_at": "2010-11-23T05:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66466",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Replying to [comment:27 jrp]:
> With normal python functions, I don't think there is any gain from powers of two.
> 
> With the self_compose from adds-compose-etc.patch:
(snip)
> Since self_compose is implemented via `lambda x: f(g(x))`, we have to eventually pass the argument through `f` the correct number of times.

Yes, `nest` is always faster than `self_compose` if you actually want to evaluate the function.  However the functions do different things: `nest` isn't really a compose function, since it returns f^n(x) not f^n.  `self_compose` is more useful than `nest` if you want to forget about f and only want to apply `f^n`.  In hindsight, `self_compose` should actually look like this, which I agree would be faster to construct and to evaluate than the powers of two method:

```

def self_compose(f,n):
    return lambda x: nest(f,n,x)
```
 
> Let's move the powers of two, and the symbolics handling, into a method of symbolic functions.  Then the compose tools for python functions can have fast, dirt-simple implementations.
I agree that we should scrap the powers of two, and not go out of our way to support symbolics in this ticket.  I'm uploading a patch that makes the change detailed above.  I'm not going to have any more time to work on this for at least a month, so someone else will have to finish the ticket if further changes are required.

The new patch works for n = 0, but still does not check whether n is symbolic.  I don't think this is the worst thing in the world: the documentation does state that n should be a nonnegative integer, and if it is symbolic then the error raised is appropriate IMO:

```

sage: _ = var('x y')
sage: nest(sin,x,y)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Applications/sage/devel/sage-dev/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in nest(f, n, x)
    939     
    940     """
--> 941     for i in xrange(n):
    942         x = f(x)
    943     return x

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__int__ (sage/symbolic/expression.cpp:4375)()

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17185)()

TypeError: cannot evaluate symbolic expression numerically
```




---

archive/issue_comments_066467.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-11-23T05:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66467",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_066468.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-24T07:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66468",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066469.json:
```json
{
    "body": "Please state clearly in the ticket description which patches have to be applied.",
    "created_at": "2010-12-02T13:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66469",
    "user": "https://github.com/jdemeyer"
}
```

Please state clearly in the ticket description which patches have to be applied.



---

archive/issue_comments_066470.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-12-02T13:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66470",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_066471.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-12-03T22:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66471",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066472.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-03T22:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66472",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066473.json:
```json
{
    "body": "This needs to be rebased to sage-4.6.2.alpha2.  You might also want to check for conflicts with #8456 (so it might be safer to base your patch to sage-4.6.2.alpha2 + #8456).",
    "created_at": "2011-01-26T18:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66473",
    "user": "https://github.com/jdemeyer"
}
```

This needs to be rebased to sage-4.6.2.alpha2.  You might also want to check for conflicts with #8456 (so it might be safer to base your patch to sage-4.6.2.alpha2 + #8456).



---

archive/issue_comments_066474.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-26T18:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66474",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066475.json:
```json
{
    "body": "does anybody know why this patch with positive review was not included in 4.6.1?\n\nPaul",
    "created_at": "2011-01-26T20:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66475",
    "user": "https://github.com/zimmermann6"
}
```

does anybody know why this patch with positive review was not included in 4.6.1?

Paul



---

archive/issue_comments_066476.json:
```json
{
    "body": "Replying to [comment:35 zimmerma]:\n> does anybody know why this patch with positive review was not included in 4.6.1?\nI know because I was the one making that decision.\n\nMost likely, the 4.6.1 release cycle was in bug-fix-only status at the time when this patch got positive_review.  Unfortunately, 4.6.1 stayed in that status for quite a while (much longer than usual Sage releases) because there were a lot of changes in the Sage build scripts giving rise to many system-specific issues which had to be tracked down.",
    "created_at": "2011-01-26T21:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66476",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:35 zimmerma]:
> does anybody know why this patch with positive review was not included in 4.6.1?
I know because I was the one making that decision.

Most likely, the 4.6.1 release cycle was in bug-fix-only status at the time when this patch got positive_review.  Unfortunately, 4.6.1 stayed in that status for quite a while (much longer than usual Sage releases) because there were a lot of changes in the Sage build scripts giving rise to many system-specific issues which had to be tracked down.



---

archive/issue_comments_066477.json:
```json
{
    "body": "Anybody wants to look at this?...",
    "created_at": "2011-02-16T09:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66477",
    "user": "https://github.com/jdemeyer"
}
```

Anybody wants to look at this?...



---

archive/issue_comments_066478.json:
```json
{
    "body": "Attachment [trac_7742-add-compose-etc_v2_rebased.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc_v2_rebased.patch) by flawrence created at 2011-02-19 07:13:33\n\nRebased for 4.6.2.rc0",
    "created_at": "2011-02-19T07:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66478",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac_7742-add-compose-etc_v2_rebased.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc_v2_rebased.patch) by flawrence created at 2011-02-19 07:13:33

Rebased for 4.6.2.rc0



---

archive/issue_comments_066479.json:
```json
{
    "body": "Only change since the positive review was updating the change to sage/misc/all.py",
    "created_at": "2011-02-19T07:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66479",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Only change since the positive review was updating the change to sage/misc/all.py



---

archive/issue_comments_066480.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-19T07:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66480",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066481.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-02-19T08:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66481",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066482.json:
```json
{
    "body": "a minor point: it would be good to check that n is indeed a nonnegative integer in\n`self_compose` and `nest`, otherwise we can get strange results:\n\n```\nsage: self_compose(sin, -3)(x) \nx\nsage: self_compose(sin, x)(x)\n...\nTypeError: cannot evaluate symbolic expression numerically\n```\n\n\nPaul",
    "created_at": "2011-02-19T08:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66482",
    "user": "https://github.com/zimmermann6"
}
```

a minor point: it would be good to check that n is indeed a nonnegative integer in
`self_compose` and `nest`, otherwise we can get strange results:

```
sage: self_compose(sin, -3)(x) 
x
sage: self_compose(sin, x)(x)
...
TypeError: cannot evaluate symbolic expression numerically
```


Paul



---

archive/issue_comments_066483.json:
```json
{
    "body": "Attachment [trac_7742-add-compose-etc_v2.1.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc_v2.1.patch) by flawrence created at 2011-02-19 10:35:52\n\nchecks that n is a nonnegative integer",
    "created_at": "2011-02-19T10:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66483",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Attachment [trac_7742-add-compose-etc_v2.1.patch](tarball://root/attachments/some-uuid/ticket7742/trac_7742-add-compose-etc_v2.1.patch) by flawrence created at 2011-02-19 10:35:52

checks that n is a nonnegative integer



---

archive/issue_comments_066484.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-19T10:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66484",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066485.json:
```json
{
    "body": "Replying to [comment:39 zimmerma]:\n> a minor point: it would be good to check that n is indeed a nonnegative integer in\n> `self_compose` and `nest`, otherwise we can get strange results\n\nDone:\n\n\n```\nsage: self_compose(sin, -3)\n...\nValueError: n must be a nonnegative integer, not -3.\nsage: self_compose(sin, x)\n...\nTypeError: n (=x) must be of type (<type 'int'>, <type 'long'>, <type 'sage.rings.integer.Integer'>).\n```\n",
    "created_at": "2011-02-19T10:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66485",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Replying to [comment:39 zimmerma]:
> a minor point: it would be good to check that n is indeed a nonnegative integer in
> `self_compose` and `nest`, otherwise we can get strange results

Done:


```
sage: self_compose(sin, -3)
...
ValueError: n must be a nonnegative integer, not -3.
sage: self_compose(sin, x)
...
TypeError: n (=x) must be of type (<type 'int'>, <type 'long'>, <type 'sage.rings.integer.Integer'>).
```




---

archive/issue_comments_066486.json:
```json
{
    "body": "positive review, thank you Christoph and Felix for that nice work!\n\nPaul",
    "created_at": "2011-02-19T14:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66486",
    "user": "https://github.com/zimmermann6"
}
```

positive review, thank you Christoph and Felix for that nice work!

Paul



---

archive/issue_comments_066487.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-19T14:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66487",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066488.json:
```json
{
    "body": "and thank you for the extra rebase work, I hope this time the patch will be included soon...\n\nPaul",
    "created_at": "2011-02-19T14:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66488",
    "user": "https://github.com/zimmermann6"
}
```

and thank you for the extra rebase work, I hope this time the patch will be included soon...

Paul



---

archive/issue_comments_066489.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-17T19:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7742#issuecomment-66489",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
