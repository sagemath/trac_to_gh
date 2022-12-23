# Issue 8957: Word problem broken for matrix groups

archive/issues_008957.json:
```json
{
    "body": "Assignee: joyner\n\nThe method \"word_problem\" in the matrix groups class is broken in two separate ways. Firstly, it's supposed to allow you to specify a custom set of generators but it silently ignores them and uses the default ones. Secondly, it returns a Factorization object which assumes (!) that the group is commutative, and hence the results are complete junk for nonabelian groups.\n\nI have a rough patch for this but it needs some polishing (mainly adding tests and docstrings).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8957\n\n",
    "created_at": "2010-05-12T18:17:43Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "Word problem broken for matrix groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8957",
    "user": "davidloeffler"
}
```
Assignee: joyner

The method "word_problem" in the matrix groups class is broken in two separate ways. Firstly, it's supposed to allow you to specify a custom set of generators but it silently ignores them and uses the default ones. Secondly, it returns a Factorization object which assumes (!) that the group is commutative, and hence the results are complete junk for nonabelian groups.

I have a rough patch for this but it needs some polishing (mainly adding tests and docstrings).

Issue created by migration from https://trac.sagemath.org/ticket/8957





---

archive/issue_comments_082566.json:
```json
{
    "body": "patch against 4.4.1",
    "created_at": "2010-05-15T18:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8957#issuecomment-82566",
    "user": "davidloeffler"
}
```

patch against 4.4.1



---

archive/issue_comments_082567.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-15T18:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8957#issuecomment-82567",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082568.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-15T18:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8957#issuecomment-82568",
    "user": "davidloeffler"
}
```

Attachment



---

archive/issue_comments_082569.json:
```json
{
    "body": "The code seems reasonable, the docstring looks good, applies to 4.4.2.a0 okay and passes sage -testall\n(except for unrelated failures).",
    "created_at": "2010-05-16T01:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8957#issuecomment-82569",
    "user": "wdj"
}
```

The code seems reasonable, the docstring looks good, applies to 4.4.2.a0 okay and passes sage -testall
(except for unrelated failures).



---

archive/issue_comments_082570.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-16T01:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8957#issuecomment-82570",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082571.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T20:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8957#issuecomment-82571",
    "user": "mhansen"
}
```

Resolution: fixed
