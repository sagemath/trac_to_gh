# Issue 4946: readline on opensuse11 64-bit still doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/4946

Original creator: was

Original creation time: 2009-01-07 00:12:43

Assignee: mabshoff

On opensuse64 (a sage.math vmware machine):

```
Overwriting libreadline.so.5.2 with the system one
cp: cannot stat `/lib/libreadline.so.5.2': No such file or directory
Readline's build claims to have finished, but files that should have been built weren't.

real    3m23.513s
user    0m15.741s
sys     0m23.429s
sage: An error occurred while installing readline-5.2.p5
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wstein/build/opensuse64/build/sage-3.2.3/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/wstein/build/opensuse64/build/sage-3.2.3/spkg/build/readline-5.2.p5 and type 'make'.
Instead type "/home/wstein/build/opensuse64/build/sage-3.2.3/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wstein/build/opensuse64/build/sage-3.2.3/spkg/build/readline-5.2.p5
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/readline-5.2.p5] Error 1
make[1]: Leaving directory `/home/wstein/build/opensuse64/build/sage-3.2.3/spkg'

real    4m7.156s
user    0m16.409s
sys     0m23.905s
. local/bin/sage-env && sage-starts && sage-maketest
Testing that Sage starts...
/usr/bin/env: sage.bin: No such file or directory
Traceback (most recent call last):
  File "/home/wstein/build/opensuse64/build/sage-3.2.3/local/bin/sage-eval", line 4, in <module>
    from sage.all import *
ImportError: No module named sage.all
Sage failed to startup.
make: *** [check] Error 1
wstein@opensuse64:~/build/opensuse64$ 
```



---

Comment by mabshoff created at 2009-01-07 03:52:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-07 03:52:32

The fix here is to use /lib64 on OpenSUSE 11.1 with 64 bits while using /lib with the 32 bit version. I will post an updated spkg in the next 24 hours.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 19:34:08

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha4/readline-5.2.p6.spkg

fixes the problem. Tested on OpenSUSE 11.1 64 bit :)

Cheers,

Michael


---

Comment by mhansen created at 2009-02-03 01:04:01

Looks good.


---

Comment by mabshoff created at 2009-02-03 01:05:19

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 01:05:19

Resolution: fixed
