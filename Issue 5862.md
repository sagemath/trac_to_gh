# Issue 5862: os x libsingular -- sage/libsingular segfaults on first creation of a ring

archive/issues_005862.json:
```json
{
    "body": "Assignee: @malb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5862\n\n",
    "created_at": "2009-04-23T04:55:58Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "os x libsingular -- sage/libsingular segfaults on first creation of a ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5862",
    "user": "@williamstein"
}
```
Assignee: @malb



Issue created by migration from https://trac.sagemath.org/ticket/5862





---

archive/issue_comments_046305.json:
```json
{
    "body": "Attachment [trac_5862.patch](tarball://root/attachments/some-uuid/ticket5862/trac_5862.patch) by @williamstein created at 2009-04-23 04:56:46",
    "created_at": "2009-04-23T04:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46305",
    "user": "@williamstein"
}
```

Attachment [trac_5862.patch](tarball://root/attachments/some-uuid/ticket5862/trac_5862.patch) by @williamstein created at 2009-04-23 04:56:46



---

archive/issue_comments_046306.json:
```json
{
    "body": "The problem is that siInit doesn't get called on 64 bit OSX (William and I verified by adding a printf() statement). After this patch it gets called, but the allocation still fails, so we need to dig a little deeper.\n\nAs is the patch is not applicable since we open the mangled name, but siInit should be declared `extern \"C\"` to avoid this.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T05:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46306",
    "user": "mabshoff"
}
```

The problem is that siInit doesn't get called on 64 bit OSX (William and I verified by adding a printf() statement). After this patch it gets called, but the allocation still fails, so we need to dig a little deeper.

As is the patch is not applicable since we open the mangled name, but siInit should be declared `extern "C"` to avoid this.

Cheers,

Michael



---

archive/issue_comments_046307.json:
```json
{
    "body": "Ok, the problem is when the first ring is instantiated. I tried to verify that omMalloc passes its make check target, but I struck out for now:\n\n```\ngcc -O0 -g -m64  -fPIC -I. -I/Users/mabshoff/sage-3.4.1.rc4-64/local/include -O0 -g -m64  \n-I/Users/mabshoff/sage-3.4.1.rc4-64/local/include -DHAVE_CONFIG_H omtTest.o_ndebug \nomtTestReal.o_ndebug omtTestDebug.o_ndebug omtTestKeep.o_ndebug omtTestError.o_ndebug \n-DOM_NDEBUG -L. -lomalloc_ndebug -o omtTest_ndebug\nUndefined symbols:\n  \"__omDebugFree\", referenced from:\n      _omtTestFreeDebug in omtTestDebug.o_ndebug\n      _omtTestFreeDebug in omtTestDebug.o_ndebug\n      _omtTestFreeKeep in omtTestKeep.o_ndebug\n      _omtTestFreeKeep in omtTestKeep.o_ndebug\n  \"__omDebugAddr\", referenced from:\n      _omtTestDupDebug in omtTestDebug.o_ndebug\n      _omtTestDupKeep in omtTestKeep.o_ndebug\nld: symbol(s) not found\n```\n\n\nI guess I need to dig into the documentation to track this down. Someone with oMalloc experience would certainly help here :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T06:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46307",
    "user": "mabshoff"
}
```

Ok, the problem is when the first ring is instantiated. I tried to verify that omMalloc passes its make check target, but I struck out for now:

```
gcc -O0 -g -m64  -fPIC -I. -I/Users/mabshoff/sage-3.4.1.rc4-64/local/include -O0 -g -m64  
-I/Users/mabshoff/sage-3.4.1.rc4-64/local/include -DHAVE_CONFIG_H omtTest.o_ndebug 
omtTestReal.o_ndebug omtTestDebug.o_ndebug omtTestKeep.o_ndebug omtTestError.o_ndebug 
-DOM_NDEBUG -L. -lomalloc_ndebug -o omtTest_ndebug
Undefined symbols:
  "__omDebugFree", referenced from:
      _omtTestFreeDebug in omtTestDebug.o_ndebug
      _omtTestFreeDebug in omtTestDebug.o_ndebug
      _omtTestFreeKeep in omtTestKeep.o_ndebug
      _omtTestFreeKeep in omtTestKeep.o_ndebug
  "__omDebugAddr", referenced from:
      _omtTestDupDebug in omtTestDebug.o_ndebug
      _omtTestDupKeep in omtTestKeep.o_ndebug
