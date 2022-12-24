# Issue 6589: bring doctest coverage for ring/laurent_series_ring.py to 100%

archive/issues_006589.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: Laurent series, doctest, coverage\n\nI (Marshall Hampton) am hoping to work on this in late July or August 2009.  If it hasn't been done by September, assume that I didn't get around to it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6589\n\n",
    "created_at": "2009-07-22T13:07:51Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bring doctest coverage for ring/laurent_series_ring.py to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6589",
    "user": "mhampton"
}
```
Assignee: tbd

Keywords: Laurent series, doctest, coverage

I (Marshall Hampton) am hoping to work on this in late July or August 2009.  If it hasn't been done by September, assume that I didn't get around to it.

Issue created by migration from https://trac.sagemath.org/ticket/6589





---

archive/issue_comments_053926.json:
```json
{
    "body": "As of Sage 5.7.beta2, the file in question does have 100% coverage. So, I think this has been done. See the related #12259 (which itself is a part of the bigger meta ticket: #12024). So, I'll set this to sage-invalid...",
    "created_at": "2013-02-03T19:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6589#issuecomment-53926",
    "user": "knsam"
}
```

As of Sage 5.7.beta2, the file in question does have 100% coverage. So, I think this has been done. See the related #12259 (which itself is a part of the bigger meta ticket: #12024). So, I'll set this to sage-invalid...



---

archive/issue_comments_053927.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-03T19:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6589#issuecomment-53927",
    "user": "knsam"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053928.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-05T18:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6589#issuecomment-53928",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053929.json:
```json
{
    "body": "Also in `5.5.rc0`:\n\n```\ntravis@travis-virtualbox:~/sage-5.5.rc0/devel/sage/sage$ sage -coverage rings/laurent_series_ring.py \n----------------------------------------------------------------------\nrings/laurent_series_ring.py\nSCORE rings/laurent_series_ring.py: 100% (25 of 25)\n----------------------------------------------------------------------\n```\n",
    "created_at": "2013-02-05T18:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6589#issuecomment-53929",
    "user": "tscrim"
}
```

Also in `5.5.rc0`:

```
travis@travis-virtualbox:~/sage-5.5.rc0/devel/sage/sage$ sage -coverage rings/laurent_series_ring.py 
----------------------------------------------------------------------
rings/laurent_series_ring.py
SCORE rings/laurent_series_ring.py: 100% (25 of 25)
----------------------------------------------------------------------
```




---

archive/issue_comments_053930.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-02-08T13:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6589#issuecomment-53930",
    "user": "jdemeyer"
}
```

Resolution: worksforme
