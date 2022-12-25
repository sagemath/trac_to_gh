# Issue 6853: [with patch, positive review] Templating tag typo

archive/issues_006853.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @TimDumol\n\nThere is an incomplete closing script tag in `server/notebook/templates/notebook/head.tmpl`:\n\n```\n<script type=\"text/javascript\" src=\"/javascript/sage3d.js\"></script\n```\n\nI don't know if this actually affects any rendering engine.  I just noticed it when viewing the source for a worksheet page in Firefox.\n\nThis depends on #6568.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6853\n\n",
    "closed_at": "2009-09-03T08:16:57Z",
    "created_at": "2009-08-31T22:09:05Z",
    "labels": [
        "component: notebook",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] Templating tag typo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6853",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @TimDumol

There is an incomplete closing script tag in `server/notebook/templates/notebook/head.tmpl`:

```
<script type="text/javascript" src="/javascript/sage3d.js"></script
```

I don't know if this actually affects any rendering engine.  I just noticed it when viewing the source for a worksheet page in Firefox.

This depends on #6568.


Issue created by migration from https://trac.sagemath.org/ticket/6853





---

archive/issue_comments_056398.json:
```json
{
    "body": "Attachment [trac_6853-template_typo.patch](tarball://root/attachments/some-uuid/ticket6853/trac_6853-template_typo.patch) by @qed777 created at 2009-08-31 22:11:44\n\nApply only this patch.",
    "created_at": "2009-08-31T22:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56398",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6853-template_typo.patch](tarball://root/attachments/some-uuid/ticket6853/trac_6853-template_typo.patch) by @qed777 created at 2009-08-31 22:11:44

Apply only this patch.



---

archive/issue_comments_056399.json:
```json
{
    "body": "I'm not sure about why these lines appear in the patch:\n\n```\n-{% endmacro %}\n\\ No newline at end of file\n+{% endmacro %}\n```\nThese also appear in the new patch at #6459.",
    "created_at": "2009-08-31T22:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56399",
    "user": "https://github.com/qed777"
}
```

I'm not sure about why these lines appear in the patch:

```
-{% endmacro %}
\ No newline at end of file
+{% endmacro %}
```
These also appear in the new patch at #6459.



---

archive/issue_comments_056400.json:
```json
{
    "body": "Those lines mean the file that's being patched had no newline and the end of the file, but the new one does. (That's an improvement.)\nIn short, nothing to worry about.\n\nAnyway, this patch applies (after #6568) and is clearly correct, so positive review.",
    "created_at": "2009-09-01T19:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56400",
    "user": "https://github.com/wjp"
}
```

Those lines mean the file that's being patched had no newline and the end of the file, but the new one does. (That's an improvement.)
In short, nothing to worry about.

Anyway, this patch applies (after #6568) and is clearly correct, so positive review.



---

archive/issue_events_016125.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-03T08:16:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6853#event-16125"
}
```



---

archive/issue_comments_056401.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T08:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56401",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
