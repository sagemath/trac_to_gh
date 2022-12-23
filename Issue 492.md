# Issue 492: gcc 4.3: fix ntl_wrap.cc in sage_c_lib

archive/issues_000492.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello,\n\nanother one in the ongoing quest: ntl_wrap.cc needs \"#include string.h\" to compile. Otherwise:\n\n```\n g++ -DPACKAGE_NAME=\\\"libcsage\\\" -DPACKAGE_TARNAME=\\\"libcsage\\\" -DPACKAGE_VERSION=\\\"0.0.1\\\" \"-DPACKAGE_STRING=\\\"libcsage 0.0.1\\\"\" -DPACKAGE_BUGREPORT=\\\"\\\" -DPACKAGE=\\\"libcsage\\\" -DVERSION=\\\"0.0.1\\\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_SETJMP_H=1 -DHAVE_PYTHON_H=1 -DHAVE_SIGNAL_H=1 -DHAVE_ZZ_H=1 -DHAVE_SIGNAL=1 -I. -I. -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/python2.5/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/NTL/ -fPIC -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/python2.5/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/NTL/ -MT ntl_wrap.lo -MD -MP -MF .deps/ntl_wrap.Tpo -c src/ntl_wrap.cc  -fPIC -DPIC -o .libs/ntl_wrap.o\nsrc/ntl_wrap.cc: In function 'char* ZZ_to_str(const NTL::ZZ*)':\nsrc/ntl_wrap.cc:38: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:40: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* ZZ_p_to_str(const NTL::ZZ_p*)':\nsrc/ntl_wrap.cc:210: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:212: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* ZZX_repr(NTL::ZZX*)':\nsrc/ntl_wrap.cc:330: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:332: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* ZZX_trace_list(NTL::ZZX*)':\nsrc/ntl_wrap.cc:633: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:635: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* ZZ_pX_repr(NTL::ZZ_pX*)':\nsrc/ntl_wrap.cc:733: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:735: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* ZZ_pX_trace_list(NTL::ZZ_pX*)':\nsrc/ntl_wrap.cc:1010: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:1012: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* mat_ZZ_to_str(NTL::mat_ZZ*)':\nsrc/ntl_wrap.cc:1109: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:1111: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* GF2X_to_str(const NTL::GF2X*)':\nsrc/ntl_wrap.cc:1234: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:1236: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* GF2E_to_str(const NTL::GF2E*)':\nsrc/ntl_wrap.cc:1370: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:1372: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* GF2EX_to_str(const NTL::GF2EX*)':\nsrc/ntl_wrap.cc:1498: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:1500: error: 'strcpy' was not declared in this scope\nsrc/ntl_wrap.cc: In function 'char* mat_GF2E_to_str(NTL::mat_GF2E*)':\nsrc/ntl_wrap.cc:1580: error: 'strlen' was not declared in this scope\nsrc/ntl_wrap.cc:1582: error: 'strcpy' was not declared in this scope\nmake: *** [ntl_wrap.lo] Error 1\n```\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/492\n\n",
    "created_at": "2007-08-25T23:38:40Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "gcc 4.3: fix ntl_wrap.cc in sage_c_lib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/492",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Hello,

another one in the ongoing quest: ntl_wrap.cc needs "#include string.h" to compile. Otherwise:

```
 g++ -DPACKAGE_NAME=\"libcsage\" -DPACKAGE_TARNAME=\"libcsage\" -DPACKAGE_VERSION=\"0.0.1\" "-DPACKAGE_STRING=\"libcsage 0.0.1\"" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"libcsage\" -DVERSION=\"0.0.1\" -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DSTDC_HEADERS=1 -DHAVE_SETJMP_H=1 -DHAVE_PYTHON_H=1 -DHAVE_SIGNAL_H=1 -DHAVE_ZZ_H=1 -DHAVE_SIGNAL=1 -I. -I. -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/python2.5/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/NTL/ -fPIC -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/python2.5/ -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local/include/NTL/ -MT ntl_wrap.lo -MD -MP -MF .deps/ntl_wrap.Tpo -c src/ntl_wrap.cc  -fPIC -DPIC -o .libs/ntl_wrap.o
src/ntl_wrap.cc: In function 'char* ZZ_to_str(const NTL::ZZ*)':
src/ntl_wrap.cc:38: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:40: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* ZZ_p_to_str(const NTL::ZZ_p*)':
src/ntl_wrap.cc:210: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:212: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* ZZX_repr(NTL::ZZX*)':
src/ntl_wrap.cc:330: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:332: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* ZZX_trace_list(NTL::ZZX*)':
src/ntl_wrap.cc:633: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:635: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* ZZ_pX_repr(NTL::ZZ_pX*)':
src/ntl_wrap.cc:733: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:735: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* ZZ_pX_trace_list(NTL::ZZ_pX*)':
src/ntl_wrap.cc:1010: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:1012: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* mat_ZZ_to_str(NTL::mat_ZZ*)':
src/ntl_wrap.cc:1109: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:1111: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* GF2X_to_str(const NTL::GF2X*)':
src/ntl_wrap.cc:1234: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:1236: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* GF2E_to_str(const NTL::GF2E*)':
src/ntl_wrap.cc:1370: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:1372: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* GF2EX_to_str(const NTL::GF2EX*)':
src/ntl_wrap.cc:1498: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:1500: error: 'strcpy' was not declared in this scope
src/ntl_wrap.cc: In function 'char* mat_GF2E_to_str(NTL::mat_GF2E*)':
src/ntl_wrap.cc:1580: error: 'strlen' was not declared in this scope
src/ntl_wrap.cc:1582: error: 'strcpy' was not declared in this scope
make: *** [ntl_wrap.lo] Error 1
```

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/492





---

archive/issue_comments_002461.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-25T23:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/492#issuecomment-2461",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002462.json:
```json
{
    "body": "This issue has been resolved by the NTL rewrite a couple releases ago.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T20:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/492#issuecomment-2462",
    "user": "mabshoff"
}
```

This issue has been resolved by the NTL rewrite a couple releases ago.

Cheers,

Michael



---

archive/issue_comments_002463.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T20:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/492#issuecomment-2463",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002464.json:
```json
{
    "body": "Resolved with an unknown release before 2.9.alpha1.",
    "created_at": "2007-12-06T20:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/492",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/492#issuecomment-2464",
    "user": "mabshoff"
}
```

Resolved with an unknown release before 2.9.alpha1.
