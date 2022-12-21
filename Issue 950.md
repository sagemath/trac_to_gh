# Issue 950: include guava in sage (in the gap package?)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-20 21:07:44

Assignee: was

The only obstruction right now is that it doesn't build on OS X:


```

if ! grep darwin sysinfo.gap ; then ( cd bin/i686-apple-darwin8.10.1-gcc ; strip gap) ; fi
GAParch=i686-apple-darwin8.10.1-gcc
( test -d bin || mkdir bin; \
test -d bin/i686-apple-darwin8.10.1-gcc || mkdir bin/i686-apple-darwin8.10.1-gcc; cd bin/i686-apple-darwin8.10.1-gcc; \
make -f ../../Makefile all2 CC="gcc" CFLAGS="-O2"; \
        cp wtdist ../wtdist; cp desauto ../desauto )
gcc -c -O2 -o leonconv.o -c ../../src/leonconv.c
../../src/leonconv.c:2:20: error: malloc.h: No such file or directory
../../src/leonconv.c: In function 'main':
../../src/leonconv.c:17: warning: incompatible implicit declaration of built-in function 'exit'
../../src/leonconv.c:28: warning: incompatible implicit declaration of built-in function 'exit'
../../src/leonconv.c: In function 'EquivalentToGuave':
../../src/leonconv.c:121: warning: incompatible implicit declaration of built-in function 'exit'
make[1]: *** [leonconv.o] Error 1
cp: wtdist: No such file or directory
cp: desauto: No such file or directory
make: *** [all] Error 1

real    2m23.081s
```



---

Comment by mabshoff created at 2007-12-04 14:22:11

Hmm. What is the current status of this?

Cheers,

Michael


---

Comment by rlm created at 2007-12-11 17:13:20

Related to #1452


---

Comment by rlm created at 2007-12-19 06:08:22

Resolution: fixed
