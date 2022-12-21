# Issue 1415: FLINT 1.0 (from 2.9.alpha1) fails to compile with gcc 4.3 prerelease

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-07 03:02:43

Assignee: was

I tried to compile Sage 2.9.alpha1 with:

```
gcc version 4.3.0 20071130 (experimental) [trunk revision 130545] (Debian 4.3-20071130-1) 
```

on my 64-bit x86 Linux Debian testing box, and compilation failed.

Here's the important chunk from the middle of the FLINT build log:

```
gcc -std=c99 -I/home/cwitty/gcc43-sage-2.9.alpha1/local/include/ -mtune=opteron -march=opteron -fPIC -funroll-loops  -O3 -c ZmodF_poly.c -o ZmodF_poly.o
gcc -std=c99 -I/home/cwitty/gcc43-sage-2.9.alpha1/local/include/ -mtune=opteron -march=opteron -fPIC -funroll-loops  -O3 -c long_extras.c -o long_extras.o
gcc -std=c99 -fPIC -shared -o libflint.so mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o -L/home/cwitty/gcc43-sage-2.9.alpha1/local/lib/  -lgmp -lpthread -lm
mpz_extras.o: In function `__gmpz_fits_uint_p':
mpz_extras.c:(.text+0x0): multiple definition of `__gmpz_fits_uint_p'
mpn_extras.o:mpn_extras.c:(.text+0x0): first defined here
mpz_extras.o: In function `__gmpz_fits_ulong_p':
mpz_extras.c:(.text+0x30): multiple definition of `__gmpz_fits_ulong_p'
mpn_extras.o:mpn_extras.c:(.text+0x30): first defined here
```

followed by many, many more "multiple definition" errors.

Presumably this is caused by the following (from the gcc 4.2 NEWS file):

```
- In the next release of GCC, 4.3, -std=c99 or -std=gnu99 will direct
  GCC to handle inline functions as specified in the C99 standard.  In
  preparation for this, GCC 4.2 will warn about any use of non-static
  inline functions in gnu99 or c99 mode.  This new warning may be
  disabled with the new gnu_inline function attribute or the new
  -fgnu89-inline command line option.  Also, GCC 4.2 and later will
  define one of the preprocessor macros __GNUC_GNU_INLINE__ or
  __GNUC_STDC_INLINE__ to indicate the semantics of inline functions
  in the current compilation.
```




---

Comment by mabshoff created at 2007-12-07 08:13:18

Presumably this will get fixed by upgrading to gmp 4.2.2 which is planned for the 2.9.1 release. That should squash a whole lot of gcc 4.3 related issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 23:18:13

The problem is in the gmp headers related to inline definitions. Since we have to apply the same fix on OSX 10.5 we can work around it, but the trouble is really upstream.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 06:27:24

Resolution: fixed


---

Comment by mabshoff created at 2008-04-20 06:27:24

This has been fixed in Sage 3.0.

Cheers,

Michael
