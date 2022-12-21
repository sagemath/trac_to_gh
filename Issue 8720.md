# Issue 8720: CC and CDF do not display numeric 0

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-04-20 02:42:33

Assignee: AlexGhitza

CC:  zimmerma mhansen

Look at the inconsistency:


```
sage: RR(0)
0.000000000000000
sage: RDF(0)
0.0
```


versus


```
sage: CDF(0)
0
sage: CC(0)
0
```



---

Comment by jason created at 2010-04-20 03:02:18

I think CDF and CC should display the same output as RDF and RR, respectively.

CCing zimmerma since he may be interested in reviewing this.


---

Comment by zimmerma created at 2010-04-20 10:55:51

since I was asked to review this ticket, I first notice that some doctests do not pass any more,
for example:

```
sage -t  gsl/dft.py
**********************************************************************
File "/usr/local/sage-4.3.5-core2/devel/sage-8720/sage/gsl/dft.py", line 528:
    sage: t = s.fft(); t
Expected:
    Indexed sequence: [5.00000000000000, 0, 0, 0, 0]
     indexed by [0, 1, 2, 3, 4]
Got:
    Indexed sequence: [5.00000000000000, 0.000000000000000, 0.000000000000000, \
0.000000000000000, 0.000000000000000]
        indexed by [0, 1, 2, 3, 4]
```

thus some more work is needed. Please check all doctests still pass.


---

Comment by zimmerma created at 2010-04-20 10:55:51

Changing status from new to needs_work.


---

Comment by jason created at 2010-04-20 13:22:47

Thanks for looking at it.  When I ran the doctests, a number of them failed, so I posted to sage-devel and kept this ticket as "needs work".  I will set it to "needs review" when I've taken care of the failing doctests.

Thanks again.


---

Comment by mhansen created at 2011-12-18 16:01:48

I'm going to run the tests shortly and produce an doctest fixing patch.


---

Comment by mhansen created at 2011-12-18 23:29:43

I've attached a patch which should fix all of the doctests in 4.8.alpha4.


---

Comment by mhansen created at 2011-12-18 23:29:43

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2011-12-19 11:09:42

note that a consequence of that ticket is that coefficients 0 that were not displayed in Taylor
series are now displayed, for example:

```
sage: E = EllipticCurve('37a')
sage: L = E.lseries().dokchitser()
sage: L.taylor_series(1,4)
0.0000000000000 + 0.305999773834052*z + 0.186547797268162*z^2 - 0.136791463097188*z^3 + O(z^4)
```

(Before this ticket, the leading `0.000000000000000` was not printed.)

I find it good, since those 0.0 values can come from numerical cancellation.

Paul


---

Comment by zimmerma created at 2011-12-19 11:53:47

all tests work on top of Sage 4.7.2, I give a positive review.

Paul


---

Comment by kcrisman created at 2011-12-19 17:47:19

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-12-19 17:47:19

> all tests work on top of Sage 4.7.2, I give a positive review.
Just doing the radio button for this.  Nice teamwork on this!


---

Comment by jdemeyer created at 2011-12-23 16:26:37

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-12-23 16:26:37

A few more doctests need to be fixed:

```
sage -t  -force_lib devel/sage/sage/matrix/matrix2.pyx
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx", line 7987:
    sage: M.round(6).zero_at(10^-6)
Expected:
    [             -1.528503                      0                      0]
    [  0.459974 - 0.40061*I              -1.741233                      0]
    [-0.934304 + 0.148868*I   0.54833 + 0.073202*I              -0.550725]
Got:
    [             -1.528503                    0.0                    0.0]
    [  0.459974 - 0.40061*I              -1.741233                    0.0]
    [-0.934304 + 0.148868*I   0.54833 + 0.073202*I              -0.550725]
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx", line 7991:
    sage: (A - M*G).zero_at(10^-12)
Expected:
    [0 0 0]
    [0 0 0]
    [0 0 0]
Got:
    [0.0 0.0 0.0]
    [0.0 0.0 0.0]
    [0.0 0.0 0.0]
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha6/devel/sage-main/sage/matrix/matrix2.pyx", line 7995:
    sage: (G*G.conjugate().transpose()).zero_at(10^-12)
Expected:
    [1.0   0   0]
    [  0 1.0   0]
    [  0   0 1.0]
Got:
    [1.0 0.0 0.0]
    [0.0 1.0 0.0]
    [0.0 0.0 1.0]
**********************************************************************

```



---

Comment by zimmerma created at 2011-12-23 16:40:57

sorry, but there is no such doctest in 4.7.2. There must be some interaction with some
other patch which you included. My positive review was valid for 4.7.2 only.

Paul


---

Comment by kcrisman created at 2011-12-23 16:57:48

Replying to [comment:11 zimmerma]:
> sorry, but there is no such doctest in 4.7.2. There must be some interaction with some
> other patch which you included. My positive review was valid for 4.7.2 only.

Probably Jeroen is referring to doctests in the latest alpha, on which (for better or for worse) patches need to be based on.


---

Comment by jdemeyer created at 2012-02-07 22:30:58

** bump **


---

Comment by mhansen created at 2012-02-08 01:28:48

I posted a patch fixing these problems.


---

Comment by mhansen created at 2012-02-08 01:28:48

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2012-02-08 01:34:36

Note that the second patch applies with a little fuzz.

