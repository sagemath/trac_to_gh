# Issue 8766: document the _iadd_ and _imul_ special integer.pyx methods, which mutate self

archive/issues_008766.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @tscrim\n\nI looked in integer.pyx at the two methods _iadd_ and _imul_, which both mutate self, e.g., allow for:\n\n```\nsage: a = 2010\nsage: a._imul_(19)\nsage: a\n38190\n```\n\nI expected to find a bug exciting docstring about how these methods are unsafe, etc.   Instead, there is *NOTHING* -- not even a doctest or docstring at all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8766\n\n",
    "created_at": "2010-04-26T13:47:27Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "document the _iadd_ and _imul_ special integer.pyx methods, which mutate self",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8766",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  @tscrim

I looked in integer.pyx at the two methods _iadd_ and _imul_, which both mutate self, e.g., allow for:

```
sage: a = 2010
sage: a._imul_(19)
sage: a
38190
```

I expected to find a bug exciting docstring about how these methods are unsafe, etc.   Instead, there is *NOTHING* -- not even a doctest or docstring at all.

Issue created by migration from https://trac.sagemath.org/ticket/8766





---

archive/issue_comments_080094.json:
```json
{
    "body": "\n```\n> This is odd. From their names one would expect them to be used in __imul__\n> and __iadd__ somewhere in the hierarchy, just like _repr_ is used in\n> __repr__, so that they will be used for:\n>\n> sage: a = 1\n> sage: a*=5\n>\n> as documented here: http://docs.python.org/reference/datamodel.html.\n> However, this is not the case. It may be a bug (or yet to be implemented\n> feature).\n\nThat is not a bug -- it is done on purpose.  The reason is because integers are meant to be *immutable*, since they have a hash method.   If _imul_ were used by __imul__, then people would be mutating integers left and right by accident, and vast amounts of code would consequently have subtle bugs all over the place.   \n\nThere might have been a time (maybe a few weeks in 2006) when __imul__ did indeed call _imul_ in Sage, so the name might be a historical remnant. \n\nPersonally, I think the best thing would be:\n\n  (1) Rename _imul_ and _iadd_ to something like _unsafe_inplace_mul_, _unsafe_inplace_add_\n\n  (2) Document them. \n\nWilliam\n```\n",
    "created_at": "2010-05-05T12:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8766#issuecomment-80094",
    "user": "https://github.com/williamstein"
}
```


```
> This is odd. From their names one would expect them to be used in __imul__
> and __iadd__ somewhere in the hierarchy, just like _repr_ is used in
> __repr__, so that they will be used for:
>
> sage: a = 1
> sage: a*=5
>
> as documented here: http://docs.python.org/reference/datamodel.html.
> However, this is not the case. It may be a bug (or yet to be implemented
> feature).

That is not a bug -- it is done on purpose.  The reason is because integers are meant to be *immutable*, since they have a hash method.   If _imul_ were used by __imul__, then people would be mutating integers left and right by accident, and vast amounts of code would consequently have subtle bugs all over the place.   

There might have been a time (maybe a few weeks in 2006) when __imul__ did indeed call _imul_ in Sage, so the name might be a historical remnant. 

Personally, I think the best thing would be:

  (1) Rename _imul_ and _iadd_ to something like _unsafe_inplace_mul_, _unsafe_inplace_add_

  (2) Document them. 

William
```




---

archive/issue_comments_080095.json:
```json
{
    "body": "> This is odd. From their names one would expect them to be used in __imul__\n> and __iadd__ somewhere in the hierarchy, just like _repr_ is used in\n> __repr__, so that they will be used for:\n>\n> sage: a = 1\n> sage: a*=5\n>\n> as documented here: http://docs.python.org/reference/datamodel.html.\n> However, this is not the case. It may be a bug (or yet to be implemented\n> feature).\n\nThat is not a bug -- it is done on purpose.  The reason is because integers are meant to be *immutable*, since they have a hash method.   If _imul_ were used by __imul__, then people would be mutating integers left and right by accident, and vast amounts of code would consequently have subtle bugs all over the place.   \n\nThere might have been a time (maybe a few weeks in 2006) when __imul__ did indeed call _imul_ in Sage, so the name might be a historical remnant. \n\nPersonally, I think the best thing would be:\n\n  (1) Rename _imul_ and _iadd_ to something like _unsafe_inplace_mul_, _unsafe_inplace_add_\n\n  (2) Document them. \n\nWilliam",
    "created_at": "2010-05-05T12:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8766#issuecomment-80095",
    "user": "https://github.com/williamstein"
}
```

> This is odd. From their names one would expect them to be used in __imul__
> and __iadd__ somewhere in the hierarchy, just like _repr_ is used in
> __repr__, so that they will be used for:
>
> sage: a = 1
> sage: a*=5
>
> as documented here: http://docs.python.org/reference/datamodel.html.
> However, this is not the case. It may be a bug (or yet to be implemented
> feature).

That is not a bug -- it is done on purpose.  The reason is because integers are meant to be *immutable*, since they have a hash method.   If _imul_ were used by __imul__, then people would be mutating integers left and right by accident, and vast amounts of code would consequently have subtle bugs all over the place.   

There might have been a time (maybe a few weeks in 2006) when __imul__ did indeed call _imul_ in Sage, so the name might be a historical remnant. 

Personally, I think the best thing would be:

  (1) Rename _imul_ and _iadd_ to something like _unsafe_inplace_mul_, _unsafe_inplace_add_

  (2) Document them. 

William



---

archive/issue_comments_080096.json:
```json
{
    "body": "Outdated, these methods no longer exist",
    "created_at": "2021-09-10T06:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8766#issuecomment-80096",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, these methods no longer exist



---

archive/issue_comments_080097.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-09-10T06:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8766#issuecomment-80097",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080098.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-09-10T06:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8766#issuecomment-80098",
    "user": "https://github.com/yyyyx4"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080099.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-09-10T17:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8766#issuecomment-80099",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
