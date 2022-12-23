# Issue 5865: Add SAGE_SIMD_FLAG="SSE2" README.txt

Issue created by migration from https://trac.sagemath.org/ticket/5865

Original creator: was

Original creation time: 2009-04-23 06:38:41

Assignee: tba

Add some documentation to README.txt that explains the 


```
export SAGE_SIMD_FLAG="SSE2"
```


flag, which makes it so one can build SAGE with ATLAS without sse3 optimizations.  This is slower but works on way more machines.


---

Comment by mabshoff created at 2009-04-24 11:29:28

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2009-04-24 11:29:28

Oops, it is *SAGE_SIMD_MODE* - not sure how this confusion arose.

Cheers,

Michael


---

Comment by was created at 2009-06-02 21:53:22

Resolution: wontfix


---

Comment by was created at 2009-06-02 21:53:22

SAGE_SIMD_MODE is deprecated.
