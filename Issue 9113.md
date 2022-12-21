# Issue 9113: sage-4.4.3.alpha1 -lpng blocker issue

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-02 02:21:57

Assignee: GeorgSWeber

On OS X we have:


```
running build_ext
building 'sage.rings.polynomial.pbori' extension
g++ -L/Users/was/build/sage-4.4.3.alpha1/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/rings/polynomial/pbori.o -L/Users/was/build/sage-4.4.3.alpha1/local//lib -lcsage -lpolybori -lpboriCudd -lgroebner -lgd -lpng -lm4ri -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/rings/polynomial/pbori.so
ld: library not found for -lpng
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.


real    0m1.706s
user    0m1.187s
sys     0m0.503s
make: *** [testlong] Error 1
```


This was caused by some patch to get Sage to build on Cygwin.


---

Comment by mhansen created at 2010-06-02 02:29:54

This is due to #8844.  We should replace the include of "-lpng" with a uname_specific command to use "png12" where needed.


---

Comment by was created at 2010-06-03 04:06:53

Resolution: duplicate


---

Comment by was created at 2010-06-03 04:06:53

I made a dupe of this: #9116
