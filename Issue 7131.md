# Issue 7131: libcliquer always builds 32-bit libraries on Solaris.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-05 23:38:20

Assignee: tbd

Using

    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

We can see that libcliquer is building 32-bit libraries, despite other packages are building 64-bit libraries. 

libcliquer.so:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libhistory.so:  ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libhistory.so.6:        ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped

Other packages building 32-bit libraries, even when SAGE64 is set to "yes" include, but are probably not limited to:

 * zlib #7128
 * libgpg_error #7129 
 * libpng #7130

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform.


---

Comment by drkirkby created at 2010-06-17 07:48:43

Resolution: fixed


---

Comment by drkirkby created at 2010-06-17 07:48:43

At some point this must have been fixed:


```
drkirkby`@`hawk:~/sage-4.4.4.alpha0$ find . -name 'libcl*'
./local/lib/libcliquer.so
drkirkby`@`hawk:~/sage-4.4.4.alpha0$ file ./local/lib/libcliquer.so
./local/lib/libcliquer.so:      ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```

