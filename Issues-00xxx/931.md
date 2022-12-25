# Issue 931: [with patch] Optimize permanent code for matrices over ZZ

archive/issues_000931.json:
```json
{
    "body": "Assignee: @williamstein\n\nI think SAGE is still the only mathematical\nsoftware with an implementation of the permanent function for\nnon-square matrices over an arbitrary field!\n\nBut it is frickin' slow, as William could have said.\nCalculating the permanent of a 13 x 17 matrix with a 'band' of 4 1's\nover the main diagonal.\n\n\nOver ZZ:\n> sage: time f(13,4)\n> CPU times: user 3.98 s, sys: 0.07 s, total: 4.05 s\n> Wall time: 4.08\n>  1596800\n\n\n\nOver QQ\n> sage: time f(13,4)\n> CPU times: user 8.39 s, sys: 0.09 s, total: 8.48 s\n> Wall time: 8.56\n>  1596800\n\n\nMy all C-program with ints based on gmp:\n> [jaap`@`paix perm_gmp]$ time ./ds 13 4\n> 1596800\n> real    0m0.328s\n> user    0m0.326s\n> sys     0m0.003s\n> [jaap`@`paix perm_gmp]$ \n\n\nIn the reference manual it still says that the code is optimized\nonly for matrices over QQ :-)!\n\nWhat we need is optimization for integer matrices (followed by more\noptimization for (0,1) matrices, eventually for (-1,0,1) matrices.\nThat are the matrices that 'count' in applications.).\n\nA speed boost can be achieved replacing 'my' pure Python function\n_combinations, to be found in sage.structure.sequence, with a real fast\nimplementation in C/Cython.\n\nJaap\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/931\n\n",
    "closed_at": "2007-10-27T02:43:18Z",
    "created_at": "2007-10-19T18:44:51Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "[with patch] Optimize permanent code for matrices over ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/931",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein

I think SAGE is still the only mathematical
software with an implementation of the permanent function for
non-square matrices over an arbitrary field!

But it is frickin' slow, as William could have said.
Calculating the permanent of a 13 x 17 matrix with a 'band' of 4 1's
over the main diagonal.


Over ZZ:
> sage: time f(13,4)
> CPU times: user 3.98 s, sys: 0.07 s, total: 4.05 s
> Wall time: 4.08
>  1596800



Over QQ
> sage: time f(13,4)
> CPU times: user 8.39 s, sys: 0.09 s, total: 8.48 s
> Wall time: 8.56
>  1596800


My all C-program with ints based on gmp:
> [jaap`@`paix perm_gmp]$ time ./ds 13 4
> 1596800
> real    0m0.328s
> user    0m0.326s
> sys     0m0.003s
> [jaap`@`paix perm_gmp]$ 


In the reference manual it still says that the code is optimized
only for matrices over QQ :-)!

What we need is optimization for integer matrices (followed by more
optimization for (0,1) matrices, eventually for (-1,0,1) matrices.
That are the matrices that 'count' in applications.).

A speed boost can be achieved replacing 'my' pure Python function
_combinations, to be found in sage.structure.sequence, with a real fast
implementation in C/Cython.

Jaap


Issue created by migration from https://trac.sagemath.org/ticket/931





---

archive/issue_comments_005670.json:
```json
{
    "body": "Attachment [patch_trac931.hg](tarball://root/attachments/some-uuid/ticket931/patch_trac931.hg) by @jaapspies created at 2007-10-25 20:57:22",
    "created_at": "2007-10-25T20:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/931#issuecomment-5670",
    "user": "https://github.com/jaapspies"
}
```

Attachment [patch_trac931.hg](tarball://root/attachments/some-uuid/ticket931/patch_trac931.hg) by @jaapspies created at 2007-10-25 20:57:22



---

archive/issue_comments_005671.json:
```json
{
    "body": "Attachment [patch_trac931.2.hg](tarball://root/attachments/some-uuid/ticket931/patch_trac931.2.hg) by @jaapspies created at 2007-10-25 21:00:24",
    "created_at": "2007-10-25T21:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/931#issuecomment-5671",
    "user": "https://github.com/jaapspies"
}
```

Attachment [patch_trac931.2.hg](tarball://root/attachments/some-uuid/ticket931/patch_trac931.2.hg) by @jaapspies created at 2007-10-25 21:00:24



---

archive/issue_events_002557.json:
```json
{
    "actor": "https://github.com/jaapspies",
    "created_at": "2007-10-25T22:04:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/931",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/931#event-2557"
}
```



---

archive/issue_comments_005672.json:
```json
{
    "body": "I'm sorry for the double attachment!\n\nTiming\n\n```\nsage: time dance(7)\nh^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840\nCPU times: user 25.20 s, sys: 0.46 s, total: 25.65 s\nWall time: 26.08\n```\n\nin sage-2.8.9:\n\n```\nsage: time dance(7)\nh^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840\nCPU times: user 42.64 s, sys: 1.12 s, total: 43.76 s\nWall time: 43.96\n\n```\n\nThis is not the last word on this issue.\n\nJaap",
    "created_at": "2007-10-25T22:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/931#issuecomment-5672",
    "user": "https://github.com/jaapspies"
}
```

I'm sorry for the double attachment!

Timing

```
sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 25.20 s, sys: 0.46 s, total: 25.65 s
Wall time: 26.08
```

in sage-2.8.9:

```
sage: time dance(7)
h^7 - 14*h^6 + 126*h^5 - 700*h^4 + 2625*h^3 - 6342*h^2 + 9072*h - 5840
CPU times: user 42.64 s, sys: 1.12 s, total: 43.76 s
Wall time: 43.96

```

This is not the last word on this issue.

Jaap



---

archive/issue_comments_005673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T02:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/931#issuecomment-5673",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed



---

archive/issue_events_002558.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2007-10-27T02:43:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/931",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/931#event-2558"
}
```
