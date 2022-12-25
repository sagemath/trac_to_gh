# Issue 5969: implement computation of rational cuspidal subgroups of modular abelian varieties

archive/issues_005969.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  boothby\n\nThis will depend on #5882.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5969\n\n",
    "closed_at": "2010-04-29T05:13:21Z",
    "created_at": "2009-05-03T05:49:30Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "implement computation of rational cuspidal subgroups of modular abelian varieties",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5969",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  boothby

This will depend on #5882.

Issue created by migration from https://trac.sagemath.org/ticket/5969





---

archive/issue_comments_047218.json:
```json
{
    "body": "Attachment [trac_5969-part2.patch](tarball://root/attachments/some-uuid/ticket5969/trac_5969-part2.patch) by @williamstein created at 2009-09-16 04:50:01",
    "created_at": "2009-09-16T04:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47218",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5969-part2.patch](tarball://root/attachments/some-uuid/ticket5969/trac_5969-part2.patch) by @williamstein created at 2009-09-16 04:50:01



---

archive/issue_comments_047219.json:
```json
{
    "body": "Attachment [trac-5969-part3.patch](tarball://root/attachments/some-uuid/ticket5969/trac-5969-part3.patch) by @williamstein created at 2010-01-21 19:36:24",
    "created_at": "2010-01-21T19:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47219",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-5969-part3.patch](tarball://root/attachments/some-uuid/ticket5969/trac-5969-part3.patch) by @williamstein created at 2010-01-21 19:36:24



---

archive/issue_comments_047220.json:
```json
{
    "body": "Hi,\n\nNote that trac-5969-part4.patch removes the abvarsub modular symbols functions for torsion, since I found that they are buggy and not finished.  The same functionality is already available in the modular abelian varieties code anyways, so this is no real loss.",
    "created_at": "2010-01-26T01:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47220",
    "user": "https://github.com/williamstein"
}
```

Hi,

Note that trac-5969-part4.patch removes the abvarsub modular symbols functions for torsion, since I found that they are buggy and not finished.  The same functionality is already available in the modular abelian varieties code anyways, so this is no real loss.



---

archive/issue_comments_047221.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T01:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47221",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047222.json:
```json
{
    "body": "Attachment [trac_5969-part4.patch](tarball://root/attachments/some-uuid/ticket5969/trac_5969-part4.patch) by @williamstein created at 2010-03-30 00:47:12\n\nI just checked that all four patches apply fine to sage-4.3.5 still with no rebasing necessary.",
    "created_at": "2010-03-30T00:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47222",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5969-part4.patch](tarball://root/attachments/some-uuid/ticket5969/trac_5969-part4.patch) by @williamstein created at 2010-03-30 00:47:12

I just checked that all four patches apply fine to sage-4.3.5 still with no rebasing necessary.



---

archive/issue_comments_047223.json:
```json
{
    "body": "The \"part2\" patch changes some things in `matrix/matrix_integer_dense.pyx`, and that causes two doctest failures:\n\n```\n\nsage -t -long \"devel/sage/sage/modules/fg_pid/fgp_module.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py\", line 1131:\n    sage: phi = Q.hom([0,V.0,V.1]); phi\nExpected:\n    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (0, 0, 1), (0, 1, 0)]\nGot:\n    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (1, 0, 0), (0, 1, 0)]\n**********************************************************************\nFile \"/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py\", line 1139:\n    sage: phi(Q.1)\nExpected:\n    (0, 0, 1)\nGot:\n    (1, 0, 0)\n**********************************************************************\n```\n\nIt was not obvious to me whether this was harmless or an actual problem.\n\nThe rest looks good, there are a couple of docstring fixes but I have a reviewer patch that can take care of them.",
    "created_at": "2010-04-03T05:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47223",
    "user": "https://github.com/aghitza"
}
```

The "part2" patch changes some things in `matrix/matrix_integer_dense.pyx`, and that causes two doctest failures:

```

sage -t -long "devel/sage/sage/modules/fg_pid/fgp_module.py"
**********************************************************************
File "/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py", line 1131:
    sage: phi = Q.hom([0,V.0,V.1]); phi
Expected:
    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (0, 0, 1), (0, 1, 0)]
Got:
    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
**********************************************************************
File "/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py", line 1139:
    sage: phi(Q.1)
Expected:
    (0, 0, 1)
Got:
    (1, 0, 0)
**********************************************************************
```

It was not obvious to me whether this was harmless or an actual problem.

The rest looks good, there are a couple of docstring fixes but I have a reviewer patch that can take care of them.



---

archive/issue_comments_047224.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-03T05:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47224",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_047225.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-23T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47225",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047226.json:
```json
{
    "body": "Attachment [trac_5969-part5.patch](tarball://root/attachments/some-uuid/ticket5969/trac_5969-part5.patch) by @williamstein created at 2010-04-23 23:36:57\n\nIt turns out that part 2 fixes a *MAJOR* bug in SNF for matrices over ZZ in an edge case.  The doctest in finitely generated modules was just wrong (ouch).    I carefully checked through this with Robert Bradshaw, and posted a patch that updates the doctest.",
    "created_at": "2010-04-23T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47226",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5969-part5.patch](tarball://root/attachments/some-uuid/ticket5969/trac_5969-part5.patch) by @williamstein created at 2010-04-23 23:36:57

It turns out that part 2 fixes a *MAJOR* bug in SNF for matrices over ZZ in an edge case.  The doctest in finitely generated modules was just wrong (ouch).    I carefully checked through this with Robert Bradshaw, and posted a patch that updates the doctest.



---

archive/issue_comments_047227.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-24T23:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47227",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047228.json:
```json
{
    "body": "This looks good to me, and passes tests.\n\nNote that the part1 patch applies with some fuzz to sage-4.4.rc0, but it's fine.",
    "created_at": "2010-04-24T23:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47228",
    "user": "https://github.com/aghitza"
}
```

This looks good to me, and passes tests.

Note that the part1 patch applies with some fuzz to sage-4.4.rc0, but it's fine.



---

archive/issue_comments_047229.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47229",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_014011.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-29T05:13:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5969#event-14011"
}
```
