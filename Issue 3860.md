# Issue 3860: itanium -- can't build mercurial extension

Issue created by migration from https://trac.sagemath.org/ticket/3860

Original creator: was

Original creation time: 2008-08-14 22:16:42

Assignee: mabshoff


```
building 'mercurial.osutil' extension
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/home/wstein/iras/build/sage-3.1.alpha2/local/include/python2.5 -c mercurial/osutil.c -o build/temp.linux-ia64-2.5/mercurial/osutil.o
gcc -pthread -shared build/temp.linux-ia64-2.5/mercurial/osutil.o -o build/lib.linux-ia64-2.5/mercurial/osutil.so
building 'hgext.inotify.linux._inotify' extension
creating build/temp.linux-ia64-2.5/hgext
creating build/temp.linux-ia64-2.5/hgext/inotify
creating build/temp.linux-ia64-2.5/hgext/inotify/linux
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/home/wstein/iras/build/sage-3.1.alpha2/loc
al/include/python2.5 -c hgext/inotify/linux/_inotify.c -o build/temp.linux-ia64-2.5/hgext/inotify/linux/_inotify.o
hgext/inotify/linux/_inotify.c:172: error: ‘IN_ONLYDIR’ undeclared here (not in a function)
hgext/inotify/linux/_inotify.c:173: error: ‘IN_DONT_FOLLOW’ undeclared here (not in a function)
hgext/inotify/linux/_inotify.c:174: error: ‘IN_MASK_ADD’ undeclared here (not in a function)
hgext/inotify/linux/_inotify.c: In function ‘define_consts’:
hgext/inotify/linux/_inotify.c:266: warning: passing argument 3 of ‘define_const’ makes integer from pointer without a
 cast
hgext/inotify/linux/_inotify.c:267: warning: passing argument 3 of ‘define_const’ makes integer from pointer without a
 cast
hgext/inotify/linux/_inotify.c:268: warning: passing argument 3 of ‘define_const’ makes integer from pointer without a
 cast
error: command 'gcc' failed with exit status 1
Error building mercurial

real    0m3.062s
user    0m2.308s
sys     0m0.280s
sage: An error occurred while installing mercurial-1.01.p0
```



---

Comment by was created at 2008-08-14 22:18:57

This is on IRAS.  It builds fine on Cleo.


---

Comment by mabshoff created at 2008-08-15 10:58:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-15 10:58:22

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1/rc0/mercurial-1.01.p1.spkg

fixes the issue by disabling the inotify extension which is broken on SLES 10 Itanium for some reason.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 11:04:48

Merged in Sage 3.1.rc0


---

Comment by mabshoff created at 2008-08-15 11:04:48

Resolution: fixed
