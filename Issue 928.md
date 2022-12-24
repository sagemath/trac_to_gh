# Issue 928: add delayed profiling mode for callgrind

archive/issues_000928.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: valgrind, callgrind\n\nIf you pass\n\n```\n --instr-atstart=no\n```\n\nto callgrind profiling is disabled until you tell callgrind via \n\n```\ncallgrind-control\n```\n\nto turn on profiling. After you have finished profiling your code you can use callgrind-contorl again to turn profiling off again. This can be very useful because if you only want to profile certain bits and also saves potentially a whole lot of time if it takes a long time to get to the part of the computation you want to profile.\n\nCarl Witty suggested this in #sage-devel yesterday.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/928\n\n",
    "created_at": "2007-10-19T16:49:03Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "add delayed profiling mode for callgrind",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/928",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Keywords: valgrind, callgrind

If you pass

```
 --instr-atstart=no
```

to callgrind profiling is disabled until you tell callgrind via 

```
callgrind-control
```

to turn on profiling. After you have finished profiling your code you can use callgrind-contorl again to turn profiling off again. This can be very useful because if you only want to profile certain bits and also saves potentially a whole lot of time if it takes a long time to get to the part of the computation you want to profile.

Carl Witty suggested this in #sage-devel yesterday.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/928





---

archive/issue_comments_005679.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-19T16:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/928#issuecomment-5679",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005680.json:
```json
{
    "body": "Changing component from packages: standard to packages: optional.",
    "created_at": "2014-11-13T14:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/928#issuecomment-5680",
    "user": "jdemeyer"
}
```

Changing component from packages: standard to packages: optional.
