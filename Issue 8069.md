# Issue 8069: New mpfi-1.3.4-cvs20071125.p8.spkg works with Open Solaris 64 bit

Issue created by migration from https://trac.sagemath.org/ticket/8069

Original creator: jsp

Original creation time: 2010-01-26 00:01:49

Assignee: drkirkby

CC:  drkirby was

Yet another correction. SAGE64=yes works also on Open Solaris 64 bit.

The spkg is here:
[http://boxen.math.washington.edu/home/jsp/ports/mpfi-1.3.4-cvs20071125.p8.spkg](http://boxen.math.washington.edu/home/jsp/ports/mpfi-1.3.4-cvs20071125.p8.spkg)



```
make[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8/src'
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8/src'

real	0m15.129s
user	0m7.916s
sys	0m6.259s
Successfully installed mpfi-1.3.4-cvs20071125.p8
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfi-1.3.4-cvs20071125.p8
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing mpfi-1.3.4-cvs20071125.p8.spkg
jaap@opensolaris:~/Downloads/sage-4.3.1$ 


```


Jaap


---

Comment by jsp created at 2010-01-26 00:02:05

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-26 11:34:50

without some way to be able to see what you have changed, it is difficult to review. Again, without a patch, it could never be integrated with anyone else that might change this package

Dave


---

Comment by drkirkby created at 2010-01-26 11:34:50

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by jsp created at 2010-01-26 18:34:38

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jsp created at 2010-01-26 18:54:52

Sorry! Clicked on the wrong file!

Jaap


---

Comment by drkirkby created at 2010-01-27 02:41:27

This is fine.


---

Comment by drkirkby created at 2010-01-27 02:41:36

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-27 04:27:47

Changing type from enhancement to defect.


---

Comment by mpatel created at 2010-02-11 15:17:40

Resolution: fixed
