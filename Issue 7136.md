# Issue 7136: gp always building 32-bit on Solaris

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-06 00:53:01

Assignee: tbd

CC:  dimpase

Using

    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

Looking at the directory $SAGE_HOME/local/bin, we can see that _pg_ is being built as 32-bit binary, despite the fact that SAGE64 was set to "yes"

```
drkirkby`@`swan:[~/sage/gcc64-sage-4.1.2.rc0/local/bin] $ file gp
gp:             ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped, no debugging information available
```


This is *far* from the only package building 32-bit when SAGE64 is set to "yes" on Solaris. All of the following do, and I suspect there are many others too.

    * zlib #7128
    * libgpg_error #7129
    * libpng #7130
    * libcliquer #7131
    * pari #7133
    * ntl #7134 
    * python #7135
    

mpir currently mixes 32 and 64-bit objects, so do not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform.



---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mjo created at 2020-07-12 19:59:54

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2020-07-12 19:59:54

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
