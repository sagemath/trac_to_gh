# Issue 9666: Implement __hash__ for NumberFieldIdeal

archive/issues_009666.json:
```json
{
    "body": "Assignee: @loefflerd\n\nI propose to use a HNF Z-basis of number field ideals to compute the hash of an ideal.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9666\n\n",
    "created_at": "2010-08-01T21:41:36Z",
    "labels": [
        "component: number fields",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Implement __hash__ for NumberFieldIdeal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9666",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @loefflerd

I propose to use a HNF Z-basis of number field ideals to compute the hash of an ideal.

Issue created by migration from https://trac.sagemath.org/ticket/9666





---

archive/issue_comments_093689.json:
```json
{
    "body": "Attachment [9666.patch](tarball://root/attachments/some-uuid/ticket9666/9666.patch) by @jdemeyer created at 2010-08-02 11:55:18",
    "created_at": "2010-08-02T11:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93689",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9666.patch](tarball://root/attachments/some-uuid/ticket9666/9666.patch) by @jdemeyer created at 2010-08-02 11:55:18



---

archive/issue_comments_093690.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-02T11:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93690",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093691.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-02T22:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93691",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093692.json:
```json
{
    "body": "You need to add a doctest that illustrates use of the hash function, on both 32 and 64-bit computers.",
    "created_at": "2010-08-02T23:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93692",
    "user": "https://github.com/williamstein"
}
```

You need to add a doctest that illustrates use of the hash function, on both 32 and 64-bit computers.



---

archive/issue_comments_093693.json:
```json
{
    "body": "When I ran the test suite there were a bunch of failures in\n\n   devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py\n\ne.g.,\n\n```\nFile \"/mnt/usb1/scratch/wstein/build/sage-4.5.2.rc0/devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py\", line 1141:\n    sage: D.selmer_group([K.ideal(2, -a+1), K.ideal(3, a+1), K.ideal(a)], 3)\nExpected:\n    [2, -a - 1, -a]\nGot:\n    [2, -a - 1, a]\n```\n",
    "created_at": "2010-08-03T02:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93693",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_093694.json:
```json
{
    "body": "Apologies.  I did not expect the hash to have influence on this, I should have tested better.\n\nI will postpone this to the release after the PARI upgrade, i.e. sage-4.6.1 or something.",
    "created_at": "2010-08-03T07:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93694",
    "user": "https://github.com/jdemeyer"
}
```

Apologies.  I did not expect the hash to have influence on this, I should have tested better.

I will postpone this to the release after the PARI upgrade, i.e. sage-4.6.1 or something.



---

archive/issue_events_009801.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-08-14T00:55:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9666#event-9801"
}
```



---

archive/issue_comments_093695.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-14T00:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93695",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_comments_093696.json:
```json
{
    "body": "The same is fixed correctly in #9400.  So I'm closing this as a dupe of that.",
    "created_at": "2010-08-14T00:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9666#issuecomment-93696",
    "user": "https://github.com/williamstein"
}
```

The same is fixed correctly in #9400.  So I'm closing this as a dupe of that.
