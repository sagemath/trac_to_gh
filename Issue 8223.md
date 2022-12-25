# Issue 8223: tab completion broken for many parent objects

archive/issues_008223.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @novoselt\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8223\n\n",
    "created_at": "2010-02-09T20:34:02Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "tab completion broken for many parent objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8223",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @novoselt

```

Issue created by migration from https://trac.sagemath.org/ticket/8223





---

archive/issue_comments_072491.json:
```json
{
    "body": "Changing assignee from tbd to @nthiery.",
    "created_at": "2010-02-09T20:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72491",
    "user": "https://github.com/nthiery"
}
```

Changing assignee from tbd to @nthiery.



---

archive/issue_comments_072492.json:
```json
{
    "body": "Attachment [trac_8223-fix_dir-nt.patch](tarball://root/attachments/some-uuid/ticket8223/trac_8223-fix_dir-nt.patch) by @nthiery created at 2010-02-09 20:56:40\n\nThe attached patch should fix the issue. That being said, I would love to see a more robust implementation of ``sage.structure.parent.dir_with_other_class``.",
    "created_at": "2010-02-09T20:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72492",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8223-fix_dir-nt.patch](tarball://root/attachments/some-uuid/ticket8223/trac_8223-fix_dir-nt.patch) by @nthiery created at 2010-02-09 20:56:40

The attached patch should fix the issue. That being said, I would love to see a more robust implementation of ``sage.structure.parent.dir_with_other_class``.



---

archive/issue_comments_072493.json:
```json
{
    "body": "on #sage-devel\n\n```\n00:39 < logix> fwiw, for me the patch in #8223 makes k.[TAB] work again (where e.g. k.<a>=GF(8) )\n```",
    "created_at": "2010-02-10T08:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72493",
    "user": "https://github.com/haraldschilly"
}
```

on #sage-devel

```
00:39 < logix> fwiw, for me the patch in #8223 makes k.[TAB] work again (where e.g. k.<a>=GF(8) )
```



---

archive/issue_comments_072494.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-15T22:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72494",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072495.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-02-15T23:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72495",
    "user": "https://github.com/novoselt"
}
```

Looks good to me.



---

archive/issue_comments_072496.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-15T23:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72496",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072497.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72497",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019677.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-17T20:41:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8223#event-19677"
}
```



---

archive/issue_comments_072498.json:
```json
{
    "body": "Merged [trac_8223-fix_dir-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8223/trac_8223-fix_dir-nt.patch) with a sensible commit message containing the ticket number.",
    "created_at": "2010-02-17T20:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8223#issuecomment-72498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8223-fix_dir-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8223/trac_8223-fix_dir-nt.patch) with a sensible commit message containing the ticket number.
