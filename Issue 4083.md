# Issue 4083: sage.finance - Options pricing implementation

Issue created by migration from https://trac.sagemath.org/ticket/4083

Original creator: cswiercz

Original creation time: 2008-09-09 02:16:17

Assignee: was

CC:  cswiercz software@pacificafog.com slelievre

Keywords: finance, options, black-scholes

Includes capabilities for options pricing using the Black-Scholes model. The primary class of this ticket is finance.Option, which uses finance.Stock.


---

Attachment

Initial implementation of the Option class.


---

Comment by cswiercz created at 2008-09-16 22:40:55

Changing status from new to assigned.


---

Comment by cswiercz created at 2008-09-16 22:40:55

Changing assignee from was to cswiercz.


---

Comment by was created at 2008-11-28 03:11:22

REFEREE:

This code is *really* good, and I definitely want it in Sage.  There are a bunch of minor issues that need to be fixed. 

1. A bunch of doctests fail when run on OSX 10.5 32-bit, which is maybe numerical noise:

```
teragon-2:finance wstein$ sage -t black_scholes.py 
sage -t  devel/sage-main/sage/finance/black_scholes.py      **********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 43:
    sage: tenyr_swap.Black(5, 1.2, 0.25, 'n')
Expected:
    0.0679829347644
Got:
    0.067982934764359987
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 333:
    sage: opt.Black(5, 1.2, 0.25, 'ln')
Expected:
    1.38685477149
Got:
    1.3868547714858503
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 335:
    sage: opt._bs_ln()
Expected:
    1.38685477149
Got:
    1.3868547714858503
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 272:
    sage: aapl_200c.Black(175, 0.4, 0.5, 'ln')
Expected:
    10.8744664878
Got:
    10.874466487776381
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 318:
    sage: opt.Black(5, 1.2, 0.25, 'n')
Expected:
    0.567982934764
Got:
    0.5679829347643599
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/finance/black_scholes.py", line 320:
    sage: opt._bs_n()
Expected:
    0.567982934764
Got:
    0.5679829347643599
**********************************************************************
4 items had failures:
   1 of   7 in __main__.example_1
   2 of   5 in __main__.example_10
   1 of   4 in __main__.example_8
   2 of   5 in __main__.example_9
***Test Failed*** 6 failures.
For whitespace errors, see the file /Users/wstein/sage/tmp/.doctest_black_scholes.py
	 [13.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage-main/sage/finance/black_scholes.py
Total time for all tests: 13.8 seconds
teragon-2:finance wstein$ 
```


2. There are three convenience functions with no doctests, which breaks the 100% coverage rule:

```
def n(x):       return scipy.stats.norm.pdf(float(x))
def N(x):       return scipy.stats.norm.cdf(float(x))
def invNorm(x): return scipy.stats.norm.ppf(float(x), loc=0, scale=1)
```

In fact the coverage score isn't very good:

```
teragon-2:finance wstein$ sage -coverage black_scholes.py 
----------------------------------------------------------------------
black_scholes.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE black_scholes.py: 50% (9 of 18)

Missing documentation:
	 * n(x):
	 * N(x):
	 * invNorm(x):
	 * _fullalpha(self, cps):
	 * _alpha(self):
	 * _beta(self):
	 * _ratio(self):
	 * _d1(self):
	 * _d2(self):
```


3. There is an empty TESTS: block at the top of the file.  (Just delete it.)

4. There are several instances of % in docstrings, which will confuse latex.  I'm not sure if this matters, since we're switching to Sphinx. 

5. I see the text "Funciton call is inherent:" in the __init__ method.  It has typos and makes no sense.

6. Change things like this in docstrings

```
# optional -- requires internet and random
```

to

```
# random; optional -- internet
```

This will work using the new -only_optional doctesting framework, which allows us to test only particular components (e.g., those that require the internet).


---

Comment by psinis created at 2009-02-23 22:17:37

Changing assignee from cswiercz to psinis.


---

Comment by psinis created at 2009-02-23 22:17:37

Changing status from assigned to new.


---

Comment by chapoton created at 2013-09-08 08:23:29

See #14671


---

Comment by mkoeppe created at 2021-10-10 20:30:02

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2021-10-10 20:30:02

outdated after sage.finance deprecation in #32427


---

Comment by slelievre created at 2021-10-25 10:59:04

Changing status from needs_review to positive_review.


---

Comment by slelievre created at 2021-10-25 10:59:04

Ok.


---

Comment by mkoeppe created at 2021-10-25 15:39:21

Resolution: invalid
