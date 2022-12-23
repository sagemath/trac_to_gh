# Issue 3366: improve subs/subsitute inheritance

archive/issues_003366.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  jbmohler\n\njbmohler wrote at #1440:\n\"\"\"\nsubs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class. I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded. Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug. \n\"\"\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/3366\n\n",
    "created_at": "2008-06-04T20:39:40Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "improve subs/subsitute inheritance",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3366",
    "user": "malb"
}
```
Assignee: somebody

CC:  jbmohler

jbmohler wrote at #1440:
"""
subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class. I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded. Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug. 
"""

Issue created by migration from https://trac.sagemath.org/ticket/3366





---

archive/issue_comments_023553.json:
```json
{
    "body": "I don't understand the complaint; the entire point of subs is that you can subs override for different for things in different parents (such as calculus).  This is vague, can you give some concrete examples of things we can fix?",
    "created_at": "2008-06-09T06:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3366#issuecomment-23553",
    "user": "gfurnish"
}
```

I don't understand the complaint; the entire point of subs is that you can subs override for different for things in different parents (such as calculus).  This is vague, can you give some concrete examples of things we can fix?



---

archive/issue_comments_023554.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3366#issuecomment-23554",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_023555.json:
```json
{
    "body": "Let's just close this ticket.",
    "created_at": "2014-06-25T00:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3366#issuecomment-23555",
    "user": "malb"
}
```

Let's just close this ticket.



---

archive/issue_comments_023556.json:
```json
{
    "body": "Agreed.",
    "created_at": "2015-02-01T16:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3366#issuecomment-23556",
    "user": "rws"
}
```

Agreed.



---

archive/issue_comments_023557.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-02-01T16:08:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3366#issuecomment-23557",
    "user": "rws"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023558.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-01T16:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3366#issuecomment-23558",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023559.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2015-02-08T15:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3366#issuecomment-23559",
    "user": "vbraun"
}
```

Resolution: invalid
