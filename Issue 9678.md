# Issue 9678: Rewrite interrupt handling

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-08-03 21:33:54

Assignee: jason

CC:  leif

Keywords: interrupt, error, c, cython

There are lots of things to be improved in the interrupt handling routines in c_lib/src/interrupt.c and c_lib/include/interrupt.h, such as:

 * using sigaction() instead of signal()
 * having an interface for more general errors which are not signals
 * testing!


---

Comment by jdemeyer created at 2010-09-16 07:41:01

Changing component from misc to c_lib.


---

Comment by jdemeyer created at 2010-09-16 07:41:01

Changing assignee from jason to tba.


---

Comment by leif created at 2010-09-16 09:09:39

Author of what? ;-)


---

Comment by jdemeyer created at 2010-10-17 18:48:11

Changing status from new to needs_work.


---

Comment by jdemeyer created at 2010-11-14 17:33:27

Changing assignee from tba to jdemeyer.


---

Comment by jdemeyer created at 2011-01-14 17:40:59

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by vbraun created at 2011-01-21 00:15:44

Definite improvement! We should put it in the very next Sage-4.6.2.alpha to give it as much exposure as possible since it touches a couple of core C files.


---

Comment by vbraun created at 2011-01-21 00:15:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-21 08:42:48

Replying to [comment:30 vbraun]:
> Definite improvement! We should put it in the very next Sage-4.6.2.alpha to give it as much exposure as possible since it touches a couple of core C files.

Alternatively, I am considering making 4.6.2 a pretty straightforward release and then putting various "big" tickets such as this one, #9433, #10572 in the next release which would then be sage-4.7.


---

Comment by jdemeyer created at 2011-02-07 20:19:06

Changing priority from major to blocker.


---

Comment by vbraun created at 2011-02-19 22:38:42

I'm trying out Sage-4.6.2.rc0 in Fedora 14 i386 inside `VirtualBox`, and it doesn't catch the SIGILL. Bactrace is below. Everything else works fine. Also, no such issue on my native Fedora 14 x86_64.

I'm not sure who is to blame here, could be something with the virtual machine. I did write a SIGILL handler in Perl and that works, so `VirtualBox` is at least in principle able to have guests raise and handle SIGILL. Though there is also some forking involved... 

The only thing thats special about SIGILL that comes to mind is that it might not be automatically be reset to SIG_DFL upon entrance. But I don't see how that could cause this. Here is my testcase:

