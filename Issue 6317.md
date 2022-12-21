# Issue 6317: optional doctest failure -- maple interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:46:05

Assignee: tbd

CC:  mkoeppe

Evidently the maple interface is even completely broken on sage.math right now!

```
sage -t -long --optional devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/calculus/calculus.py", line 479:
    sage: g = maple(f); g                             # optional -- requires maple
Expected:
    sin(x^2)+y^z
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/calculus/calculus.py", line 481:
    sage: g.integrate(x)                              # optional -- requires maple
Expected:
    1/2*2^(1/2)*Pi^(1/2)*FresnelS(2^(1/2)/Pi^(1/2)*x)+y^z*x
Got:
    read "/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399";
    read "/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399";
    read "/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399";
    sage2
**********************************************************************
1 items had failures:
   2 of  56 in __main__.example_1
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_calculus.py
	 [13.3 s]
```



---

Comment by was created at 2009-06-16 14:57:01

More doctest failures caused by the Maple interface being broken:

```
sage -t -long --optional devel/sage/sage/modules/free_module_element.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx", line 839:
    sage: maple(v)                                  #optional
Expected:
    Vector[row](4, [0,1,2,3])
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx", line 845:
    sage: maple(v)                                  #optional
Expected:
    Vector[row](3, [2/3,0,5/4])
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx", line 852:
    sage: maple(v)                                           #optional
Expected:
    Vector[row](3, [x^2+2,2*x+1,-2*x^2+4*x])
Got:
    <BLANKLINE>
**********************************************************************
1 items had failures:
   3 of   9 in __main__.example_22
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_free_module_element.py
	 [8.7 s]
```



---

Comment by was created at 2009-06-16 14:57:28

And more:

```
sage -t -long --optional devel/sage/sage/symbolic/constants.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/constants.py", line 51:
    sage: maple(pi)                   # optional
Expected:
    Pi
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/constants.py", line 1210:
    sage: m.N(200)                                 # optional
Expected:
    2.6854520010653064453097148354817956938203822939944629530511523455572188595371520028011411749318476979951534659052880900828976777164109630517925334832596683818523154213321194996260393285220448194096181                
Got:
    2.68545200106530644530971483548179569382038229399446295305115234555721885953715200280114117493184769799515346590528809008289767771641096305179253348325966838185231542133211949962603932852204481940961807
**********************************************************************
2 items had failures:
   1 of  58 in __main__.example_0
   1 of   5 in __main__.example_62
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_constants.py
	 [6.4 s]
```



---

Comment by was created at 2009-06-16 15:21:09

And of course there are many more failures, including a total hang:

```
sage -t -long --optional devel/sage/sage/interfaces/maple.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py", line 27:
    sage: maple('3 * 5')                                 # optional - maple
Expected:
    15
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py", line 29:
    sage: maple.eval('ifactor(2005)')                    # optional - maple
Expected:
    '"(5)*"(401)'
Got:
    ''
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py", line 31:
    sage: maple.ifactor(2005)                            # optional - maple
Expected:
    "(5)*"(401)
Got:
    <BLANKLINE>
... hundreds more...

```



---

Comment by chapoton created at 2015-09-16 12:38:32

Changing keywords from "" to "maple".


---

Comment by chapoton created at 2020-10-02 14:05:59

obsolete ?


---

Comment by chapoton created at 2022-10-08 07:33:02

Resolution: invalid


---

Comment by chapoton created at 2022-10-08 07:33:02

closing as very old and working now
