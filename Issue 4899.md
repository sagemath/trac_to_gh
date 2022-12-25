# Issue 4899: bug in sqrt(1) over GF(2^e) for e>15

archive/issues_004899.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: finite fields\n\n\n```\nsage: GF(2^15,'a')(1).sqrt()\n1\nsage: GF(2^16,'a')(1).sqrt()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/john/<ipython console> in <module>()\n\n/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/rings/finite_field_ntl_gf2e.so in sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2eElement.sqrt (sage/rings/finite_field_ntl_gf2e.cpp:7072)()\n\nAttributeError: 'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_g' object has no attribute '_one_element'\n```\n\nThe point is that `GF(2^16)` (and higher) are of type  'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e'\nand the code (lines 826,827 in finite_field_ntl_gf2e.pyx)\n\n```\n        if self.is_one():\n            return self._one_element\n```\n\nfails.  It should be self.parent()._one_element  (though I don't know why \"return self\" would not be ok too).\n\nPatch up very soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4899\n\n",
    "created_at": "2009-01-01T12:14:52Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "bug in sqrt(1) over GF(2^e) for e>15",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4899",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tbd

Keywords: finite fields


```
sage: GF(2^15,'a')(1).sqrt()
1
sage: GF(2^16,'a')(1).sqrt()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/john/<ipython console> in <module>()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/rings/finite_field_ntl_gf2e.so in sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2eElement.sqrt (sage/rings/finite_field_ntl_gf2e.cpp:7072)()

AttributeError: 'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_g' object has no attribute '_one_element'
```

The point is that `GF(2^16)` (and higher) are of type  'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e'
and the code (lines 826,827 in finite_field_ntl_gf2e.pyx)

```
        if self.is_one():
            return self._one_element
```

fails.  It should be self.parent()._one_element  (though I don't know why "return self" would not be ok too).

Patch up very soon.

Issue created by migration from https://trac.sagemath.org/ticket/4899





---

archive/issue_comments_037089.json:
```json
{
    "body": "Attachment [trac_4899.patch](tarball://root/attachments/some-uuid/ticket4899/trac_4899.patch) by @JohnCremona created at 2009-01-01 12:22:26",
    "created_at": "2009-01-01T12:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4899#issuecomment-37089",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4899.patch](tarball://root/attachments/some-uuid/ticket4899/trac_4899.patch) by @JohnCremona created at 2009-01-01 12:22:26



---

archive/issue_comments_037090.json:
```json
{
    "body": "Attachment [trac_4899-referee.patch](tarball://root/attachments/some-uuid/ticket4899/trac_4899-referee.patch) by @williamstein created at 2009-01-03 05:00:39\n\napply this after trac_4899.patch",
    "created_at": "2009-01-03T05:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4899#issuecomment-37090",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4899-referee.patch](tarball://root/attachments/some-uuid/ticket4899/trac_4899-referee.patch) by @williamstein created at 2009-01-03 05:00:39

apply this after trac_4899.patch



---

archive/issue_comments_037091.json:
```json
{
    "body": "REFEREE REPORT:\n\nNice find.   You remark \"It should be self.parent()._one_element (though I don't know why \"return self\" would not be ok too).\".  In fact, I think returning self would be ok.  I tried that and it is also over twice as fast.  So I've posted a followup patch that does that instead.",
    "created_at": "2009-01-03T05:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4899#issuecomment-37091",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

Nice find.   You remark "It should be self.parent()._one_element (though I don't know why "return self" would not be ok too).".  In fact, I think returning self would be ok.  I tried that and it is also over twice as fast.  So I've posted a followup patch that does that instead.



---

archive/issue_comments_037092.json:
```json
{
    "body": "Shouldn't we add a doctest here?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-03T05:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4899#issuecomment-37092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Shouldn't we add a doctest here?

Cheers,

Michael



---

archive/issue_comments_037093.json:
```json
{
    "body": "Merged both patches in Sage 3.2.3.final",
    "created_at": "2009-01-03T06:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4899#issuecomment-37093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.3.final



---

archive/issue_events_005142.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-03T06:03:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4899#event-5142"
}
```



---

archive/issue_comments_037094.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-03T06:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4899#issuecomment-37094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037095.json:
```json
{
    "body": "Never mind, John's patch contained a doctest as William just pointed out to me in IRC.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-03T06:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4899#issuecomment-37095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Never mind, John's patch contained a doctest as William just pointed out to me in IRC.

Cheers,

Michael
