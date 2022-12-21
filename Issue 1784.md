# Issue 1784: number field doctest failure

Issue created by migration from Trac.

Original creator: pdenapo

Original creation time: 2008-01-15 19:10:16

Assignee: was

A doctest failure in sage-2.9.3

./sage -t ./devel/sage-main/sage/rings/number_field/number_field.py
sage -t  devel/sage-main/sage/rings/number_field/number_field.py**********************************************************************
File "number_field.py", line 2042:
    sage: Z(-1)
Expected:
    0.0333333333333333
Got:
    0
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_58
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field.py
         [90.3 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/rings/number_field/number_field.py
Total time for all tests: 90.3 seconds

The failed test is the following:




---

Comment by pdenapo created at 2008-01-15 19:11:15

Changing component from algebraic geometry to number theory.


---

Comment by mabshoff created at 2008-01-15 19:18:04

I cannot reproduce this. So could you supply more information, i.e. compiler used, operating system and so on. What seems strange is that it took 90 seconds to get to a failure. on sage.math the whole doctest takes 20 second.

Please also assign a milestone to all your tickets. In case of doctest failures it should be always the next release.

Cheers,

Michael


---

Comment by was created at 2008-01-15 19:26:04

This is very very suspicious.  I can't replicate it anywhere either.

The doctest in question is running a stand-alone PARI program to compute the special value of a zeta function at -1.  I think the answer should be 0.03333... as claimed.  Hmmm...   As you say, we need to know if the problem is reproducible from the command line, what computer, etc.,


---

Comment by mabshoff created at 2008-01-15 19:29:16

Hmm, any chance your improved pari.spkg from #258 is involved here?

Cheers,

Michael


---

Comment by pdenapo created at 2008-01-19 22:12:53

Resolution: invalid


---

Comment by pdenapo created at 2008-01-19 22:12:53

May be you are right about some problem with my own version of
pari in #258, I could not reproduce the bug in a fresh install
of sage-2.9.3

I'll check further...
