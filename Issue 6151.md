# Issue 6151: fedora 10 64-bit -- tab completion causes segfault

Issue created by migration from https://trac.sagemath.org/ticket/6151

Original creator: was

Original creation time: 2009-05-28 17:56:51

Assignee: cwitty

The following was reported by kskedl on sage-support.  I can replicate it on the 64-bit fedora 10 vmware machine on boxen.math. 

I'll attach a big traceback below.  Note that surprisingly tab completing in "sage -ipython" does work. 


---

Comment by was created at 2009-05-28 17:57:31


```
wstein@boxen:~$ ssh fedora64
Last login: Thu May 14 07:31:14 2009 from host
ls /space
wstein@fedora64:~$ ls /space
wstein  x
wstein@fedora64:~$ cd /space/wstein/
wstein@fedora64:/space/wstein$ ls
farm  sage
wstein@fedora64:/space/wstein$ cd sage
wstein@fedora64:/space/wstein/sage$ ls
db  gap  init.sage  ipython  maxima_commandlist_cache.sobj  temp  valgrind
wstein@fedora64:/space/wstein/sage$ cd ../farm
wstein@fedora64:/space/wstein/farm$ ls
sage-4.0.rc1
wstein@fedora64:/space/wstein/farm$ cd sage-4.0.rc1/
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ ls
0.png        devel        HISTORY.txt  local       sage       sage.png             spkg          tmp
COPYING.txt  docs-0.html  install.log  makefile    sage0.png  sage-python          testlong.log  tmp.sws
data         examples     ipython      README.txt  sage1.png  sage-README-osx.txt  test.sobj
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Mod
| Sage Version 4.0.rc1, Release Date: 2009-05-28                     |
| Type notebook() for the GUI, and license() for information.        |
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

/space/wstein/farm/sage-4.0.rc1/local/bin/sage-sage: line 198: 15524 Segmentation fault      sage-ipython "$@" -i
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ ----------------------------------------------------------------------
----------------------------------------------------------------------
ERROR: Internal Python error in the inspect module.
Below is the traceback from this internal error.
| Sage Version 4.0.rc1, Release Date: 2009-05-28                     |
| Type notebook() for the GUI, and license() for information.        |
Traceback (most recent call last):
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 614, in text
    records = _fixed_getinnerframes(etb, context,self.tb_offset)
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 230, in _fixed_getinnerframes
    records  = fix_frame_records_filenames(inspect.getinnerframes(etb, context))
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/inspect.py", line 876, in getinnerframes
ERROR: Internal Python error in the inspect module.
Below is the traceback from this internal error.

Traceback (most recent call last):
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 614, in text
    records = _fixed_getinnerframes(etb, context,self.tb_offset)
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 230, in _fixed_getinnerframes
    records  = fix_frame_records_filenames(inspect.getinnerframes(etb, context))
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/inspect.py", line 876, in getinnerframes
    framelist.append((tb.tb_frame,) + getframeinfo(tb, context))
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/inspect.py", line 840, in getframeinfo
    lines, lnum = findsource(frame)
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/site-packages/IPython/ultraTB.py", line 149, in findsource
    lines = linecache.getlines(file, globals_dict)
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/linecache.py", line 40, in getlines
    return updatecache(filename, module_globals)
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/linecache.py", line 129, in updatecache
    lines = fp.readlines()
  File "/space/wstein/farm/sage-4.0.rc1/local/lib/python2.5/site-packages/sage/interfaces/get_sigs.py", line 9, in my_sigint
    raise KeyboardInterrupt
KeyboardInterrupt

Unfortunately, your original traceback can not be constructed.



**********************************************************************

Oops, IPython crashed. We do our best to make it stable, but...

A crash report was automatically generated with the following information:
  - A verbatim copy of the crash traceback.
  - A copy of your input history during this session.
  - Data on your current IPython configuration.

It was left in the file named:
	'/scratch/wstein/sage/ipython/IPython_crash_report.txt'
If you can email this file to the developers, the information in it will help
them in understanding and correcting the problem.

You can mail it to: Ville Vainio at vivainio@gmail.com
with the subject 'IPython Crash Report'.

If you want to do it now, the following command will work (under Unix):
mail -s 'IPython Crash Report' vivainio@gmail.com < /scratch/wstein/sage/ipython/IPython_crash_report.txt

To ensure accurate tracking of this issue, please file a report about it at:
http://projects.scipy.org/ipython/ipython/report

Press enter to exit:wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ wstein@fedora64:/space/wstein/farm/sage-4.0.rcwstein@fedora64:/space/wstein/farm/sage-4.0.rc1$                                                                
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ 
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ 
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ 
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ 
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ 
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ 
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ ls
0.png        devel        HISTORY.txt  local       sage       sage.png             spkg          tmp
COPYING.txt  docs-0.html  install.log  makefile    sage0.png  sage-python          testlong.log  tmp.sws
data         examples     ipython      README.txt  sage1.png  sage-README-osx.txt  test.sobj
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ ./sage -python
Python 2.5.2 (r252:60911, May 28 2009, 01:27:17) 
[GCC 4.3.2 20081105 (Red Hat 4.3.2-7)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ ./sage -ipython
Python 2.5.2 (r252:60911, May 28 2009, 01:27:17) 
Type "copyright", "credits" or "license" for more information.

IPython 0.9.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object'. ?object also works, ?? prints more.

In [1]: 
Do you really want to exit ([y]/n)? y
wstein@fedora64:/space/wstein/farm/sage-4.0.rc1$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/space/wstein/farm/sage-4.0.rc1/local/bin/sage-ipython
GNU gdb Fedora (6.8-29.fc10)
Copyright (C) 2008 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu"...
[Thread debugging using libthread_db enabled]
Python 2.5.2 (r252:60911, May 28 2009, 01:27:17) 
[GCC 4.3.2 20081105 (Red Hat 4.3.2-7)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
[New Thread 0x7ffff7fe46f0 (LWP 15668)]
Detaching after fork from child process 15677.
Detaching after fork from child process 15706.
sage: Mod
Program received signal SIGSEGV, Segmentation fault.
0x0000000000906499 in rl_complete_internal (what_to_do=33) at ../complete.c:1672
1672	../complete.c: No such file or directory.
	in ../complete.c
Missing separate debuginfos, use: debuginfo-install e2fsprogs-libs-1.41.3-2.fc10.x86_64 expat-2.0.1-5.x86_64 fontconfig-2.6.0-3.fc10.x86_64 glibc-2.9-3.x86_64 keyutils-libs-1.2-3.fc9.x86_64 krb5-libs-1.6.3-16.fc10.x86_64 libX11-1.1.4-6.fc10.x86_64 libXau-1.0.4-1.fc10.x86_64 libXdmcp-1.0.2-6.fc10.x86_64 libXpm-3.5.7-4.fc9.x86_64 libgcc-4.3.2-7.x86_64 libselinux-2.0.73-1.fc10.x86_64 libstdc++-4.3.2-7.x86_64 libxcb-1.1.91-5.fc10.x86_64 ncurses-libs-5.6-20.20080927.fc10.x86_64 openssl-0.9.8g-12.fc10.x86_64
(gdb) bt
#0  0x0000000000906499 in rl_complete_internal (what_to_do=33) at ../complete.c:1672
#1  0x0000000000906839 in rl_complete (ignore=<value optimized out>, invoking_key=-922097997) at ../complete.c:351
#2  0x00000000008ff35b in _rl_dispatch_subseq (key=9, map=<value optimized out>, got_subseq=0)
    at ../readline.c:737
#3  0x00000000008ff63f in _rl_dispatch (key=-882072640, map=0x7fffc909e6b3) at ../readline.c:687
#4  0x00000000008ffa1a in readline_internal_char () at ../readline.c:519
#5  0x00000000008ffd57 in readline_internal_charloop () at ../readline.c:545
#6  readline_internal () at ../readline.c:559
#7  readline (prompt=<value optimized out>) at ../readline.c:321
#8  0x0000000000112d99 in readline_until_enter_or_signal (prompt=0x7fffc90339e4 "sage: ", signal=0x7fffffffcec4)
    at /space/wstein/farm/sage-4.0.rc1/spkg/build/python-2.5.2.p9/src/Modules/readline.c:843
#9  0x0000000000112e52 in call_readline (sys_stdin=0x36cc56c6a0, sys_stdout=0x36cc56c780, 
    prompt=0x7fffc90339e4 "sage: ")
    at /space/wstein/farm/sage-4.0.rc1/spkg/build/python-2.5.2.p9/src/Modules/readline.c:873
#10 0x00000000004d15c2 in PyOS_Readline (sys_stdin=0x36cc56c6a0, sys_stdout=0x36cc56c780, 
    prompt=0x7fffc90339e4 "sage: ") at Parser/myreadline.c:208
#11 0x0000000000484d63 in builtin_raw_input (self=<value optimized out>, args=<value optimized out>)
    at Python/bltinmodule.c:1752
#12 0x000000000048ede0 in call_function () at Python/ceval.c:3573
#13 PyEval_EvalFrameEx (f=0x7fffc909a6b0, throwflag=<value optimized out>) at Python/ceval.c:2272
#14 0x00000000004904fd in PyEval_EvalCodeEx (co=0x7ffff0064198, globals=<value optimized out>, 
    locals=<value optimized out>, args=0x7ffff010a0c8, argcount=3, kws=0x7ffff010a0e0, kwcount=0, 
    defs=0x7ffff00a3140, defcount=2, closure=0x0) at Python/ceval.c:2836
#15 0x000000000048eab4 in fast_function () at Python/ceval.c:3669
#16 call_function () at Python/ceval.c:3594
#17 PyEval_EvalFrameEx (f=0x7ffff0109f20, throwflag=<value optimized out>) at Python/ceval.c:2272
#18 0x00000000004904fd in PyEval_EvalCodeEx (co=0x7ffff005c990, globals=<value optimized out>, 
    locals=<value optimized out>, args=0x7fffc909a278, argcount=2, kws=0x7fffc909a288, kwcount=0, 
    defs=0x7ffff0098ce8, defcount=1, closure=0x0) at Python/ceval.c:2836
#19 0x000000000048eab4 in fast_function () at Python/ceval.c:3669
#20 call_function () at Python/ceval.c:3594
#21 PyEval_EvalFrameEx (f=0x7fffc909a0f0, throwflag=<value optimized out>) at Python/ceval.c:2272
#22 0x00000000004904fd in PyEval_EvalCodeEx (co=0x7ffff005c6c0, globals=<value optimized out>, 
    locals=<value optimized out>, args=0x7ffff0117c50, argcount=2, kws=0x7ffff0117c60, kwcount=0, 
    defs=0x7ffff0098ca8, defcount=1, closure=0x0) at Python/ceval.c:2836
#23 0x000000000048eab4 in fast_function () at Python/ceval.c:3669
#24 call_function () at Python/ceval.c:3594
#25 PyEval_EvalFrameEx (f=0x7ffff0117ac0, throwflag=<value optimized out>) at Python/ceval.c:2272
#26 0x00000000004904fd in PyEval_EvalCodeEx (co=0x7ffff3222918, globals=<value optimized out>, 
    locals=<value optimized out>, args=0x3, argcount=1, kws=0x7e6060, kwcount=2, defs=0x7ffff16b7fe0, defcount=2, 
    closure=0x0) at Python/ceval.c:2836
#27 0x000000000048eab4 in fast_function () at Python/ceval.c:3669
#28 call_function () at Python/ceval.c:3594
#29 PyEval_EvalFrameEx (f=0x7e5ee0, throwflag=<value optimized out>) at Python/ceval.c:2272
#30 0x00000000004904fd in PyEval_EvalCodeEx (co=0x7ffff7f8dc60, globals=<value optimized out>, 
    locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2836
#31 0x00000000004906f2 in PyEval_EvalCode (co=0x7fffcb6ca3c0, globals=0x7fffc909e6b3, locals=0xffffffffcc39b750)
    at Python/ceval.c:494
#32 0x00000000004affd8 in run_mod () at Python/pythonrun.c:1273
#33 PyRun_FileExFlags (fp=0x775660, 
    filename=0x7fffffffec14 "/space/wstein/farm/sage-4.0.rc1/local/bin/sage-ipython", 
    start=<value optimized out>, globals=0x77e400, locals=0x77e400, closeit=0, flags=0x7fffffffddf0)
    at Python/pythonrun.c:1259
#34 0x00000000004b027b in PyRun_SimpleFileExFlags (fp=0x775660, 
    filename=0x7fffffffec14 "/space/wstein/farm/sage-4.0.rc1/local/bin/sage-ipython", closeit=0, 
    flags=0x7fffffffddf0) at Python/pythonrun.c:879
#35 0x000000000041244c in RunStartupFile () at Modules/main.c:134
#36 Py_Main (argc=<value optimized out>, argv=<value optimized out>) at Modules/main.c:520
#37 0x00000036cc21e576 in __libc_start_main () from /lib64/libc.so.6
#38 0x00000000004116f9 in _start ()
(gdb) 
```



---

Comment by was created at 2009-05-28 17:58:14

Note that the problem does *not* occur on 32-bit Fedora.


---

Comment by was created at 2009-05-28 18:34:55

i'm changing this to critical from blocker.  It should not block 4.0, since it could be very hard to fix, has been around forever, and wasn't a 4.0 goal.


---

Comment by was created at 2009-05-28 18:34:55

Changing priority from blocker to critical.


---

Comment by was created at 2009-05-28 19:23:45

mhansen points out that this is relevant: http://bugs.python.org/issue1593035


---

Comment by mhansen created at 2009-05-28 20:36:07

I've tested the spkg at #5218, and it fixes this issue.


---

Comment by mhansen created at 2009-05-28 20:36:07

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 20:36:07

Changing assignee from cwitty to mhansen.


---

Comment by was created at 2009-05-29 13:38:56

Resolution: fixed


---

Comment by was created at 2009-05-29 13:38:56

closing, since fixed by #5218.
