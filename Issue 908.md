# Issue 908: paru/gen.c causes internal compiler error on OpenSuSE 10.2

archive/issues_000908.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen building 2.8.7 on suse 10.2 amd64:\n\n> -I/home/wdj/sagefiles/sage-2.8.7/local/include/python2.5 -c\n> sage/libs/pari/gen.c -o\n> build/temp.linux-x86_64-2.5/sage/libs/pari/gen.o -w\n> sage/libs/pari/gen.c: In function '__pyx_f_py_3gen_3gen_factor':\n> sage/libs/pari/gen.c:19784: internal compiler error: in\n> merge_alias_info, at tree-ssa-copy.c:235\n> Please submit a full bug report,\n> with preprocessed source if appropriate.\n\n\"gcc blows up ...\"\n\nwdj`@`tinah:~/sagefiles/sage-2.8.7> uname -a\nLinux tinah 2.6.16.13-4-default #1 Wed May 3 04:53:23 UTC 2006 x86_64 x86_64 x86_64 GNU/Linux\nwdj`@`tinah:~/sagefiles/sage-2.8.7> gcc -v\nUsing built-in specs.\nTarget: x86_64-suse-linux\nConfigured with: ../configure --enable-threads=posix --prefix=/usr --with-local-prefix=/usr/local --infodir=/usr/share/info --mandir=/usr/share/man --libdir=/usr/lib64 --libexecdir=/usr/lib64 --enable-languages=c,c++,objc,fortran,java,ada --enable-checking=release --with-gxx-include-dir=/usr/include/c++/4.1.0 --enable-ssp --disable-libssp --enable-java-awt=gtk --enable-gtk-cairo --disable-libjava-multilib --with-slibdir=/lib64 --with-system-zlib --enable-shared --enable-__cxa_atexit --enable-libstdcxx-allocator=new --without-system-libunwind --with-cpu=generic --host=x86_64-suse-linux\nThread model: posix\ngcc version 4.1.0 (SUSE Linux)\n\nIssue created by migration from https://trac.sagemath.org/ticket/908\n\n",
    "created_at": "2007-10-16T16:07:35Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "paru/gen.c causes internal compiler error on OpenSuSE 10.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/908",
    "user": "@wdjoyner"
}
```
Assignee: mabshoff

When building 2.8.7 on suse 10.2 amd64:

> -I/home/wdj/sagefiles/sage-2.8.7/local/include/python2.5 -c
> sage/libs/pari/gen.c -o
> build/temp.linux-x86_64-2.5/sage/libs/pari/gen.o -w
> sage/libs/pari/gen.c: In function '__pyx_f_py_3gen_3gen_factor':
> sage/libs/pari/gen.c:19784: internal compiler error: in
> merge_alias_info, at tree-ssa-copy.c:235
> Please submit a full bug report,
> with preprocessed source if appropriate.

"gcc blows up ..."

wdj`@`tinah:~/sagefiles/sage-2.8.7> uname -a
Linux tinah 2.6.16.13-4-default #1 Wed May 3 04:53:23 UTC 2006 x86_64 x86_64 x86_64 GNU/Linux
wdj`@`tinah:~/sagefiles/sage-2.8.7> gcc -v
Using built-in specs.
Target: x86_64-suse-linux
Configured with: ../configure --enable-threads=posix --prefix=/usr --with-local-prefix=/usr/local --infodir=/usr/share/info --mandir=/usr/share/man --libdir=/usr/lib64 --libexecdir=/usr/lib64 --enable-languages=c,c++,objc,fortran,java,ada --enable-checking=release --with-gxx-include-dir=/usr/include/c++/4.1.0 --enable-ssp --disable-libssp --enable-java-awt=gtk --enable-gtk-cairo --disable-libjava-multilib --with-slibdir=/lib64 --with-system-zlib --enable-shared --enable-__cxa_atexit --enable-libstdcxx-allocator=new --without-system-libunwind --with-cpu=generic --host=x86_64-suse-linux
Thread model: posix
gcc version 4.1.0 (SUSE Linux)

Issue created by migration from https://trac.sagemath.org/ticket/908





---

archive/issue_comments_005583.json:
```json
{
    "body": "It is a known regression. See\n\nhttp://gcc.gnu.org/ml/gcc-bugs/2006-04/msg00700.html\nhttp://lists.debian.org/debian-gcc/2006/05/msg00139.html\n\nI think there is little we can do except to recommend upgrading to a proper compiler.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-16T16:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/908#issuecomment-5583",
    "user": "mabshoff"
}
```

It is a known regression. See

http://gcc.gnu.org/ml/gcc-bugs/2006-04/msg00700.html
http://lists.debian.org/debian-gcc/2006/05/msg00139.html

I think there is little we can do except to recommend upgrading to a proper compiler.

Cheers,

Michael



---

archive/issue_comments_005584.json:
```json
{
    "body": "I disagree that the only solution is to recommend a proper compiler.  We're not the GMP project after all.\n\nSage-2.8.5 compiled fine on SUSE, so this problem only\noccurs with a very recent version of gen.pyx.   I recently modified\nthe factor function in gen.pyx so that it would do provably-correct\nfactorization of integers.   Since that's the function causing the compiler\nerror, probably something I did caused this.    \n\nI'll likely make some attempts to modify my implementation\nto see if I can get around the broken compilers on SUSE.\n\n -- William",
    "created_at": "2007-10-16T18:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/908#issuecomment-5584",
    "user": "@williamstein"
}
```

I disagree that the only solution is to recommend a proper compiler.  We're not the GMP project after all.

Sage-2.8.5 compiled fine on SUSE, so this problem only
occurs with a very recent version of gen.pyx.   I recently modified
the factor function in gen.pyx so that it would do provably-correct
factorization of integers.   Since that's the function causing the compiler
error, probably something I did caused this.    

I'll likely make some attempts to modify my implementation
to see if I can get around the broken compilers on SUSE.

 -- William



---

archive/issue_comments_005585.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2007-10-16T18:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/908#issuecomment-5585",
    "user": "@williamstein"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_005586.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-16T18:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/908#issuecomment-5586",
    "user": "@williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005587.json:
```json
{
    "body": "Well, that remark about GMP is just priceless 8).\n\nIf you find a workaround that should solve this problem I am obviously fine with it, but recently we have seen more and more issues with gcc throwing in the towel, so I still think that the internal tool chain for Sage has its purpose. And we pretty much agree that this is the only way to go on Solaris, Linux Itanium and so on.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-16T18:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/908#issuecomment-5587",
    "user": "mabshoff"
}
```

Well, that remark about GMP is just priceless 8).

If you find a workaround that should solve this problem I am obviously fine with it, but recently we have seen more and more issues with gcc throwing in the towel, so I still think that the internal tool chain for Sage has its purpose. And we pretty much agree that this is the only way to go on Solaris, Linux Itanium and so on.

Cheers,

Michael



---

archive/issue_comments_005588.json:
```json
{
    "body": "Hello,\n\ngood news for SuSE 10.2 user:\n\n```\n[09:33] <Syzygy-> Hmph. I cannot get yast to tell me what the g77-package is named. *grmbl*\n[09:33] <mabshoff> Which SuSE release?\n[09:34] <mabshoff> Hi malb__\n[09:34] <malb__> hi\n[09:34] <mabshoff> You should probably install gfortran\n[09:34] <mabshoff> 10.3 no longer ships g77 or g95, but gfortran.\n[09:34] <Syzygy-> OpenSuSE 10.2\n[09:34] <Syzygy-> Right.\n[09:35] <mabshoff> Really? There is a bug in that gcc that crashes when compiling gen.c\n[09:35] <mabshoff> Does Sage start and compute 2+2?\n[09:35] <Syzygy-> Yes.\n[09:35] <mabshoff> ok, but then you probably update via yast.\n[09:35] <Syzygy-> gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)\n[09:36] <mabshoff> Thanks\n[09:36] <mabshoff> Excellent, you just closed ticket #908.\n[09:37] <Syzygy-> Hehe\n[09:37] <Syzygy-> Happy to help. :)\n```\n\n\nSo we should close this ticket and recommend for people to update via yast to the latest gcc rpms that SuSE provides.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-02T08:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/908#issuecomment-5588",
    "user": "mabshoff"
}
```

Hello,

good news for SuSE 10.2 user:

```
[09:33] <Syzygy-> Hmph. I cannot get yast to tell me what the g77-package is named. *grmbl*
[09:33] <mabshoff> Which SuSE release?
[09:34] <mabshoff> Hi malb__
[09:34] <malb__> hi
[09:34] <mabshoff> You should probably install gfortran
[09:34] <mabshoff> 10.3 no longer ships g77 or g95, but gfortran.
[09:34] <Syzygy-> OpenSuSE 10.2
[09:34] <Syzygy-> Right.
[09:35] <mabshoff> Really? There is a bug in that gcc that crashes when compiling gen.c
[09:35] <mabshoff> Does Sage start and compute 2+2?
[09:35] <Syzygy-> Yes.
[09:35] <mabshoff> ok, but then you probably update via yast.
[09:35] <Syzygy-> gcc version 4.1.2 20061115 (prerelease) (SUSE Linux)
[09:36] <mabshoff> Thanks
[09:36] <mabshoff> Excellent, you just closed ticket #908.
[09:37] <Syzygy-> Hehe
[09:37] <Syzygy-> Happy to help. :)
```


So we should close this ticket and recommend for people to update via yast to the latest gcc rpms that SuSE provides.

Cheers,

Michael



---

archive/issue_comments_005589.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T08:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/908#issuecomment-5589",
    "user": "mabshoff"
}
```

Resolution: fixed
