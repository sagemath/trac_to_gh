# Issue 2712: [with patch, positive review] Add 'scalar_part()' and other methods for quaternion elements

archive/issues_002712.json:
```json
{
    "body": "Assignee: cwitty\n\nFollowing John Cremona's suggestion, I've added 'scalar_part()\", 'pure_part()', and 'is_pure()' for quaternions.\n\nThe method 'is_scalar()' is already implemented, so in a sense, this completes the picture.  This was spurred on by a request on the support list (from Chris Godsil).\n\nThe implementation assumes characteristic not 2, which is OK since it's implicitly or explicitly assumed throughout the quaternion code.\n\nI think the terms 'scalar' and 'pure', for a value in the base ring and having trace 0 (and being non-zero), respectively, is fairly standard.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2712\n\n",
    "closed_at": "2008-03-29T00:44:53Z",
    "created_at": "2008-03-28T21:39:20Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, positive review] Add 'scalar_part()' and other methods for quaternion elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2712",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: cwitty

Following John Cremona's suggestion, I've added 'scalar_part()", 'pure_part()', and 'is_pure()' for quaternions.

The method 'is_scalar()' is already implemented, so in a sense, this completes the picture.  This was spurred on by a request on the support list (from Chris Godsil).

The implementation assumes characteristic not 2, which is OK since it's implicitly or explicitly assumed throughout the quaternion code.

I think the terms 'scalar' and 'pure', for a value in the base ring and having trace 0 (and being non-zero), respectively, is fairly standard.




Issue created by migration from https://trac.sagemath.org/ticket/2712





---

archive/issue_comments_018655.json:
```json
{
    "body": "Adding patch.  The patch includes doctests, and the file passes the \"-t\" test.  The resulting file has 57% coverage (I did not add tests where there were none).\n\nThe patch is against a clean 2.10.4 tree.",
    "created_at": "2008-03-28T21:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18655",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Adding patch.  The patch includes doctests, and the file passes the "-t" test.  The resulting file has 57% coverage (I did not add tests where there were none).

The patch is against a clean 2.10.4 tree.



---

archive/issue_comments_018656.json:
```json
{
    "body": "Attachment [Trac2712.patch](tarball://root/attachments/some-uuid/ticket2712/Trac2712.patch) by justin created at 2008-03-28 23:04:38\n\nPatch implementing the element methods described above.",
    "created_at": "2008-03-28T23:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18656",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Attachment [Trac2712.patch](tarball://root/attachments/some-uuid/ticket2712/Trac2712.patch) by justin created at 2008-03-28 23:04:38

Patch implementing the element methods described above.



---

archive/issue_comments_018657.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-29T00:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18657",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_006333.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T00:11:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2712#event-6333"
}
```



---

archive/issue_comments_018658.json:
```json
{
    "body": "Changing component from Cygwin to misc.",
    "created_at": "2008-03-29T00:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18658",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from Cygwin to misc.



---

archive/issue_comments_018659.json:
```json
{
    "body": "Changing assignee from mabshoff to cwitty.",
    "created_at": "2008-03-29T00:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18659",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to cwitty.



---

archive/issue_comments_018660.json:
```json
{
    "body": "Not sure about the component - feel free to reclassify.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T00:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Not sure about the component - feel free to reclassify.

Cheers,

Michael



---

archive/issue_events_006334.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T00:44:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2712#event-6334"
}
```



---

archive/issue_comments_018661.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-29T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18661",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018662.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18662",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