ld: symbol(s) not found
```


I guess I need to dig into the documentation to track this down. Someone with oMalloc experience would certainly help here :)

Cheers,

Michael



---

archive/issue_comments_046308.json:
```json
{
    "body": "Did you ping Hannes on this? Why did you remove `RTLD_GLOBAL`? IIRC this is rather crucial.",
    "created_at": "2009-04-23T08:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46308",
    "user": "@malb"
}
```

Did you ping Hannes on this? Why did you remove `RTLD_GLOBAL`? IIRC this is rather crucial.



---

archive/issue_comments_046309.json:
```json
{
    "body": "Replying to [comment:3 malb]:\n> Did you ping Hannes on this?\n\nI did just run `make check` after running `spkg-install` manually, so I assume that a proper `configure` run should result in something useful. \n\n>  Why did you remove `RTLD_GLOBAL`? IIRC this is rather crucial.\n\nI think the removal of `RTLD_GLOBAL` should not happen. I don't think you need it when using `dlsym()`, but it does not hurt either. As is the patch should not go in since we depend on the mangled name of `siInit` and should declare that function as `extern C` to have an unmangled name. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T08:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46309",
    "user": "mabshoff"
}
```

Replying to [comment:3 malb]:
> Did you ping Hannes on this?

I did just run `make check` after running `spkg-install` manually, so I assume that a proper `configure` run should result in something useful. 

>  Why did you remove `RTLD_GLOBAL`? IIRC this is rather crucial.

I think the removal of `RTLD_GLOBAL` should not happen. I don't think you need it when using `dlsym()`, but it does not hurt either. As is the patch should not go in since we depend on the mangled name of `siInit` and should declare that function as `extern C` to have an unmangled name. 

Cheers,

Michael



---

archive/issue_comments_046310.json:
```json
{
    "body": "Hi,\n\nI digged around in the Mac OS X documentation, especially: http://developer.apple.com/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryUsageGuidelines.html#//apple_ref/doc/uid/TP40001928-SW10\n\nIn the section about \"Opening Dynamic Libraries\" there is also something said about closing dynamic libraries. Especially, the dynamic loader might or might not after \"dlclose()\" remove the library from the applications address space. That would be an explanation for seeing segfaults, I guess.\n\nNow in line 168 of \"multi_polynomial_libsingular.pyx\", there is a call to \"dlclose()\", and this call most probably is done before any ring is instantiated. I remember to have seen a file where on Sage shutdown many memory deallocations and such are performed, probably that call to \"dlclose()\" is done better there (I don't remember what that place was).\n\nSee also trac #5522 about issues with whether libsingular was loaded or not.\n\nCheers, gsw",
    "created_at": "2009-04-29T20:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46310",
    "user": "GeorgSWeber"
}
```

Hi,

I digged around in the Mac OS X documentation, especially: http://developer.apple.com/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryUsageGuidelines.html#//apple_ref/doc/uid/TP40001928-SW10

In the section about "Opening Dynamic Libraries" there is also something said about closing dynamic libraries. Especially, the dynamic loader might or might not after "dlclose()" remove the library from the applications address space. That would be an explanation for seeing segfaults, I guess.

Now in line 168 of "multi_polynomial_libsingular.pyx", there is a call to "dlclose()", and this call most probably is done before any ring is instantiated. I remember to have seen a file where on Sage shutdown many memory deallocations and such are performed, probably that call to "dlclose()" is done better there (I don't remember what that place was).

See also trac #5522 about issues with whether libsingular was loaded or not.

Cheers, gsw



---

archive/issue_comments_046311.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> The problem is that siInit doesn't get called on 64 bit OSX (William and I verified by adding a printf() statement). After this patch it gets called, but the allocation still fails, so we need to dig a little deeper.\n\nI cannot confirm this, siInit does get called, I just added a `printf` statement myself.",
    "created_at": "2009-05-11T17:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46311",
    "user": "@malb"
}
```

