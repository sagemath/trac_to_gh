# Issue 1202: sqlite-3.5.2.p1.spkg segfaults sage/databases/database.py

Issue created by migration from https://trac.sagemath.org/ticket/1202

Original creator: mabshoff

Original creation time: 2007-11-18 23:11:00

Assignee: yi


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



---

Comment by mabshoff created at 2007-11-20 09:38:25

On OSX 10.5 that doctest just hangs.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-14 02:10:02

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 02:10:02

Fixed by #1492.
