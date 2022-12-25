# Issue 7945: Class groups of number fields: an_element() not in self

archive/issues_007945.json:
```json
{
    "body": "Assignee: @loefflerd\n\n\n```\nsage: K.<a> = NumberField(x^2 + 23)\nsage: G = K.class_group(); G\nClass group of order 3 with structure C3 of Number Field in a with defining polynomial x^2 + 23\nsage: G.an_element() in G\nFalse\n```\n\n\nCatched with #7921.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7945\n\n",
    "created_at": "2010-01-16T12:28:51Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Class groups of number fields: an_element() not in self",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7945",
    "user": "https://github.com/nthiery"
}
```
Assignee: @loefflerd


```
sage: K.<a> = NumberField(x^2 + 23)
sage: G = K.class_group(); G
Class group of order 3 with structure C3 of Number Field in a with defining polynomial x^2 + 23
sage: G.an_element() in G
False
```


Catched with #7921.

Issue created by migration from https://trac.sagemath.org/ticket/7945





---

archive/issue_comments_069200.json:
```json
{
    "body": "This is fixed by my patch at #9244.",
    "created_at": "2010-06-29T11:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7945#issuecomment-69200",
    "user": "https://github.com/loefflerd"
}
```

This is fixed by my patch at #9244.



---

archive/issue_comments_069201.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T11:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7945#issuecomment-69201",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069202.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T11:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7945#issuecomment-69202",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069203.json:
```json
{
    "body": "I'm setting this to \"positive review\" to bring it to the attention of the release maintainer.",
    "created_at": "2010-06-29T11:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7945#issuecomment-69203",
    "user": "https://github.com/loefflerd"
}
```

I'm setting this to "positive review" to bring it to the attention of the release maintainer.



---

archive/issue_comments_069204.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-20T07:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7945#issuecomment-69204",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_comments_069205.json:
```json
{
    "body": "I'm resolving this ticket as a \"duplicate.\"",
    "created_at": "2010-07-20T07:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7945#issuecomment-69205",
    "user": "https://github.com/qed777"
}
```

I'm resolving this ticket as a "duplicate."
