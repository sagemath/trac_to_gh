# Issue 8196: bad documentation output in tty mode

archive/issues_008196.json:
```json
{
    "body": "Assignee: mvngu\n\n\n```\nsage: a=mod(3,15)\nsage: a.is_square?\n...\n            ALGORITHM: Calculate the Jacobi symbol\n            `(mathtt{self}/p)` at each prime `p`\n            dividing `n`. It must be 1 or 0 for each prime, and if it\n            is 0 mod `p`, where `p^k || n`, then\n            `ord_p(mathtt{self})` must be even or greater than\n```\n\nClearly the math formulae are not displayed correctly in tty mode.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8196\n\n",
    "created_at": "2010-02-05T20:14:00Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bad documentation output in tty mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8196",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mvngu


```
sage: a=mod(3,15)
sage: a.is_square?
...
            ALGORITHM: Calculate the Jacobi symbol
            `(mathtt{self}/p)` at each prime `p`
            dividing `n`. It must be 1 or 0 for each prime, and if it
            is 0 mod `p`, where `p^k || n`, then
            `ord_p(mathtt{self})` must be even or greater than
```

Clearly the math formulae are not displayed correctly in tty mode.

Issue created by migration from https://trac.sagemath.org/ticket/8196





---

archive/issue_comments_072164.json:
```json
{
    "body": "> Clearly the math formulae are not displayed correctly in tty mode.\n\nHow would you expect them to be displayed, given that it's tty mode?",
    "created_at": "2010-02-05T20:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8196#issuecomment-72164",
    "user": "https://github.com/jhpalmieri"
}
```

> Clearly the math formulae are not displayed correctly in tty mode.

How would you expect them to be displayed, given that it's tty mode?



---

archive/issue_comments_072165.json:
```json
{
    "body": "> How would you expect them to be displayed, given that it's tty mode? \n\nthe \"mathtt{...}\" should not appear, thus we should get something like:\n\n```\n            ALGORITHM: Calculate the Jacobi symbol\n            `(self/p)` at each prime `p`\n            dividing `n`. It must be 1 or 0 for each prime, and if it\n            is 0 mod `p`, where `p^k || n`, then\n            `ord_p(self)` must be even or greater than\n```\n",
    "created_at": "2010-02-07T21:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8196#issuecomment-72165",
    "user": "https://github.com/zimmermann6"
}
```

> How would you expect them to be displayed, given that it's tty mode? 

the "mathtt{...}" should not appear, thus we should get something like:

```
            ALGORITHM: Calculate the Jacobi symbol
            `(self/p)` at each prime `p`
            dividing `n`. It must be 1 or 0 for each prime, and if it
            is 0 mod `p`, where `p^k || n`, then
            `ord_p(self)` must be even or greater than
```




---

archive/issue_comments_072166.json:
```json
{
    "body": "Replying to [comment:2 zimmerma]:\n> the \"mathtt{...}\" should not appear\n\nThe patch at #8209 does this, but really only because mathtt is broken everywhere: broken in notebook documentation and in the reference manual, so might as well fix it from the command line, too.  I really don't think we want to write what would essentially be a LaTeX --> text converter, so there are limits to how good the help strings will look from the command line.\n\nI suggest we close this, since #8209 takes care of the specific issue here.",
    "created_at": "2010-02-07T21:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8196#issuecomment-72166",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:2 zimmerma]:
> the "mathtt{...}" should not appear

The patch at #8209 does this, but really only because mathtt is broken everywhere: broken in notebook documentation and in the reference manual, so might as well fix it from the command line, too.  I really don't think we want to write what would essentially be a LaTeX --> text converter, so there are limits to how good the help strings will look from the command line.

I suggest we close this, since #8209 takes care of the specific issue here.



---

archive/issue_comments_072167.json:
```json
{
    "body": "I confirm #8209 fixes that issue, thus ok to close #8196.",
    "created_at": "2010-02-07T21:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8196#issuecomment-72167",
    "user": "https://github.com/zimmermann6"
}
```

I confirm #8209 fixes that issue, thus ok to close #8196.



---

archive/issue_comments_072168.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-07T22:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8196#issuecomment-72168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: wontfix



---

archive/issue_events_008399.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-07T22:43:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8196",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8196#event-8399"
}
```
