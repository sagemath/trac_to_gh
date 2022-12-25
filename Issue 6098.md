# Issue 6098: 3d bezier path plotting

archive/issues_006098.json:
```json
{
    "body": "Assignee: ekirkman\n\nCC:  @rlmill @mwhansen\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6098\n\n",
    "created_at": "2009-05-21T02:19:19Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "3d bezier path plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6098",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```
Assignee: ekirkman

CC:  @rlmill @mwhansen



Issue created by migration from https://trac.sagemath.org/ticket/6098





---

archive/issue_comments_048534.json:
```json
{
    "body": "This picture was created with input sage: bezier3d([This is the Trac macro ** that was inherited from the migration called with arguments (0,0,0),)](https://trac.sagemath.org/wiki/WikiMacros#-macro))",
    "created_at": "2009-05-21T02:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6098#issuecomment-48534",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

This picture was created with input sage: bezier3d([This is the Trac macro ** that was inherited from the migration called with arguments (0,0,0),)](https://trac.sagemath.org/wiki/WikiMacros#-macro))



---

archive/issue_comments_048535.json:
```json
{
    "body": "Attachment [trac6098_bezier3d.patch](tarball://root/attachments/some-uuid/ticket6098/trac6098_bezier3d.patch) by @rlmill created at 2009-05-21 18:59:58\n\nReferee edit",
    "created_at": "2009-05-21T18:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6098#issuecomment-48535",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac6098_bezier3d.patch](tarball://root/attachments/some-uuid/ticket6098/trac6098_bezier3d.patch) by @rlmill created at 2009-05-21 18:59:58

Referee edit



---

archive/issue_comments_048536.json:
```json
{
    "body": "Unfortunately, against 4.0.2.alpha0:\n\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t -long devel/sage/sage/plot/plot3d/shapes2.py # 4 doctests failed\n        sage -t -long devel/sage/sage/plot/plot3d/shapes2.py # 4 doctests failed\n        sage -t -long devel/sage/sage/plot/bezier_path.py # 2 doctests failed\n----------------------------------------------------------------------\n```\n",
    "created_at": "2009-06-13T21:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6098#issuecomment-48536",
    "user": "https://github.com/ncalexan"
}
```

Unfortunately, against 4.0.2.alpha0:


```
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/sage/plot/plot3d/shapes2.py # 4 doctests failed
        sage -t -long devel/sage/sage/plot/plot3d/shapes2.py # 4 doctests failed
        sage -t -long devel/sage/sage/plot/bezier_path.py # 2 doctests failed
----------------------------------------------------------------------
```




---

archive/issue_comments_048537.json:
```json
{
    "body": "Apply only this patch",
    "created_at": "2009-07-13T21:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6098#issuecomment-48537",
    "user": "https://github.com/rlmill"
}
```

Apply only this patch



---

archive/issue_comments_048538.json:
```json
{
    "body": "Attachment [trac_6098-rebased.patch](tarball://root/attachments/some-uuid/ticket6098/trac_6098-rebased.patch) by @rlmill created at 2009-07-13 21:12:15\n\nIt was completely trivial to get this patch working again. I did the work while Emily watched over my shoulder. If one positive review isn't enough, then you have two! :)",
    "created_at": "2009-07-13T21:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6098#issuecomment-48538",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6098-rebased.patch](tarball://root/attachments/some-uuid/ticket6098/trac_6098-rebased.patch) by @rlmill created at 2009-07-13 21:12:15

It was completely trivial to get this patch working again. I did the work while Emily watched over my shoulder. If one positive review isn't enough, then you have two! :)



---

archive/issue_comments_048539.json:
```json
{
    "body": "Oops... ignore the patch `trac_6098-reviewer.patch`. Just to let people know, only the patch `trac_6098-rebased.patch` has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T16:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6098#issuecomment-48539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Oops... ignore the patch `trac_6098-reviewer.patch`. Just to let people know, only the patch `trac_6098-rebased.patch` has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_events_006349.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-07-16T21:18:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6098#event-6349"
}
```



---

archive/issue_comments_048540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6098#issuecomment-48540",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
