# Issue 3821: bernmm shouldn't depend on pyport.h

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-08-12 16:27:35

Assignee: mabshoff

I'd rather not have bernmm dependent on pyport.h.

Patch will be up momentarily; should be applied on top of #3807 patch; I've only tested this on my laptop.



---

Attachment


---

Comment by mabshoff created at 2008-08-12 16:38:23

The patch seems to go in the right direction, but gcc 4.3.1 is still unhappy with bern_modp_util.cpp while two other files are fine:

```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DUSE_THREADS=1 -I/tmp/foo/sage-3.1.alpha1/local//include -I/tmp/foo/sage-3.1.alpha1/local//include/csage -I/tmp/foo/sage-3.1.alpha1/devel//sage/sage/ext -I/tmp/foo/sage-3.1.alpha1/local/include/python2.5 -c sage/rings/bernmm/bern_modp_util.cpp -o build/temp.linux-x86_64-2.5/sage/rings/bernmm/bern_modp_util.o -w -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
In file included from sage/rings/bernmm/bern_modp_util.cpp:24:
sage/rings/bernmm/bern_modp_util.h:32:2: error: #error Oops! Unsigned long is neither 32 nor 64 bits.
sage/rings/bernmm/bern_modp_util.h:33:2: error: #error You need to update bern_modp_util.h.
In file included from sage/rings/bernmm/bern_modp_util.cpp:24:
sage/rings/bernmm/bern_modp_util.h: In member function ‘bool bernmm::PrimeTable::get(long int) const’:
sage/rings/bernmm/bern_modp_util.h:91: error: ‘ULONG_BITS’ was not declared in this scope
sage/rings/bernmm/bern_modp_util.h: In member function ‘void bernmm::PrimeTable::set(long int)’:
sage/rings/bernmm/bern_modp_util.h:97: error: ‘ULONG_BITS’ was not declared in this scope
sage/rings/bernmm/bern_modp_util.cpp: In constructor ‘bernmm::PrimeTable::PrimeTable(long int)’:
sage/rings/bernmm/bern_modp_util.cpp:92: error: ‘ULONG_BITS’ was not declared in this scope
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```


I am looking into this.


---

Comment by mabshoff created at 2008-08-12 16:41:18

Moving the climits include before the macro

```
#if ULONG_MAX == 4294967295U
#define ULONG_BITS 32
#elif ULONG_MAX == 18446744073709551615U
#define ULONG_BITS 64
#else
#error Oops! Unsigned long is neither 32 nor 64 bits.
#error You need to update bern_modp_util.h.
#endif
```

in devel/sage/sage/rings/bernmm/bern_modp_util.h fixes the issue for me. Now doctesting the install.

Cheers,

Michael


---

Comment by dmharvey created at 2008-08-12 17:16:38

Arggh, I'm sorry, I'm an idiot. Of course the #include needs to go before the macro.


---

Comment by mabshoff created at 2008-08-12 17:21:44

Hi David,

Replying to [comment:4 dmharvey]:
> Arggh, I'm sorry, I'm an idiot. Of course the #include needs to go before the macro.

:) - I do the same thing on a pretty regular basis. Do you want to update the patch or should I post a follow up patch?

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-08-12 21:32:03

Positive review. Thanks David for the quick fix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-12 21:38:10

Resolution: fixed


---

Comment by mabshoff created at 2008-08-12 21:38:10

Merged both patches in Sage 3.1.alpha2
