# Issue 8287: The _check used for creation of words makes it slower

archive/issues_008287.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  vdelecroix\n\nThe `_check` function of the Combinatorial class of all words (checking that the 40 first letters of the word are in the parent) is called for each word created by the user ....and by any other function. It would be good to add a check parameter (True or False) whether to do the checking. For example, for internal function, it could be turned off. Here is a example of what can be gained from this modification when generating all words of a given length :\n\nBEFORE:\n\n```\nsage: W = Words([0,1])\nsage: time l = list(W.iterate_by_length(15))\nCPU times: user 2.60 s, sys: 0.09 s, total: 2.69 s\nWall time: 2.71 s\n```\n\n\nAFTER:\n\n\n```\nsage: W = Words([0,1])\nsage: time l = list(W.iterate_by_length(15))\nCPU times: user 1.99 s, sys: 0.06 s, total: 2.05 s\nWall time: 2.08 s\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8287\n\n",
    "created_at": "2010-02-16T22:12:09Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "The _check used for creation of words makes it slower",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8287",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  vdelecroix

The `_check` function of the Combinatorial class of all words (checking that the 40 first letters of the word are in the parent) is called for each word created by the user ....and by any other function. It would be good to add a check parameter (True or False) whether to do the checking. For example, for internal function, it could be turned off. Here is a example of what can be gained from this modification when generating all words of a given length :

BEFORE:

```
sage: W = Words([0,1])
sage: time l = list(W.iterate_by_length(15))
CPU times: user 2.60 s, sys: 0.09 s, total: 2.69 s
Wall time: 2.71 s
```


AFTER:


```
sage: W = Words([0,1])
sage: time l = list(W.iterate_by_length(15))
CPU times: user 1.99 s, sys: 0.06 s, total: 2.05 s
Wall time: 2.08 s
```




Issue created by migration from https://trac.sagemath.org/ticket/8287





---

archive/issue_comments_073378.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-17T00:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8287#issuecomment-73378",
    "user": "slabbe"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_073379.json:
```json
{
    "body": "Attachment [trac_8287_check-sl.patch](tarball://root/attachments/some-uuid/ticket8287/trac_8287_check-sl.patch) by slabbe created at 2010-02-17 00:03:44",
    "created_at": "2010-02-17T00:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8287#issuecomment-73379",
    "user": "slabbe"
}
```

Attachment [trac_8287_check-sl.patch](tarball://root/attachments/some-uuid/ticket8287/trac_8287_check-sl.patch) by slabbe created at 2010-02-17 00:03:44



---

archive/issue_comments_073380.json:
```json
{
    "body": "It was done last year in #17021. I suggest to close this ticket as duplicate.",
    "created_at": "2015-12-02T10:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8287#issuecomment-73380",
    "user": "slabbe"
}
```

It was done last year in #17021. I suggest to close this ticket as duplicate.



---

archive/issue_comments_073381.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-12-02T10:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8287#issuecomment-73381",
    "user": "slabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073382.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-12-02T19:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8287#issuecomment-73382",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073383.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-12-04T22:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8287#issuecomment-73383",
    "user": "vbraun"
}
```

Resolution: fixed
