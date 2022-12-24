# Issue 8037: add sagetex to the french tutorial

archive/issues_008037.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @dandrake\n\nMake changes in the French tutorial corresponding to those in #7617 in the English version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8037\n\n",
    "created_at": "2010-01-22T06:18:10Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "add sagetex to the french tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8037",
    "user": "@jhpalmieri"
}
```
Assignee: mvngu

CC:  @dandrake

Make changes in the French tutorial corresponding to those in #7617 in the English version.

Issue created by migration from https://trac.sagemath.org/ticket/8037





---

archive/issue_comments_070208.json:
```json
{
    "body": "Attachment [trac_8037_sagetex_french_tutorial.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.patch) by @mezzarobba created at 2010-02-25 22:53:42",
    "created_at": "2010-02-25T22:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70208",
    "user": "@mezzarobba"
}
```

Attachment [trac_8037_sagetex_french_tutorial.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.patch) by @mezzarobba created at 2010-02-25 22:53:42



---

archive/issue_comments_070209.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T22:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70209",
    "user": "@mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070210.json:
```json
{
    "body": "Changing assignee from mvngu to @mezzarobba.",
    "created_at": "2010-02-25T22:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70210",
    "user": "@mezzarobba"
}
```

Changing assignee from mvngu to @mezzarobba.



---

archive/issue_comments_070211.json:
```json
{
    "body": "Uh oh, there's a tiny reject with this patch in 4.3.3 -- a \"[SA]\" got turned into \"[Sage]\". I'll upload a new patch.",
    "created_at": "2010-02-26T02:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70211",
    "user": "@dandrake"
}
```

Uh oh, there's a tiny reject with this patch in 4.3.3 -- a "[SA]" got turned into "[Sage]". I'll upload a new patch.



---

archive/issue_comments_070212.json:
```json
{
    "body": "fix a small reject in introduction.rst",
    "created_at": "2010-02-26T02:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70212",
    "user": "@dandrake"
}
```

fix a small reject in introduction.rst



---

archive/issue_comments_070213.json:
```json
{
    "body": "Attachment [trac_8037_sagetex_french_tutorial.2.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.2.patch) by @dandrake created at 2010-02-26 02:21:25\n\nBy the way, the documentation builds fine and appears as it should. (I'm using 4.3.3.) I think this can be a positive review, although I would prefer to have a French speaker (or at least someone who knows more than I do!) look over the patch.",
    "created_at": "2010-02-26T02:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70213",
    "user": "@dandrake"
}
```

Attachment [trac_8037_sagetex_french_tutorial.2.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.2.patch) by @dandrake created at 2010-02-26 02:21:25

By the way, the documentation builds fine and appears as it should. (I'm using 4.3.3.) I think this can be a positive review, although I would prefer to have a French speaker (or at least someone who knows more than I do!) look over the patch.



---

archive/issue_comments_070214.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T02:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70214",
    "user": "@dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070215.json:
```json
{
    "body": "Merged [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch).\n\n\n\nMarc, Dan: Avoid putting the following line at the top of your patch file:\n\n```\nexporting patch:\n```\n\nIt can result in Mercurial ignoring your commit message, so that your commit message won't show up in the changelog.",
    "created_at": "2010-03-02T22:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70215",
    "user": "mvngu"
}
```

Merged [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch).



Marc, Dan: Avoid putting the following line at the top of your patch file:

```
exporting patch:
```

It can result in Mercurial ignoring your commit message, so that your commit message won't show up in the changelog.



---

archive/issue_comments_070216.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70216",
    "user": "mvngu"
}
```

Resolution: fixed
