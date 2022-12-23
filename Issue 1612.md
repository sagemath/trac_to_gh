# Issue 1612: Finding eigenforms within spaces of ModularForms

archive/issues_001612.json:
```json
{
    "body": "Assignee: was\n\nThere doesn't seem to be a way to find eigenforms within spaces of modular forms.\n\nAlso, the sturm_bound and hecke_bound methods seem not to work:\n\n\n```\nS37=CuspForms(37,2)\nS37.sturm_bound()}}}\n\n{{{Exception (click to the left for traceback):\n...\nAttributeError: 'CuspidalSubmodule_g0_Q' object has no attribute '_ModularFormsSpace__sturm_bound'}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/1612\n\n",
    "created_at": "2007-12-27T16:23:08Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "Finding eigenforms within spaces of ModularForms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1612",
    "user": "ljpk"
}
```
Assignee: was

There doesn't seem to be a way to find eigenforms within spaces of modular forms.

Also, the sturm_bound and hecke_bound methods seem not to work:


```
S37=CuspForms(37,2)
S37.sturm_bound()}}}

{{{Exception (click to the left for traceback):
...
AttributeError: 'CuspidalSubmodule_g0_Q' object has no attribute '_ModularFormsSpace__sturm_bound'}}}

Issue created by migration from https://trac.sagemath.org/ticket/1612





---

archive/issue_comments_010258.json:
```json
{
    "body": "These are two separate issues.  The second one is now #1736.",
    "created_at": "2008-01-09T12:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1612#issuecomment-10258",
    "user": "AlexGhitza"
}
```

These are two separate issues.  The second one is now #1736.



---

archive/issue_comments_010259.json:
```json
{
    "body": "This is already fixed. (Most of this came in with the new modular abelian varieties code.)",
    "created_at": "2008-06-15T02:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1612#issuecomment-10259",
    "user": "craigcitro"
}
```

This is already fixed. (Most of this came in with the new modular abelian varieties code.)



---

archive/issue_comments_010260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T02:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1612#issuecomment-10260",
    "user": "craigcitro"
}
```

Resolution: fixed
