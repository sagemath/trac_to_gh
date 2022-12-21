# Issue 7842: Let attrcall objects accept further arguments

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-01-04 15:27:08

Assignee: nthiery

CC:  sage-combinat

Keywords: attrcall

The attached patch allows for the following:


```
            sage: xseries = attrcall('series', x)
            sage: xseries(sin(x), 4)
            1*x + (-1/6)*x^3 + Order(x^4)
```


This is used in #7753


---

Attachment


---

Comment by nthiery created at 2010-01-04 15:28:39

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-01-04 17:54:05

Another nice thing to have now that I think about it would be this syntax:


```
sage: xseries = attrcall.series(x)
sage: xseries(sin(x), 4)
1*x + (-1/6)*x^3 + Order(x^4)
```


I'll make a new ticket for this so that that it'll backward-compatible with the old version.


---

Comment by nthiery created at 2010-01-04 18:03:07

Replying to [comment:2 mhansen]:
> Another nice thing to have now that I think about it would be this syntax:
> 
> {{{
> sage: xseries = attrcall.series(x)
> sage: xseries(sin(x), 4)
> 1*x + (-1/6)*x^3 + Order(x^4)
> }}}

Your point is that this syntax gives a better visual hint about this being about method calls, right? So here, attrcall would be some sort of dummy object placeholder? Why not. Though I am a bit reluctant with having two syntaxes.

> I'll make a new ticket for this so that that it'll backward-compatible with the old version.

Do you mind reviewing this first, so that we can get #7753 in?

I'll review your patch in return :-)


---

Comment by mhansen created at 2010-01-04 18:08:48

This patch looks good to me.

We should also maybe allow putting keywords in too at the "second stage".


---

Comment by mhansen created at 2010-01-04 18:08:48

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 07:51:39

Resolution: fixed
