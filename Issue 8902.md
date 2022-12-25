# Issue 8902: Subsets element construction is broken

archive/issues_008902.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: Subsets constructor\n\n\n```\nsage: S2 = Subsets(2)\nsage: S2([])\n<type 'sage.structure.parent.Set_generic'>\nsage: S2([1])\n<type 'sage.structure.parent.Set_generic'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8902\n\n",
    "created_at": "2010-05-06T02:30:52Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Subsets element construction is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8902",
    "user": "https://github.com/hivert"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: Subsets constructor


```
sage: S2 = Subsets(2)
sage: S2([])
<type 'sage.structure.parent.Set_generic'>
sage: S2([1])
<type 'sage.structure.parent.Set_generic'>
```


Issue created by migration from https://trac.sagemath.org/ticket/8902





---

archive/issue_comments_081808.json:
```json
{
    "body": "Note: This is a temporary fixes before the cleanup of combinat (categorification of the combinatorial classes is done).",
    "created_at": "2010-05-12T20:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8902#issuecomment-81808",
    "user": "https://github.com/hivert"
}
```

Note: This is a temporary fixes before the cleanup of combinat (categorification of the combinatorial classes is done).



---

archive/issue_comments_081809.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-12T20:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8902#issuecomment-81809",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081810.json:
```json
{
    "body": "Changing assignee from sage-combinat to @hivert.",
    "created_at": "2010-05-12T20:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8902#issuecomment-81810",
    "user": "https://github.com/hivert"
}
```

Changing assignee from sage-combinat to @hivert.



---

archive/issue_comments_081811.json:
```json
{
    "body": "Attachment [trac_8902-subsets_call_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8902/trac_8902-subsets_call_fix-fh.patch) by @hivert created at 2010-05-31 10:28:05",
    "created_at": "2010-05-31T10:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8902#issuecomment-81811",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8902-subsets_call_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8902/trac_8902-subsets_call_fix-fh.patch) by @hivert created at 2010-05-31 10:28:05



---

archive/issue_comments_081812.json:
```json
{
    "body": "Nicolas on sage-combinat series file:\n\n```\ntrac_8902-subsets_call_fix-fh.patch               # Positive review, assuming tests pass (NT)\n```\n\nI got a all test passes on massena.\n\nNote: the category related problem we discussed on the phone is postponed until #8910 in the patch `trac_8910-subsets_an_element-fh.patch`. \n\nIf you are ok with that can you put a positive review ?",
    "created_at": "2010-05-31T10:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8902#issuecomment-81812",
    "user": "https://github.com/hivert"
}
```

Nicolas on sage-combinat series file:

```
trac_8902-subsets_call_fix-fh.patch               # Positive review, assuming tests pass (NT)
```

I got a all test passes on massena.

Note: the category related problem we discussed on the phone is postponed until #8910 in the patch `trac_8910-subsets_an_element-fh.patch`. 

If you are ok with that can you put a positive review ?



---

archive/issue_comments_081813.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-31T11:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8902#issuecomment-81813",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009058.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T22:18:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8902#event-9058"
}
```



---

archive/issue_comments_081814.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8902#issuecomment-81814",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
