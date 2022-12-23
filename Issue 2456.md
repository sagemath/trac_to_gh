# Issue 2456: matrix_symbolic_dense doctest failures

archive/issues_002456.json:
```json
{
    "body": "Assignee: was\n\n\n```\nFile \"matrix_symbolic_dense.pyx\", line 873:\n    sage: list(a.fcp())\nExpected:\n    [(x^2 - 65*x - 250, 1), (x, 3)]\nGot:\n    [(x, 3), (x^2 - 65*x - 250, 1)]\n```\n\nBut inside sage:\n\n```\nsage: a = matrix(SR, 5, [1..5^2]) \nsage: a.fcp()\n(x^2 - 65*x - 250) * x^3\nsage: list(a.fcp())\n[(x^2 - 65*x - 250, 1), (x, 3)]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2456\n\n",
    "created_at": "2008-03-10T13:53:55Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "title": "matrix_symbolic_dense doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2456",
    "user": "gfurnish"
}
```
Assignee: was


```
File "matrix_symbolic_dense.pyx", line 873:
    sage: list(a.fcp())
Expected:
    [(x^2 - 65*x - 250, 1), (x, 3)]
Got:
    [(x, 3), (x^2 - 65*x - 250, 1)]
```

But inside sage:

```
sage: a = matrix(SR, 5, [1..5^2]) 
sage: a.fcp()
(x^2 - 65*x - 250) * x^3
sage: list(a.fcp())
[(x^2 - 65*x - 250, 1), (x, 3)]
```


Issue created by migration from https://trac.sagemath.org/ticket/2456





---

archive/issue_comments_016631.json:
```json
{
    "body": "This patch is correct because of changes in #2206",
    "created_at": "2008-03-10T14:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16631",
    "user": "gfurnish"
}
```

This patch is correct because of changes in #2206



---

archive/issue_comments_016632.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-10T14:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16632",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_016633.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T14:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16633",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016634.json:
```json
{
    "body": "This patch fixes problems in factorization that cause problems here.",
    "created_at": "2008-03-10T15:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16634",
    "user": "gfurnish"
}
```

This patch fixes problems in factorization that cause problems here.



---

archive/issue_comments_016635.json:
```json
{
    "body": "REFEREE REPORT:\n\n* The second chunk in trac_2456.patch, which swaps the order of sort and simplify, breaks things.  This is because simplify assumes its input is sorted, as it combines adjacent pairs.\n\n* The rest of the patch looks fine.",
    "created_at": "2008-03-10T16:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16635",
    "user": "was"
}
```

REFEREE REPORT:

* The second chunk in trac_2456.patch, which swaps the order of sort and simplify, breaks things.  This is because simplify assumes its input is sorted, as it combines adjacent pairs.

* The rest of the patch looks fine.



---

archive/issue_comments_016636.json:
```json
{
    "body": "Attachment\n\nreplaced patch addresses my concern.",
    "created_at": "2008-03-10T16:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16636",
    "user": "was"
}
```

Attachment

replaced patch addresses my concern.



---

archive/issue_comments_016637.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-10T17:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16637",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016638.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc4",
    "created_at": "2008-03-10T17:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2456#issuecomment-16638",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc4
