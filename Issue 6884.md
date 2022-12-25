# Issue 6884: notebook doctest failures in Sage 4.1.2.alpha0 on mod.math

archive/issues_006884.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @TimDumol\n\nThe following doctests failed in Sage 4.1.2.alpha0 on mod.math:\n\n```\nsage -t -long devel/sage-main/sage/server/notebook/notebook.py # 12 doctests failed\nsage -t -long devel/sage-main/sage/server/notebook/worksheet.py # 5 doctests failed\n```\n\nThis was reported at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5370af4b74c5ca3c) thread. A full log is attached with this ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6884\n\n",
    "created_at": "2009-09-04T07:45:12Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "notebook doctest failures in Sage 4.1.2.alpha0 on mod.math",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: boothby

CC:  @TimDumol

The following doctests failed in Sage 4.1.2.alpha0 on mod.math:

```
sage -t -long devel/sage-main/sage/server/notebook/notebook.py # 12 doctests failed
sage -t -long devel/sage-main/sage/server/notebook/worksheet.py # 5 doctests failed
```

This was reported at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5370af4b74c5ca3c) thread. A full log is attached with this ticket.

Issue created by migration from https://trac.sagemath.org/ticket/6884





---

archive/issue_comments_056779.json:
```json
{
    "body": "Attachment [doctest-4.1.2.alpha0-mod.log](tarball://root/attachments/some-uuid/ticket6884/doctest-4.1.2.alpha0-mod.log) by mvngu created at 2009-09-04 07:45:59\n\ndoctest log on mod.math",
    "created_at": "2009-09-04T07:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-4.1.2.alpha0-mod.log](tarball://root/attachments/some-uuid/ticket6884/doctest-4.1.2.alpha0-mod.log) by mvngu created at 2009-09-04 07:45:59

doctest log on mod.math



---

archive/issue_comments_056780.json:
```json
{
    "body": "Update MANIFEST.in to include all Jinja templates.",
    "created_at": "2009-09-05T14:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56780",
    "user": "https://github.com/qed777"
}
```

Update MANIFEST.in to include all Jinja templates.



---

archive/issue_comments_056781.json:
```json
{
    "body": "Attachment [trac_6684-templates_manifest.patch](tarball://root/attachments/some-uuid/ticket6884/trac_6684-templates_manifest.patch) by @qed777 created at 2009-09-05 14:10:59\n\nI apologize for missing this.",
    "created_at": "2009-09-05T14:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56781",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6684-templates_manifest.patch](tarball://root/attachments/some-uuid/ticket6884/trac_6684-templates_manifest.patch) by @qed777 created at 2009-09-05 14:10:59

I apologize for missing this.



---

archive/issue_comments_056782.json:
```json
{
    "body": "Attachment [trac_6884-templates_manifest.patch](tarball://root/attachments/some-uuid/ticket6884/trac_6884-templates_manifest.patch) by @qed777 created at 2009-09-05 15:17:49\n\nCorrected ticket number in patch filename. Apply only this patch.",
    "created_at": "2009-09-05T15:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56782",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6884-templates_manifest.patch](tarball://root/attachments/some-uuid/ticket6884/trac_6884-templates_manifest.patch) by @qed777 created at 2009-09-05 15:17:49

Corrected ticket number in patch filename. Apply only this patch.



---

archive/issue_comments_056783.json:
```json
{
    "body": "If the \"manifest\" patch at #6568 fixes the doctest failures, please close this ticket.",
    "created_at": "2009-09-07T11:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56783",
    "user": "https://github.com/qed777"
}
```

If the "manifest" patch at #6568 fixes the doctest failures, please close this ticket.



---

archive/issue_comments_056784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-07T16:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016189.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-07T16:19:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6884#event-16189"
}
```



---

archive/issue_comments_056785.json:
```json
{
    "body": "The doctest failures are fixed by the patch `trac_6568-manifest.patch` at #6568.",
    "created_at": "2009-09-07T16:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The doctest failures are fixed by the patch `trac_6568-manifest.patch` at #6568.
