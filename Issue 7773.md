# Issue 7773: Test failures with Fedora 12 on intel i7 860 processor

Issue created by migration from https://trac.sagemath.org/ticket/7773

Original creator: jsp

Original creation time: 2009-12-27 13:52:40

Assignee: GeorgSWeber

CC:  robertwb malb roed wstein

On this machine I got memory errors, some of wich are reported by glibc-2.11 as double free:

*** glibc detected *** python: double free or corruption (fasttop):


```
       sage -t  devel/sage/sage/groups/generic.py # Segfault
       sage -t  devel/sage/sage/matrix/matrix_space.py # Segfault
       sage -t  devel/sage/sage/matrix/matrix_sparse.pyx # Segfault
       sage -t  devel/sage/sage/matrix/matrix2.pyx # Segfault
       sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # Segfault
       sage -t  devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py # Segfault
[snipped]
```


Valgrind to the rescue! I made a new optional spkg:
[http://trac.sagemath.org/sage_trac/ticket/7766](http://trac.sagemath.org/sage_trac/ticket/7766)

Rebuild sage-4.3 with SAGE_VALGRIND="yes", installed valgrind-3.6.0.svn with the help of 
[http://wiki.sagemath.org/ValgrindingSage](http://wiki.sagemath.org/ValgrindingSage)

./sage -t -valgrind devel/sage/sage/matrix/matrix_sparse.pyx

Some results:


```
==8933== Invalid free() / delete / delete[]
==8933==    at 0x4A04D72: free (vg_replace_malloc.c:325)
==8933==    by 0xE2F6A53: __pyx_f_4sage_5rings_6memory_pymem_free (memory.c:1993)
==8933==    by 0xE716DBC: randclear_lc (in /home/jaap/downloads/sage-4.3/local/lib/libgmp.so.3.4.6)
==8933==    by 0x20D1B78F: gmp_randclass::~gmp_randclass() (gmpxx.h:3248)
==8933==    by 0x3D2D635B71: exit (in /lib64/libc-2.11.so)
==8933==    by 0x4BA729: handle_system_exit (pythonrun.c:1716)
==8933==    by 0x4BA944: PyErr_PrintEx (pythonrun.c:1126)
==8933==    by 0x4BB68F: PyRun_SimpleFileExFlags (pythonrun.c:935)
==8933==    by 0x413CAE: Py_Main (main.c:599)
==8933==    by 0x3D2D61EB1C: (below main) (in /lib64/libc-2.11.so)
==8933==  Address 0x347fd730 is 0 bytes inside a block of size 8 free'd
==8933==    at 0x4A04D72: free (vg_replace_malloc.c:325)
==8933==    by 0xE2F6A53: __pyx_f_4sage_5rings_6memory_pymem_free (memory.c:1993)
==8933==    by 0xE716DBC: randclear_lc (in /home/jaap/downloads/sage-4.3/local/lib/libgmp.so.3.4.6)
==8933==    by 0x3D2D635B71: exit (in /lib64/libc-2.11.so)
==8933==    by 0x4BA729: handle_system_exit (pythonrun.c:1716)
==8933==    by 0x4BA944: PyErr_PrintEx (pythonrun.c:1126)
==8933==    by 0x4BB68F: PyRun_SimpleFileExFlags (pythonrun.c:935)
==8933==    by 0x413CAE: Py_Main (main.c:599)
==8933==    by 0x3D2D61EB1C: (below main) (in /lib64/libc-2.11.so)

```


The complete report can be found on my homepage on sage.math
(i'll put a link here as soon sage.math is up again) valgrind_memcheck_test_matrix_sparse.bz2

Jaap


---

Comment by jsp created at 2010-01-28 01:09:52


```
Gokhan Sever wrote:
> Hello,
> 
> uname -a
> Linux ccn 2.6.31.9-174.fc12.i686.PAE #1 SMP Mon Dec 21 06:04:56 UTC
> 2009 i686 i686 i386 GNU/Linux
> 
> Getting many errors after ./sage -testall
> 
> ----------------------------------------------------------------------
> The following tests failed:
> 
> 	sage -t  "devel/sage/sage/modules/free_module.py" # Segfault
> 	sage -t  "devel/sage/sage/coding/code_constructions.py" # Segfault
> 	sage -t  "devel/sage/sage/coding/linear_code.py" # Segfault
> 	sage -t  "devel/sage/sage/groups/generic.py" # Segfault
> 	sage -t  "devel/sage/sage/modular/ssmod/ssmod.py" # Segfault
> 	sage -t  "devel/sage/sage/modular/modform/ambient.py" # Segfault
> 	sage -t  "devel/sage/sage/modular/modsym/space.py" # Segfault
> 	sage -t  "devel/sage/sage/modular/modsym/modsym.py" # Segfault
> 	sage -t  "devel/sage/sage/matrix/matrix_sparse.pyx" # Segfault
> 	sage -t  "devel/sage/sage/matrix/matrix2.pyx" # Segfault
> 	sage -t  "devel/sage/sage/matrix/matrix_space.py" # Segfault



```


Finally someone with test failures that relate to mine on Fedora 12 x86_64!

Jaap


---

Attachment


---

Comment by GokhanSever created at 2010-01-28 04:55:01

Doctest error log added.


---

Comment by zimmerma created at 2010-02-05 18:57:29

I get a similar failure with linear_codes.py on a Core 2 Duo under Fedora 12 (sage 4.3.1):

```
sage -t  "devel/sage-main/sage/coding/linear_code.py"       
*** glibc detected *** python: double free or corruption (fasttop): 0x000000000528e970 ***
======= Backtrace: =========
/lib64/libc.so.6[0x308e874a76]
/lib64/libc.so.6(exit+0xe2)[0x308e835b82]
python[0x4bc46a]
python(PyErr_PrintEx+0x1a5)[0x4bc685]
python(PyRun_SimpleFileExFlags+0x1e0)[0x4bd3d0]
python(Py_Main+0x9af)[0x413e1f]
/lib64/libc.so.6(__libc_start_main+0xfd)[0x308e81eb1d]
python[0x413079]
```

All files reported by Gokhan Sever fail. In particular modsym says:

```
*** glibc detected *** python: corrupted double-linked list: 0x0000000006119c00 ***
```



---

Comment by erik.galicki created at 2010-02-21 18:34:44

I encounter a similar error with Fedora 12 on Intel Pentium M:

my cpuinfo:

```
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 9
model name	: Intel(R) Pentium(R) M processor 1600MHz
stepping	: 5
cpu MHz		: 1600.000
cache size	: 1024 KB
fdiv_bug	: no
hlt_bug		: no
f00f_bug	: no
coma_bug	: no
fpu		: yes
fpu_exception	: yes
cpuid level	: 2
wp		: yes
flags		: fpu vme de pse tsc msr mce cx8 mtrr pge mca cmov clflush dts acpi mmx fxsr sse sse2 tm pbe up bts est tm2
bogomips	: 3189.39
clflush size	: 64
power management:
```


my gcc -v:

```
Using built-in specs.
Target: i686-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre --enable-libgcj-multifile --enable-java-maintainer-mode --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --disable-libjava-multilib --with-ppl --with-cloog --with-tune=generic --with-arch=i686 --build=i686-redhat-linux
Thread model: posix
gcc version 4.4.3 20100127 (Red Hat 4.4.3-4) (GCC) 
```



my lsb_release:

```
LSB Version:	:core-3.1-ia32:core-3.1-noarch:core-3.2-ia32:core-3.2-noarch:desktop-3.1-ia32:desktop-3.1-noarch:desktop-3.2-ia32:desktop-3.2-noarch
Distributor ID:	Fedora
Description:	Fedora release 12 (Constantine)
Release:	12
Codename:	Constantine
```


last lines of test.log:


```
The following tests failed:


	sage -t  "devel/sage/sage/misc/functional.py"
	sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py" # Segfault
	sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py" # Segfault
	sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py" # Segfault
	sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_point.py" # Segfault
	sage -t  "devel/sage/sage/modules/free_module.py" # Segfault
	sage -t  "devel/sage/sage/groups/generic.py" # Segfault
	sage -t  "devel/sage/sage/rings/polynomial/polynomial_quotient_ring_element.py" # Segfault
	sage -t  "devel/sage/sage/rings/finite_field_ntl_gf2e.pyx" # Segfault
	sage -t  "devel/sage/sage/rings/finite_field_morphism.py" # Segfault
	sage -t  "devel/sage/sage/rings/number_field/number_field.py" # Segfault
	sage -t  "devel/sage/sage/rings/number_field/number_field_rel.py" # Segfault
	sage -t  "devel/sage/sage/rings/finite_field_ext_pari.py" # Segfault
	sage -t  "devel/sage/sage/matrix/matrix_sparse.pyx" # Segfault
	sage -t  "devel/sage/sage/matrix/matrix2.pyx" # Segfault
	sage -t  "devel/sage/sage/matrix/matrix_space.py" # Segfault
	sage -t  "devel/sage/sage/graphs/graph_plot.py"
	sage -t  "devel/sage/sage/coding/linear_code.py" # Segfault
	sage -t  "devel/sage/sage/coding/code_constructions.py" # Segfault
	sage -t  "devel/sage/sage/modular/ssmod/ssmod.py" # Segfault
	sage -t  "devel/sage/sage/modular/modsym/modsym.py" # Segfault
	sage -t  "devel/sage/sage/modular/modsym/space.py" # Segfault
	sage -t  "devel/sage/sage/modular/modform/ambient.py" # Segfault
	sage -t  "devel/sage/sage/tests/benchmark.py" # Segfault
Total time for all tests: 12153.0 seconds

```


detailed failure results:


```
[erik@localhost sage-4.3.3.alpha1]$ ./sage -t devel/sage-main/sage/coding/linear_code.py 
sage -t  "devel/sage-main/sage/coding/linear_code.py"       
*** glibc detected *** python: double free or corruption (fasttop): 0x0bbfb540 ***
======= Backtrace: =========
/lib/libc.so.6[0x296751]
/home/erik/src/sage-4.3.3.alpha1/local/lib/python/site-packages/sage/rings/memory.so(+0x106d)[0xeeb06d]
/home/erik/src/sage-4.3.3.alpha1/local/lib/libgmp.so.3(__gmpz_clear+0x2a)[0x1b52ba]
/lib/libc.so.6(exit+0xdf)[0x25609f]
python[0x80f36d7]
python(PyErr_PrintEx+0x18d)[0x80f38bd]
python(PyErr_Print+0x12)[0x80f3ac2]
python(PyRun_SimpleFileExFlags+0x1ab)[0x80f45db]
python(Py_Main+0xa88)[0x80586d8]
python(main+0x1b)[0x805791b]
/lib/libc.so.6(__libc_start_main+0xe6)[0x23ebb6]
python[0x8057861]
======= Memory map: ========
00106000-00108000 r-xp 00000000 08:03 414026     /lib/libkeyutils-1.2.so
00108000-00109000 rw-p 00001000 08:03 414026     /lib/libkeyutils-1.2.so
00110000-00114000 r-xp 00000000 08:03 162524     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/select.so
00114000-00116000 rw-p 00003000 08:03 162524     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/select.so
00116000-00118000 r-xp 00000000 08:03 416226     /lib/libutil-2.11.1.so
00118000-00119000 r--p 00001000 08:03 416226     /lib/libutil-2.11.1.so
00119000-0011a000 rw-p 00002000 08:03 416226     /lib/libutil-2.11.1.so
0011a000-0012a000 r-xp 00000000 08:03 694112     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/c_lib/libcsage.so
0012a000-0012b000 rw-p 0000f000 08:03 694112     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/c_lib/libcsage.so
0012b000-0013d000 r-xp 00000000 08:03 676319     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/build/sage/misc/misc_c.so
0013d000-00144000 rw-p 00012000 08:03 676319     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/build/sage/misc/misc_c.so
00144000-00145000 r-xp 00000000 08:03 162527     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_bisect.so
00145000-00146000 rw-p 00001000 08:03 162527     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_bisect.so
00146000-00148000 r-xp 00000000 08:03 162536     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_hashlib.so
00148000-00149000 rw-p 00002000 08:03 162536     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_hashlib.so
00149000-00176000 r-xp 00000000 08:03 57413      /lib/libgssapi_krb5.so.2.2
00176000-00177000 rw-p 0002d000 08:03 57413      /lib/libgssapi_krb5.so.2.2
00177000-00178000 rwxp 00000000 00:00 0 
00179000-001a3000 r-xp 00000000 08:03 57410      /lib/libk5crypto.so.3.1
001a3000-001a4000 rw-p 0002a000 08:03 57410      /lib/libk5crypto.so.3.1
001a4000-00201000 r-xp 00000000 08:03 98113      /home/erik/src/sage-4.3.3.alpha1/local/lib/libgmp.so.3.4.6
00201000-00202000 rw-p 0005c000 08:03 98113      /home/erik/src/sage-4.3.3.alpha1/local/lib/libgmp.so.3.4.6
00202000-00204000 r-xp 00000000 08:03 162534     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_heapq.so
00204000-00206000 rw-p 00002000 08:03 162534     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_heapq.so
00206000-00224000 r-xp 00000000 08:03 413969     /lib/ld-2.11.1.so
00224000-00225000 r--p 0001d000 08:03 413969     /lib/ld-2.11.1.so
00225000-00226000 rw-p 0001e000 08:03 413969     /lib/ld-2.11.1.so
00226000-00227000 r-xp 00000000 08:03 162523     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/crypt.so
00227000-00228000 rw-p 00000000 08:03 162523     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/crypt.so
00228000-00397000 r-xp 00000000 08:03 413971     /lib/libc-2.11.1.so
00397000-00399000 r--p 0016e000 08:03 413971     /lib/libc-2.11.1.so
00399000-0039a000 rw-p 00170000 08:03 413971     /lib/libc-2.11.1.so
0039a000-0039d000 rw-p 00000000 00:00 0 
0039d000-0039e000 r-xp 00000000 08:03 576385     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/build/sage/libs/flint/flint.so
0039e000-0039f000 rw-p 00001000 08:03 576385     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/build/sage/libs/flint/flint.so
0039f000-003a2000 r-xp 00000000 08:03 414002     /lib/libdl-2.11.1.so
003a2000-003a3000 r--p 00002000 08:03 414002     /lib/libdl-2.11.1.so
003a3000-003a4000 rw-p 00003000 08:03 414002     /lib/libdl-2.11.1.so
003a6000-003bc000 r-xp 00000000 08:03 413981     /lib/libpthread-2.11.1.so
003bc000-003bd000 r--p 00015000 08:03 413981     /lib/libpthread-2.11.1.so
003bd000-003be000 rw-p 00016000 08:03 413981     /lib/libpthread-2.11.1.so
003be000-003c0000 rw-p 00000000 00:00 0 
003c2000-003ea000 r-xp 00000000 08:03 413990     /lib/libm-2.11.1.so
003ea000-003eb000 r--p 00027000 08:03 413990     /lib/libm-2.11.1.so
003eb000-003ec000 rw-p 00028000 08:03 413990     /lib/libm-2.11.1.so
003ec000-003ed000 r-xp 00000000 08:03 162562     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_weakref.so
003ed000-003ee000 rw-p 00000000 08:03 162562     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_weakref.so
003ee000-003f5000 r-xp 00000000 08:03 162561     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/itertools.so
003f5000-003f8000 rw-p 00006000 08:03 162561     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/itertools.so
003f8000-00408000 r-xp 00000000 08:03 162526     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/cPickle.so
00408000-00409000 rw-p 0000f000 08:03 162526     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/cPickle.so
00409000-00420000 r-xp 00000000 08:03 162507     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/bz2.so
00420000-00423000 rw-p 00016000 08:03 162507     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/bz2.so
00423000-00452000 r-xp 00000000 08:03 416038     /lib/libncursesw.so.5.7
00452000-00453000 rw-p 0002f000 08:03 416038     /lib/libncursesw.so.5.7
00453000-00456000 r-xp 00000000 08:03 162518     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/termios.so
00456000-00458000 rw-p 00002000 08:03 162518     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/termios.so
00458000-0045b000 r-xp 00000000 08:03 162540     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/readline.so
0045b000-0045d000 rw-p 00002000 08:03 162540     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/readline.so
0045d000-00474000 r-xp 00000000 08:03 162519     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_ctypes.so
00474000-00477000 rw-p 00016000 08:03 162519     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_ctypes.so
00477000-0047a000 r-xp 00000000 08:03 162567     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_lsprof.so
0047a000-0047b000 rw-p 00002000 08:03 162567     /home/erik/src/sage-4.3.3.alpha1/local/lib/python2.6/lib-dynload/_lsprof.so
0047b000-00481000 r-xp 00000000 08:03 584404     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/build/sage/structure/parent_base.so
00481000-00482000 rw-p 00006000 08:03 584404     /home/erik/src/sage-4.3.3.alpha1/devel/sage-main/build/sage/structure/parent_base.soA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
	 [40.5 s]

```



---

Comment by zimmerma created at 2010-02-23 15:42:10

This problem is still present with 4.3.3. I have put on http://www.loria.fr/~zimmerma/sage-t.log.4.3.3 the log of `sage -t *`, and in http://www.loria.fr/~zimmerma/install.log.4.3.3.bz2
the install log.


---

Comment by zimmerma created at 2010-02-23 15:42:10

Changing assignee from GeorgSWeber to zimmerma.


---

Comment by zimmerma created at 2010-02-27 23:15:01

With sage-4.3.3 I've isolated the problem in `finite_field_morphism.py` to:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: H = Hom(GF(32, 'a'), GF(1024, 'b'))
sage: H[1]
Ring morphism:
  From: Finite Field in a of size 2^5
  To:   Finite Field in b of size 2^10
  Defn: a |--> b^7 + b^5
sage: quit
Exiting SAGE (CPU time 0m0.54s, Wall time 0m7.06s).
/usr/local/sage-4.3.3/sage/local/bin/sage-sage: line 206:  4274 Segmentation fault      (core dumped) sage-ipython "$@" -i
```

(Note the problem does not happen during the Sage session, but only when we quit Sage and it
tries to free the memory.) The run of `sage -memcheck` with that session is available on
http://www.loria.fr/~zimmerma/sage-memcheck.4232.
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
Note: I could not try `sage -memcheck` on sage.math since it did quit immediately, with the
following in the sage.memcheck file:

```
==29083== FATAL: can't open suppressions file '/usr/local/sage/local/lib/valgrind/sage.supp'
```

It seems the directory `/usr/local/sage/local/lib/valgrind` is missing, and the file
`sage.supp` in it (for my test above on my laptop, I did create an empty sage.supp file).


---

Comment by GokhanSever created at 2010-03-03 21:30:16

I don't have these two lines failing on v4.3.3 comparing to my 4.3.2.alpha0 tests:

Using ./sage -testall

	sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx"

	sage -t  "devel/sage/sage/libs/cremona/newforms.pyx"


```
uname -a
Linux ccn 2.6.31.9-174.fc12.i686.PAE #1 SMP Mon Dec 21 06:04:56 UTC 2009 i686 i686 i386 GNU/Linux
```



---

Comment by zimmerma created at 2010-03-05 20:20:56

Changing priority from minor to major.


---

Comment by zimmerma created at 2010-03-05 20:20:56

thanks to Robert Bradshaw, I was able to isolate the following test case:

```
H = Hom(GF(32, 'a'), GF(1024, 'b'))
D = H.domain()
C = H.codomain()
f = D.modulus()
g = C['x'](f)
r = g.roots()
r = [r[0]]
print r[0][0]
v = D.hom(r[0][0], C)
quit
```

where the Segfault does not occur without the last instruction `v = D.hom(r[0][0], C)`.
Now D.hom is a builtin with Givaro...


---

Comment by zimmerma created at 2010-03-06 09:44:04

Note: I'm ready to do more investigation if someone tells me what to do...


---

Comment by roed created at 2010-03-06 14:04:39

I don't have time to look at this this weekend, but only note that GF(32) and GF(1024) are `FiniteField_ntl_gf2e` objects.  Does the same problem happen with Givaro?  If not, maybe it's a problem restoring the NTL context; I already found one such bug in `finite_field_ntl_gf2e`.


---

Comment by zimmerma created at 2010-03-06 20:15:07

David,

> but only note that GF(32) and GF(1024) are FiniteField_ntl_gf2e objects

are you sure? I get:

```
sage: R=GF(32,'a')
sage: parent(R)
<type 'sage.rings.finite_field_givaro.FiniteField_givaro'>
```

Is there a way to force GF() to use Givaro or Ntl?


---

Comment by roed created at 2010-03-07 16:12:00

Ah, you're right.  You should be able to use the `impl` keyword to `GF` to get other implementations.

I don't know what's going on if it's givaro.


---

Comment by zimmerma created at 2010-03-07 18:31:06

> You should be able to use the impl keyword to GF to get other implementations. 

I wasn't able to find how to use the `impl` keyword, but with the following it works:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 7993
sage: F = sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e
sage: H = Hom(F(32, 'a'), F(1024, 'b'))
sage: D = H.domain()
sage: C = H.codomain()
sage: f = D.modulus()
sage: g = C['x'](f)
sage: r = g.roots()
sage: r = [r[0]]
sage: print r[0][0]
b^4 + b^3 + b
sage: D.hom(r[0][0], C)
Ring morphism:
  From: Finite Field in a of size 2^5
  To:   Finite Field in b of size 2^10
  Defn: a |--> b^4 + b^3 + b
sage: quit
Exiting SAGE (CPU time 0m0.25s, Wall time 0m3.09s).
[zimmerma@coing ~]$
```

No SegFault occurs with NTL, which shows the problem is linked with Givaro.


---

Comment by zimmerma created at 2010-03-07 19:05:53

I tried again the 22 tests which did produce a Segfault, by changing zech_log_bound from 2<sup>16</sup> to
2 in rings/finite_field.py, thus disabling Givaro for extension fields. I get no Segfault any more.
However, 9 of the 22 tests do fail, for example:

```
[zimmerma@coing sage]$ sage -t matrix/matrix_space.py
sage -t  "devel/sage-7773/sage/matrix/matrix_space.py"      
**********************************************************************
File "/usr/local/sage-4.3.3/sage/devel/sage-7773/sage/matrix/matrix_space.py", line 1222:
    sage: Mat(GF(9,'a'),3,sparse=True).random_element()
Expected:
    [    2*a       a       1]
    [      2       1 2*a + 1]
    [      a       2       2]
Got:
    [  a + 2 2*a + 1       a]
    [2*a + 2     2*a       0]
    [      0     2*a       0]
```

I'm not sure we can doctest the result of the `random_element` method.
In other words, is it normal that some tests do fail if one changes `zech_log_bound`?
Should I open a separate ticket for this?


---

Comment by zimmerma created at 2010-04-20 11:24:51

Changing assignee from zimmerma to GeorgSWeber.


---

Comment by zimmerma created at 2010-04-20 11:24:51

With sage 4.3.5, this problem is still there:

```
sage -t  groups/generic.py # Killed/crashed
sage -t  coding/code_constructions.py # Killed/crashed
sage -t  matrix/matrix_sparse.pyx # Killed/crashed
sage -t  coding/linear_code.py # Killed/crashed
sage -t  matrix/matrix_space.py # Killed/crashed
sage -t  modular/ssmod/ssmod.py # Killed/crashed
sage -t  modular/modform/ambient.py # Killed/crashed
sage -t  modular/modsym/space.py # Killed/crashed
sage -t  modules/free_module.py # Killed/crashed
sage -t  matrix/matrix2.pyx # Killed/crashed
sage -t  rings/finite_field_morphism.py # Killed/crashed
sage -t  rings/finite_field_ntl_gf2e.pyx # Killed/crashed
sage -t  rings/finite_field_ext_pari.py # Killed/crashed
sage -t  rings/polynomial/polynomial_quotient_ring_element.py # Killed/crashed
sage -t  rings/number_field/number_field_rel.py # Killed/crashed
sage -t  schemes/hyperelliptic_curves/hyperelliptic_finite_field.py # Killed/crashed
sage -t  rings/number_field/number_field.py # Killed/crashed
sage -t  schemes/hyperelliptic_curves/hyperelliptic_generic.py # Killed/crashed
sage -t  tests/benchmark.py # Killed/crashed
sage -t  schemes/elliptic_curves/ell_point.py # Killed/crashed
sage -t  modular/modsym/modsym.py # File not found
```



---

Comment by jsp created at 2010-05-01 18:38:29

All this doctest failures went away for me with the release of sage-4.4.1.alpha3!!!!

Jaap


---

Comment by zimmerma created at 2010-05-02 09:25:14

Jaap,

> All this doctest failures went away for me with the release of sage-4.4.1.alpha3!!!! 

great! Did you still have those failures with 4.4? This shows that the culprit is Sage and not
Fedora 12, and it would be good to investigate which package is the culprit. What were the main
package upgrades in 4.4.1?

Paul


---

Comment by jsp created at 2010-05-02 12:29:54

Replying to [comment:18 zimmerma]:
> Jaap,
> 
> > All this doctest failures went away for me with the release of sage-4.4.1.alpha3!!!! 
> 
> great! Did you still have those failures with 4.4? This shows that the culprit is Sage and not
> Fedora 12, and it would be good to investigate which package is the culprit. What were the main
> package upgrades in 4.4.1?
> 

The failures were still there in sage-4.4.1.alpha0. I'll try alpha1.

sage-4.4.1.alpha2 failed to build.

Jaap


> Paul


---

Comment by jsp created at 2010-05-02 15:10:24

Paul,

sage-4.4.1.alpha1 was a mess on Fedora 12.

In sage-4.4.1.rc0 all test passed.

Jaap


---

Comment by zimmerma created at 2010-05-02 15:31:38

Jaap,

> sage-4.4.1.alpha1 was a mess on Fedora 12. 
> In sage-4.4.1.rc0 all test passed. 

thus the problem disappeared between both. Can you guess from the Changelog which package might
be the culprit? I would guess it is a basic package like Pari/GP.

Paul


---

Comment by zimmerma created at 2013-01-08 08:48:06

should we close this ticket?

Paul


---

Comment by zimmerma created at 2013-01-08 08:48:06

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-01-12 21:58:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-17 10:06:00

Resolution: worksforme
