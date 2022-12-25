# Issue 7607: add uncommitted files to the script repository

archive/issues_007607.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @mwhansen\n\nWith Sage 4.3.alpha0 and 4.3.alpha1, this shows up under the script repository:\n\n```\n~/Desktop/sage-4.3.alpha1/sage -hg st\n? hmac256\n? jmol\n? pilconvert.py\n? pildriver.py\n? pilfile.py\n? pilfont.py\n? pilprint.py\n? sphinx-autogen\n```\nThose files should be added using \"hg add\" and then checked in with \"hg ci\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/7607\n\n",
    "created_at": "2009-12-05T13:33:46Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "add uncommitted files to the script repository",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7607",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
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

archive/issue_comments_064778.json:
```json
{
    "body": "I don't think that those should be checked in since they are installed by spkgs.",
    "created_at": "2009-12-05T13:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64778",
    "user": "https://github.com/mwhansen"
}
```

I don't think that those should be checked in since they are installed by spkgs.



---

archive/issue_comments_064779.json:
```json
{
    "body": "based on Sage 4.3.alpha1",
    "created_at": "2009-12-05T13:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.3.alpha1



---

archive/issue_comments_064780.json:
```json
{
    "body": "Changing component from documentation to misc.",
    "created_at": "2009-12-05T13:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from documentation to misc.



---

archive/issue_comments_064781.json:
```json
{
    "body": "Attachment [trac_7607-hgignore.patch](tarball://root/attachments/some-uuid/ticket7607/trac_7607-hgignore.patch) by mvngu created at 2009-12-05 13:59:52\n\nReplying to [comment:1 mhansen]:\n> I don't think that those should be checked in since they are installed by spkgs.\n\n\nYes, good point! Would you consider configuring Mercurial to ignore those files? If so, I have attached the patch `trac_7607-hgignore.patch` to take care of the Mercurial configuration. That patch should be applied to the script repository.",
    "created_at": "2009-12-05T13:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7607-hgignore.patch](tarball://root/attachments/some-uuid/ticket7607/trac_7607-hgignore.patch) by mvngu created at 2009-12-05 13:59:52

Replying to [comment:1 mhansen]:
> I don't think that those should be checked in since they are installed by spkgs.


Yes, good point! Would you consider configuring Mercurial to ignore those files? If so, I have attached the patch `trac_7607-hgignore.patch` to take care of the Mercurial configuration. That patch should be applied to the script repository.



---

archive/issue_comments_064782.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-05T13:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064783.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-06T08:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64783",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_064784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T08:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7607#issuecomment-64784",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018077.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-06T08:28:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7607",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7607#event-18077"
}
```
