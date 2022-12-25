# Issue 3805: sage gets basic arithmetic with sqrt(3) wrong

archive/issues_003805.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n\n```\nsage: t1 = (sqrt(3)-3)*(sqrt(3)+1)/6;\nsage: tt1 = -1/sqrt(3);\nsage: t2 = sqrt(3)/6;\nsage: tt1 == t1\n-1/sqrt(3) == (sqrt(3) - 3)*(sqrt(3) + 1)/6\nsage: bool(tt1 == t1)\nTrue\nsage: float(expand(t1+t2))\n-0.43301270189221941\nsage: float(expand(tt1+t2))\n-0.28867513459481292\n```\n\nBut it seems that this does not happen in a clean maxima session directly:\n\n```\nsage: !maxima\nMaxima 5.13.0 http://maxima.sourceforge.net\nUsing Lisp CLISP 2.46 (2008-07-02)\nDistributed under the GNU Public License. See the file COPYING.\nDedicated to the memory of William Schelter.\nThis is a development version of Maxima. The function bug_report()\nprovides bug reporting information.\n(%i1) t1 : (sqrt(3)-3)*(sqrt(3)+1)/6;\n                          (sqrt(3) - 3) (sqrt(3) + 1)\n(%o1)                     ---------------------------\n                                       6\n(%i2) tt1 : -1/sqrt(3);\n                                        1\n(%o2)                              - -------\n                                     sqrt(3)\n(%i3) t2 : sqrt(3)/6;\n                                     - 1/2\n                                    3\n(%o3)                               ------\n                                      2\n(%i4) tt1, numer;\n(%o4)                         - .5773502691896258\n(%i5) t1, numer;\n(%o5)                         - .5773502691896258\n(%i6) expand(t1+t2), numer;\n(%o6)                         - .2886751345948129\n(%i7) expand(tt1+t2), numer;\n(%o7)                         - .2886751345948129\n```\n\n\nSo I'm not sure what is going wrong, but it need not be a bug in Maxima.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3805\n\n",
    "created_at": "2008-08-11T16:51:43Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "sage gets basic arithmetic with sqrt(3) wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3805",
    "user": "https://github.com/williamstein"
}
```
Assignee: @garyfurnish


```
sage: t1 = (sqrt(3)-3)*(sqrt(3)+1)/6;
sage: tt1 = -1/sqrt(3);
sage: t2 = sqrt(3)/6;
sage: tt1 == t1
-1/sqrt(3) == (sqrt(3) - 3)*(sqrt(3) + 1)/6
sage: bool(tt1 == t1)
True
sage: float(expand(t1+t2))
-0.43301270189221941
sage: float(expand(tt1+t2))
-0.28867513459481292
```

But it seems that this does not happen in a clean maxima session directly:

```
sage: !maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.46 (2008-07-02)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) t1 : (sqrt(3)-3)*(sqrt(3)+1)/6;
                          (sqrt(3) - 3) (sqrt(3) + 1)
(%o1)                     ---------------------------
                                       6
(%i2) tt1 : -1/sqrt(3);
                                        1
(%o2)                              - -------
                                     sqrt(3)
(%i3) t2 : sqrt(3)/6;
                                     - 1/2
                                    3
(%o3)                               ------
                                      2
