# Issue 8918: Strange behavior for Permutation()

Issue created by migration from Trac.

Original creator: lvendramin

Original creation time: 2010-05-07 16:48:02

Assignee: sage-combinat

CC:  jbandlow

See these examples:


```
sage: Permutation([1,2,3])
[1, 2, 3]
sage: Permutation([1,2,3,1])
[1, 2, 3, 1]
sage: [1,2,3] in Permutations()
True
sage: [1,2,3,1] in Permutations()
False
sage: Permutation([1,2,3,1]) in Permutations()
True
```



---

Comment by lftabera created at 2010-09-08 13:03:37

Yes, this is an error

[1,2,3,1] dos not define a permutation, so the method should raise an error. See also #9831


---

Comment by knsam created at 2013-01-27 00:14:21

I think, this in fact can be closed as a duplicate of the ticket you mention (#9831).

Replying to [comment:1 lftabera]:
> Yes, this is an error
> 
> [1,2,3,1] dos not define a permutation, so the method should raise an error. See also #9831


---

Comment by tscrim created at 2013-01-29 19:46:21

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-01-29 19:46:21

One of a few tickets like this. Bonus points if you can find them all.

Also, don't forget to set this to needs_review. Thanks.


---

Comment by tscrim created at 2013-01-29 19:46:36

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-31 20:38:24

Resolution: duplicate
