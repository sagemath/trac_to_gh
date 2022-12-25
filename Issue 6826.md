# Issue 6826: [with patch, needs review] magma_free interface is broken

archive/issues_006826.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nKeywords: magma free internet interface\n\nThe magma free interface has changed slightly.  The attached patch updates the interface.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6826\n\n",
    "created_at": "2009-08-26T01:16:34Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] magma_free interface is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6826",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @williamstein

Keywords: magma free internet interface

The magma free interface has changed slightly.  The attached patch updates the interface.

Issue created by migration from https://trac.sagemath.org/ticket/6826





---

archive/issue_comments_056202.json:
```json
{
    "body": "Attachment [trac_6826-magma_free.patch](tarball://root/attachments/some-uuid/ticket6826/trac_6826-magma_free.patch) by @ncalexan created at 2009-08-26 01:17:41",
    "created_at": "2009-08-26T01:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6826#issuecomment-56202",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6826-magma_free.patch](tarball://root/attachments/some-uuid/ticket6826/trac_6826-magma_free.patch) by @ncalexan created at 2009-08-26 01:17:41



---

archive/issue_comments_056203.json:
```json
{
    "body": "It looks like it is still \"input\" rather than \"commands\" when looking at the source for http://magma.maths.usyd.edu.au/calc/.",
    "created_at": "2009-09-01T22:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6826#issuecomment-56203",
    "user": "https://github.com/mwhansen"
}
```

It looks like it is still "input" rather than "commands" when looking at the source for http://magma.maths.usyd.edu.au/calc/.



---

archive/issue_comments_056204.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> It looks like it is still \"input\" rather than \"commands\" when looking at the source for http://magma.maths.usyd.edu.au/calc/.\n\nYep, it did to me too.  All I know is that it didn't work before the patch, and it now works with the patch.  That's the important part -- is that the same for you?",
    "created_at": "2009-09-02T16:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6826#issuecomment-56204",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:1 mhansen]:
> It looks like it is still "input" rather than "commands" when looking at the source for http://magma.maths.usyd.edu.au/calc/.

Yep, it did to me too.  All I know is that it didn't work before the patch, and it now works with the patch.  That's the important part -- is that the same for you?



---

archive/issue_comments_056205.json:
```json
{
    "body": "It works both before and after for me.  Maybe the test input that I'm using is too simple.",
    "created_at": "2009-09-02T19:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6826#issuecomment-56205",
    "user": "https://github.com/mwhansen"
}
```

It works both before and after for me.  Maybe the test input that I'm using is too simple.



---

archive/issue_comments_056206.json:
```json
{
    "body": "It's id=\"input\" name=\"commands\". \n\nIt still works for me too, but this should probably be fixed for consistencies sake.",
    "created_at": "2009-09-22T22:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6826#issuecomment-56206",
    "user": "https://github.com/robertwb"
}
```

It's id="input" name="commands". 

It still works for me too, but this should probably be fixed for consistencies sake.



---

archive/issue_events_016078.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-24T06:18:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6826#event-16078"
}
```



---

archive/issue_comments_056207.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T06:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6826#issuecomment-56207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056208.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6826",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6826#issuecomment-56208",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
