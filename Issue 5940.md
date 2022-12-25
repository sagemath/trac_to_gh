# Issue 5940: graph theory -- bug in is_circular_planar

archive/issues_005940.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\nsage: g = graphs.KrackhardtKiteGraph()\nsage: g.is_circular_planar()\nTraceback...\nIndexError: list index out of range\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5940\n\n",
    "created_at": "2009-04-29T17:03:47Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "graph theory -- bug in is_circular_planar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5940",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill


```
sage: g = graphs.KrackhardtKiteGraph()
sage: g.is_circular_planar()
Traceback...
IndexError: list index out of range
```


Issue created by migration from https://trac.sagemath.org/ticket/5940





---

archive/issue_comments_046867.json:
```json
{
    "body": "Attachment [trac5940_circ_planar_empty_boundary.patch](tarball://root/attachments/some-uuid/ticket5940/trac5940_circ_planar_empty_boundary.patch) by ekirkman created at 2009-05-18 19:18:49",
    "created_at": "2009-05-18T19:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5940#issuecomment-46867",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Attachment [trac5940_circ_planar_empty_boundary.patch](tarball://root/attachments/some-uuid/ticket5940/trac5940_circ_planar_empty_boundary.patch) by ekirkman created at 2009-05-18 19:18:49



---

archive/issue_comments_046868.json:
```json
{
    "body": "The offending example needs to be added as a doctest. Otherwise, positive review.",
    "created_at": "2009-05-18T20:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5940#issuecomment-46868",
    "user": "https://github.com/rlmill"
}
```

The offending example needs to be added as a doctest. Otherwise, positive review.



---

archive/issue_comments_046869.json:
```json
{
    "body": "Apply instead.",
    "created_at": "2009-05-18T20:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5940#issuecomment-46869",
    "user": "https://github.com/rlmill"
}
```

Apply instead.



---

archive/issue_comments_046870.json:
```json
{
    "body": "Attachment [trac_5940-ref_fix.patch](tarball://root/attachments/some-uuid/ticket5940/trac_5940-ref_fix.patch) by @rlmill created at 2009-05-18 20:46:18",
    "created_at": "2009-05-18T20:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5940#issuecomment-46870",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5940-ref_fix.patch](tarball://root/attachments/some-uuid/ticket5940/trac_5940-ref_fix.patch) by @rlmill created at 2009-05-18 20:46:18



---

archive/issue_comments_046871.json:
```json
{
    "body": "Thanks for posting the patch with the doctest.  Looks good to me.",
    "created_at": "2009-05-18T20:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5940#issuecomment-46871",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Thanks for posting the patch with the doctest.  Looks good to me.



---

archive/issue_comments_046872.json:
```json
{
    "body": "Merged trac_5940-ref_fix.patch only in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T20:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5940#issuecomment-46872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5940-ref_fix.patch only in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_046873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T20:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5940#issuecomment-46873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006194.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-19T20:13:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5940",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5940#event-6194"
}
```
