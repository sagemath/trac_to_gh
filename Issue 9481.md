# Issue 9481: random_element fails for power series over real field, has inaccurate docstring

Issue created by migration from Trac.

Original creator: niles

Original creation time: 2010-07-12 13:37:14

Assignee: malb

CC:  rishi

Keywords: power series, random element

The random_element method of univariate power series does not pass arguments to the underlying polynomial ring accurately, and the description of its second argument is inaccurate.

c.f. this [thread](http://groups.google.com/group/sage-devel/browse_thread/thread/2e4af4234e6bb33f) from sage-devel



```
sage: SQ = PowerSeriesRing(QQ,'v')
sage: SR = PowerSeriesRing(RR,'v')

sage: SQ.random_element(5,100)  # docstring promises coefficients are uniformly distributed between -100 and 100
-7/3 + 5/8*v + 37/60*v^2 + 33/8*v^3 + 77/89*v^4 + O(v^5)

sage: SR.random_element(5)  # broken
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
```



---

Comment by niles created at 2010-07-12 14:36:51

Changing priority from minor to major.


---

Comment by niles created at 2010-07-12 14:36:51

Changing status from new to needs_review.


---

Comment by niles created at 2010-08-01 16:27:25

emulated behavior of polynomial ring random_element, as suggested on sage-devel; commit message now references ticket number


---

Attachment


---

Comment by niles created at 2010-12-03 20:55:41

Changing keywords from "power series, random element" to "power series, random element, beginner".


---

Comment by aly.deines created at 2011-01-10 22:58:40

Changing status from needs_review to positive_review.


---

Comment by aly.deines created at 2011-01-10 22:58:40

Looks good.


---

Attachment

Same patch, fixed commit message


---

Comment by jdemeyer created at 2011-01-19 13:26:28

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-19 13:26:28

Docstring needs reformatting to proper Sphinx markup.


---

Comment by jdemeyer created at 2011-01-19 13:30:27

Apply on top of previous patch


---

Comment by jdemeyer created at 2011-01-19 13:30:47

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by niles created at 2011-01-19 13:39:42

Changing status from needs_review to positive_review.


---

Comment by niles created at 2011-01-19 13:39:42

All documentation now builds without error or warning, so positive review for [attachment:9481_docstring.patch]


---

Comment by jdemeyer created at 2011-01-19 22:21:23

Resolution: fixed
