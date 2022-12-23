# Issue 8618: Non standard alphabet

archive/issues_008618.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: word, substitution\n\nIt seems that some functions that use morphisms of words do not work for not standard alphabet. This ticket follows the bug found in the fixed_point method (#8595).\n\n**pseudo palindrome**\n\n\n```\nsage: t = WordMorphism({'a1':['a2'], 'a2':['a1']})\nsage: W = Words(['a1','a2'])\nsage: W(['a1','a2']).is_palindrome(t)\nAttributeError Traceback (most recent call last)\n...\nKeyError: 'a'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8618\n\n",
    "created_at": "2010-03-28T09:12:23Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Non standard alphabet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8618",
    "user": "vdelecroix"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: word, substitution

It seems that some functions that use morphisms of words do not work for not standard alphabet. This ticket follows the bug found in the fixed_point method (#8595).

**pseudo palindrome**


```
sage: t = WordMorphism({'a1':['a2'], 'a2':['a1']})
sage: W = Words(['a1','a2'])
sage: W(['a1','a2']).is_palindrome(t)
AttributeError Traceback (most recent call last)
...
KeyError: 'a'
```



Issue created by migration from https://trac.sagemath.org/ticket/8618





---

archive/issue_comments_078102.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-31T10:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-78102",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078103.json:
```json
{
    "body": "Attachment\n\nDepends on #8595",
    "created_at": "2010-03-31T13:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-78103",
    "user": "slabbe"
}
```

Attachment

Depends on #8595



---

archive/issue_comments_078104.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-08T07:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-78104",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078105.json:
```json
{
    "body": "Thank you for this correction.",
    "created_at": "2010-04-08T07:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-78105",
    "user": "vdelecroix"
}
```

Thank you for this correction.



---

archive/issue_comments_078106.json:
```json
{
    "body": "Merged \"trac_8618_is_identity-sl.patch\" in 4.4.alpha0",
    "created_at": "2010-04-16T18:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-78106",
    "user": "jhpalmieri"
}
```

Merged "trac_8618_is_identity-sl.patch" in 4.4.alpha0



---

archive/issue_comments_078107.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-78107",
    "user": "jhpalmieri"
}
```

Resolution: fixed
