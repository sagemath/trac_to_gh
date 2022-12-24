# Issue 1050: update optional valgrind+omega spkg to r7070 (or later)

archive/issues_001050.json:
```json
{
    "body": "Assignee: @williamstein\n\nFrom the r7069/r7070 commit log message:\n\n```\nMerged the MASSIF2 branch to the trunk.  Main changes:\n\n- ms_main.c: completely overhauled.\n\n- massif/tests/*:  lots of them now.\n\n- massif/perf/:  added.\n\n- massif/hp2ps:  removed.  No longer used.\n\n- vg_regtest: renamed the previously unused \"posttest\" notion to \"post\".\n  Using it for checking ms_print's output.\n\nAlthough the code has changed dramatically, as has the form of the tool's\noutput, the information presented in the output is basically the same,\nalthough it's now (hopefully) much more useful.  So the tool name is\nunchanged.\n```\n\nI should also add a spkg-check script to run the test suite, we are after all running code from the development branch.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1050\n\n",
    "created_at": "2007-11-01T04:48:39Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "update optional valgrind+omega spkg to r7070 (or later)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1050",
    "user": "mabshoff"
}
```
Assignee: @williamstein

From the r7069/r7070 commit log message:

```
Merged the MASSIF2 branch to the trunk.  Main changes:

- ms_main.c: completely overhauled.

- massif/tests/*:  lots of them now.

- massif/perf/:  added.

- massif/hp2ps:  removed.  No longer used.

- vg_regtest: renamed the previously unused "posttest" notion to "post".
  Using it for checking ms_print's output.

Although the code has changed dramatically, as has the form of the tool's
output, the information presented in the output is basically the same,
although it's now (hopefully) much more useful.  So the tool name is
unchanged.
```

I should also add a spkg-check script to run the test suite, we are after all running code from the development branch.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1050





---

archive/issue_comments_006390.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2007-11-01T04:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1050#issuecomment-6390",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_006391.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-11-01T04:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1050#issuecomment-6391",
    "user": "mabshoff"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_006392.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-11-01T04:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1050#issuecomment-6392",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_006393.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-01T04:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1050#issuecomment-6393",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006394.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/valgrind_3.3.0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T20:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1050#issuecomment-6394",
    "user": "mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/valgrind_3.3.0.spkg

Cheers,

Michael



---

archive/issue_comments_006395.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-25T20:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1050#issuecomment-6395",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006396.json:
```json
{
    "body": "Merged in the optional spkg repo and mirrored out.",
    "created_at": "2008-01-25T20:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1050",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1050#issuecomment-6396",
    "user": "mabshoff"
}
```

Merged in the optional spkg repo and mirrored out.
