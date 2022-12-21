# Issue 5284: Set sage-flags.txt up to SSE2 only when building Sage in SSE2 only mode/remove SSSE3 and SSE4 flags (followup to #5219)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-16 11:54:08

Assignee: mabshoff

This is a followup to #5219:

 * When building ATLAS in SSE2 only mode the sage-flags should be set accordingly to avoid that Sage complains on startup.

 * We do not use any SSE instructions beyond PNI (i.e. SSE3) at the moment, yet we check for SSSE3 and SSE4 flags. So do not add them to sage-flags since they will trigger wrong warning.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 11:54:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-01 02:30:12

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 07:06:27

This needs to be fixed in 3.4.1!

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 07:07:52

We need to check

```
SAGE_SIMD_MODE
```

The only supported value at the moment is `SSE2`. So remove pni, ssse3 from the flags array.

Cheers,

Michael


---

Attachment


---

Comment by tornaria created at 2009-04-22 03:52:39

Looks good to me.

For the record, I want to point out that mpir may be using `lahf` flag, which is _not_ among the tested-for flags. Note that `lahf` does not depend on `ssse3` (e.g. a Pentium D 930 has `lahf` but not `ssse3`). Apparently the first intel 64 bit cpus did _not_ have `lahf`.


---

Comment by was created at 2009-04-22 03:59:39

I also tried this and it works fine.

tornaria -- good catch regarding lahf.  We need to make a ticket about that!!


---

Comment by mabshoff created at 2009-04-22 04:11:08

Replying to [comment:9 was]:
> I also tried this and it works fine.
> 
> tornaria -- good catch regarding lahf.  We need to make a ticket about that!!

That is part of #5849.

A P4 that does not have lahf is exceedingly rare and AFAIK we have never seen a problem with it, but I am sure we will hit it in the future. Note that x86 vs. core2 code in 64 bit MPIR is quote noticeable performance wise for some benchmarks.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 04:12:10

Merged in Sage 3.4.1.final. Last ticket for 3.4.1 - w00000t.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 04:12:10

Resolution: fixed
