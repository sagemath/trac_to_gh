# Issue 9789: corrections and ideas for enhancements of the Sage tutorial

Issue created by migration from https://trac.sagemath.org/ticket/9790

Original creator: phil

Original creation time: 2010-08-24 00:42:02

Assignee: mvngu

Here are some some questions and comments regarding the Sage tutorial.

1. in tour_algebra.rst "x_{i} is the displacement from equilibrium of mass i, " should it be
of mass "m_{i}" ?

2. in tour_algebra.rst:  "Several orthogonal polynomials and special functions are implemented, using both PARI [GAP]"
  the reference should be [GP]

3. In tour_plotting.rst: "In both the notebook and the REPL, ..."
What is "REPL"?

4. Also, it would be nice to include the actual plot in tour_plotting.rst

5.  In tour_numtheory.rst The sentence "Much work has been done
implementing rings of integers in (...) p-adic fields or number fields
other than . " is not complete


---

Comment by phil created at 2010-08-24 23:49:06

7. in tour_help.rst: I don't think there is any information in the statement "a line is in most cases ended by a newline"

8. in tour_help.rst: Much of the content of this file does not really fit to the section heding "Getting Help".

9. in programmin.rst the ending } in "and replacing e.g., R.2 by R.gen(2)}" should be deleted


---

Comment by phil created at 2010-08-27 23:18:19

10. in tour_polynomial.rst "so you cannot use it to enter a polynomial (such as :math:`t^2+1`) belonging to ``R``." 

I don't understand what is meant by "belonging to ``R``".


---

Comment by phil created at 2010-08-27 23:31:54

Replying to [comment:2 phil]:
i'm stupid. please ignore 10. ;)


---

Comment by phil created at 2010-08-30 00:08:29

11. in programming.rst:
"
    sage: d = {2:4, 3:9, 4:16}
    sage: [a*b for a, b in d.iteritems()]
    [8, 27, 64]

A dictionary is unordered, as the last output illustrates."

- Why does the last output illustrate this?


---

Comment by phil created at 2010-10-04 20:20:49

12. in interfaces.rst:
in the end of the file,  writing "(do not type the ...)" one time is enough.
(the reader should not be considered stupid)

13. in programming.rst:
"Iterators are a recent addition to Python " *recent* means Python 2.2 which was release in 2002. It would be better to write: "Since version 2.2, iterators are a part of Python. ...


---

Comment by phil created at 2010-10-04 20:20:57

Changing status from new to needs_work.


---

Comment by phil created at 2010-10-05 14:38:59

14. in the pdf version there is an empty chapter ten called bibliography in addition to the proper bibliography.


---

Comment by phil created at 2010-10-06 01:11:42

15. in appendex.rst:
"table in § 5.14" should now be "table in § 5.15".


---

Comment by phil created at 2010-10-09 00:51:14

16. in tour_algebra.rst
    "sage: bessel_I(2,1.1,"maxima")  # last few digits are random
    0.16708949925104899"

why are the last few digits random? how can I tell?


---

Comment by mmezzarobba created at 2015-01-28 15:49:59

See also #482.
