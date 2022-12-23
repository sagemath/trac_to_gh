# Issue 3494: var --> name

archive/issues_003494.json:
```json
{
    "body": "Assignee: craigcitro\n\nLots of things that are matrix-related in `sage` use `var`, whereas `name` would often be more appropriate. Someone should fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3494\n\n",
    "created_at": "2008-06-23T18:49:35Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "var --> name",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3494",
    "user": "craigcitro"
}
```
Assignee: craigcitro

Lots of things that are matrix-related in `sage` use `var`, whereas `name` would often be more appropriate. Someone should fix this.

Issue created by migration from https://trac.sagemath.org/ticket/3494





---

archive/issue_comments_024605.json:
```json
{
    "body": "He's talking about the name of the keyword arguments.\n\n\n```\n[23:39] <jason--> craigcitro: 3494 is awfully vague\n[23:39] <craigcitro> hah, true\n[23:39] <craigcitro> but it's also sad that it's not uniform\n[23:39] <craigcitro> the number of times i have to try three different things to find the right argument is sad\n[23:40] <jason--> Can you at least point out one instance?\n[23:41] <craigcitro> charpoly, minpoly, eigenspaces\n[23:41] <jason--> mabshoff: what is the status on 3435?\n[23:41] <craigcitro> whereas, say, PolynomialRing uses name\n[23:41] <craigcitro> seems like it should just uniformly be name.\n```\n",
    "created_at": "2008-11-14T05:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3494#issuecomment-24605",
    "user": "jason"
}
```

He's talking about the name of the keyword arguments.


```
[23:39] <jason--> craigcitro: 3494 is awfully vague
[23:39] <craigcitro> hah, true
[23:39] <craigcitro> but it's also sad that it's not uniform
[23:39] <craigcitro> the number of times i have to try three different things to find the right argument is sad
[23:40] <jason--> Can you at least point out one instance?
[23:41] <craigcitro> charpoly, minpoly, eigenspaces
[23:41] <jason--> mabshoff: what is the status on 3435?
[23:41] <craigcitro> whereas, say, PolynomialRing uses name
[23:41] <craigcitro> seems like it should just uniformly be name.
```




---

archive/issue_comments_024606.json:
```json
{
    "body": "Outdated, too late to change it.",
    "created_at": "2021-11-16T05:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3494#issuecomment-24606",
    "user": "mkoeppe"
}
```

Outdated, too late to change it.



---

archive/issue_comments_024607.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-11-16T05:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3494#issuecomment-24607",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024608.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-11-16T08:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3494#issuecomment-24608",
    "user": "klee"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024609.json:
```json
{
    "body": "I don't like the \"too late\" argument. But since we can do\n\n```\nsage: m = matrix(2,[1,2,3,4])\nsage: var('y')\ny\nsage: m.charpoly(y)\ny^2 - 5*y - 2\n```\n\nit is not clear if `name` is preferable than `var`. So let's close this ticket until we have a fresh discussion, which is too late perhaps...",
    "created_at": "2021-11-16T08:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3494#issuecomment-24609",
    "user": "klee"
}
```

I don't like the "too late" argument. But since we can do

```
sage: m = matrix(2,[1,2,3,4])
sage: var('y')
y
sage: m.charpoly(y)
y^2 - 5*y - 2
```

it is not clear if `name` is preferable than `var`. So let's close this ticket until we have a fresh discussion, which is too late perhaps...



---

archive/issue_comments_024610.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-11-20T23:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3494",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3494#issuecomment-24610",
    "user": "mkoeppe"
}
```

Resolution: invalid
