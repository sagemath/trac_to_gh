# Issue 6213: easy addition of an alias to eta product (trivial ticket to deal with)

archive/issues_006213.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @loefflerd\n\n\n```\n    Hi David,\n\n    This is inconsistent:\n\n\n    sage: e =EtaProduct(3, {3:12, 1:-12})\n    sage: e.qexp(10)  # but no q_expansion function\n\n    Everywhere else in Sage we write \"q_expansion\" and have qexp as an alias. It thus took me a while to find e.qexp, since I expected e.q_expansion. What do you think?\n\n\nAgreed. I wrote most of that class during a lunch break at a conference last summer, and at the time I didn't have much of a clue about Sage conventions (as is probably clear to anyone reading the code). Please feel free to change it!\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6213\n\n",
    "created_at": "2009-06-04T21:01:26Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "easy addition of an alias to eta product (trivial ticket to deal with)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6213",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @loefflerd


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

archive/issue_comments_049539.json:
```json
{
    "body": "Attachment [trac-6213.patch](tarball://root/attachments/some-uuid/ticket6213/trac-6213.patch) by @craigcitro created at 2009-06-05 06:31:57",
    "created_at": "2009-06-05T06:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49539",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6213.patch](tarball://root/attachments/some-uuid/ticket6213/trac-6213.patch) by @craigcitro created at 2009-06-05 06:31:57



---

archive/issue_comments_049540.json:
```json
{
    "body": "Quick and easy fix attached.",
    "created_at": "2009-06-05T06:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49540",
    "user": "https://github.com/craigcitro"
}
```

Quick and easy fix attached.



---

archive/issue_comments_049541.json:
```json
{
    "body": "that was easy :-)",
    "created_at": "2009-06-05T07:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49541",
    "user": "https://github.com/williamstein"
}
```

that was easy :-)



---

archive/issue_comments_049542.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2009-06-07T13:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49542",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_049543.json:
```json
{
    "body": "This clearly belongs in component = modular forms (not that it really matters).",
    "created_at": "2009-06-07T13:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49543",
    "user": "https://github.com/loefflerd"
}
```

This clearly belongs in component = modular forms (not that it really matters).



---

archive/issue_comments_049544.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2009-06-07T13:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49544",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_049545.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49545",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_014573.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-13T21:07:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6213#event-14573"
}
```



---

archive/issue_comments_049546.json:
```json
{
    "body": "William should get reviewer credit for this, not me.",
    "created_at": "2009-06-16T11:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6213#issuecomment-49546",
    "user": "https://github.com/loefflerd"
}
```

William should get reviewer credit for this, not me.
