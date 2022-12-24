# Issue 7607: add uncommitted files to the script repository

archive/issues_007607.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @mwhansen\n\nWith Sage 4.3.alpha0 and 4.3.alpha1, this shows up under the script repository:\n\n```\n~/Desktop/sage-4.3.alpha1/sage -hg st\n? hmac256\n? jmol\n? pilconvert.py\n? pildriver.py\n? pilfile.py\n? pilfont.py\n? pilprint.py\n? sphinx-autogen\n```\n\nThose files should be added using \"hg add\" and then checked in with \"hg ci\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/7607\n\n",
    "created_at": "2009-12-05T13:33:46Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "add uncommitted files to the script repository",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7607",
    "user": "mvngu"
}
```
Assignee: mvngu

CC:  @mwhansen

With Sage 4.3.alpha0 and 4.3.alpha1, this shows up under the script repository:

```
~/Desktop/sage-4.3.alpha1/sage -hg st
? hmac256
? jmol
? pilconvert.py
? pildriver.py
? pilfile.py
? pilfont.py
? pilprint.py
? sphinx-autogen
```

Those files should be added using "hg add" and then checked in with "hg ci".

Issue created by migration from https://trac.sagemath.org/ticket/7607





---

archive/issue_comments_064894.json:
```json
{
    "body": "I don't think that those should be checked in since they are installed by spkgs.",
    "created_at": "2009-12-05T13:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64894",
    "user": "@mwhansen"
}
```

I don't think that those should be checked in since they are installed by spkgs.



---

archive/issue_comments_064895.json:
```json
{
    "body": "based on Sage 4.3.alpha1",
    "created_at": "2009-12-05T13:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64895",
    "user": "mvngu"
}
```

based on Sage 4.3.alpha1



---

archive/issue_comments_064896.json:
```json
{
    "body": "Changing component from documentation to misc.",
    "created_at": "2009-12-05T13:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64896",
    "user": "mvngu"
}
```

Changing component from documentation to misc.



---

archive/issue_comments_064897.json:
```json
{
    "body": "Attachment [trac_7607-hgignore.patch](tarball://root/attachments/some-uuid/ticket7607/trac_7607-hgignore.patch) by mvngu created at 2009-12-05 13:59:52\n\nReplying to [comment:1 mhansen]:\n> I don't think that those should be checked in since they are installed by spkgs.\n\nYes, good point! Would you consider configuring Mercurial to ignore those files? If so, I have attached the patch `trac_7607-hgignore.patch` to take care of the Mercurial configuration. That patch should be applied to the script repository.",
    "created_at": "2009-12-05T13:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64897",
    "user": "mvngu"
}
```

Attachment [trac_7607-hgignore.patch](tarball://root/attachments/some-uuid/ticket7607/trac_7607-hgignore.patch) by mvngu created at 2009-12-05 13:59:52

Replying to [comment:1 mhansen]:
> I don't think that those should be checked in since they are installed by spkgs.

Yes, good point! Would you consider configuring Mercurial to ignore those files? If so, I have attached the patch `trac_7607-hgignore.patch` to take care of the Mercurial configuration. That patch should be applied to the script repository.



---

archive/issue_comments_064898.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-05T13:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64898",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064899.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-06T08:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64899",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_064900.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T08:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64900",
    "user": "@mwhansen"
}
```

Resolution: fixed
