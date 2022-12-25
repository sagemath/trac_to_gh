# Issue 6234: make parallel GCC'ing of Sage library not experimental

archive/issues_006234.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @mwhansen @ncalexan\n\nJust get rid of the SAGE_PARALLEL_DIST check here in `devel/sage/setup.py`:\n\n\n```\n        # See if we're trying out the experimental parallel build\n        # code.\n        if ncpus > 1 and os.environ.has_key('SAGE_PARALLEL_DIST'):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6234\n\n",
    "created_at": "2009-06-06T16:47:27Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "make parallel GCC'ing of Sage library not experimental",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6234",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

CC:  @mwhansen @ncalexan

Just get rid of the SAGE_PARALLEL_DIST check here in `devel/sage/setup.py`:


```
        # See if we're trying out the experimental parallel build
        # code.
        if ncpus > 1 and os.environ.has_key('SAGE_PARALLEL_DIST'):
```


Issue created by migration from https://trac.sagemath.org/ticket/6234





---

archive/issue_comments_049640.json:
```json
{
    "body": "I've added a patch that removes the check for the `SAGE_PARALLEL_DIST` flag, and adds a few comments at the top. This should be pretty easy to review; if it makes anyone feel better, I'll probably be using it while merging tickets, and I can report back.",
    "created_at": "2009-06-09T09:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49640",
    "user": "https://github.com/craigcitro"
}
```

I've added a patch that removes the check for the `SAGE_PARALLEL_DIST` flag, and adds a few comments at the top. This should be pretty easy to review; if it makes anyone feel better, I'll probably be using it while merging tickets, and I can report back.



---

archive/issue_comments_049641.json:
```json
{
    "body": "Attachment [trac-6234.patch](tarball://root/attachments/some-uuid/ticket6234/trac-6234.patch) by @craigcitro created at 2009-06-10 00:39:43",
    "created_at": "2009-06-10T00:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49641",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6234.patch](tarball://root/attachments/some-uuid/ticket6234/trac-6234.patch) by @craigcitro created at 2009-06-10 00:39:43



---

archive/issue_comments_049642.json:
```json
{
    "body": "Fixed patch to correct a silly typo noted by Nick.",
    "created_at": "2009-06-10T00:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49642",
    "user": "https://github.com/craigcitro"
}
```

Fixed patch to correct a silly typo noted by Nick.



---

archive/issue_comments_049643.json:
```json
{
    "body": "This wasn't showing up in the \"needs review\" list, because that does a text search for \"needs review\" and thus misses \"needs easy review\".",
    "created_at": "2009-06-10T10:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49643",
    "user": "https://github.com/loefflerd"
}
```

This wasn't showing up in the "needs review" list, because that does a text search for "needs review" and thus misses "needs easy review".



---

archive/issue_comments_049644.json:
```json
{
    "body": "I can't say for certain that this is at fault, but this was from the build of 4.0.2.alpha0 on sage.math:\n\n\n```\n...\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\\\ntch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\\\neleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix2.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix2.o -w\ng++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pEX.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lcsage \\\n-lntl -lgmp -lgmpxx -lm -lstdc++ -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pEX.so\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local/lib/python2.5/si\\\nte-packages/numpy/core/include -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//inc\\\nlude/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local/include/python2.5 \\\n-c sage/matrix/matrix_complex_double_dense.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.o -w\ngcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/action.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lstdc++ -lntl\\\n -o build/lib.linux-x86_64-2.5/sage/matrix/action.so\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\\\ntch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\\\neleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix_cyclo_dense.cpp -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_cyclo_dense.\\\no -w\ncc1plus: warning: command line option \"-Wstrict-prototypes\" is valid for Ada/C/ObjC but not for C++\ngcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -\\\nlcsage -lcblas -latlas -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.so\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\\\ntch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\\\neleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix_dense.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_dense.o -w\ng++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pX.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lcsage -\\\nlntl -lgmp -lgmpxx -lm -lstdc++ -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pX.so\nerror: could not create 'build/temp.linux-x86_64-2.5/sage/matrix': File exists\nsage: There was an error installing modified sage library code.\n\nERROR installing SAGE\n...\n```\n",
    "created_at": "2009-06-11T20:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49644",
    "user": "https://github.com/ncalexan"
}
```

I can't say for certain that this is at fault, but this was from the build of 4.0.2.alpha0 on sage.math:


```
...
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\
tch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\
eleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix2.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix2.o -w
g++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pEX.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lcsage \
-lntl -lgmp -lgmpxx -lm -lstdc++ -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pEX.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local/lib/python2.5/si\
te-packages/numpy/core/include -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//inc\
lude/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local/include/python2.5 \
-c sage/matrix/matrix_complex_double_dense.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.o -w
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/action.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lstdc++ -lntl\
 -o build/lib.linux-x86_64-2.5/sage/matrix/action.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\
