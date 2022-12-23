# Issue 2919: [with patch, needs review] gcc 4.3: compilation issues in partitions_c.cc

Issue created by migration from https://trac.sagemath.org/ticket/2919

Original creator: mabshoff

Original creation time: 2008-04-14 19:28:37

Assignee: mabshoff

partitions_c.cc does not build with gcc 4.3 since it dislikes 

```
template <> static inline dd_real pi() { return dd_pi; }
```

The attached patch fixes those issues, compile tested with gcc 4.3, 4.1 and 4.0

Cheers,

Michael 


---

Attachment


---

Comment by mhansen created at 2008-04-14 19:31:58

Looks good to me :)


---

Comment by mabshoff created at 2008-04-14 19:57:35

Resolution: fixed


---

Comment by mabshoff created at 2008-04-14 19:57:35

Merged in Sage 3.0.alpha5
