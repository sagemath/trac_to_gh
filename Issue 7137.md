# Issue 7137: always building 32-bit on Solaris even when SAGE64="yes"

Issue created by migration from https://trac.sagemath.org/ticket/7137

Original creator: drkirkby

Original creation time: 2009-10-06 01:01:17

Assignee: tbd

Using

    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

Looking at the directory $SAGE_HOME/local/bin, we can see that _ratpoint_ is being built as 32-bit binary, despite the fact that SAGE64 was set to "yes"

```
drkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/bin] $ file ratpoint
ratpoint:       ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, stripped
```


This is *far* from the only package building 32-bit when SAGE64 is set to "yes" on Solaris. All of the following do, and I suspect there are many others too.

    * zlib #7128
    * libgpg_error #7129
    * libpng #7130
    * libcliquer #7131
    * pari #7133
    * ntl #7134 
    * python #7135
    * gp #7136
    
mpir currently mixes 32 and 64-bit objects, so does not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform.



---

Comment by drkirkby created at 2010-08-20 15:27:01

This was fixed for OpenSolaris #8351. The fix also works for Solaris 10, so this can be closed. 

Dave


---

Comment by drkirkby created at 2010-08-20 15:27:01

Resolution: fixed
