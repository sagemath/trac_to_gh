# Issue 2475: [with patch; with positive review] doctest -- get coverage of modular/dims.py up to 100%

archive/issues_002475.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen I started this (sage-2.10.3):\n\n```\ndims.py\nSCORE dims.py: 11% (6 of 54)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2475\n\n",
    "closed_at": "2008-03-15T08:32:39Z",
    "created_at": "2008-03-11T23:06:58Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch; with positive review] doctest -- get coverage of modular/dims.py up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2475",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

When I started this (sage-2.10.3):

```
dims.py
SCORE dims.py: 11% (6 of 54)
```

Issue created by migration from https://trac.sagemath.org/ticket/2475





---

archive/issue_comments_016726.json:
```json
{
    "body": "SCORE dims.py: 31% (17 of 54); and I fixed a serious bug in p-new subspace!",
    "created_at": "2008-03-12T01:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16726",
    "user": "https://github.com/williamstein"
}
```

SCORE dims.py: 31% (17 of 54); and I fixed a serious bug in p-new subspace!



---

archive/issue_comments_016727.json:
```json
{
    "body": "Attachment [sage-2475-part1.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part1.patch) by @williamstein created at 2008-03-15 02:27:58\n\nthis brings coverage to 100% and fixes a serious bug.",
    "created_at": "2008-03-15T02:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16727",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2475-part1.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part1.patch) by @williamstein created at 2008-03-15 02:27:58

this brings coverage to 100% and fixes a serious bug.



---

archive/issue_events_005847.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-15T02:30:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2475#event-5847"
}
```



---

archive/issue_comments_016728.json:
```json
{
    "body": "Attachment [sage-2475-part2_of_2.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part2_of_2.patch) by @williamstein created at 2008-03-15 02:30:17\n\nTo referee these patches:\n1. verify that they fix the coverage to 100%\n2. look for typos in the docstrings\n3. The p-new subspace \"serious bugfixes\" make it so one doesn't get negative dimensions.  This was because the old new subspace code subtracted off the images of old subspaces from the tiny little new subspace instead of subtracting off from the ful l cuspidal subspace. \n4. This is almost all docstring addition and fixing return types to be Integer.\n\nAfter applying these two patches:\n\n```\nteragon:modular was$ sage -coverage dims.py\n----------------------------------------------------------------------\ndims.py\nSCORE dims.py: 100% (46 of 46)\n----------------------------------------------------------------------\n```",
    "created_at": "2008-03-15T02:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16728",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2475-part2_of_2.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part2_of_2.patch) by @williamstein created at 2008-03-15 02:30:17

To referee these patches:
1. verify that they fix the coverage to 100%
2. look for typos in the docstrings
3. The p-new subspace "serious bugfixes" make it so one doesn't get negative dimensions.  This was because the old new subspace code subtracted off the images of old subspaces from the tiny little new subspace instead of subtracting off from the ful l cuspidal subspace. 
4. This is almost all docstring addition and fixing return types to be Integer.

After applying these two patches:

```
teragon:modular was$ sage -coverage dims.py
----------------------------------------------------------------------
dims.py
SCORE dims.py: 100% (46 of 46)
----------------------------------------------------------------------
```



---

archive/issue_comments_016729.json:
```json
{
    "body": "Attachment [sage-2475-part4-touch-ups.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part4-touch-ups.patch) by @craigcitro created at 2008-03-15 07:59:23",
    "created_at": "2008-03-15T07:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16729",
    "user": "https://github.com/craigcitro"
}
```

Attachment [sage-2475-part4-touch-ups.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part4-touch-ups.patch) by @craigcitro created at 2008-03-15 07:59:23



---

archive/issue_comments_016730.json:
```json
{
    "body": "Looks good. Changed a few comments in doctests, touched up a few things.",
    "created_at": "2008-03-15T08:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16730",
    "user": "https://github.com/craigcitro"
}
```

Looks good. Changed a few comments in doctests, touched up a few things.



---

archive/issue_comments_016731.json:
```json
{
    "body": "I forgot an `r` on the docstring for `mu30`. mabshoff is correcting this when he merges.",
    "created_at": "2008-03-15T08:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16731",
    "user": "https://github.com/craigcitro"
}
```

I forgot an `r` on the docstring for `mu30`. mabshoff is correcting this when he merges.



---

archive/issue_comments_016732.json:
```json
{
    "body": "Attachment [trac_2475-part5.patch](tarball://root/attachments/some-uuid/ticket2475/trac_2475-part5.patch) by @craigcitro created at 2008-03-15 08:31:06",
    "created_at": "2008-03-15T08:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16732",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_2475-part5.patch](tarball://root/attachments/some-uuid/ticket2475/trac_2475-part5.patch) by @craigcitro created at 2008-03-15 08:31:06



---

archive/issue_events_005848.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T08:32:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2475#event-5848"
}
```



---

archive/issue_comments_016733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T08:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016734.json:
```json
{
    "body": "Attachment [sage-2475-part6.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part6.patch) by mabshoff created at 2008-03-15 08:32:39\n\nMerged all six patches in Sage 2.10.4.alpha0",
    "created_at": "2008-03-15T08:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2475#issuecomment-16734",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-2475-part6.patch](tarball://root/attachments/some-uuid/ticket2475/sage-2475-part6.patch) by mabshoff created at 2008-03-15 08:32:39

Merged all six patches in Sage 2.10.4.alpha0
