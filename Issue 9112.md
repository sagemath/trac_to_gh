# Issue 9112: adding maximum entry option to SemistandardTableaux()

Issue created by migration from https://trac.sagemath.org/ticket/9112

Original creator: QuantumKing

Original creation time: 2010-06-01 22:45:57

Assignee: sage-combinat

CC:  hthomas

Keywords: semistandard tableaux

Sage-4.4.2, combinat/tableau.py:

Currently, the function SemistandardTableaux(p=None, mu=None) has a default maximum entry of sum(p) if p is a partition and p if p is an integer. I want to add the option to specify a maximum entry.

SemistandardTableaux(mu=[...]) returns all semistandard tableaux when it should return semistandard tableaux with content mu.

Also, the representation of the SST classes should state the maximum entry.

Eric


---

Comment by mhansen created at 2010-06-01 23:06:17

I'm not sure if printing the maximum entry is the best way to do it.  Once CombinatorialClasses are Parents, then that information will be accessible from the parent.


---

Comment by QuantumKing created at 2010-06-01 23:15:54

Replying to [comment:2 mhansen]:
> I'm not sure if printing the maximum entry is the best way to do it.  Once CombinatorialClasses are Parents, then that information will be accessible from the parent.

I didn't understand that..wouldn't it be convenient to have the maximum entry printed?
I have a patch for this which I was just about to attach, but does change the repr.


---

Attachment

After #8910, you'll be able to do something like


```
sage: S = SemistandardTableaux([3,2,1])
sage: s = S.random_element()
sage: s
[[2, 2, 2], [3, 5], [4]]
sage: s.parent() # after #8910
Semistandard tableaux of shape [3, 2, 1]
```


If you had a different parent such as "Semistandard tableaux of shape [3, 2, 1] with maximum entry 8" then you could get at the 8 from the parent method of the tableaux.

I see this as similar to the following example


```

sage: R = Integers(6)
sage: f = R(1); f
1
sage: f.parent().order()
6
```


Here, the element `f` does not print out that it is 1 mod 6.  It just prints out 1.


---

Comment by QuantumKing created at 2010-06-01 23:43:56

Replying to [comment:4 mhansen]:
> After #8910, you'll be able to do something like
> 
> {{{
> sage: S = SemistandardTableaux([3,2,1])
> sage: s = S.random_element()
> sage: s
> [[2, 2, 2], [3, 5], [4]]
> sage: s.parent() # after #8910
> Semistandard tableaux of shape [3, 2, 1]
> }}}
> 
> If you had a different parent such as "Semistandard tableaux of shape [3, 2, 1] with maximum entry 8" then you could get at the 8 from the parent method of the tableaux.
> 
> I see this as similar to the following example
> 
> {{{
> 
> sage: R = Integers(6)
> sage: f = R(1); f
> 1
> sage: f.parent().order()
> 6
> }}}
> 
> Here, the element `f` does not print out that it is 1 mod 6.  It just prints out 1. 


Ok, I still don't really see what is wrong with printing the maximum element. In your example, the patch would change it to:


```
sage: S = SemistandardTableaux([3,2,1])
sage: s = S.random_element()
sage: s
[[2, 2, 2], [3, 5], [4]]
sage: s.parent() # after #8910
Semistandard tableaux of shape [3, 2, 1] and maximum entry 6 # after #9112
```


But you think there should be a method which returns the maximum entry? Like:


```
sage: S = SemistandardTableaux([3,2,1])
sage: s = S.random_element()
sage: s
[[2, 2, 2], [3, 5], [4]]
sage: s.parent() # after #8910
Semistandard tableaux of shape [3, 2, 1]
sage: s.parent().max_entry()
6
```



---

Comment by QuantumKing created at 2010-06-01 23:47:24

Changing assignee from sage-combinat to QuantumKing.


---

Comment by QuantumKing created at 2010-06-01 23:47:24

By the way, how do you remove an attached file? I didn't put the trac number in the filename. This is my first time contributing.


---

Comment by mhansen created at 2010-06-01 23:59:20

I'm sorry -- I was confused. I thought you were suggesting printing the maximum entry with each individual tableau rather than with the parent class.  So, ignore my comments regarding that :-)

Regarding the patch, a couple of questions:

1.  Why is corners() being changed?  It seems unrelated to the ticket.

2.  4 spaces should always be used as the indentation.

3.  Any comparisons with None should be used using `is` instead of `==`.  For example, `if mu is None` or `if max_entry is not None`.  Also, tests like `not i == 1` should be `i != 1`.

4.  Instead of having -1 represent a max_entry of infinity, I think we should just use Sage's object for infinity instead.  


```
sage: type(oo)
<class 'sage.rings.infinity.PlusInfinity'>
sage: SST = SemistandardTableaux(3, max_entry=oo); SST 
Semistandard tableaux of size 3 and no maximum entry 
```


