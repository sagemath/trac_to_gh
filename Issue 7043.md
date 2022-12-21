# Issue 7043: ntl 5.4.2.p9 passes -fPIC to Sun linker with SunStudio

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-28 00:43:35

Assignee: tbd

CC:  leif dimpase

Keywords: ntl solaris linker

I'm using
    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha4
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

```
C: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
/opt/xxxsunstudio12.1/bin/CC -I../include -I.  -O2 -g   -fPIC -c G_LLL_RR.c
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
/opt/xxxsunstudio12.1/bin/CC -I../include -I.  -O2 -g   -fPIC -c vec_ulong.c
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
/opt/xxxsunstudio12.1/bin/CC -I../include -I.  -O2 -g   -fPIC -c vec_vec_ulong.c
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ntl-5.4.2.p9/src/src'
/opt/xxxsunstudio12.1/bin/CC -I../include -I.  -O2 -g    -fPIC -shared -o lib`cat DIRNAME`.so FFT.o FacVec.o GF2.o GF2E.o GF2EX.o GF2EXFactoring.o GF2X.o GF2X1.o GF2XFactoring.o GF2XVec.o GetTime.o HNF.o ctools.o LLL.o LLL_FP.o LLL_QP.o LLL_RR.o LLL_XD.o RR.o WordVector.o ZZ.o ZZVec.o ZZX.o ZZX1.o ZZXCharPoly.o ZZXFactoring.o ZZ_p.o ZZ_pE.o ZZ_pEX.o ZZ_pEXFactoring.o ZZ_pX.o ZZ_pX1.o ZZ_pXCharPoly.o ZZ_pXFactoring.o fileio.o lip.o lzz_p.o lzz_pE.o lzz_pEX.o lzz_pEXFactoring.o lzz_pX.o lzz_pX1.o lzz_pXCharPoly.o lzz_pXFactoring.o mat_GF2.o mat_GF2E.o mat_RR.o mat_ZZ.o mat_ZZ_p.o mat_ZZ_pE.o mat_lzz_p.o mat_lzz_pE.o mat_poly_ZZ.o mat_poly_ZZ_p.o mat_poly_lzz_p.o pair_GF2EX_long.o pair_GF2X_long.o pair_ZZX_long.o pair_ZZ_pEX_long.o pair_ZZ_pX_long.o pair_lzz_pEX_long.o pair_lzz_pX_long.o quad_float.o tools.o vec_GF2.o vec_GF2E.o vec_GF2XVec.o vec_RR.o vec_ZZ.o vec_ZZVec.o vec_ZZ_p.o vec_ZZ_pE.o vec_double.o vec_long.o vec_lzz_p.o vec_lzz_pE.o vec_quad_float.o vec_vec_GF2.o vec_vec_GF2E.o vec_vec_RR.o vec_vec_ZZ.o vec_vec_ZZ_p.o vec_vec_ZZ_pE.o vec_vec_long.o vec_vec_lzz_p.o vec_vec_lzz_pE.o vec_xdouble.o xdouble.o G_LLL_FP.o G_LLL_QP.o G_LLL_XD.o G_LLL_RR.o vec_ulong.o vec_vec_ulong.o -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib -lgmp
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
CC: Warning: Option -shared passed to ld, if ld is invoked, ignored otherwise
ld: fatal: option -h and building a dynamic executable are incompatible
ld: fatal: option -f and building a dynamic executable are incompatible
ld: fatal: Flags processing errors
make[2]: *** [libntl.so] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ntl-5.4.2.p9/src/src'
Error creating ntl shared library.

```



---

Comment by leif created at 2010-09-03 22:11:46

Nice to have that reviewer. ;-)

There's a ticket for upgrading NTL (#5731) I've just "revived"...

----

Hey trac, I *did not* delete `work_issues`.


---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing component from build to packages: standard.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by slelievre created at 2020-08-22 07:16:14

Resolution: invalid
