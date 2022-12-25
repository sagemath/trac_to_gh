# Issue 4356: modular forms -- echelon_form broken

archive/issues_004356.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis used to work (e.g., it is in my modular forms book), but now it doesn't.  No clue why it is broken:\n\n```\nsage: M = ModularForms(1,36, prec=10).echelon_form()\nTraceback (most recent call last):\n...\nValueError: The given basis vectors must be linearly independent.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4356\n\n",
    "created_at": "2008-10-24T02:03:06Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "modular forms -- echelon_form broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4356",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

This used to work (e.g., it is in my modular forms book), but now it doesn't.  No clue why it is broken:

```
sage: M = ModularForms(1,36, prec=10).echelon_form()
Traceback (most recent call last):
...
ValueError: The given basis vectors must be linearly independent.
```


Issue created by migration from https://trac.sagemath.org/ticket/4356





---

archive/issue_comments_031935.json:
```json
{
    "body": "So I can't find any examples that don't work ... in my copy of 3.1.4, I get:\n\n\n```\nsage: M = ModularForms(1, 36, prec=6).echelon_form()\nsage: M.basis()\n[\n1 + 6218175600*q^4 + 15281788354560*q^5 + O(q^6),\nq + 57093088*q^4 + 37927345230*q^5 + O(q^6),\nq^2 + 194184*q^4 + 7442432*q^5 + O(q^6),\nq^3 - 72*q^4 + 2484*q^5 + O(q^6)\n]\n```\n\n\nWhat machine were you running into this on?",
    "created_at": "2008-10-24T08:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4356#issuecomment-31935",
    "user": "https://github.com/craigcitro"
}
```

So I can't find any examples that don't work ... in my copy of 3.1.4, I get:


```
sage: M = ModularForms(1, 36, prec=6).echelon_form()
sage: M.basis()
[
1 + 6218175600*q^4 + 15281788354560*q^5 + O(q^6),
q + 57093088*q^4 + 37927345230*q^5 + O(q^6),
q^2 + 194184*q^4 + 7442432*q^5 + O(q^6),
q^3 - 72*q^4 + 2484*q^5 + O(q^6)
]
```


What machine were you running into this on?



---

archive/issue_comments_031936.json:
```json
{
    "body": "This is invalid.  I was thrown off by a my messed up #4347!",
    "created_at": "2008-10-30T16:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4356#issuecomment-31936",
    "user": "https://github.com/williamstein"
}
```

This is invalid.  I was thrown off by a my messed up #4347!



---

archive/issue_comments_031937.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-10-30T16:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4356#issuecomment-31937",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid
