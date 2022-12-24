# Issue 6922: Matrix term ordering

archive/issues_006922.json:
```json
{
    "body": "Assignee: Somebody\n\nCC:  novoselt\n\nKeywords: term order\n\nIn Sage, I am trying to construct a polynomial ring with matrix\nordering. \n....\nAFAIK, it is not implemented, but I think that some people were\nworking on it.\n\nIt is in fact one of the things that I miss in Sage's polynomial rings\n(the other thing are supercommutative rings), so that I need to use\nthe Singular interface rather than libsingular. \n....\nAnyway it will be great that the matrix ordering is included in Sage\nnatively. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6922\n\n",
    "created_at": "2009-09-11T04:47:10Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Matrix term ordering",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6922",
    "user": "klee"
}
```
Assignee: Somebody

CC:  novoselt

Keywords: term order

In Sage, I am trying to construct a polynomial ring with matrix
ordering. 
....
AFAIK, it is not implemented, but I think that some people were
working on it.

It is in fact one of the things that I miss in Sage's polynomial rings
(the other thing are supercommutative rings), so that I need to use
the Singular interface rather than libsingular. 
....
Anyway it will be great that the matrix ordering is included in Sage
natively. 

Issue created by migration from https://trac.sagemath.org/ticket/6922





---

archive/issue_comments_057137.json:
```json
{
    "body": "The patch introduces matrix term ordering, but it does not work yet unfortunately.\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: local2\nsage: R.<x,y>=PolynomialRing(QQ,order=\"matrix(1,3,1,0)\")\nsage: r=singular(R)\nsage: r\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n//   characteristic : 0\n//   number of vars : 2\n//        block   1 : ordering M\n//                  : names    x y \n//                  : weights  1 3 \n//                  : weights  1 0 \n//        block   2 : ordering C\nsage: f=x^2+y\nsage: f.lt()\nx^2\nsage: f=x^3+y\nsage: f.lt()\nx^3\nsage: t=R.term_order()\nsage: t\nmatrix(1,3,1,0) term order\n```\n\n\nPlease someone who knows better check the patch, and make it work!\n\nSimon says:\n\nBetter wait for a proper implementation in libsingular \n(which is beyond my capabilities, I am afraid).\n\nCheers,\nSimon",
    "created_at": "2009-09-11T05:05:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57137",
    "user": "klee"
}
```

The patch introduces matrix term ordering, but it does not work yet unfortunately.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: local2
sage: R.<x,y>=PolynomialRing(QQ,order="matrix(1,3,1,0)")
sage: r=singular(R)
sage: r
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
//   characteristic : 0
//   number of vars : 2
//        block   1 : ordering M
//                  : names    x y 
//                  : weights  1 3 
//                  : weights  1 0 
//        block   2 : ordering C
sage: f=x^2+y
sage: f.lt()
x^2
sage: f=x^3+y
sage: f.lt()
x^3
sage: t=R.term_order()
sage: t
matrix(1,3,1,0) term order
```


Please someone who knows better check the patch, and make it work!

Simon says:

Better wait for a proper implementation in libsingular 
(which is beyond my capabilities, I am afraid).

Cheers,
Simon



---

archive/issue_comments_057138.json:
```json
{
    "body": "I don't think we should support the 'matrix()' syntax. The Singular syntax is 'M()' which we should support for compatibility and familiarity. However, adding another string expression does not seem to make sense, because we will be able to simply write `order=A` where A is an integer matrix which is much more python-ic.",
    "created_at": "2009-09-11T10:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57138",
    "user": "malb"
}
```

I don't think we should support the 'matrix()' syntax. The Singular syntax is 'M()' which we should support for compatibility and familiarity. However, adding another string expression does not seem to make sense, because we will be able to simply write `order=A` where A is an integer matrix which is much more python-ic.



---

