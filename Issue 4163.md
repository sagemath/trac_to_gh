# Issue 4163: tut -- improve factorial / valuation example

archive/issues_004163.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @JohnCremona\n\n\n```\nThat's a good point.\n\n2008/9/20 pong <wypong00>:\n>\n> This is not a bug report. But I'm not sure where to post a suggestion.\n>\n> In the SAGE tutorial, http://www.sagemath.org/doc/tut/node27.html\n>\n> there is an example:\n>\n> sage: c = factorial(25); c\n> 15511210043330985984000000\n> sage: [valuation(c,p) for p in prime_range(2,23)]\n> [22, 10, 6, 3, 2, 1, 1, 1]\n>\n> Since prime_range(2,23) does not include 23 itself, maybe it's better\n> to change it to prime_range(2,25). In that case, the product of primes\n> to the corresponding powers will actually give the factorial of 25.\n\nI would also include\nsage: c.factor()\n2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23\n(which would be helpful to people who might know know this meaning of\n\"valuation\", standard in number theory), and even perhaps\nsage: list(c.factor())\n[(2, 22), (3, 10), (5, 6), (7, 3), (11, 2), (13, 1), (17, 1), (19, 1), (23, 1)]\n\nJohn Cremona\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4163\n\n",
    "created_at": "2008-09-21T14:00:40Z",
    "labels": [
        "component: documentation",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "tut -- improve factorial / valuation example",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4163",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

CC:  @JohnCremona


```
That's a good point.

2008/9/20 pong <wypong00>:
>
> This is not a bug report. But I'm not sure where to post a suggestion.
>
> In the SAGE tutorial, http://www.sagemath.org/doc/tut/node27.html
>
> there is an example:
>
> sage: c = factorial(25); c
> 15511210043330985984000000
> sage: [valuation(c,p) for p in prime_range(2,23)]
> [22, 10, 6, 3, 2, 1, 1, 1]
>
> Since prime_range(2,23) does not include 23 itself, maybe it's better
> to change it to prime_range(2,25). In that case, the product of primes
> to the corresponding powers will actually give the factorial of 25.

I would also include
sage: c.factor()
2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
(which would be helpful to people who might know know this meaning of
"valuation", standard in number theory), and even perhaps
sage: list(c.factor())
[(2, 22), (3, 10), (5, 6), (7, 3), (11, 2), (13, 1), (17, 1), (19, 1), (23, 1)]

John Cremona
```


Issue created by migration from https://trac.sagemath.org/ticket/4163





---

archive/issue_comments_030150.json:
```json
{
    "body": "Attachment [4163-tut_factorial.patch](tarball://root/attachments/some-uuid/ticket4163/4163-tut_factorial.patch) by @aghitza created at 2008-09-23 08:06:35\n\ndoc patch",
    "created_at": "2008-09-23T08:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4163#issuecomment-30150",
    "user": "https://github.com/aghitza"
}
```

Attachment [4163-tut_factorial.patch](tarball://root/attachments/some-uuid/ticket4163/4163-tut_factorial.patch) by @aghitza created at 2008-09-23 08:06:35

doc patch



---

archive/issue_comments_030151.json:
```json
{
    "body": "see the attached doc patch (made on 3.1.3.alpha0).",
    "created_at": "2008-09-23T08:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4163#issuecomment-30151",
    "user": "https://github.com/aghitza"
}
```

see the attached doc patch (made on 3.1.3.alpha0).



---

archive/issue_comments_030152.json:
```json
{
    "body": "Looks good to me. You did not add c.factor(), so I am not sure what to do in that regard.\n\nJohn: Do you have a preference here?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T08:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4163#issuecomment-30152",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. You did not add c.factor(), so I am not sure what to do in that regard.

John: Do you have a preference here?

Cheers,

Michael



---

archive/issue_comments_030153.json:
```json
{
    "body": "i thought that it would be preferrable not to clutter the example too much, but i don't have strong feelings about this.  i can easily add that in if people think it's a good idea.",
    "created_at": "2008-09-23T08:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4163#issuecomment-30153",
    "user": "https://github.com/aghitza"
}
```

i thought that it would be preferrable not to clutter the example too much, but i don't have strong feelings about this.  i can easily add that in if people think it's a good idea.



---

archive/issue_comments_030154.json:
```json
{
    "body": "Replying to [comment:3 AlexGhitza]:\n> i thought that it would be preferrable not to clutter the example too much, but i don't have strong feelings about this.  i can easily add that in if people think it's a good idea.\n\nI'm happy with it the way it is.  John",
    "created_at": "2008-09-23T08:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4163#issuecomment-30154",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 AlexGhitza]:
> i thought that it would be preferrable not to clutter the example too much, but i don't have strong feelings about this.  i can easily add that in if people think it's a good idea.

I'm happy with it the way it is.  John



---

archive/issue_comments_030155.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T09:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4163#issuecomment-30155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_030156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T09:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4163#issuecomment-30156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004401.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-23T09:41:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4163",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4163#event-4401"
}
```
