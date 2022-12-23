# Issue 7129: libgpg_error-1.6.p2 always builds 32-bit binaries on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/7129

Original creator: drkirkby

Original creation time: 2009-10-05 23:07:56

Assignee: tbd

CC:  david.kirkby@onetel.ne

A look in $SAGE_HOME/local/lib shows this is being built 32-bit, even when SAGE64 is set to yes. Note how the libraries of libhisotry below are 64-bit (as they should be), but libgpg's are 32-bit. 

zlib is another package to suffer this problem - see #7128

libgcrypt fails to build in 64-bit on Solaris SPARC with gcc (see #7127). This might actually be related and a fault of this package, rather than of libgcrypt, though there is another Solaris issue on that package. 


```
libgpg-error.la:        commands text
libgpg-error.so:        ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libgpg-error.so.0:      ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libgpg-error.so.0.4.0:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libhistory.a:   current ar archive, not a dynamic executable or shared object
libhistory.so:  ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libhistory.so.6:        ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
```


I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64. 

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX. 

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64. 

The sensible way to resolve this is to add the correct flag on every platform. 


---

Comment by drkirkby created at 2009-10-05 23:27:01

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2011-04-02 13:20:40

This can be closed as fixed by #8066 in sage-4.3.3.alpha0 

Dave


---

Comment by jdemeyer created at 2011-04-05 15:50:42

Resolution: duplicate
