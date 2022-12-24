# Issue 2712: Add 'scalar_part()' and other methods for quaternion elements

archive/issues_002712.json:
```json
{
    "body": "Assignee: mabshoff\n\nFollowing John Cremona's suggestion, I've added 'scalar_part()\", 'pure_part()', and 'is_pure()' for quaternions.\n\nThe method 'is_scalar()' is already implemented, so in a sense, this completes the picture.  This was spurred on by a request on the support list (from Chris Godsil).\n\nThe implementation assumes characteristic not 2, which is OK since it's implicitly or explicitly assumed throughout the quaternion code.\n\nI think the terms 'scalar' and 'pure', for a value in the base ring and having trace 0 (and being non-zero), respectively, is fairly standard.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2712\n\n",
    "created_at": "2008-03-28T21:39:20Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "title": "Add 'scalar_part()' and other methods for quaternion elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2712",
    "user": "justin"
}
```
Assignee: mabshoff

Following John Cremona's suggestion, I've added 'scalar_part()", 'pure_part()', and 'is_pure()' for quaternions.

The method 'is_scalar()' is already implemented, so in a sense, this completes the picture.  This was spurred on by a request on the support list (from Chris Godsil).

The implementation assumes characteristic not 2, which is OK since it's implicitly or explicitly assumed throughout the quaternion code.

I think the terms 'scalar' and 'pure', for a value in the base ring and having trace 0 (and being non-zero), respectively, is fairly standard.




Issue created by migration from https://trac.sagemath.org/ticket/2712





---

archive/issue_comments_018694.json:
```json
{
    "body": "Adding patch.  The patch includes doctests, and the file passes the \"-t\" test.  The resulting file has 57% coverage (I did not add tests where there were none).\n\nThe patch is against a clean 2.10.4 tree.",
    "created_at": "2008-03-28T21:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18694",
    "user": "justin"
}
```

Adding patch.  The patch includes doctests, and the file passes the "-t" test.  The resulting file has 57% coverage (I did not add tests where there were none).

The patch is against a clean 2.10.4 tree.



---

archive/issue_comments_018695.json:
```json
{
    "body": "Attachment [Trac2712.patch](tarball://root/attachments/some-uuid/ticket2712/Trac2712.patch) by justin created at 2008-03-28 23:04:38\n\nPatch implementing the element methods described above.",
    "created_at": "2008-03-28T23:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18695",
    "user": "justin"
}
```

Attachment [Trac2712.patch](tarball://root/attachments/some-uuid/ticket2712/Trac2712.patch) by justin created at 2008-03-28 23:04:38

Patch implementing the element methods described above.



---

archive/issue_comments_018696.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-29T00:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18696",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_018697.json:
```json
{
    "body": "Changing component from Cygwin to misc.",
    "created_at": "2008-03-29T00:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18697",
    "user": "mabshoff"
}
```

Changing component from Cygwin to misc.



---

archive/issue_comments_018698.json:
```json
{
    "body": "Changing assignee from mabshoff to cwitty.",
    "created_at": "2008-03-29T00:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18698",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to cwitty.



---

archive/issue_comments_018699.json:
```json
{
    "body": "Not sure about the component - feel free to reclassify.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T00:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18699",
    "user": "mabshoff"
}
```

Not sure about the component - feel free to reclassify.

Cheers,

Michael



---

archive/issue_comments_018700.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-29T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18700",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018701.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T00:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2712",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2712#issuecomment-18701",
    "user": "mabshoff"
}
```

Resolution: fixed
