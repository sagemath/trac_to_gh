# Issue 6213: easy addition of an alias to eta product (trivial ticket to deal with)

archive/issues_006213.json:
```json
{
    "body": "Assignee: was\n\nCC:  davidloeffler\n\n\n```\n    Hi David,\n\n    This is inconsistent:\n\n\n    sage: e =EtaProduct(3, {3:12, 1:-12})\n    sage: e.qexp(10)  # but no q_expansion function\n\n    Everywhere else in Sage we write \"q_expansion\" and have qexp as an alias. It thus took me a while to find e.qexp, since I expected e.q_expansion. What do you think?\n\n\nAgreed. I wrote most of that class during a lunch break at a conference last summer, and at the time I didn't have much of a clue about Sage conventions (as is probably clear to anyone reading the code). Please feel free to change it!\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6213\n\n",
    "created_at": "2009-06-04T21:01:26Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "easy addition of an alias to eta product (trivial ticket to deal with)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6213",
    "user": "was"
}
```
Assignee: was

CC:  davidloeffler


```
    Hi David,

    This is inconsistent:


    sage: e =EtaProduct(3, {3:12, 1:-12})
    sage: e.qexp(10)  # but no q_expansion function

    Everywhere else in Sage we write "q_expansion" and have qexp as an alias. It thus took me a while to find e.qexp, since I expected e.q_expansion. What do you think?


Agreed. I wrote most of that class during a lunch break at a conference last summer, and at the time I didn't have much of a clue about Sage conventions (as is probably clear to anyone reading the code). Please feel free to change it!

```


Issue created by migration from https://trac.sagemath.org/ticket/6213





---

archive/issue_comments_049634.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-05T06:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49634",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_049635.json:
```json
{
    "body": "Quick and easy fix attached.",
    "created_at": "2009-06-05T06:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49635",
    "user": "craigcitro"
}
```

Quick and easy fix attached.



---

archive/issue_comments_049636.json:
```json
{
    "body": "that was easy :-)",
    "created_at": "2009-06-05T07:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49636",
    "user": "was"
}
```

that was easy :-)



---

archive/issue_comments_049637.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2009-06-07T13:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49637",
    "user": "davidloeffler"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_049638.json:
```json
{
    "body": "This clearly belongs in component = modular forms (not that it really matters).",
    "created_at": "2009-06-07T13:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49638",
    "user": "davidloeffler"
}
```

This clearly belongs in component = modular forms (not that it really matters).



---

archive/issue_comments_049639.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2009-06-07T13:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49639",
    "user": "davidloeffler"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_049640.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49640",
    "user": "ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_049641.json:
```json
{
    "body": "William should get reviewer credit for this, not me.",
    "created_at": "2009-06-16T11:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49641",
    "user": "davidloeffler"
}
```

William should get reviewer credit for this, not me.
