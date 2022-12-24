# Issue 9267: Update the charge statistic on words

archive/issues_009267.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: words, charge, cocharge\n\nThe following behavior is currently in sage:\n\n```\nsage: w = Word([1,2,3,1,2])\nsage: w.charge()\n0\n```\n\nThis is inconsistent with the definition one usually finds in the\nliterature, which would give the charge of this word as 2. (see\nMacdonald's book, for example).\n\nThe goal of this ticket is to fix this bug, add a cocharge statistic, and extend the definition to words without partition content.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9267\n\n",
    "created_at": "2010-06-18T18:40:13Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Update the charge statistic on words",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9267",
    "user": "jbandlow"
}
```
Assignee: sage-combinat

Keywords: words, charge, cocharge

The following behavior is currently in sage:

```
sage: w = Word([1,2,3,1,2])
sage: w.charge()
0
```

This is inconsistent with the definition one usually finds in the
literature, which would give the charge of this word as 2. (see
Macdonald's book, for example).

The goal of this ticket is to fix this bug, add a cocharge statistic, and extend the definition to words without partition content.

Issue created by migration from https://trac.sagemath.org/ticket/9267





---

archive/issue_comments_087284.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T18:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87284",
    "user": "jbandlow"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087285.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-29T19:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87285",
    "user": "saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087286.json:
```json
{
    "body": "Tested against sage-4.4.4. Patch applies cleanly. All tests pass. The code looks good.\n\nJust a few documentation issues:\n\n- Add a line break here:\n\n```\n r\"\"\"Implements Lascoux and Schutzenberger's `s_i` operator, swapping\n```\n\n\n- Please add a reference in the documentation to an article or book that defines charge, cocharge, Lascoux and Schutzenberger's `s_i` operators, etc.\n\n- Since this definition of charge differs from that found in Macdonald's book, and since Sage uses many of Macdonald's conventions, I think it is a good idea to add a warning in the docstring of charge that explains that this is the common definition found in the literature and that it differs from that in Macdonald's book.",
    "created_at": "2010-06-29T19:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87286",
    "user": "saliola"
}
```

Tested against sage-4.4.4. Patch applies cleanly. All tests pass. The code looks good.

Just a few documentation issues:

- Add a line break here:

```
 r"""Implements Lascoux and Schutzenberger's `s_i` operator, swapping
```


- Please add a reference in the documentation to an article or book that defines charge, cocharge, Lascoux and Schutzenberger's `s_i` operators, etc.

- Since this definition of charge differs from that found in Macdonald's book, and since Sage uses many of Macdonald's conventions, I think it is a good idea to add a warning in the docstring of charge that explains that this is the common definition found in the literature and that it differs from that in Macdonald's book.



---

archive/issue_comments_087287.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-30T16:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87287",
    "user": "jbandlow"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087288.json:
```json
{
    "body": "Wow, I can't believe I forgot to put those comments in after all the discussion.  Thanks a lot for the review, Franco.  Please look at the new version and let me know what you think.",
    "created_at": "2010-06-30T16:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87288",
    "user": "jbandlow"
}
```

Wow, I can't believe I forgot to put those comments in after all the discussion.  Thanks a lot for the review, Franco.  Please look at the new version and let me know what you think.



---

archive/issue_comments_087289.json:
```json
{
    "body": "Jason, is the \\A intentional in references [2] and [3]?\n\nOtherwise, this gets a positive review from me, provided that the documentation builds correctly (I have not had the chance to build it yet, and won't be able to do it today).",
    "created_at": "2010-06-30T17:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87289",
    "user": "saliola"
}
```

Jason, is the \A intentional in references [2] and [3]?

Otherwise, this gets a positive review from me, provided that the documentation builds correctly (I have not had the chance to build it yet, and won't be able to do it today).



---

archive/issue_comments_087290.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-06-30T17:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87290",
    "user": "saliola"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_087291.json:
```json
{
    "body": "Attachment [trac_9267-charge_jb.patch](tarball://root/attachments/some-uuid/ticket9267/trac_9267-charge_jb.patch) by jbandlow created at 2010-06-30 18:04:08",
    "created_at": "2010-06-30T18:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87291",
    "user": "jbandlow"
}
```

Attachment [trac_9267-charge_jb.patch](tarball://root/attachments/some-uuid/ticket9267/trac_9267-charge_jb.patch) by jbandlow created at 2010-06-30 18:04:08



---

archive/issue_comments_087292.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-06-30T18:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87292",
    "user": "jbandlow"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_087293.json:
```json
{
    "body": "Replying to [comment:4 saliola]:\n> Jason, is the \\A intentional in references [2] and [3]?\n\nIn a first, incorrectly sphinxed, attempt to add these references, the 'A.' was being interpreted as the start of a list, so I had to make the 'A' a literal.  But that's not happening anymore, so I've removed the backslash.\n\n> Otherwise, this gets a positive review from me, provided that the documentation builds correctly (I have not had the chance to build it yet, and won't be able to do it today).\n\nGreat!  I think the doc builds ok, but I will wait until someone else verifies this instead of setting positive review on my own patch.\n\nThanks again, Franco.",
    "created_at": "2010-06-30T18:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87293",
    "user": "jbandlow"
}
```

Replying to [comment:4 saliola]:
> Jason, is the \A intentional in references [2] and [3]?

In a first, incorrectly sphinxed, attempt to add these references, the 'A.' was being interpreted as the start of a list, so I had to make the 'A' a literal.  But that's not happening anymore, so I've removed the backslash.

> Otherwise, this gets a positive review from me, provided that the documentation builds correctly (I have not had the chance to build it yet, and won't be able to do it today).

Great!  I think the doc builds ok, but I will wait until someone else verifies this instead of setting positive review on my own patch.

Thanks again, Franco.



---

archive/issue_comments_087294.json:
```json
{
    "body": "Documentation looks good.",
    "created_at": "2010-07-02T01:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87294",
    "user": "saliola"
}
```

Documentation looks good.



---

archive/issue_comments_087295.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T01:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87295",
    "user": "saliola"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9267",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9267#issuecomment-87296",
    "user": "mpatel"
}
```

Resolution: fixed
