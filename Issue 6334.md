# Issue 6334: optional doctest failure -- broken finance doctest failures

Issue created by migration from https://trac.sagemath.org/ticket/6334

Original creator: was

Original creation time: 2009-06-16 15:16:52

Assignee: tbd

CC:  cswiercz


```
sage -t -long --optional devel/sage/sage/finance/stock.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/finance/stock.py", line 180:
    sage: finance.Stock('vmw').google()[:5]   # optional -- internet
Expected:
    [
     28-Nov-07 80.57 88.49 80.57 87.69    7496000,
     29-Nov-07 90.91 93.20 89.50 90.85    5497600,
     30-Nov-07 95.39 95.60 89.85 91.37    4750200,
      3-Dec-07 89.87 96.00 88.70 94.97    4401100,
      4-Dec-07 92.26 97.10 92.05 95.08    2896600
    ]
Got:
    [
     16-Jun-08 66.00 67.50 65.60 67.47    1742000,
     17-Jun-08 67.84 67.84 66.03 67.00    1196900,
     18-Jun-08 66.50 66.56 64.76 66.19    1186400,
     19-Jun-08 65.92 66.50 64.69 65.72     549200,
     20-Jun-08 65.72 65.72 63.12 63.86    1242300
    ]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_9
***Test Failed*** 1 failures.
```



---

Comment by cswiercz created at 2009-06-16 15:44:25

Changing assignee from tbd to cswiercz.


---

Attachment

I also updated stock.py's documentation for Sphinx formatting.


---

Comment by cswiercz created at 2009-06-16 22:18:20

Changing keywords from "" to "finance, stock".


---

Comment by rbeezer created at 2009-07-17 04:00:53

1.  I still get 12 optional doctest failures, it looks like the requested dates are not being honored, but I haven't deduced a pattern to it.  Full output in attached text file.

2.  Documentation can be built with a lot fewer blank lines, especially inbetween list elements.  Reviewer patch illustrates this and corrects one misspelled word.

3.  I couldn't test the documentation since it doesn't seem to get pulled into the reference manual.  Should it be included?  If not, how should it be tested?


---

Comment by rbeezer created at 2009-07-17 04:01:49

sage -t -optional   output on  stock.py


---

Attachment


---

Comment by burcin created at 2013-01-11 11:05:51

Changing status from needs_work to needs_review.


---

Attachment

It looks like Minh fixed the documentation in `sage/finance` with [attachment:trac_9218-reviewer.patch:ticket:9218].

There is also #13884 to fix the optional doctests, where Karl-Dieter posted a patch.

Shall we close this ticket as duplicate?


---

Comment by ncohen created at 2013-12-25 13:29:12

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2013-12-25 13:29:31

Changing status from needs_info to positive_review.


---

Comment by vbraun created at 2014-01-04 04:23:19

Resolution: duplicate
