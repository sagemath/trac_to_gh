# Issue 2222: sage-2.10.2.alpha1 -- bessel_K is now broken -- higher precision doesn't work

archive/issues_002222.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage -t  const.tex                                          **********************************************************************\nFile \"const.py\", line 4626:\n    : bessel_K(3,2,100)\nExpected:\n    0.64738539094863415315923557097\nGot:\n    0.647385390948634\n```\n\n\nNote that the later 100 input is totally ignored.  I think this is due\nto some use of scipy or something for some special functions by David\nJoyner recently??\n\nIssue created by migration from https://trac.sagemath.org/ticket/2222\n\n",
    "created_at": "2008-02-20T06:46:29Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage-2.10.2.alpha1 -- bessel_K is now broken -- higher precision doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2222",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage -t  const.tex                                          **********************************************************************
File "const.py", line 4626:
    : bessel_K(3,2,100)
Expected:
    0.64738539094863415315923557097
Got:
    0.647385390948634
```


Note that the later 100 input is totally ignored.  I think this is due
to some use of scipy or something for some special functions by David
Joyner recently??

Issue created by migration from https://trac.sagemath.org/ticket/2222





---

archive/issue_comments_014692.json:
```json
{
    "body": "Yes. The correct syntax is bessel_K(3,2,\"pari\",100):\nsage: bessel_K(3,2,\"pari\",100)\n0.64738539094863415315923557097\nI ran \"sage -t\" on the file - I guess I should have run \"sage -testall\" also,\nto find things like this.",
    "created_at": "2008-02-20T11:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2222#issuecomment-14692",
    "user": "https://github.com/wdjoyner"
}
```

Yes. The correct syntax is bessel_K(3,2,"pari",100):
sage: bessel_K(3,2,"pari",100)
0.64738539094863415315923557097
I ran "sage -t" on the file - I guess I should have run "sage -testall" also,
to find things like this.



---

archive/issue_comments_014693.json:
```json
{
    "body": "You should just make pari the default algorithm, which would fix the issue in all other files.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-20T11:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2222#issuecomment-14693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

You should just make pari the default algorithm, which would fix the issue in all other files.

Cheers,

Michael



---

archive/issue_comments_014694.json:
```json
{
    "body": "As I see it. pari is the default:\ndef bessel_K(nu,z,alg=\"pari\",prec=53):\nI must be missing something obvious or else const.tex needs to change.\n\nsage: bessel_K(3,2,\"pari\",100)\n0.64738539094863415315923557097\nsage: bessel_K(3,2,prec=100)\n0.64738539094863415315923557097\nsage: bessel_K(3,2,100)\n0.647385390948634\n\nI'm happy to be corrected but it seems to me that the patch is okay,\nit's just that it's broken const.tex.",
    "created_at": "2008-02-20T19:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2222#issuecomment-14694",
    "user": "https://github.com/wdjoyner"
}
```

As I see it. pari is the default:
def bessel_K(nu,z,alg="pari",prec=53):
I must be missing something obvious or else const.tex needs to change.

sage: bessel_K(3,2,"pari",100)
0.64738539094863415315923557097
sage: bessel_K(3,2,prec=100)
0.64738539094863415315923557097
sage: bessel_K(3,2,100)
0.647385390948634

I'm happy to be corrected but it seems to me that the patch is okay,
it's just that it's broken const.tex.



---

archive/issue_events_002392.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-21T17:05:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2222",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2222#event-2392"
}
```



---

archive/issue_comments_014695.json:
```json
{
    "body": "The patch at #2246 fixes the issue -> close this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T17:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2222#issuecomment-14695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch at #2246 fixes the issue -> close this ticket.

Cheers,

Michael



---

archive/issue_comments_014696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T17:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2222",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2222#issuecomment-14696",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