5. `raise TypeError, "mu must be of size p (= %s)"%p ` might be better as a `ValueError`.

Other than that, I'm pretty happy with the changes.

You need certain privileges to remove files.  If you just post the new one, I can delete any ones that need to be deleted.


---

Comment by QuantumKing created at 2010-06-02 00:07:59

Cool, thanks a lot.

I'll fix those things and post the new patch.


---

Attachment


---

Comment by jbandlow created at 2010-06-15 15:06:55

Hi, I'm interested in helping with this; either in terms of a review or helping with the code.  What is the status right now?  There are patches posted, but they are not marked as needing review.  Is more work being done?


---

Comment by QuantumKing created at 2010-06-15 15:47:07

Replying to [comment:10 jbandlow]:

Hello,
"trac_9112_tableau_py.patch" adds the functionality mentioned in the ticket.
There was talk of adding more features such as an option to input an alphabet...
I guess I was waiting to see what happened with that but its been a while now so I think I'll go ahead and mark this ticket as needing a review.
We can always add a new ticket later.


---

Comment by QuantumKing created at 2010-06-15 15:47:41

Changing status from new to needs_review.


---

Attachment

This looks good for the most part.  I've uploaded a reviewer patch which fixes some failing doctests, changes `__repr__` to `_repr_` throughout the file, improves some docstrings, and improves the efficiency of `__contains__` for semistandard tableaux.  There is a lot more that can be done with this file, but these patches make sage better and there is no reason for them not to go in right away.  I'll open another ticket for general cleanup of tableau.py.

So, in short, I give a positive review to the patch [http://trac.sagemath.org/sage_trac/attachment/ticket/9112/trac_9112_tableau_py.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9112/trac_9112_tableau_py.patch) , provided my reviewer patch is applied on top of it.  So now someone (possibly the original author) needs to approve the reviewer patch, and the ticket can be marked as positive review.


---

Comment by QuantumKing created at 2010-06-17 15:55:13

Replying to [comment:13 jbandlow]:

The reviewer patch looks good. I've uploaded some extra very small changes:

Previously, if you called `SemistandardTableaux(max_entry=0)`, `_repr_` would print "Semistandard Tableaux".

Also, if you called `SemistandardTableaux(max_entry=oo)`, `_repr_` would print "Semistandard Tableaux with maximum entry +Infinity" when it should just be "Semistandard Tableaux".

I've allowed for the user to give `PlusInfinity` as well as anything that has type `PlusInfinity`
as an infinite max_entry.

So with trac_9112_rereviewed.patch on top of the two others I'm happy. Let me know if you're happy!

Eric


---

Comment by jbandlow created at 2010-06-18 16:08:21

Replying to [comment:14 QuantumKing]:

> I've allowed for the user to give `PlusInfinity` as well as anything that has type `PlusInfinity`
> as an infinite max_entry.

Just curious, do you know of anything that has type `PlusInfinity` other than `PlusInfinity`?  This check looks redundant to me...


---

Comment by QuantumKing created at 2010-06-18 19:43:03

Replying to [comment:15 jbandlow]:

Well I'm not an expert in this, but if I do "oo is PlusInfinity" it gives me False so I have to do "type(oo) is PlusInfinity" to give me True. Also, if I do "type(PlusInfinity) is PlusInfinity" it gives me False...Does that make sense? Is this the way it should be?

Thanks,

 Eric


---

Comment by jbandlow created at 2010-06-18 21:43:20

Replying to [comment:16 QuantumKing]:

I think you want `oo is PlusInfinity()` (note the parentheses).  Does that behave like you expect?


---

Comment by QuantumKing created at 2010-06-19 22:24:30

Replying to [comment:17 jbandlow]:

Well, its just that if someone decides to call `SemistandardTableaux`(max_entry=`PlusInfinity`) and prints _repr_ they'll get "Semistandard Tableaux with maximum entry +Infinity" when it should really just say "Semistandard Tableaux".

But I'm new here and don't know how things are usually done..So let me know what you think.

Thanks,
 Eric


---

Comment by QuantumKing created at 2010-06-19 22:35:49

Replying to [comment:17 jbandlow]:

Nevermind. That works just fine. If the user were to call that they would get an error saying max_entry must be an integer. I'll upload a replacement.


---

Attachment


---

Attachment

Thanks Eric, positive review!  Nice work.  I've uploaded a patch which folds all the other changes together, to make things easier on the release manager. It contains nothing new.


---

Comment by jbandlow created at 2010-06-28 13:52:53

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-06-30 17:20:57

The patch `trac_9112_folded_untabified.patch` uses tabs for indentation, which is against sage coding conventions. I have uploaded a version with spaces instead of tabs.


---

Attachment

Version without tabs - apply only this patch


---

Comment by mpatel created at 2010-07-21 01:43:57

Resolution: fixed
