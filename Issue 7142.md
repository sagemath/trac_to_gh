# Issue 7142: We must check if the version of 'tar' found is gnu tar

archive/issues_007142.json:
```json
{
    "body": "Assignee: tbd\n\nSage needs GNU tar (at least I know the Sun tar is not suitable), so we need to check that 'tar' is in fact gnu tar, and not some other version of tar. \n\nOn HP-UX there does not appear to be a version of GNU tar on the system. With Solaris, there  is a version called 'gtar' at /usr/sfw/bin/gtar. \n\nOne way or another, we need to make sure that the tar that Sage files is the GNU version. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7142\n\n",
    "created_at": "2009-10-06T17:03:53Z",
    "labels": [
        "build",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "We must check if the version of 'tar' found is gnu tar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7142",
    "user": "drkirkby"
}
```
Assignee: tbd

Sage needs GNU tar (at least I know the Sun tar is not suitable), so we need to check that 'tar' is in fact gnu tar, and not some other version of tar. 

On HP-UX there does not appear to be a version of GNU tar on the system. With Solaris, there  is a version called 'gtar' at /usr/sfw/bin/gtar. 

One way or another, we need to make sure that the tar that Sage files is the GNU version. 

Issue created by migration from https://trac.sagemath.org/ticket/7142





---

archive/issue_comments_059183.json:
```json
{
    "body": "Possibly a better solution would be to write tar files in a more portable format. It would appear the GNU tar developers are going to change to a POSIX format for the default format of GNU tar, rather than their current 'gnu' format. See\n\n[http://groups.google.com/group/sage-devel/browse_thread/thread/c1d1f27d455e3c72#](http://groups.google.com/group/sage-devel/browse_thread/thread/c1d1f27d455e3c72#)\n\nHowever, at this point in time, I'm not aware of whether that will solve the problem. It may be on some platforms the 'tar' program is just not suitable and so insisting on the use of GNU tar will be necessary.",
    "created_at": "2009-11-02T13:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7142#issuecomment-59183",
    "user": "drkirkby"
}
```

Possibly a better solution would be to write tar files in a more portable format. It would appear the GNU tar developers are going to change to a POSIX format for the default format of GNU tar, rather than their current 'gnu' format. See

[http://groups.google.com/group/sage-devel/browse_thread/thread/c1d1f27d455e3c72#](http://groups.google.com/group/sage-devel/browse_thread/thread/c1d1f27d455e3c72#)

However, at this point in time, I'm not aware of whether that will solve the problem. It may be on some platforms the 'tar' program is just not suitable and so insisting on the use of GNU tar will be necessary.



---

archive/issue_comments_059184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-20T06:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7142#issuecomment-59184",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059185.json:
```json
{
    "body": "Fixed by #7352",
    "created_at": "2009-11-20T06:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7142",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7142#issuecomment-59185",
    "user": "mhansen"
}
```

Fixed by #7352