```
$ hg qpush
applying trac_8720-doctests.patch
patching file sage/matrix/matrix_double_dense.pyx
Hunk #1 succeeded at 189 with fuzz 2 (offset 9 lines).
now at: trac_8720-doctests.patch
```

I'll run tests and check.  I should have set `sage -b` to do parallel building


---

Comment by kcrisman created at 2012-02-08 02:16:44

{{[

Doctesting 1 file using 1 thread
sage -t  devel/sage-main/sage/matrix/matrix_double_dense.pyx
	 [19.7 s]
 
}}}

Now running full long doctests.


---

Comment by kcrisman created at 2012-02-08 03:24:28

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-02-08 03:24:28


```

$ ../../sage -tp 4 -long sage/lfunctions/lcalc.py 
Global iterations: 1
File iterations: 1
Using long cached timings to run longest doctests first.
Doctesting 1 file using 1 thread
sage -t -long devel/sage-main/sage/lfunctions/lcalc.py
  ***   Warning: new stack size = 1028976 (0.981 Mbytes).
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
  ***   Warning: new stack size = 1001472 (0.955 Mbytes).
**********************************************************************
File "/Users/.../sage-5.0.beta2/devel/sage-main/sage/lfunctions/lcalc.py", line 229:
    sage: E.lseries().values_along_line(0.5, 3, 5)
Expected:
    [(0.000000000, 0.209951303), (0.500000000, -2.92081722e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
Got:
    [(0.000000000, 0.209951303), (0.500000000, -2.92081723e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/.../.sage/tmp/new_host_2.home-37994/lcalc_37997.py
	 [3.0 s]
```

The difference was in the e-16 one. I think there is a reason that one used to be `-...e-16` in the old doctest.  I'm going to ignore the stack size warnings, since they don't seem to have affected the outcome, though I'm sure they're not ideal.

All else is fine!


---

Comment by jason created at 2012-02-08 03:39:57

Can you double-check to make sure that test was passing before the patches?  It seems odd to me that error would have been triggered by this patch.


---

Comment by kcrisman created at 2012-02-08 03:45:36

> Can you double-check to make sure that test was passing before the patches?  It seems odd to me that error would have been triggered by this patch.
Notice that the test now fails because we used to ignore all digits before the exponent, not because of the stack thing - the doc even points out that warnings might happen, it's no big deal for now.

```
        Sometimes warnings are printed (by lcalc) when this command is
        run::
        
            sage: E = EllipticCurve('389a')
            sage: E.lseries().values_along_line(0.5, 3, 5)
            [(0, 0.209951303),
             (0.500000000, -...e-16),
             (1.00000000, 0.133768433),
             (1.50000000, 0.360092864),
             (2.00000000, 0.552975867)]
```

Here is 5.0.beta1:

```
$ ./sage -t -long devel/sage/sage/lfunctions/lcalc.py 
sage -t -long "devel/sage/sage/lfunctions/lcalc.py"         
	 [20.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 20.5 seconds
<snip>
sage:             sage: E = EllipticCurve('389a')
sage:             sage: E.lseries().values_along_line(0.5, 3, 5)
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
[(0, 0.209951303), (0.500000000, -2.92081723e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
```

so we can see that all that has to be done is go back to the previous doctest for that one number (not even the whole list).


---

Comment by jason created at 2012-02-08 04:02:03

Ah, I understand.  Mike made this test much more rigid, and that is what is failing here.  Yeah, I agree with your conclusion, Karl-Dieter.


---

Comment by mhansen created at 2012-03-28 21:01:35

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2012-03-28 21:01:35

I've gone ahead and fixed that doctest.


---

Comment by davidloeffler created at 2012-03-29 17:14:18

I'm afraid that, according to the patchbot, this new patch works on latest release (4.8) but fails a doctest on 5.0.beta3, and doesn't even apply to 5.0.beta11.


---

Comment by davidloeffler created at 2012-03-29 17:14:18

Changing status from needs_review to needs_work.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2012-03-29 20:20:41

I've rebased the files on beta11.


---

Comment by mhansen created at 2012-03-29 20:20:41

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2012-03-30 07:33:03

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-30 07:33:03

The beta11 patchbot brings up some doctest failures:

```
The following tests failed:

	sage -t  -force_lib devel/sage-8720/sage/plot/hyperbolic_triangle.py # 2 doctests failed
	sage -t  -force_lib devel/sage-8720/sage/plot/hyperbolic_arc.py # 1 doctests failed
	sage -t  -force_lib devel/sage-8720/sage/matrix/matrix_space.py # 1 doctests failed
	sage -t  -force_lib devel/sage-8720/sage/matrix/constructor.py # 1 doctests failed
```



---

Attachment

apply this patch on top of the other three


---

Comment by zimmerma created at 2012-04-03 06:59:52

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2012-04-03 06:59:52

I have attached a patch for sage-5.0.beta11, which makes the 4 doctests from comment [comment:24] work. Note that the change in `matrix/constructor.py` seems to indicate it
was not working properly before this ticket. Please review.

Paul


---

Comment by zimmerma created at 2012-04-03 07:03:16

changed description for the patchbot.

Paul


---

Comment by kcrisman created at 2012-04-03 13:05:22

Seems to work fine on these files.  Running long doctests now but I don't anticipate any more problems.

As to constructor.py, the `-0.1` was removed in the first doctest patch, so the problem was in the test, not the behavior.


---

Comment by kcrisman created at 2012-04-03 16:13:39

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-04-19 06:43:48

Resolution: fixed
