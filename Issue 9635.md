# Issue 9635: symbolic sum gives wrong answer

archive/issues_009635.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\nsage: (n,k,j)=var('n,k,j')\nsage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)\n0\nsage: (n,j)=(5,3)\nsage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j) for k in range(j\n+1,n+1))\n1 \n```\n\nThe above sum should be 1 for n>=j and 0 otherwise.\n\nFrom kcrisman:\nThis appears to be a bug in Maxima. \n\n```\n(%i1) load(simplify_sum);\n<snip>\n(%i3) simplify_sum(sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j\n+1,n));\n\n(%o3)                                  0\n(%i4) simplify_sum(sum(binomial(5,k)*binomial(k-1,3)*(-1)**(k-1-3),k,\n4,5));\n(%o4)                                  1\n(%i5) 5*1*1+1*4*(-1);\n(%o5)                                  1 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9635\n\n",
    "created_at": "2010-07-29T07:34:28Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "symbolic sum gives wrong answer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9635",
    "user": "Henryk.Trappmann"
}
```
Assignee: AlexGhitza


```
sage: (n,k,j)=var('n,k,j')
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
0
sage: (n,j)=(5,3)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j) for k in range(j
+1,n+1))
1 
```

The above sum should be 1 for n>=j and 0 otherwise.

From kcrisman:
This appears to be a bug in Maxima. 

```
(%i1) load(simplify_sum);
<snip>
(%i3) simplify_sum(sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j
+1,n));

(%o3)                                  0
(%i4) simplify_sum(sum(binomial(5,k)*binomial(k-1,3)*(-1)**(k-1-3),k,
4,5));
(%o4)                                  1
(%i5) 5*1*1+1*4*(-1);
(%o5)                                  1 
```


Issue created by migration from https://trac.sagemath.org/ticket/9635





---

archive/issue_comments_093395.json:
```json
{
    "body": "Changing assignee from AlexGhitza to burcin.",
    "created_at": "2010-07-29T13:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93395",
    "user": "kcrisman"
}
```

Changing assignee from AlexGhitza to burcin.



---

archive/issue_comments_093396.json:
```json
{
    "body": "Changing component from basic arithmetic to calculus.",
    "created_at": "2010-07-29T13:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93396",
    "user": "kcrisman"
}
```

Changing component from basic arithmetic to calculus.



---

archive/issue_comments_093397.json:
```json
{
    "body": "This is now Maxima bug 3036579.",
    "created_at": "2010-07-29T13:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93397",
    "user": "kcrisman"
}
```

This is now Maxima bug 3036579.



---

archive/issue_comments_093398.json:
```json
{
    "body": "Maxima 5.23.2 still has this, and no movement on the original bug report.",
    "created_at": "2011-03-14T20:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93398",
    "user": "kcrisman"
}
```

Maxima 5.23.2 still has this, and no movement on the original bug report.



---

archive/issue_comments_093399.json:
```json
{
    "body": "The [bug report](http://sourceforge.net/tracker/?func=detail&aid=3036579&group_id=4933&atid=104933) got updated over a year ago.\n\nIn the current Sage:\n\n```\n(%i1) load(simplify_sum); \n(%o1) /Users/karl-dietercrisman/Downloads/sage-5.0/local/share/maxima/5.26.0/s\\\nhare/contrib/solve_rec/simplify_sum.mac\n(%i2) simplify_sum(sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j +1,n)); \n\nIs  j + 1  positive, negative, or zero?\n\npos;\n(%o2)                                  1\n```\n\nSo just need a doctest.\n\n```\nsage: (n,k,j)=var('n,k,j')\nsage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)\n-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)\nsage: assume(j>-1)\nsage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)\n1\nsage: forget()\nsage: assume(n>=j)\nsage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)\n-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)\nsage: forget()\nsage: assume(j==-1)\nsage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)\n1\nsage: forget()\nsage: assume(j<-1)\nsage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)\n-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)\n```\n\nWas the original report here wrong?  Maxima currently says that the sign of `j+1` is all that matters, which sort of makes sense",
    "created_at": "2012-07-07T03:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93399",
    "user": "kcrisman"
}
```

The [bug report](http://sourceforge.net/tracker/?func=detail&aid=3036579&group_id=4933&atid=104933) got updated over a year ago.

In the current Sage:

```
(%i1) load(simplify_sum); 
(%o1) /Users/karl-dietercrisman/Downloads/sage-5.0/local/share/maxima/5.26.0/s\
hare/contrib/solve_rec/simplify_sum.mac
(%i2) simplify_sum(sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j +1,n)); 