Replying to [comment:1 mabshoff]:
> The problem is that siInit doesn't get called on 64 bit OSX (William and I verified by adding a printf() statement). After this patch it gets called, but the allocation still fails, so we need to dig a little deeper.

I cannot confirm this, siInit does get called, I just added a `printf` statement myself.



---

archive/issue_comments_046312.json:
```json
{
    "body": "Here's what I believe is the cause of the problem:\n\nWhen oMalloc creates a new bucket it assigns the global `om_ZeroPage` to `s_bin->bin->current_page` in `omBin.c`, a NULL pointer so to speak. \n\nIt is defined in `om_Alloc.c` as `omBinPage_t om_ZeroPage[] = {{0, NULL, NULL, NULL, NULL}};`. In `omInsertBinPage` it checks whether the current page is this zero page and this is where things go wrong. It should detect that it indeed deals with the zero page and take another code path. However, for some reason there are at least two `om_ZeroPage` objects around, i.e. the pointer comparison fails. \n\nLinker fun ahead!",
    "created_at": "2009-05-11T17:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46312",
    "user": "@malb"
}
```

Here's what I believe is the cause of the problem:

When oMalloc creates a new bucket it assigns the global `om_ZeroPage` to `s_bin->bin->current_page` in `omBin.c`, a NULL pointer so to speak. 

It is defined in `om_Alloc.c` as `omBinPage_t om_ZeroPage[] = {{0, NULL, NULL, NULL, NULL}};`. In `omInsertBinPage` it checks whether the current page is this zero page and this is where things go wrong. It should detect that it indeed deals with the zero page and take another code path. However, for some reason there are at least two `om_ZeroPage` objects around, i.e. the pointer comparison fails. 

Linker fun ahead!



---

archive/issue_comments_046313.json:
```json
{
    "body": "\n```\nbash-3.2$ uname -a\nDarwin bsd.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386\n\nbash-3.2$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\ns_bin->bin->current_page 106e83000\ns_bin->bin->current_page 0\nYou rock!\nsage: R.<x,y> = PolynomialRing(QQ)\nsage: x^20\nx^20\nsage: x^20 + y\nx^20 + y\n```\n",
    "created_at": "2009-05-11T18:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46313",
    "user": "@malb"
}
```


```
bash-3.2$ uname -a
Darwin bsd.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386

bash-3.2$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
s_bin->bin->current_page 106e83000
s_bin->bin->current_page 0
You rock!
sage: R.<x,y> = PolynomialRing(QQ)
sage: x^20
x^20
sage: x^20 + y
x^20 + y
```




---

archive/issue_comments_046314.json:
```json
{
    "body": "Attachment [libsingular_osx64.patch](tarball://root/attachments/some-uuid/ticket5862/libsingular_osx64.patch) by @malb created at 2009-05-11 19:02:33\n\nremoves linking in static libraries",
    "created_at": "2009-05-11T19:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46314",
    "user": "@malb"
}
```

Attachment [libsingular_osx64.patch](tarball://root/attachments/some-uuid/ticket5862/libsingular_osx64.patch) by @malb created at 2009-05-11 19:02:33

removes linking in static libraries



---

archive/issue_comments_046315.json:
```json
{
    "body": "The attached patch `libsingular_osx64.patch` + the spkg at\n\n  http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-4-20090511.spkg\n\nwe get:\n\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/calculus/calculus.py # 0 doctests failed\n        sage -t  devel/sage/sage/libs/pari/gen.pyx # 2 doctests failed\n        sage -t  devel/sage/sage/interfaces/maxima.py # 0 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1579.9 seconds\n```\n\n\nI also tested it on sage.math, doctests still running.",
    "created_at": "2009-05-11T19:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46315",
    "user": "@malb"
}
```

The attached patch `libsingular_osx64.patch` + the spkg at

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-4-20090511.spkg

we get:


```
The following tests failed:

        sage -t  devel/sage/sage/calculus/calculus.py # 0 doctests failed
        sage -t  devel/sage/sage/libs/pari/gen.pyx # 2 doctests failed
        sage -t  devel/sage/sage/interfaces/maxima.py # 0 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1579.9 seconds
