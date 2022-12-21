# Issue 3787: make ATLAS use extended cpuid

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-07 03:02:05

Assignee: mabshoff

CC:  cwitty cremona


```
[7:14pm] cwitty: 1) My spiffy new Xeon-branded core 2 quad computer is
very slow at compiling ATLAS.
[7:14pm] mabshoff: mhhh, how long?
[7:15pm] cwitty: I think ATLAS doesn't support the extended cpuid.
[7:15pm] cwitty: About 2 hours.
[7:15pm] mabshoff: On an Itanium 2 with loads of memory it takes about
3 hours with loads of cache.
[7:15pm] mabshoff: Can you check the ARCH in the makefile?
[7:16pm] cwitty: PIII64SSE3
[7:17pm] mabshoff: Ok, then it is identified. We might not have tuning
info.
[7:18pm] mabshoff: Let me check in a little while, but the compile
time depends on the L2 size.
[7:18pm] cwitty: Umm... Pentium 3?  I'm pretty sure it's not a pentium
3.
[7:18pm] mabshoff: Oops
[7:18pm] mabshoff: Yeah, you are right.
[7:18pm] mabshoff: ATLAS uses cpuid, not extended cpuid.
[7:18pm] mabshoff: I am not sure if 3.8.2 fixes that, but I can patch
it in case it does not.
```



---

Comment by mabshoff created at 2008-08-07 03:02:10

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-08 19:11:16

Clint just told me in an offlist email that he is tracking the problem at

 http://math-atlas.sourceforge.net/errata.html#cpuid

That and another issue will be fixed in ATLAS 3.9.2 out this weekend.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-08 20:05:28

And I figure it is better to quote the solution since the errata page tends to get updated quite a bit:

ATLAS configure mis-identifies your new system as an older system (eg., Core2-Xeon detected as PIII)
In the original x86 ISA, when using CPUID to detect family and model, we were advised to only add in the extended bits for certain base bits. Intel and AMD now say to always add them in, and have reused the base bits for newer architectures. This means that 3.8.x (which uses the original CPUID instructions) will sometimes detect a modern machine as some older machine (for instance my Xeon E5420 was detected as a Pentium III). To fix this, simply comment out lines 95 and 99 of ATLAS/src/backend/archinfo_x86.c. So, change line 95 from:

   if (*family == 0xf || *family == 0) /* extended family is added in */

to:

/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */

and change line 99 from

   if (*model == 0xf)                  /* extended model is concatenated */

to:

/* if (*model == 0xf)*/                /* extended model is concatenated */

Essentially, all the Core2-based systems are treated the same by ATLAS. So, to get to use the architectural defaults on Core2-based XEONs, change line 297 from:

      case 15:

to:

      case 15: ; case 23:
[end quote]


---

Comment by mabshoff created at 2008-12-17 13:47:39

The latest errata is the following:

```
To fix this, simply comment out lines 95 and 99 of ATLAS/CONFIG/src/backend
/archinfo_x86.c. So, change line 95 from:

   if (*family == 0xf || *family == 0) /* extended family is added in */

to:

/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */

and change line 99 from

   if (*model == 0xf)                  /* extended model is concatenated */

to:

/* if (*model == 0xf)*/                /* extended model is concatenated */

Essentially, all the Core2-based systems are treated the same by ATLAS. So, 
to get to use the architectural defaults on Core2-based XEONs, change line 
297 from:

      case 15:

to:

      case 15: ; case 23:

Finally, to enable better P4E identification, change line 313 from:

      case 4:

to:

      case 4: ; case 6:
```



---

Comment by mabshoff created at 2008-12-17 14:16:13

This will be resolved via #3785.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-02 07:09:14

This will be fixed via #3785. The spkg is also there.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-02 21:53:33

Positive review via #3785.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-02 21:54:17

Merged in Sage 3.2.3.final


---

Comment by mabshoff created at 2009-01-02 21:54:17

Resolution: fixed