archive/issue_comments_057139.json:
```json
{
    "body": "I agree partially. Should we follow the Singular syntax exactly? For short syntax, how about just \"m(1,3,1,0)\"? I personally think the Singular syntax for term ordering is somewhat cryptic.\n\nI think it is better for Sage to support both the string description and `TermOrder` description. Thus for examples,\n\n\n```\norder='m(1,3,1,0)'+'deglex(2)'\n```\n\n\n\n```\norder='m(1,3,1,0),deglex(3)'\n```\n\n\nfor a square matrix m,\n\n```\norder=TermOrder(m)+TermOrder('deglex',3)\n```\n\n\nare all supported.\n\nMarshall Hampton says:\n\nI agree with John that Simon's example:\n\n\n```\n  sage: M = Matrix(2,2, [1,3,1,0])\n  sage: R.<a,b,c,d,e,f> = PolynomialRing(QQ, order=TermOrder(M)\n+TermOrder('deglex',3))\n```\n\n\nlooks good and reasonably intuitive to me.",
    "created_at": "2009-09-12T01:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57139",
    "user": "klee"
}
```

I agree partially. Should we follow the Singular syntax exactly? For short syntax, how about just "m(1,3,1,0)"? I personally think the Singular syntax for term ordering is somewhat cryptic.

I think it is better for Sage to support both the string description and `TermOrder` description. Thus for examples,


```
order='m(1,3,1,0)'+'deglex(2)'
```



```
order='m(1,3,1,0),deglex(3)'
```


for a square matrix m,

```
order=TermOrder(m)+TermOrder('deglex',3)
```


are all supported.

Marshall Hampton says:

I agree with John that Simon's example:


```
  sage: M = Matrix(2,2, [1,3,1,0])
  sage: R.<a,b,c,d,e,f> = PolynomialRing(QQ, order=TermOrder(M)
+TermOrder('deglex',3))
```


looks good and reasonably intuitive to me.



---

archive/issue_comments_057140.json:
```json
{
    "body": "Replying to [comment:3 klee]:\n> I agree partially. Should we follow the Singular syntax exactly? For short syntax, how about just \"m(1,3,1,0)\"? I personally think the Singular syntax for term ordering is somewhat cryptic.\n\nSure, but it would be accepted anyway and passed through to Singular (in an ideal implementation) :)\n\n> I think it is better for Sage to support both the string description and `TermOrder` description. Thus for examples,\n> \n> {{{\n> order='m(1,3,1,0)'+'deglex(2)'\n> }}}\n> \n> {{{\n> order='m(1,3,1,0),deglex(3)'\n> }}}\n\nThis description is a mix of Singular syntax and Sage string syntax. I would like to avoid Sage string syntax as much as possible.\n\n> for a square matrix m,\n> {{{\n> order=TermOrder(m)+TermOrder('deglex',3)\n> }}}\n> are all supported.\n\nI like this best.\n \n> Marshall Hampton says:\n> \n> I agree with John that Simon's example:\n> \n> {{{\n>   sage: M = Matrix(2,2, [1,3,1,0])\n>   sage: R.<a,b,c,d,e,f> = PolynomialRing(QQ, order=TermOrder(M)\n> +TermOrder('deglex',3))\n> }}}\n> \n> looks good and reasonably intuitive to me.\n\nYep, that's what I would be aiming for.",
    "created_at": "2009-09-12T09:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57140",
    "user": "malb"
}
```

Replying to [comment:3 klee]:
> I agree partially. Should we follow the Singular syntax exactly? For short syntax, how about just "m(1,3,1,0)"? I personally think the Singular syntax for term ordering is somewhat cryptic.

Sure, but it would be accepted anyway and passed through to Singular (in an ideal implementation) :)

> I think it is better for Sage to support both the string description and `TermOrder` description. Thus for examples,
> 
> {{{
> order='m(1,3,1,0)'+'deglex(2)'
> }}}
> 
> {{{
> order='m(1,3,1,0),deglex(3)'
> }}}

This description is a mix of Singular syntax and Sage string syntax. I would like to avoid Sage string syntax as much as possible.

> for a square matrix m,
> {{{
> order=TermOrder(m)+TermOrder('deglex',3)
> }}}
> are all supported.

