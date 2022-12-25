# Issue 577: add MPolynomialRing.long_repr method

archive/issues_000577.json:
```json
{
    "body": "Assignee: somebody\n\nIf a multivariate polynomial ring is structured via a block or product ordering and has lots and lots of variables printing it normally looks messy quickly. The proposed patch (attached) adds a method long_repr with provides a more structured view for those rings, e.g.\n\n\n```\nPolynomial Ring\n  Base Ring : Finite Field in a of size 2^4\n       Size : 52 Variables\n   Block  0 : Ordering : degrevlex\n              Names    : k300, k301, k302, k303, x300, x301, x302, x303, w300, w301, w302, w303, s200, s201, s202, s203\n   Block  1 : Ordering : degrevlex\n              Names    : k200, k201, k202, k203, x200, x201, x202, x203, w200, w201, w202, w203, s100, s101, s102, s103\n   Block  2 : Ordering : degrevlex\n              Names    : k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003\n   Block  3 : Ordering : degrevlex\n              Names    : k000, k001, k002, k003\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/577\n\n",
    "created_at": "2007-09-03T15:03:36Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "add MPolynomialRing.long_repr method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/577",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

If a multivariate polynomial ring is structured via a block or product ordering and has lots and lots of variables printing it normally looks messy quickly. The proposed patch (attached) adds a method long_repr with provides a more structured view for those rings, e.g.


```
Polynomial Ring
  Base Ring : Finite Field in a of size 2^4
       Size : 52 Variables
   Block  0 : Ordering : degrevlex
              Names    : k300, k301, k302, k303, x300, x301, x302, x303, w300, w301, w302, w303, s200, s201, s202, s203
   Block  1 : Ordering : degrevlex
              Names    : k200, k201, k202, k203, x200, x201, x202, x203, w200, w201, w202, w203, s100, s101, s102, s103
   Block  2 : Ordering : degrevlex
              Names    : k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003
   Block  3 : Ordering : degrevlex
              Names    : k000, k001, k002, k003
```


Issue created by migration from https://trac.sagemath.org/ticket/577





---

archive/issue_comments_002981.json:
```json
{
    "body": "Attachment [5853.patch](tarball://root/attachments/some-uuid/ticket577/5853.patch) by mabshoff created at 2007-09-11 19:11:53",
    "created_at": "2007-09-11T19:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/577#issuecomment-2981",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [5853.patch](tarball://root/attachments/some-uuid/ticket577/5853.patch) by mabshoff created at 2007-09-11 19:11:53



---

archive/issue_comments_002982.json:
```json
{
    "body": "Let's see if I can sneak this in 2.8.4.3",
    "created_at": "2007-09-15T13:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/577#issuecomment-2982",
    "user": "https://github.com/malb"
}
```

Let's see if I can sneak this in 2.8.4.3



---

archive/issue_comments_002983.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T02:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/577",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/577#issuecomment-2983",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000631.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-21T02:09:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/577",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/577#event-631"
}
```
