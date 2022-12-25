# Issue 3775: sage -maxima broken on OSX

archive/issues_003775.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nHowever, this is what happens when I invoke maxima, from the sage\ndirectory:\n\n$ /Applications/sage/local/bin/maxima\ndyld: Library not loaded: /Users/was/build/sage-3.0.5/local/lib/\nlibreadline.5.2.dylib\n  Referenced from: /Applications/sage/local/lib/maxima/5.13.0/binary-\nclisp/lisp.run\n  Reason: image not found\nTrace/BPT trap \n```\n\nThe solution is to source local/bin/sage-env before starting Maxima.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3775\n\n",
    "created_at": "2008-08-05T17:29:39Z",
    "labels": [
        "component: build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage -maxima broken on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3775",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
However, this is what happens when I invoke maxima, from the sage
directory:

$ /Applications/sage/local/bin/maxima
dyld: Library not loaded: /Users/was/build/sage-3.0.5/local/lib/
libreadline.5.2.dylib
  Referenced from: /Applications/sage/local/lib/maxima/5.13.0/binary-
clisp/lisp.run
  Reason: image not found
Trace/BPT trap 
```

The solution is to source local/bin/sage-env before starting Maxima.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3775





---

archive/issue_events_003997.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-05T17:35:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3775",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3775#event-3997"
}
```



---

archive/issue_comments_026792.json:
```json
{
    "body": "Arrg, invalid. The above happened when invoking Maxima directly, so this is not a bug on our end.",
    "created_at": "2008-08-05T17:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3775#issuecomment-26792",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Arrg, invalid. The above happened when invoking Maxima directly, so this is not a bug on our end.



---

archive/issue_comments_026793.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-05T17:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3775#issuecomment-26793",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid
