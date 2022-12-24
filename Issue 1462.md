# Issue 1462: speed up "sage -b" -- don't do anything cython stuff if no .pyx, .pxd, or .pxi file changes (not a dupe!)

archive/issues_001462.json:
```json
{
    "body": "Assignee: was\n\nThis is a very very simple patch that makes it so \n\n  sage -b\n\ntakes 1 seconds (on my mac laptop) instead of 10 seconds, so long as \nno Cython code has changed.  Otherwise it works just as before.\n\nThis is orthogonal to Bobby Moretti's patch for caching Cython dependencies.\nBoth should be used.\n\nThis is much simpler -- all it does is -- in 1/100th of a second (or so) compute a hash got from all cython-related files in the repo, and if that hasn't changed from last time, skip all cython-ing of code. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1462\n\n",
    "created_at": "2007-12-11T20:17:38Z",
    "labels": [
        "user interface",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "speed up \"sage -b\" -- don't do anything cython stuff if no .pyx, .pxd, or .pxi file changes (not a dupe!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1462",
    "user": "was"
}
```
Assignee: was

This is a very very simple patch that makes it so 

  sage -b

takes 1 seconds (on my mac laptop) instead of 10 seconds, so long as 
no Cython code has changed.  Otherwise it works just as before.

This is orthogonal to Bobby Moretti's patch for caching Cython dependencies.
Both should be used.

This is much simpler -- all it does is -- in 1/100th of a second (or so) compute a hash got from all cython-related files in the repo, and if that hasn't changed from last time, skip all cython-ing of code. 



Issue created by migration from https://trac.sagemath.org/ticket/1462





---

archive/issue_comments_009415.json:
```json
{
    "body": "Attachment [trac-1462.patch](tarball://root/attachments/some-uuid/ticket1462/trac-1462.patch) by was created at 2007-12-11 20:18:09",
    "created_at": "2007-12-11T20:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1462#issuecomment-9415",
    "user": "was"
}
```

Attachment [trac-1462.patch](tarball://root/attachments/some-uuid/ticket1462/trac-1462.patch) by was created at 2007-12-11 20:18:09



---

archive/issue_comments_009416.json:
```json
{
    "body": "I applied this for 2.9.",
    "created_at": "2007-12-12T15:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1462#issuecomment-9416",
    "user": "was"
}
```

I applied this for 2.9.



---

archive/issue_comments_009417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-12T15:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1462#issuecomment-9417",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_009418.json:
```json
{
    "body": "Attachment [trac-1462-part2.patch](tarball://root/attachments/some-uuid/ticket1462/trac-1462-part2.patch) by was created at 2007-12-13 23:03:19",
    "created_at": "2007-12-13T23:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1462",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1462#issuecomment-9418",
    "user": "was"
}
```

Attachment [trac-1462-part2.patch](tarball://root/attachments/some-uuid/ticket1462/trac-1462-part2.patch) by was created at 2007-12-13 23:03:19
