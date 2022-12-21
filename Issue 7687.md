# Issue 7687: Remove leonconv binary from gap spkg (guava pkg).

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-15 19:24:16

Assignee: tbd

We ship a Linux *binary* `leonconv` with every copy of Sage.  This is bad and a potential security issue.  Delete this.  


```
wstein`@`sage:~/build/sage-4.3.rc0/spkg/standard/gap-4.4.10.p12/src/pkg/guava3.4/src$ ls -lh
total 36K
drwxr-xr-x 2 wstein wstein 4.0K 2008-03-31 03:55 ctjhai
-rw-r--r-- 1 wstein wstein  147 2008-03-17 14:40 defs.h
drwxr-xr-x 4 wstein wstein 4.0K 2008-03-31 03:55 leon
-rwxr-xr-x 1 wstein wstein  15K 2008-03-17 14:40 leonconv
-rw-r--r-- 1 wstein wstein 4.0K 2008-03-17 14:40 leonconv.c
-rwxr-xr-x 1 wstein wstein  262 2008-03-17 14:44 Makefile
wstein`@`sage:~/build/sage-4.3.rc0/spkg/standard/gap-4.4.10.p12/src/pkg/guava3.4/src$ ./leonconv
Error, usage: leonconv <switch> <inputfile> <outputfile>
```



---

Comment by wdj created at 2009-12-15 20:24:47

Since guava was supposed to be removed a long time ago (http://trac.sagemath.org/sage_trac/ticket/5701), I don't see why this trac ticket is necessary.


---

Comment by aapitzsch created at 2014-06-22 14:10:27

`leonconv` is not shipped anymore.


---

Comment by aapitzsch created at 2014-06-22 14:10:27

Changing status from new to needs_review.


---

Comment by vbraun created at 2014-10-25 21:44:39

Resolution: fixed
