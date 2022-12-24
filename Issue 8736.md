# Issue 8736: Bug in computing radical of univariate polynomial

archive/issues_008736.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nFrom #sage-devel:\n<wjp> sage: R.<x> = GF(2)[]\n<wjp> sage: (x^2).radical()\n<wjp> 1\n\nIssue created by migration from https://trac.sagemath.org/ticket/8736\n\n",
    "created_at": "2010-04-21T09:43:31Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "Bug in computing radical of univariate polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8736",
    "user": "johanbosman"
}
```
Assignee: AlexGhitza

From #sage-devel:
<wjp> sage: R.<x> = GF(2)[]
<wjp> sage: (x^2).radical()
<wjp> 1

Issue created by migration from https://trac.sagemath.org/ticket/8736





---

archive/issue_comments_079899.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-21T11:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79899",
    "user": "johanbosman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079900.json:
```json
{
    "body": "I was told it is not bad to put the corresponding ticket number in the doctest and/or near the code that fixes an issue for later reference.",
    "created_at": "2010-04-21T20:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79900",
    "user": "leif"
}
```

I was told it is not bad to put the corresponding ticket number in the doctest and/or near the code that fixes an issue for later reference.



---

archive/issue_comments_079901.json:
```json
{
    "body": "Attachment [trac_8736_radical_fix.patch](tarball://root/attachments/some-uuid/ticket8736/trac_8736_radical_fix.patch) by johanbosman created at 2010-04-22 10:54:19",
    "created_at": "2010-04-22T10:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79901",
    "user": "johanbosman"
}
```

Attachment [trac_8736_radical_fix.patch](tarball://root/attachments/some-uuid/ticket8736/trac_8736_radical_fix.patch) by johanbosman created at 2010-04-22 10:54:19



---

archive/issue_comments_079902.json:
```json
{
    "body": "Like this? ;)",
    "created_at": "2010-04-22T10:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79902",
    "user": "johanbosman"
}
```

Like this? ;)



---

archive/issue_comments_079903.json:
```json
{
    "body": "Probably like that, but now this patch file contains two patches and does not apply cleanly. I know that if you remove the existing patch before repeating the export command, everything should be fine and you will get a nice new patch. Maybe there are better ways which I am not aware of. Otherwise the patch seems fine to me and passes all doctests (I ran them on the previous working version).",
    "created_at": "2010-04-22T21:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79903",
    "user": "novoselt"
}
```

Probably like that, but now this patch file contains two patches and does not apply cleanly. I know that if you remove the existing patch before repeating the export command, everything should be fine and you will get a nice new patch. Maybe there are better ways which I am not aware of. Otherwise the patch seems fine to me and passes all doctests (I ran them on the previous working version).



---

archive/issue_comments_079904.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-22T21:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79904",
    "user": "novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079905.json:
```json
{
    "body": "Johan's patch with first hunk deleted",
    "created_at": "2010-04-22T22:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79905",
    "user": "leif"
}
```

Johan's patch with first hunk deleted



---

archive/issue_comments_079906.json:
```json
{
    "body": "Attachment [trac_8736_radical_fix_single_patch.patch](tarball://root/attachments/some-uuid/ticket8736/trac_8736_radical_fix_single_patch.patch) by leif created at 2010-04-22 22:33:07\n\nIt's easier to just edit the patch (i.e., delete the first hunk)...",
    "created_at": "2010-04-22T22:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79906",
    "user": "leif"
}
```

Attachment [trac_8736_radical_fix_single_patch.patch](tarball://root/attachments/some-uuid/ticket8736/trac_8736_radical_fix_single_patch.patch) by leif created at 2010-04-22 22:33:07

It's easier to just edit the patch (i.e., delete the first hunk)...



---

archive/issue_comments_079907.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-22T22:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79907",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079908.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-23T03:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79908",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079909.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T04:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8736#issuecomment-79909",
    "user": "was"
}
```

Resolution: fixed
