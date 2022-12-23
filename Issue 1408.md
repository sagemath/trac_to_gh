# Issue 1408: optional macaulay2 spkg doesn't install on osx10.5.1 due to problems with gc

Issue created by migration from https://trac.sagemath.org/ticket/1408

Original creator: was

Original creation time: 2007-12-06 04:19:03

Assignee: was

This was reported by Matt Miller:

```


       then mv -f ".deps/darwin_stop_world.Tpo" ".deps/
darwin_stop_world.Plo"; else rm -f ".deps/darwin_stop_world.Tpo"; exit
1; fi
rm -f .libs/darwin_stop_world.lo
gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=
\"6.8\" "-DPACKAGE_STRING=\"gc 6.8\"" -DPACKAGE_BUGREPORT=
\"Hans.Boehm@hp.com\" -DGC_VERSION_MAJOR=6 -DGC_VERSION_MINOR=8 -
DPACKAGE=\"gc\" -DVERSION=\"6.8\" -DGC_DARdarwin_stop_world.c:203:
error: 'ppc_thread_state_t' has no member named 'r1'
darwin_stop_world.c:205: error: 'ppc_thread_state_t' has no member
named 'r0'
...
darwin_stop_world.c:235: error: 'ppc_thread_state_t' has no member
named 'r31'
make[1]: *** [darwin_stop_world.lo] Error 1
make: *** [install-recursive] Error 1
Error installing GC garbage collection library.

real    2m44.303s
user    0m33.283s
sys     0m37.224s
sage: An error occurred while installing macaulay2-20061014
```



---

Comment by was created at 2007-12-06 04:19:49

Note also trac #1036.


---

Comment by mabshoff created at 2007-12-06 04:56:39

And also #10.


---

Comment by mabshoff created at 2008-07-29 17:43:11

Resolution: fixed


---

Comment by mabshoff created at 2008-07-29 17:43:11

This has been fixed by the new M2.spkg from #10.

Cheers,

Michael
