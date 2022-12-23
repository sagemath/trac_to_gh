# Issue 7064: fix warnings when building reference manual in Sage 4.1.2.alpha4

Issue created by migration from https://trac.sagemath.org/ticket/7064

Original creator: mvngu

Original creation time: 2009-09-29 06:30:40

Assignee: tba

CC:  malb polybori

On a fresh compiled Sage 4.1.2.alpha4, building the HTML version of the reference manual resulted in the following warnings:

```
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/numerical/knapsack.py:docstring of sage.numerical.knapsack.knapsack:69: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.MonomialFactory:1: (WARNING/2) Inline literal start-string without end-string.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.PolynomialFactory:1: (WARNING/2) Inline literal start-string without end-string.
WARNING: /scratch/mvngu/release/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage/rings/polynomial/pbori.so:docstring of sage.rings.polynomial.pbori.VariableFactory:1: (WARNING/2) Inline literal start-string without end-string.
```

This should be fixed before releasing the upcoming rc0. I have made this ticket a blocker for 4.1.2. The HTML version of the reference manual should build without any warnings.


---

Comment by mvngu created at 2009-09-29 09:06:55

based on Sage 4.1.2.alpha4


---

Attachment


---

Comment by mvngu created at 2009-09-30 03:55:16

Resolution: fixed
