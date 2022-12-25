# Issue 8545: \opi -> \overline\pi in coxter_groups.py

archive/issues_008545.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  sage-combinat\n\nThe docstring to apply_simple_projection method of CoxeterGroups\ncontains `\\opi` which is not a valid latex symbol.\n\nAs a consequence the pdf version of the reference manual does\nnot build cleanly. Thus \n\n`sage -docbuild reference pdf`\n\neventually halts with the line:\n\n\n```\n! Undefined control sequence.\n<recently read> \\opi \n                     \nl.185462 projection $\\pi_i$ (resp. $\\opi\n                                        _i$) on self.\n```\n\n\nEvidently ``\\opi`` is supposed to be ``\\overline\\pi``, as elsewhere in the file around line 379 in coxeter_groups.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8545\n\n",
    "created_at": "2010-03-15T21:02:37Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\\opi -> \\overline\\pi in coxter_groups.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8545",
    "user": "https://github.com/dwbump"
}
```
Assignee: mvngu

CC:  sage-combinat

The docstring to apply_simple_projection method of CoxeterGroups
contains `\opi` which is not a valid latex symbol.

As a consequence the pdf version of the reference manual does
not build cleanly. Thus 

`sage -docbuild reference pdf`

eventually halts with the line:


```
! Undefined control sequence.
<recently read> \opi 
                     
l.185462 projection $\pi_i$ (resp. $\opi
                                        _i$) on self.
```


Evidently ``\opi`` is supposed to be ``\overline\pi``, as elsewhere in the file around line 379 in coxeter_groups.py.

Issue created by migration from https://trac.sagemath.org/ticket/8545





---

archive/issue_comments_077135.json:
```json
{
    "body": "Attachment [trac_8545_opi.patch](tarball://root/attachments/some-uuid/ticket8545/trac_8545_opi.patch) by @dwbump created at 2010-03-15 21:05:02",
    "created_at": "2010-03-15T21:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8545#issuecomment-77135",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_8545_opi.patch](tarball://root/attachments/some-uuid/ticket8545/trac_8545_opi.patch) by @dwbump created at 2010-03-15 21:05:02



---

archive/issue_comments_077136.json:
```json
{
    "body": "I think this is fixed in #8492 (which I tried to cc you on).",
    "created_at": "2010-03-15T21:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8545#issuecomment-77136",
    "user": "https://github.com/jhpalmieri"
}
```

I think this is fixed in #8492 (which I tried to cc you on).



---

archive/issue_events_008726.json:
```json
{
    "actor": "https://github.com/dwbump",
    "created_at": "2010-03-15T22:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8545",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8545#event-8726"
}
```



---

archive/issue_comments_077137.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-03-15T22:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8545#issuecomment-77137",
    "user": "https://github.com/dwbump"
}
```

Resolution: duplicate



---

archive/issue_comments_077138.json:
```json
{
    "body": "For some reason cc: bump does not cause me to be copied.",
    "created_at": "2010-03-15T22:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8545#issuecomment-77138",
    "user": "https://github.com/dwbump"
}
```

For some reason cc: bump does not cause me to be copied.
