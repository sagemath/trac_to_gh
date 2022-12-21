# Issue 7058: linbox reports "using frickin' slow GSL C-blas" if building with Sun Studio compiler

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-28 21:38:45

Assignee: tbd

CC:  david.kirkby@onetel.ne


```
linbox-1.1.6.p2/spkg-debian
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
Copying commentator patch
WARNING WARNING
WARNING WARNING
WARNING WARNING
WARNING WARNING
using frickin' slow GSL C-blas
WARNING WARNING
WARNING WARNING
WARNING WARNING
WARNING WARNING
WARNING WARNING
*************************************************
 Using LINBOX_BLAS=/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib/libgslcblas.so
*************************************************

```


It should be noted, that linbox later fails to build with Sun Studio, see #7026, as it does not think GMP is installed. That is of course another, and more serious issue. 


---

Comment by aapitzsch created at 2015-05-19 18:02:40

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2015-05-19 18:02:40

Is this still an issue?


---

Comment by jdemeyer created at 2016-09-14 09:51:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2016-09-14 09:51:51

The recent changes to linbox have made this obsolete.


---

Comment by vbraun created at 2017-01-21 18:03:11

Resolution: invalid
