# Issue 8063: New gsl-1.10.p2.spkg works with Open Solaris 64 bit

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-25 21:49:41

Assignee: drkirkby

Setting SAGE64=yes not only works on OSX, but also with Open Solaris 64 bit.

The package can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/gsl-1.10.p2.spkg](http://boxen.math.washington.edu/home/jsp/ports/gsl-1.10.p2.spkg)

Jaap


---

Comment by jsp created at 2010-01-25 21:49:53

Changing status from new to needs_review.


---

Attachment

I'm not sure I'd personally bother sorting out SAGE64 issues in packages unless they are building 32-bit, which this one is not. 

But you have also removed Michael Abshoff as a maintainer, and also removed the 


```
echo "64 bit MacIntel"
```


so I would agree the fixes are desirable. 

I would search for packages which are building 32-bit. 


```
$ file local/lib/* | grep 32-bit
$ file local/lib/* | grep 32-bit
```


and only bother fixing them. 

Dave


---

Comment by jsp created at 2010-01-27 13:51:02

Replying to [comment:2 drkirkby]:

> 
> so I would agree the fixes are desirable. 
> 

So positive review?

Jaap


---

Comment by drkirkby created at 2010-01-27 14:02:37

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:17:03

Resolution: fixed
