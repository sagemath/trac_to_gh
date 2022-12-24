# Issue 2303: bessel_I(1,1,"scipy") segfaults with gcc 4.2.3 on Linux x86

archive/issues_002303.json:
```json
{
    "body": "Assignee: mabshoff\n\nKate reports in https://groups.google.com/group/sage-support/browse_thread/thread/f7bc183b6f052943/70f4b300f5be3d13#70f4b300f5be3d13\n\n```\nWhen I build 2.10.2 from source on my\nx86-Linux box (pentium4-fc6) using gcc-4.2.3,\nI get a 'make check' failure at\n\n./sage -t devel/sage-main/sage/functions/special.py\n\nsh: line 1:  3345 Illegal instruction     /home/kate/sage/sage-2.10.2-\nx86-Linux/local/bin/python .doctest_special.py >.doctest/out\n2>.doctest/err\n\nA mysterious error (perphaps a memory error?) occurred, which may have\ncrashed doctest.\n         [3.6 s]\nexit code: 256\n\nThe offending line seems to be\n\nsage: bessel_I(1,1,\"scipy\")\n/home/kate/sage/sage-2.10.2-x86-Linux/local/bin/sage-sage: line 212:\n3484 Illegal instruction     sage-ipython -c \"$SAGE_STARTUP_COMMAND;\"\n\"$@\"\n\nKate \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2303\n\n",
    "created_at": "2008-02-25T21:23:59Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "bessel_I(1,1,\"scipy\") segfaults with gcc 4.2.3 on Linux x86",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2303",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Kate reports in https://groups.google.com/group/sage-support/browse_thread/thread/f7bc183b6f052943/70f4b300f5be3d13#70f4b300f5be3d13

```
When I build 2.10.2 from source on my
x86-Linux box (pentium4-fc6) using gcc-4.2.3,
I get a 'make check' failure at

./sage -t devel/sage-main/sage/functions/special.py

sh: line 1:  3345 Illegal instruction     /home/kate/sage/sage-2.10.2-
x86-Linux/local/bin/python .doctest_special.py >.doctest/out
2>.doctest/err

A mysterious error (perphaps a memory error?) occurred, which may have
crashed doctest.
         [3.6 s]
exit code: 256

The offending line seems to be

sage: bessel_I(1,1,"scipy")
/home/kate/sage/sage-2.10.2-x86-Linux/local/bin/sage-sage: line 212:
3484 Illegal instruction     sage-ipython -c "$SAGE_STARTUP_COMMAND;"
"$@"

Kate 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2303





---

archive/issue_comments_015316.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-25T21:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15316",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015317.json:
```json
{
    "body": "If anybody can reproduce this, e.g., has a P4 computer, please post here.\nThe temporary solution will be to disable the scipy option for bessel_l, \nthen report this upstream (with a gdb traceback?) to scipy.",
    "created_at": "2008-02-25T21:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15317",
    "user": "was"
}
```

If anybody can reproduce this, e.g., has a P4 computer, please post here.
The temporary solution will be to disable the scipy option for bessel_l, 
then report this upstream (with a gdb traceback?) to scipy.



---

archive/issue_comments_015318.json:
```json
{
    "body": "Using Sage 2.10.2 on this computer (Ubuntu 7.10, 32-bit):\n\n```\nvendor_id       : GenuineIntel\ncpu family      : 15\nmodel           : 4\nmodel name      : Intel(R) Pentium(R) 4 CPU 3.80GHz\nstepping        : 1\ncpu MHz         : 3790.991\ncache size      : 1024 KB\n\n$ gcc -v\nUsing built-in specs.\nTarget: i486-linux-gnu\nConfigured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.1.3 --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release i486-linux-gnu\nThread model: posix\ngcc version 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)\n\n```\n\n\nthe doctest passes:\n\n\n```\n$ sage -t sage/devel/sage-main/sage/functions/special.py \nsage -t  sage/devel/sage-main/sage/functions/special.py     \n         [7.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 7.3 seconds\n```\n\n\nand I get:\n\n\n```\nsage: bessel_I(1,1,\"scipy\")\n0.565159103992000\n```\n",
    "created_at": "2008-03-08T20:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15318",
    "user": "jason"
}
```

Using Sage 2.10.2 on this computer (Ubuntu 7.10, 32-bit):

```
vendor_id       : GenuineIntel
cpu family      : 15
model           : 4
model name      : Intel(R) Pentium(R) 4 CPU 3.80GHz
stepping        : 1
cpu MHz         : 3790.991
cache size      : 1024 KB

$ gcc -v
Using built-in specs.
Target: i486-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.1.3 --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release i486-linux-gnu
Thread model: posix
gcc version 4.1.3 20070929 (prerelease) (Ubuntu 4.1.2-16ubuntu2)

```


the doctest passes:


```
$ sage -t sage/devel/sage-main/sage/functions/special.py 
sage -t  sage/devel/sage-main/sage/functions/special.py     
         [7.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.3 seconds
```


and I get:


```
sage: bessel_I(1,1,"scipy")
0.565159103992000
```




---

archive/issue_comments_015319.json:
```json
{
    "body": "We can finally replicate the problem:\n\n```\n(gdb) bt\n#0  0x02e474ac in dgamln_ () from /tmp/foo/sage-3.0.4.rc0-x86-Linux-fc8/local/lib/python/site-packages/scipy/special/_cephes.so\n#1  0x0028bbc9 in log () from /lib/libm.so.6\n#2  0x40000000 in ?? ()\n```\n\nWilliam says:\n\n```\nWilliam:  here is the sage-free version to replicate the problem:\nscipy.special.iv(float(1),complex(1,0))\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T22:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15319",
    "user": "mabshoff"
}
```

We can finally replicate the problem:

```
(gdb) bt
#0  0x02e474ac in dgamln_ () from /tmp/foo/sage-3.0.4.rc0-x86-Linux-fc8/local/lib/python/site-packages/scipy/special/_cephes.so
#1  0x0028bbc9 in log () from /lib/libm.so.6
#2  0x40000000 in ?? ()
```

William says:

```
William:  here is the sage-free version to replicate the problem:
scipy.special.iv(float(1),complex(1,0))
```


Cheers,

Michael



---

archive/issue_comments_015320.json:
```json
{
    "body": "Attachment [2303-scipy-bessel.patch](tarball://root/attachments/some-uuid/ticket2303/2303-scipy-bessel.patch) by robertwb created at 2008-07-08 23:55:51",
    "created_at": "2008-07-08T23:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15320",
    "user": "robertwb"
}
```

Attachment [2303-scipy-bessel.patch](tarball://root/attachments/some-uuid/ticket2303/2303-scipy-bessel.patch) by robertwb created at 2008-07-08 23:55:51



---

archive/issue_comments_015321.json:
```json
{
    "body": "After discussing with William Stein, we are disabling this option. Note that if one wants to use it it is much faster to directly call scypy.special.iv.",
    "created_at": "2008-07-08T23:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15321",
    "user": "robertwb"
}
```

After discussing with William Stein, we are disabling this option. Note that if one wants to use it it is much faster to directly call scypy.special.iv.



---

archive/issue_comments_015322.json:
```json
{
    "body": "Robert's patch is unfortunately no good because there are *dozens* of different special\nfunctions that crash from scipy. We can't release something that is this broken.  \n\nSo no solution to this yet.",
    "created_at": "2008-07-09T01:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15322",
    "user": "was"
}
```

Robert's patch is unfortunately no good because there are *dozens* of different special
functions that crash from scipy. We can't release something that is this broken.  

So no solution to this yet.



---

archive/issue_comments_015323.json:
```json
{
    "body": "In that case we should probably not bother applying this ticket at all.",
    "created_at": "2008-07-09T01:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15323",
    "user": "robertwb"
}
```

In that case we should probably not bother applying this ticket at all.



---

archive/issue_comments_015324.json:
```json
{
    "body": "Having poked around the solution might be to disabled the \"-fwrapv\" build option for Python. We already do that on Itanium since it caused numerous unexplained doctest failures.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-09T16:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15324",
    "user": "mabshoff"
}
```

Having poked around the solution might be to disabled the "-fwrapv" build option for Python. We already do that on Itanium since it caused numerous unexplained doctest failures.

Cheers,

Michael



---

archive/issue_comments_015325.json:
```json
{
    "body": "It is not a -fwrapv issue, but I have a patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T17:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15325",
    "user": "mabshoff"
}
```

It is not a -fwrapv issue, but I have a patch coming up.

Cheers,

Michael



---

archive/issue_comments_015326.json:
```json
{
    "body": "With the new spkg the following three doctests that used to segfault all due to illegal instruction now pass:\n\n```\n[mabshoff@cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t  devel/sage/sage/plot/plot3d/list_plot3d.py\nsage -t  devel/sage/sage/plot/plot3d/list_plot3d.py         \n\t [6.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 6.3 seconds\n[mabshoff@cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t  devel/sage/sage/finance/time_series.pyx\nsage -t  devel/sage/sage/finance/time_series.pyx            \n\t [15.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 15.1 seconds\n[mabshoff@cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t devel/sage/sage/functions/special.py \nsage -t  devel/sage/sage/functions/special.py               \n\t [8.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 8.2 seconds\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T18:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15326",
    "user": "mabshoff"
}
```

With the new spkg the following three doctests that used to segfault all due to illegal instruction now pass:

```
[mabshoff@cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t  devel/sage/sage/plot/plot3d/list_plot3d.py
sage -t  devel/sage/sage/plot/plot3d/list_plot3d.py         
	 [6.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.3 seconds
[mabshoff@cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t  devel/sage/sage/finance/time_series.pyx
sage -t  devel/sage/sage/finance/time_series.pyx            
	 [15.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 15.1 seconds
[mabshoff@cicero sage-3.0.4-x86-Linux-fc8]$ ./sage -t devel/sage/sage/functions/special.py 
sage -t  devel/sage/sage/functions/special.py               
	 [8.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 8.2 seconds
```


Cheers,

Michael



---

archive/issue_comments_015327.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/numpy-20080104-1.0.4.p5.spkg\n\nfixes the problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T18:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15327",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/numpy-20080104-1.0.4.p5.spkg

fixes the problem.

Cheers,

Michael



---

archive/issue_comments_015328.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-11T18:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2303#issuecomment-15328",
    "user": "was"
}
```

Resolution: fixed
