# Issue 9358: zn_poly passes all tests on on Solaris 10 64-bit SPARC, but fails to install

archive/issues_009358.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jhpalmieri @jaapspies\n\nznpoly passes about 40 self-tests, but fails to install properly. \n\n\n```\nzn_array_mulmid_fft()... ok\nzn_array_mul_fft_dft()... ok\nzn_array_invert()... ok\n\nAll tests passed.\ngcc -O3 -g -m64 -fPIC -L. -I/export/home/drkirkby/sage-4.5.alpha0/local/include \n-I./include -DNDEBUG -o src/tuning.o -c src/tuning.c\nIn file included from ./include/zn_poly.h:75,\n                 from ./include/zn_poly_internal.h:41,\n                 from src/tuning.c:28:\n./include/wide_arith.h:297:2: warning: #warning No assembly implementation of wi\nde multiplication available for this machine; using generic C code instead.\nar -r libzn_poly.a src/array.o src/invert.o src/ks_support.o src/mulmid.o src/mu\nlmid_ks.o src/misc.o src/mpn_mulmid.o src/mul.o src/mul_fft.o src/mul_fft_dft.o \nsrc/mul_ks.o src/nuss.o src/pack.o src/pmf.o src/pmfvec_fft.o src/tuning.o src/z\nn_mod.o\nar: creating libzn_poly.a\nranlib libzn_poly.a\ngcc -shared -m64  -Wl,-soname,libzn_poly-`cat VERSION`.so -o libzn_poly-`cat VER\nSION`.so src/array.o src/invert.o src/ks_support.o src/mulmid.o src/mulmid_ks.o \nsrc/misc.o src/mpn_mulmid.o src/mul.o src/mul_fft.o src/mul_fft_dft.o src/mul_ks\n.o src/nuss.o src/pack.o src/pmf.o src/pmfvec_fft.o src/tuning.o src/zn_mod.o -L\n/export/home/drkirkby/sage-4.5.alpha0/local/lib -lgmp -lm\nld: warning: option -o appears more than once, first setting taken\nld: fatal: file libzn_poly-0.9.so: unknown file type\nld: fatal: File processing errors. No output written to libzn_poly-0.9.so\ncollect2: ld returned 1 exit status\nmake: *** [libzn_poly.so] Error 1\nError building zn_poly shared library.\n\nreal\t1m38.825s\nuser\t1m34.368s\nsys\t0m3.849s\nsage: An error occurred while installing zn_poly-0.9.p4\n```\n\n\nThis looks like a problem in spkg-install, which is undoubtedly my fault. The script has in if/elif/else/fi which considers\n\n* A 64-bit build\n* A Solaris build with the Sun linker. \n\nIt does **not** cover the possibility of a 64-bit build on Solaris with the Sun linker. \n\nThis should be hopefully quite easy to fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9358\n\n",
    "created_at": "2010-06-28T16:47:26Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "zn_poly passes all tests on on Solaris 10 64-bit SPARC, but fails to install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9358",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jhpalmieri @jaapspies

znpoly passes about 40 self-tests, but fails to install properly. 


```
zn_array_mulmid_fft()... ok
zn_array_mul_fft_dft()... ok
zn_array_invert()... ok

All tests passed.
gcc -O3 -g -m64 -fPIC -L. -I/export/home/drkirkby/sage-4.5.alpha0/local/include 
-I./include -DNDEBUG -o src/tuning.o -c src/tuning.c
In file included from ./include/zn_poly.h:75,
                 from ./include/zn_poly_internal.h:41,
                 from src/tuning.c:28:
./include/wide_arith.h:297:2: warning: #warning No assembly implementation of wi
de multiplication available for this machine; using generic C code instead.
ar -r libzn_poly.a src/array.o src/invert.o src/ks_support.o src/mulmid.o src/mu
lmid_ks.o src/misc.o src/mpn_mulmid.o src/mul.o src/mul_fft.o src/mul_fft_dft.o 
src/mul_ks.o src/nuss.o src/pack.o src/pmf.o src/pmfvec_fft.o src/tuning.o src/z
n_mod.o
ar: creating libzn_poly.a
ranlib libzn_poly.a
gcc -shared -m64  -Wl,-soname,libzn_poly-`cat VERSION`.so -o libzn_poly-`cat VER
SION`.so src/array.o src/invert.o src/ks_support.o src/mulmid.o src/mulmid_ks.o 
src/misc.o src/mpn_mulmid.o src/mul.o src/mul_fft.o src/mul_fft_dft.o src/mul_ks
.o src/nuss.o src/pack.o src/pmf.o src/pmfvec_fft.o src/tuning.o src/zn_mod.o -L
/export/home/drkirkby/sage-4.5.alpha0/local/lib -lgmp -lm
ld: warning: option -o appears more than once, first setting taken
ld: fatal: file libzn_poly-0.9.so: unknown file type
ld: fatal: File processing errors. No output written to libzn_poly-0.9.so
collect2: ld returned 1 exit status
make: *** [libzn_poly.so] Error 1
Error building zn_poly shared library.

real	1m38.825s
user	1m34.368s
sys	0m3.849s
sage: An error occurred while installing zn_poly-0.9.p4
```


This looks like a problem in spkg-install, which is undoubtedly my fault. The script has in if/elif/else/fi which considers

* A 64-bit build
* A Solaris build with the Sun linker. 

