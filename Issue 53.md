# Issue 53: p-adic log is broken

archive/issues_000053.json:
```json
{
    "body": "Assignee: dmharvey\n\n\n```\nsage: x = 1 + 5 + O(5^6)\nsage: y = 1 + 5 + O(5^5)\nsage: x.log()\n 5 + 2*5^2 + 4*5^3 + 2*5^4 + O(5^6)\nsage: y.log()\n 5 + 2*5^2 + 4*5^3 + 5^4 + O(5^5)\n```\n\n\nThe answers should agree mod 5!^5. I bet someone forgot to take into account the p-adic valuation of the denominators in the series.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/53\n\n",
    "created_at": "2006-09-13T19:43:11Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "p-adic log is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/53",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: dmharvey


```
sage: x = 1 + 5 + O(5^6)
sage: y = 1 + 5 + O(5^5)
sage: x.log()
 5 + 2*5^2 + 4*5^3 + 2*5^4 + O(5^6)
sage: y.log()
 5 + 2*5^2 + 4*5^3 + 5^4 + O(5^5)
```


The answers should agree mod 5!^5. I bet someone forgot to take into account the p-adic valuation of the denominators in the series.


Issue created by migration from https://trac.sagemath.org/ticket/53





---

archive/issue_comments_000289.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-09-16T05:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/53",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/53#issuecomment-289",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Resolution: fixed



---

archive/issue_events_000052.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/dmharvey",
    "created_at": "2006-09-16T05:05:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/53",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/53#event-52"
}
```



---

archive/issue_comments_000290.json:
```json
{
    "body": "Fixed.\n\nWed Sep 13 18:09:41 PDT 2006  dmharvey`@`math.harvard.edu\n* fix p-adic log -- fixed p-adic log which gave incorrect answers sometimes (trac ticket #53)",
    "created_at": "2006-09-16T05:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/53",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/53#issuecomment-290",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Fixed.

Wed Sep 13 18:09:41 PDT 2006  dmharvey`@`math.harvard.edu
* fix p-adic log -- fixed p-adic log which gave incorrect answers sometimes (trac ticket #53)