I like this best.
 
> Marshall Hampton says:
> 
> I agree with John that Simon's example:
> 
> {{{
>   sage: M = Matrix(2,2, [1,3,1,0])
>   sage: R.<a,b,c,d,e,f> = PolynomialRing(QQ, order=TermOrder(M)
> +TermOrder('deglex',3))
> }}}
> 
> looks good and reasonably intuitive to me.

Yep, that's what I would be aiming for.



---

archive/issue_comments_057141.json:
```json
{
    "body": "The replaced patch is still in beta stage, due to lack of docstrings. It adds matrix ordering to Sage term order suite, which works fine. It is based on Sage 4.4.2. The reason that I uploaded this premature patch is related with the ticket !#9003",
    "created_at": "2010-05-25T15:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57141",
    "user": "klee"
}
```

The replaced patch is still in beta stage, due to lack of docstrings. It adds matrix ordering to Sage term order suite, which works fine. It is based on Sage 4.4.2. The reason that I uploaded this premature patch is related with the ticket !#9003



---

archive/issue_comments_057142.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-25T15:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57142",
    "user": "klee"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_057143.json:
```json
{
    "body": "The replaced patch now works, though only with PolyDict engine.",
    "created_at": "2010-05-27T02:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57143",
    "user": "klee"
}
```

The replaced patch now works, though only with PolyDict engine.



---

archive/issue_comments_057144.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-27T02:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57144",
    "user": "klee"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057145.json:
```json
{
    "body": "Replying to [comment:6 klee]:\n> The replaced patch now works, though only with PolyDict engine.\n\nSorry for being a bit obnoxious about it, but shouldn't this be needs work until it works across the board? At least we should fall back to the `PolyDict` version automatically if a matrix term ordering is selected or something.",
    "created_at": "2010-06-02T18:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57145",
    "user": "malb"
}
```

Replying to [comment:6 klee]:
> The replaced patch now works, though only with PolyDict engine.

Sorry for being a bit obnoxious about it, but shouldn't this be needs work until it works across the board? At least we should fall back to the `PolyDict` version automatically if a matrix term ordering is selected or something.



---

archive/issue_comments_057146.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-03T00:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57146",
    "user": "klee"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057147.json:
```json
{
    "body": "Replying to [comment:9 malb]:\n\n> Sorry for being a bit obnoxious about it, but shouldn't this be needs work until it works across the board? At least we should fall back to the `PolyDict` version automatically if a matrix term ordering is selected or something. \u00a0\u00a0\n\nI am sorry that I cannot understand what you mean. Do you mean that matrix term order should work with Singular version before this patch is merged? Now, if a matrix term ordering is selected, then {{PolyDict}} version is used automatically because Singular version does not support matrix term ordering. If someone implements matrix term ordering with Singular version, then I would be happy. I have been waiting for this to be done. As it is not the case, I thought it's not bad to add matrix term ordering support only with {{PolyDict}} version--Singular version may be added later.",
    "created_at": "2010-06-03T00:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57147",
    "user": "klee"
}
```

Replying to [comment:9 malb]:

> Sorry for being a bit obnoxious about it, but shouldn't this be needs work until it works across the board? At least we should fall back to the `PolyDict` version automatically if a matrix term ordering is selected or something.   

I am sorry that I cannot understand what you mean. Do you mean that matrix term order should work with Singular version before this patch is merged? Now, if a matrix term ordering is selected, then {{PolyDict}} version is used automatically because Singular version does not support matrix term ordering. If someone implements matrix term ordering with Singular version, then I would be happy. I have been waiting for this to be done. As it is not the case, I thought it's not bad to add matrix term ordering support only with {{PolyDict}} version--Singular version may be added later.



---