It does **not** cover the possibility of a 64-bit build on Solaris with the Sun linker. 

This should be hopefully quite easy to fix.

Issue created by migration from https://trac.sagemath.org/ticket/9358





---

archive/issue_comments_088704.json:
```json
{
    "body": "Attachment [zn_poly-0.9.p4.log](tarball://root/attachments/some-uuid/ticket9358/zn_poly-0.9.p4.log) by drkirkby created at 2010-06-28 16:48:41\n\nLog file of building on a Sun Blade 1000 SPARC (64-bit build)",
    "created_at": "2010-06-28T16:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88704",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [zn_poly-0.9.p4.log](tarball://root/attachments/some-uuid/ticket9358/zn_poly-0.9.p4.log) by drkirkby created at 2010-06-28 16:48:41

Log file of building on a Sun Blade 1000 SPARC (64-bit build)



---

archive/issue_comments_088705.json:
```json
{
    "body": "This also fails with a 64-bit build on fulvia (Solaris on x86), by the way.",
    "created_at": "2010-08-02T22:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88705",
    "user": "https://github.com/jhpalmieri"
}
```

This also fails with a 64-bit build on fulvia (Solaris on x86), by the way.



---

archive/issue_comments_088706.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> This also fails with a 64-bit build on fulvia (Solaris on x86), by the way.\n\nYou do not surprise me. \n\nI have a patch, but I'm working on improving `spkg-install` and `spkg-check`. Currently `spkg-install` runs a quick test suite with `make check`. That does not seem such a bad idea, so I'm not changing that.  With SAGE_CHECK unset, this takes 46 seconds to build and run the quick test suite on my Sun Ultra 27 to build. \n\nHowever, `spkg-check` currently runs the same test suite for a second time, which is clearly pointless. I'm changing `spkg-check` to run run the more extensive test suite. That increases the time to 7 minutes and 37 seconds on my 3.33 GHz Sun Ultra 27. That will probably close to hour on the Sun T5240 't2.math.washington.edu', so if you run with SAGE_CHECK=yes, bear that in mind. \n\nDave",
    "created_at": "2010-08-04T00:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88706",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:2 jhpalmieri]:
> This also fails with a 64-bit build on fulvia (Solaris on x86), by the way.

You do not surprise me. 

I have a patch, but I'm working on improving `spkg-install` and `spkg-check`. Currently `spkg-install` runs a quick test suite with `make check`. That does not seem such a bad idea, so I'm not changing that.  With SAGE_CHECK unset, this takes 46 seconds to build and run the quick test suite on my Sun Ultra 27 to build. 

However, `spkg-check` currently runs the same test suite for a second time, which is clearly pointless. I'm changing `spkg-check` to run run the more extensive test suite. That increases the time to 7 minutes and 37 seconds on my 3.33 GHz Sun Ultra 27. That will probably close to hour on the Sun T5240 't2.math.washington.edu', so if you run with SAGE_CHECK=yes, bear that in mind. 

Dave



---

archive/issue_comments_088707.json:
```json
{
    "body": "Whilst looking at the zn_poly package, I found what I think is a serious flaw in the dependencies for the package - see #9681. I'd appreciate a second pair of eyes on that one. \n\nDave",
    "created_at": "2010-08-04T00:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88707",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Whilst looking at the zn_poly package, I found what I think is a serious flaw in the dependencies for the package - see #9681. I'd appreciate a second pair of eyes on that one. 

Dave



---

archive/issue_comments_088708.json:
```json
{
    "body": "A fix can now be found. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/zn_poly-0.9.p5.spkg\n\nA much more extensive test suite can now be run if `SAGE_CHECK` is exported to \"yes\". \n\nDave",
    "created_at": "2010-08-07T20:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88708",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

A fix can now be found. 

http://boxen.math.washington.edu/home/kirkby/patches/zn_poly-0.9.p5.spkg

A much more extensive test suite can now be run if `SAGE_CHECK` is exported to "yes". 

Dave



---

archive/issue_comments_088709.json:
```json
{
    "body": "Attachment [9358-zn_poly.patch](tarball://root/attachments/some-uuid/ticket9358/9358-zn_poly.patch) by drkirkby created at 2010-08-07 20:02:51",
    "created_at": "2010-08-07T20:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88709",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9358-zn_poly.patch](tarball://root/attachments/some-uuid/ticket9358/9358-zn_poly.patch) by drkirkby created at 2010-08-07 20:02:51



---

archive/issue_comments_088710.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-07T20:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88710",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088711.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-12T00:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88711",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088712.json:
```json
{
    "body": "Looks good to me.  Builds successfully on lots of different platforms with SAGE_CHECK='yes' including t2 (both 32- and 64-bit) and fulvia (32-bit, and according to SAGE_CHECK, 64-bit -- since I don't have a working 64-bit build because of maxima, it's hard to be positive).",
    "created_at": "2010-08-12T00:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88712",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  Builds successfully on lots of different platforms with SAGE_CHECK='yes' including t2 (both 32- and 64-bit) and fulvia (32-bit, and according to SAGE_CHECK, 64-bit -- since I don't have a working 64-bit build because of maxima, it's hard to be positive).



---

archive/issue_comments_088713.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T08:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9358#issuecomment-88713",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023089.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-15T08:04:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9358",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9358#event-23089"
}
```
