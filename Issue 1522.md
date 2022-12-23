# Issue 1522: more 2.9-alpha7 ppc osx prebuilt problems

archive/issues_001522.json:
```json
{
    "body": "Assignee: mabshoff\n\nMore problems:\n\n\n```\ng++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/craigcitro/bd7-sage/local/lib -lntl -lgmp -lpari\nld: warning can't open dynamic library: /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib referenced from: /Users/craigcitro/bd7-sage/local/lib/libntl.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)\nld: Undefined symbols:\n___gmpn_add_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_addmul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_divrem_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_gcd referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_gcdext referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_lshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_mod_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_mul referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_mul_1 referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_rshift referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_sqrtrem referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_sub_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n___gmpn_tdiv_qr referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib\n/usr/bin/libtool: internal link edit command failed\nscons: *** [libcsage.dylib] Error 1\nERROR: There was an error building c_lib.\n\n```\n\n\nThe file libntl.dylib in local/lib mentions /Users/was/ when you do a \"strings -\" on it, which may or may not be fishy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1522\n\n",
    "created_at": "2007-12-15T07:03:06Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "more 2.9-alpha7 ppc osx prebuilt problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1522",
    "user": "craigcitro"
}
```
Assignee: mabshoff

More problems:


```
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/craigcitro/bd7-sage/local/lib -lntl -lgmp -lpari
ld: warning can't open dynamic library: /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib referenced from: /Users/craigcitro/bd7-sage/local/lib/libntl.dylib (checking for undefined symbols may be affected) (No such file or directory, errno = 2)
ld: Undefined symbols:
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
___gmpn_sqrtrem referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_sub_n referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
___gmpn_tdiv_qr referenced from libntl expected to be defined in /Users/was/sage-2.9.alpha7/local/lib/libgmp.3.dylib
/usr/bin/libtool: internal link edit command failed
scons: *** [libcsage.dylib] Error 1
ERROR: There was an error building c_lib.

```


The file libntl.dylib in local/lib mentions /Users/was/ when you do a "strings -" on it, which may or may not be fishy.

Issue created by migration from https://trac.sagemath.org/ticket/1522





---

archive/issue_comments_009744.json:
```json
{
    "body": "Singular might need similar linker flags like the updated NTL, so that the paths to various libraries aren't hardcoded.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-15T07:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1522#issuecomment-9744",
    "user": "mabshoff"
}
```

Singular might need similar linker flags like the updated NTL, so that the paths to various libraries aren't hardcoded.

Cheers,

Michael



---

archive/issue_comments_009745.json:
```json
{
    "body": "This was fixed either late in the 2.8.x or in the 2.9.x cycle.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T06:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1522#issuecomment-9745",
    "user": "mabshoff"
}
```

This was fixed either late in the 2.8.x or in the 2.9.x cycle.

Cheers,

Michael



---

archive/issue_comments_009746.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-10T06:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1522#issuecomment-9746",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009747.json:
```json
{
    "body": "D'oh - this was fixed in 2.9.x [see summary] - need sleep soon ;)",
    "created_at": "2008-01-10T06:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1522#issuecomment-9747",
    "user": "mabshoff"
}
```

D'oh - this was fixed in 2.9.x [see summary] - need sleep soon ;)
