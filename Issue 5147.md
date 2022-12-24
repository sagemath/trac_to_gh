# Issue 5147: make plot output file in DOCTEST_MODE changeable for sage-mode.el

archive/issues_005147.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: doctest plot output filename\n\nWhilst incorporating sage-view.el into sage-mode.el, I needed to be able to change the output filename while in DOCTEST_MODE.  This tiny patches adds a module scope variable name with the output file name.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5147\n\n",
    "created_at": "2009-02-01T02:42:56Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "make plot output file in DOCTEST_MODE changeable for sage-mode.el",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5147",
    "user": "ncalexan"
}
```
Assignee: mabshoff

Keywords: doctest plot output filename

Whilst incorporating sage-view.el into sage-mode.el, I needed to be able to change the output filename while in DOCTEST_MODE.  This tiny patches adds a module scope variable name with the output file name.

Issue created by migration from https://trac.sagemath.org/ticket/5147





---

archive/issue_comments_039382.json:
```json
{
    "body": "Attachment [trac_5147-plot-output-filename.patch](tarball://root/attachments/some-uuid/ticket5147/trac_5147-plot-output-filename.patch) by ncalexan created at 2009-02-01 02:44:48",
    "created_at": "2009-02-01T02:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5147#issuecomment-39382",
    "user": "ncalexan"
}
```

Attachment [trac_5147-plot-output-filename.patch](tarball://root/attachments/some-uuid/ticket5147/trac_5147-plot-output-filename.patch) by ncalexan created at 2009-02-01 02:44:48



---

archive/issue_comments_039383.json:
```json
{
    "body": "I see this as harmless, and it is very useful to me and users of sage-mode.el...",
    "created_at": "2009-02-01T02:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5147#issuecomment-39383",
    "user": "ncalexan"
}
```

I see this as harmless, and it is very useful to me and users of sage-mode.el...



---

archive/issue_comments_039384.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-02-01T20:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5147#issuecomment-39384",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_039385.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5147#issuecomment-39385",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_039386.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T02:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5147#issuecomment-39386",
    "user": "mabshoff"
}
```

Resolution: fixed
