# Issue 1408: optional macaulay2 spkg doesn't install on osx10.5.1 due to problems with gc

archive/issues_001408.json:
```json
{
    "body": "Assignee: was\n\nThis was reported by Matt Miller:\n\n```\n\n\n       then mv -f \".deps/darwin_stop_world.Tpo\" \".deps/\ndarwin_stop_world.Plo\"; else rm -f \".deps/darwin_stop_world.Tpo\"; exit\n1; fi\nrm -f .libs/darwin_stop_world.lo\ngcc -DPACKAGE_NAME=\\\"gc\\\" -DPACKAGE_TARNAME=\\\"gc\\\" -DPACKAGE_VERSION=\n\\\"6.8\\\" \"-DPACKAGE_STRING=\\\"gc 6.8\\\"\" -DPACKAGE_BUGREPORT=\n\\\"Hans.Boehm@hp.com\\\" -DGC_VERSION_MAJOR=6 -DGC_VERSION_MINOR=8 -\nDPACKAGE=\\\"gc\\\" -DVERSION=\\\"6.8\\\" -DGC_DARdarwin_stop_world.c:203:\nerror: 'ppc_thread_state_t' has no member named 'r1'\ndarwin_stop_world.c:205: error: 'ppc_thread_state_t' has no member\nnamed 'r0'\n...\ndarwin_stop_world.c:235: error: 'ppc_thread_state_t' has no member\nnamed 'r31'\nmake[1]: *** [darwin_stop_world.lo] Error 1\nmake: *** [install-recursive] Error 1\nError installing GC garbage collection library.\n\nreal    2m44.303s\nuser    0m33.283s\nsys     0m37.224s\nsage: An error occurred while installing macaulay2-20061014\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1408\n\n",
    "created_at": "2007-12-06T04:19:03Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "optional macaulay2 spkg doesn't install on osx10.5.1 due to problems with gc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1408",
    "user": "was"
}
```
Assignee: was

This was reported by Matt Miller:

```


       then mv -f ".deps/darwin_stop_world.Tpo" ".deps/
darwin_stop_world.Plo"; else rm -f ".deps/darwin_stop_world.Tpo"; exit
1; fi
rm -f .libs/darwin_stop_world.lo
gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=
\"6.8\" "-DPACKAGE_STRING=\"gc 6.8\"" -DPACKAGE_BUGREPORT=
\"Hans.Boehm@hp.com\" -DGC_VERSION_MAJOR=6 -DGC_VERSION_MINOR=8 -
DPACKAGE=\"gc\" -DVERSION=\"6.8\" -DGC_DARdarwin_stop_world.c:203:
error: 'ppc_thread_state_t' has no member named 'r1'
darwin_stop_world.c:205: error: 'ppc_thread_state_t' has no member
named 'r0'
...
darwin_stop_world.c:235: error: 'ppc_thread_state_t' has no member
named 'r31'
make[1]: *** [darwin_stop_world.lo] Error 1
make: *** [install-recursive] Error 1
Error installing GC garbage collection library.

real    2m44.303s
user    0m33.283s
sys     0m37.224s
sage: An error occurred while installing macaulay2-20061014
```


Issue created by migration from https://trac.sagemath.org/ticket/1408





---

archive/issue_comments_009084.json:
```json
{
    "body": "Note also trac #1036.",
    "created_at": "2007-12-06T04:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1408#issuecomment-9084",
    "user": "was"
}
```

Note also trac #1036.



---

archive/issue_comments_009085.json:
```json
{
    "body": "And also #10.",
    "created_at": "2007-12-06T04:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1408#issuecomment-9085",
    "user": "mabshoff"
}
```

And also #10.



---

archive/issue_comments_009086.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-29T17:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1408#issuecomment-9086",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009087.json:
```json
{
    "body": "This has been fixed by the new M2.spkg from #10.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T17:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1408#issuecomment-9087",
    "user": "mabshoff"
}
```

This has been fixed by the new M2.spkg from #10.

Cheers,

Michael