```
[vbraun`@`localhost ~]$ sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
/home/vbraun/Sage/sage/local/bin/sage-ipython
GNU gdb (GDB) Fedora (7.2-41.fc14)
Copyright (C) 2010 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-redhat-linux-gnu".
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>...
Reading symbols from /mnt/sage/vbraun/sage-4.6.2.rc0/local/bin/python...done.
[Thread debugging using libthread_db enabled]
Python 2.6.4 (r264:75706, Feb 19 2011, 16:56:24) 
[GCC 4.5.1 20100924 (Red Hat 4.5.1-4)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Traceback (most recent call last):
  File "/usr/share/gdb/auto-load/usr/lib/libstdc++.so.6.0.14-gdb.py", line 59, in <module>
    from libstdcxx.v6.printers import register_libstdcxx_printers
  File "/usr/lib/../share/gcc-4.5.1/python/libstdcxx/v6/printers.py", line 19, in <module>
    import itertools
ImportError: No module named itertools
Detaching after fork from child process 10247.
}}}  
So far, so good. Now run:
{{{
sage: import sage.tests.interrupt
sage: sage.tests.interrupt.test_signal_ill()
Detaching after fork from child process 10248.
| Sage Version 4.6.2.rc0, Release Date: 2011-02-18                   |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGILL, Illegal instruction.
0x05dac6b1 in _sig_on_prejmp (__pyx_self=<value optimized out>, __pyx_args=0xb7fa702c, __pyx_kwds=0x0) at /home/vbraun/Sage/sage/local/include/csage/interrupt.h:192
192	        _signals.sig_on_count++;
Missing separate debuginfos, use: debuginfo-install expat-2.0.1-10.fc13.i686 fontconfig-2.8.0-2.fc14.i686 glibc-2.13-1.i686 keyutils-libs-1.2-6.fc12.i686 krb5-libs-1.8.2-8.fc14.i686 libcom_err-1.41.12-6.fc14.i686 libgcc-4.5.1-4.fc14.i686 libgfortran-4.5.1-4.fc14.i686 libselinux-2.0.96-6.fc14.1.i686 libstdc++-4.5.1-4.fc14.i686 ncurses-libs-5.7-9.20100703.fc14.i686 nss-softokn-freebl-3.12.9-2.fc14.i686 openssl-1.0.0d-1.fc14.i686
(gdb) l
187	    fprintf(stderr, "sig_on (counter = %i) at %s:%i\n", _signals.sig_on_count+1, file, line);
188	    fflush(stderr);
189	#endif
190	    if (_signals.sig_on_count > 0)
191	    {
192	        _signals.sig_on_count++;
193	        return 1;
194	    }
195	
196	    /* At this point, _signals.sig_on_count == 0 */
(gdb) bt
#0  0x05dac6b1 in _sig_on_prejmp (__pyx_self=<value optimized out>, __pyx_args=0xb7fa702c, __pyx_kwds=0x0)
    at /home/vbraun/Sage/sage/local/include/csage/interrupt.h:192
#1  __pyx_pf_4sage_5tests_9interrupt_test_signal_ill (__pyx_self=<value optimized out>, __pyx_args=0xb7fa702c, __pyx_kwds=0x0) at sage/tests/interrupt.c:2878
#2  0x0017c398 in PyCFunction_Call (func=0xaad686c, arg=0xb7fa702c, kw=0x0) at Objects/methodobject.c:85
#3  0x001de9dd in call_function (f=0x820c4d4, throwflag=0) at Python/ceval.c:3706
#4  PyEval_EvalFrameEx (f=0x820c4d4, throwflag=0) at Python/ceval.c:2389
#5  0x001e06e7 in PyEval_EvalCodeEx (co=0xaa5fd58, globals=0x83cf3e4, locals=0x83cf3e4, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, 
    closure=0x0) at Python/ceval.c:2968
#6  0x001e0803 in PyEval_EvalCode (co=0xaa5fd58, globals=0x83cf3e4, locals=0x83cf3e4) at Python/ceval.c:522
#7  0x001deccb in exec_statement (f=0x81630ec, throwflag=0) at Python/ceval.c:4401
#8  PyEval_EvalFrameEx (f=0x81630ec, throwflag=0) at Python/ceval.c:1717
#9  0x001e06e7 in PyEval_EvalCodeEx (co=0x837aa88, globals=0x8370714, locals=0x0, args=0x8162c08, argcount=2, kws=0x8162c10, kwcount=0, defs=0x0, defcount=0, 
    closure=0x0) at Python/ceval.c:2968
#10 0x001dea92 in fast_function (f=0x8162abc, throwflag=0) at Python/ceval.c:3802
}}}


---

Comment by jdemeyer created at 2011-02-20 11:09:27

Volker, do you have `strace` installed?  If so, you could try

```
$ mkdir trace
$ strace -ff -o trace/sage ./sage -c 'import sage.tests.interrupt; sage.tests.interrupt.test_signal_ill()'
```


and send me the `trace/` directory.

And maybe do the same for `test_signal_bus()` to compare with.


---

Comment by vbraun created at 2011-02-20 11:25:00

Sure, no problem. I did strace ill, bus, and fpe and uploaded the trace/ directory to http://www.stp.dias.ie/~vbraun/trace.tar.bz2


---

Comment by vbraun created at 2011-02-20 11:31:07

Hold your horses! Its working now, and SIGILL is caught correctly. I did rebuild the sage library in the meantime, so I probably miscompiled something before.


---

Comment by jdemeyer created at 2011-02-20 14:48:28

In any case, based on your trace, it looks like everything is working correctly.  I see the following:

```
--- SIGILL (Illegal instruction) `@` 0 (0) ---
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
write(2, "Traceback (most recent call last"..., 35) = 35
write(2, "  File \"/home/vbraun/Sage/sage/l"..., 74) = 74
```


So, the program receives `SIGILL` and prints a Traceback, which is exactly what should happen.

I cannot understand why at some point it did not work for you...


---

Comment by vbraun created at 2011-02-20 16:49:42

After many more rebuilds I found the problem: On i386 (and only i386) the Parma Polyhedra library (PPL, #10039) tests if SSE is available. It does this during the library initialization by installing a SIGILL handler and then issuing SSE instructions. It then resets the handler to `signal(SIGILL, SIG_DFL)`. Clearly, this deactivates Sage's SIGILL handler. 

Since we don't use PPL's floating point arithmetics I'll make sure to configure it in a way that it does not test for SSE availability.


---

Comment by jdemeyer created at 2011-02-20 16:55:10

Replying to [comment:40 vbraun]:
> After many more rebuilds I found the problem: On i386 (and only i386) the Parma Polyhedra library (PPL, #10039) tests if SSE is available. It does this during the library initialization by installing a SIGILL handler and then issuing SSE instructions. It then resets the handler to `signal(SIGILL, SIG_DFL)`. Clearly, this deactivates Sage's SIGILL handler. 

I consider this to be a bug in PPL.  Using `sigaction()` or `signal()`, it is possible to save an existing signal handler and then restore it afterwards.


---

Comment by vbraun created at 2011-02-20 17:05:31

I agree and will report it upstream.


---

Comment by jdemeyer created at 2011-03-08 21:45:19

Resolution: fixed
