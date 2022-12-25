# Issue 9085: random_element fails for a cartesian product of fields

archive/issues_009085.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @nthiery\n\nKeywords: random element cartesian product\n\nVictor Miller reports:\n\n```\nHere's something a bit odd:\n\nsage: F = GF(2)\nsage: A = CartesianProduct(F,F)\nsage: print A.random_element()\n\nThis gets a trace back and the message\n\nTypeError: You must specify the names of the variables \n```\n\n\nHere is what is happening (certainly a bug).  In the code which picks a random element from F, F is treated as a sequence and then\nsubscripted with a random subscript.  But (as you can verify)\nevaluating F[0] or F[1] raises an error, since the `__getitem__` method of a field is used to create polynomial rings (as in F['x']).\n\nThis does not happen when you just do F.random_element() since that\nhas an independent implementation.\n\nI think the fault lies in line 125 of /sage/misc/prandom.py in the\nfunction choice() which says\n\n```\nreturn _pyrand().choice(seq)\n```\n\nbut in your example \"seq\" is the field F.  It would work if that said list(seq), since\n\n```\n_pyrand().choice(F)\n```\n\nfails but\n\n```\n_pyrand().choice(list(F))\n```\n\nworks.  But it would be more efficient if that choice function tried\nto call a random_element() function on its  argument instead --\nimagine if the field was very large, it would be stupid to construct a list of its elements for each random choice. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9085\n\n",
    "created_at": "2010-05-29T11:24:12Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "random_element fails for a cartesian product of fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9085",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @aghitza

CC:  @nthiery

Keywords: random element cartesian product

Victor Miller reports:

```
Here's something a bit odd:

sage: F = GF(2)
sage: A = CartesianProduct(F,F)
sage: print A.random_element()

This gets a trace back and the message

TypeError: You must specify the names of the variables 
```


Here is what is happening (certainly a bug).  In the code which picks a random element from F, F is treated as a sequence and then
subscripted with a random subscript.  But (as you can verify)
evaluating F[0] or F[1] raises an error, since the `__getitem__` method of a field is used to create polynomial rings (as in F['x']).

This does not happen when you just do F.random_element() since that
has an independent implementation.

I think the fault lies in line 125 of /sage/misc/prandom.py in the
function choice() which says

```
return _pyrand().choice(seq)
```

but in your example "seq" is the field F.  It would work if that said list(seq), since

```
_pyrand().choice(F)
```

fails but

```
_pyrand().choice(list(F))
```

works.  But it would be more efficient if that choice function tried
to call a random_element() function on its  argument instead --
imagine if the field was very large, it would be stupid to construct a list of its elements for each random choice. 


Issue created by migration from https://trac.sagemath.org/ticket/9085





---

archive/issue_comments_084225.json:
```json
{
    "body": "Suggestion:  in the {{{__item__}} method for rings, which constructs a polynomial ring (so that mathematicians can be happy writing things like ZZ['x']), it would be possible to test if ring R is finite and the argument was a non-negative integer n, to return the n'th element of list(R).",
    "created_at": "2010-05-29T17:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9085#issuecomment-84225",
    "user": "https://github.com/JohnCremona"
}
```

Suggestion:  in the {{{__item__}} method for rings, which constructs a polynomial ring (so that mathematicians can be happy writing things like ZZ['x']), it would be possible to test if ring R is finite and the argument was a non-negative integer n, to return the n'th element of list(R).



---

archive/issue_comments_084226.json:
```json
{
    "body": "This works now.\n\n```\nsage: F = GF(1951)\nsage: A = F.cartesian_product(F)\nsage: A.random_element()\n(1405, 126)\nsage: A.random_element()\n(1151, 1050)\n```\n",
    "created_at": "2016-02-05T12:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9085#issuecomment-84226",
    "user": "https://github.com/fchapoton"
}
```

This works now.

```
sage: F = GF(1951)
sage: A = F.cartesian_product(F)
sage: A.random_element()
(1405, 126)
sage: A.random_element()
(1151, 1050)
```




---

archive/issue_comments_084227.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-02-05T12:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9085#issuecomment-84227",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084228.json:
```json
{
    "body": "And, thanks to #18411, also with the original syntax:\n\n```\n    sage: F = GF(2)\n    sage: A = CartesianProduct(F,F)\n    sage: print A.random_element()\n    (1,0)\n```\n\n\nThanks Fr\u00e9d\u00e9ric for spotting this outdated ticket.",
    "created_at": "2016-02-05T13:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9085#issuecomment-84228",
    "user": "https://github.com/nthiery"
}
```

And, thanks to #18411, also with the original syntax:

```
    sage: F = GF(2)
    sage: A = CartesianProduct(F,F)
    sage: print A.random_element()
    (1,0)
```


Thanks Frédéric for spotting this outdated ticket.



---

archive/issue_comments_084229.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-05T13:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9085#issuecomment-84229",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084230.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2016-02-23T22:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9085#issuecomment-84230",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid



---

archive/issue_events_009242.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-02-23T22:53:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9085",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9085#event-9242"
}
```
