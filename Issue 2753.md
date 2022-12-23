# Issue 2753: [with patch, needs review] new "randstate" framework for a global Sage random number seed

archive/issues_002753.json:
```json
{
    "body": "Assignee: somebody\n\nThe attached patch keeps track of the random number seed used on Sage startup, and lets you set a single random number seed, which gets propagated on demand into random number generators for GMP (+ MPFR), Python, NTL, Pari, gp, GAP, and libc (so far).\n\nAlso, it moves away from libc's random() in favor of the other generators mentioned above, which are portable across operating systems and architectures; this means that doctest results using random numbers are now reproducible, so I've removed many \"# random\" from the doctests.\n\nPasses testall on the platforms I have access to (32-bit x86 Linux, 64-bit x86 Linux, and 32-bit x86 OSX).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2753\n\n",
    "created_at": "2008-04-01T14:28:37Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] new \"randstate\" framework for a global Sage random number seed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2753",
    "user": "cwitty"
}
```
Assignee: somebody

The attached patch keeps track of the random number seed used on Sage startup, and lets you set a single random number seed, which gets propagated on demand into random number generators for GMP (+ MPFR), Python, NTL, Pari, gp, GAP, and libc (so far).

Also, it moves away from libc's random() in favor of the other generators mentioned above, which are portable across operating systems and architectures; this means that doctest results using random numbers are now reproducible, so I've removed many "# random" from the doctests.

Passes testall on the platforms I have access to (32-bit x86 Linux, 64-bit x86 Linux, and 32-bit x86 OSX).

Issue created by migration from https://trac.sagemath.org/ticket/2753





---

archive/issue_comments_018909.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-01T14:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2753#issuecomment-18909",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_018910.json:
```json
{
    "body": "Attachment\n\nApplies cleanly to Sage 2.11. I am taking cwitty's word on doctests- I haven't run any of my own. IMO, this greatly improves the robustness of our doctesting infrastructure.",
    "created_at": "2008-04-04T02:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2753#issuecomment-18910",
    "user": "rlm"
}
```

Attachment

Applies cleanly to Sage 2.11. I am taking cwitty's word on doctests- I haven't run any of my own. IMO, this greatly improves the robustness of our doctesting infrastructure.



---

archive/issue_comments_018911.json:
```json
{
    "body": "Patch should be rebased on 3.0.alpha0.",
    "created_at": "2008-04-04T02:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2753#issuecomment-18911",
    "user": "rlm"
}
```

Patch should be rebased on 3.0.alpha0.



---

archive/issue_comments_018912.json:
```json
{
    "body": "manula merges of the rejected hunks against my 3.0.alpha1 merge tree",
    "created_at": "2008-04-04T05:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2753#issuecomment-18912",
    "user": "mabshoff"
}
```

manula merges of the rejected hunks against my 3.0.alpha1 merge tree



---

archive/issue_comments_018913.json:
```json
{
    "body": "Attachment\n\nMerged all three patches in Sage 3.0.alpha1",
    "created_at": "2008-04-04T05:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2753#issuecomment-18913",
    "user": "mabshoff"
}
```

Attachment

Merged all three patches in Sage 3.0.alpha1



---

archive/issue_comments_018914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T05:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2753#issuecomment-18914",
    "user": "mabshoff"
}
```

Resolution: fixed
