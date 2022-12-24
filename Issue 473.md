# Issue 473: make the -valgrind target more flexible, add massif support

archive/issues_000473.json:
```json
{
    "body": "Assignee: mabshoff\n\nAt the moment the valgrind tool and flags are hardcoded in various scripts. So add checks for environment flag SAGE_VALGRIND_FLAGS to overwrite default.\n\nTo illustrate what you can do with other tools from the valgrind suite have a look at the two attached graphs created by the heap profiler massif.\n\nIt might also be nice to add a -valgrind to \"sage -testall\" to valgrind the whole test suite.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/473\n\n",
    "created_at": "2007-08-21T01:13:34Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "make the -valgrind target more flexible, add massif support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/473",
    "user": "mabshoff"
}
```
Assignee: mabshoff

At the moment the valgrind tool and flags are hardcoded in various scripts. So add checks for environment flag SAGE_VALGRIND_FLAGS to overwrite default.

To illustrate what you can do with other tools from the valgrind suite have a look at the two attached graphs created by the heap profiler massif.

It might also be nice to add a -valgrind to "sage -testall" to valgrind the whole test suite.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/473





---

archive/issue_comments_002366.json:
```json
{
    "body": "example of massif heap profiler",
    "created_at": "2007-08-21T01:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/473#issuecomment-2366",
    "user": "mabshoff"
}
```

example of massif heap profiler



---

archive/issue_comments_002367.json:
```json
{
    "body": "Attachment [massif.19869.ps](tarball://root/attachments/some-uuid/ticket473/massif.19869.ps) by mabshoff created at 2007-08-21 15:48:28\n\nIn addition increase the timeout value in sage-doctest to above 180 seconds depending on whether valgrind is used. Otherwise certain tests fail with timeouts:\n\n```\n==31586== Using valgrind-3.2.1, a dynamic binary instrumentation framework.\n==31586== Copyright (C) 2000-2006, and GNU GPL'd, by Julian Seward et al.\n==31586== For more details, rerun with: -v\n==31586==\n--31586-- DWARF2 CFI reader: unhandled CFI instruction 0:10\n--31586-- DWARF2 CFI reader: unhandled CFI instruction 0:10\n==31586==\n==31586== Total spacetime:   1,269,947,691,109 ms.B\n==31586== heap:              84.8%\n==31586== heap admin:        14.6%\n==31586== stack(s):           0.4%\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [222.3 s]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-08-21T15:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/473#issuecomment-2367",
    "user": "mabshoff"
}
```

Attachment [massif.19869.ps](tarball://root/attachments/some-uuid/ticket473/massif.19869.ps) by mabshoff created at 2007-08-21 15:48:28

In addition increase the timeout value in sage-doctest to above 180 seconds depending on whether valgrind is used. Otherwise certain tests fail with timeouts:

```
==31586== Using valgrind-3.2.1, a dynamic binary instrumentation framework.
==31586== Copyright (C) 2000-2006, and GNU GPL'd, by Julian Seward et al.
==31586== For more details, rerun with: -v
==31586==
--31586-- DWARF2 CFI reader: unhandled CFI instruction 0:10
--31586-- DWARF2 CFI reader: unhandled CFI instruction 0:10
==31586==
==31586== Total spacetime:   1,269,947,691,109 ms.B
==31586== heap:              84.8%
==31586== heap admin:        14.6%
==31586== stack(s):           0.4%
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [222.3 s]
```


Cheers,

Michael



---

archive/issue_comments_002368.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-22T19:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/473#issuecomment-2368",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002369.json:
```json
{
    "body": "The sage -t -valgrind support should have been added to the 2.8.3 release. \n\nMassif support will come for 2.9.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-30T00:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/473#issuecomment-2369",
    "user": "mabshoff"
}
```

The sage -t -valgrind support should have been added to the 2.8.3 release. 

Massif support will come for 2.9.

Cheers,

Michael



---

archive/issue_comments_002370.json:
```json
{
    "body": "http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-more-valgrind-to-sage-sage.patch\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-sage-cachegrind.patch\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-sage-massif.patch\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-change-location-of-log-file.patch\n\nCheers,\n\nMichael",
    "created_at": "2007-09-06T18:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/473#issuecomment-2370",
    "user": "mabshoff"
}
```

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-more-valgrind-to-sage-sage.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-sage-cachegrind.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-add-sage-massif.patch
http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.3.6-change-location-of-log-file.patch

Cheers,

Michael



---

archive/issue_comments_002371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T19:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/473#issuecomment-2371",
    "user": "was"
}
```

Resolution: fixed
