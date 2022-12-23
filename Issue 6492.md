# Issue 6492: ratpoints -- new spkg is totally completely broken on OS X 64-bit

Issue created by migration from https://trac.sagemath.org/ticket/6492

Original creator: was

Original creation time: 2009-07-09 02:35:35

Assignee: mabshoff

I really should have tested this before letting this spkg get into Sage!   On OS X do the following:

(1) export SAGE64="yes"
(2) Try to build Sage
(3) install the experimental fortran spkg:

```
sage -i fortran-OSX64-20090120
```



Then continue the build and get DISASTER when ratpoints is hit:

```
Finished extraction
****************************************************
Host system
uname -a:
Darwin bsd.local 9.7.0 Darwin Kernel Version 9.7.0: Tue Mar 31 22:52:17 PDT 2009; root:xnu-1228.12.14~1/RELEASE_I386 i386
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin9
Configured with: /var/tmp/gcc/gcc-5465~16/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=i686-apple-darwin9 --with-arch=apple --with-tune=generic --host=i686-apple-darwin9 --target=i686-apple-darwin9
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5465)
****************************************************
Building without SSE2 instructions (OS X).
gcc sift.c -c -o sift.o -I/Users/was/build/64bit/sage-4.1.rc1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -funroll-loops -fnested-functions
gcc gen_init_sieve_h.c -o gen_init_sieve_h  -I/Users/was/build/64bit/sage-4.1.rc1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -L/Users/was/build/64bit/sage-4.1.rc1/local/lib -lgmp -lm -fnested-functions
ld: warning in /Users/was/build/64bit/sage-4.1.rc1/local/lib/libgmp.dylib, file is not of required architecture
./gen_init_sieve_h > init_sieve.h
gcc init.c -c -o init.o -I/Users/was/build/64bit/sage-4.1.rc1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -funroll-loops -O3 -fnested-functions
gcc sturm.c -c -o sturm.o -I/Users/was/build/64bit/sage-4.1.rc1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -fnested-functions
gcc gen_find_points_h.c -o gen_find_points_h  -I/Users/was/build/64bit/sage-4.1.rc1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -L/Users/was/build/64bit/sage-4.1.rc1/local/lib -lgmp -lm -fnested-functions
ld: warning in /Users/was/build/64bit/sage-4.1.rc1/local/lib/libgmp.dylib, file is not of required architecture
./gen_find_points_h > find_points.h
gcc find_points.c -c -o find_points.o -I/Users/was/build/64bit/sage-4.1.rc1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -fnested-functions
ar rs libratpoints.a sift.o init.o sturm.o find_points.o
ar: creating archive libratpoints.a
gcc main.c -o ratpoints -I/Users/was/build/64bit/sage-4.1.rc1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME=7 -L/Users/was/build/64bit/sage-4.1.rc1/local/lib -lgmp -lm -L. -lratpoints -fnested-functions
ld: warning in /Users/was/build/64bit/sage-4.1.rc1/local/lib/libgmp.dylib, file is not of required architecture
Undefined symbols:
  "___gmpz_init", referenced from:
      _read_input in cciW77q8.o
      _main in cciW77q8.o
      _main in cciW77q8.o
      _main in cciW77q8.o
      _find_points_init in libratpoints.a(find_points.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_mul_ui", referenced from:
      _scan_mpz in cciW77q8.o
      __ratpoints_check_point in libratpoints.a(find_points.o)
      __ratpoints_check_point in libratpoints.a(find_points.o)
  "___gmpz_add", referenced from:
      __ratpoints_check_point in libratpoints.a(find_points.o)
      _eval_sign in libratpoints.a(sturm.o)
  "___gmpz_get_str", referenced from:
      _print_poly in cciW77q8.o
      _print_poly in cciW77q8.o
      _print_poly in cciW77q8.o
  "___gmpz_sqrt", referenced from:
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_mul", referenced from:
      __ratpoints_check_point in libratpoints.a(find_points.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_fdiv_q", referenced from:
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_get_si", referenced from:
      _get_2adic_info in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_clear", referenced from:
      _read_input in cciW77q8.o
      _main in cciW77q8.o
      _main in cciW77q8.o
      _main in cciW77q8.o
      _main in cciW77q8.o
      _main in cciW77q8.o
      _find_points_clear in libratpoints.a(find_points.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_fdiv_q_2exp", referenced from:
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_fdiv_r_ui", referenced from:
      _sieving_info in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_add_ui", referenced from:
      _scan_mpz in cciW77q8.o
  "___gmpz_set_si", referenced from:
      _scan_mpz in cciW77q8.o
      __ratpoints_check_point in libratpoints.a(find_points.o)
      __ratpoints_check_point in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_sqrtrem", referenced from:
      __ratpoints_check_point in libratpoints.a(find_points.o)
  "___gmpz_set", referenced from:
      _print_poly in cciW77q8.o
      _scan_mpz in cciW77q8.o
      __ratpoints_check_point in libratpoints.a(find_points.o)
      _valuation in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _eval_sign in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_submul", referenced from:
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_fits_slong_p", referenced from:
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_set_ui", referenced from:
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_mul_2exp", referenced from:
      _eval_sign in libratpoints.a(sturm.o)
  "___gmpz_kronecker_si", referenced from:
      _sieving_info in libratpoints.a(find_points.o)
  "___gmpz_cmp_si", referenced from:
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_cmp_ui", referenced from:
      _print_poly in cciW77q8.o
      _print_poly in cciW77q8.o
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_fdiv_q_ui", referenced from:
      _valuation in libratpoints.a(find_points.o)
      _valuation in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_scan1", referenced from:
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_gcd", referenced from:
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
  "___gmpz_out_str", referenced from:
      _process in cciW77q8.o
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpn_perfect_square_p", referenced from:
      _find_points_work in libratpoints.a(find_points.o)
      _find_points_work in libratpoints.a(find_points.o)
  "___gmpz_mul_si", referenced from:
      __ratpoints_check_point in libratpoints.a(find_points.o)
      _eval_sign in libratpoints.a(sturm.o)
      __ratpoints_compute_sturm in libratpoints.a(sturm.o)
ld: symbol(s) not found
collect2: ld returned 1 exit status
make[2]: *** [ratpoints] Error 1
./spkg-install: line 34: [: Darwin: integer expression expected
Error building ratpoints

real    0m2.012s
user    0m1.769s
sys     0m0.215s
sage: An error occurred while installing ratpoints-2.1.2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/was/build/64bit/sage-4.1.rc1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/was/build/64bit/sage-4.1.rc1/spkg/build/ratpoints-2.1.2 and type 'make'.
Instead type "/Users/was/build/64bit/sage-4.1.rc1/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/was/build/64bit/sage-4.1.rc1/spkg/build/ratpoints-2.1.2
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/ratpoints-2.1.2] Error 1

real    8m8.519s
user    5m29.564s
sys     2m6.462s
Error building Sage.
wstein@bsd:~/build/64bit/sage-4.1.rc1$ 
```



