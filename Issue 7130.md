# Issue 7130: libpng 1.2.35 always builds 32-bit libraries on Solaris.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-05 23:21:28

Assignee: tbd

CC:  jsp

Using
 * A Sun Blade 2000 running Solaris 10 update 7
 * Sage 4.1.2.rc0
 * gcc 4.4.1
 * SAGE64 exported to "yes"

We can see that libpng is building 32-bit libraries, despite other packages are building 64-bit libraries. 


```
libpng12.so:    ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libpng12.so.0:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libpng12.so.0.35.0:     ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libreadline.a:  current ar archive, not a dynamic executable or shared object
libreadline.so: ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libreadline.so.6:       ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
```


Other packages building 32-bit libraries, even when SAGE64 is set to  yes include, but are probably not limited to. 
 * zlib #7128
 * libgpg_error #7129

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform. 


---

Comment by drkirkby created at 2009-10-05 23:28:01

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2010-01-02 21:38:19

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-02 21:38:19

This is a quick hack, to get this to build only with only gcc and perhaps Sun Studio, as they both take -m64. A more portable solution, which will work for any compiler will be implemented later. 

http://boxen.math.washington.edu/home/kirkby/portability/libpng-1.2.35.p0/

dave


---

Attachment


---

Comment by drkirkby created at 2010-06-19 13:17:43

This can be closed. The latest version of libpng (libpng-1.2.35.p2) in Sage builds fine without problems. I don't know what ticket number fixed it, but these two log entries 



```
changeset:   13:ae01944f408c
user:        Jaap Spies <jaapspies`@`gmail.com>
date:        Thu Feb 04 19:32:51 2010 +0100
summary:     Corrected stupid typo I thought I had corrected earlier.

changeset:   12:329a8eb6dd2e
user:        Jaap Spies <jaapspies`@`gmail.com>
date:        Wed Feb 03 19:09:41 2010 +0100
summary:     Let SAGE64=yes work not only on OSX, but also on Open Solaris and possibly on other platform
```


As such, this can be closed as "fixed"


---

Comment by drkirkby created at 2010-06-19 13:17:43

Resolution: fixed
