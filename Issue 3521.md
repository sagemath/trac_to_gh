# Issue 3521: Atkin-Lehner operator doesn't square to 1

archive/issues_003521.json:
```json
{
    "body": "Assignee: craigcitro\n\nKeywords: modular symbols, atkin-lehner\n\nThe following should produce the identity matrix:\n\n```\nsage: e = (DirichletGroup(13).0)^2\nsage: M = ModularSymbols(e, 2)\nsage: M.atkin_lehner_operator().matrix()^2\n[         1          0          0          0]\n[         0          1          0          0]\n[-zeta6 - 1          0          1  zeta6 + 1]\n[ zeta6 + 1          0          0     -zeta6]\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3521\n\n",
    "created_at": "2008-06-27T14:02:05Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Atkin-Lehner operator doesn't square to 1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3521",
    "user": "roed"
}
```
Assignee: craigcitro

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

archive/issue_comments_024815.json:
```json
{
    "body": "For me this illustrates the bug more clearly:\n\n```\nsage: M = ModularSymbols(Gamma1(13),2)\nsage: M\nModular Symbols space of dimension 15 for Gamma_1(13) of weight 2 with sign 0 and over Rational Field\nsage: M.atkin_lehner_operator(13).matrix()^2 == 1\nTrue\nsage: M = ModularSymbols(DirichletGroup(13).0^2)\nsage: M.atkin_lehner_operator(13).matrix()^2 == 1\nFalse\nsage: M.atkin_lehner_operator(13).matrix()^2 \n\n[         1          0          0          0]\n[         0          1          0          0]\n[-zeta6 - 1          0          1  zeta6 + 1]\n[ zeta6 + 1          0          0     -zeta6]\n```\n",
    "created_at": "2008-06-27T14:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24815",
    "user": "was"
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

archive/issue_comments_024816.json:
```json
{
    "body": "Attachment\n\nWARNING:\n\nThe atkin-lehner operator does *not* leave the space $M_k(N,\\chi)$ invariant unless $\\chi$ is quadratic. Really it sends $M_k(N,\\chi)$ to $M_k(N,\\chibar)$.   So Sage should give an error message when $\\chi$ is not quadratic.",
    "created_at": "2008-06-27T19:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24816",
    "user": "was"
}
```

Attachment

WARNING:

The atkin-lehner operator does *not* leave the space $M_k(N,\chi)$ invariant unless $\chi$ is quadratic. Really it sends $M_k(N,\chi)$ to $M_k(N,\chibar)$.   So Sage should give an error message when $\chi$ is not quadratic.



---

archive/issue_comments_024817.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-29T02:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24817",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_024818.json:
```json
{
    "body": "Looks good. I added a patch that actually corrects a bug (some statements were out of order), and just reformats/corrects typos. This is ready to go.",
    "created_at": "2008-06-29T02:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24818",
    "user": "craigcitro"
}
```

Looks good. I added a patch that actually corrects a bug (some statements were out of order), and just reformats/corrects typos. This is ready to go.



---

archive/issue_comments_024819.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-02T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24819",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_024820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-02T19:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3521#issuecomment-24820",
    "user": "mabshoff"
}
```

Resolution: fixed
