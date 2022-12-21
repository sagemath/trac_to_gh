# Issue 4085: [with patch, needs review] high precision real literals

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-09 05:46:07

Assignee: jkantor

Before 


```
sage: RealField(256)(1.2)
1.199999999999999955591079014993738383054733276367187500000000000000000000000
```


After


```
sage: RealField(256)(1.2)
1.200000000000000000000000000000000000000000000000000000000000000000000000000
```


While I was in there I made several optimizations. 


---

Attachment


---

Comment by mhansen created at 2008-09-09 08:32:34

Technically, this looks good to me and it's definitely a change for the better.  There will be some doctest failures as Sage is now more accurate, but I'll let mabshoff test the tree, and then I can make the clean up patch.

We also have this nice behavior:

```
sage: ComplexField(200)(1.1,0.1)
1.1000000000000000000000000000000000000000000000000000000000 + 0.10000000000000000000000000000000000000000000000000000000000*I
```


Nice work Robert!


---

Comment by mabshoff created at 2008-09-09 09:38:22

Here we go:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx     
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/sage_object.py", line 57:
    sage: type(a)
Expected:
    <type 'sage.rings.real_mpfr.RealNumber'>
Got:
    <type 'sage.rings.real_mpfr.RealLiteral'>
**********************************************************************
1 items had failures:
   1 of  15 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_sage_object.py
	 [3.3 s]
exit code: 1024
 
sage -t -long devel/sage/sage/rings/real_rqdf.pyx           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/real_rqdf.py", line 24:
    sage: RQDF( 123.2) * RR (.543)
Expected:
    66.89760000000000624851281827432114309792736749325567465385058291
Got:
    66.89760000000000154329882207093760371208190917968750000000000000
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_real_rqdf.py
	 [2.8 s]
exit code: 1024
 
sage -t -long devel/sage/sage/rings/real_mpfr.pyx           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/real_mpfr.py", line 883:
    sage: (-3.1415)._pari_().python()
Expected:
    -3.14150000000000018
Got:
    -3.14150000000000000
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_28
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_real_mpfr.py
	 [8.3 s]
exit code: 1024
 

sage -t -long devel/sage/sage/rings/complex_double.pyx      
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/complex_double.py", line 960:
    sage: log(abs(ComplexField(200)(1.1,0.1)))
Expected:
    0.099425429372582675602989386713555936556752871164033127857198
Got:
    0.099425429372582595066319157757531449594489450091985182495705
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_52
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_complex_double.py
	 [4.6 s]
exit code: 1024
 

sage -t -long devel/sage/sage/rings/qqbar.py                    
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/qqbar.py", line 288:
    sage: rhs
Expected:
    2.642040335819351?e44
Got:
    2.64204033581936?e44
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/qqbar.py", line 290:
    sage: lhs - rhs
Expected:
    0.?e29
Got:
    0.?e30
**********************************************************************
1 items had failures:
   2 of 127 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_qqbar.py
	 [114.2 s]
exit code: 1024
 
sage -t -long devel/sage/sage/misc/functional.py            
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/functional.py", line 804:
    sage: type(real(a))
Expected:
    <type 'sage.rings.real_mpfr.RealNumber'>
Got:
    <type 'sage.rings.real_mpfr.RealLiteral'>
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_50
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_functional.py
	 [6.6 s]
exit code: 1024
 
sage -t -long devel/sage/sage/matrix/matrix0.pyx            
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/matrix0.py", line 532:
    sage: a[2.7]
Expected:
    Traceback (most recent call last):
    ...
    TypeError: 'sage.rings.real_mpfr.RealNumber' object cannot be interpreted as an index
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[12]>", line 1, in <module>
        a[RealNumber('2.7')]###line 532:
    sage: a[2.7]
      File "matrix0.pyx", line 707, in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:4109)
      File "matrix1.pyx", line 635, in sage.matrix.matrix1.Matrix.row (sage/matrix/matrix1.c:5406)
    TypeError: 'sage.rings.real_mpfr.RealLiteral' object cannot be interpreted as an index
**********************************************************************
1 items had failures:
   1 of  42 in __main__.example_21
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_matrix0.py
	 [3.1 s]
exit code: 1024
 
sage -t -long devel/sage/sage/libs/pari/gen.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/gen.py", line 4408:
    sage: e.elllseries(2.1)
Expected:
    0.4028380479566455155
Got:
    0.4028380479566454783
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/gen.py", line 4416:
    sage: e.elllseries(2.1, A=1.1)
Expected:
    0.402838047956645515...
Got:
    0.4028380479566454785
**********************************************************************
1 items had failures:
   2 of   7 in __main__.example_164
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.2.rc1/tmp/.doctest_gen.py
	 [57.5 s]
exit code: 1024
 }}}


---

Attachment


---

Comment by mabshoff created at 2008-09-13 02:44:03

Looks good, passes doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-13 02:44:18

Resolution: fixed


---

Comment by mabshoff created at 2008-09-13 02:44:18

Merged both patches in Sage 3.1.2.rc2
