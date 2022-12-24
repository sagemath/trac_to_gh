# Issue 3580: ensure that numpy is not imported on startup.

archive/issues_003580.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  craigcitro jvoight\n\nThis is a followup to #3577 that is forced by a merge conflict.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3580\n\n",
    "created_at": "2008-07-07T02:56:55Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "ensure that numpy is not imported on startup.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3580",
    "user": "was"
}
```
Assignee: cwitty

CC:  craigcitro jvoight

This is a followup to #3577 that is forced by a merge conflict.

Issue created by migration from https://trac.sagemath.org/ticket/3580





---

archive/issue_comments_025274.json:
```json
{
    "body": "Currently sage.rings.number_field.totallyreal_data imports numpy at startup. That might be due to the cythonization of totallyreal*, but I am not sure.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-02T03:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25274",
    "user": "mabshoff"
}
```

Currently sage.rings.number_field.totallyreal_data imports numpy at startup. That might be due to the cythonization of totallyreal*, but I am not sure.

Cheers,

Michael



---

archive/issue_comments_025275.json:
```json
{
    "body": "Moved the `import` further in, which was fine (didn't slow things down).\n\nMichael, should we add the following as a doctest somewhere?\n\n\n```\nsage: search_src(\"^import\", \"numpy\")\n\nsage: search_src(\"^from\", \"numpy\")\n\n```\n",
    "created_at": "2008-11-07T18:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25275",
    "user": "craigcitro"
}
```

Moved the `import` further in, which was fine (didn't slow things down).

Michael, should we add the following as a doctest somewhere?


```
sage: search_src("^import", "numpy")

sage: search_src("^from", "numpy")

```




---

archive/issue_comments_025276.json:
```json
{
    "body": "Changing assignee from cwitty to craigcitro.",
    "created_at": "2008-11-07T18:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25276",
    "user": "craigcitro"
}
```

Changing assignee from cwitty to craigcitro.



---

archive/issue_comments_025277.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-07T18:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25277",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025278.json:
```json
{
    "body": "We already have a doctest that is supposed to catch this (via grepping for numpy in \"sage -startuptime\"), but I think we should add a test in $SAGE_ROOT/devel/sage/tests that looks for the import of numpy in \"from sage import all\". Right now John's totally real code imports numpy, but the doctest to detect a numpy import at the top level is broken.\n\nWhat I would like to see is to not import numpy each time, but use something like the mechanism in \n\nhttp://trac.sagemath.org/sage_trac/attachment/ticket/3498/numpy-3.patch\n\nThe mechanism from that patch should be be stuck somewhere in the global namespace and we should enforce its use, i.e. a patch reviewed seeing something like a straight numpy import should complain.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-07T18:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25278",
    "user": "mabshoff"
}
```

We already have a doctest that is supposed to catch this (via grepping for numpy in "sage -startuptime"), but I think we should add a test in $SAGE_ROOT/devel/sage/tests that looks for the import of numpy in "from sage import all". Right now John's totally real code imports numpy, but the doctest to detect a numpy import at the top level is broken.

What I would like to see is to not import numpy each time, but use something like the mechanism in 

http://trac.sagemath.org/sage_trac/attachment/ticket/3498/numpy-3.patch

The mechanism from that patch should be be stuck somewhere in the global namespace and we should enforce its use, i.e. a patch reviewed seeing something like a straight numpy import should complain.

Cheers,

Michael



---

archive/issue_comments_025279.json:
```json
{
    "body": "This removes the numpy import from the totally real enumeration code, and it fixes a pesky but somewhat serious bug in the code. \n\nJohn Voight and I team wrote/reviewed this.\n\nI will open a new ticket for the new import of numpy on startup.",
    "created_at": "2008-11-09T04:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25279",
    "user": "craigcitro"
}
```

This removes the numpy import from the totally real enumeration code, and it fixes a pesky but somewhat serious bug in the code. 

John Voight and I team wrote/reviewed this.

I will open a new ticket for the new import of numpy on startup.



---

archive/issue_comments_025280.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-09T04:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25280",
    "user": "craigcitro"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_025281.json:
```json
{
    "body": "There is a slight problem:\n\n```\nsage -t -long devel/sage/sage/rings/number_field/totallyreal_data.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage/sage/rings/number_field/totallyreal_data.pyx\", line 200:\n    sage: [RealField(10)(x) for x in ls]\nExpected:\n    [-1.0000, -1.0000]\nGot:\n    [-1.0, -1.0]\n**********************************************************************\n1 items had failures:\n```\n",
    "created_at": "2008-11-09T08:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25281",
    "user": "mabshoff"
}
```

There is a slight problem:

```
sage -t -long devel/sage/sage/rings/number_field/totallyreal_data.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage/sage/rings/number_field/totallyreal_data.pyx", line 200:
    sage: [RealField(10)(x) for x in ls]
Expected:
    [-1.0000, -1.0000]
Got:
    [-1.0, -1.0]
**********************************************************************
1 items had failures:
```




---

archive/issue_comments_025282.json:
```json
{
    "body": "Attachment [trac-3580.patch](tarball://root/attachments/some-uuid/ticket3580/trac-3580.patch) by craigcitro created at 2008-11-09 08:22:18",
    "created_at": "2008-11-09T08:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25282",
    "user": "craigcitro"
}
```

Attachment [trac-3580.patch](tarball://root/attachments/some-uuid/ticket3580/trac-3580.patch) by craigcitro created at 2008-11-09 08:22:18



---

archive/issue_comments_025283.json:
```json
{
    "body": "Oops. Ticket updated.",
    "created_at": "2008-11-09T08:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25283",
    "user": "craigcitro"
}
```

Oops. Ticket updated.



---

archive/issue_comments_025284.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-09T08:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25284",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025285.json:
```json
{
    "body": "Merged in Sage 3.2.rc0",
    "created_at": "2008-11-09T08:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3580#issuecomment-25285",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc0
