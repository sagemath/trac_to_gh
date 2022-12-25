# Issue 1143: [with patch] improve nintegrate documentation in response to Paul Zimmerman's talk

archive/issues_001143.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @jasongrout\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1143\n\n",
    "created_at": "2007-11-11T11:32:47Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] improve nintegrate documentation in response to Paul Zimmerman's talk",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1143",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

CC:  @jasongrout



Issue created by migration from https://trac.sagemath.org/ticket/1143





---

archive/issue_comments_006926.json:
```json
{
    "body": "Attachment [zimmer.patch](tarball://root/attachments/some-uuid/ticket1143/zimmer.patch) by @williamstein created at 2007-11-11 15:32:10\n\nDo not apply -- Paul points out that\n\n```\nOf course. It seems to me that **nintegral** calls Maxima and not GSL\n(it is numerical_integral which calls GSL).\n\nYou might want to provide only one interface to numerical quadrature\n(which might call GSL or Maxima or Pari with some options), and also\nallow for arbitrary precision quadrature (it seems only Pari/GP allows this).\n```\n\nand he's right -- it's just calling maxima.  So the above patch would\nactually break the docs!",
    "created_at": "2007-11-11T15:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6926",
    "user": "https://github.com/williamstein"
}
```

Attachment [zimmer.patch](tarball://root/attachments/some-uuid/ticket1143/zimmer.patch) by @williamstein created at 2007-11-11 15:32:10

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

archive/issue_comments_006927.json:
```json
{
    "body": "So, should be invalidate this or what is the solution to this ticket?\n\nCheers,\n\nMichael",
    "created_at": "2007-11-18T14:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6927",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

So, should be invalidate this or what is the solution to this ticket?

Cheers,

Michael



---

archive/issue_comments_006928.json:
```json
{
    "body": "Attachment [trac1143-part2.patch](tarball://root/attachments/some-uuid/ticket1143/trac1143-part2.patch) by @williamstein created at 2007-12-02 19:22:57",
    "created_at": "2007-12-02T19:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6928",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac1143-part2.patch](tarball://root/attachments/some-uuid/ticket1143/trac1143-part2.patch) by @williamstein created at 2007-12-02 19:22:57



---

archive/issue_events_001270.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-02T20:23:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1143#event-1270"
}
```



---

archive/issue_comments_006929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T20:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006930.json:
```json
{
    "body": "Attachment [trac1143-part3.patch](tarball://root/attachments/some-uuid/ticket1143/trac1143-part3.patch) by mabshoff created at 2007-12-02 20:23:23",
    "created_at": "2007-12-02T20:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1143#issuecomment-6930",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac1143-part3.patch](tarball://root/attachments/some-uuid/ticket1143/trac1143-part3.patch) by mabshoff created at 2007-12-02 20:23:23