(%i4) tt1, numer;
(%o4)                         - .5773502691896258
(%i5) t1, numer;
(%o5)                         - .5773502691896258
(%i6) expand(t1+t2), numer;
(%o6)                         - .2886751345948129
(%i7) expand(tt1+t2), numer;
(%o7)                         - .2886751345948129
```


So I'm not sure what is going wrong, but it need not be a bug in Maxima.

Issue created by migration from https://trac.sagemath.org/ticket/3805





---

archive/issue_comments_026979.json:
```json
{
    "body": "This works for me.\n\n\n```\nsage: t1 = (sqrt(3)-3)*(sqrt(3)+1)/6;\nsage: tt1 = -1/sqrt(3);\nsage: t2 = sqrt(3)/6;\nsage: tt1 == t1\n-1/sqrt(3) == (sqrt(3) - 3)*(sqrt(3) + 1)/6\n\n# bool is only trustworthy on symbolic expressions when it returns True, right?\nsage: bool(tt1 == t1) \nTrue\n\nsage: float(expand(t1 + t2))\n-0.28867513459481292\n\nsage: float(expand(tt1 + t2))\n-0.28867513459481292\n\n```\n",
    "created_at": "2008-08-31T22:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26979",
    "user": "https://github.com/jicama"
}
```

This works for me.


```
sage: t1 = (sqrt(3)-3)*(sqrt(3)+1)/6;
sage: tt1 = -1/sqrt(3);
sage: t2 = sqrt(3)/6;
sage: tt1 == t1
-1/sqrt(3) == (sqrt(3) - 3)*(sqrt(3) + 1)/6

# bool is only trustworthy on symbolic expressions when it returns True, right?
sage: bool(tt1 == t1) 
True

sage: float(expand(t1 + t2))
-0.28867513459481292

sage: float(expand(tt1 + t2))
-0.28867513459481292

```




---

archive/issue_comments_026980.json:
```json
{
    "body": "Attachment [expand.patch](tarball://root/attachments/some-uuid/ticket3805/expand.patch) by @jicama created at 2008-08-31 22:55:00",
    "created_at": "2008-08-31T22:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26980",
    "user": "https://github.com/jicama"
}
```

Attachment [expand.patch](tarball://root/attachments/some-uuid/ticket3805/expand.patch) by @jicama created at 2008-08-31 22:55:00



---

archive/issue_comments_026981.json:
```json
{
    "body": "The patch adds a doctest that shows this functionality working.",
    "created_at": "2008-08-31T22:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26981",
    "user": "https://github.com/jicama"
}
```

The patch adds a doctest that shows this functionality working.



---

archive/issue_comments_026982.json:
```json
{
    "body": "The is an updated patcj of jwmerrill's patch with the numerical noise accounted for",
    "created_at": "2008-09-01T01:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The is an updated patcj of jwmerrill's patch with the numerical noise accounted for



---

archive/issue_comments_026983.json:
```json
{
    "body": "Attachment [trac_3805_expand.patch](tarball://root/attachments/some-uuid/ticket3805/trac_3805_expand.patch) by mabshoff created at 2008-09-01 01:55:38\n\nI have attached a patch that accounts for some numerical noise on Linux 64 bit. It also passes doctest on 32 bit Intel OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T01:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26983",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3805_expand.patch](tarball://root/attachments/some-uuid/ticket3805/trac_3805_expand.patch) by mabshoff created at 2008-09-01 01:55:38

I have attached a patch that accounts for some numerical noise on Linux 64 bit. It also passes doctest on 32 bit Intel OSX.

Cheers,

Michael



---

archive/issue_comments_026984.json:
```json
{
    "body": "Jason,\n\nif you solve tickets please take over ownership of them. I did reassign this ticket to you.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T01:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26984",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jason,

if you solve tickets please take over ownership of them. I did reassign this ticket to you.

Cheers,

Michael



---

archive/issue_comments_026985.json:
```json
{
    "body": "Changing assignee from @garyfurnish to @jicama.",
    "created_at": "2008-09-01T01:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26985",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @garyfurnish to @jicama.



---

archive/issue_comments_026986.json:
```json
{
    "body": "Positive review on your updated patch.  Ownership procedure noted.",
    "created_at": "2008-09-01T02:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26986",
    "user": "https://github.com/jicama"
}
```

Positive review on your updated patch.  Ownership procedure noted.



---

archive/issue_comments_026987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T02:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26987",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004027.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-01T02:20:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3805#event-4027"
}
```



---

archive/issue_comments_026988.json:
```json
{
    "body": "Merged trac_3805_expand.patch in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T02:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3805",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3805#issuecomment-26988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_3805_expand.patch in Sage 3.1.2.alpha4
