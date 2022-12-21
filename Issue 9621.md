# Issue 9621: Fix GAP interface problem in sylow_subgroup method

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-07-28 08:18:22

Assignee: joyner

Keywords: GAP string representation

The following was reported by [Kenny Brown](http://groups.google.com/group/sage-support/browse_thread/thread/9fbca4e4dbadbe37):

```
sage: n = 3^2 * 7^2
sage: G = CyclicPermutationGroup(n)
sage: G.sylow_subgroup(3)
Traceback (most recent call last):
...
```


The problem is that in the sylow_subgroup method, it is attempted to get the string presentation of a permutation in GAP by calling gap.eval(...). However, GAP truncates the output. So, better use gap.eval('Print(...)') instead.

Moreover, the method uses quite generic variable names in the GAP interface. This is dangerous, as the use of variable names that any average user might choose as well can have nasty side effects.

The attached patch fixes both problems.


---

Attachment

Fixes GAP interface bug of sylow_subgroup method (with doctest)


---

Comment by SimonKing created at 2010-07-28 08:24:50

Changing status from new to needs_review.


---

Comment by jsrn created at 2010-07-30 11:53:57

Bear with me as this is my first action on the ticket system :-)

It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. I have added an extra patch file for this.


---

Comment by jsrn created at 2010-07-30 11:54:28

Simplification of the above patch


---

Attachment

Replaces the other two patches


---

Attachment

Hi Johan!

Replying to [comment:2 jsrn]:
> It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. 

You have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().

However, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.

Now the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??

Cheers,
Simon


---

Comment by jsrn created at 2010-07-30 13:18:09

Ah, embarrassing; I had seen that mistake, but must have forgotten to remake the patch or something :-) 

Thanks for adding me as author. I guess we'll have to wait for a nice person to come along and review the (final?) patch.

Regards,
Johan

Replying to [comment:3 SimonKing]:
> Hi Johan!
> 
> Replying to [comment:2 jsrn]:
> > It seems that some parsing functionality has already been built into the gap interface, so all the last lines of sylow_subgroups can be greatly simplified. 
> 
> You have a misprint in your patch. You wrote self_element_class(), but it should be self._element_class().
> 
> However, your suggestion makes indeed sense. So, I created a patch that corrects that misprint and combines both of our patches into one.
> 
> Now the big question is: I think we are both Authors now (and I inserted your name in the corresponding field of this ticket). So, who will review??
> 
> Cheers,
> Simon


---

Comment by SimonKing created at 2011-03-08 12:03:21

Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch

(For the patchbot)

Probably this patch is bit rotting and we need rebasing. But who knows, perhaps we are lucky...


---

Comment by johanbosman created at 2011-11-30 21:43:14

Changing status from needs_review to needs_work.


---

Comment by johanbosman created at 2011-11-30 21:43:14

Replying to [comment:5 SimonKing]:
> Apply trac-9621_permgroup_sylow_subgroup_with_simplification.patch
> 
> (For the patchbot)
> 
> Probably this patch is bit rotting and we need rebasing. 
Indeed we do. :).


---

Comment by mhansen created at 2012-05-14 22:56:58

I think this can be closed as I fixed this problem in #10334.


---

Comment by SimonKing created at 2012-05-15 05:20:35

Replying to [comment:7 mhansen]:
> I think this can be closed as I fixed this problem in #10334.

OK, I just tested that it works with sage-5.0.rc0. Hence, it is a duplicate (or sub-problem) of #10334.


---

Comment by SimonKing created at 2012-05-15 05:20:35

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-05-21 08:02:48

Resolution: duplicate
