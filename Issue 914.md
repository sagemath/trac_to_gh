# Issue 914: NTL wrapper build fails on Ubuntu 7.10

archive/issues_000914.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nI just upgraded to Ubuntu 7.10, and I have some issues building the NTL wrapper.\n\ng++ -o src/ntl_wrap.os -c -fPIC -I/opt/sage/local/include -I/opt/sage/local/include/python2.5 -I/opt/sage/local/include/NTL -Iinclude src/ntl_wrap.cpp\nsrc/ntl_wrap.cpp: In function \u2018NTL::ZZ_pX ZZ_pE_to_ZZ_pX(ZZ_pE)\u2019:\nsrc/ntl_wrap.cpp:794: error: \u2018x\u2019 has incomplete type\nsrc/ntl_wrap.cpp:794: error: forward declaration of \u2018struct ZZ_pE\u2019\nsrc/ntl_wrap.cpp: At global scope:\nsrc/ntl_wrap.cpp:912: error: expected constructor, destructor, or type conversion before \u2018*\u2019 token\nsrc/ntl_wrap.cpp:923: error: expected constructor, destructor, or type conversion before \u2018*\u2019 token\nsrc/ntl_wrap.cpp:1082: error: expected constructor, destructor, or type conversion before \u2018*\u2019 token\nsrc/ntl_wrap.cpp:1087: error: expected constructor, destructor, or type conversion before \u2018*\u2019 token\nsrc/ntl_wrap.cpp:1092: error: variable or field \u2018ZZ_pEContext_restore\u2019 declared void\nsrc/ntl_wrap.cpp:1092: error: \u2018ZZ_pEContext\u2019 was not declared in this scope\nsrc/ntl_wrap.cpp:1092: error: \u2018ctx\u2019 was not declared in this scope\nsrc/ntl_wrap.cpp:1093: error: expected \u2018,\u2019 or \u2018;\u2019 before \u2018{\u2019 token\nscons: *** [src/ntl_wrap.os] Error 1\nERROR: There was an error building c_lib.\n\n\nHere is the ouput of g++ -v\nmike@mike-laptop:/opt/sage$ g++ -v\nUsing built-in specs.\nTarget: x86_64-linux-gnu\nConfigured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.1.3 --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release x86_64-linux-gnu\nThread model: posix\ngcc version 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/914\n\n",
    "created_at": "2007-10-17T17:07:50Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "NTL wrapper build fails on Ubuntu 7.10",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/914",
    "user": "https://github.com/mwhansen"
}
```
Assignee: mabshoff


```
I just upgraded to Ubuntu 7.10, and I have some issues building the NTL wrapper.

g++ -o src/ntl_wrap.os -c -fPIC -I/opt/sage/local/include -I/opt/sage/local/include/python2.5 -I/opt/sage/local/include/NTL -Iinclude src/ntl_wrap.cpp
src/ntl_wrap.cpp: In function ‘NTL::ZZ_pX ZZ_pE_to_ZZ_pX(ZZ_pE)’:
src/ntl_wrap.cpp:794: error: ‘x’ has incomplete type
src/ntl_wrap.cpp:794: error: forward declaration of ‘struct ZZ_pE’
src/ntl_wrap.cpp: At global scope:
src/ntl_wrap.cpp:912: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:923: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:1082: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:1087: error: expected constructor, destructor, or type conversion before ‘*’ token
src/ntl_wrap.cpp:1092: error: variable or field ‘ZZ_pEContext_restore’ declared void
src/ntl_wrap.cpp:1092: error: ‘ZZ_pEContext’ was not declared in this scope
src/ntl_wrap.cpp:1092: error: ‘ctx’ was not declared in this scope
src/ntl_wrap.cpp:1093: error: expected ‘,’ or ‘;’ before ‘{’ token
scons: *** [src/ntl_wrap.os] Error 1
ERROR: There was an error building c_lib.


Here is the ouput of g++ -v
mike@mike-laptop:/opt/sage$ g++ -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.1.3 --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release x86_64-linux-gnu
Thread model: posix
gcc version 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)
```


Issue created by migration from https://trac.sagemath.org/ticket/914





---

archive/issue_comments_005589.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-17T17:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5589",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005590.json:
```json
{
    "body": "Here's the steps I took to get it to work.\n\nrm -rf $SAGE_ROOT/devel/sage-main\nrm -rf $SAGE_ROOT/spkg/installed/sage-2.8.7\nsage -upgrade\n\nThis should probably be marked as invalid.",
    "created_at": "2007-10-17T22:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5590",
    "user": "https://github.com/mwhansen"
}
```

Here's the steps I took to get it to work.

rm -rf $SAGE_ROOT/devel/sage-main
rm -rf $SAGE_ROOT/spkg/installed/sage-2.8.7
sage -upgrade

This should probably be marked as invalid.



---

archive/issue_events_001030.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T01:21:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/914#event-1030"
}
```



---

archive/issue_comments_005591.json:
```json
{
    "body": "There is a problem here, but it's basically probably too hard too fix, and there is an easy workaround (see above).",
    "created_at": "2007-10-19T01:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5591",
    "user": "https://github.com/williamstein"
}
```

There is a problem here, but it's basically probably too hard too fix, and there is an easy workaround (see above).



---

archive/issue_comments_005592.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-19T01:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5592",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_005593.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-19T01:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5593",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001031.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T01:21:19Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/914#event-1031"
}
```



---

archive/issue_comments_005594.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-19T01:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5594",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_005595.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-19T01:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5595",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_events_001032.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T01:21:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/914#event-1032"
}
```



---

archive/issue_comments_005596.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-19T01:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5596",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001033.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T01:21:30Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/914#event-1033"
}
```



---

archive/issue_comments_005597.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2007-10-19T01:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5597",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from invalid to 



---

archive/issue_events_001034.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T01:21:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/914#event-1034"
}
```



---

archive/issue_comments_005598.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2007-10-19T01:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/914#issuecomment-5598",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix
