# Issue 7372: Fix iterator for finite fields

archive/issues_007372.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @malb ylchapuy\n\nKeywords: finite field iterator\n\n\n```\nsage: K.<a>=GF(2^16)\nsage: K.list()\n...\nTypeError: 'sage.rings.ring.FiniteFieldIterator' object is not iterable\n```\n\n\nSee #7366 for smaller fields (givaro implementation), this is for fields as large as 2^16.\n\nDiscussion: http://groups.google.com/group/sage-devel/browse_thread/thread/f141bdaaebf4bcbf\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7372\n\n",
    "created_at": "2009-11-01T23:57:36Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix iterator for finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7372",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @aghitza

CC:  @malb ylchapuy

Keywords: finite field iterator


```
sage: K.<a>=GF(2^16)
sage: K.list()
...
TypeError: 'sage.rings.ring.FiniteFieldIterator' object is not iterable
```


See #7366 for smaller fields (givaro implementation), this is for fields as large as 2^16.

Discussion: http://groups.google.com/group/sage-devel/browse_thread/thread/f141bdaaebf4bcbf


Issue created by migration from https://trac.sagemath.org/ticket/7372





---

archive/issue_comments_061653.json:
```json
{
    "body": "Attachment [trac_7372_finite_field_iteration.patch](tarball://root/attachments/some-uuid/ticket7372/trac_7372_finite_field_iteration.patch) by @rbeezer created at 2009-11-01 23:59:29",
    "created_at": "2009-11-01T23:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7372#issuecomment-61653",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_7372_finite_field_iteration.patch](tarball://root/attachments/some-uuid/ticket7372/trac_7372_finite_field_iteration.patch) by @rbeezer created at 2009-11-01 23:59:29



---

archive/issue_comments_061654.json:
```json
{
    "body": "This is a dupe of #7370 although your doctest is better :)",
    "created_at": "2009-11-02T00:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7372#issuecomment-61654",
    "user": "https://github.com/malb"
}
```

This is a dupe of #7370 although your doctest is better :)



---

archive/issue_comments_061655.json:
```json
{
    "body": "OK, malb caught me in the act, and this is fixed.  See #7370.\n\nRelease manager - mark this obsolete.",
    "created_at": "2009-11-02T00:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7372#issuecomment-61655",
    "user": "https://github.com/rbeezer"
}
```

OK, malb caught me in the act, and this is fixed.  See #7370.

Release manager - mark this obsolete.



---

archive/issue_comments_061656.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-11-02T04:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7372#issuecomment-61656",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_017433.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-02T04:20:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7372",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7372#event-17433"
}
```



---

archive/issue_events_017434.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-02T04:20:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7372",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7372#event-17434"
}
```
