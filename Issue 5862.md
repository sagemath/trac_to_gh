# Issue 5862: os x libsingular -- sage/libsingular segfaults on first creation of a ring

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-23 04:55:58

Assignee: malb




---

Attachment


---

Comment by mabshoff created at 2009-04-23 05:12:36

The problem is that siInit doesn't get called on 64 bit OSX (William and I verified by adding a printf() statement). After this patch it gets called, but the allocation still fails, so we need to dig a little deeper.

As is the patch is not applicable since we open the mangled name, but siInit should be declared `extern "C"` to avoid this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 06:11:24

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

Comment by malb created at 2009-04-23 08:24:54

Did you ping Hannes on this? Why did you remove `RTLD_GLOBAL`? IIRC this is rather crucial.


---

Comment by mabshoff created at 2009-04-23 08:46:57

Replying to [comment:3 malb]:
> Did you ping Hannes on this?

I did just run `make check` after running `spkg-install` manually, so I assume that a proper `configure` run should result in something useful. 

>  Why did you remove `RTLD_GLOBAL`? IIRC this is rather crucial.

I think the removal of `RTLD_GLOBAL` should not happen. I don't think you need it when using `dlsym()`, but it does not hurt either. As is the patch should not go in since we depend on the mangled name of `siInit` and should declare that function as `extern C` to have an unmangled name. 

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-04-29 20:57:54

Hi,

I digged around in the Mac OS X documentation, especially: http://developer.apple.com/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryUsageGuidelines.html#//apple_ref/doc/uid/TP40001928-SW10

In the section about "Opening Dynamic Libraries" there is also something said about closing dynamic libraries. Especially, the dynamic loader might or might not after "dlclose()" remove the library from the applications address space. That would be an explanation for seeing segfaults, I guess.

Now in line 168 of "multi_polynomial_libsingular.pyx", there is a call to "dlclose()", and this call most probably is done before any ring is instantiated. I remember to have seen a file where on Sage shutdown many memory deallocations and such are performed, probably that call to "dlclose()" is done better there (I don't remember what that place was).

See also trac #5522 about issues with whether libsingular was loaded or not.

Cheers, gsw


---

Comment by malb created at 2009-05-11 17:49:02

Replying to [comment:1 mabshoff]:
> The problem is that siInit doesn't get called on 64 bit OSX (William and I verified by adding a printf() statement). After this patch it gets called, but the allocation still fails, so we need to dig a little deeper.

I cannot confirm this, siInit does get called, I just added a `printf` statement myself.


---

Comment by malb created at 2009-05-11 17:55:11

Here's what I believe is the cause of the problem:

When oMalloc creates a new bucket it assigns the global `om_ZeroPage` to `s_bin->bin->current_page` in `omBin.c`, a NULL pointer so to speak. 

It is defined in `om_Alloc.c` as `omBinPage_t om_ZeroPage[] = {{0, NULL, NULL, NULL, NULL}};`. In `omInsertBinPage` it checks whether the current page is this zero page and this is where things go wrong. It should detect that it indeed deals with the zero page and take another code path. However, for some reason there are at least two `om_ZeroPage` objects around, i.e. the pointer comparison fails. 

Linker fun ahead!


---

Comment by malb created at 2009-05-11 18:06:06


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

Attachment

removes linking in static libraries


---

Comment by malb created at 2009-05-11 19:08:00

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

Comment by GeorgSWeber created at 2009-05-11 21:40:43

Hi,
the hg repository of the spkg posted is unclean, "hg diff" gives:

```
diff -r aff77485c3e8 patches/src.Singular.Makefile.in
--- a/patches/src.Singular.Makefile.in  Mon May 11 11:27:30 2009 -0700
+++ b/patches/src.Singular.Makefile.in  Mon May 11 23:25:18 2009 +0200
`@``@` -101,7 +101,7 `@``@`
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

Comment by malb created at 2009-05-11 23:41:15

I fixed the spkg (same place). I think I ran `-tp 4` for the above timing, so I guess it is not that impressive.


---

Comment by mabshoff created at 2009-05-12 06:06:54

Positive review on spkg and patch. Everything looks kosher inside the spkg. 

Of the doctest failures gen.pyx is a real issue, the other two have been fixed by the first two patches at #5929.

W00t - thanks malb :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 06:35:30

Merged the singular.spkg as well as libsingular_osx64.patch in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 06:35:30

Resolution: fixed


---

Comment by mabshoff created at 2009-05-12 21:13:40

:)
