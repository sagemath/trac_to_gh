# Issue 542: get gmp-4.2.2 into SAGE

archive/issues_000542.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/542\n\n",
    "created_at": "2007-08-31T19:30:21Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "get gmp-4.2.2 into SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/542",
    "user": "@williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/542





---

archive/issue_comments_002750.json:
```json
{
    "body": "gmp 4.2.2 has been officially released:\n\n```\nChanges between GMP version 4.2.1 and 4.2.2\n\n  * License is now LGPL version 3.\n\n  Bugs:\n  * Shared library numbers corrected for libcxx.\n  * Fixed serious bug in gmpxx.h where a=a+b*c would generate garbage.\n    Note that this only affects C++ programs.\n  * Fix crash in mpz_set_d for arguments with large negative exponent.\n  * Fix 32-bit ABI bug with Itanium assembly for popcount and hamdist.\n  * Fix assembly syntax problem for powerpc-ibm-aix with AIX native assembler.\n  * Fix problems with x86 --enable-fat, where the compiler where told to\n    generate code for the build machine, not plain i386 code as it should.\n  * Improved recognition of powerpc systems wrt Altivec/VMX capability.\n  * Misc minor fixes, mainly workarounds for compiler/assembler bugs.\n\n  Speedups:\n  * \"Core 2\" and Pentium 4 processors, running in 64-bit mode will get a\n     slight boost as they are now specifically recognized.\n\n  Features:\n  * New support for x86_64-solaris\n  * New, rudimentary support for x86-apple-darwin and x86_64-apple-darwin.\n    (Please see http://gmplib.org/macos.html for more information.)\n```\n",
    "created_at": "2007-09-12T05:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/542#issuecomment-2750",
    "user": "mabshoff"
}
```

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

archive/issue_comments_002751.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-04-07T03:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/542#issuecomment-2751",
    "user": "mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_002752.json:
```json
{
    "body": "Due to licensing restrictions, i.e. LGPL V3+, this will not be merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T03:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/542#issuecomment-2752",
    "user": "mabshoff"
}
```

Due to licensing restrictions, i.e. LGPL V3+, this will not be merged.

Cheers,

Michael
