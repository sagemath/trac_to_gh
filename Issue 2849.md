# Issue 2849: Bug in elliptic curve cardinality for j=0 in char. 3

archive/issues_002849.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nDustin Moody reported\n\n```\n    While working on some things, I found a bug in SAGE:\n\n sage:k.<a>=GF(3^5)\n\n sage:E=EllipticCurve(k,[-1,-1])\n\n sage:E.trace_of_frobenius()\n 0\n\n This isn't correct.  It should be -27.  I also discovered you can get\naround it.\n\n sage:E.cardinality_exhaustive()\n 271\n\n sage:E.trace_of_frobenius()\n -27\n\n Somehow, doing .cardinality_exhaustive() fixes the bug.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2849\n\n",
    "created_at": "2008-04-07T20:35:32Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "title": "Bug in elliptic curve cardinality for j=0 in char. 3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2849",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

Dustin Moody reported

```
    While working on some things, I found a bug in SAGE:

 sage:k.<a>=GF(3^5)

 sage:E=EllipticCurve(k,[-1,-1])

 sage:E.trace_of_frobenius()
 0

 This isn't correct.  It should be -27.  I also discovered you can get
around it.

 sage:E.cardinality_exhaustive()
 271

 sage:E.trace_of_frobenius()
 -27

 Somehow, doing .cardinality_exhaustive() fixes the bug.
```


Issue created by migration from https://trac.sagemath.org/ticket/2849





---

archive/issue_comments_019509.json:
```json
{
    "body": "Attachment [trac2849.patch](tarball://root/attachments/some-uuid/ticket2849/trac2849.patch) by @JohnCremona created at 2008-04-07 20:49:46",
    "created_at": "2008-04-07T20:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2849#issuecomment-19509",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac2849.patch](tarball://root/attachments/some-uuid/ticket2849/trac2849.patch) by @JohnCremona created at 2008-04-07 20:49:46



---

archive/issue_comments_019510.json:
```json
{
    "body": "Here's the patch:   A case where q=3 (mod 4) only worked for p>3 and was being used for p=3, odd degree.  Should be a trivial review.\n\nNote that I am in the middle of implementing vastly better support for the cases j=0 and j=1728, which are not so straightforward in characterisitcs 2 and 3 but I am getting there!",
    "created_at": "2008-04-07T20:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2849#issuecomment-19510",
    "user": "https://github.com/JohnCremona"
}
```

Here's the patch:   A case where q=3 (mod 4) only worked for p>3 and was being used for p=3, odd degree.  Should be a trivial review.

Note that I am in the middle of implementing vastly better support for the cases j=0 and j=1728, which are not so straightforward in characterisitcs 2 and 3 but I am getting there!



---

archive/issue_comments_019511.json:
```json
{
    "body": "apply after trac2849.patch",
    "created_at": "2008-04-07T21:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2849#issuecomment-19511",
    "user": "https://github.com/aghitza"
}
```

apply after trac2849.patch



---

archive/issue_comments_019512.json:
```json
{
    "body": "Attachment [trac2849_doctest.patch](tarball://root/attachments/some-uuid/ticket2849/trac2849_doctest.patch) by @aghitza created at 2008-04-07 22:00:56\n\nLooks fine and it fixes the issue.  I've added a mini-patch that puts in a doctest demonstrating the fixed status.\n\nApply both patches.",
    "created_at": "2008-04-07T22:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2849#issuecomment-19512",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac2849_doctest.patch](tarball://root/attachments/some-uuid/ticket2849/trac2849_doctest.patch) by @aghitza created at 2008-04-07 22:00:56

Looks fine and it fixes the issue.  I've added a mini-patch that puts in a doctest demonstrating the fixed status.

Apply both patches.



---

archive/issue_comments_019513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T22:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2849#issuecomment-19513",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019514.json:
```json
{
    "body": "Merged trac2849.patch and trac2849_doctest.patch in Sage 3.0.alpha3",
    "created_at": "2008-04-07T22:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2849#issuecomment-19514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac2849.patch and trac2849_doctest.patch in Sage 3.0.alpha3



---

archive/issue_events_006529.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T22:20:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2849#event-6529"
}
```



---

archive/issue_comments_019515.json:
```json
{
    "body": "Replying to [comment:2 AlexGhitza]:\n> Looks fine and it fixes the issue.  I've added a mini-patch that puts in a doctest demonstrating the fixed status.\n> \n\n\nThanks, Alex -- I should have done that but only remembered after uploading the patch.\n\n> Apply both patches.",
    "created_at": "2008-04-08T07:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2849#issuecomment-19515",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 AlexGhitza]:
> Looks fine and it fixes the issue.  I've added a mini-patch that puts in a doctest demonstrating the fixed status.
> 


Thanks, Alex -- I should have done that but only remembered after uploading the patch.

> Apply both patches.
