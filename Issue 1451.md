# Issue 1451: segfault in permgroup.py

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2007-12-10 18:55:31

Assignee: mhansen

CC:  sage-combinat

GDB backtrace:

```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47660312751968 (LWP 17787)]
0x00002b58c7e5b8ef in malloc_consolidate () from /lib/libc.so.6
(gdb) bt
#0  0x00002b58c7e5b8ef in malloc_consolidate () from /lib/libc.so.6
#1  0x00002b58c7e5d879 in _int_malloc () from /lib/libc.so.6
#2  0x00002b58c7e5f25d in malloc () from /lib/libc.so.6
#3  0x00000000004a3d76 in PyArena_New () at Python/pyarena.c:83
#4  0x00000000004a6ef7 in Py_CompileStringFlags (str=0x2b58c802a0e0 "\001", filename=0x0, start=388, flags=0x7fffe326c020)
    at Python/pythonrun.c:1314
#5  0x000000000047bf59 in builtin_compile (self=<value optimized out>, args=<value optimized out>) at Python/bltinmodule.c:464
#6  0x0000000000483032 in PyEval_EvalFrameEx (f=0x183fa90, throwflag=<value optimized out>) at Python/ceval.c:3564
#7  0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2b58da42d120, globals=<value optimized out>, locals=<value optimized out>, 
    args=0x183edd0, argcount=4, kws=0x183edf0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#8  0x000000000048365d in PyEval_EvalFrameEx (f=0x183ec20, throwflag=<value optimized out>) at Python/ceval.c:3660
#9  0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2b58da42d288, globals=<value optimized out>, locals=<value optimized out>, 
    args=0x3, argcount=2, kws=0x6c64a0, kwcount=0, defs=0x2b58daa9be28, defcount=3, closure=0x0) at Python/ceval.c:2831
#10 0x000000000048365d in PyEval_EvalFrameEx (f=0x6c62b0, throwflag=<value optimized out>) at Python/ceval.c:3660
#11 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2b58da42dbe8, globals=<value optimized out>, locals=<value optimized out>, 
    args=0x8, argcount=1, kws=0x6bed68, kwcount=3, defs=0x2b58daa95be8, defcount=9, closure=0x0) at Python/ceval.c:2831
#12 0x000000000048365d in PyEval_EvalFrameEx (f=0x6bebc0, throwflag=<value optimized out>) at Python/ceval.c:3660
#13 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2b58c81945d0, globals=<value optimized out>, locals=<value optimized out>, 
    args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#14 0x00000000004851d2 in PyEval_EvalCode (co=0x2b58c802a0e0, globals=0x0, locals=0x7560000000000184) at Python/ceval.c:494
#15 0x00000000004a648e in PyRun_FileExFlags (fp=0x64f010, filename=0x7fffe326decb ".doctest_permgroup.py", 
    start=<value optimized out>, globals=0x672630, locals=0x672630, closeit=1, flags=0x7fffe326cce0) at Python/pythonrun.c:1271
#16 0x00000000004a6720 in PyRun_SimpleFileExFlags (fp=0x64f010, filename=0x7fffe326decb ".doctest_permgroup.py", closeit=1, 
    flags=0x7fffe326cce0) at Python/pythonrun.c:877
#17 0x0000000000412100 in Py_Main (argc=<value optimized out>, argv=0x7fffe326cdf8) at Modules/main.c:523
#18 0x00002b58c7e0d4ca in __libc_start_main () from /lib/libc.so.6
#19 0x000000000041163a in _start () at ../sysdeps/x86_64/elf/start.S:113
```



---

Comment by rlm created at 2007-12-10 19:22:51

To reproduce run doctests under gdb and hit "bt"


---

Comment by mabshoff created at 2007-12-11 17:58:33

Fixed by #1296, which was merged in 2.9.alpha5.


---

Comment by mabshoff created at 2007-12-11 17:58:33

Resolution: fixed