---

Comment by was created at 2009-07-09 02:46:44

The first mistake in the spkg is this:

```
if [ $? -ne 0 ]; then
    if [ `uname` -ne "Darwin" ]; then
        echo "Build failed. Trying without SSE2 instructions."
```


Evidently "-ne" can *only* be used for numerical comparisons. Here we must use the following.

```
if [ $? -ne 0 ]; then
    if [ `uname` != "Darwin" ]; then
        echo "Build failed. Trying without SSE2 instructions."
```


Also, I had to add an -m64 option...

OK, here's the spkg that fixes all the problems:

   http://sage.math.washington.edu/home/wstein/patches/ratpoints-2.1.2.p1.spkg


---

Comment by saliola created at 2009-07-09 11:08:37

ratpoints is also a problem on some Linux machines: see #6498. The new spkg seems to fix things.


---

Comment by rlm created at 2009-07-09 18:22:32

Changing priority from major to blocker.


---

Comment by rlm created at 2009-07-09 18:41:18

Resolution: fixed


---

Comment by rlm created at 2009-07-09 18:41:18

Merged in sage-4.1 final.


---

Comment by was created at 2009-07-09 22:08:01

New spkg here: http://sage.math.washington.edu/home/wstein/patches/ratpoints-2.1.2.p2.spkg


---

Comment by was created at 2009-07-09 22:08:01

Changing status from closed to reopened.


---

Comment by was created at 2009-07-09 22:08:01

Resolution changed from fixed to 


---

Comment by rlm created at 2009-07-09 23:33:25

Works this time... :)


---

Comment by rlm created at 2009-07-09 23:33:25

Resolution: fixed
