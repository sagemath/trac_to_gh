# Issue 3153: make finite_field_ntl_gf2e use randstate framework

archive/issues_003153.json:
```json
{
    "body": "Assignee: tbd\n\nThe patch from #3020 added a new call to a pseudo-random-number generator, not under the control of the Sage randstate framework.  This patch fixes that up, as well as adding some new documentation to randstate.  Applies on top of the patch from #3020.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3153\n\n",
    "created_at": "2008-05-10T22:41:39Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "make finite_field_ntl_gf2e use randstate framework",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3153",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: tbd

The patch from #3020 added a new call to a pseudo-random-number generator, not under the control of the Sage randstate framework.  This patch fixes that up, as well as adding some new documentation to randstate.  Applies on top of the patch from #3020.

Issue created by migration from https://trac.sagemath.org/ticket/3153





---

archive/issue_comments_021816.json:
```json
{
    "body": "Attachment [GF2X_sparse_poly_fix_random.patch](tarball://root/attachments/some-uuid/ticket3153/GF2X_sparse_poly_fix_random.patch) by cwitty created at 2008-05-10 22:41:57",
    "created_at": "2008-05-10T22:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3153#issuecomment-21816",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [GF2X_sparse_poly_fix_random.patch](tarball://root/attachments/some-uuid/ticket3153/GF2X_sparse_poly_fix_random.patch) by cwitty created at 2008-05-10 22:41:57



---

archive/issue_comments_021817.json:
```json
{
    "body": "This is a very good idea indeed.  The patch looks fine to me though it would also be agood idea if someone more familiar with Sage's random framework looked at it too.",
    "created_at": "2008-05-14T21:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3153#issuecomment-21817",
    "user": "https://github.com/JohnCremona"
}
```

This is a very good idea indeed.  The patch looks fine to me though it would also be agood idea if someone more familiar with Sage's random framework looked at it too.



---

archive/issue_events_007125.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-17T18:31:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3153",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3153#event-7125"
}
```



---

archive/issue_comments_021818.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T18:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3153#issuecomment-21818",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021819.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T18:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3153",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3153#issuecomment-21819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1
