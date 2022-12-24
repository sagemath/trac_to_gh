# Issue 1520: prebuilt 2.9-alpha7 osx ppc binary has hardcoded paths

archive/issues_001520.json:
```json
{
    "body": "Assignee: mabshoff\n\nFile untars and runs just fine, but trying to change anything and build causes a lot of this:\n\n\n```\ng++ -bundle -undefined dynamic_lookup build/temp.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.o -L/Users/craigcitro/bd7-sage/local//lib -lcsage -lcsage -lntl -lstdc++ -lstdc++ -lntl -o build/lib.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.so\n/usr/bin/ld: warning can't open dynamic library: /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib referenced from: /Users/craigcitro/bd7-sage/local//lib/libcsage.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)\n/usr/bin/ld: warning can't open dynamic library: libpari-gmp.dylib referenced from: /Users/craigcitro/bd7-sage/local//lib/libcsage.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)\n/usr/bin/ld: Undefined symbols:\n___gmpn_add_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_addmul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_divrem_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_gcd referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_gcdext referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_lshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_mod_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_mul referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_mul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_rshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_sqrtrem referenced from libntl expected to be defined in /Users/was/sage\n-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_sub_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_tdiv_qr referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\ncollect2: ld returned 1 exit status\nerror: command 'g++' failed with exit status 1\nsage: There was an error installing modified sage library code.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1520\n\n",
    "created_at": "2007-12-15T05:54:59Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "prebuilt 2.9-alpha7 osx ppc binary has hardcoded paths",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1520",
    "user": "craigcitro"
}
```
Assignee: mabshoff

File untars and runs just fine, but trying to change anything and build causes a lot of this:


```
g++ -bundle -undefined dynamic_lookup build/temp.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.o -L/Users/craigcitro/bd7-sage/local//lib -lcsage -lcsage -lntl -lstdc++ -lstdc++ -lntl -o build/lib.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.so
/usr/bin/ld: warning can't open dynamic library: /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib referenced from: /Users/craigcitro/bd7-sage/local//lib/libcsage.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/bin/ld: warning can't open dynamic library: libpari-gmp.dylib referenced from: /Users/craigcitro/bd7-sage/local//lib/libcsage.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
/usr/bin/ld: Undefined symbols:
___gmpn_add_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_addmul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_divrem_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_gcd referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_gcdext referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_lshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_mod_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_mul referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_mul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_rshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_sqrtrem referenced from libntl expected to be defined in /Users/was/sage
-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_sub_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_tdiv_qr referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.

```


Issue created by migration from https://trac.sagemath.org/ticket/1520





---

archive/issue_comments_009735.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-15T06:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1520#issuecomment-9735",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009736.json:
```json
{
    "body": "Attachment [Sage-2.9.rc0-fix-link-issue-on-OSX-10.4.patch](tarball://root/attachments/some-uuid/ticket1520/Sage-2.9.rc0-fix-link-issue-on-OSX-10.4.patch) by mabshoff created at 2007-12-15 06:53:19",
    "created_at": "2007-12-15T06:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1520#issuecomment-9736",
    "user": "mabshoff"
}
```

Attachment [Sage-2.9.rc0-fix-link-issue-on-OSX-10.4.patch](tarball://root/attachments/some-uuid/ticket1520/Sage-2.9.rc0-fix-link-issue-on-OSX-10.4.patch) by mabshoff created at 2007-12-15 06:53:19



---

archive/issue_comments_009737.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T06:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1520#issuecomment-9737",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009738.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T06:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1520#issuecomment-9738",
    "user": "mabshoff"
}
```

Resolution: fixed
