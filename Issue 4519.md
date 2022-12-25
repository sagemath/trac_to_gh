# Issue 4519: [with patch, needs review] problem with build code

archive/issues_004519.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThere's a problem with the build code that was first introduced by #4377. Here's an example of how to see this: pick your favorite `.pyx` file (I was using `gen.pyx`), and break it -- just make some syntax error, and save. Now do a `sage -br` -- you see that it says there's an error ... but then it still runs sage! Oops.\n\nThe underlying problem is that if we pass back a different exit code (in the case I was running into, it was 256), the `python setup.py install` still returns 0. \n\nThe attached patch fixes the trouble. Is there a way to test something like this?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4519\n\n",
    "created_at": "2008-11-14T06:26:15Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] problem with build code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4519",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

There's a problem with the build code that was first introduced by #4377. Here's an example of how to see this: pick your favorite `.pyx` file (I was using `gen.pyx`), and break it -- just make some syntax error, and save. Now do a `sage -br` -- you see that it says there's an error ... but then it still runs sage! Oops.

The underlying problem is that if we pass back a different exit code (in the case I was running into, it was 256), the `python setup.py install` still returns 0. 

The attached patch fixes the trouble. Is there a way to test something like this?

Issue created by migration from https://trac.sagemath.org/ticket/4519





---

archive/issue_comments_033475.json:
```json
{
    "body": "Attachment [trac-4519.patch](tarball://root/attachments/some-uuid/ticket4519/trac-4519.patch) by @craigcitro created at 2008-11-14 06:26:54",
    "created_at": "2008-11-14T06:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4519#issuecomment-33475",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4519.patch](tarball://root/attachments/some-uuid/ticket4519/trac-4519.patch) by @craigcitro created at 2008-11-14 06:26:54



---

archive/issue_comments_033476.json:
```json
{
    "body": "Hmmm,\n\nit seems to me that somewhere I have read that only the lowest 8 bit of \"such\" return values would be taken into account. I don't remember a reference however, or in what precise context --- bash? posix? ...\n\nBut that \"256\" suddenly becomes \"0\" would support this faint memory of mine.\n\nBe it as it be, I just tested (with 3.2.rc0) that this patch does indeed fix the problem described (which is there without the patch); and the nature of the patch is local enough one can be pretty sure that nothing else does break.\n\nPositive review from my side.\n\nThe only thing I don't agree with is the original classification as \"blocker\" --- nothing really bad happens, because the old \"gen.so\" or \"gen.dylib\" or whatever compiled python extension from the last successful run is still there, and accessed by the wrongly started Sage session. And the error message is displayed prominently enough.",
    "created_at": "2008-11-14T20:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4519#issuecomment-33476",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hmmm,

it seems to me that somewhere I have read that only the lowest 8 bit of "such" return values would be taken into account. I don't remember a reference however, or in what precise context --- bash? posix? ...

But that "256" suddenly becomes "0" would support this faint memory of mine.

Be it as it be, I just tested (with 3.2.rc0) that this patch does indeed fix the problem described (which is there without the patch); and the nature of the patch is local enough one can be pretty sure that nothing else does break.

Positive review from my side.

The only thing I don't agree with is the original classification as "blocker" --- nothing really bad happens, because the old "gen.so" or "gen.dylib" or whatever compiled python extension from the last successful run is still there, and accessed by the wrongly started Sage session. And the error message is displayed prominently enough.



---

archive/issue_comments_033477.json:
```json
{
    "body": "This is definitely a blocker plain and simple since one does not check any large compilation, i.e. a `-ba` for errors. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T20:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4519#issuecomment-33477",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is definitely a blocker plain and simple since one does not check any large compilation, i.e. a `-ba` for errors. 

Cheers,

Michael



---

archive/issue_comments_033478.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-14T20:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4519#issuecomment-33478",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_events_004764.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-15T05:03:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4519",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4519#event-4764"
}
```



---

archive/issue_comments_033479.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-15T05:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4519#issuecomment-33479",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_comments_033480.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T05:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4519#issuecomment-33480",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
