# Issue 5255: [with patch, positive review] Deprecating the use of iterator in CombinatorialClass

archive/issues_005255.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: __iter__, iterator\n\nRight now, when one want's to iterate along a combinatorial class C, there is at least three solution:\n\n```\n[ x for x in C.iterator() ]\n[ x for x in C.__iter__() ]\n[ x for x in C ]\n```\nThere is no semantic differences beetween these three and there should not be any mesurable speedup for any. The latter solution is sintactically better and perfectly python/Sage idiomatic. So the goal of this patch is to mark the use of `C.iterator()` as deprecated *ASAP* (there are already 96 definition and something close to 400 uses in sage-combinat). \n\nA subsequent series of patches should apply this rule trough all combinatorial classes. Right now to avoid breaking doctests the raising of the deprecation warning is commented out. I'll uncomment it after the series of patches. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5255\n\n",
    "closed_at": "2009-02-15T08:04:53Z",
    "created_at": "2009-02-13T16:16:17Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] Deprecating the use of iterator in CombinatorialClass",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5255",
    "user": "https://github.com/hivert"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: __iter__, iterator

Right now, when one want's to iterate along a combinatorial class C, there is at least three solution:

```
[ x for x in C.iterator() ]
[ x for x in C.__iter__() ]
[ x for x in C ]
```
There is no semantic differences beetween these three and there should not be any mesurable speedup for any. The latter solution is sintactically better and perfectly python/Sage idiomatic. So the goal of this patch is to mark the use of `C.iterator()` as deprecated *ASAP* (there are already 96 definition and something close to 400 uses in sage-combinat). 

A subsequent series of patches should apply this rule trough all combinatorial classes. Right now to avoid breaking doctests the raising of the deprecation warning is commented out. I'll uncomment it after the series of patches. 

Issue created by migration from https://trac.sagemath.org/ticket/5255





---

archive/issue_comments_040245.json:
```json
{
    "body": "Patch proposal",
    "created_at": "2009-02-13T16:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40245",
    "user": "https://github.com/hivert"
}
```

Patch proposal



---

archive/issue_events_012204.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2009-02-13T23:34:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5255#event-12204"
}
```



---

archive/issue_comments_040246.json:
```json
{
    "body": "Attachment [combinatorialclass__iter_-5255-submitted.patch](tarball://root/attachments/some-uuid/ticket5255/combinatorialclass__iter_-5255-submitted.patch) by @hivert created at 2009-02-13 23:34:01",
    "created_at": "2009-02-13T23:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40246",
    "user": "https://github.com/hivert"
}
```

Attachment [combinatorialclass__iter_-5255-submitted.patch](tarball://root/attachments/some-uuid/ticket5255/combinatorialclass__iter_-5255-submitted.patch) by @hivert created at 2009-02-13 23:34:01



---

archive/issue_comments_040247.json:
```json
{
    "body": "I think\n\n```\nit = C.__iter__() # indirect doctest \n```\n\nshould be \n\n```\nit = iter(C) # indirect doctest \n```\n\ni.e. one should avoid calling `__foo__` functions directly.",
    "created_at": "2009-02-14T17:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40247",
    "user": "https://github.com/malb"
}
```

I think

```
it = C.__iter__() # indirect doctest 
```

should be 

```
it = iter(C) # indirect doctest 
```

i.e. one should avoid calling `__foo__` functions directly.



---

archive/issue_comments_040248.json:
```json
{
    "body": "Attachment [trac_5255-review.patch](tarball://root/attachments/some-uuid/ticket5255/trac_5255-review.patch) by @mwhansen created at 2009-02-14 22:40:44\n\nThe original patch looks good.  I made a few updates in the review patch.",
    "created_at": "2009-02-14T22:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40248",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5255-review.patch](tarball://root/attachments/some-uuid/ticket5255/trac_5255-review.patch) by @mwhansen created at 2009-02-14 22:40:44

The original patch looks good.  I made a few updates in the review patch.



---

archive/issue_comments_040249.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> The original patch looks good.  I made a few updates in the review patch.\n\n\nThe review patch looks good to me.",
    "created_at": "2009-02-14T23:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40249",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:3 mhansen]:
> The original patch looks good.  I made a few updates in the review patch.


The review patch looks good to me.



---

archive/issue_comments_040250.json:
```json
{
    "body": "Apply both patches.",
    "created_at": "2009-02-15T00:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40250",
    "user": "https://github.com/mwhansen"
}
```

Apply both patches.



---

archive/issue_comments_040251.json:
```json
{
    "body": "Merged both patches in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T08:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040252.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-15T08:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5255#issuecomment-40252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012205.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-15T08:04:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5255",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5255#event-12205"
}
```
