# Issue 7135: python always building 32-bit on Solaris

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-06 00:48:50

Assignee: tbd

CC:  dimpase

Using

    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

looking at the directory $SAGE_HOME/local/bin, we can see that python is being built as 32-bit, despite the fact that SAGE64 was set to "yes"


```
python:         ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
python2.6:      ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
```


This is *far* from the only package building 32-bit when SAGE64 is set to "yes" on Solaris. All of the following do, and I suspect there are many others too. 

    * zlib #7128
    * libgpg_error #7129
    * libpng #7130
    * libcliquer #7131
    * pari #7133 
    * ntl #7134

mpir currently mixes 32 and 64-bit objects, so do not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform. 


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-07-08 19:32:17

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-09 08:26:26

Resolution: invalid
