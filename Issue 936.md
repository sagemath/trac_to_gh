# Issue 936: doctest optional doctests

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-20 03:04:59

Assignee: failure

Do 

   sage -t --optional SAGE_ROOT/devel/sage

and fix the numerous problems.  This requires a Sage install with all optional packages installed,
and maple,mathematica,matlab,reduce,etc., all installed.  (I.e., sage.math.)


---

Comment by was created at 2007-10-20 03:14:59

See the file

```
   /home/was/d/sage/optional.txt
```

on sage.math


---

Comment by mhansen created at 2007-10-20 04:34:14

fixed issued in permgroup.py


---

Attachment

The errors in lie.py come from the new coercion model:


```
sage: a = lie('2')
sage: 2*a
Exception exceptions.RuntimeError: RuntimeError('An error occured running a LiE command:\nIdentifier sage5 is not defined. \n(in <)',) in 'parent._unregister_pair' ignored
Exception exceptions.RuntimeError: RuntimeError('An error occured running a LiE command:\nIdentifier sage5 is not defined. \n(in <)',) in 'parent._unregister_pair' ignored
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/mhansen/sage/devel/sage-main/sage/geometry/<ipython console> in <module>()

/home/mhansen/sage/devel/sage-main/sage/geometry/element.pyx in element.RingElement.__mul__()

/home/mhansen/sage/devel/sage-main/sage/geometry/coerce.pyx in coerce.CoercionModel_cache_maps.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Integer Ring' and 'LiE Interpreter'
sage: b = lie('2')
sage: a*b
4
```



---

Comment by mhansen created at 2007-10-20 04:58:07

All tests pass for me on polytope.py after running 'polymake --reconfigure'


---

Comment by mhansen created at 2007-10-20 05:04:52

I attached a patch to fix one of the issues with matlab.  The other one is due to the new coercion model:


```
File "matlab.py", line 38:
    sage: avg = (a+b+c)/3                    # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mhansen/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[8]>", line 1, in <module>
        avg = (a+b+c)/Integer(3)                    # optional###line 38:
    sage: avg = (a+b+c)/3                    # optional
      File "element.pyx", line 1486, in element.RingElement.__div__
      File "coerce.pyx", line 271, in coerce.CoercionModel_cache_maps.bin_op_c
    TypeError: unsupported operand parent(s) for '/': 'Matlab' and 'Integer Ring'

```



---

Attachment


---

Comment by mhansen created at 2007-10-20 05:24:41

Patch added for errors in kash.py


---

Attachment

Added patch for error in remote_file.py .  It's an error in the URL.  The file in question should be moved to a more permanent spot.


---

Attachment

Attached patch for number_field.py


---

Attachment


---

Comment by mhansen created at 2007-10-20 06:22:13

Regarding lseries_ell.py,

It requires that the following commands are run first:

```
sage: sympow('-new_data 2')
sage: sympow('-new_data 1d0')
sage: sympow('-new_data 1d1')
sage: sympow('-new_data 1d2')
```


After that, these are the following errors:


```
**********************************************************************
File "lseries_ell.py", line 158:
    sage: RR(a)                      # optional
Expected:
    2.4922620442736498
Got:
    2.49226204427365
**********************************************************************
File "lseries_ell.py", line 184:
    sage: E.Lseries().sympow_derivs(1,16,2)      # optional -- requires precomputing "sympow('-new_data 2')"
Expected:
    1n0: 3.837774351482055E-01
    1w0: 3.777214305638848E-01
    1n1: 3.059997738340522E-01
    1w1: 3.059997738340524E-01
    1n2: 1.519054910249753E-01
    1w2: 1.545605024269432E-01
Got:
    'sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details\nMinimal model of curve  is [0,0,1,-1,0]\nAt 37: Inertia Group is  C1 MULTIPLICATIVE REDUCTION\nConductor is 37\nsp 1: Conductor at 37 is 1+0, root number is 1\nsp 1: Euler factor at 37 is 1+1*x\n1st sym power conductor is 37, global root number is -1\nNT 1d0: 35\nNT 1d1: 32\nNT 1d2: 28\nMaximal number of terms is 35\nDone with small primes 1049\nComputed:  1d0  1d1  1d2 \nChecked out:  1d1 \n 1n0: 3.837774351482055E-01\n 1w0: 3.777214305638848E-01\n 1n1: 3.059997738340522E-01\n 1w1: 3.059997738340524E-01\n 1n2: 1.519054910249753E-01\n 1w2: 1.545605024269432E-01'
```



---

Comment by mhansen created at 2007-10-20 19:31:19

Problems with the lie interface fixed -- patch attached.


---

Attachment


---

Comment by mhansen created at 2007-10-20 19:50:40

Recap of errors from /home/was/d/sage/optional.txt

* *functions/functions.py*: passes once Octave is installed

* *functions/constants.py*: one error related to precision once Octave is installed

```
**********************************************************************
File "constants.py", line 870:
    sage: m.N(200)                                 # optional
Expected:
    2.6854520010653064453097148354817956938203822939944629530511523455572188595371520028011411749318476979951534659052880900828976777164109630517925334832596683818523154213321194996260393285220448194096181                
Got:
    2.685452001065306445309714835481795693820382293994462953051152345557218859537152002801141174931847697995153465905288090082897677716410963051792533483259668381852315421332119499626039328522044819409618068664166428930847788062036073705
```


* *geometry/polytope.py*: passes once 'polymake --reconfigure' is run

* *groups/perm_gps/permgroup.py*: passes once above patch is applied

* *interfaces/lie.py*: passes once above patch is applied

* *interfaces/axiom.py*: cannot install the new axiom spkg to test

* *interfaces/kash.py*: passes once the above patch is applied

* *misc/remote_file.py*: passes once the above patch is applied

* *rings/polynomial/multi_polynomial_ideal.py*: I just get a timeout error. I tried running some of the failed tests manually, and they all looked good.

* *rings/polynomial/multi_polynomial_libsingular.pyx*: should work once 'polymake --reconfigure' is run

* *rings/number_field/number_field.py*: passes once the above patch is applied

* *schemes/elliptic_curves/ec_database.py*: passes once the new elliptic curve database package is installed

* *schemes/elliptic_curves/lseries_ell.py*: see above comment for current status


---

Comment by was created at 2007-10-20 23:38:37

Resolution: fixed
