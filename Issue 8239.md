# Issue 8239: misleading teichmuller behaviour

archive/issues_008239.json:
```json
{
    "body": "Assignee: roed\n\nCC:  roed\n\nThis is kind of misleading:\n\n\n```\nsage: K.<a> = Qq(25)\nsage: K.teichmuller(K(2/5))\n2*5^-1 + 1 + 2*5 + 5^2 + 3*5^3 + 4*5^4 + 2*5^5 + 3*5^6 + 3*5^8 + 2*5^9 + 2*5^10 + 4*5^12 + 5^13 + 3*5^14 + 2*5^15 + 4*5^16 + 4*5^18 + O(5^19)\n```\n\n\nIt should raise an exception.\n\nThe prime case behaves as I would expect:\n\n\n```\nsage: K = Qp(5)\nsage: K.teichmuller(K(2/5))\nTraceback (click to the left of this block for traceback)\n...\nValueError: cannot set negative valuation element to Teichmuller\nrepresentative.\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8239\n\n",
    "created_at": "2010-02-11T19:45:25Z",
    "labels": [
        "padics",
        "major",
        "bug"
    ],
    "title": "misleading teichmuller behaviour",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8239",
    "user": "dmharvey"
}
```
Assignee: roed

CC:  roed

This is kind of misleading:


```
sage: K.<a> = Qq(25)
sage: K.teichmuller(K(2/5))
2*5^-1 + 1 + 2*5 + 5^2 + 3*5^3 + 4*5^4 + 2*5^5 + 3*5^6 + 3*5^8 + 2*5^9 + 2*5^10 + 4*5^12 + 5^13 + 3*5^14 + 2*5^15 + 4*5^16 + 4*5^18 + O(5^19)
```


It should raise an exception.

The prime case behaves as I would expect:


```
sage: K = Qp(5)
sage: K.teichmuller(K(2/5))
Traceback (click to the left of this block for traceback)
...
ValueError: cannot set negative valuation element to Teichmuller
representative.
```



Issue created by migration from https://trac.sagemath.org/ticket/8239





---

archive/issue_comments_072802.json:
```json
{
    "body": "Attachment [8239.patch](tarball://root/attachments/some-uuid/ticket8239/8239.patch) by roed created at 2011-11-11 02:20:41",
    "created_at": "2011-11-11T02:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8239#issuecomment-72802",
    "user": "roed"
}
```

Attachment [8239.patch](tarball://root/attachments/some-uuid/ticket8239/8239.patch) by roed created at 2011-11-11 02:20:41



---

archive/issue_comments_072803.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-11T02:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8239#issuecomment-72803",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072804.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-12T14:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8239#issuecomment-72804",
    "user": "johanbosman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072805.json:
```json
{
    "body": "This looks okay and passes all tests. :).",
    "created_at": "2011-11-12T14:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8239#issuecomment-72805",
    "user": "johanbosman"
}
```

This looks okay and passes all tests. :).



---

archive/issue_comments_072806.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-11-15T08:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8239#issuecomment-72806",
    "user": "jdemeyer"
}
```

Resolution: fixed
