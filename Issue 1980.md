# Issue 1980: flint fails to build with -fstack-protector

Issue created by migration from https://trac.sagemath.org/ticket/1980

Original creator: malb

Original creation time: 2008-01-30 10:31:07

Assignee: mabshoff

Error message:


```
.o mpz_poly.o ZmodF_poly.o long_extras.o -L/home/malb/sage-2.10.1.rc2-stack-protector/local/lib/  -
lgmp -lpthread -lm
/home/malb/sage-2.10.1.rc2-stack-protector/local/lib//libgmp.so: undefined reference to `__stack_chk_guard'
/home/malb/sage-2.10.1.rc2-stack-protector/local/lib//libgmp.so: undefined reference to `__stack_chk_fail'
collect2: ld returned 1 exit status
make[2]: *** [mpn_extras-test] Error 1
make[2]: Leaving directory `/home/malb/sage-2.10.1.rc2-stack-protector/spkg/build/flint-1.06/src'
./spkg-check: line 46: ./mpn_extras-test: No such file or directory
./spkg-check: line 47: ./ZmodF-test: No such file or directory
...
```


See http://lists.debian.org/debian-devel-announce/2008/01/msg00006.html and http://wiki.debian.org/Hardening for rationale of `-fstack-protector`.



---

Comment by mabshoff created at 2008-01-30 10:34:24

Did the `-fstack-protector` get passed on to gmp? How do you pass `CFLAGS` and so on to all the other packages? 

Cheers,

Michael


---

Comment by malb created at 2008-01-30 10:37:36

Sorry for being ambiguous. To reproduce:


```
export CFLAGS="-fstack-protector"
export CXXLAGS="-fstack-protector"
cd <SAGE_ROOT>
make
```


This requires GCC 4.1 and up.


---

Comment by malb created at 2008-01-30 10:38:12

erm, it is supposed to be `CXXFLAGS`.


---

Comment by aapitzsch created at 2014-08-18 18:30:17

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-08-18 18:30:17

Works for me.


---

Comment by vbraun created at 2014-10-25 21:43:59

Resolution: fixed
