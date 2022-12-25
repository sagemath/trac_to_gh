# Issue 7691: Expect interfaces should not timeout

archive/issues_007691.json:
```json
{
    "body": "Assignee: @williamstein\n\nLong, long ago I randomly decided that the pexpect interfaces (to maxima, gp, etc.) should timeout if the subprocess takes more than 30 seconds to startup.  This is completely arbitrary, and really makes no sense, especially since randomly loaded systems (especially heavy NFS load) can easily and reasonably increase the startup time to > 30 seconds.  \n\nLet's change it so that there is *no* timeout.  If you type\n\n```\n sage: gp('2+2')\n```\nthen Sage should simply wait until gp starts, no matter how long that takes.   That's just like typing \n\n```\n bash$ gp\n```\non the command line and the command line not killing gp because it takes > 30 seconds to start.\n\nThis will also sort out many doctest issues on highly loaded machines. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7691\n\n",
    "created_at": "2009-12-15T19:46:14Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Expect interfaces should not timeout",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7691",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Long, long ago I randomly decided that the pexpect interfaces (to maxima, gp, etc.) should timeout if the subprocess takes more than 30 seconds to startup.  This is completely arbitrary, and really makes no sense, especially since randomly loaded systems (especially heavy NFS load) can easily and reasonably increase the startup time to > 30 seconds.  

Let's change it so that there is *no* timeout.  If you type

```
 sage: gp('2+2')
```
then Sage should simply wait until gp starts, no matter how long that takes.   That's just like typing 

```
 bash$ gp
```
on the command line and the command line not killing gp because it takes > 30 seconds to start.

This will also sort out many doctest issues on highly loaded machines. 

Issue created by migration from https://trac.sagemath.org/ticket/7691





---

archive/issue_comments_065870.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-15T21:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7691#issuecomment-65870",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065871.json:
```json
{
    "body": "Here is the patch:\n\n    http://sage.math.washington.edu/home/wstein/patches/trac_7691.patch",
    "created_at": "2009-12-15T21:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7691#issuecomment-65871",
    "user": "https://github.com/williamstein"
}
```

Here is the patch:

    http://sage.math.washington.edu/home/wstein/patches/trac_7691.patch



---

archive/issue_comments_065872.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-16T02:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7691#issuecomment-65872",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_065873.json:
```json
{
    "body": "Attachment [trac_7691.patch](tarball://root/attachments/some-uuid/ticket7691/trac_7691.patch) by @mwhansen created at 2009-12-16 02:28:54",
    "created_at": "2009-12-16T02:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7691#issuecomment-65873",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7691.patch](tarball://root/attachments/some-uuid/ticket7691/trac_7691.patch) by @mwhansen created at 2009-12-16 02:28:54



---

archive/issue_events_018378.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-16T02:28:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7691",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7691#event-18378"
}
```



---

archive/issue_events_018379.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:43:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7691",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7691#event-18379"
}
```
