# Issue 1448: iterate over MatrixSpace

archive/issues_001448.json:
```json
{
    "body": "Assignee: was\n\nThis should work:\n\n```\nsage: MS = MatrixSpace(GF(2),2)\nsage: for A in MS:\n...     print A\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1448\n\n",
    "created_at": "2007-12-10T14:20:20Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "title": "iterate over MatrixSpace",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1448",
    "user": "malb"
}
```
Assignee: was

This should work:

```
sage: MS = MatrixSpace(GF(2),2)
sage: for A in MS:
...     print A
```


Issue created by migration from https://trac.sagemath.org/ticket/1448





---

archive/issue_comments_009327.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-14T07:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1448#issuecomment-9327",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_009328.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-14T07:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1448#issuecomment-9328",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009329.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-14T07:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1448#issuecomment-9329",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_009330.json:
```json
{
    "body": "Attachment\n\nI've been reviewing this patch. Generally pretty good (I like the implementation for infinite base rings, very neat)... a few minor issues to address:\n\n* I'd like to see more (i.e. nonzero) documentation in the docstring, in particular giving the definition of what ordering is being produced, and explaining what's going on in the case of an infinite base ring\n\n* The doctests should show more than that just the number of generated matrices is correct; currently they only give the number of matrices and the first matrix (which is all zero)\n\n* I'm a bit puzzled by the order of iteration. It starts by incrementing in the bottom right and then moves upwards. To me the other direction seems more natural. Maybe I'm \"wrong\" about this though.\n\n* There are some corner cases to address:\n\n\n```\nsage: MS = MatrixSpace(ZZ, 2, 0)\nsage: i = iter(MS)\nsage: i.next()\n[]\nsage: i.next()\n(boom)\n```\n\n\n* The doctests should include examples for 0xN, Nx0, 0x0 matrices.",
    "created_at": "2007-12-21T17:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1448#issuecomment-9330",
    "user": "dmharvey"
}
```

Attachment

I've been reviewing this patch. Generally pretty good (I like the implementation for infinite base rings, very neat)... a few minor issues to address:

* I'd like to see more (i.e. nonzero) documentation in the docstring, in particular giving the definition of what ordering is being produced, and explaining what's going on in the case of an infinite base ring

* The doctests should show more than that just the number of generated matrices is correct; currently they only give the number of matrices and the first matrix (which is all zero)

* I'm a bit puzzled by the order of iteration. It starts by incrementing in the bottom right and then moves upwards. To me the other direction seems more natural. Maybe I'm "wrong" about this though.

* There are some corner cases to address:


```
sage: MS = MatrixSpace(ZZ, 2, 0)
sage: i = iter(MS)
sage: i.next()
[]
sage: i.next()
(boom)
```


* The doctests should include examples for 0xN, Nx0, 0x0 matrices.



---

archive/issue_comments_009331.json:
```json
{
    "body": "Attachment\n\nok, I'm happy with this now.",
    "created_at": "2007-12-22T16:14:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1448#issuecomment-9331",
    "user": "dmharvey"
}
```

Attachment

ok, I'm happy with this now.



---

archive/issue_comments_009332.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T17:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1448#issuecomment-9332",
    "user": "rlm"
}
```

merged in 2.9.1 rc0



---

archive/issue_comments_009333.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T17:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1448#issuecomment-9333",
    "user": "rlm"
}
```

Resolution: fixed
