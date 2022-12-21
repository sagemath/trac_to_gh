# Issue 8077: New python_gnutls-1.1.4.p7.spkg works with Open Solaris 64 bit

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-26 12:25:32

Assignee: drkirkby

CC:  drkirby was

Now SAGE64="yes" works for Open Solaris too.

The package can de found here:
[http://boxen.math.washington.edu/home/jsp/ports/python_gnutls-1.1.4.p7.spkg](http://boxen.math.washington.edu/home/jsp/ports/python_gnutls-1.1.4.p7.spkg)



```
Writing /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/python_gnutls-1.1.4-py2.6.egg-info

real	0m6.243s
user	0m0.188s
sys	0m0.245s
Successfully installed python_gnutls-1.1.4.p7
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1/spkg/build/python_gnutls-1.1.4.p7
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python_gnutls-1.1.4.p7.spkg
jaap`@`opensolaris:~/Downloads/sage-4.3.1$ touch spkg/installed/gnutls-1.1.4.p6

```



Jaap


---

Comment by jsp created at 2010-01-26 12:25:49

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-01-27 12:06:11

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-27 12:06:11

Works fine. Positive review.


---

Comment by mpatel created at 2010-02-11 15:17:53

Resolution: fixed
