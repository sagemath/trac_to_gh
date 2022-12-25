# Issue 5126: error coercing stacked polynomial rings to relative number fields

archive/issues_005126.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @roed314\n\nKeywords: polynomial ring coercion relative number field\n\nFrom David Roe, reviewing #1367:\n\n\n```\nI'm not completely convinced that the following example is the behavior we want:\n\nsage: K.<a> = NumberField?(ZZx?.05 + 2, 'a') sage: L.<b> = K.extension(ZZx?.02 + 3*a, 'b') sage: u = QQu?.gen() sage: t = u.parent()t?.gen()\n\nsage: L(u*5) 5*b\n\nI guess if we're going to convert at all this makes the most sense, but I want to think about it a bit more. I'm even less convinced of the following:\n\nsage: W.<w> = t.parent()[] sage: L(w*5) 5*b sage: L(W(t)) 5*a sage: L(W(u)) TypeError?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5126\n\n",
    "created_at": "2009-01-29T05:07:46Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "error coercing stacked polynomial rings to relative number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5126",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @roed314

Keywords: polynomial ring coercion relative number field

From David Roe, reviewing #1367:


```
I'm not completely convinced that the following example is the behavior we want:

sage: K.<a> = NumberField?(ZZx?.05 + 2, 'a') sage: L.<b> = K.extension(ZZx?.02 + 3*a, 'b') sage: u = QQu?.gen() sage: t = u.parent()t?.gen()

sage: L(u*5) 5*b

I guess if we're going to convert at all this makes the most sense, but I want to think about it a bit more. I'm even less convinced of the following:

sage: W.<w> = t.parent()[] sage: L(w*5) 5*b sage: L(W(t)) 5*a sage: L(W(u)) TypeError?
```


Issue created by migration from https://trac.sagemath.org/ticket/5126





---

archive/issue_comments_039102.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5126#issuecomment-39102",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_039103.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5126#issuecomment-39103",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.
