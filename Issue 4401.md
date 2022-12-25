# Issue 4401: Sage 3.1.4: magma related optional doctest failure in sage/crypto/mq/mpolynomialsystem.py

archive/issues_004401.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage -t -long -optional devel/sage/sage/crypto/mq/mpolynomialsystem.py\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/mpolynomialsystem.py\", line 851:\n    sage: F._magma_() # optional, requires MAGMA\nExpected nothing\nGot:\n    Ideal of Polynomial ring of rank 20 over GF(2)\n    Graded Reverse Lexicographical Order\n    Variables: k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003, k000, k001, k002, k003\n    Basis:\n    [\n    w100 + k000 + 1,\n    w101 + k001,\n    w102 + k002 + 1,\n    w103 + k003 + 1,\n    k000^2 + k000,\n    k001^2 + k001,\n    k002^2 + k002,\n    k003^2 + k003,\n    k100 + x100 + x102 + x103 + 1,\n    k101 + x100 + x101 + x103,\n    k102 + x100 + x101 + x102 + 1,\n    k103 + x101 + x102 + x103,\n    x100*w100 + x103*w100 + x102*w101 + x101*w102 + x100*w103,\n    x100*w100 + x101*w100 + x100*w101 + x103*w101 + x102*w102 + x101*w103,\n    x101*w100 + x102*w100 + x100*w101 + x101*w101 + x100*w102 + x103*w102 + x102*w103,\n    x102*w100 + x101*w101 + x100*w102 + x103*w103 + 1,\n    x100*w100 + x101*w100 + x103*w100 + x101*w101 + x100*w102 + x102*w102 + x100*w103 + x100,\n    x102*w100 + x100*w101 + x101*w101 + x103*w101 + x101*w102 + x100*w103 + x102*w103 + x101,\n    x100*w100 + x101*w100 + x102*w100 + x102*w101 + x100*w102 + x101*w102 + x103*w102 + x101*w103 + x102,\n    x101*w100 + x100*w101 + x102*w101 + x100*w102 + x101*w103 + x103*w103 + x103,\n    x100*w100 + x102*w100 + x103*w100 + x100*w101 + x101*w101 + x102*w102 + x100*w103 + w100,\n    x101*w100 + x103*w100 + x101*w101 + x102*w101 + x100*w102 + x103*w102 + x101*w103 + w101,\n    x100*w100 + x102*w100 + x100*w101 + x102*w101 + x103*w101 + x100*w102 + x101*w102 + x102*w103 + w102,\n    x101*w100 + x102*w100 + x100*w101 + x103*w101 + x101*w102 + x103*w103 + w103,\n    x100^2 + x100,\n    x101^2 + x101,\n    x102^2 + x102,\n    x103^2 + x103,\n    w100^2 + w100,\n    w101^2 + w101,\n    w102^2 + w102,\n    w103^2 + w103,\n    k100 + s000 + s002 + s003,\n    k101 + s000 + s001 + s003 + 1,\n    k102 + s000 + s001 + s002 + 1,\n    k103 + s001 + s002 + s003 + 1,\n    k100^2 + k100,\n    k101^2 + k101,\n    k102^2 + k102,\n    k103^2 + k103,\n    s000^2 + s000,\n    s001^2 + s001,\n    s002^2 + s002,\n    s003^2 + s003,\n    s000*k000 + s003*k000 + s002*k001 + s001*k002 + s000*k003,\n    s000*k000 + s001*k000 + s000*k001 + s003*k001 + s002*k002 + s001*k003,\n    s001*k000 + s002*k000 + s000*k001 + s001*k001 + s000*k002 + s003*k002 + s002*k003,\n    s002*k000 + s001*k001 + s000*k002 + s003*k003 + 1,\n    s000*k000 + s002*k000 + s003*k000 + s000*k001 + s001*k001 + s002*k002 + s000*k003 + k000,\n    s001*k000 + s003*k000 + s001*k001 + s002*k001 + s000*k002 + s003*k002 + s001*k003 + k001,\n    s000*k000 + s002*k000 + s000*k001 + s002*k001 + s003*k001 + s000*k002 + s001*k002 + s002*k003 + k002,\n    s001*k000 + s002*k000 + s000*k001 + s003*k001 + s001*k002 + s003*k003 + k003,\n    s000*k000 + s001*k000 + s003*k000 + s001*k001 + s000*k002 + s002*k002 + s000*k003 + s000,\n    s002*k000 + s000*k001 + s001*k001 + s003*k001 + s001*k002 + s000*k003 + s002*k003 + s001,\n    s000*k000 + s001*k000 + s002*k000 + s002*k001 + s000*k002 + s001*k002 + s003*k002 + s001*k003 + s002,\n    s001*k000 + s000*k001 + s002*k001 + s000*k002 + s001*k003 + s003*k003 + s003\n    ]\n**********************************************************************\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4401\n\n",
    "closed_at": "2008-11-24T22:54:06Z",
    "created_at": "2008-10-30T17:33:04Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Sage 3.1.4: magma related optional doctest failure in sage/crypto/mq/mpolynomialsystem.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4401",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

