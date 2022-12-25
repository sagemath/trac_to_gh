# Issue 7834: Implement conjugate() for RealDoubleElement

archive/issues_007834.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis appears inconsistent, and is an actual problem for me:\n\n```\nsage: ZZ(4).conjugate()\n4\nsage: RR(4).conjugate()\n4.00000000000000\nsage: RDF(4).conjugate()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/uio/arkimedes/s07/dagss/.sage/temp/corcaroli.uio.no/12687/_uio_arkimedes_s07_dagss__sage_init_sage_0.py in <module>()\n\nAttributeError: 'sage.rings.real_double.RealDoubleElement' object has no attribute 'conjugate'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7834\n\n",
    "created_at": "2010-01-03T18:53:11Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Implement conjugate() for RealDoubleElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7834",
    "user": "https://trac.sagemath.org/admin/accounts/users/dagss"
}
```
Assignee: @aghitza

This appears inconsistent, and is an actual problem for me:

```
sage: ZZ(4).conjugate()
4
sage: RR(4).conjugate()
4.00000000000000
sage: RDF(4).conjugate()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/uio/arkimedes/s07/dagss/.sage/temp/corcaroli.uio.no/12687/_uio_arkimedes_s07_dagss__sage_init_sage_0.py in <module>()

AttributeError: 'sage.rings.real_double.RealDoubleElement' object has no attribute 'conjugate'
```


Issue created by migration from https://trac.sagemath.org/ticket/7834





---

archive/issue_comments_067749.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T18:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7834#issuecomment-67749",
    "user": "https://trac.sagemath.org/admin/accounts/users/dagss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067750.json:
```json
{
    "body": "Attachment [RDF_conjugate.patch](tarball://root/attachments/some-uuid/ticket7834/RDF_conjugate.patch) by dagss created at 2010-01-03 18:53:52",
    "created_at": "2010-01-03T18:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7834#issuecomment-67750",
    "user": "https://trac.sagemath.org/admin/accounts/users/dagss"
}
```

Attachment [RDF_conjugate.patch](tarball://root/attachments/some-uuid/ticket7834/RDF_conjugate.patch) by dagss created at 2010-01-03 18:53:52



---

archive/issue_comments_067751.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-03T22:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7834#issuecomment-67751",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067752.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-01-03T22:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7834#issuecomment-67752",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.



---

archive/issue_events_018735.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-04T02:03:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7834",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7834#event-18735"
}
```



---

archive/issue_comments_067753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T02:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7834#issuecomment-67753",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
