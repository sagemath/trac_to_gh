# Issue 595: get lie to build on all standard machines -- specific problems

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-05 18:01:06

Assignee: was

Here is a problem reported on sage-support by David DeGeorge:


```
Dear Developers
I am running Suse 10.1  and
sage-2.8.3-32bit-linux-suse10-i686-Linux
I can't get lie to build. It complains about not finding -lcurses.
libcurses.a is
not in a standard place (it is in /usr/lib/curses), I tried adding a
symbolic link to
/usr/lib but then the build failed in readline.
1. Here is the part where -lcurses was the problem
gcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o
gettype.o getvalue.o init.o learn.o main.o mem.o node.o onoff.o output.o
poly.o sym.o print.o getl.o date.o static/*.o box/*.o -lreadline -lcurses
/usr/lib/gcc/i586-suse-linux/4.1.0/../../../../i586-suse-linux/bin/ld:
cannot find -lcurses
2. Here is a part of what happened after I added a link in /usr/lib to
/usr/lib/curses/libcurses.a

gcc  -o Lie.exe lexer.o parser.o non-ANSI.o bigint.o binmat.o creatop.o
gettype.o getval
ue.o init.o learn.o main.o mem.o node.o onoff.o output.o poly.o sym.o
print.o getl.o dat
e.o static/*.o box/*.o -lreadline -lcurses
learn.o: In function `Learn':
learn.c:(.text+0x542): warning: the use of `tmpnam' is dangerous, better
use `mkstemp'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetnum'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgoto'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetflag'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tputs'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetent'
/usr/local/sage-2.8.3-32bit-linux-suse10-i686-Linux/local/lib/libreadline.so:
undefined
reference to `tgetstr'
```



---

Comment by was created at 2007-09-05 18:01:15

Changing component from algebraic geometry to packages.


---

Comment by mabshoff created at 2007-09-05 18:06:41

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-09-06 21:44:50

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-07 00:38:47

There is a new lie.spkg at 

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/sage/lie-2.2.2.p3.spkg

Cheers,

Michael


---

Comment by was created at 2007-09-07 00:54:39

Resolution: fixed


---

Comment by was created at 2007-09-07 00:54:39

posted, hence done.


---

Comment by was created at 2007-09-07 00:56:33

Changing status from closed to reopened.


---

Comment by was created at 2007-09-07 00:56:33

Resolution changed from fixed to 


---

Comment by was created at 2007-09-07 01:00:19

Resolution: fixed
