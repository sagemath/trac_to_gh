# Issue 6613: patch from #6393 should also demonstrate that bug is fixed

archive/issues_006613.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  revans@ucsd.edu\n\nAt this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/84bdf37a75345bb5/2a86396377e1c81d) thread, Ron Evans provided a test case to demonstrate that the function `jacobi_sum()` in Sage 4.1 provided wrong answers:\n\n```\nsage: G=DirichletGroup(5); X=G.list(); Y=X[0]; Z=X[1];  #Y is trivial and Z is quartic\n\nsage: sum([Y(x)*Z(1-x) for x in IntegerModRing(5)])\n -1\nsage: # The value -1 above is the correct value of the Jacobi sum J(Y, Z).\n\nsage: Y.jacobi_sum(Z);    Z.jacobi_sum(Y)\n0\n0\nsage: #The 0 values above are incorrect values of J(Y, Z).\n```\n\nThe patch at #6393 fixed the reported bug, but left out the test case. The reported test case should be included to demonstrate that the bug has been fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6613\n\n",
    "created_at": "2009-07-24T14:33:13Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "patch from #6393 should also demonstrate that bug is fixed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6613",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @craigcitro

CC:  revans@ucsd.edu

At this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/84bdf37a75345bb5/2a86396377e1c81d) thread, Ron Evans provided a test case to demonstrate that the function `jacobi_sum()` in Sage 4.1 provided wrong answers:

```
sage: G=DirichletGroup(5); X=G.list(); Y=X[0]; Z=X[1];  #Y is trivial and Z is quartic

sage: sum([Y(x)*Z(1-x) for x in IntegerModRing(5)])
 -1
sage: # The value -1 above is the correct value of the Jacobi sum J(Y, Z).

sage: Y.jacobi_sum(Z);    Z.jacobi_sum(Y)
0
0
sage: #The 0 values above are incorrect values of J(Y, Z).
```

The patch at #6393 fixed the reported bug, but left out the test case. The reported test case should be included to demonstrate that the bug has been fixed.

Issue created by migration from https://trac.sagemath.org/ticket/6613





---

archive/issue_comments_054036.json:
```json
{
    "body": "depends on #6393",
    "created_at": "2009-07-24T14:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6613#issuecomment-54036",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

depends on #6393



---

archive/issue_comments_054037.json:
```json
{
    "body": "Attachment [trac_6613-test-case.patch](tarball://root/attachments/some-uuid/ticket6613/trac_6613-test-case.patch) by mvngu created at 2009-07-24 14:39:45",
    "created_at": "2009-07-24T14:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6613#issuecomment-54037",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6613-test-case.patch](tarball://root/attachments/some-uuid/ticket6613/trac_6613-test-case.patch) by mvngu created at 2009-07-24 14:39:45



---

archive/issue_comments_054038.json:
```json
{
    "body": "i confirm that the doctests correctly repesents the given testcase.",
    "created_at": "2009-07-24T16:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6613#issuecomment-54038",
    "user": "https://github.com/haraldschilly"
}
```

i confirm that the doctests correctly repesents the given testcase.



---

archive/issue_comments_054039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T22:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6613",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6613#issuecomment-54039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
