# Issue 8910: Have CombinatorialClass inherits from Parent

archive/issues_008910.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nThis is the first step of the cleanup of the combinatorial classes see \n  http://trac.sagemath.org/sage_trac/wiki/SageCombinatRoadMap\n\nIssue created by migration from https://trac.sagemath.org/ticket/8910\n\n",
    "created_at": "2010-05-07T12:02:11Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Have CombinatorialClass inherits from Parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8910",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

This is the first step of the cleanup of the combinatorial classes see 
  http://trac.sagemath.org/sage_trac/wiki/SageCombinatRoadMap

Issue created by migration from https://trac.sagemath.org/ticket/8910





---

archive/issue_comments_081944.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-12T17:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81944",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081945.json:
```json
{
    "body": "Attachment [trac_8910-combinatorial_class_parent-fh.patch](tarball://root/attachments/some-uuid/ticket8910/trac_8910-combinatorial_class_parent-fh.patch) by @hivert created at 2010-05-31 15:37:21\n\nThe patch has been reviewed by Nicolas on the patch queue. I folded the review patches:\n\n```\n$ hg qgoto trac_8910-subsets_an_element-fh.patch\n$ hg qfold trac_8910-subsets_an_element-review-nt.patch\n$ hg qfold trac_8910-subsets_an_element-review-review-fh.patch\n```\n\nAnd Nicolas said by e-mail\n\n```\n> D\u00e8s que j'ai ton feu vert, je folde tout, et met la positive review sur trac.\n\nFeu vert!\n```\n\nMeaning: (FH) as soon as I have your green light I fold the whole bunch, and set positive review on trac. (Answer from Nicolas) Green Light.\n\nTherefore I allowed myself to put the positive review.",
    "created_at": "2010-05-31T15:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81945",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8910-combinatorial_class_parent-fh.patch](tarball://root/attachments/some-uuid/ticket8910/trac_8910-combinatorial_class_parent-fh.patch) by @hivert created at 2010-05-31 15:37:21

The patch has been reviewed by Nicolas on the patch queue. I folded the review patches:

```
$ hg qgoto trac_8910-subsets_an_element-fh.patch
$ hg qfold trac_8910-subsets_an_element-review-nt.patch
$ hg qfold trac_8910-subsets_an_element-review-review-fh.patch
```

And Nicolas said by e-mail

```
> Dès que j'ai ton feu vert, je folde tout, et met la positive review sur trac.

Feu vert!
```

Meaning: (FH) as soon as I have your green light I fold the whole bunch, and set positive review on trac. (Answer from Nicolas) Green Light.

Therefore I allowed myself to put the positive review.



---

archive/issue_comments_081946.json:
```json
{
    "body": "Changing keywords from \"\" to \"CombinatorialClass Parent\".",
    "created_at": "2010-05-31T15:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81946",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "" to "CombinatorialClass Parent".



---

archive/issue_comments_081947.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-31T15:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81947",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081948.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-31T15:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81948",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081949.json:
```json
{
    "body": "> Meaning: (FH) as soon as I have your green light I fold the whole bunch, and set positive review on trac. (Answer from Nicolas) Green Light.\n\n> Therefore I allowed myself to put the positive review.\n\nDone",
    "created_at": "2010-05-31T15:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81949",
    "user": "https://github.com/hivert"
}
```

> Meaning: (FH) as soon as I have your green light I fold the whole bunch, and set positive review on trac. (Answer from Nicolas) Green Light.

> Therefore I allowed myself to put the positive review.

Done



---

archive/issue_comments_081950.json:
```json
{
    "body": "I forgot to tell: depend on #8881 (review in progress. Should be done soon).",
    "created_at": "2010-05-31T15:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81950",
    "user": "https://github.com/hivert"
}
```

I forgot to tell: depend on #8881 (review in progress. Should be done soon).



---

archive/issue_comments_081951.json:
```json
{
    "body": "Attachment [trac_8910-subsets_an_element-fh.patch](tarball://root/attachments/some-uuid/ticket8910/trac_8910-subsets_an_element-fh.patch) by @hivert created at 2010-05-31 15:44:42",
    "created_at": "2010-05-31T15:44:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81951",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8910-subsets_an_element-fh.patch](tarball://root/attachments/some-uuid/ticket8910/trac_8910-subsets_an_element-fh.patch) by @hivert created at 2010-05-31 15:44:42



---

archive/issue_comments_081952.json:
```json
{
    "body": "Note that this depends on #8902.",
    "created_at": "2010-06-05T22:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81952",
    "user": "https://github.com/mwhansen"
}
```

Note that this depends on #8902.



---

archive/issue_comments_081953.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8910#issuecomment-81953",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_009066.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T22:21:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8910",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8910#event-9066"
}
```
