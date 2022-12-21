# Issue 9890: substitute goes too far: (5-e^x).substitute(x=log(x)) -> 5-log(x)

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-09-10 19:53:23

Assignee: burcin

CC:  rbk

Keywords: pynac

Reported by Kees on sage-support:

http://groups.google.com/group/sage-support/t/bfa34b077dd31b73


```
Running the following few lines:

eq=5-e^x
print "1:",eq.substitute(x=3*x)
print "2:",eq.substitute(x=log(x))

yields the output (Sage 4.5.2 with Ubuntu):

1: -e^(3*x) + 5
2: -log(x) + 5
```


This is also present in GiNaC:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.7)
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> subs(5-exp(x),x==log(x));
5-log(x)
```




---

Comment by burcin created at 2010-09-19 14:35:55

Changing status from new to needs_work.


---

Comment by burcin created at 2010-09-19 14:35:55

This was fixed in GiNaC by Richard Kreckel:

http://www.ginac.de/pipermail/ginac-list/2010-September/001738.html

I merged his changes to pynac, so it will be available in the next release.


---

Attachment

add doctest


---

Comment by kcrisman created at 2011-02-17 01:39:58

Burcin, I'm still getting

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: (5-e^x).substitute(x=log(x))
-log(x) + 5
```

Which version of Pynac is this in?


---

Comment by rbk created at 2011-02-17 07:44:27

For reference, here is a link to the upstream patch:
http://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=90ad10b58d02365a407b2d84d8b93e50030feaa5


---

Comment by kcrisman created at 2011-02-17 14:09:07

I can confirm this is not in the latest version of Pynac in Sage or on its website (0.2.1), by looking at container.h.


---

Comment by burcin created at 2011-05-09 15:08:53

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2011-05-09 15:08:53

New pynac package with the fix is at #11317.


---

Comment by kcrisman created at 2011-05-09 18:33:23

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-05-09 18:33:23

Okay, this is fine.

Burcin, I have to say I feel a little odd saying that I'm reviewing Kreckel's work, when I'm really reviewing your merging his work and your doctest (though I looked at the actual patch, naturally).  Is there a different way to put the author in?  You are the author of the actual patch here, not the Ginac update; I don't think any other spkgs put upstream people who committed things in this way.


---

Comment by burcin created at 2011-05-09 19:04:15

Thanks for the review!

Replying to [comment:7 kcrisman]:
> Burcin, I have to say I feel a little odd saying that I'm reviewing Kreckel's work, when I'm really reviewing your merging his work and your doctest (though I looked at the actual patch, naturally).  Is there a different way to put the author in?  You are the author of the actual patch here, not the Ginac update; I don't think any other spkgs put upstream people who committed things in this way.

I put Richard's name in the authors list since he should get the credit for fixing this in the Sage release notes. I think we should give more credit to upstream developers. Are you suggesting my name should be in the authors or the reviewers field? :)


---

Comment by jdemeyer created at 2011-05-27 12:01:22

Resolution: fixed
