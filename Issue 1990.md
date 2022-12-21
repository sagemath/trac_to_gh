# Issue 1990: ZZ.random_element() -- never returns 0 and typos/nonsense in docstrings

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 03:45:39

Assignee: somebody

1. ZZ.random_element() never returns 0. This is a bug.

2. "ZZ.random_element() -- return an integer over the natrual distribution $Pr(n) = 1/2|n|(|n|+1)$."  This contains a typo "natrual".  Also the formula doesn't make any sense.  What's in the numerator / denominator?  What does it mean at 0?


---

Comment by was created at 2008-01-31 04:03:54


```
[10:40pm] william_stein: the doc for ZZ.random_element is:"ZZ.random_element() -- return an integer over the natrual distribution $Pr(n) = 1/2|n|(|n|+1)$."
[10:40pm] kedlaya: if you really picked a random element of Z, would it ever be 0?
[10:40pm] william_stein: kedlaya -- there is a documented distribution.
[10:40pm] kedlaya: oh, ok.
[10:41pm] william_stein: I don't even know what "$Pr(n) = 1/2|n|(|n|+1)$." means.
[10:46pm] kedlaya: you mean because of bad parentheses?
[10:46pm] william_stein: yes
[10:47pm] kedlaya: and the fact that it doesn't make sense at n=0
[10:47pm] william_stein: yep
[10:47pm] kedlaya: i guess it means 0 for n = 0, and otherwise 1/(2 |n| (|n| + 1))
[10:47pm] kedlaya: since that distro does have total measure 1
[10:48pm] william_stein: that's most likely.
[10:48pm] kedlaya: but who picked that anyway?
[10:48pm] william_stein: But it is not a good choice.
[10:48pm] william_stein: I think either Robert Bradshaw or jkantor?
[10:48pm] kedlaya: i'm not sure what constitutes a good choice.
[10:48pm] jkantor: not me
[10:48pm] jkantor: poisson distribution would be good
[10:48pm] william_stein: jkantor -- I've made this trac #1990...
[10:49pm] kedlaya: doesn't that still leave a parameter choice? And poisson is only a distro on nonnegative integers.
[10:49pm] jkantor: your right
[10:50pm] kedlaya: but other than that, I agree with you. 
[10:50pm] jkantor: about the non-negative, sorry
[10:50pm] kedlaya: i'd say pick the sign at random, but then I'm not sure what to do with 0
```



---

Comment by robertwb created at 2008-01-31 07:40:35

I was the one that picked this distribution--after soliciting feedback from (a much smaller) sage-devel. A better way to think of this is floor(1/X) where X is a real number uniformly chosen from [-1,1]. 

I was looking for a distribution that was:

 * Parameterless
 * Reasonably small mean absolute value, with non-negligible probability for large values
 * Unbounded
 * Fast

I'm willing to forgo the first criterion. I figured it was better than a uniform choice out of [-2,-1,0,1,2], though the fact that it never chose 0 did bother me a bit. 

The poisson distribution, multiplied by a random sign, might work, but what choice for a parameter? It is also strange because it would have two "peaks" (unless the mean is really small, in which case no large integers would ever be produced in practice).


---

Comment by robertwb created at 2008-02-14 06:26:14

Absent further discussion on this ticket, I will modify this function so it returns 0 some of the time and improve/correct the docstring.


---

Attachment


---

Comment by robertwb created at 2008-03-29 18:53:29

Works great and looks good to me. Resolves the problems too (now 0 is returned 20% of the type by default, and it has a much better docstring).


---

Comment by mabshoff created at 2008-03-29 19:18:54

Merged in Sage 2.11.rc0


---

Comment by mabshoff created at 2008-03-29 19:18:54

Resolution: fixed
