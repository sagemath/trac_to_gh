# Issue 1615: mpfi -- build is seriously broken on at least one system

archive/issues_001615.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n\nHi Kate,\n\n> When I build sage-2.9.1.1 from source on the architectures\n> of interest to me, I get an error when building\n>\n>      mpfi-1.3.4-cvs20071125.p2\n>\n> gcc -fPIC -o test_mpfi test_mpfi.o  ../src/.libs/libmpfi.a\n> /home/kate/sage/sage-2.9.1.1-x86_64-Linux/local/lib/libmpfr.a -lgmp\n> ../src/.libs/libmpfi.a(mpfi_io.o): In function `mpfi_inp_str':\n> mpfi_io.c:(.text+0x999): undefined reference to `__gmp_get_memory_functions'\n>\n> If I look in sage-2.9.1.1/local/lib, I notice that mpfr is built statically,\n> but gmp is not.  (Is there a good reason for this?)\n\nDefault policy is to build all libraries dynamically so that we do not\nneed to recompile loads of dependencies. What you encounter is a bug\nin mpfi.\n\n>  If I change\n> the line in gmp-4.2.1.p12/spkg-install from\n>\n>    SAGE_CONF_OPTS=\"--enable-shared --disable-static\"\n>\n> to\n>     SAGE_CONF_OPTS=\"--enable-shared\"\n>\n> then gmp builds a static version.\n>\n> If I then change mpfi-1.3.4-cvs20071125.p2/spkg-install\n> from\n>\n> ./configure --prefix=\"$SAGE_LOCAL\" --with-mpfr-dir=\"$SAGE_LOCAL\"\n> --with-gmp-incpath=\"$SAGE_LOCAL\"/include CFLAGS=\"-fPIC\"\n>\n> to\n>\n> ./configure --prefix=\"$SAGE_LOCAL\" --with-gmp-dir=\"$SAGE_LOCAL\"\n> --with-mpfr-dir=\"$SAGE_LOCAL\" CFLAGS=\"-fPIC\"\n>\n> then mpfi builds fine.\n\nWe should add the --with-gmp-dir to the mpfi configure per default and\nalso fix the the problem so that a dynamic gmp is accepted.\n\n> I suspect you are NOT seeing this problem because your compile\n> machines have a system gmp installed that is being picked up.\n>\n> Naturally, there may be a better way to fix the problem than\n> I have given.\n>\n\nCheers,\n\nMichael\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1615\n\n",
    "created_at": "2007-12-28T20:44:11Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "mpfi -- build is seriously broken on at least one system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1615",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```

Hi Kate,

> When I build sage-2.9.1.1 from source on the architectures
> of interest to me, I get an error when building
>
>      mpfi-1.3.4-cvs20071125.p2
>
> gcc -fPIC -o test_mpfi test_mpfi.o  ../src/.libs/libmpfi.a
> /home/kate/sage/sage-2.9.1.1-x86_64-Linux/local/lib/libmpfr.a -lgmp
> ../src/.libs/libmpfi.a(mpfi_io.o): In function `mpfi_inp_str':
> mpfi_io.c:(.text+0x999): undefined reference to `__gmp_get_memory_functions'
>
> If I look in sage-2.9.1.1/local/lib, I notice that mpfr is built statically,
> but gmp is not.  (Is there a good reason for this?)

Default policy is to build all libraries dynamically so that we do not
need to recompile loads of dependencies. What you encounter is a bug
in mpfi.

>  If I change
> the line in gmp-4.2.1.p12/spkg-install from
>
>    SAGE_CONF_OPTS="--enable-shared --disable-static"
>
> to
>     SAGE_CONF_OPTS="--enable-shared"
>
> then gmp builds a static version.
>
> If I then change mpfi-1.3.4-cvs20071125.p2/spkg-install
> from
>
> ./configure --prefix="$SAGE_LOCAL" --with-mpfr-dir="$SAGE_LOCAL"
> --with-gmp-incpath="$SAGE_LOCAL"/include CFLAGS="-fPIC"
>
> to
>
> ./configure --prefix="$SAGE_LOCAL" --with-gmp-dir="$SAGE_LOCAL"
> --with-mpfr-dir="$SAGE_LOCAL" CFLAGS="-fPIC"
>
> then mpfi builds fine.

