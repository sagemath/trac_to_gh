# Issue 6463: Residue fields broken for relative extensions

archive/issues_006463.json:
```json
{
    "body": "Assignee: was\n\nKeywords: ideals\n\nThe code for residue fields of ideals in number fields is broken for ideals of relative extensions, as it tries to call \"norm\" on an ideal, which we have chosen to deliberately break for relative ideals.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6463\n\n",
    "created_at": "2009-07-04T15:42:22Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Residue fields broken for relative extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6463",
    "user": "davidloeffler"
}
```
Assignee: was

Keywords: ideals

The code for residue fields of ideals in number fields is broken for ideals of relative extensions, as it tries to call "norm" on an ideal, which we have chosen to deliberately break for relative ideals.

Issue created by migration from https://trac.sagemath.org/ticket/6463





---

archive/issue_comments_052229.json:
```json
{
    "body": "patch against 4.1.alpha2",
    "created_at": "2009-07-04T15:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6463#issuecomment-52229",
    "user": "davidloeffler"
}
```

patch against 4.1.alpha2



---

archive/issue_comments_052230.json:
```json
{
    "body": "Attachment [trac_6463-relative_residue_field.patch](tarball://root/attachments/some-uuid/ticket6463/trac_6463-relative_residue_field.patch) by davidloeffler created at 2009-07-04 15:52:37",
    "created_at": "2009-07-04T15:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6463#issuecomment-52230",
    "user": "davidloeffler"
}
```

Attachment [trac_6463-relative_residue_field.patch](tarball://root/attachments/some-uuid/ticket6463/trac_6463-relative_residue_field.patch) by davidloeffler created at 2009-07-04 15:52:37



---

archive/issue_comments_052231.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2009-07-14T21:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6463#issuecomment-52231",
    "user": "ncalexan"
}
```

Fine by me.



---

archive/issue_comments_052232.json:
```json
{
    "body": "David, the patch `trac_6463-relative_residue_field.patch` doesn't have your username, so I'm committing it in your name.",
    "created_at": "2009-07-16T21:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6463#issuecomment-52232",
    "user": "mvngu"
}
```

David, the patch `trac_6463-relative_residue_field.patch` doesn't have your username, so I'm committing it in your name.



---

archive/issue_comments_052233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6463#issuecomment-52233",
    "user": "mvngu"
}
```

Resolution: fixed
