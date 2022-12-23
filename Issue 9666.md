# Issue 9666: Implement __hash__ for NumberFieldIdeal

archive/issues_009666.json:
```json
{
    "body": "Assignee: davidloeffler\n\nI propose to use a HNF Z-basis of number field ideals to compute the hash of an ideal.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9666\n\n",
    "created_at": "2010-08-01T21:41:36Z",
    "labels": [
        "number fields",
        "minor",
        "enhancement"
    ],
    "title": "Implement __hash__ for NumberFieldIdeal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9666",
    "user": "jdemeyer"
}
```
Assignee: davidloeffler

I propose to use a HNF Z-basis of number field ideals to compute the hash of an ideal.

Issue created by migration from https://trac.sagemath.org/ticket/9666





---

archive/issue_comments_093846.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-02T11:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93846",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_093847.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-02T11:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93847",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093848.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-02T22:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93848",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093849.json:
```json
{
    "body": "You need to add a doctest that illustrates use of the hash function, on both 32 and 64-bit computers.",
    "created_at": "2010-08-02T23:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93849",
    "user": "was"
}
```

You need to add a doctest that illustrates use of the hash function, on both 32 and 64-bit computers.



---

archive/issue_comments_093850.json:
```json
{
    "body": "When I ran the test suite there were a bunch of failures in\n\n   devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py\n\ne.g.,\n\n```\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.5.2.rc0/devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py\", line 1141:\n    sage: D.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)\nExpected:\n    [2, -a - 1, -a]\nGot:\n    [2, -a - 1, a]\n```\n",
    "created_at": "2010-08-03T02:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93850",
    "user": "was"
}
```

When I ran the test suite there were a bunch of failures in

   devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py

e.g.,

```
File "/mnt/usb1/scratch/wstein/build/sage-4.5.2.rc0/devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py", line 1141:
    sage: D.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)
Expected:
    [2, -a - 1, -a]
Got:
    [2, -a - 1, a]
```




---

archive/issue_comments_093851.json:
```json
{
    "body": "Apologies.  I did not expect the hash to have influence on this, I should have tested better.\n\nI will postpone this to the release after the PARI upgrade, i.e. sage-4.6.1 or something.",
    "created_at": "2010-08-03T07:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93851",
    "user": "jdemeyer"
}
```

Apologies.  I did not expect the hash to have influence on this, I should have tested better.

I will postpone this to the release after the PARI upgrade, i.e. sage-4.6.1 or something.



---

archive/issue_comments_093852.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-14T00:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93852",
    "user": "was"
}
```

Resolution: duplicate



---

archive/issue_comments_093853.json:
```json
{
    "body": "The same is fixed correctly in #9400.  So I'm closing this as a dupe of that.",
    "created_at": "2010-08-14T00:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93853",
    "user": "was"
}
```

The same is fixed correctly in #9400.  So I'm closing this as a dupe of that.
