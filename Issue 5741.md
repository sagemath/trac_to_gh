# Issue 5741: Detect Atom CPUs as Core2 in the ATLAS detection script

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-11 01:21:48

Assignee: mabshoff

Build time on Sage for Atom hardware is insane since ATLAS does not identify Atom CPUs as known hardware and does a full tune, i.e. building Sage takes half a day :(

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 01:21:53

Changing status from new to assigned.


---

Comment by was created at 2009-04-11 05:25:33

This works fine for me.


```
real    13m57.018s
user    8m13.339s
sys     4m13.032s
Successfully installed gmp-mpir-1.0.rc8
```



---

Comment by mabshoff created at 2009-04-11 05:27:22

Well, this is about ATLAS :)

Cheer,

Michael


---

Comment by mabshoff created at 2009-04-18 02:10:34

This is basically the fix to make ATLAS detect an Atom as a Core2. There is 32 and 64 bit tuning info:

```
diff -r 0de046c62166 patches/archinfo_x86.c
--- a/patches/archinfo_x86.c	Sat Feb 21 00:57:22 2009 -0800
+++ b/patches/archinfo_x86.c	Fri Apr 17 19:09:51 2009 -0700
`@``@` -301,6 +301,7 `@``@`
          break;
       case 15:
       case 23:
+      case 28:
       case 29:
          iret = IntCore2;
          break;
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 23:24:56

Resolution: fixed


---

Comment by mabshoff created at 2009-04-18 23:24:56

Fixed in Sage 3.4.1.rc4 via #5219.

Cheers,

Michael
