# Issue 5969: implement computation of rational cuspidal subgroups of modular abelian varieties

archive/issues_005969.json:
```json
{
    "body": "Assignee: was\n\nCC:  boothby\n\nThis will depend on #5882.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5969\n\n",
    "created_at": "2009-05-03T05:49:30Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "implement computation of rational cuspidal subgroups of modular abelian varieties",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5969",
    "user": "was"
}
```
Assignee: was

CC:  boothby

This will depend on #5882.

Issue created by migration from https://trac.sagemath.org/ticket/5969





---

archive/issue_comments_047309.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-16T04:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47309",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_047310.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-21T19:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47310",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_047311.json:
```json
{
    "body": "Hi,\n\nNote that trac-5969-part4.patch removes the abvarsub modular symbols functions for torsion, since I found that they are buggy and not finished.  The same functionality is already available in the modular abelian varieties code anyways, so this is no real loss.",
    "created_at": "2010-01-26T01:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47311",
    "user": "was"
}
```

Hi,

Note that trac-5969-part4.patch removes the abvarsub modular symbols functions for torsion, since I found that they are buggy and not finished.  The same functionality is already available in the modular abelian varieties code anyways, so this is no real loss.



---

archive/issue_comments_047312.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T01:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47312",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047313.json:
```json
{
    "body": "Attachment\n\nI just checked that all four patches apply fine to sage-4.3.5 still with no rebasing necessary.",
    "created_at": "2010-03-30T00:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47313",
    "user": "was"
}
```

Attachment

I just checked that all four patches apply fine to sage-4.3.5 still with no rebasing necessary.



---

archive/issue_comments_047314.json:
```json
{
    "body": "The \"part2\" patch changes some things in `matrix/matrix_integer_dense.pyx`, and that causes two doctest failures:\n\n\n```\n\nsage -t -long \"devel/sage/sage/modules/fg_pid/fgp_module.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py\", line 1131:\n    sage: phi = Q.hom([0,V.0,V.1]); phi\nExpected:\n    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (0, 0, 1), (0, 1, 0)]\nGot:\n    Morphism from module over Integer Ring with invariants (2, 0, 0) to module with invariants (0, 0, 0) that sends the generators to [(0, 0, 0), (1, 0, 0), (0, 1, 0)]\n**********************************************************************\nFile \"/mnt/usb1/scratch/ghitza/sage-4.3.5-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/modules/fg_pid/fgp_module.py\", line 1139:\n    sage: phi(Q.1)\nExpected:\n    (0, 0, 1)\nGot:\n    (1, 0, 0)\n**********************************************************************\n```\n\n\nIt was not obvious to me whether this was harmless or an actual problem.\n\nThe rest looks good, there are a couple of docstring fixes but I have a reviewer patch that can take care of them.",
    "created_at": "2010-04-03T05:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47314",
    "user": "AlexGhitza"
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

archive/issue_comments_047315.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-03T05:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47315",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_047316.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-23T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47316",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047317.json:
```json
{
    "body": "Attachment\n\nIt turns out that part 2 fixes a *MAJOR* bug in SNF for matrices over ZZ in an edge case.  The doctest in finitely generated modules was just wrong (ouch).    I carefully checked through this with Robert Bradshaw, and posted a patch that updates the doctest.",
    "created_at": "2010-04-23T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47317",
    "user": "was"
}
```

Attachment

It turns out that part 2 fixes a *MAJOR* bug in SNF for matrices over ZZ in an edge case.  The doctest in finitely generated modules was just wrong (ouch).    I carefully checked through this with Robert Bradshaw, and posted a patch that updates the doctest.



---

archive/issue_comments_047318.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-24T23:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47318",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047319.json:
```json
{
    "body": "This looks good to me, and passes tests.\n\nNote that the part1 patch applies with some fuzz to sage-4.4.rc0, but it's fine.",
    "created_at": "2010-04-24T23:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47319",
    "user": "AlexGhitza"
}
```

This looks good to me, and passes tests.

Note that the part1 patch applies with some fuzz to sage-4.4.rc0, but it's fine.



---

archive/issue_comments_047320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5969",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5969#issuecomment-47320",
    "user": "was"
}
```

Resolution: fixed
