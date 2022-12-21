# Issue 7412: from_lehmer_code modifies its argument

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-11-08 16:32:34

Assignee: mhansen

CC:  hivert

Here is the problem:


```
sage: L = [0,0,0]
sage: sage.combinat.permutation.from_lehmer_code( L )
[1, 2, 3]
sage: L
[1, 1, 1]
```



---

Comment by hivert created at 2009-11-08 16:56:16

Hi Yann ! 

Thanks for the report ! Are you working on it ? The fix is rather trivial and I'm not in the mood for racing with you to get the first patch :-)
 
By the way, thanks for putting me in CC, but it is better to put all the sage-combinat group for all these problem.

Cheers,

Florent


---

Comment by ylchapuy created at 2009-11-08 17:41:35

need #7011


---

Comment by ylchapuy created at 2009-11-08 17:47:26

Changing status from new to needs_review.


---

Attachment

Hi Florent,

Here is the patch. Sorry for the CC, next time I'll follow your advice.

Regards,
 Yann


---

Comment by hivert created at 2009-11-08 18:59:26

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-11-08 18:59:26

The patch is ok and ready to go but I don't see any dependence with #7011...
Maybe you meant #7411, but there is no problem with it. The two patches do commute. 

Cheers,

Florent


---

Comment by ylchapuy created at 2009-11-08 19:04:25

Oups, yes I meant #7411. Thanks for the review.


---

Comment by ylchapuy created at 2009-11-10 00:53:12

Resolution: duplicate


---

Comment by ylchapuy created at 2009-11-10 00:53:12

I don't know if duplicate is the right word, but the patch in #7414 solves this problem as well, but improve also the performance. Sometimes it's useful to think a little bit more...

Yann
