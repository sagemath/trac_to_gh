# Issue 8819: warnings in building documentation of Sage 4.4.1.alpha2

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-29 08:26:34

Assignee: mvngu

Building the documentation of Sage 4.4.1.alpha2 results in the following warnings in the reference manual:

```
docstring of sage.calculus.interpolators.CCSpline.derivative:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.calculus.interpolators.CCSpline.value:6: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.calculus.interpolators.PSpline.derivative:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
docstring of sage.calculus.interpolators.PSpline.value:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.1.alpha2/local/lib/python2.6/site-packages/sage/modular/modsym/space.py:docstring of sage.modular.modsym.space.ModularSymbolsSpace.abvarquo_rational_cuspidal_subgroup:13: (WARNING/2) Literal block expected; none found.
```



---

Comment by mvngu created at 2010-04-29 09:02:55

Changing status from new to needs_review.


---

Attachment

based on Sage 4.4.1.alpha2


---

Comment by mvngu created at 2010-05-03 00:04:18

Changing priority from blocker to minor.


---

Comment by cremona created at 2010-05-11 15:25:22

Patch applies fine to 4.4.2.alpha0.  docbuild reference html produced no warnings or errors.  The html files which are changed look ok (not perfect, e.g. some more math markup would be nice, but that is not the issue here).

Hence positive review.


---

Comment by cremona created at 2010-05-11 15:25:22

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-12 22:46:28

Resolution: fixed