archive/issue_comments_057148.json:
```json
{
    "body": "> I am sorry that I cannot understand what you mean. Do you mean that matrix term \n> order should work with Singular version before this patch is merged? Now, if a \n> matrix term ordering is selected, then `PolyDict` version is used \n> automatically because Singular version does not support matrix term ordering. \n\nRight, I forgot that I implemented to fall back this way :) Okay, my bad then. \n\n> If someone implements matrix term ordering with Singular version, then I would be \n> happy. \n\nWe all would be happy. All one needs to do btw. is to fix the constructor.\n\n> I have been waiting for this to be done. \n\nWhy not give it a try yourself? I'd love to help but other commitments prevent me from doing so.\n\n> As it is not the case, I thought it's not bad to add matrix term ordering support \n> only with `PolyDict` version--Singular version may be added later.\u00a0\n\nYou are right, I stand corrected.",
    "created_at": "2010-06-03T21:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57148",
    "user": "malb"
}
```

> I am sorry that I cannot understand what you mean. Do you mean that matrix term 
> order should work with Singular version before this patch is merged? Now, if a 
> matrix term ordering is selected, then `PolyDict` version is used 
> automatically because Singular version does not support matrix term ordering. 

Right, I forgot that I implemented to fall back this way :) Okay, my bad then. 

> If someone implements matrix term ordering with Singular version, then I would be 
> happy. 

We all would be happy. All one needs to do btw. is to fix the constructor.

> I have been waiting for this to be done. 

Why not give it a try yourself? I'd love to help but other commitments prevent me from doing so.

> As it is not the case, I thought it's not bad to add matrix term ordering support 
> only with `PolyDict` version--Singular version may be added later. 

You are right, I stand corrected.



---

archive/issue_comments_057149.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-03T21:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57149",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057150.json:
```json
{
    "body": "I stand corrected twice. YOU implemented it to fall back not me. I thought the automatic fallback would kick in, but from your patch it looks like it doesn't.",
    "created_at": "2010-06-03T21:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57150",
    "user": "malb"
}
```

I stand corrected twice. YOU implemented it to fall back not me. I thought the automatic fallback would kick in, but from your patch it looks like it doesn't.



---

