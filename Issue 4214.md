# Issue 4214: elliptic_logarithm gives inaccurate answers

Issue created by migration from https://trac.sagemath.org/ticket/4214

Original creator: AlexGhitza

Original creation time: 2008-09-28 22:47:17

Assignee: tbd

It seems that our implementation of `elliptic_logarithm` performs much worse than Pari's `ellpointtoz`.  This is from an actual doctest in `ell_point.py`:


```
sage: E = EllipticCurve([1, 0, 1, -85357462, 303528987048]) #18074g1
sage: P = E([4458713781401/835903744, -64466909836503771/24167649046528, 1])
sage: P.elliptic_logarithm(precision=54)
NaN
sage: P.elliptic_logarithm(precision=55)
0.2735052671206336
sage: P.elliptic_logarithm()  # 100 bits
0.27656204014107100870070982517
```


Note that, while we ask for a precision of 55 bits (about 16 decimal digits), we seem to only get 2 accurate digits!  Compare this with the following `gp` session:


```
? \p 16                                           
   realprecision = 19 significant digits (16 digits displayed)
? e = ellinit([1, 0, 1, -85357462, 303528987048]);
? ellpointtoz(e, [4458713781401/835903744, -64466909836503771/24167649046528])
%6 = 0.2765620403
? \p 32                                                                       
   realprecision = 38 significant digits (32 digits displayed)
? e = ellinit([1, 0, 1, -85357462, 303528987048]);                            
? ellpointtoz(e, [4458713781401/835903744, -64466909836503771/24167649046528])
%8 = 0.27656204014107061464076203097
```


With the smaller precision, Pari knows that the result is not accurate to its current 16 displayed decimals, and prints only 10 of them (of which only the last is wrong).  We also see that Sage's result with 100 bits of precision has only 14 accurate decimals (less than half of what we asked for).

Possible solutions:

 1. add a flag `algorithm` to `elliptic_logarithm` and set it to "pari" by default; given the loss of precision that even Pari's more accurate algorithm seems to suffer, we might want to ask it to do the computations with slightly higher precision than we need

 2. find where Sage's algorithm loses so much precision and fix it

I tend towards doing 1 right now and working on 2.  


---

Comment by AlexGhitza created at 2008-09-28 22:49:31

Changing assignee from tbd to was.


---

Comment by AlexGhitza created at 2008-09-28 22:49:31

Changing component from algebra to number theory.


---

Comment by AlexGhitza created at 2008-10-01 11:43:23

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2008-10-01 11:43:23

The attached patch (based on 3.1.3.alpha2) implements solution 1 described above, in such a way that the result is very likely (if we trust Pari) to have the precision requested by the user.


---

Comment by GeorgSWeber created at 2008-10-09 19:27:00

Hi Alex,
unfortunately, the patch does not work yet. This is what I get before applying the patch:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha3/tmp/ell_point.py", line 1103:
    sage: P.elliptic_logarithm(precision=55)
Expected:
    0.2735052644156991
Got:
    0.2735052671206336
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha3/tmp/ell_point.py", line 1105:
    sage: P.elliptic_logarithm()  # 100 bits
Expected:
    0.27656204014107100870071052662
Got:
    0.27656204014107100870070982517
**********************************************************************
1 items had failures:
   2 of  20 in __main__.example_33
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/georgweber/Public/sage/sage-3.1.3.alpha3/tmp/.doctest_ell_point.py
         [35.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
Total time for all tests: 35.2 seconds
```


But after applying the patch (to vanilla Sage 3.1.3alpha3 on my Intel Mac OS X 10.4), I still get:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha3/tmp/ell_point.py", line 1120:
    sage: P.elliptic_logarithm(algorithm='sage')  # 100 bits
Expected:
    0.27656204014107100870071052662
Got:
    0.27656204014107100870070982517
**********************************************************************
1 items had failures:
   1 of  21 in __main__.example_33
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/georgweber/Public/sage/sage-3.1.3.alpha3/tmp/.doctest_ell_point.py
         [28.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
Total time for all tests: 28.4 seconds
```


Thus the patch got one failure away, but the other pertains.

Maybe just use dots for the time being (see the following line) there in the doctest,
as even these fewer digits already display what you want to show (accuracy problem
of the Sage internal algorithm)?


```
0.2765620401410710087...
```



---

Comment by AlexGhitza created at 2008-10-09 20:57:34

Ah yes.  I'll have some time to do this in a few hours.  I just realized that I probably should also test it on a 64-bit machine.


---

Comment by AlexGhitza created at 2008-10-10 02:11:28

OK, so I've replaced the patch with one that should take care of these problems.


---

Comment by mabshoff created at 2008-10-10 21:23:48

Well, it seems like whack-a-mole:

```
sage -t -long devel/sage/sage/libs/pari/gen.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/gen.py", line 4971:
    sage: e.ellpointtoz([0,0])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_175[3]>", line 1, in <module>
        e.ellpointtoz([Integer(0),Integer(0)])###line 4971:
    sage: e.ellpointtoz([0,0])
      File "gen.pyx", line 4958, in sage.libs.pari.gen.gen.ellpointtoz (sage/libs/pari/gen.c:18454)
    TypeError: function takes exactly 2 arguments (1 given)
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/gen.py", line 4975:
    sage: e.ellpointtoz([0])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_175[4]>", line 1, in <module>
        e.ellpointtoz([Integer(0)])###line 4975:
    sage: e.ellpointtoz([0])
      File "gen.pyx", line 4958, in sage.libs.pari.gen.gen.ellpointtoz (sage/libs/pari/gen.c:18454)
    TypeError: function takes exactly 2 arguments (1 given)
**********************************************************************
```


Cheers,

Michael


---

Attachment

Grrr.  Yes, I was careless (did I really not test gen.pyx?)

Anyway, it was just a matter of giving a default value to the parameter precision.  It's in the new patch.


---

Comment by mabshoff created at 2008-10-10 23:03:42

The patch now passes doctests - also in gen.pyx. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-10 23:03:59

Resolution: fixed


---

Comment by mabshoff created at 2008-10-10 23:03:59

Merged in Sage 3.1.3.rc0
