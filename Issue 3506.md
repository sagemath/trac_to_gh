# Issue 3506: [with patch; needs review] Sage's m4ri extension fails to build with gcc 4.1.2 20060928 (prerelease) (Ubuntu 4.1.1-13ubuntu5)

archive/issues_003506.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @malb\n\nThe problem:\n\n```\nbuilding 'sage.matrix.matrix_mod2_dense' extension\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/usr/local/sage/local//include -I/usr/local/sage/local//include/csage -I/usr/local/sage/devel//sage/sage/ext -I/usr/local/sage/local/include/python2.5 -c sage/matrix/matrix_mod2_dense.c -o build/temp.linux-i686-2.5/sage/matrix/matrix_mod2_dense.o -w -w\nsage/matrix/matrix_mod2_dense.c: In function \u2018__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense___init__\u2019:\nsage/matrix/matrix_mod2_dense.c:1733: error: \u2018bit\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c:1733: error: (Each undeclared identifier is reported only once\nsage/matrix/matrix_mod2_dense.c:1733: error: for each function it appears in.)\nsage/matrix/matrix_mod2_dense.c:1733: error: expected \u2018;\u2019 before \u2018__pyx_8\u2019\nsage/matrix/matrix_mod2_dense.c:1930: error: \u2018__pyx_8\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c: In function \u2018__pyx_f_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense_set_unsafe\u2019:\nsage/matrix/matrix_mod2_dense.c:2047: error: \u2018bit\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c:2047: error: expected \u2018;\u2019 before \u2018__pyx_3\u2019\nsage/matrix/matrix_mod2_dense.c:2061: error: \u2018__pyx_3\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c: In function \u2018__pyx_f_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense_get_unsafe\u2019:\nsage/matrix/matrix_mod2_dense.c:2086: error: \u2018bit\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c:2086: error: expected \u2018;\u2019 before \u2018__pyx_1\u2019\nsage/matrix/matrix_mod2_dense.c:2095: error: \u2018__pyx_1\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c: In function \u2018__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense__list\u2019:\nsage/matrix/matrix_mod2_dense.c:3462: error: \u2018bit\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c:3462: error: expected \u2018;\u2019 before \u2018__pyx_4\u2019\nsage/matrix/matrix_mod2_dense.c:3504: error: \u2018__pyx_4\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c: In function \u2018__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense__pivots\u2019:\nsage/matrix/matrix_mod2_dense.c:4077: error: \u2018bit\u2019 undeclared (first use in this function)\nsage/matrix/matrix_mod2_dense.c:4077: error: expected \u2018;\u2019 before \u2018__pyx_4\u2019\nsage/matrix/matrix_mod2_dense.c:4164: error: \u2018__pyx_4\u2019 undeclared (first use in this function)\nerror: command 'gcc' failed with exit status 1\nsage: There was an error installing modified sage library code.\n```\n\nFix attached.   This may have to do with a C namespace clash for some compilers.  On\nthe vmware sage image we have:\n\n```\nroot@sage:/usr/local/sage# gcc -v\nUsing built-in specs.\nTarget: i486-linux-gnu\nConfigured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release i486-linux-gnu\nThread model: posix\ngcc version 4.1.2 20060928 (prerelease) (Ubuntu 4.1.1-13ubuntu5)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3506\n\n",
    "closed_at": "2008-07-02T20:38:43Z",
    "created_at": "2008-06-25T01:38:51Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch; needs review] Sage's m4ri extension fails to build with gcc 4.1.2 20060928 (prerelease) (Ubuntu 4.1.1-13ubuntu5)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3506",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @malb

The problem:

```
building 'sage.matrix.matrix_mod2_dense' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/usr/local/sage/local//include -I/usr/local/sage/local//include/csage -I/usr/local/sage/devel//sage/sage/ext -I/usr/local/sage/local/include/python2.5 -c sage/matrix/matrix_mod2_dense.c -o build/temp.linux-i686-2.5/sage/matrix/matrix_mod2_dense.o -w -w
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense___init__’:
sage/matrix/matrix_mod2_dense.c:1733: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:1733: error: (Each undeclared identifier is reported only once
sage/matrix/matrix_mod2_dense.c:1733: error: for each function it appears in.)
sage/matrix/matrix_mod2_dense.c:1733: error: expected ‘;’ before ‘__pyx_8’
sage/matrix/matrix_mod2_dense.c:1930: error: ‘__pyx_8’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_f_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense_set_unsafe’:
sage/matrix/matrix_mod2_dense.c:2047: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:2047: error: expected ‘;’ before ‘__pyx_3’
sage/matrix/matrix_mod2_dense.c:2061: error: ‘__pyx_3’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_f_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense_get_unsafe’:
sage/matrix/matrix_mod2_dense.c:2086: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:2086: error: expected ‘;’ before ‘__pyx_1’
sage/matrix/matrix_mod2_dense.c:2095: error: ‘__pyx_1’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense__list’:
sage/matrix/matrix_mod2_dense.c:3462: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:3462: error: expected ‘;’ before ‘__pyx_4’
sage/matrix/matrix_mod2_dense.c:3504: error: ‘__pyx_4’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c: In function ‘__pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense__pivots’:
sage/matrix/matrix_mod2_dense.c:4077: error: ‘bit’ undeclared (first use in this function)
sage/matrix/matrix_mod2_dense.c:4077: error: expected ‘;’ before ‘__pyx_4’
sage/matrix/matrix_mod2_dense.c:4164: error: ‘__pyx_4’ undeclared (first use in this function)
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```

Fix attached.   This may have to do with a C namespace clash for some compilers.  On
the vmware sage image we have:

```
root@sage:/usr/local/sage# gcc -v
Using built-in specs.
Target: i486-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release i486-linux-gnu
Thread model: posix
gcc version 4.1.2 20060928 (prerelease) (Ubuntu 4.1.1-13ubuntu5)
```

Issue created by migration from https://trac.sagemath.org/ticket/3506





---

archive/issue_comments_024666.json:
```json
{
    "body": "Attachment [sage-3506.patch](tarball://root/attachments/some-uuid/ticket3506/sage-3506.patch) by @williamstein created at 2008-06-25 01:40:02",
    "created_at": "2008-06-25T01:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3506#issuecomment-24666",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3506.patch](tarball://root/attachments/some-uuid/ticket3506/sage-3506.patch) by @williamstein created at 2008-06-25 01:40:02



---

archive/issue_comments_024667.json:
```json
{
    "body": "While I love a descriptive Summary for trac tickets this is taking it slightly too far :)\n\nCheers,\n\nMichael",
    "created_at": "2008-06-25T02:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3506#issuecomment-24667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

While I love a descriptive Summary for trac tickets this is taking it slightly too far :)

Cheers,

Michael



---

archive/issue_comments_024668.json:
```json
{
    "body": "Fixed Summary slightly and added malb to the CC field since he seems to be the canonical person to review this.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-25T02:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3506#issuecomment-24668",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed Summary slightly and added malb to the CC field since he seems to be the canonical person to review this.

Cheers,

Michael



---

archive/issue_comments_024669.json:
```json
{
    "body": "This was the correct fix until the upgrade of the M4RI package. I claim that this update (libm4ri-20080521.p0) renders this fix unnecessary since the bit got renamed to BIT. Btw.: The analysis is correct it was a C nameclash. I'd say: wontfix but I won't just close the ticket. Which Sage is that btw.?",
    "created_at": "2008-06-25T11:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3506#issuecomment-24669",
    "user": "https://github.com/malb"
}
```

This was the correct fix until the upgrade of the M4RI package. I claim that this update (libm4ri-20080521.p0) renders this fix unnecessary since the bit got renamed to BIT. Btw.: The analysis is correct it was a C nameclash. I'd say: wontfix but I won't just close the ticket. Which Sage is that btw.?



---

archive/issue_comments_024670.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-07-02T20:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3506#issuecomment-24670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_007998.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-02T20:38:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3506",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3506#event-7998"
}
```



---

archive/issue_comments_024671.json:
```json
{
    "body": "```\n[1:35pm] malb: I vote for closing #3506\n[1:35pm] malb: wjp so you reviewed the first two patches and added a third?\n[1:36pm] mabshoff: malb: that is what wstein|afk said about 3506, so I am closing it.\n```",
    "created_at": "2008-07-02T20:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3506#issuecomment-24671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

```
[1:35pm] malb: I vote for closing #3506
[1:35pm] malb: wjp so you reviewed the first two patches and added a third?
[1:36pm] mabshoff: malb: that is what wstein|afk said about 3506, so I am closing it.
```
