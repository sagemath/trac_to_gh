# Issue 5322: Sage 3.3.rc2: mandriva 32/64 bit fails with mysterious error 139 in make

Issue created by migration from https://trac.sagemath.org/ticket/5322

Original creator: mabshoff

Original creation time: 2009-02-20 13:20:39

Assignee: mabshoff

This might be relevant, but seems to be rather old:

  http://mail.python.org/pipermail/python-list/2003-February/190047.html


This is the tail of the log:

```
gcc -pthread -fPIC -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I. -I/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/./Include -I. -IInclude -I./Include -I/space/wstein/farm/sage-3.3.rc2/local/include -I/usr/local/include -I/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Include -I/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src -c /space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.c -o build/temp.linux-i686-2.5/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.o
In file included from /space/wstein/farm/sage-3.3.rc2/local/include/readline/readline.h:37,
                 from /space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.c:31:
/space/wstein/farm/sage-3.3.rc2/local/include/readline/rltypedefs.h:35: warning: function declaration isn’t a prototype
/space/wstein/farm/sage-3.3.rc2/local/include/readline/rltypedefs.h:36: warning: function declaration isn’t a prototype
/space/wstein/farm/sage-3.3.rc2/local/include/readline/rltypedefs.h:37: warning: function declaration isn’t a prototype
/space/wstein/farm/sage-3.3.rc2/local/include/readline/rltypedefs.h:38: warning: function declaration isn’t a prototype
In file included from /space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.c:31:
/space/wstein/farm/sage-3.3.rc2/local/include/readline/readline.h:378: warning: function declaration isn’t a prototype
/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.c: In function ‘flex_complete’:
/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.c:681: warning: implicit declaration of function ‘completion_matches’
/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.c:681: warning: return makes pointer from integer without a cast
gcc -pthread -shared -L/space/wstein/farm/sage-3.3.rc2/local/lib -I. -IInclude -I./Include -I/space/wstein/farm/sage-3.3.rc2/local/include build/temp.linux-i686-2.5/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src/Modules/readline.o -L/usr/lib/termcap -L/space/wstein/farm/sage-3.3.rc2/local/lib -L/usr/local/lib -lreadline -ltermcap -o build/lib.linux-i686-2.5/readline.so
/bin/sh: line 1: 16345 Segmentation fault      CC='gcc -pthread' LDSHARED='gcc -pthread -shared' OPT='-DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes' ./python -E ./setup.py build
make[2]: *** [sharedmods] Error 139
make[2]: Leaving directory `/space/wstein/farm/sage-3.3.rc2/spkg/build/python-2.5.2.p8/src'
Error building Python.
```



---

Comment by mabshoff created at 2009-03-01 02:22:22

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by jdemeyer created at 2013-04-11 16:19:37

Closing since this refers to a very old version.


---

Comment by jdemeyer created at 2013-04-11 16:19:37

Resolution: invalid