```


I also tested it on sage.math, doctests still running.



---

archive/issue_comments_046316.json:
```json
{
    "body": "Hi,\nthe hg repository of the spkg posted is unclean, \"hg diff\" gives:\n\n```\ndiff -r aff77485c3e8 patches/src.Singular.Makefile.in\n--- a/patches/src.Singular.Makefile.in  Mon May 11 11:27:30 2009 -0700\n+++ b/patches/src.Singular.Makefile.in  Mon May 11 23:25:18 2009 +0200\n@@ -101,7 +101,7 @@\n #\n # Handle libSINGULAR stuff\n #\n-LIBSINGULAR_LIBS =-lsingfac -lsingcf -lntl -lreadline -lgmp -lomalloc_ndebug\n+LIBSINGULAR_LIBS =-lsingfac -lsingcf -lntl -lreadline -lgmp -lomalloc\n \n SO_SUFFIX = so\n #LIBSINGULAR_FLAGS = -export-dynamic \n```\n\n(The file as-is should be the correct one, so just has to be checked in. There is an editor-artifact file of the same name followed by a tilde in the spkg.)\n\nThe changes themselves look pretty reasonable and OK to me, but I can't test this on a OS X 64-bit system. I could test only whether they don't break anything on OS X 10.4 32-bit, and I have not done this yet. However, \"1579.9 seconds\" looks awesome --- on my MacIntel box with 2 GHz Core2Duo and Mac OS X 10.4, \"make -j2 test\" needs over 6000 seconds.",
    "created_at": "2009-05-11T21:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46316",
    "user": "GeorgSWeber"
}
```

Hi,
the hg repository of the spkg posted is unclean, "hg diff" gives:

```
diff -r aff77485c3e8 patches/src.Singular.Makefile.in
--- a/patches/src.Singular.Makefile.in  Mon May 11 11:27:30 2009 -0700
+++ b/patches/src.Singular.Makefile.in  Mon May 11 23:25:18 2009 +0200
@@ -101,7 +101,7 @@
 #
 # Handle libSINGULAR stuff
 #
-LIBSINGULAR_LIBS =-lsingfac -lsingcf -lntl -lreadline -lgmp -lomalloc_ndebug
+LIBSINGULAR_LIBS =-lsingfac -lsingcf -lntl -lreadline -lgmp -lomalloc
 
 SO_SUFFIX = so
 #LIBSINGULAR_FLAGS = -export-dynamic 
```

(The file as-is should be the correct one, so just has to be checked in. There is an editor-artifact file of the same name followed by a tilde in the spkg.)

The changes themselves look pretty reasonable and OK to me, but I can't test this on a OS X 64-bit system. I could test only whether they don't break anything on OS X 10.4 32-bit, and I have not done this yet. However, "1579.9 seconds" looks awesome --- on my MacIntel box with 2 GHz Core2Duo and Mac OS X 10.4, "make -j2 test" needs over 6000 seconds.



---

archive/issue_comments_046317.json:
```json
{
    "body": "I fixed the spkg (same place). I think I ran `-tp 4` for the above timing, so I guess it is not that impressive.",
    "created_at": "2009-05-11T23:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46317",
    "user": "@malb"
}
```

I fixed the spkg (same place). I think I ran `-tp 4` for the above timing, so I guess it is not that impressive.



---

archive/issue_comments_046318.json:
```json
{
    "body": "Positive review on spkg and patch. Everything looks kosher inside the spkg. \n\nOf the doctest failures gen.pyx is a real issue, the other two have been fixed by the first two patches at #5929.\n\nW00t - thanks malb :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T06:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46318",
    "user": "mabshoff"
}
```

Positive review on spkg and patch. Everything looks kosher inside the spkg. 

Of the doctest failures gen.pyx is a real issue, the other two have been fixed by the first two patches at #5929.

W00t - thanks malb :)

Cheers,

Michael



---

archive/issue_comments_046319.json:
```json
{
    "body": "Merged the singular.spkg as well as libsingular_osx64.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T06:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46319",
    "user": "mabshoff"
}
```

Merged the singular.spkg as well as libsingular_osx64.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_046320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T06:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46320",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046321.json:
```json
{
    "body": ":)",
    "created_at": "2009-05-12T21:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5862#issuecomment-46321",
    "user": "mabshoff"
}
```

:)