Is  j + 1  positive, negative, or zero?

pos;
(%o2)                                  1
```

So just need a doctest.

```
sage: (n,k,j)=var('n,k,j')
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
sage: assume(j>-1)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
1
sage: forget()
sage: assume(n>=j)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
sage: forget()
sage: assume(j==-1)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
1
sage: forget()
sage: assume(j<-1)
sage: sum(binomial(n,k)*binomial(k-1,j)*(-1)**(k-1-j),k,j+1,n)
-sum((-1)^(-j + k)*binomial(k - 1, j)*binomial(n, k), k, j + 1, n)
```

Was the original report here wrong?  Maxima currently says that the sign of `j+1` is all that matters, which sort of makes sense



---

archive/issue_comments_093400.json:
```json
{
    "body": "Now it's no longer solved at all, i.e., the sum is returned. Since there is no longer an erroneous result the ticket can be closed I think.",
    "created_at": "2015-02-01T10:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93400",
    "user": "rws"
}
```

Now it's no longer solved at all, i.e., the sum is returned. Since there is no longer an erroneous result the ticket can be closed I think.



---

archive/issue_comments_093401.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-02-01T10:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93401",
    "user": "rws"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093402.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-02-02T01:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93402",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_093403.json:
```json
{
    "body": "All closures like this should be doctested - in case the bad behavior returns.",
    "created_at": "2015-02-02T01:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93403",
    "user": "kcrisman"
}
```

All closures like this should be doctested - in case the bad behavior returns.



---

archive/issue_comments_093404.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-02-02T08:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93404",
    "user": "rws"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_093405.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-02-02T08:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93405",
    "user": "rws"
}
```

New commits:



---

archive/issue_comments_093406.json:
```json
{
    "body": "Actually, in this case the doctest I pasted above is absolutely correct.  One still has to *assume* the right thing for it to return anything other than the original sum!  Your part is fine, you can just review the additional ones (unless you think they are too much).\n----\nNew commits:",
    "created_at": "2015-02-03T02:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93406",
    "user": "kcrisman"
}
```

Actually, in this case the doctest I pasted above is absolutely correct.  One still has to *assume* the right thing for it to return anything other than the original sum!  Your part is fine, you can just review the additional ones (unless you think they are too much).
----
New commits:



---

archive/issue_comments_093407.json:
```json
{
    "body": "Somehow I still expect results like `a (for x<0); b (for x==0); c (else)` but I digress...",
    "created_at": "2015-02-03T08:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93407",
    "user": "rws"
}
```

Somehow I still expect results like `a (for x<0); b (for x==0); c (else)` but I digress...



---

archive/issue_comments_093408.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-03T08:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93408",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093409.json:
```json
{
    "body": "Tests OK, is fine.",
    "created_at": "2015-02-03T08:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93409",
    "user": "rws"
}
```

Tests OK, is fine.



---

archive/issue_comments_093410.json:
```json
{
    "body": "> Somehow I still expect results like a (for x<0); b (for x==0); c (else) but I digress...\n\nThat isn't possible with the current Maxima setup (at least not in a useful way, given the crazy number of branches Maxima gives us) but perhaps via sympy?  That would be a very, very good improvement.",
    "created_at": "2015-02-03T13:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93410",
    "user": "kcrisman"
}
```

> Somehow I still expect results like a (for x<0); b (for x==0); c (else) but I digress...

That isn't possible with the current Maxima setup (at least not in a useful way, given the crazy number of branches Maxima gives us) but perhaps via sympy?  That would be a very, very good improvement.



---

archive/issue_comments_093411.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-02-08T15:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9635#issuecomment-93411",
    "user": "vbraun"
}
```

Resolution: fixed
