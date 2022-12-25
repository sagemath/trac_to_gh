# Issue 1202: sqlite-3.5.2.p1.spkg segfaults sage/databases/database.py

archive/issues_001202.json:
```json
{
    "body": "Assignee: @yqiang\n\n```\nStarting program: /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/bin/python .doctest_database.py\n[Thread debugging using libthread_db enabled]\n[New Thread 47503556656992 (LWP 22789)]\n[New Thread 1082132832 (LWP 23296)]\n[Thread 1082132832 (LWP 23296) exited]\n[New Thread 1090525536 (LWP 23297)]\n[Thread 1090525536 (LWP 23297) exited]\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 47503556656992 (LWP 22789)]\nsqlite3_step (pStmt=<value optimized out>) at ./src/vdbeapi.c:389\n389     ./src/vdbeapi.c: No such file or directory.\n        in ./src/vdbeapi.c\n(gdb) bt\n#0  sqlite3_step (pStmt=<value optimized out>) at ./src/vdbeapi.c:389\n#1  0x00002b34588676f1 in _sqlite_step_with_busyhandler (statement=0x0, connection=<value optimized out>)\n    at /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/spkg/build/python-2.5.1.p8/src/Modules/_sqlite/util.c:33\n#2  0x00002b34588644b3 in cursor_executescript (self=0x2b345a33d0e0, args=<value optimized out>)\n    at /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/spkg/build/python-2.5.1.p8/src/Modules/_sqlite/cursor.c:788\n#3  0x0000000000415523 in PyObject_Call (func=0x0, arg=0x1, kw=0x1) at Objects/abstract.c:1860\n#4  0x000000000047c851 in PyEval_CallObjectWithKeywords (func=0x2aaaaaaf1bd8, arg=0x2b345a3400d0, kw=0x0)\n    at Python/ceval.c:3433\n#5  0x00002b3458862405 in connection_executescript (self=<value optimized out>, args=0x2b345a3400d0,\n    kwargs=<value optimized out>)\n    at /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/spkg/build/python-2.5.1.p8/src/Modules/_sqlite/connection.c:1001\n#6  0x0000000000483032 in PyEval_EvalFrameEx (f=0x19f3020, throwflag=<value optimized out>) at Python/ceval.c:3564\n#7  0x000000000048403b in PyEval_EvalFrameEx (f=0x19f2a50, throwflag=<value optimized out>) at Python/ceval.c:3650\n#8  0x000000000048403b in PyEval_EvalFrameEx (f=0x1be2330, throwflag=<value optimized out>) at Python/ceval.c:3650\n#9  0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2aaaaaaf0b70, globals=<value optimized out>,\n    locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)\n    at Python/ceval.c:2831\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1202\n\n",
    "closed_at": "2007-12-14T02:10:02Z",
    "created_at": "2007-11-18T23:11:00Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "sqlite-3.5.2.p1.spkg segfaults sage/databases/database.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @yqiang

```
Starting program: /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/bin/python .doctest_database.py
[Thread debugging using libthread_db enabled]
[New Thread 47503556656992 (LWP 22789)]
[New Thread 1082132832 (LWP 23296)]
[Thread 1082132832 (LWP 23296) exited]
[New Thread 1090525536 (LWP 23297)]
[Thread 1090525536 (LWP 23297) exited]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47503556656992 (LWP 22789)]
sqlite3_step (pStmt=<value optimized out>) at ./src/vdbeapi.c:389
389     ./src/vdbeapi.c: No such file or directory.
        in ./src/vdbeapi.c
(gdb) bt
#0  sqlite3_step (pStmt=<value optimized out>) at ./src/vdbeapi.c:389
#1  0x00002b34588676f1 in _sqlite_step_with_busyhandler (statement=0x0, connection=<value optimized out>)
    at /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/spkg/build/python-2.5.1.p8/src/Modules/_sqlite/util.c:33
#2  0x00002b34588644b3 in cursor_executescript (self=0x2b345a33d0e0, args=<value optimized out>)
    at /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/spkg/build/python-2.5.1.p8/src/Modules/_sqlite/cursor.c:788
#3  0x0000000000415523 in PyObject_Call (func=0x0, arg=0x1, kw=0x1) at Objects/abstract.c:1860
#4  0x000000000047c851 in PyEval_CallObjectWithKeywords (func=0x2aaaaaaf1bd8, arg=0x2b345a3400d0, kw=0x0)
    at Python/ceval.c:3433
#5  0x00002b3458862405 in connection_executescript (self=<value optimized out>, args=0x2b345a3400d0,
    kwargs=<value optimized out>)
    at /tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/spkg/build/python-2.5.1.p8/src/Modules/_sqlite/connection.c:1001
#6  0x0000000000483032 in PyEval_EvalFrameEx (f=0x19f3020, throwflag=<value optimized out>) at Python/ceval.c:3564
#7  0x000000000048403b in PyEval_EvalFrameEx (f=0x19f2a50, throwflag=<value optimized out>) at Python/ceval.c:3650
#8  0x000000000048403b in PyEval_EvalFrameEx (f=0x1be2330, throwflag=<value optimized out>) at Python/ceval.c:3650
#9  0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2aaaaaaf0b70, globals=<value optimized out>,
    locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2831
```

Issue created by migration from https://trac.sagemath.org/ticket/1202





---

archive/issue_comments_007426.json:
```json
{
    "body": "On OSX 10.5 that doctest just hangs.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-20T09:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1202#issuecomment-7426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

On OSX 10.5 that doctest just hangs.

Cheers,

Michael



---

archive/issue_comments_007427.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T02:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1202#issuecomment-7427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007428.json:
```json
{
    "body": "Fixed by #1492.",
    "created_at": "2007-12-14T02:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1202#issuecomment-7428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by #1492.



---

archive/issue_events_003203.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-14T02:10:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1202",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1202#event-3203"
}
```
