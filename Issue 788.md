# Issue 788: a doctest change: random low order bits

archive/issues_000788.json:
```json
{
    "body": "Assignee: failure\n\nAll doctests in sage like this\n\n```\n sage: numerical thing   # random low order bits\n 1.234283409283408238 + 19190.9393*I\n```\n\nshould be changed to\n\n```\n sage: numerical thing\n 1.234283409283408... + 19190.93...*I\n```\n\nwhere the ... goes for the ambiguity in low order bits. \n\nThere are 44 such cases (at least).  See them by typing\n\n```\nsage: search_src('random low')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/788\n\n",
    "created_at": "2007-10-02T14:23:57Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "a doctest change: random low order bits",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/788",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

All doctests in sage like this

```
 sage: numerical thing   # random low order bits
 1.234283409283408238 + 19190.9393*I
```

should be changed to

```
 sage: numerical thing
 1.234283409283408... + 19190.93...*I
```

where the ... goes for the ambiguity in low order bits. 

There are 44 such cases (at least).  See them by typing

```
sage: search_src('random low')
```


Issue created by migration from https://trac.sagemath.org/ticket/788





---

archive/issue_comments_004719.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-07-31T04:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_004720.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-31T04:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004721.json:
```json
{
    "body": "There now seem to be quite a number of those. I will post a patch here to attempt to wipe them out.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T04:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There now seem to be quite a number of those. I will post a patch here to attempt to wipe them out.

Cheers,

Michael



---

archive/issue_comments_004722.json:
```json
{
    "body": "Changing assignee from mabshoff to anakha.",
    "created_at": "2008-10-24T05:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4722",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Changing assignee from mabshoff to anakha.



---

archive/issue_comments_004723.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-10-24T05:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4723",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Changing status from assigned to new.



---

archive/issue_comments_004724.json:
```json
{
    "body": "This patch needs to be tested on a lot of machines with either sage -testall or\n\n\n```\nsage -t sage/calculus/calculus.py sage/calculus/functional.py sage/calculus/wester.py sage/graphs/graph.py sage/gsl/dft.py sage/matrix/matrix_complex_double_dense.pyx sage/matrix/matrix_real_double_dense.pyx sage/modular/modform/numerical.py sage/modules/real_double_vector.pyx sage/rings/number_field/number_field.py sage/rings/number_field/totallyreal_data.pyx sage/rings/polynomial/polynomial_element.pyx sage/rings/real_double.pyx sage/schemes/elliptic_curves/sha_tate.py\n```\n\n\nwhich tests only the modified files.\n\nDo not mark as positive unless there is about 3 different architectures tested ({x86, ppc, sparc} x {32-bit, 64-bit})\n\nPlease report on what architecture you did the test.",
    "created_at": "2008-10-24T05:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4724",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

This patch needs to be tested on a lot of machines with either sage -testall or


```
sage -t sage/calculus/calculus.py sage/calculus/functional.py sage/calculus/wester.py sage/graphs/graph.py sage/gsl/dft.py sage/matrix/matrix_complex_double_dense.pyx sage/matrix/matrix_real_double_dense.pyx sage/modular/modform/numerical.py sage/modules/real_double_vector.pyx sage/rings/number_field/number_field.py sage/rings/number_field/totallyreal_data.pyx sage/rings/polynomial/polynomial_element.pyx sage/rings/real_double.pyx sage/schemes/elliptic_curves/sha_tate.py
```


which tests only the modified files.

Do not mark as positive unless there is about 3 different architectures tested ({x86, ppc, sparc} x {32-bit, 64-bit})

Please report on what architecture you did the test.



---

archive/issue_comments_004725.json:
```json
{
    "body": "Attachment [trac_788-part2.patch](tarball://root/attachments/some-uuid/ticket788/trac_788-part2.patch) by @dandrake created at 2008-10-24 05:57:02\n\nThe patches apply, and everything works except for one doctest:\n\n```\nsage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx**********************************************************************\nFile \"/opt/sage-3.2.alpha0/tmp/polynomial_element.py\", line 1940:\n    sage: f.factor()\nExpected:\n    (1.0*x - 1.00000... + 1.0000...*I) * (1.0*x - 1.00000... + 0.999989...*I) * (1.0*x - 0.9999... + 1.00000...*I) * (1.0*x + 0.99999... - 1.00000...*I) * (1.0*x + 0.999996... - 0.99998...*I) * (1.0*x + 1.00001... - 1.00000...*I)\nGot:\n    (1.0*x - 1.00000621124 + 1.00000779481*I) * (1.0*x - 1.00000364483 + 0.999990723518*I) * (1.0*x - 0.99999014393 + 1.00000148167*I) * (1.0*x + 0.99999217079 - 1.00000864146*I) * (1.0*x + 0.999996430878 - 0.999988898998*I) * (1.0*x + 1.00001139833 - 1.00000245954*I)\n**********************************************************************\n1 items had failures:\n   1 of  74 in __main__.example_46\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /opt/sage-3.2.alpha0/tmp/.doctest_polynomial_element.py\n\t [6.7 s]\n```\n\nThis is on Ubuntu Intrepid amd64, on a Core 2 Quad processor. The doctest fails every time, and no other test does. It looks like the `0.999989` in the second factor should be `0.0.99999`.",
    "created_at": "2008-10-24T05:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4725",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_788-part2.patch](tarball://root/attachments/some-uuid/ticket788/trac_788-part2.patch) by @dandrake created at 2008-10-24 05:57:02

The patches apply, and everything works except for one doctest:

```
sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx**********************************************************************
File "/opt/sage-3.2.alpha0/tmp/polynomial_element.py", line 1940:
    sage: f.factor()
Expected:
    (1.0*x - 1.00000... + 1.0000...*I) * (1.0*x - 1.00000... + 0.999989...*I) * (1.0*x - 0.9999... + 1.00000...*I) * (1.0*x + 0.99999... - 1.00000...*I) * (1.0*x + 0.999996... - 0.99998...*I) * (1.0*x + 1.00001... - 1.00000...*I)
Got:
    (1.0*x - 1.00000621124 + 1.00000779481*I) * (1.0*x - 1.00000364483 + 0.999990723518*I) * (1.0*x - 0.99999014393 + 1.00000148167*I) * (1.0*x + 0.99999217079 - 1.00000864146*I) * (1.0*x + 0.999996430878 - 0.999988898998*I) * (1.0*x + 1.00001139833 - 1.00000245954*I)
**********************************************************************
1 items had failures:
   1 of  74 in __main__.example_46
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-3.2.alpha0/tmp/.doctest_polynomial_element.py
	 [6.7 s]
```

This is on Ubuntu Intrepid amd64, on a Core 2 Quad processor. The doctest fails every time, and no other test does. It looks like the `0.999989` in the second factor should be `0.0.99999`.



---

archive/issue_comments_004726.json:
```json
{
    "body": "Replying to [comment:3 ddrake]:\nI applied the patches on an Intel Core 2 Duo OS X machine (10.5) and got the same failure in polynomial_element:\n\n```\nFile \"/Applications/sage/tmp/polynomial_element.py\", line 1947:\n    sage: f.factor()\nExpected:\n    (1.0*x - 1.00000... + 1.0000...*I) * (1.0*x - 1.00000... + 0.999989...*I) * (1.0*x - 0.9999... + 1.00000...*I) * (1.0*x + 0.99999... - 1.00000...*I) * (1.0*x + 0.999996... - 0.99998...*I) * (1.0*x + 1.00001... - 1.00000...*I)\nGot:\n    (1.0*x - 1.00001180498 + 0.999999639235*I) * (1.0*x - 0.999994409957 + 1.00001040378*I) * (1.0*x - 0.999993785062 + 0.999989956987*I) * (1.0*x + 0.999991652054 - 1.00000998012*I) * (1.0*x + 0.999995530902 - 0.999987780431*I) * (1.0*x + 1.00001281704 - 1.00000223945*I)\n**********************************************************************\n```\n\n(There were other failures as well, but (1) the new files were compiled with gcc 4.01, a known buggy compiler, and (2) the first patch didn't apply cleanly against 3.1.2, so until we hear otherwise, we should perhaps blame me and my laptop and not the doctests.)",
    "created_at": "2008-10-25T01:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4726",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:3 ddrake]:
I applied the patches on an Intel Core 2 Duo OS X machine (10.5) and got the same failure in polynomial_element:

```
File "/Applications/sage/tmp/polynomial_element.py", line 1947:
    sage: f.factor()
Expected:
    (1.0*x - 1.00000... + 1.0000...*I) * (1.0*x - 1.00000... + 0.999989...*I) * (1.0*x - 0.9999... + 1.00000...*I) * (1.0*x + 0.99999... - 1.00000...*I) * (1.0*x + 0.999996... - 0.99998...*I) * (1.0*x + 1.00001... - 1.00000...*I)
Got:
    (1.0*x - 1.00001180498 + 0.999999639235*I) * (1.0*x - 0.999994409957 + 1.00001040378*I) * (1.0*x - 0.999993785062 + 0.999989956987*I) * (1.0*x + 0.999991652054 - 1.00000998012*I) * (1.0*x + 0.999995530902 - 0.999987780431*I) * (1.0*x + 1.00001281704 - 1.00000223945*I)
**********************************************************************
```

(There were other failures as well, but (1) the new files were compiled with gcc 4.01, a known buggy compiler, and (2) the first patch didn't apply cleanly against 3.1.2, so until we hear otherwise, we should perhaps blame me and my laptop and not the doctests.)



---

archive/issue_comments_004727.json:
```json
{
    "body": "Attachment [trac_788.patch](tarball://root/attachments/some-uuid/ticket788/trac_788.patch) by anakha created at 2008-10-25 06:03:14",
    "created_at": "2008-10-25T06:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4727",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_788.patch](tarball://root/attachments/some-uuid/ticket788/trac_788.patch) by anakha created at 2008-10-25 06:03:14



---

archive/issue_comments_004728.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-25T06:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4728",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004729.json:
```json
{
    "body": "Patch updated (same name) to fix the failures you've seen.\n\nAbout your two points, \n\n(1) I do all my builds with \"gcc version 4.0.1 (Apple Inc. build 5484)\" and I never had any problem (on PPC though)\n\n(2) Yes that is your fault, these patches are against 3.1.4.\n\nSo if you try again with 3.1.4 as the base and still get the other failures, I would be interested.\n\nBy the way we now have tests report for x86, x84_64 and PPC 32 now.  I would still like tests on sparc or another architecture, but if the current patch does not get any failures, then I would consider it ready to go in.",
    "created_at": "2008-10-25T06:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4729",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Patch updated (same name) to fix the failures you've seen.

About your two points, 

(1) I do all my builds with "gcc version 4.0.1 (Apple Inc. build 5484)" and I never had any problem (on PPC though)

(2) Yes that is your fault, these patches are against 3.1.4.

So if you try again with 3.1.4 as the base and still get the other failures, I would be interested.

By the way we now have tests report for x86, x84_64 and PPC 32 now.  I would still like tests on sparc or another architecture, but if the current patch does not get any failures, then I would consider it ready to go in.



---

archive/issue_comments_004730.json:
```json
{
    "body": "Patch looks good to me. I did not merge the hunk in sage/rings/polynomial/polynomial_element.pyx around line 1942. That can be taken care of down the road. \n\nSince we will do an alpha2 shortly any numerical noise doctest failure can be fixed before rc0, so positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T04:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. I did not merge the hunk in sage/rings/polynomial/polynomial_element.pyx around line 1942. That can be taken care of down the road. 

Since we will do an alpha2 shortly any numerical noise doctest failure can be fixed before rc0, so positive review.

Cheers,

Michael



---

archive/issue_comments_004731.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-30T04:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_004732.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-30T04:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/788#issuecomment-4732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2
