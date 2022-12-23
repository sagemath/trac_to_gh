# Issue 542: get gmp-4.2.2 into SAGE

Issue created by migration from https://trac.sagemath.org/ticket/542

Original creator: was

Original creation time: 2007-08-31 19:30:21

Assignee: was




---

Comment by mabshoff created at 2007-09-12 05:10:06

gmp 4.2.2 has been officially released:

```
Changes between GMP version 4.2.1 and 4.2.2

  * License is now LGPL version 3.

  Bugs:
  * Shared library numbers corrected for libcxx.
  * Fixed serious bug in gmpxx.h where a=a+b*c would generate garbage.
    Note that this only affects C++ programs.
  * Fix crash in mpz_set_d for arguments with large negative exponent.
  * Fix 32-bit ABI bug with Itanium assembly for popcount and hamdist.
  * Fix assembly syntax problem for powerpc-ibm-aix with AIX native assembler.
  * Fix problems with x86 --enable-fat, where the compiler where told to
    generate code for the build machine, not plain i386 code as it should.
  * Improved recognition of powerpc systems wrt Altivec/VMX capability.
  * Misc minor fixes, mainly workarounds for compiler/assembler bugs.

  Speedups:
  * "Core 2" and Pentium 4 processors, running in 64-bit mode will get a
     slight boost as they are now specifically recognized.

  Features:
  * New support for x86_64-solaris
  * New, rudimentary support for x86-apple-darwin and x86_64-apple-darwin.
    (Please see http://gmplib.org/macos.html for more information.)
```



---

Comment by mabshoff created at 2008-04-07 03:49:51

Resolution: wontfix


---

Comment by mabshoff created at 2008-04-07 03:49:51

Due to licensing restrictions, i.e. LGPL V3+, this will not be merged.

Cheers,

Michael
