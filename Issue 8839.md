# Issue 8839: comment in rating

Issue created by migration from https://trac.sagemath.org/ticket/8839

Original creator: aliajouz

Original creation time: 2010-05-01 23:59:25

Assignee: jason, was

Hello , 
html is ebabled in comment which allow to add iframe ,images ,etc ...

example 

http://alpha.sagenb.org/home/pub/1/rate?rating=4&comment=very%20good<br><br><img src="http://games.pcmasters.de/fileadmin/Games/Sport/TDU2/3.jpg">

thanks .


---

Comment by aliajouz created at 2010-05-02 00:05:02

Changing type from defect to enhancement.


---

Comment by aliajouz created at 2010-05-02 00:05:23

Changing assignee from jason, was to aliajouz.


---

Comment by kcrisman created at 2014-12-19 04:38:36

Changing type from enhancement to defect.


---

Comment by kcrisman created at 2014-12-19 04:38:36

Oh yeah, this is terrible!  Thank you for bringing this to our attention - definitely a security problem, though relatively minor since hardly anyone actually uses the ratings.

https://github.com/sagemath/sagenb/issues/318


---

Comment by kcrisman created at 2014-12-19 04:38:36

Changing priority from major to critical.


---

Comment by kcrisman created at 2015-02-12 15:14:43

This was merged in upstream which is now in Sage rc.  See also https://github.com/sagemath/sagenb/pull/324 for an improved way to handle this.


---

Comment by kcrisman created at 2015-02-12 15:14:43

Changing status from new to needs_review.


---

Comment by kcrisman created at 2015-02-12 15:14:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-02-12 21:16:58

Resolution: fixed