archive/issue_comments_057151.json:
```json
{
    "body": "* `NotImplementedError, \"Singular engine in Sage cannot handle matrix ordering yet.\"` should be replaced by `NotImplementedError(\"Matrix term orderings are not supported by the libSingular interface yet.\"` or something along those lines. I propose this change to make it clearer that Singular can indeed deal with Matrix term orderings and that it is us who cannot.\n  * `TypeError: Cannot use a matrix term order as a block.` shouldn't that be a `NotImplementedError`?\n  * I thought the agreement was not to allow 'matrix(0,1,2,3)' but to use Singular's convention instead? It seems you are allowing at and using it internally.",
    "created_at": "2010-06-03T21:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57151",
    "user": "malb"
}
```

* `NotImplementedError, "Singular engine in Sage cannot handle matrix ordering yet."` should be replaced by `NotImplementedError("Matrix term orderings are not supported by the libSingular interface yet."` or something along those lines. I propose this change to make it clearer that Singular can indeed deal with Matrix term orderings and that it is us who cannot.
  * `TypeError: Cannot use a matrix term order as a block.` shouldn't that be a `NotImplementedError`?
  * I thought the agreement was not to allow 'matrix(0,1,2,3)' but to use Singular's convention instead? It seems you are allowing at and using it internally.



---

archive/issue_comments_057152.json:
```json
{
    "body": "Oh, one more thing, isn't\n\n\n```python\nTermOrder([0,1,2,3])\n```\n\n\nambiguous since it could be interpreted as a list of weights? I'd vote to not to allow it for matrix term orders.",
    "created_at": "2010-06-03T21:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57152",
    "user": "malb"
}
```

Oh, one more thing, isn't


```python
TermOrder([0,1,2,3])
```


ambiguous since it could be interpreted as a list of weights? I'd vote to not to allow it for matrix term orders.



---

archive/issue_comments_057153.json:
```json
{
    "body": "Replying to [comment:13 malb]:\n\n> * `NotImplementedError, \"Singular engine in Sage cannot handle matrix ordering yet.\"` should be replaced by `NotImplementedError(\"Matrix term orderings are not supported by the libSingular interface yet.\"` or something along those lines. I propose this change to make it clearer that Singular can indeed deal with Matrix term orderings and that it is us who cannot. \n\nI agree.\n\n> * `TypeError: Cannot use a matrix term order as a block.` shouldn't that be a `NotImplementedError`? \n\nI know Singular allow matrix term orderings in block order. But this feature is not one of the aims of the current patch. That could be included in a future patch that use Singular version.\n\n> * I thought the agreement was not to allow 'matrix(0,1,2,3)' but to use Singular's convention instead? It seems you are allowing at and using it internally.\n\nI did not agree then. :-) Anyway, I will change it to 'm(...)'",
    "created_at": "2010-06-04T01:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57153",
    "user": "klee"
}
```

Replying to [comment:13 malb]:

> * `NotImplementedError, "Singular engine in Sage cannot handle matrix ordering yet."` should be replaced by `NotImplementedError("Matrix term orderings are not supported by the libSingular interface yet."` or something along those lines. I propose this change to make it clearer that Singular can indeed deal with Matrix term orderings and that it is us who cannot. 

I agree.

> * `TypeError: Cannot use a matrix term order as a block.` shouldn't that be a `NotImplementedError`? 

I know Singular allow matrix term orderings in block order. But this feature is not one of the aims of the current patch. That could be included in a future patch that use Singular version.

> * I thought the agreement was not to allow 'matrix(0,1,2,3)' but to use Singular's convention instead? It seems you are allowing at and using it internally.

I did not agree then. :-) Anyway, I will change it to 'm(...)'



---

archive/issue_comments_057154.json:
```json
{
    "body": "Replying to [comment:14 malb]:\n\n> Oh, one more thing, isn't ` #!python TermOrder([0,1,2,3]) ` ambiguous since it could be interpreted as a list of weights? I'd vote to not to allow it for matrix term orders. \n\nOk.",
    "created_at": "2010-06-04T01:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57154",
    "user": "klee"
}
```

Replying to [comment:14 malb]:

> Oh, one more thing, isn't ` #!python TermOrder([0,1,2,3]) ` ambiguous since it could be interpreted as a list of weights? I'd vote to not to allow it for matrix term orders. 

Ok.



---

archive/issue_comments_057155.json:
```json
{
    "body": "Attachment [trac#6922.patch](tarball://root/attachments/some-uuid/ticket6922/trac#6922.patch) by klee created at 2010-06-04 01:35:55\n\nreplaced",
    "created_at": "2010-06-04T01:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57155",
    "user": "klee"
}
```

Attachment [trac#6922.patch](tarball://root/attachments/some-uuid/ticket6922/trac#6922.patch) by klee created at 2010-06-04 01:35:55

replaced



---

archive/issue_comments_057156.json:
```json
{
    "body": "The patch applies cleanly and doctests pass.\n\nI'm still not happy with the interface:\n\n\n```python\nsage: P.<a,b> = PolynomialRing(GF(32003),order=TermOrder(Matrix([1,2,0,3])))\nsage: P.term_order()\nm(1,2,0,3) term order\n```\n\n\nThis uses the non-standard \"m(...)\" representation which I would avoid. I'd be happy with either \"M()\" (Singular notation) or \"Matrix term ordering with matrix ...\" or so.\n\nAlso, the \"m()\" notation is allowed but shouldn't.\n\n\n```python\nsage: P.<a,b> = PolynomialRing(GF(32003),order='m(1,2,0,3)')\n```\n\n\nI understand that this is a typical paint-the-bike-shed scenario and in particular a question of choice. Still, I think we shouldn't invent more ad-hoc string notation when (a) there is an established notation and (b) we have a much nicer object oriented way of constructing term orderings.\n\nHowever, since this isn't really that big of a deal, I am okay with being overruled by some other referee who disagrees.\n\nPS: Apologies for taking so long to revisit this ticket.",
    "created_at": "2010-06-24T12:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57156",
    "user": "malb"
}
```

The patch applies cleanly and doctests pass.

I'm still not happy with the interface:


```python
sage: P.<a,b> = PolynomialRing(GF(32003),order=TermOrder(Matrix([1,2,0,3])))
sage: P.term_order()
m(1,2,0,3) term order
```


This uses the non-standard "m(...)" representation which I would avoid. I'd be happy with either "M()" (Singular notation) or "Matrix term ordering with matrix ..." or so.

Also, the "m()" notation is allowed but shouldn't.


```python
sage: P.<a,b> = PolynomialRing(GF(32003),order='m(1,2,0,3)')
```


I understand that this is a typical paint-the-bike-shed scenario and in particular a question of choice. Still, I think we shouldn't invent more ad-hoc string notation when (a) there is an established notation and (b) we have a much nicer object oriented way of constructing term orderings.

However, since this isn't really that big of a deal, I am okay with being overruled by some other referee who disagrees.

PS: Apologies for taking so long to revisit this ticket.



---

archive/issue_comments_057157.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-25T00:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57157",
    "user": "klee"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057158.json:
```json
{
    "body": "Replying to [comment:17 malb]:\n\nI prefer \"Matrix term ordering with matrix ...\".\n\nboth \"M(1,2,0,3)\" and \"m(1,2,0,3)\" is allowed, which is not bad. The situation is the same with other orderings like \"Lex\", which is converted to lower case internally. I don't mind that \"M(...)\" should be the official string representation of matrix orderings.\n\nI am working to make matrix ordering work with Singular version. I am not really confident whether the code is sound as it is based on a knowledge obtained by a reverse engineering of libSingular Sage interface. \n\nI will upload a revised patch soon, perhaps within a couple of hours. Then I wish you again to review the patch.",
    "created_at": "2010-06-25T00:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57158",
    "user": "klee"
}
```

Replying to [comment:17 malb]:

I prefer "Matrix term ordering with matrix ...".

both "M(1,2,0,3)" and "m(1,2,0,3)" is allowed, which is not bad. The situation is the same with other orderings like "Lex", which is converted to lower case internally. I don't mind that "M(...)" should be the official string representation of matrix orderings.

I am working to make matrix ordering work with Singular version. I am not really confident whether the code is sound as it is based on a knowledge obtained by a reverse engineering of libSingular Sage interface. 

I will upload a revised patch soon, perhaps within a couple of hours. Then I wish you again to review the patch.



---

archive/issue_comments_057159.json:
```json
{
    "body": "with singular version support",
    "created_at": "2010-06-25T04:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57159",
    "user": "klee"
}
```

with singular version support



---

archive/issue_comments_057160.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-25T04:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57160",
    "user": "klee"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057161.json:
```json
{
    "body": "Attachment [trac#6922.2.patch](tarball://root/attachments/some-uuid/ticket6922/trac#6922.2.patch) by klee created at 2010-06-25 04:58:21\n\nThe new patch supports also the Singular version.  Now \"M(...)\" is the official string representation of matrix  orderings.",
    "created_at": "2010-06-25T04:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57161",
    "user": "klee"
}
```

Attachment [trac#6922.2.patch](tarball://root/attachments/some-uuid/ticket6922/trac#6922.2.patch) by klee created at 2010-06-25 04:58:21

The new patch supports also the Singular version.  Now "M(...)" is the official string representation of matrix  orderings.



---

archive/issue_comments_057162.json:
```json
{
    "body": "Replying to [comment:18 klee]:\n> The situation is the same with other orderings like \"Lex\", which is converted to \n> lower case internally.\n\nGood point, I'm convinced.\n\n> I am working to make matrix ordering work with Singular version. I am not really \n> confident whether the code is sound as it is based on a knowledge obtained by a \n> reverse engineering of libSingular Sage interface. \n\nGreat, I'll take a look.",
    "created_at": "2010-06-25T07:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57162",
    "user": "malb"
}
```

Replying to [comment:18 klee]:
> The situation is the same with other orderings like "Lex", which is converted to 
> lower case internally.

Good point, I'm convinced.

> I am working to make matrix ordering work with Singular version. I am not really 
> confident whether the code is sound as it is based on a knowledge obtained by a 
> reverse engineering of libSingular Sage interface. 

Great, I'll take a look.



---

archive/issue_comments_057163.json:
```json
{
    "body": "Patch looks good (small issue see below), applies cleanly, doctests pass.\n\nSo, this stuff now works, very cool:\n\n\n```python\nsage: P = PolynomialRing(GF(127),2,'x',order=Matrix([1,2,0,3]))\nsage: P.term_order()\nMatrix term order with matrix\n[1 2]\n[0 3]\nsage: magma(P)\nPolynomial ring of rank 2 over GF(127)\nOrder: Weight [full]\nVariables: x0, x1\nsage: singular(P)\n//   characteristic : 127\n//   number of vars : 2\n//        block   1 : ordering M\n//                  : names    x0 x1\n//                  : weights   1  2\n//                  : weights   0  3\n//        block   2 : ordering C\n```\n\n\nI've attached a small referee patch which Kwankyu or someone else has to sign of. Kwankyu's patch gets a positive review modulo the issue in the referee patch.",
    "created_at": "2010-06-25T09:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57163",
    "user": "malb"
}
```

Patch looks good (small issue see below), applies cleanly, doctests pass.

So, this stuff now works, very cool:


```python
sage: P = PolynomialRing(GF(127),2,'x',order=Matrix([1,2,0,3]))
sage: P.term_order()
Matrix term order with matrix
[1 2]
[0 3]
sage: magma(P)
Polynomial ring of rank 2 over GF(127)
Order: Weight [full]
Variables: x0, x1
sage: singular(P)
//   characteristic : 127
//   number of vars : 2
//        block   1 : ordering M
//                  : names    x0 x1
//                  : weights   1  2
//                  : weights   0  3
//        block   2 : ordering C
```


I've attached a small referee patch which Kwankyu or someone else has to sign of. Kwankyu's patch gets a positive review modulo the issue in the referee patch.



---

archive/issue_comments_057164.json:
```json
{
    "body": "Attachment [trac_6922_referee.patch](tarball://root/attachments/some-uuid/ticket6922/trac_6922_referee.patch) by malb created at 2010-06-25 09:07:23\n\napply after klee's patch",
    "created_at": "2010-06-25T09:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57164",
    "user": "malb"
}
```

Attachment [trac_6922_referee.patch](tarball://root/attachments/some-uuid/ticket6922/trac_6922_referee.patch) by malb created at 2010-06-25 09:07:23

apply after klee's patch



---

archive/issue_comments_057165.json:
```json
{
    "body": "Attachment [trac#6922_final.patch](tarball://root/attachments/some-uuid/ticket6922/trac#6922_final.patch) by klee created at 2010-06-25 10:44:58\n\ncombined with referee's patch",
    "created_at": "2010-06-25T10:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57165",
    "user": "klee"
}
```

Attachment [trac#6922_final.patch](tarball://root/attachments/some-uuid/ticket6922/trac#6922_final.patch) by klee created at 2010-06-25 10:44:58

combined with referee's patch



---

archive/issue_comments_057166.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-25T10:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57166",
    "user": "klee"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057167.json:
```json
{
    "body": "Positive review for the referee's patch. Thank you!",
    "created_at": "2010-06-25T10:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57167",
    "user": "klee"
}
```

Positive review for the referee's patch. Thank you!



---

archive/issue_comments_057168.json:
```json
{
    "body": "I'm applying just `trac#6922_final.patch` to 4.5.2.alpha0.  Just let me know if I'm wrong.",
    "created_at": "2010-07-20T08:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57168",
    "user": "mpatel"
}
```

I'm applying just `trac#6922_final.patch` to 4.5.2.alpha0.  Just let me know if I'm wrong.



---

archive/issue_comments_057169.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6922",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6922#issuecomment-57169",
    "user": "mpatel"
}
```

Resolution: fixed
