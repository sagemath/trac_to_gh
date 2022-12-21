# Issue 7175: HP-UX failure to build of pyprocessing 0.52.p0

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-10 08:22:33

Assignee: tbd

Keywords: HP-UX

See errors below, from an HP C3600 workstation running HP-UX 11i.

A developer can be given access to this machine. 

```
processing/doc
copying doc/intro.html -> build/lib.hp-ux-B.11.11-9000-785-2.6/processing/doc
copying doc/CHANGES.html -> build/lib.hp-ux-B.11.11-9000-785-2.6/processing/doc
copying doc/html4css1.css -> build/lib.hp-ux-B.11.11-9000-785-2.6/processing/doc
copying doc/../index.html -> build/lib.hp-ux-B.11.11-9000-785-2.6/processing/doc/..
running build_ext
building 'processing._processing' extension
creating build/temp.hp-ux-B.11.11-9000-785-2.6
creating build/temp.hp-ux-B.11.11-9000-785-2.6/src
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_SEM_OPEN=1 -DHAVE_FD_TRANSFER=1 -DHAVE_SEM_TIMEDWAIT=1 -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -c src/processing.c -o build/temp.hp-ux-B.11.11-9000-785-2.6/src/processing.o
src/processing.c: In function 'processing_sendfd':
src/processing.c:158: warning: implicit declaration of function 'CMSG_SPACE'
src/processing.c:175: warning: implicit declaration of function 'CMSG_LEN'
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_SEM_OPEN=1 -DHAVE_FD_TRANSFER=1 -DHAVE_SEM_TIMEDWAIT=1 -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -c src/socket_connection.c -o build/temp.hp-ux-B.11.11-9000-785-2.6/src/socket_connection.o
In file included from src/socket_connection.c:200:
src/connection.h: In function 'Connection_new':
src/connection.h:31: warning: format '%d' expects type 'int', but argument 3 has type 'long int'
src/connection.h: In function 'Connection_repr':
src/connection.h:311: warning: format '%d' expects type 'int', but argument 3 has type 'long int'
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_SEM_OPEN=1 -DHAVE_FD_TRANSFER=1 -DHAVE_SEM_TIMEDWAIT=1 -I/home/drkirkby/sage-4.1.2.rc0/local/include/python2.6 -c src/semaphore.c -o build/temp.hp-ux-B.11.11-9000-785-2.6/src/semaphore.o
src/semaphore.c: In function 'SemLock_acquire':
src/semaphore.c:296: warning: implicit declaration of function 'sem_timedwait'
src/semaphore.c: In function 'SemLock_new':
src/semaphore.c:402: error: 'SEM_FAILED' undeclared (first use in this function)
src/semaphore.c:402: error: (Each undeclared identifier is reported only once
src/semaphore.c:402: error: for each function it appears in.)
src/semaphore.c: In function 'SemLock_dealloc':
src/semaphore.c:462: error: 'SEM_FAILED' undeclared (first use in this function)
error: command 'gcc' failed with exit status 1

real    0m2.771s
user    0m2.290s
sys     0m0.220s
sage: An error occurred while installing pyprocessing-0.52.p0
```



---

Comment by drkirkby created at 2010-08-09 21:05:45

Resolution: fixed


---

Comment by drkirkby created at 2010-08-09 21:05:45

This was resolved 5 months ago in sage 4.3.4 by #6503, which removed pyprocessing from Sage.
