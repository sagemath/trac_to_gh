# Issue 28: weird power series behavior

archive/issues_000028.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<m> = LaurentSeriesRing(QQ)\n   sage: S.<t> = LaurentSeriesRing(pAdicField(11))\n   sage: S(m^(-2) + 10*m + m^2 + O(m^3))\n   t^1 + 10*t^3 + t^4 + O(t^5) + 10*t^4 + 10*t^3 + t^4 + O(t^5) + t^5 + 10*t^3 + t^4 + O(t^5) + O(t^6 + 10*t^3 + t^4 + O(t^5))\n```\n\n  \nHuh?\n\nIssue created by migration from https://trac.sagemath.org/ticket/28\n\n",
    "created_at": "2006-09-12T23:25:31Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "weird power series behavior",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/28",
    "user": "was"
}
```
Assignee: somebody


```
sage: R.<m> = LaurentSeriesRing(QQ)
   sage: S.<t> = LaurentSeriesRing(pAdicField(11))
   sage: S(m^(-2) + 10*m + m^2 + O(m^3))
   t^1 + 10*t^3 + t^4 + O(t^5) + 10*t^4 + 10*t^3 + t^4 + O(t^5) + t^5 + 10*t^3 + t^4 + O(t^5) + O(t^6 + 10*t^3 + t^4 + O(t^5))
```

  
Huh?

Issue created by migration from https://trac.sagemath.org/ticket/28





---

archive/issue_comments_000199.json:
```json
{
    "body": "looks similar to ticket #7",
    "created_at": "2006-09-13T00:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/28",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/28#issuecomment-199",
    "user": "dmharvey"
}
```

looks similar to ticket #7



---

archive/issue_comments_000200.json:
```json
{
    "body": "This is now fixed in sage-1.6:\n\n```\nsage: R.<m> = LaurentSeriesRing(QQ)\n   sage: S.<t> = LaurentSeriesRing(pAdicField(11))\n   sage: S(m^(-2) + 10*m + m^2 + O(m^3))\nt^-2 + (10 + O(11^Infinity))*t + t^2 + O(t^3)\n```\n",
    "created_at": "2007-01-13T01:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/28",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/28#issuecomment-200",
    "user": "was"
}
```

This is now fixed in sage-1.6:

```
sage: R.<m> = LaurentSeriesRing(QQ)
   sage: S.<t> = LaurentSeriesRing(pAdicField(11))
   sage: S(m^(-2) + 10*m + m^2 + O(m^3))
t^-2 + (10 + O(11^Infinity))*t + t^2 + O(t^3)
```




---

archive/issue_comments_000201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T01:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/28",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/28#issuecomment-201",
    "user": "was"
}
```

Resolution: fixed
