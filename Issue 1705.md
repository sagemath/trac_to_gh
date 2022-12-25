# Issue 1705: factorization of polynomials over non-prime finite fields is TOTALLY BROKEN in Sage (and Singular?!)

archive/issues_001705.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  mabshoff\n\n\n```\nsage: k.<a> = GF(9)\nsage: R.<x,y> = PolynomialRing(k)\nsage: f = (x-a)*(y-a)\nsage: f.factor()\nx*y + ( - a)*x + ( - a)*y + (a + 1)\nsage: singular(f)\nx*y+(-a)*x+(-a)*y+(a+1)\nsage: singular(f).factorH()\n[1]:\n   _[1]=1\n   _[2]=x*y+(-a)*x+(-a)*y+(a+1)\n[2]:\n   1,1\nsage: f = (x-2)*(y-1)\nsage: f.factor()\n(y - 1) * (x + 1)\nsage: singular(f).factorH()\n[1]:\n   _[1]=1\n   _[2]=x+1\n   _[3]=y-1\n[2]:\n   1,1,1\n```\n\n\nIn Magma this works fine:\n\n```\nk<a> := GF(9);\nR<x,y> := PolynomialRing(k, 2);\nf := (x-a)*(y-a);\nprint Factorization(f);\n\n[\n<y + a^5, 1>,\n<x + a^5, 1>\n]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1705\n\n",
    "created_at": "2008-01-07T04:01:49Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "factorization of polynomials over non-prime finite fields is TOTALLY BROKEN in Sage (and Singular?!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1705",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

CC:  mabshoff


```
sage: k.<a> = GF(9)
sage: R.<x,y> = PolynomialRing(k)
sage: f = (x-a)*(y-a)
sage: f.factor()
x*y + ( - a)*x + ( - a)*y + (a + 1)
sage: singular(f)
x*y+(-a)*x+(-a)*y+(a+1)
sage: singular(f).factorH()
[1]:
   _[1]=1
   _[2]=x*y+(-a)*x+(-a)*y+(a+1)
[2]:
   1,1
sage: f = (x-2)*(y-1)
sage: f.factor()
(y - 1) * (x + 1)
sage: singular(f).factorH()
[1]:
   _[1]=1
   _[2]=x+1
   _[3]=y-1
[2]:
   1,1,1
```


In Magma this works fine:

```
k<a> := GF(9);
R<x,y> := PolynomialRing(k, 2);
f := (x-a)*(y-a);
print Factorization(f);

[
<y + a^5, 1>,
<x + a^5, 1>
]
```


Issue created by migration from https://trac.sagemath.org/ticket/1705





---

archive/issue_comments_010771.json:
```json
{
    "body": "I can confirm this behaviour with official Singular binary:\n\n\n```\n> ring r = (3,a),(x,y),dp;\n> minpoly = a^2 + 2*a + 2;\n> poly f = (x-a)*(y-a);\n> factorize(f);\n[1]:\n   _[1]=1\n   _[2]=xy+(-a)*x+(-a)*y+(a+1)\n[2]:\n   1,1\n```\n\n\nMichael volunteered to report this upstream.",
    "created_at": "2008-01-07T11:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1705#issuecomment-10771",
    "user": "https://github.com/malb"
}
```

I can confirm this behaviour with official Singular binary:


```
> ring r = (3,a),(x,y),dp;
> minpoly = a^2 + 2*a + 2;
> poly f = (x-a)*(y-a);
> factorize(f);
[1]:
   _[1]=1
   _[2]=xy+(-a)*x+(-a)*y+(a+1)
[2]:
   1,1
```


Michael volunteered to report this upstream.



---

archive/issue_comments_010772.json:
```json
{
    "body": "This bug is *so* terrible, that I think it should be considered a blocker, and we should have a NOtImplementedError be raised any time somebody factors a poly over a finite field in n variables.   This is really bad.",
    "created_at": "2008-01-07T16:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1705#issuecomment-10772",
    "user": "https://github.com/williamstein"
}
```

This bug is *so* terrible, that I think it should be considered a blocker, and we should have a NOtImplementedError be raised any time somebody factors a poly over a finite field in n variables.   This is really bad.



---

archive/issue_comments_010773.json:
```json
{
    "body": "The Singular team is working on a fix for this issue. I will keep you updated.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T16:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1705#issuecomment-10773",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The Singular team is working on a fix for this issue. I will keep you updated.

Cheers,

Michael



---

archive/issue_comments_010774.json:
```json
{
    "body": "Attachment [trac_1705.patch](tarball://root/attachments/some-uuid/ticket1705/trac_1705.patch) by mabshoff created at 2008-01-18 01:48:17\n\nMerged trac_1705.patch. We are closing this ticket and will open a new one once the issue is fixed upstream.",
    "created_at": "2008-01-18T01:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1705#issuecomment-10774",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_1705.patch](tarball://root/attachments/some-uuid/ticket1705/trac_1705.patch) by mabshoff created at 2008-01-18 01:48:17

Merged trac_1705.patch. We are closing this ticket and will open a new one once the issue is fixed upstream.



---

archive/issue_comments_010775.json:
```json
{
    "body": "Merged in Sage 2.10.alpha4.",
    "created_at": "2008-01-18T01:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1705#issuecomment-10775",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha4.



---

archive/issue_events_001864.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-18T01:48:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1705",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1705#event-1864"
}
```



---

archive/issue_comments_010776.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-18T01:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1705#issuecomment-10776",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
