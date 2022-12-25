# Issue 7244: Implement dicyclic groups as permutation groups

archive/issues_007244.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @wdjoyner\n\nKeywords: dicyclic\n\nThe dicyclic groups are nonabelian groups of order 4n, n> 2.\n\nWith these added, it will be possible to easily construct every subgroup of order 8 and 12 as a permutation group, and then every subgroup of size 15 or less will be easy to construct.\n\nDiscussion originated at:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/df6697653527006c\n\nIssue created by migration from https://trac.sagemath.org/ticket/7244\n\n",
    "created_at": "2009-10-19T04:48:24Z",
    "labels": [
        "component: group theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Implement dicyclic groups as permutation groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7244",
    "user": "https://github.com/rbeezer"
}
```
Assignee: joyner

CC:  @wdjoyner

Keywords: dicyclic

The dicyclic groups are nonabelian groups of order 4n, n> 2.

With these added, it will be possible to easily construct every subgroup of order 8 and 12 as a permutation group, and then every subgroup of size 15 or less will be easy to construct.

Discussion originated at:

http://groups.google.com/group/sage-devel/browse_thread/thread/df6697653527006c

Issue created by migration from https://trac.sagemath.org/ticket/7244





---

archive/issue_comments_060033.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-19T05:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60033",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060034.json:
```json
{
    "body": "Dicyclic groups are implemented as a new class in the named permutation groups collection.\n\nThe \"quaternion group\" is implemented by simply forming the dicyclic group of order 8.  The intent is that this small group is a good one for students to contrast with the other four groups of this order.",
    "created_at": "2009-10-19T05:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60034",
    "user": "https://github.com/rbeezer"
}
```

Dicyclic groups are implemented as a new class in the named permutation groups collection.

The "quaternion group" is implemented by simply forming the dicyclic group of order 8.  The intent is that this small group is a good one for students to contrast with the other four groups of this order.



---

archive/issue_comments_060035.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-21T16:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60035",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060036.json:
```json
{
    "body": "There's a typo in line 495, and these groups are sufficiently unusual that some reference to online documentation of them would be useful.   I realize these are fairly trivial comments, my apologies.",
    "created_at": "2009-10-21T16:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60036",
    "user": "https://github.com/kcrisman"
}
```

There's a typo in line 495, and these groups are sufficiently unusual that some reference to online documentation of them would be useful.   I realize these are fairly trivial comments, my apologies.



---

archive/issue_comments_060037.json:
```json
{
    "body": "Attachment [trac_7244_dicyclic_groups.patch](tarball://root/attachments/some-uuid/ticket7244/trac_7244_dicyclic_groups.patch) by @rbeezer created at 2009-10-22 02:34:57",
    "created_at": "2009-10-22T02:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60037",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_7244_dicyclic_groups.patch](tarball://root/attachments/some-uuid/ticket7244/trac_7244_dicyclic_groups.patch) by @rbeezer created at 2009-10-22 02:34:57



---

archive/issue_comments_060038.json:
```json
{
    "body": "Karl-Dieter,\n\nThanks for the comments.  I've replaced the patch with a new one addressing your comments.\n\nIf you test building the docs will you see if you get the warning\n\n```\n/doc/en/reference/sage/groups/perm_gps/permgroup_named.rst:: document isn't included in any toctree\n```\n\nThis file really needs a workover, and probably shouldn't be in the docs as-is, but I'm not sure if the warning was there before, or if I've induced it.\n\nThanks,\nRob",
    "created_at": "2009-10-22T02:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60038",
    "user": "https://github.com/rbeezer"
}
```

Karl-Dieter,

Thanks for the comments.  I've replaced the patch with a new one addressing your comments.

If you test building the docs will you see if you get the warning

```
/doc/en/reference/sage/groups/perm_gps/permgroup_named.rst:: document isn't included in any toctree
```

This file really needs a workover, and probably shouldn't be in the docs as-is, but I'm not sure if the warning was there before, or if I've induced it.

Thanks,
Rob



---

archive/issue_comments_060039.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-22T02:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60039",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060040.json:
```json
{
    "body": "passes sage -testall (on ubuntu 9.04 32 but running under vmware under mac 10.6) and does what it claims.\n\nThanks Rob!",
    "created_at": "2009-10-25T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60040",
    "user": "https://github.com/wdjoyner"
}
```

passes sage -testall (on ubuntu 9.04 32 but running under vmware under mac 10.6) and does what it claims.

Thanks Rob!



---

archive/issue_comments_060041.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-25T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60041",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060042.json:
```json
{
    "body": "Release manager:  please obsolete #7151 when this gets merged.  Thanks!",
    "created_at": "2009-10-26T04:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60042",
    "user": "https://github.com/rbeezer"
}
```

Release manager:  please obsolete #7151 when this gets merged.  Thanks!



---

archive/issue_comments_060043.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7244#issuecomment-60043",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017154.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T16:37:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7244",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7244#event-17154"
}
```
