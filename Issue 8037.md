# Issue 8037: add sagetex to the french tutorial

archive/issues_008037.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @dandrake\n\nMake changes in the French tutorial corresponding to those in #7617 in the English version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8037\n\n",
    "created_at": "2010-01-22T06:18:10Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "add sagetex to the french tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8037",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: mvngu

CC:  @dandrake

Make changes in the French tutorial corresponding to those in #7617 in the English version.

Issue created by migration from https://trac.sagemath.org/ticket/8037





---

archive/issue_comments_070087.json:
```json
{
    "body": "Attachment [trac_8037_sagetex_french_tutorial.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.patch) by @mezzarobba created at 2010-02-25 22:53:42",
    "created_at": "2010-02-25T22:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70087",
    "user": "https://github.com/mezzarobba"
}
```

Attachment [trac_8037_sagetex_french_tutorial.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.patch) by @mezzarobba created at 2010-02-25 22:53:42



---

archive/issue_comments_070088.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T22:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70088",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070089.json:
```json
{
    "body": "Changing assignee from mvngu to @mezzarobba.",
    "created_at": "2010-02-25T22:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70089",
    "user": "https://github.com/mezzarobba"
}
```

Changing assignee from mvngu to @mezzarobba.



---

archive/issue_comments_070090.json:
```json
{
    "body": "Uh oh, there's a tiny reject with this patch in 4.3.3 -- a \"[SA]\" got turned into \"[Sage]\". I'll upload a new patch.",
    "created_at": "2010-02-26T02:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70090",
    "user": "https://github.com/dandrake"
}
```

Uh oh, there's a tiny reject with this patch in 4.3.3 -- a "[SA]" got turned into "[Sage]". I'll upload a new patch.



---

archive/issue_comments_070091.json:
```json
{
    "body": "fix a small reject in introduction.rst",
    "created_at": "2010-02-26T02:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70091",
    "user": "https://github.com/dandrake"
}
```

fix a small reject in introduction.rst



---

archive/issue_comments_070092.json:
```json
{
    "body": "Attachment [trac_8037_sagetex_french_tutorial.2.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.2.patch) by @dandrake created at 2010-02-26 02:21:25\n\nBy the way, the documentation builds fine and appears as it should. (I'm using 4.3.3.) I think this can be a positive review, although I would prefer to have a French speaker (or at least someone who knows more than I do!) look over the patch.",
    "created_at": "2010-02-26T02:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70092",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_8037_sagetex_french_tutorial.2.patch](tarball://root/attachments/some-uuid/ticket8037/trac_8037_sagetex_french_tutorial.2.patch) by @dandrake created at 2010-02-26 02:21:25

By the way, the documentation builds fine and appears as it should. (I'm using 4.3.3.) I think this can be a positive review, although I would prefer to have a French speaker (or at least someone who knows more than I do!) look over the patch.



---

archive/issue_comments_070093.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T02:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70093",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070094.json:
```json
{
    "body": "Merged [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch).\n\n\n\nMarc, Dan: Avoid putting the following line at the top of your patch file:\n\n```\nexporting patch:\n```\nIt can result in Mercurial ignoring your commit message, so that your commit message won't show up in the changelog.",
    "created_at": "2010-03-02T22:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70094",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8037_sagetex_french_tutorial.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8037/trac_8037_sagetex_french_tutorial.2.patch).



Marc, Dan: Avoid putting the following line at the top of your patch file:

```
exporting patch:
```
It can result in Mercurial ignoring your commit message, so that your commit message won't show up in the changelog.



---

archive/issue_events_019256.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T22:11:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8037#event-19256"
}
```



---

archive/issue_comments_070095.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T22:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8037",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8037#issuecomment-70095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
