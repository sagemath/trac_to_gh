# Issue 1724: Creating ModularForms from q-expansions

archive/issues_001724.json:
```json
{
    "body": "Assignee: was\n\nThere is a way of creating modular forms from their Fourier expansions; for instance\n\n\n```\nS12=CuspForms(1,12)\nPSR.<q>=PowerSeriesRing(QQ)\nS12(q- 24*q^2 + 252*q^3 - 1472*q^4)\n```\n\ngives\n\n```\nq - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)\n```\n\n\nHowever, one needs strictly more than the Sturm bound's worth of Fourier coefficients to make this work:\n\n```\nS12(q+O(q^2))\n```\n\ngives\n\n```\nException (click to the left for traceback):\n...\nTypeError: q-expansion needed to at least precision 4\n```\n\n\n... as here the Sturm bound is 1.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1724\n\n",
    "created_at": "2008-01-08T21:20:05Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Creating ModularForms from q-expansions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1724",
    "user": "ljpk"
}
```
Assignee: was

There is a way of creating modular forms from their Fourier expansions; for instance


```
S12=CuspForms(1,12)
PSR.<q>=PowerSeriesRing(QQ)
S12(q- 24*q^2 + 252*q^3 - 1472*q^4)
```

gives

```
q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)
```


However, one needs strictly more than the Sturm bound's worth of Fourier coefficients to make this work:

```
S12(q+O(q^2))
```

gives

```
Exception (click to the left for traceback):
...
TypeError: q-expansion needed to at least precision 4
```


... as here the Sturm bound is 1.

Issue created by migration from https://trac.sagemath.org/ticket/1724





---

archive/issue_comments_010921.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-21T08:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1724#issuecomment-10921",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010922.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-01-21T08:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1724#issuecomment-10922",
    "user": "craigcitro"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_010923.json:
```json
{
    "body": "Attachment [craigcitro-1724.patch](tarball://root/attachments/some-uuid/ticket1724/craigcitro-1724.patch) by craigcitro created at 2008-01-21 08:46:00\n\nThis fixes the above bug. It also smooths out a few issues to do with the following: at  various places in the modular forms code, it seems that self.prec() is used where self.sturm_bound() is what we really want. There may be more of these that are hard to track down -- for instance, one might use self.basis()[0].prec(), etc.",
    "created_at": "2008-01-21T08:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1724#issuecomment-10923",
    "user": "craigcitro"
}
```

Attachment [craigcitro-1724.patch](tarball://root/attachments/some-uuid/ticket1724/craigcitro-1724.patch) by craigcitro created at 2008-01-21 08:46:00

This fixes the above bug. It also smooths out a few issues to do with the following: at  various places in the modular forms code, it seems that self.prec() is used where self.sturm_bound() is what we really want. There may be more of these that are hard to track down -- for instance, one might use self.basis()[0].prec(), etc.



---

archive/issue_comments_010924.json:
```json
{
    "body": "Oops -- I forgot to mention, this patch will only apply to a branch that already has the patches for #1844 applied.",
    "created_at": "2008-01-21T08:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1724#issuecomment-10924",
    "user": "craigcitro"
}
```

Oops -- I forgot to mention, this patch will only apply to a branch that already has the patches for #1844 applied.



---

archive/issue_comments_010925.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-25T23:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1724#issuecomment-10925",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_010926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T23:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1724#issuecomment-10926",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010927.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-25T23:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1724#issuecomment-10927",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
