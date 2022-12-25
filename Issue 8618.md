# Issue 8618: Non standard alphabet

archive/issues_008618.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: word, substitution\n\nIt seems that some functions that use morphisms of words do not work for not standard alphabet. This ticket follows the bug found in the fixed_point method (#8595).\n\n**pseudo palindrome**\n\n\n```\nsage: t = WordMorphism({'a1':['a2'], 'a2':['a1']})\nsage: W = Words(['a1','a2'])\nsage: W(['a1','a2']).is_palindrome(t)\nAttributeError Traceback (most recent call last)\n...\nKeyError: 'a'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8618\n\n",
    "created_at": "2010-03-28T09:12:23Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Non standard alphabet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8618",
    "user": "https://github.com/videlec"
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

archive/issue_comments_077974.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-31T10:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-77974",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077975.json:
```json
{
    "body": "Attachment [trac_8618_is_identity-sl.patch](tarball://root/attachments/some-uuid/ticket8618/trac_8618_is_identity-sl.patch) by @seblabbe created at 2010-03-31 13:52:06\n\nDepends on #8595",
    "created_at": "2010-03-31T13:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-77975",
    "user": "https://github.com/seblabbe"
}
```

Attachment [trac_8618_is_identity-sl.patch](tarball://root/attachments/some-uuid/ticket8618/trac_8618_is_identity-sl.patch) by @seblabbe created at 2010-03-31 13:52:06

Depends on #8595



---

archive/issue_comments_077976.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-08T07:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-77976",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077977.json:
```json
{
    "body": "Thank you for this correction.",
    "created_at": "2010-04-08T07:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-77977",
    "user": "https://github.com/videlec"
}
```

Thank you for this correction.



---

archive/issue_comments_077978.json:
```json
{
    "body": "Merged \"trac_8618_is_identity-sl.patch\" in 4.4.alpha0",
    "created_at": "2010-04-16T18:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-77978",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8618_is_identity-sl.patch" in 4.4.alpha0



---

archive/issue_events_008789.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:50:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8618#event-8789"
}
```



---

archive/issue_comments_077979.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8618#issuecomment-77979",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