We should add the --with-gmp-dir to the mpfi configure per default and
also fix the the problem so that a dynamic gmp is accepted.

> I suspect you are NOT seeing this problem because your compile
> machines have a system gmp installed that is being picked up.
>
> Naturally, there may be a better way to fix the problem than
> I have given.
>

Cheers,

Michael
```


Issue created by migration from https://trac.sagemath.org/ticket/1615





---

archive/issue_comments_010242.json:
```json
{
    "body": "I changed the following two macros in `src/configure.ac`:\n\n```\n# Checks for MPFR lib (Before GMP!)\nif ` test \"$with_mpfr_lib\" `\nthen\n  AC_MSG_CHECKING(MPFR library)\n        if  test -r \"$with_mpfr_lib/libmpfr.so\"\n        then\n          LDADD=\"$LDADD -L$with_gmp_lib -lmpfr\"\n        else\n           AC_MSG_ERROR([$with_mpfr_lib/libmpfr.so not found])\n        fi\n  AC_MSG_RESULT(yes)\nelse\n  AC_CHECK_LIB(mpfr, main, , AC_MSG_ERROR([Library MPFR not found]))\nfi\n\n# Checks for GMP lib\nif ` test \"$with_gmp_lib\" `\nthen\n  AC_MSG_CHECKING(GMP library)\n        if  test -r \"$with_gmp_lib/libgmp.so\"\n        then\n          LDADD=\"$LDADD -L$with_gmp_lib -lgmp\"\n        else\n           AC_MSG_ERROR([$with_gmp_lib/libgmp.so not found])\n        fi\n  AC_MSG_RESULT(yes)\nelse\n  AC_CHECK_LIB(gmp, main, , AC_MSG_ERROR([Library GMP not found]))\nfi\n```\n\nThe updated spkg is at \n\n http://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-cvs20071125.p0.spkg\n\nand needs to be tested.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T09:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1615#issuecomment-10242",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I changed the following two macros in `src/configure.ac`:

```
# Checks for MPFR lib (Before GMP!)
if ` test "$with_mpfr_lib" `
then
  AC_MSG_CHECKING(MPFR library)
        if  test -r "$with_mpfr_lib/libmpfr.so"
        then
          LDADD="$LDADD -L$with_gmp_lib -lmpfr"
        else
           AC_MSG_ERROR([$with_mpfr_lib/libmpfr.so not found])
        fi
  AC_MSG_RESULT(yes)
else
  AC_CHECK_LIB(mpfr, main, , AC_MSG_ERROR([Library MPFR not found]))
fi

# Checks for GMP lib
if ` test "$with_gmp_lib" `
then
  AC_MSG_CHECKING(GMP library)
        if  test -r "$with_gmp_lib/libgmp.so"
        then
          LDADD="$LDADD -L$with_gmp_lib -lgmp"
        else
           AC_MSG_ERROR([$with_gmp_lib/libgmp.so not found])
        fi
  AC_MSG_RESULT(yes)
else
  AC_CHECK_LIB(gmp, main, , AC_MSG_ERROR([Library GMP not found]))
fi
```

The updated spkg is at 

 http://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-cvs20071125.p0.spkg

and needs to be tested.

Cheers,

Michael



---

archive/issue_comments_010243.json:
```json
{
    "body": "Arrg, the correct spkg is at \n\n http://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-cvs20071125.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T09:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1615#issuecomment-10243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Arrg, the correct spkg is at 

 http://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-cvs20071125.p3.spkg

Cheers,

Michael



---

archive/issue_comments_010244.json:
```json
{
    "body": "Ok, the above spkg didn't work on OSX since there the dynamic library extension is `dylib`. Change the macros to:\n\n```\n# Checks for MPFR lib (Before GMP!)\nif ` test \"$with_mpfr_lib\" `\nthen\n  AC_MSG_CHECKING(MPFR library)\n        if test -r \"$with_mpfr_lib/libmpfr.so\"\n        then\n          LDADD=\"$LDADD -L$with_gmp_lib -lmpfr\"\n        else\n           if test -r \"$with_mpfr_lib/libmpfr.dylib\"\n           then\n             LDADD=\"$LDADD -L$with_gmp_lib -lmpfr\"\n           else\n             AC_MSG_ERROR([$with_mpfr_lib/libmpfr.so or libmpfr.dylib not found])\n           fi\n        fi\n  AC_MSG_RESULT(yes)\nelse\n  AC_CHECK_LIB(mpfr, main, , AC_MSG_ERROR([Library MPFR not found]))\nfi\n\n# Checks for GMP lib\nif ` test \"$with_gmp_lib\" `\nthen\n  AC_MSG_CHECKING(GMP library)\n        if test -r \"$with_gmp_lib/libgmp.so\"\n        then\n          LDADD=\"$LDADD -L$with_gmp_lib -lgmp\"\n        else\n          if test -r \"$with_gmp_lib/libgmp.dylib\"\n          then\n            LDADD=\"$LDADD -L$with_gmp_lib -lgmp\"\n          else\n            AC_MSG_ERROR([$with_gmp_lib/libgmp.so or libgmp.dylib not found])\n          fi\n        fi\n  AC_MSG_RESULT(yes)\nelse\n  AC_CHECK_LIB(gmp, main, , AC_MSG_ERROR([Library GMP not found]))\nfi\n```\n\nThe spkg is linked at\n\nhttp://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-cvs20071125.p4.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T10:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1615#issuecomment-10244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, the above spkg didn't work on OSX since there the dynamic library extension is `dylib`. Change the macros to:

```
# Checks for MPFR lib (Before GMP!)
if ` test "$with_mpfr_lib" `
then
  AC_MSG_CHECKING(MPFR library)
        if test -r "$with_mpfr_lib/libmpfr.so"
        then
          LDADD="$LDADD -L$with_gmp_lib -lmpfr"
        else
           if test -r "$with_mpfr_lib/libmpfr.dylib"
           then
             LDADD="$LDADD -L$with_gmp_lib -lmpfr"
           else
             AC_MSG_ERROR([$with_mpfr_lib/libmpfr.so or libmpfr.dylib not found])
           fi
        fi
  AC_MSG_RESULT(yes)
else
  AC_CHECK_LIB(mpfr, main, , AC_MSG_ERROR([Library MPFR not found]))
fi

# Checks for GMP lib
if ` test "$with_gmp_lib" `
then
  AC_MSG_CHECKING(GMP library)
        if test -r "$with_gmp_lib/libgmp.so"
        then
          LDADD="$LDADD -L$with_gmp_lib -lgmp"
        else
          if test -r "$with_gmp_lib/libgmp.dylib"
          then
            LDADD="$LDADD -L$with_gmp_lib -lgmp"
          else
            AC_MSG_ERROR([$with_gmp_lib/libgmp.so or libgmp.dylib not found])
          fi
        fi
  AC_MSG_RESULT(yes)
else
  AC_CHECK_LIB(gmp, main, , AC_MSG_ERROR([Library GMP not found]))
fi
```

The spkg is linked at

http://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-cvs20071125.p4.spkg

Cheers,

Michael



---

archive/issue_comments_010245.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-04T10:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1615#issuecomment-10245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004018.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-04T10:13:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1615",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1615#event-4018"
}
```
