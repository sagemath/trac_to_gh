# Issue 6884: notebook doctest failures in Sage 4.1.2.alpha0 on mod.math

archive/issues_006884.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timdumol\n\nThe following doctests failed in Sage 4.1.2.alpha0 on mod.math:\n\n```\nsage -t -long devel/sage-main/sage/server/notebook/notebook.py # 12 doctests failed\nsage -t -long devel/sage-main/sage/server/notebook/worksheet.py # 5 doctests failed\n```\n\nThis was reported at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5370af4b74c5ca3c) thread. A full log is attached with this ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6884\n\n",
    "created_at": "2009-09-04T07:45:12Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook doctest failures in Sage 4.1.2.alpha0 on mod.math",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6884",
    "user": "mvngu"
}
```
Assignee: boothby

CC:  timdumol

The following doctests failed in Sage 4.1.2.alpha0 on mod.math:

```
sage -t -long devel/sage-main/sage/server/notebook/notebook.py # 12 doctests failed
sage -t -long devel/sage-main/sage/server/notebook/worksheet.py # 5 doctests failed
```

This was reported at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5370af4b74c5ca3c) thread. A full log is attached with this ticket.

Issue created by migration from https://trac.sagemath.org/ticket/6884





---

archive/issue_comments_056887.json:
```json
{
    "body": "Attachment\n\ndoctest log on mod.math",
    "created_at": "2009-09-04T07:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56887",
    "user": "mvngu"
}
```

Attachment

doctest log on mod.math



---

archive/issue_comments_056888.json:
```json
{
    "body": "Update MANIFEST.in to include all Jinja templates.",
    "created_at": "2009-09-05T14:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56888",
    "user": "mpatel"
}
```

Update MANIFEST.in to include all Jinja templates.



---

archive/issue_comments_056889.json:
```json
{
    "body": "Attachment\n\nI apologize for missing this.",
    "created_at": "2009-09-05T14:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56889",
    "user": "mpatel"
}
```

Attachment

I apologize for missing this.



---

archive/issue_comments_056890.json:
```json
{
    "body": "Attachment\n\nCorrected ticket number in patch filename. Apply only this patch.",
    "created_at": "2009-09-05T15:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56890",
    "user": "mpatel"
}
```

Attachment

Corrected ticket number in patch filename. Apply only this patch.



---

archive/issue_comments_056891.json:
```json
{
    "body": "If the \"manifest\" patch at #6568 fixes the doctest failures, please close this ticket.",
    "created_at": "2009-09-07T11:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56891",
    "user": "mpatel"
}
```

If the "manifest" patch at #6568 fixes the doctest failures, please close this ticket.



---

archive/issue_comments_056892.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-07T16:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56892",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056893.json:
```json
{
    "body": "The doctest failures are fixed by the patch `trac_6568-manifest.patch` at #6568.",
    "created_at": "2009-09-07T16:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6884#issuecomment-56893",
    "user": "mvngu"
}
```

The doctest failures are fixed by the patch `trac_6568-manifest.patch` at #6568.
