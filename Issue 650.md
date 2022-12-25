# Issue 650: serious modular forms bug

archive/issues_000650.json:
```json
{
    "body": "Assignee: was or craigcitro\n\n\n```\nsage: d = ModularSymbols(Gamma0(43), 2, sign=1).cuspidal_subspace().new_subspace().decomposition()\nsage: d\n\n[\nModular Symbols subspace of dimension 1 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field,\nModular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field\n]\nsage: for a in d: print a.q_eigenform(10)\n....:\nq - 2*q^2 - 2*q^3 + 2*q^4 - 4*q^5 + 4*q^6 + q^9 + O(q^10)\nq + alpha*q^2 + -alpha*q^3 + (-alpha + 2)*q^5 + -2*q^6 + (alpha - 2)*q^7 + -2*alpha*q^8 + -q^9 + O(q^10)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/650\n\n",
    "created_at": "2007-09-13T18:47:19Z",
    "labels": [
        "component: modular forms",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "serious modular forms bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/650",
    "user": "https://github.com/williamstein"
}
```
Assignee: was or craigcitro


```
sage: d = ModularSymbols(Gamma0(43), 2, sign=1).cuspidal_subspace().new_subspace().decomposition()
sage: d

[
Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field,
Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field
]
sage: for a in d: print a.q_eigenform(10)
....:
q - 2*q^2 - 2*q^3 + 2*q^4 - 4*q^5 + 4*q^6 + q^9 + O(q^10)
q + alpha*q^2 + -alpha*q^3 + (-alpha + 2)*q^5 + -2*q^6 + (alpha - 2)*q^7 + -2*alpha*q^8 + -q^9 + O(q^10)
```


Issue created by migration from https://trac.sagemath.org/ticket/650





---

archive/issue_comments_003366.json:
```json
{
    "body": "Added a patch that turns this into a NotImplementedError. The problem is that the code for computing newspaces of modular forms is written ... oddly. We're going to fix this in the near future, but this will at least stop giving wrong answers in the interim.",
    "created_at": "2007-09-13T23:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3366",
    "user": "https://github.com/craigcitro"
}
```

Added a patch that turns this into a NotImplementedError. The problem is that the code for computing newspaces of modular forms is written ... oddly. We're going to fix this in the near future, but this will at least stop giving wrong answers in the interim.



---

archive/issue_comments_003367.json:
```json
{
    "body": "Changing assignee from was or craigcitro to @craigcitro.",
    "created_at": "2007-10-02T00:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3367",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from was or craigcitro to @craigcitro.



---

archive/issue_comments_003368.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-02T00:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3368",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003369.json:
```json
{
    "body": "Actually, I discovered a second place where this needed to be turned into a NotImplementedError. I replaced the above bundle with a fix for both.",
    "created_at": "2007-10-12T21:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3369",
    "user": "https://github.com/craigcitro"
}
```

Actually, I discovered a second place where this needed to be turned into a NotImplementedError. I replaced the above bundle with a fix for both.



---

archive/issue_comments_003370.json:
```json
{
    "body": "Attachment [trac_650_bandaid.hg](tarball://root/attachments/some-uuid/ticket650/trac_650_bandaid.hg) by @craigcitro created at 2007-10-12 21:59:03",
    "created_at": "2007-10-12T21:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3370",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_650_bandaid.hg](tarball://root/attachments/some-uuid/ticket650/trac_650_bandaid.hg) by @craigcitro created at 2007-10-12 21:59:03



---

archive/issue_comments_003371.json:
```json
{
    "body": "\n```\n22:55 < cwitty_> #650: applies cleanly, but the doctests fail.  It's odd...unless Mercurial is screwing \n                 up the history somehow, it looks like the doctests never could have worked after this \n                 patch.\n22:57 < williamstein> I think the doctests were wrong.\n22:57 < williamstein> I.e., they claimed a result that was mathematically wrong.\n22:59 < cwitty_> Right.  But the patch comments out the doctest \"N = ...\", but leaves the next doctest \n                 alone, \"N.basis()\".  Why didn't he comment out that doctest too?\n22:59 < williamstein> It's a mistake on his part.\n```\n",
    "created_at": "2007-10-13T06:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3371",
    "user": "https://github.com/williamstein"
}
```


```
22:55 < cwitty_> #650: applies cleanly, but the doctests fail.  It's odd...unless Mercurial is screwing 
                 up the history somehow, it looks like the doctests never could have worked after this 
                 patch.
22:57 < williamstein> I think the doctests were wrong.
22:57 < williamstein> I.e., they claimed a result that was mathematically wrong.
22:59 < cwitty_> Right.  But the patch comments out the doctest "N = ...", but leaves the next doctest 
                 alone, "N.basis()".  Why didn't he comment out that doctest too?
22:59 < williamstein> It's a mistake on his part.
```




---

archive/issue_comments_003372.json:
```json
{
    "body": "As the comments above point out, I was too hasty in commenting out the other doctests, and didn't test it due to lack of time. I updated the patch to comment out the last three doctests I missed on the first run, and I'm about to upload it.",
    "created_at": "2007-10-14T07:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3372",
    "user": "https://github.com/craigcitro"
}
```

As the comments above point out, I was too hasty in commenting out the other doctests, and didn't test it due to lack of time. I updated the patch to comment out the last three doctests I missed on the first run, and I'm about to upload it.



---

archive/issue_events_000716.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-19T01:48:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/650#event-716"
}
```



---

archive/issue_comments_003373.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T01:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3373",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_003374.json:
```json
{
    "body": "Attachment [trac_650_bandaid.2.hg](tarball://root/attachments/some-uuid/ticket650/trac_650_bandaid.2.hg) by @williamstein created at 2007-10-19 01:48:40",
    "created_at": "2007-10-19T01:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/650#issuecomment-3374",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_650_bandaid.2.hg](tarball://root/attachments/some-uuid/ticket650/trac_650_bandaid.2.hg) by @williamstein created at 2007-10-19 01:48:40
