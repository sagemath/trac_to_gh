# Issue 1906: [with patch, with positive review] eisenstein_series_qexp does not pay attention to the field parameter

archive/issues_001906.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe function eisenstein_series_qexp() has a parameter K which is supposed to say what field the coefficients of the series should live in, but it always returns rational coefficients:\n\n```\nsage: eisenstein_series_qexp(10,6,GF(5))\n-1/264 + q + 513*q^2 + 19684*q^3 + 262657*q^4 + 1953126*q^5 + O(q^6)\nsage: eisenstein_series_qexp(10,6,QQ)\n-1/264 + q + 513*q^2 + 19684*q^3 + 262657*q^4 + 1953126*q^5 + O(q^6)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1906\n\n",
    "closed_at": "2008-01-25T18:13:00Z",
    "created_at": "2008-01-24T03:34:38Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, with positive review] eisenstein_series_qexp does not pay attention to the field parameter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1906",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

The function eisenstein_series_qexp() has a parameter K which is supposed to say what field the coefficients of the series should live in, but it always returns rational coefficients:

```
sage: eisenstein_series_qexp(10,6,GF(5))
-1/264 + q + 513*q^2 + 19684*q^3 + 262657*q^4 + 1953126*q^5 + O(q^6)
sage: eisenstein_series_qexp(10,6,QQ)
-1/264 + q + 513*q^2 + 19684*q^3 + 262657*q^4 + 1953126*q^5 + O(q^6)
```

Issue created by migration from https://trac.sagemath.org/ticket/1906





---

archive/issue_comments_012042.json:
```json
{
    "body": "Attachment [1906-qexp-field.patch](tarball://root/attachments/some-uuid/ticket1906/1906-qexp-field.patch) by @aghitza created at 2008-01-24 03:37:29",
    "created_at": "2008-01-24T03:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1906#issuecomment-12042",
    "user": "https://github.com/aghitza"
}
```

Attachment [1906-qexp-field.patch](tarball://root/attachments/some-uuid/ticket1906/1906-qexp-field.patch) by @aghitza created at 2008-01-24 03:37:29



---

archive/issue_comments_012043.json:
```json
{
    "body": "Easy fix and new doctest -- see the attached patch.",
    "created_at": "2008-01-24T03:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1906#issuecomment-12043",
    "user": "https://github.com/aghitza"
}
```

Easy fix and new doctest -- see the attached patch.



---

archive/issue_comments_012044.json:
```json
{
    "body": "Looks good -- clearly I didn't even read the docstring to notice there was supposed to be a base_ring argument when rewriting this! :)\n\nOn a completely insignificant note, I'm not sure why you did a0inv = ..., and then K(1/a0inv) -- K(a0) would raise a ZeroDivisionError all the same. (It still works just fine, of course, it just confused me for a sec.)",
    "created_at": "2008-01-25T18:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1906#issuecomment-12044",
    "user": "https://github.com/craigcitro"
}
```

Looks good -- clearly I didn't even read the docstring to notice there was supposed to be a base_ring argument when rewriting this! :)

On a completely insignificant note, I'm not sure why you did a0inv = ..., and then K(1/a0inv) -- K(a0) would raise a ZeroDivisionError all the same. (It still works just fine, of course, it just confused me for a sec.)



---

archive/issue_events_004588.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-25T18:13:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1906",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1906#event-4588"
}
```



---

archive/issue_comments_012045.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T18:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1906#issuecomment-12045",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_012046.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T18:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1906#issuecomment-12046",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012047.json:
```json
{
    "body": "Craig: you're completely right about the a0inv thing, of course.  It's just that in the error message that we're raising I wanted to print the value of a0inv, and I couldn't think of a better way of doing it.",
    "created_at": "2008-01-25T23:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1906#issuecomment-12047",
    "user": "https://github.com/aghitza"
}
```

Craig: you're completely right about the a0inv thing, of course.  It's just that in the error message that we're raising I wanted to print the value of a0inv, and I couldn't think of a better way of doing it.
