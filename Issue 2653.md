# Issue 2653: norm and trace of elements of orders are Rational not Integer

archive/issues_002653.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: orders, norm, trace\n\nFor elements of an order, the norm and trace are (mathematically) integers, but Sage returns Rationals.  More generally, the charpoly and minpoly are returned as Rational polynomials when they are (mathematically) in ZZ[].\n\n\n```\nsage: Zi.<i>=ZZ.extension(x^2+1)\nsage: n=(1+i).norm()\nsage: type(n)\n<type 'sage.rings.rational.Rational'>\nsage: t=(1+i).trace()\nsage: type(t)\n<type 'sage.rings.rational.Rational'>\nsage: p=(1+i).charpoly()\nsage: type(p)\n<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>\nsage: p=(1+i).minpoly()\nsage: type(p)\n<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>\n```\n\n\nI would like this to change, as it led to some very inefficient behaviour until I discovered it, and now I am having to manually coerce norms and traces into ZZ.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2653\n\n",
    "created_at": "2008-03-23T10:34:32Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "norm and trace of elements of orders are Rational not Integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2653",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: orders, norm, trace

For elements of an order, the norm and trace are (mathematically) integers, but Sage returns Rationals.  More generally, the charpoly and minpoly are returned as Rational polynomials when they are (mathematically) in ZZ[].


```
sage: Zi.<i>=ZZ.extension(x^2+1)
sage: n=(1+i).norm()
sage: type(n)
<type 'sage.rings.rational.Rational'>
sage: t=(1+i).trace()
sage: type(t)
<type 'sage.rings.rational.Rational'>
sage: p=(1+i).charpoly()
sage: type(p)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>
sage: p=(1+i).minpoly()
sage: type(p)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>
```


I would like this to change, as it led to some very inefficient behaviour until I discovered it, and now I am having to manually coerce norms and traces into ZZ.


Issue created by migration from https://trac.sagemath.org/ticket/2653





---

archive/issue_comments_018196.json:
```json
{
    "body": "Actually it is worse than that:\n\n```\nsage: Zi.<i>=ZZ.extension(x^2+1)\nsage: a=1+i\nsage: a.norm()\n4\nsage: a.trace()\n4\nsage: a.minpoly()\nx - 2\nsage: a.charpoly()\nx^2 - 4*x + 4\n```\n\n\nThese are wrong!  Both the minpoly and charpoly of 1+i should be x^2-2*x+2, the trace should be 2 and the norm 2.",
    "created_at": "2008-03-23T10:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2653#issuecomment-18196",
    "user": "https://github.com/JohnCremona"
}
```

Actually it is worse than that:

```
sage: Zi.<i>=ZZ.extension(x^2+1)
sage: a=1+i
sage: a.norm()
4
sage: a.trace()
4
sage: a.minpoly()
x - 2
sage: a.charpoly()
x^2 - 4*x + 4
```


These are wrong!  Both the minpoly and charpoly of 1+i should be x^2-2*x+2, the trace should be 2 and the norm 2.



---

archive/issue_comments_018197.json:
```json
{
    "body": "Apologies:  the code\n\n```\nsage: Zi.<i>=ZZ.extension(x^2+1)\n```\n\nresults in i being asigned to the first Z-module generator of the order, which is 1:\n\n```\nsage: i\n1\n```\n\nso the second posting on this ticket is incorrect to say that the minpoly and charpoly (etc) are wrongly computed.\n\nHowever I do *not* think that users should be allowed to enter\n\n```\nsage: Zi.<i>=ZZ.extension(x^2+1)\n```\n\nand have i assigned to 1.",
    "created_at": "2008-03-23T10:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2653#issuecomment-18197",
    "user": "https://github.com/JohnCremona"
}
```

Apologies:  the code

```
sage: Zi.<i>=ZZ.extension(x^2+1)
```

results in i being asigned to the first Z-module generator of the order, which is 1:

```
sage: i
1
```

so the second posting on this ticket is incorrect to say that the minpoly and charpoly (etc) are wrongly computed.

However I do *not* think that users should be allowed to enter

```
sage: Zi.<i>=ZZ.extension(x^2+1)
```

and have i assigned to 1.



---

archive/issue_comments_018198.json:
```json
{
    "body": "Attachment [2653-integral-norms.patch](tarball://root/attachments/some-uuid/ticket2653/2653-integral-norms.patch) by @robertwb created at 2008-03-26 04:34:09",
    "created_at": "2008-03-26T04:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2653#issuecomment-18198",
    "user": "https://github.com/robertwb"
}
```

Attachment [2653-integral-norms.patch](tarball://root/attachments/some-uuid/ticket2653/2653-integral-norms.patch) by @robertwb created at 2008-03-26 04:34:09



---

archive/issue_comments_018199.json:
```json
{
    "body": "Review of patch:  the code looks just fine and appears to solve the problem raised.  I only say \"appears\" as I'm travelling and not in a position to test it myself, but the added doctests give me sufficitne confidence to say: OK!",
    "created_at": "2008-03-26T22:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2653#issuecomment-18199",
    "user": "https://github.com/JohnCremona"
}
```

Review of patch:  the code looks just fine and appears to solve the problem raised.  I only say "appears" as I'm travelling and not in a position to test it myself, but the added doctests give me sufficitne confidence to say: OK!



---

archive/issue_comments_018200.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-26T22:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2653#issuecomment-18200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_events_002844.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-26T22:13:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2653",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2653#event-2844"
}
```



---

archive/issue_comments_018201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-26T22:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2653#issuecomment-18201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
