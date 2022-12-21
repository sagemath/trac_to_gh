# Issue 489: Expose LiE functionality in SAGE

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-08-24 16:06:44

Assignee: was

Now, that LiE ( http://www-math.univ-poitiers.fr/~maavl/LiE/ ) is officially GPL, we can include it in SAGE.  Things to do:

1) Write an interface to the LiE interpreter.

2) Begin making a C/Pyrex wrapper.  (I've looked at the code, and it looks like it'll be pretty clean.)


---

Comment by mhansen created at 2007-08-24 16:06:54

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-08-24 16:22:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-08-24 17:00:35

and it already has been build on neron. Just add -L${SAGE_LOCAL} -lncurses to the link flags, i.e. 

```
mabshoff`@`neron LiE$ gcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o gettype.o getvalue.o init.o learn.o main.o mem.o node.o onoff.o output.o poly.o sym.o print.o getl.o date.o static/*.o box/*.o -L /extra/home/mabshoff/SAGE-build/sage-2.8.2.rc1/local/lib/ -lreadline -lcurses
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-08-24 17:05:08

one more thing I forgot: The build requires bison, so we should just run bison on the grammar file and include the output so bison isn't invoked. For that see also ticket #472 which fixed the same "problem" for Singular

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-24 21:39:39

The ncurses/curses issue also rears its ugly head on a Centos 5/RedHat Enterprise 5 box on x86-64:

```
gcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o gettype.o getvalue.o init.o learn.o main.o mem.o node.o onoff.o output.o poly.o sym.o print.o getl.o date.o static/*.o box/*.o -lreadline
learn.o: In function `Learn':
learn.c:(.text+0x59a): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `PC'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `tgetflag'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `tgetent'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `UP'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `tputs'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `tgoto'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `tgetnum'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `BC'
/usr/lib/gcc/x86_64-redhat-linux/4.1.1/../../../../lib64/libreadline.so: undefined reference to `tgetstr'
collect2: ld returned 1 exit status
make[1]: *** [Lie.exe] Error 1
make[1]: Leaving directory `/tmp/Work2/LiE'
make: *** [all] Error 2
[mabshoff`@`m940 LiE]$ gcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o gettype.o getvalue.o init.o learn.o main.o mem.o node.o onoff.o output.o poly.o sym.o print.o getl.o date.o static/*.o box/*.o -lreadline -lncurses
learn.o: In function `Learn':
learn.c:(.text+0x59a): warning: the use of `tmpnam' is dangerous, better use `mkstemp'
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-08-24 21:50:30

And while we are at it some valgrinding can't hurt:

```
[mabshoff`@`m940 LiE]$ valgrind --tool=memcheck --leak-resolution=high ./Lie.exe < progs/maxsub
==22512== Memcheck, a memory error detector.
==22512== Copyright (C) 2002-2006, and GNU GPL'd, by Julian Seward et al.
==22512== Using LibVEX rev 1658, a library for dynamic binary translation.
==22512== Copyright (C) 2004-2006, and GNU GPL'd, by OpenWorks LLP.
==22512== Using valgrind-3.2.1, a dynamic binary instrumentation framework.
==22512== Copyright (C) 2000-2006, and GNU GPL'd, by Julian Seward et al.
==22512== For more details, rerun with: -v
==22512==
New tree space with maximum number of nodes: 50000.
     type A
==22512== Syscall param write(buf) points to uninitialised byte(s)
==22512==    at 0x31058BFA60: __write_nocancel (in /lib64/libc-2.5.so)
==22512==    by 0x31058686D2: _IO_file_write`@``@`GLIBC_2.2.5 (in /lib64/libc-2.5.so)
==22512==    by 0x31058685E5: _IO_do_write`@``@`GLIBC_2.2.5 (in /lib64/libc-2.5.so)
==22512==    by 0x310586971F: _IO_file_close_it`@``@`GLIBC_2.2.5 (in /lib64/libc-2.5.so)
==22512==    by 0x310585E249: fclose`@``@`GLIBC_2.2.5 (in /lib64/libc-2.5.so)
==22512==    by 0x40565C: Objectwrite (in /tmp/Work2/LiE/Lie.exe)
==22512==    by 0x41241E: vid_writestring_tex_grp_tex (in /tmp/Work2/LiE/Lie.exe)
==22512==    by 0x406325: eval_value (in /tmp/Work2/LiE/Lie.exe)
==22512==    by 0x41346F: arg_sequence (in /tmp/Work2/LiE/Lie.exe)
==22512==    by 0x406169: eval_value (in /tmp/Work2/LiE/Lie.exe)
==22512==    by 0x40291D: yyparse (in /tmp/Work2/LiE/Lie.exe)
==22512==    by 0x40764D: main (in /tmp/Work2/LiE/Lie.exe)
==22512==  Address 0x4C0B00F is not stack'd, malloc'd or (recently) free'd
     type B
     type C
<SNIP>
```


Generally speaking there is a varying amount of still-reachable memory at exit time:


```
==22519== LEAK SUMMARY:
==22519==    definitely lost: 0 bytes in 0 blocks.
==22519==      possibly lost: 0 bytes in 0 blocks.
==22519==    still reachable: 1,769,812 bytes in 55 blocks.
==22519==         suppressed: 0 bytes in 0 blocks.
```


This might or might not become a problem if you do a bunch of computations using the same executable instance. If somebody has an example of something big that we can run in a loop let me know.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-24 22:00:40

And just to be through: http://groups.google.com/group/sage-devel/t/bfa83514467cdfe6


---

Comment by mhansen created at 2007-08-28 00:43:28

I've created and attached an initial spkg for LiE.

I've also attached a bundle with an expect interface for LiE.  It supports tab-completion, help, etc.

I'm not sure how much more beneficial a C library interface to it would be...


---

Comment by mhansen created at 2007-08-28 00:44:25

LiE expect interface bundle


---

Attachment


---

Comment by was created at 2007-08-29 01:59:40

Resolution: fixed
