# Issue 8261: cygwin: mpfr fails 1 test in its test suite on windows

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-14 06:55:25

Assignee: tbd

Upon building mpfr-2.4.1.p1 on cygwin we get one test failure:

```
...
PASS: tprintf.exe
Error in mpfr_sprintf (s, "%'30Re", x);
expected: "      1,899347461279296875e+07"
got:      "      1.899347461279296875e+07"
FAIL: tsprintf.exe
PASS: tfprintf.exe
PASS: trec_sqrt.exe
PASS: tpow_all.exe
=====================
1 of 148 tests failed
```



---

Comment by mhansen created at 2010-02-16 21:24:56

This is the same issue here: http://permalink.gmane.org/gmane.comp.lib.mpfr.general/375

There is a patch posted there, but I have not tried it yet.


---

Comment by mhansen created at 2010-02-16 23:12:22

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-02-16 23:12:22

MPFR 2.4.2 has the fix posted in that thread.  I've made an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/mpfr-2.4.2.spkg

I'm building it now to test to see if it works.


---

Comment by mhansen created at 2010-02-17 00:43:17

I just check and all tests pass on Cygwin with MPFR 2.4.2.


---

Comment by mvngu created at 2010-03-03 23:43:31

Replying to [comment:3 mhansen]:
> I just check and all tests pass on Cygwin with MPFR 2.4.2.

I have verified this on winxp1 on boxen.math. The Sage 4.3.4.alpha0 build failed when trying to compile the gd spkg. That didn't prevent me from manually installing your upgraded MPFR spkg. First, I set these environment variables:

```
export SAGE_PORT=yes
export SAGE_CHECK=yes
```

Then I forced an installation with

```
./sage -f /URL/to/mpfr-2.4.2.spkg
```

The build went OK and the test suite of MPFR passed. I'll now test on t2.math and some other machines.


---

Comment by mvngu created at 2010-03-03 23:54:37

I qrefresh'd Mike's upgraded spkg to include the ticket number in the commit message and changelog. The resulting spkg can be found at

http://sage.math.washington.edu/home/mvngu/spkg/standard/mpfr/mpfr-2.4.2.spkg


---

Comment by mvngu created at 2010-03-06 08:13:51

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-06 08:13:51

The upgraded MPFR spkg builds on sage.math, t2.math, bsd.math, rosemary.math, and Cygwin (winxp1 on boxen.math). First, I set the environment variable

```
export SAGE_CHECK=yes
```

and forced a re-installation with

```
./sage -f /URL/or/path/to/mpfr-2.4.2.spkg
```

The build went OK and the test suite of MPFR passed without any reported failures.

*Note to release manager:* Use the package at

http://sage.math.washington.edu/home/mvngu/spkg/standard/mpfr/mpfr-2.4.2.spkg


---

Comment by mhansen created at 2010-03-06 08:18:20

Resolution: fixed
