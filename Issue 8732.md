# Issue 8732: bug in new HMM code

Issue created by migration from https://trac.sagemath.org/ticket/8732

Original creator: was

Original creation time: 2010-04-20 20:48:47

Assignee: amhou

CC:  mhampton boothby jason

Crap, there is a bug in the new HMM code (#8547) that just went into sage-4.4.alpha0:

Try this:


```
sage: m = hmm.DiscreteHiddenMarkovModel([[1/3]*3]*3, [ [5]*5 ]*3, [1/3]*3, 'abcde'); m
sage: v = list('a'*100); v
sage: m.baum_welch(v)
sage: m.sample(10)
['e', 'a', 'e', 'e', 'a', 'c', 'c', 'c', 'c', 'a']
sage: m
Discrete Hidden Markov Model with 3 States and 5 Emissions
Transition matrix:
[0.333333333333 0.333333333333 0.333333333333]
[0.333333333333 0.333333333333 0.333333333333]
[0.333333333333 0.333333333333 0.333333333333]
Emission matrix:
[1.0 0.0 0.0 0.0 0.0]
[1.0 0.0 0.0 0.0 0.0]
[1.0 0.0 0.0 0.0 0.0]
Initial probabilities: [0.3333, 0.3333, 0.3333]
```


Notice above that it is impossible for the model to emit anything except 'a'.  Yet in the sample it does!  

This bug wasn't in the previous HMM code, of course.  I'll fix this ASAP for sage-4.4. 


William


---

Attachment


---

Comment by was created at 2010-04-20 21:46:26

I had a C array index backwards.


---

Comment by was created at 2010-04-20 21:46:26

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-20 23:01:28

I'm cc'ing some possible reviewers...


---

Comment by mhampton created at 2010-04-21 03:11:09

OK, patch looks good.  Passes tests and coverage, change makes sense, and I did some random testing so I am giving this a positive review.


---

Comment by mhampton created at 2010-04-21 03:11:09

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-23 17:09:04

Merged into 4.4.alpha2.


---

Comment by jhpalmieri created at 2010-04-23 17:09:04

Resolution: fixed
