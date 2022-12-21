# Issue 4187: Fix compilation problem for libfplll.spkg on Solaris 10

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-24 08:48:38

Assignee: mabshoff

In Sage 3.1.3.alpha0 fplll.pyx blows up spectacularly on Solaris 10:

```
building 'sage.libs.fplll.fplll' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local/include/fplll -I/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include -I/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/csage -I/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/devel//sage/sage/ext -I/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local/include/python2.5 -c sage/libs/fplll/fplll.cpp -o build/temp.solaris-2.10-i86pc-2.5/sage/libs/fplll/fplll.o -w -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/vec_RR.h:5,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/vec_vec_RR.h:5,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/mat_RR.h:6,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/LLL.h:5,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/csage/ntl_wrap.h:20,
                 from sage/libs/fplll/fplll.cpp:123:
/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/RR.h:226:30: error: macro "round" passed 2 arguments, but takes just 1
/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/RR.h:228:22: error: macro "round" passed 2 arguments, but takes just 1
In file included from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/vec_RR.h:5,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/vec_vec_RR.h:5,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/mat_RR.h:6,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/LLL.h:5,
                 from /home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/csage/ntl_wrap.h:20,
                 from sage/libs/fplll/fplll.cpp:123:
/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/RR.h:226: error: variable or field ‘round’ declared void
/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/RR.h:227: error: expected `)' before ‘(’ token
/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/local//include/NTL/RR.h:227: error: expected `)' before ‘(’ token
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```

Ironically this exposed a bug in a workaround in libfplll that made it compile on Solaris which I put there a while ago. It does end up fixing the doctest failures in various places due to LLL being wrong that were caused by the workaround, so this was one lucky coincidence. The spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.3/alpha1/libfplll-2.1.6-20071129.p5.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 08:48:55

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-24 09:34:43

+1


---

Comment by mabshoff created at 2008-09-24 10:05:25

Resolution: fixed


---

Comment by mabshoff created at 2008-09-24 10:05:25

Merged in Sage 3.1.3.alpha1
