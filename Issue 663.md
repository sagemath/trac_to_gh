# Issue 663: get flint into SAGE!!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-15 20:34:27

Assignee: was




---

Comment by was created at 2007-09-15 21:03:56


```
Problems with gcc-3.3:

3:58 < williamstein> mabshoff -- regarding gcc and flint -- shouldn't sage still work with gcc-3.3?
13:59 < williamstein> I.e., so far SAGe doesn't require gcc-3.4, so shouldn't we make it so flint can work with gcc-3.3.
13:59 < williamstein> Or?
13:59 < mabshoff> Well, gcc 3.3.x is a decent compiler.
13:59 < mabshoff> So it should work, and there are some workarounds for the problems in FLINT.
14:02 < mabshoff> well:
14:02 < mabshoff>  GCC provides built-in versions of the ISO C99 floating point comparison
14:02 < mabshoff> macros that avoid raising exceptions for unordered operands.  They have
14:02 < mabshoff> the same names as the standard macros ( `isgreater', `isgreaterequal',
14:02 < mabshoff> `isless', `islessequal', `islessgreater', and `isunordered') , with
14:02 < mabshoff> `__builtin_' prefixed.  We intend for a library implementor to be able
14:02 < mabshoff> to simply `#define' each standard macro to its built-in equivalent.
```



---

Comment by was created at 2007-09-20 19:15:37

Resolution: fixed
