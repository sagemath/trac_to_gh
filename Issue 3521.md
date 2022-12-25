# Issue 3521: Atkin-Lehner operator doesn't square to 1

archive/issues_003521.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: modular symbols, atkin-lehner\n\nThe following should produce the identity matrix:\n\n```\nsage: e = (DirichletGroup(13).0)^2\nsage: M = ModularSymbols(e, 2)\nsage: M.atkin_lehner_operator().matrix()^2\n[         1          0          0          0]\n[         0          1          0          0]\n[-zeta6 - 1          0          1  zeta6 + 1]\n[ zeta6 + 1          0          0     -zeta6]\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3521\n\n",
    "created_at": "2008-06-27T14:02:05Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Atkin-Lehner operator doesn't square to 1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3521",
    "user": "https://github.com/roed314"
}
```
Assignee: @craigcitro

Keywords: modular symbols, atkin-lehner

The following should produce the identity matrix:

```
sage: e = (DirichletGroup(13).0)^2
sage: M = ModularSymbols(e, 2)
sage: M.atkin_lehner_operator().matrix()^2
[         1          0          0          0]
[         0          1          0          0]
[-zeta6 - 1          0          1  zeta6 + 1]
[ zeta6 + 1          0          0     -zeta6]


Issue created by migration from https://trac.sagemath.org/ticket/3521





---

archive/issue_comments_024766.json:
```json
{
    "body": "For me this illustrates the bug more clearly:\n\n```\nsage: M = ModularSymbols(Gamma1(13),2)\nsage: M\nModular Symbols space of dimension 15 for Gamma_1(13) of weight 2 with sign 0 and over Rational Field\nsage: M.atkin_lehner_operator(13).matrix()^2 == 1\nTrue\nsage: M = ModularSymbols(DirichletGroup(13).0^2)\nsage: M.atkin_lehner_operator(13).matrix()^2 == 1\nFalse\nsage: M.atkin_lehner_operator(13).matrix()^2 \n\n[         1          0          0          0]\n[         0          1          0          0]\n[-zeta6 - 1          0          1  zeta6 + 1]\n[ zeta6 + 1          0          0     -zeta6]\n```\n",
    "created_at": "2008-06-27T14:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24766",
    "user": "https://github.com/williamstein"
}
```

For me this illustrates the bug more clearly:

```
sage: M = ModularSymbols(Gamma1(13),2)
sage: M
Modular Symbols space of dimension 15 for Gamma_1(13) of weight 2 with sign 0 and over Rational Field
sage: M.atkin_lehner_operator(13).matrix()^2 == 1
True
sage: M = ModularSymbols(DirichletGroup(13).0^2)
sage: M.atkin_lehner_operator(13).matrix()^2 == 1
False
sage: M.atkin_lehner_operator(13).matrix()^2 

[         1          0          0          0]
[         0          1          0          0]
[-zeta6 - 1          0          1  zeta6 + 1]
[ zeta6 + 1          0          0     -zeta6]
```




---

archive/issue_comments_024767.json:
```json
{
    "body": "Attachment [sage-3521.patch](tarball://root/attachments/some-uuid/ticket3521/sage-3521.patch) by @williamstein created at 2008-06-27 19:31:12\n\nWARNING:\n\nThe atkin-lehner operator does *not* leave the space $M_k(N,\\chi)$ invariant unless $\\chi$ is quadratic. Really it sends $M_k(N,\\chi)$ to $M_k(N,\\chibar)$.   So Sage should give an error message when $\\chi$ is not quadratic.",
    "created_at": "2008-06-27T19:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24767",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3521.patch](tarball://root/attachments/some-uuid/ticket3521/sage-3521.patch) by @williamstein created at 2008-06-27 19:31:12

WARNING:

The atkin-lehner operator does *not* leave the space $M_k(N,\chi)$ invariant unless $\chi$ is quadratic. Really it sends $M_k(N,\chi)$ to $M_k(N,\chibar)$.   So Sage should give an error message when $\chi$ is not quadratic.



---

archive/issue_comments_024768.json:
```json
{
    "body": "Attachment [trac-3521-touch-ups.patch](tarball://root/attachments/some-uuid/ticket3521/trac-3521-touch-ups.patch) by @craigcitro created at 2008-06-29 02:04:50",
    "created_at": "2008-06-29T02:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24768",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-3521-touch-ups.patch](tarball://root/attachments/some-uuid/ticket3521/trac-3521-touch-ups.patch) by @craigcitro created at 2008-06-29 02:04:50



---

archive/issue_comments_024769.json:
```json
{
    "body": "Looks good. I added a patch that actually corrects a bug (some statements were out of order), and just reformats/corrects typos. This is ready to go.",
    "created_at": "2008-06-29T02:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24769",
    "user": "https://github.com/craigcitro"
}
```

Looks good. I added a patch that actually corrects a bug (some statements were out of order), and just reformats/corrects typos. This is ready to go.



---

archive/issue_comments_024770.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-02T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24770",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_events_008035.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-02T19:30:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3521#event-8035"
}
```



---

archive/issue_events_008036.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-02T19:30:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3521#event-8036"
}
```



---

archive/issue_comments_024771.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-02T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24771",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
