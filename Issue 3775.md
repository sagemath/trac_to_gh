# Issue 3775: sage -maxima broken on OSX

archive/issues_003775.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nHowever, this is what happens when I invoke maxima, from the sage\ndirectory:\n\n$ /Applications/sage/local/bin/maxima\ndyld: Library not loaded: /Users/was/build/sage-3.0.5/local/lib/\nlibreadline.5.2.dylib\n  Referenced from: /Applications/sage/local/lib/maxima/5.13.0/binary-\nclisp/lisp.run\n  Reason: image not found\nTrace/BPT trap \n```\n\nThe solution is to source local/bin/sage-env before starting Maxima.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3775\n\n",
    "created_at": "2008-08-05T17:29:39Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "title": "sage -maxima broken on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3775",
    "user": "mabshoff"
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

archive/issue_comments_026850.json:
```json
{
    "body": "Arrg, invalid. The above happened when invoking Maxima directly, so this is not a bug on our end.",
    "created_at": "2008-08-05T17:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3775#issuecomment-26850",
    "user": "mabshoff"
}
```

Arrg, invalid. The above happened when invoking Maxima directly, so this is not a bug on our end.



---

archive/issue_comments_026851.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-05T17:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3775#issuecomment-26851",
    "user": "mabshoff"
}
```

Resolution: invalid