tch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\
eleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix_cyclo_dense.cpp -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_cyclo_dense.\
o -w
cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++
gcc -pthread -shared build/temp.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -\
lcsage -lcblas -latlas -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/matrix/matrix_complex_double_dense.so
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//include -I/scra\
tch/ncalexan/releases/sage-4.0.2.alpha0/local//include/csage -I/scratch/ncalexan/releases/sage-4.0.2.alpha0/devel//sage/sage/ext -I/scratch/ncalexan/r\
eleases/sage-4.0.2.alpha0/local/include/python2.5 -c sage/matrix/matrix_dense.c -o build/temp.linux-x86_64-2.5/sage/matrix/matrix_dense.o -w
g++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pX.o -L/scratch/ncalexan/releases/sage-4.0.2.alpha0/local//lib -lcsage -lcsage -\
lntl -lgmp -lgmpxx -lm -lstdc++ -lstdc++ -lntl -o build/lib.linux-x86_64-2.5/sage/libs/ntl/ntl_ZZ_pX.so
error: could not create 'build/temp.linux-x86_64-2.5/sage/matrix': File exists
sage: There was an error installing modified sage library code.

ERROR installing SAGE
...
```




---

archive/issue_comments_049645.json:
```json
{
    "body": "Attachment [trac-6234-pt2.patch](tarball://root/attachments/some-uuid/ticket6234/trac-6234-pt2.patch) by @craigcitro created at 2009-06-12 02:12:34",
    "created_at": "2009-06-12T02:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49645",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6234-pt2.patch](tarball://root/attachments/some-uuid/ticket6234/trac-6234-pt2.patch) by @craigcitro created at 2009-06-12 02:12:34



---

archive/issue_comments_049646.json:
```json
{
    "body": "I think that's a race condition -- I suspect two calls to build_ext simultaneously realize that there's no directory to store a file and try to create it at the same time. The first is okay, but the second gets an error and bails.\n\nThe attached patch should fix this, as long as that's what's going on -- it creates all the appropriate directories in `build/` while processing files in serial, thereby eliminating the potential race problem.",
    "created_at": "2009-06-12T02:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49646",
    "user": "https://github.com/craigcitro"
}
```

I think that's a race condition -- I suspect two calls to build_ext simultaneously realize that there's no directory to store a file and try to create it at the same time. The first is okay, but the second gets an error and bails.

The attached patch should fix this, as long as that's what's going on -- it creates all the appropriate directories in `build/` while processing files in serial, thereby eliminating the potential race problem.



---

archive/issue_comments_049647.json:
```json
{
    "body": "Real test will sage-4.0.2.alpha1.",
    "created_at": "2009-06-12T06:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49647",
    "user": "https://github.com/ncalexan"
}
```

Real test will sage-4.0.2.alpha1.



---

archive/issue_events_014610.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2009-06-12T08:07:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6234#event-14610"
}
```



---

archive/issue_comments_049648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T08:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6234#issuecomment-49648",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed
