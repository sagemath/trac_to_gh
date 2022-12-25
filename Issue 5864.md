# Issue 5864: Correctly inherit build environment in eclib

archive/issues_005864.json:
```json
{
    "body": "Assignee: mabshoff\n\nChange 'make' to ${MAKE} - is the recommended way to recursively invoke make to ensure that the subordinate make is the same as the parent make (and also ensures that the two make instances will communicate on things like '-jX').\n\nExplicitly use gmake instead of make on FreeBSD.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5864\n\n",
    "created_at": "2009-04-23T06:35:45Z",
    "labels": [
        "component: porting: bsd",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Correctly inherit build environment in eclib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5864",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: mabshoff

Change 'make' to ${MAKE} - is the recommended way to recursively invoke make to ensure that the subordinate make is the same as the parent make (and also ensures that the two make instances will communicate on things like '-jX').

Explicitly use gmake instead of make on FreeBSD.

Issue created by migration from https://trac.sagemath.org/ticket/5864





---

archive/issue_comments_046237.json:
```json
{
    "body": "Attachment [eclib-20080310.p7.patch](tarball://root/attachments/some-uuid/ticket5864/eclib-20080310.p7.patch) by @peterjeremy created at 2009-04-23 06:47:10",
    "created_at": "2009-04-23T06:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5864#issuecomment-46237",
    "user": "https://github.com/peterjeremy"
}
```

Attachment [eclib-20080310.p7.patch](tarball://root/attachments/some-uuid/ticket5864/eclib-20080310.p7.patch) by @peterjeremy created at 2009-04-23 06:47:10



---

archive/issue_comments_046238.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T07:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5864#issuecomment-46238",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046239.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T07:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5864#issuecomment-46239",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046240.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/eclib-20080310.p8.spkg",
    "created_at": "2009-06-20T07:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5864#issuecomment-46240",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

The spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/eclib-20080310.p8.spkg



---

archive/issue_comments_046241.json:
```json
{
    "body": "I am confused here.  I already have a .p8 version, dated 2009-01-07.  Now you have created a new .p8 which must be different!\n\nChecking the SPKG.txt in my p8 I see this entry:\n### eclib-20080310.p8 (John Cremona, January 6th, 2009)\n* Change to debugging output in procs/p2points.cc (not relevant for Sage)\n* Change to pdivs() in procs/marith.cc (not relevant for Sage)\n\nI suggest that we syncronise, otherwise I will get even more confused.  For a start, this ticket should have had me in its CC list!  I don't see how I can be expected to be responsible for this spkg if people are changing it without even telling me!\n\nHence I have changed this back to \"needs work\".",
    "created_at": "2009-06-20T14:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5864#issuecomment-46241",
    "user": "https://github.com/JohnCremona"
}
```

I am confused here.  I already have a .p8 version, dated 2009-01-07.  Now you have created a new .p8 which must be different!

Checking the SPKG.txt in my p8 I see this entry:
### eclib-20080310.p8 (John Cremona, January 6th, 2009)
* Change to debugging output in procs/p2points.cc (not relevant for Sage)
* Change to pdivs() in procs/marith.cc (not relevant for Sage)

I suggest that we syncronise, otherwise I will get even more confused.  For a start, this ticket should have had me in its CC list!  I don't see how I can be expected to be responsible for this spkg if people are changing it without even telling me!

Hence I have changed this back to "needs work".



---

archive/issue_comments_046242.json:
```json
{
    "body": "This ticket is no longer needed with eclib-20080310.p10",
    "created_at": "2010-07-13T20:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5864#issuecomment-46242",
    "user": "https://github.com/peterjeremy"
}
```

This ticket is no longer needed with eclib-20080310.p10



---

archive/issue_comments_046243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-13T20:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5864#issuecomment-46243",
    "user": "https://github.com/peterjeremy"
}
```

Resolution: fixed
