# Issue 7952: broken binomial sum (fixed in maxima)

Issue created by migration from https://trac.sagemath.org/ticket/7952

Original creator: burcin

Original creation time: 2010-01-16 18:08:01

Assignee: burcin

CC:  jpflori mjo

Keywords: maxima

From the following sage-devel thread:

http://groups.google.com/group/sage-devel/t/c7a742292f424b04


```
On Jan 10, 6:15 pm, Harald Schilly <harald.schi...@gmail.com> wrote:
> Hi, I got this from the report a problem link:
>
> Typing (in the inotebook)
>
> var('t,k,i')
> sum(binomial(i+t,t),i,0,k)
>
> results in
>
> binomial(k + t + 1, t + 1) - 1
>
> which is false, the well-known answer is binomial(k + t + 1, t + 1)  

There is a fix for this bug in maxima cvs. If you don't want to wait
for the next release I can provide a patch.

Andrej
```



---

Comment by burcin created at 2010-01-17 08:32:21

Here is the patch, we should add this to our package:

http://maxima.cvs.sourceforge.net/viewvc/maxima/maxima/src/combin.lisp?r1=1.39&r2=1.40&view=patch


---

Comment by kcrisman created at 2010-11-16 14:21:45

jpflori reports this is fixed in #10187's package.  Maybe s/he will contribute a patch :)


---

Attachment

Add a doctest for the correct behavior.


---

Comment by mjo created at 2011-12-14 00:31:13

Changing status from new to needs_review.


---

Comment by mjo created at 2011-12-14 00:31:13

This is fixed in sage-4.8.alpha4, so I've added a doctest.


---

Comment by kcrisman created at 2012-01-28 02:36:40

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-01-28 02:36:40

Positive review.


---

Comment by jdemeyer created at 2012-02-02 12:52:00

Resolution: fixed
