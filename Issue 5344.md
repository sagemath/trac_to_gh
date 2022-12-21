# Issue 5344: [with patch, needs review] Singular/omalloc "double free" problem

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2009-02-22 22:02:49

Assignee: mabshoff

CC:  robertwb

Singular/omalloc relies on and incorporates as "default malloc" a certain adapted version of dlmalloc version 2.6.5 from 1998.

Let's explicitly choose this very dlmalloc code to be an "external malloc" for Singular/omalloc, by taking the current "singular-3-0-4-4-20080711.p3.spkg" and adding to its spkg-install in its "config()" subscript the three lines:

```
                --with-malloc=external \
                --with-external-malloc-h=dlmalloc.h \
                --with-external-malloc-c=dlmalloc.c \
```

Compiling and installing the thus adapted spkg results in a omalloc library which is almost identical (up to possibly some redefinition
of "strdup").

This is due to the fact that the omalloc "configure" run produces essentially the same output, with only one exception: it now chooses to define the macro "OMALLOC_USES_MALLOC", which by default is not the case. "Inside" omalloc, the differences are marginal.

But in the Singular code itself, there are three files where code depends on the presence of this macro "OMALLOC_USES_MALLOC". This leads to differences, although the underlying omalloc binaries are virtually the same (the "strdup" issue hardly interferes).

Now from the Sage point of view, the difference is more than annoying, since on a Mac OS X system suddenly:

```
sage: EllipticCurve(GF(17),[0,1,1,10,13])
Elliptic Curve defined by y^2 + y = x^3 + x^2 + 10*x + 13 over Finite Field of size 17
sage: exit
Exiting SAGE (CPU time 0m0.14s, Wall time 0m34.71s).
sage.bin(20597) malloc: ***  Deallocation of a pointer not malloced: 0x7e75018; This could be a double free(), or free() called with the middle of an allocated block; Try setting environment variable MallocHelp to see tools to help debug
sage.bin(20597) malloc: ***  Deallocation of a pointer not malloced: 0x7e75020; This could be a double free(), or free() called with the middle of an allocated block; Try setting environment variable MallocHelp to see tools to help debug
sage.bin(20597) malloc: ***  Deallocation of a pointer not malloced: 0x7e73078; This could be a double free(), or free() called with the middle of an allocated block; Try setting environment variable MallocHelp to see tools to help debug
sage.bin(20597) malloc: ***  Deallocation of a pointer not malloced: 0x7e73068; This could be a double free(), or free() called with the middle of an allocated block; Try setting environment variable MallocHelp to see tools to help debug
```

we run into a "double free" problem at exiting sage, whenever code is called that relies somehow on Singular.

Since the macro "OMALLOC_USES_MALLOC" is essentially the only thing that changed, and there are only less than a handful places in the Singular code where it is evaluated, a search by hand and trial-and-error resulted in the files "kernel/mminit.cc" resp.
"kernel/mmstd.c" being the culprits.

Now the omalloc submodule could be patched ("configure" and "configure.in") so that the macro "OMALLOC_USES_MALLOC" is not set at all. But from the test case at hand is to be deduced that the "OMALLOC_USES_MALLOC" code branch in "kernel/mminit.cc" as such is not trustworthy, so patching the omalloc submodule would only cover the bug, far away from its source.

Looking at the code in "kernel/mminit.cc", why the heck suddenly these "double frees" should occur?

Maybe it's trivially somewhere the "wrong" free() being called (instead of the one implicitly set by "mp_set_memory_functions()")?

Looking at the file "kernel/mmstd.c", especially given that exactly for "ix86_Win", "ppcMac_darwin", and "ix86Mac_darwin" (see lines 13 - 20) the function freeSize() is defined using unconditionally the
"system" free(), there is quite some plausibility for this.

(Could somebody upstream that question to the Singular dev team?)

Anyway, for now, one cannot trust any further that alternate code path, which in "default" Singular is the one *not* being compiled in.



---

Comment by GeorgSWeber created at 2009-02-22 22:03:37

apply to singular spkg (tested with Sage 3.3)


---

Attachment

Georg,

this is a know problem when using the system malloc with Singular, i.e. the above problem happens also on OSX in 64 bit mode where we already build Singular with the system malloc per default. There are more problems than four double frees at exit. The problem is that

 * the destructor for Rational in Givaro is not called, but the one in Singular
 * the same applies to some mpf_* function
 * What is even worst is that Sage's minpoly is not called, but instead libsingular's without the ring check

Due to the above about 25 doctests will segafault, so this is more than a cosmetic issue. I am clueless why this happens, but I suspect a scope issue in Cython.

RobertWB: thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 22:24:47

This is definitely needs work and is not a blocker against 3.4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 22:24:47

Changing priority from blocker to critical.


---

Comment by mabshoff created at 2009-02-22 23:13:28

Wait, maybe I was too hasty, so let me put this back to needs review and test some of the code I have around.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-23 07:29:09

Unfortunately while this patch does indeed fix two of the three problems the minpoly issue mentioned above does still occur. Switching back to mmap makes that problem go away, so this is "needs work" until that issue is resolved. Obviously switching back to mmap makes the "666 rings make Sage fail with out of memory conditions on OSX 32 bit" reappear.  

Note that it is likely a scope issues with Cython and unrelated to memory management issues with libSingular, but it is a show stopper for this patch until that problem is resolved

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-02-23 07:59:37

OK, I try tp rephrase it:

There is a hidden Singular related bug "four double frees". Currently it occurs only for OS X 64Bit and is brought to light by using "--with-malloc=system", as in the patch attached to #4181. It is also possible to make it appear by switching to "--with-malloc=external" and then using the original dlmalloc, as explained above in the original description.

But:


The patch attached to this ticket does *not* touch the build of omalloc (or the underlying mem allocator) at all! (There is no "--with-malloc whatsoever" in it).


Instead, the patch to this ticket attempts to fix an issue in the Singular kernel. From both reading the code and from my tests it is obvious that the Singular kernel at a certain place screws up its memory management (see the end of the description above), mixing two different "free()" implementations.

And I'm unsure what exactly you mean by "switching back and forth from/to mmap" --- could please be more verbose on that?


---

Comment by GeorgSWeber created at 2009-02-23 08:12:37

Michael,

I *am* willing to hunt this bug down to its end, and by now, I know how I could e.g. replace the old dlmalloc v2.6.5 in omalloc "seamlessly" by any of the newer versions, or even by a version especially adapted (to use both sbrk()/mmap() or only one of these on certaim platforms, or whatever).

But I am bit at a loss by what you mean by "switching back to mmap makes the appeared minpoly issue go away".

1. Under which circumstances does this "minpoly issue" occur? Please give me a kind of recipe.

2. Under which circumstances, in contrast, does the "minpoly issue" go away? Again, please give me a list of what to be done/seen.

Hopefully this (steps 1 and 2) could be done on a Mac OS X 10.4.11 box (either Intel or PPC), or else I will have to work remotely.

Thank you!

Cheers, gsw


---

Comment by mabshoff created at 2009-02-23 09:32:22

Hi Georg,

I commented on list in the thread at 

 http://groups.google.com/group/sage-devel/browse_thread/thread/d0690523a4bdab3e

to get more eyeballs in the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-23 22:48:51

Positive review. Build on OSX 32 bit, OSX 64 bit, FC 10 and also sage.math. I did valgrind the *entire* test suite on sage.math.

George's patch is integrated into

http://sage.math.washington.edu/home/mabshoff/SPKG/singular-3-0-4-4-20080711.p4.spkg

Excellent work!

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:36:36

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:36:36

Resolution: fixed
