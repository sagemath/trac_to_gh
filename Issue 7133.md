# Issue 7133: pari-2.3.3 always builds 32-bit libraries on Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/7133

Original creator: drkirkby

Original creation time: 2009-10-06 00:28:10

Assignee: tbd

Using

    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

We can see that _pari_ is building 32-bit libraries, despite the fact SAGE64 was set to "yes"



```
drkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/lib] $ file *pari*
libpari-gmp.so.2:       ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped, no debugging information available
libpari-gmp.so.2.3.3:   ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped, no debugging information available
libpari.a:      current ar archive, not a dynamic executable or shared object
libpari.so:     ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped, no debugging information available
```



Other packages building 32-bit libraries, even when SAGE64 is set to "yes" include, but are probably not limited to:

    * zlib #7128
    * libgpg_error #7129
    * libpng #7130 
    * libcliquer #7131

mpir currently mixes 32 and 64-bit objects, so do not build at all #7132. 

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform. 



---

Comment by drkirkby created at 2010-06-17 07:36:16

This is fixed by #8099


---

Comment by drkirkby created at 2010-06-17 07:36:16

Resolution: fixed
