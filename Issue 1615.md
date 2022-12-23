# Issue 1615: mpfi -- build is seriously broken on at least one system

Issue created by migration from https://trac.sagemath.org/ticket/1615

Original creator: was

Original creation time: 2007-12-28 20:44:11

Assignee: was


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



---

Comment by mabshoff created at 2008-01-04 09:27:07

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

Comment by mabshoff created at 2008-01-04 09:32:41

Arrg, the correct spkg is at 

 http://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-cvs20071125.p3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-04 10:02:26

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

Comment by mabshoff created at 2008-01-04 10:13:22

Resolution: fixed
