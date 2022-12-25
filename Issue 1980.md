# Issue 1980: flint fails to build with -fstack-protector

archive/issues_001980.json:
```json
{
    "body": "Assignee: mabshoff\n\nError message:\n\n\n```\n.o mpz_poly.o ZmodF_poly.o long_extras.o -L/home/malb/sage-2.10.1.rc2-stack-protector/local/lib/  -\nlgmp -lpthread -lm\n/home/malb/sage-2.10.1.rc2-stack-protector/local/lib//libgmp.so: undefined reference to `__stack_chk_guard'\n/home/malb/sage-2.10.1.rc2-stack-protector/local/lib//libgmp.so: undefined reference to `__stack_chk_fail'\ncollect2: ld returned 1 exit status\nmake[2]: *** [mpn_extras-test] Error 1\nmake[2]: Leaving directory `/home/malb/sage-2.10.1.rc2-stack-protector/spkg/build/flint-1.06/src'\n./spkg-check: line 46: ./mpn_extras-test: No such file or directory\n./spkg-check: line 47: ./ZmodF-test: No such file or directory\n...\n```\n\n\nSee http://lists.debian.org/debian-devel-announce/2008/01/msg00006.html and http://wiki.debian.org/Hardening for rationale of `-fstack-protector`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1980\n\n",
    "created_at": "2008-01-30T10:31:07Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "flint fails to build with -fstack-protector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1980",
    "user": "https://github.com/malb"
}
```
Assignee: mabshoff

Error message:


```
.o mpz_poly.o ZmodF_poly.o long_extras.o -L/home/malb/sage-2.10.1.rc2-stack-protector/local/lib/  -
lgmp -lpthread -lm
/home/malb/sage-2.10.1.rc2-stack-protector/local/lib//libgmp.so: undefined reference to `__stack_chk_guard'
/home/malb/sage-2.10.1.rc2-stack-protector/local/lib//libgmp.so: undefined reference to `__stack_chk_fail'
collect2: ld returned 1 exit status
make[2]: *** [mpn_extras-test] Error 1
make[2]: Leaving directory `/home/malb/sage-2.10.1.rc2-stack-protector/spkg/build/flint-1.06/src'
./spkg-check: line 46: ./mpn_extras-test: No such file or directory
./spkg-check: line 47: ./ZmodF-test: No such file or directory
...
```


See http://lists.debian.org/debian-devel-announce/2008/01/msg00006.html and http://wiki.debian.org/Hardening for rationale of `-fstack-protector`.


Issue created by migration from https://trac.sagemath.org/ticket/1980





---

archive/issue_comments_012803.json:
```json
{
    "body": "Did the `-fstack-protector` get passed on to gmp? How do you pass `CFLAGS` and so on to all the other packages? \n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T10:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1980#issuecomment-12803",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Did the `-fstack-protector` get passed on to gmp? How do you pass `CFLAGS` and so on to all the other packages? 

Cheers,

Michael



---

archive/issue_comments_012804.json:
```json
{
    "body": "Sorry for being ambiguous. To reproduce:\n\n\n```\nexport CFLAGS=\"-fstack-protector\"\nexport CXXLAGS=\"-fstack-protector\"\ncd <SAGE_ROOT>\nmake\n```\n\n\nThis requires GCC 4.1 and up.",
    "created_at": "2008-01-30T10:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1980#issuecomment-12804",
    "user": "https://github.com/malb"
}
```

Sorry for being ambiguous. To reproduce:


```
export CFLAGS="-fstack-protector"
export CXXLAGS="-fstack-protector"
cd <SAGE_ROOT>
make
```


This requires GCC 4.1 and up.



---

archive/issue_comments_012805.json:
```json
{
    "body": "erm, it is supposed to be `CXXFLAGS`.",
    "created_at": "2008-01-30T10:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1980#issuecomment-12805",
    "user": "https://github.com/malb"
}
```

erm, it is supposed to be `CXXFLAGS`.



---

archive/issue_comments_012806.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-18T18:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1980#issuecomment-12806",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_events_004782.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-08-18T18:30:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1980#event-4782"
}
```



---

archive/issue_comments_012807.json:
```json
{
    "body": "Works for me.",
    "created_at": "2014-08-18T18:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1980#issuecomment-12807",
    "user": "https://github.com/a-andre"
}
```

Works for me.



---

archive/issue_events_004783.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-10-25T21:43:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1980#event-4783"
}
```



---

archive/issue_comments_012808.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-10-25T21:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1980#issuecomment-12808",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
