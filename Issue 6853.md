# Issue 6853: [with patch, needs review] Templating tag typo

archive/issues_006853.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timdumol\n\nThere is an incomplete closing script tag in `server/notebook/templates/notebook/head.tmpl`:\n\n```\n<script type=\"text/javascript\" src=\"/javascript/sage3d.js\"></script\n```\n\n\nI don't know if this actually affects any rendering engine.  I just noticed it when viewing the source for a worksheet page in Firefox.\n\nThis depends on #6568.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6853\n\n",
    "created_at": "2009-08-31T22:09:05Z",
    "labels": [
        "notebook",
        "trivial",
        "bug"
    ],
    "title": "[with patch, needs review] Templating tag typo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6853",
    "user": "mpatel"
}
```
Assignee: boothby

CC:  timdumol

There is an incomplete closing script tag in `server/notebook/templates/notebook/head.tmpl`:

```
<script type="text/javascript" src="/javascript/sage3d.js"></script
```


I don't know if this actually affects any rendering engine.  I just noticed it when viewing the source for a worksheet page in Firefox.

This depends on #6568.


Issue created by migration from https://trac.sagemath.org/ticket/6853





---

archive/issue_comments_056501.json:
```json
{
    "body": "Attachment [trac_6853-template_typo.patch](tarball://root/attachments/some-uuid/ticket6853/trac_6853-template_typo.patch) by mpatel created at 2009-08-31 22:11:44\n\nApply only this patch.",
    "created_at": "2009-08-31T22:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56501",
    "user": "mpatel"
}
```

Attachment [trac_6853-template_typo.patch](tarball://root/attachments/some-uuid/ticket6853/trac_6853-template_typo.patch) by mpatel created at 2009-08-31 22:11:44

Apply only this patch.



---

archive/issue_comments_056502.json:
```json
{
    "body": "I'm not sure about why these lines appear in the patch:\n\n```\n-{% endmacro %}\n\\ No newline at end of file\n+{% endmacro %}\n```\n\nThese also appear in the new patch at #6459.",
    "created_at": "2009-08-31T22:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56502",
    "user": "mpatel"
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

archive/issue_comments_056503.json:
```json
{
    "body": "Those lines mean the file that's being patched had no newline and the end of the file, but the new one does. (That's an improvement.)\nIn short, nothing to worry about.\n\nAnyway, this patch applies (after #6568) and is clearly correct, so positive review.",
    "created_at": "2009-09-01T19:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56503",
    "user": "wjp"
}
```

Those lines mean the file that's being patched had no newline and the end of the file, but the new one does. (That's an improvement.)
In short, nothing to worry about.

Anyway, this patch applies (after #6568) and is clearly correct, so positive review.



---

archive/issue_comments_056504.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T08:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6853#issuecomment-56504",
    "user": "mvngu"
}
```

Resolution: fixed
