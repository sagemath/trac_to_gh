# Issue 1143: [with patch] improve nintegrate documentation in response to Paul Zimmerman's talk

archive/issues_001143.json:
```json
{
    "body": "Assignee: tba\n\nCC:  jason\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1143\n\n",
    "created_at": "2007-11-11T11:32:47Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "[with patch] improve nintegrate documentation in response to Paul Zimmerman's talk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1143",
    "user": "was"
}
```
Assignee: tba

CC:  jason



Issue created by migration from https://trac.sagemath.org/ticket/1143





---

archive/issue_comments_006947.json:
```json
{
    "body": "Attachment\n\nDo not apply -- Paul points out that\n\n```\nOf course. It seems to me that **nintegral** calls Maxima and not GSL\n(it is numerical_integral which calls GSL).\n\nYou might want to provide only one interface to numerical quadrature\n(which might call GSL or Maxima or Pari with some options), and also\nallow for arbitrary precision quadrature (it seems only Pari/GP allows this).\n```\n\nand he's right -- it's just calling maxima.  So the above patch would\nactually break the docs!",
    "created_at": "2007-11-11T15:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6947",
    "user": "was"
}
```

Attachment

Do not apply -- Paul points out that

```
Of course. It seems to me that **nintegral** calls Maxima and not GSL
(it is numerical_integral which calls GSL).

You might want to provide only one interface to numerical quadrature
(which might call GSL or Maxima or Pari with some options), and also
allow for arbitrary precision quadrature (it seems only Pari/GP allows this).
```

and he's right -- it's just calling maxima.  So the above patch would
actually break the docs!



---

archive/issue_comments_006948.json:
```json
{
    "body": "So, should be invalidate this or what is the solution to this ticket?\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T14:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6948",
    "user": "mabshoff"
}
```

So, should be invalidate this or what is the solution to this ticket?

Cheers,

Michael



---

archive/issue_comments_006949.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-02T19:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6949",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_006950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T20:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6950",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006951.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-02T20:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6951",
    "user": "mabshoff"
}
```

Attachment
