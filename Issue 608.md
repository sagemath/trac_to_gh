# Issue 608: bug in mobius

Issue created by migration from https://trac.sagemath.org/ticket/608

Original creator: was

Original creation time: 2007-09-07 00:37:08

Assignee: somebody


```
I'm distraught (well, not quite that bad) about the following transcript for
two reasons:
1)  It shouldn't simply blow up
2)  I think it should actually work (and it used to work back about last
spring -- I have code that relies on it)

--
Joel

joel@friedrich ~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.3.6, Release Date: 2007-09-06                     |
| Type notebook() for the GUI, and license() for information.        |
sage: x=GF(7)['x'].0
sage: moebius(x+2)

 ***   not an integer argument in an arithmetic function
/home/joel/sage/local/bin/sage-sage: line 190: 18621 Aborted
sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"
joel@friedrich ~$
```



---

Comment by mabshoff created at 2007-09-07 00:55:57

backtrace:

```
[Switching to Thread 46912496204160 (LWP 17241)]
0x0000003105830015 in raise () from /lib64/libc.so.6
(gdb) bt
#0  0x0000003105830015 in raise () from /lib64/libc.so.6
#1  0x0000003105831980 in abort () from /lib64/libc.so.6
#2  0x00002aaab4d14f8a in pari_init_opts () from /tmp/Work2/sage-2.8.3.6-clean/local/lib/libpari-gmp.so.2
#3  0x00007fffa64021c0 in ?? ()
#4  0x000000000ac3e9d0 in ?? ()
#5  0x00000000004a0009 in r_object (p=0x6) at Python/marshal.c:682
#6  0x00000000004a077e in r_object (p=0x73) at Python/marshal.c:428
#7  0x00007fffa63ffde1 in ?? ()
#8  0x0000000000721ea0 in _Py_SwappedOp ()
#9  0x000000000049be72 in find_module (fullname=0x7fffa6400e60 "c", subname=0xac6d140 "", path=<value optimized out>,
    buf=0x7fffa63ffde1 ".pyc", buflen=4097, p_fp=0x7fffa6400da0, p_loader=0xacce908) at Python/import.c:1427
#10 0x0000000000000001 in ?? ()
#11 0x000000000acce908 in ?? ()
#12 0x0000000000000004 in ?? ()
#13 0x00002aaaae4cbcf0 in ?? ()
#14 0x0000000000000000 in ?? ()
```



---

Comment by was created at 2007-09-07 01:37:40

Fixed -- see attached patch.


---

Attachment


---

Comment by was created at 2007-09-07 01:37:59

Resolution: fixed
