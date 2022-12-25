# Issue 7063: SageNB -- Get SageNB to work seamlessly with old notebook saves

archive/issues_007063.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\nKeywords: sagenb notebook\n\n[ ] make sure that the old notebook directory \"just works\" with the new notebook:\nproblem -- old notebooks unpickle into the old notebook code!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7063\n\n",
    "created_at": "2009-09-29T04:37:12Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "SageNB -- Get SageNB to work seamlessly with old notebook saves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7063",
    "user": "https://github.com/TimDumol"
}
```
Assignee: tbd

CC:  @williamstein

Keywords: sagenb notebook

[ ] make sure that the old notebook directory "just works" with the new notebook:
problem -- old notebooks unpickle into the old notebook code!

Issue created by migration from https://trac.sagemath.org/ticket/7063





---

archive/issue_comments_058316.json:
```json
{
    "body": "Migrates old notebook saves to the new notebook",
    "created_at": "2009-09-29T04:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7063#issuecomment-58316",
    "user": "https://github.com/TimDumol"
}
```

Migrates old notebook saves to the new notebook



---

archive/issue_comments_058317.json:
```json
{
    "body": "Attachment [trac_7063-sagenb-migrate-old-notebook.2.patch](tarball://root/attachments/some-uuid/ticket7063/trac_7063-sagenb-migrate-old-notebook.2.patch) by @TimDumol created at 2009-09-29 04:57:33\n\nApply this patch only.",
    "created_at": "2009-09-29T04:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7063#issuecomment-58317",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7063-sagenb-migrate-old-notebook.2.patch](tarball://root/attachments/some-uuid/ticket7063/trac_7063-sagenb-migrate-old-notebook.2.patch) by @TimDumol created at 2009-09-29 04:57:33

Apply this patch only.



---

archive/issue_comments_058318.json:
```json
{
    "body": "Attachment [trac_7063-sagenb-migrate-old-notebook.3.patch](tarball://root/attachments/some-uuid/ticket7063/trac_7063-sagenb-migrate-old-notebook.3.patch) by @TimDumol created at 2009-09-29 05:37:42\n\nExcludes everything under `backups` and `worksheets`. Apply this patch only./",
    "created_at": "2009-09-29T05:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7063#issuecomment-58318",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7063-sagenb-migrate-old-notebook.3.patch](tarball://root/attachments/some-uuid/ticket7063/trac_7063-sagenb-migrate-old-notebook.3.patch) by @TimDumol created at 2009-09-29 05:37:42

Excludes everything under `backups` and `worksheets`. Apply this patch only./



---

archive/issue_comments_058319.json:
```json
{
    "body": "Only backs up `nb.sobj` and `conf.sobj`s, since they're the only things affected anyways.",
    "created_at": "2009-09-29T05:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7063#issuecomment-58319",
    "user": "https://github.com/TimDumol"
}
```

Only backs up `nb.sobj` and `conf.sobj`s, since they're the only things affected anyways.



---

archive/issue_comments_058320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T06:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7063#issuecomment-58320",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_007283.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-09-29T06:28:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7063#event-7283"
}
```



---

archive/issue_comments_058321.json:
```json
{
    "body": "Attachment [trac_7063-sagenb-migrate-old-notebook.4.patch](tarball://root/attachments/some-uuid/ticket7063/trac_7063-sagenb-migrate-old-notebook.4.patch) by @williamstein created at 2009-09-29 06:28:34",
    "created_at": "2009-09-29T06:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7063#issuecomment-58321",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7063-sagenb-migrate-old-notebook.4.patch](tarball://root/attachments/some-uuid/ticket7063/trac_7063-sagenb-migrate-old-notebook.4.patch) by @williamstein created at 2009-09-29 06:28:34



---

archive/issue_comments_058322.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-10-23T21:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7063",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7063#issuecomment-58322",
    "user": "https://github.com/jasongrout"
}
```

Changing component from algebra to notebook.
