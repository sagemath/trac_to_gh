# Issue 9525: Installation of cvxopt will always report succesful, even if it fails.

Issue created by migration from https://trac.sagemath.org/ticket/9525

Original creator: drkirkby

Original creation time: 2010-07-17 08:32:55

Assignee: GeorgSWeber

CC:  jdemeyer

Whilst trying to locate a bug causing a 64-bit build of Sage on Solaris to be unstable, I found that cvxopt will always report it has successfully installed, even if it does not. The last line in `spkg-install` is


```
python setup.py install
```


with no error checking. 




---

Comment by mhansen created at 2010-07-17 18:29:55

This needs to be coordinated with #6456


---

Comment by dimpase created at 2010-07-26 15:00:55

Changing status from new to needs_review.


---

Comment by dimpase created at 2010-07-26 15:00:55

Replying to [comment:1 mhansen]:
> This needs to be coordinated with #6456

this is done in my latest update just submitted on #6456


---

Comment by kcrisman created at 2010-12-02 16:22:33

Note that #6456 has been merged; can this be closed (i.e., was it in fact fixed in that spkg) once that receives positive review?


---

Comment by kcrisman created at 2011-01-19 21:12:11

To release manager: this one should be closed, as far as all the information suggests.


---

Comment by jdemeyer created at 2011-01-19 22:13:25

Resolution: duplicate
