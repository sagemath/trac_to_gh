# Issue 8759: Make the Sass css_dir be /data instead of /data/sage/css so that other components can use Sass

archive/issues_008759.json:
```json
{
    "body": "Assignee: acleone\n\nCC:  acleone was timdumol\n\nSass is the templating engine Sage uses for it's CSS.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8759\n\n",
    "created_at": "2010-04-24T23:19:58Z",
    "labels": [
        "notebook",
        "trivial",
        "enhancement"
    ],
    "title": "Make the Sass css_dir be /data instead of /data/sage/css so that other components can use Sass",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8759",
    "user": "acleone"
}
```
Assignee: acleone

CC:  acleone was timdumol

Sass is the templating engine Sage uses for it's CSS.

Issue created by migration from https://trac.sagemath.org/ticket/8759





---

archive/issue_comments_080143.json:
```json
{
    "body": "Changes the Sass css_dir to /data instead of /data/sage/css and moves the files accordingly in src.",
    "created_at": "2010-04-24T23:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80143",
    "user": "acleone"
}
```

Changes the Sass css_dir to /data instead of /data/sage/css and moves the files accordingly in src.



---

archive/issue_comments_080144.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-24T23:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80144",
    "user": "acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080145.json:
```json
{
    "body": "Attachment [trac_8759-sass-dir-change.patch](tarball://root/attachments/some-uuid/ticket8759/trac_8759-sass-dir-change.patch) by acleone created at 2010-04-24 23:22:43",
    "created_at": "2010-04-24T23:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80145",
    "user": "acleone"
}
```

Attachment [trac_8759-sass-dir-change.patch](tarball://root/attachments/some-uuid/ticket8759/trac_8759-sass-dir-change.patch) by acleone created at 2010-04-24 23:22:43



---

archive/issue_comments_080146.json:
```json
{
    "body": "Attachment [trac_8759-sass-dir-change.git-format.patch](tarball://root/attachments/some-uuid/ticket8759/trac_8759-sass-dir-change.git-format.patch) by acleone created at 2010-04-25 00:47:39\n\nReplaces earlier patch.  Now in git-format so that files are just renamed instead of removed/added",
    "created_at": "2010-04-25T00:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80146",
    "user": "acleone"
}
```

Attachment [trac_8759-sass-dir-change.git-format.patch](tarball://root/attachments/some-uuid/ticket8759/trac_8759-sass-dir-change.git-format.patch) by acleone created at 2010-04-25 00:47:39

Replaces earlier patch.  Now in git-format so that files are just renamed instead of removed/added



---

archive/issue_comments_080147.json:
```json
{
    "body": "I don't think any of the other components under /data are developed by us (except sage3d, which uses no CSS), so I'm not sure how useful this is.",
    "created_at": "2010-07-05T10:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80147",
    "user": "timdumol"
}
```

I don't think any of the other components under /data are developed by us (except sage3d, which uses no CSS), so I'm not sure how useful this is.



---

archive/issue_comments_080148.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-07-05T10:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80148",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_080149.json:
```json
{
    "body": "Agreed.  If there is truly a need for this, should be opened on https://github.com/sagemath/sagenb/ and clarified.",
    "created_at": "2014-12-11T15:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80149",
    "user": "kcrisman"
}
```

Agreed.  If there is truly a need for this, should be opened on https://github.com/sagemath/sagenb/ and clarified.



---

archive/issue_comments_080150.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2014-12-11T15:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80150",
    "user": "kcrisman"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_080151.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-12-11T18:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8759",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8759#issuecomment-80151",
    "user": "vbraun"
}
```

Resolution: invalid
