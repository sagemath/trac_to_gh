# Issue 702: Ellipsis range notation

archive/issues_000702.json:
```json
{
    "body": "Assignee: was\n\nThere have been proposal to add syntax to SAGE similar to magma/mathmatica/etc 1..n for ranges. See the mailing list for much discusssion. \n\nIssue created by migration from https://trac.sagemath.org/ticket/702\n\n",
    "created_at": "2007-09-20T11:00:18Z",
    "labels": [
        "user interface",
        "major",
        "enhancement"
    ],
    "title": "Ellipsis range notation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/702",
    "user": "robertwb"
}
```
Assignee: was

There have been proposal to add syntax to SAGE similar to magma/mathmatica/etc 1..n for ranges. See the mailing list for much discusssion. 

Issue created by migration from https://trac.sagemath.org/ticket/702





---

archive/issue_comments_003681.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-20T11:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3681",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_003682.json:
```json
{
    "body": "The above patches are one such proposal. NOTE: it has not been decided whether or not to include this feature. However, I like it. \n\n\n```\nsage: [1..10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nsage: n = 5\nsage: [1..n]\n[1, 2, 3, 4, 5]\nsage: [0,2,..,10]\n[0, 2, 4, 6, 8, 10]\nsage: [0,2,..,10,20..30]\n[0, 2, 4, 6, 8, 10, 20, 22, 24, 26, 28, 30]\n\nsage: (0,2,..,10)       \n<generator object at 0xc57cd78>\nsage: A = (5,7,..)\nsage: [A.next() for _ in range(20)]\n[5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]\n\n```\n\n\nAnd a non-trivial example\n\n\n```\nsage: L = [1..5]\nsage: [L[4], .., next_prime(10), 3, 2, 1]\n[5, 6, 7, 8, 9, 10, 11, 3, 2, 1]\n```\n",
    "created_at": "2007-09-20T11:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3682",
    "user": "robertwb"
}
```

The above patches are one such proposal. NOTE: it has not been decided whether or not to include this feature. However, I like it. 


```
sage: [1..10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: n = 5
sage: [1..n]
[1, 2, 3, 4, 5]
sage: [0,2,..,10]
[0, 2, 4, 6, 8, 10]
sage: [0,2,..,10,20..30]
[0, 2, 4, 6, 8, 10, 20, 22, 24, 26, 28, 30]

sage: (0,2,..,10)       
<generator object at 0xc57cd78>
sage: A = (5,7,..)
sage: [A.next() for _ in range(20)]
[5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

```


And a non-trivial example


```
sage: L = [1..5]
sage: [L[4], .., next_prime(10), 3, 2, 1]
[5, 6, 7, 8, 9, 10, 11, 3, 2, 1]
```




---

archive/issue_comments_003683.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-20T11:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3683",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003684.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-09-20T11:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3684",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_003685.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-20T11:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3685",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_003686.json:
```json
{
    "body": "Fixed:\n\n\n```\nsage: A = (5,7,..)\nsage: [A.next() for _ in range(10)]\n[5, 7, 9, 11, 13, 15, 17, 19, 21, 23]\n```\n",
    "created_at": "2007-09-20T11:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3686",
    "user": "robertwb"
}
```

Fixed:


```
sage: A = (5,7,..)
sage: [A.next() for _ in range(10)]
[5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
```




---

archive/issue_comments_003687.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-20T19:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3687",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_003688.json:
```json
{
    "body": "Fixed an issue with double quotes, and now this works as well \n\n\n```\nsage: list(1..5)\n[1, 2, 3, 4, 5]\n```\n",
    "created_at": "2007-09-20T19:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3688",
    "user": "robertwb"
}
```

Fixed an issue with double quotes, and now this works as well 


```
sage: list(1..5)
[1, 2, 3, 4, 5]
```




---

archive/issue_comments_003689.json:
```json
{
    "body": "Attachment\n\nApplied.  (And I fixed a few bugs.)",
    "created_at": "2007-09-20T20:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3689",
    "user": "was"
}
```

Attachment

Applied.  (And I fixed a few bugs.)



---

archive/issue_comments_003690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-20T20:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3690",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_003691.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-21T22:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3691",
    "user": "robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003692.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-21T22:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3692",
    "user": "robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_003693.json:
```json
{
    "body": "[1,2,..,-10] should return the empty list.",
    "created_at": "2007-09-21T22:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3693",
    "user": "robertwb"
}
```

[1,2,..,-10] should return the empty list.



---

archive/issue_comments_003694.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-21T22:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3694",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_003695.json:
```json
{
    "body": "Fixed. \n\n\n```\nsage: [1,2..-1]\n[]\nsage: [10..1]\n[]\nsage: [1..10]\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nsage: [1..10,step=2] # no extra preparsing needed\n[1, 3, 5, 7, 9]\n```\n",
    "created_at": "2007-09-21T23:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3695",
    "user": "robertwb"
}
```

Fixed. 


```
sage: [1,2..-1]
[]
sage: [10..1]
[]
sage: [1..10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: [1..10,step=2] # no extra preparsing needed
[1, 3, 5, 7, 9]
```




---

archive/issue_comments_003696.json:
```json
{
    "body": "Why doesn't [10..1] return [10,9,8,7,6,5,4,3,2,1]?",
    "created_at": "2007-09-22T00:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3696",
    "user": "jason"
}
```

Why doesn't [10..1] return [10,9,8,7,6,5,4,3,2,1]?



---

archive/issue_comments_003697.json:
```json
{
    "body": "I don't think this should be an error:\n\n\n```\nsage: [1..5, step=0.5]\n<type 'exceptions.TypeError'>: unable to coerce element to an integer\n```\n\n\ni.e., the universe stuff should take into account the step if given.",
    "created_at": "2007-09-23T21:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3697",
    "user": "was"
}
```

I don't think this should be an error:


```
sage: [1..5, step=0.5]
<type 'exceptions.TypeError'>: unable to coerce element to an integer
```


i.e., the universe stuff should take into account the step if given.



---

archive/issue_comments_003698.json:
```json
{
    "body": "Fixed now by Robert...",
    "created_at": "2007-09-25T05:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3698",
    "user": "was"
}
```

Fixed now by Robert...



---

archive/issue_comments_003699.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-25T05:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/702#issuecomment-3699",
    "user": "was"
}
```

Resolution: fixed