```
sage -t -long -optional devel/sage/sage/crypto/mq/mpolynomialsystem.py
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/mpolynomialsystem.py", line 851:
    sage: F._magma_() # optional, requires MAGMA
Expected nothing
Got:
    Ideal of Polynomial ring of rank 20 over GF(2)
    Graded Reverse Lexicographical Order
    Variables: k100, k101, k102, k103, x100, x101, x102, x103, w100, w101, w102, w103, s000, s001, s002, s003, k000, k001, k002, k003
    Basis:
    [
    w100 + k000 + 1,
    w101 + k001,
    w102 + k002 + 1,
    w103 + k003 + 1,
    k000^2 + k000,
    k001^2 + k001,
    k002^2 + k002,
    k003^2 + k003,
    k100 + x100 + x102 + x103 + 1,
    k101 + x100 + x101 + x103,
    k102 + x100 + x101 + x102 + 1,
    k103 + x101 + x102 + x103,
    x100*w100 + x103*w100 + x102*w101 + x101*w102 + x100*w103,
    x100*w100 + x101*w100 + x100*w101 + x103*w101 + x102*w102 + x101*w103,
    x101*w100 + x102*w100 + x100*w101 + x101*w101 + x100*w102 + x103*w102 + x102*w103,
    x102*w100 + x101*w101 + x100*w102 + x103*w103 + 1,
    x100*w100 + x101*w100 + x103*w100 + x101*w101 + x100*w102 + x102*w102 + x100*w103 + x100,
    x102*w100 + x100*w101 + x101*w101 + x103*w101 + x101*w102 + x100*w103 + x102*w103 + x101,
    x100*w100 + x101*w100 + x102*w100 + x102*w101 + x100*w102 + x101*w102 + x103*w102 + x101*w103 + x102,
    x101*w100 + x100*w101 + x102*w101 + x100*w102 + x101*w103 + x103*w103 + x103,
    x100*w100 + x102*w100 + x103*w100 + x100*w101 + x101*w101 + x102*w102 + x100*w103 + w100,
    x101*w100 + x103*w100 + x101*w101 + x102*w101 + x100*w102 + x103*w102 + x101*w103 + w101,
    x100*w100 + x102*w100 + x100*w101 + x102*w101 + x103*w101 + x100*w102 + x101*w102 + x102*w103 + w102,
    x101*w100 + x102*w100 + x100*w101 + x103*w101 + x101*w102 + x103*w103 + w103,
    x100^2 + x100,
    x101^2 + x101,
    x102^2 + x102,
    x103^2 + x103,
    w100^2 + w100,
    w101^2 + w101,
    w102^2 + w102,
    w103^2 + w103,
    k100 + s000 + s002 + s003,
    k101 + s000 + s001 + s003 + 1,
    k102 + s000 + s001 + s002 + 1,
    k103 + s001 + s002 + s003 + 1,
    k100^2 + k100,
    k101^2 + k101,
    k102^2 + k102,
    k103^2 + k103,
    s000^2 + s000,
    s001^2 + s001,
    s002^2 + s002,
    s003^2 + s003,
    s000*k000 + s003*k000 + s002*k001 + s001*k002 + s000*k003,
    s000*k000 + s001*k000 + s000*k001 + s003*k001 + s002*k002 + s001*k003,
    s001*k000 + s002*k000 + s000*k001 + s001*k001 + s000*k002 + s003*k002 + s002*k003,
    s002*k000 + s001*k001 + s000*k002 + s003*k003 + 1,
    s000*k000 + s002*k000 + s003*k000 + s000*k001 + s001*k001 + s002*k002 + s000*k003 + k000,
    s001*k000 + s003*k000 + s001*k001 + s002*k001 + s000*k002 + s003*k002 + s001*k003 + k001,
    s000*k000 + s002*k000 + s000*k001 + s002*k001 + s003*k001 + s000*k002 + s001*k002 + s002*k003 + k002,
    s001*k000 + s002*k000 + s000*k001 + s003*k001 + s001*k002 + s003*k003 + k003,
    s000*k000 + s001*k000 + s003*k000 + s001*k001 + s000*k002 + s002*k002 + s000*k003 + s000,
    s002*k000 + s000*k001 + s001*k001 + s003*k001 + s001*k002 + s000*k003 + s002*k003 + s001,
    s000*k000 + s001*k000 + s002*k000 + s002*k001 + s000*k002 + s001*k002 + s003*k002 + s001*k003 + s002,
    s001*k000 + s000*k001 + s002*k001 + s000*k002 + s001*k003 + s003*k003 + s003
    ]
**********************************************************************
```

Issue created by migration from https://trac.sagemath.org/ticket/4401





---

archive/issue_comments_032306.json:
```json
{
    "body": "Fixed in Sage 3.2.1.alpha1 via #4601.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-24T22:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4401#issuecomment-32306",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.2.1.alpha1 via #4601.

Cheers,

Michael



---

archive/issue_comments_032307.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-24T22:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4401#issuecomment-32307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009936.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-24T22:54:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4401",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4401#event-9936"
}
```
