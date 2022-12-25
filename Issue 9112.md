# Issue 9112: adding maximum entry option to SemistandardTableaux()

archive/issues_009112.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @hughrthomas\n\nKeywords: semistandard tableaux\n\nSage-4.4.2, combinat/tableau.py:\n\nCurrently, the function SemistandardTableaux(p=None, mu=None) has a default maximum entry of sum(p) if p is a partition and p if p is an integer. I want to add the option to specify a maximum entry.\n\nSemistandardTableaux(mu=[...]) returns all semistandard tableaux when it should return semistandard tableaux with content mu.\n\nAlso, the representation of the SST classes should state the maximum entry.\n\nEric\n\nIssue created by migration from https://trac.sagemath.org/ticket/9112\n\n",
    "created_at": "2010-06-01T22:45:57Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "adding maximum entry option to SemistandardTableaux()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9112",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```
Assignee: sage-combinat

CC:  @hughrthomas

Keywords: semistandard tableaux

Sage-4.4.2, combinat/tableau.py:

Currently, the function SemistandardTableaux(p=None, mu=None) has a default maximum entry of sum(p) if p is a partition and p if p is an integer. I want to add the option to specify a maximum entry.

SemistandardTableaux(mu=[...]) returns all semistandard tableaux when it should return semistandard tableaux with content mu.

Also, the representation of the SST classes should state the maximum entry.

Eric

Issue created by migration from https://trac.sagemath.org/ticket/9112





---

archive/issue_comments_084631.json:
```json
{
    "body": "I'm not sure if printing the maximum entry is the best way to do it.  Once CombinatorialClasses are Parents, then that information will be accessible from the parent.",
    "created_at": "2010-06-01T23:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84631",
    "user": "https://github.com/mwhansen"
}
```

I'm not sure if printing the maximum entry is the best way to do it.  Once CombinatorialClasses are Parents, then that information will be accessible from the parent.



---

archive/issue_comments_084632.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> I'm not sure if printing the maximum entry is the best way to do it.  Once CombinatorialClasses are Parents, then that information will be accessible from the parent.\n\nI didn't understand that..wouldn't it be convenient to have the maximum entry printed?\nI have a patch for this which I was just about to attach, but does change the repr.",
    "created_at": "2010-06-01T23:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84632",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Replying to [comment:2 mhansen]:
> I'm not sure if printing the maximum entry is the best way to do it.  Once CombinatorialClasses are Parents, then that information will be accessible from the parent.

I didn't understand that..wouldn't it be convenient to have the maximum entry printed?
I have a patch for this which I was just about to attach, but does change the repr.



---

archive/issue_comments_084633.json:
```json
{
    "body": "Attachment [combinat-tableau_py.patch](tarball://root/attachments/some-uuid/ticket9112/combinat-tableau_py.patch) by @mwhansen created at 2010-06-01 23:24:59\n\nAfter #8910, you'll be able to do something like\n\n\n```\nsage: S = SemistandardTableaux([3,2,1])\nsage: s = S.random_element()\nsage: s\n[[2, 2, 2], [3, 5], [4]]\nsage: s.parent() # after #8910\nSemistandard tableaux of shape [3, 2, 1]\n```\n\n\nIf you had a different parent such as \"Semistandard tableaux of shape [3, 2, 1] with maximum entry 8\" then you could get at the 8 from the parent method of the tableaux.\n\nI see this as similar to the following example\n\n\n```\n\nsage: R = Integers(6)\nsage: f = R(1); f\n1\nsage: f.parent().order()\n6\n```\n\n\nHere, the element `f` does not print out that it is 1 mod 6.  It just prints out 1.",
    "created_at": "2010-06-01T23:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84633",
    "user": "https://github.com/mwhansen"
}
```

Attachment [combinat-tableau_py.patch](tarball://root/attachments/some-uuid/ticket9112/combinat-tableau_py.patch) by @mwhansen created at 2010-06-01 23:24:59

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

archive/issue_comments_084634.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> After #8910, you'll be able to do something like\n> \n> {{{\n> sage: S = SemistandardTableaux([3,2,1])\n> sage: s = S.random_element()\n> sage: s\n> [[2, 2, 2], [3, 5], [4]]\n> sage: s.parent() # after #8910\n> Semistandard tableaux of shape [3, 2, 1]\n> }}}\n> \n> If you had a different parent such as \"Semistandard tableaux of shape [3, 2, 1] with maximum entry 8\" then you could get at the 8 from the parent method of the tableaux.\n> \n> I see this as similar to the following example\n> \n> {{{\n> \n> sage: R = Integers(6)\n> sage: f = R(1); f\n> 1\n> sage: f.parent().order()\n> 6\n> }}}\n> \n> Here, the element `f` does not print out that it is 1 mod 6.  It just prints out 1. \n\n\nOk, I still don't really see what is wrong with printing the maximum element. In your example, the patch would change it to:\n\n\n```\nsage: S = SemistandardTableaux([3,2,1])\nsage: s = S.random_element()\nsage: s\n[[2, 2, 2], [3, 5], [4]]\nsage: s.parent() # after #8910\nSemistandard tableaux of shape [3, 2, 1] and maximum entry 6 # after #9112\n```\n\n\nBut you think there should be a method which returns the maximum entry? Like:\n\n\n```\nsage: S = SemistandardTableaux([3,2,1])\nsage: s = S.random_element()\nsage: s\n[[2, 2, 2], [3, 5], [4]]\nsage: s.parent() # after #8910\nSemistandard tableaux of shape [3, 2, 1]\nsage: s.parent().max_entry()\n6\n```\n",
    "created_at": "2010-06-01T23:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84634",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

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

archive/issue_comments_084635.json:
```json
{
    "body": "Changing assignee from sage-combinat to QuantumKing.",
    "created_at": "2010-06-01T23:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84635",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Changing assignee from sage-combinat to QuantumKing.



---

archive/issue_comments_084636.json:
```json
{
    "body": "By the way, how do you remove an attached file? I didn't put the trac number in the filename. This is my first time contributing.",
    "created_at": "2010-06-01T23:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84636",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

By the way, how do you remove an attached file? I didn't put the trac number in the filename. This is my first time contributing.



---

archive/issue_comments_084637.json:
```json
{
    "body": "I'm sorry -- I was confused. I thought you were suggesting printing the maximum entry with each individual tableau rather than with the parent class.  So, ignore my comments regarding that :-)\n\nRegarding the patch, a couple of questions:\n\n1.  Why is corners() being changed?  It seems unrelated to the ticket.\n\n2.  4 spaces should always be used as the indentation.\n\n3.  Any comparisons with None should be used using `is` instead of `==`.  For example, `if mu is None` or `if max_entry is not None`.  Also, tests like `not i == 1` should be `i != 1`.\n\n4.  Instead of having -1 represent a max_entry of infinity, I think we should just use Sage's object for infinity instead.  \n\n\n```\nsage: type(oo)\n<class 'sage.rings.infinity.PlusInfinity'>\nsage: SST = SemistandardTableaux(3, max_entry=oo); SST \nSemistandard tableaux of size 3 and no maximum entry \n```\n\n\n5. `raise TypeError, \"mu must be of size p (= %s)\"%p ` might be better as a `ValueError`.\n\nOther than that, I'm pretty happy with the changes.\n\nYou need certain privileges to remove files.  If you just post the new one, I can delete any ones that need to be deleted.",
    "created_at": "2010-06-01T23:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84637",
    "user": "https://github.com/mwhansen"
}
```

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

archive/issue_comments_084638.json:
```json
{
    "body": "Cool, thanks a lot.\n\nI'll fix those things and post the new patch.",
    "created_at": "2010-06-02T00:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84638",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Cool, thanks a lot.

I'll fix those things and post the new patch.



---

archive/issue_comments_084639.json:
```json
{
    "body": "Attachment [trac_9112_tableau_py.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_tableau_py.patch) by @hughrthomas created at 2010-06-02 17:53:49",
    "created_at": "2010-06-02T17:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84639",
    "user": "https://github.com/hughrthomas"
}
```

Attachment [trac_9112_tableau_py.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_tableau_py.patch) by @hughrthomas created at 2010-06-02 17:53:49



---

archive/issue_comments_084640.json:
```json
{
    "body": "Hi, I'm interested in helping with this; either in terms of a review or helping with the code.  What is the status right now?  There are patches posted, but they are not marked as needing review.  Is more work being done?",
    "created_at": "2010-06-15T15:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84640",
    "user": "https://github.com/jbandlow"
}
```

Hi, I'm interested in helping with this; either in terms of a review or helping with the code.  What is the status right now?  There are patches posted, but they are not marked as needing review.  Is more work being done?



---

archive/issue_comments_084641.json:
```json
{
    "body": "Replying to [comment:10 jbandlow]:\n\nHello,\n\"trac_9112_tableau_py.patch\" adds the functionality mentioned in the ticket.\nThere was talk of adding more features such as an option to input an alphabet...\nI guess I was waiting to see what happened with that but its been a while now so I think I'll go ahead and mark this ticket as needing a review.\nWe can always add a new ticket later.",
    "created_at": "2010-06-15T15:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84641",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Replying to [comment:10 jbandlow]:

Hello,
"trac_9112_tableau_py.patch" adds the functionality mentioned in the ticket.
There was talk of adding more features such as an option to input an alphabet...
I guess I was waiting to see what happened with that but its been a while now so I think I'll go ahead and mark this ticket as needing a review.
We can always add a new ticket later.



---

archive/issue_comments_084642.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-15T15:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84642",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084643.json:
```json
{
    "body": "Attachment [trac_9112_reviewer.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_reviewer.patch) by @jbandlow created at 2010-06-17 13:03:05\n\nThis looks good for the most part.  I've uploaded a reviewer patch which fixes some failing doctests, changes `__repr__` to `_repr_` throughout the file, improves some docstrings, and improves the efficiency of `__contains__` for semistandard tableaux.  There is a lot more that can be done with this file, but these patches make sage better and there is no reason for them not to go in right away.  I'll open another ticket for general cleanup of tableau.py.\n\nSo, in short, I give a positive review to the patch [http://trac.sagemath.org/sage_trac/attachment/ticket/9112/trac_9112_tableau_py.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9112/trac_9112_tableau_py.patch) , provided my reviewer patch is applied on top of it.  So now someone (possibly the original author) needs to approve the reviewer patch, and the ticket can be marked as positive review.",
    "created_at": "2010-06-17T13:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84643",
    "user": "https://github.com/jbandlow"
}
```

Attachment [trac_9112_reviewer.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_reviewer.patch) by @jbandlow created at 2010-06-17 13:03:05

This looks good for the most part.  I've uploaded a reviewer patch which fixes some failing doctests, changes `__repr__` to `_repr_` throughout the file, improves some docstrings, and improves the efficiency of `__contains__` for semistandard tableaux.  There is a lot more that can be done with this file, but these patches make sage better and there is no reason for them not to go in right away.  I'll open another ticket for general cleanup of tableau.py.

So, in short, I give a positive review to the patch [http://trac.sagemath.org/sage_trac/attachment/ticket/9112/trac_9112_tableau_py.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9112/trac_9112_tableau_py.patch) , provided my reviewer patch is applied on top of it.  So now someone (possibly the original author) needs to approve the reviewer patch, and the ticket can be marked as positive review.



---

archive/issue_comments_084644.json:
```json
{
    "body": "Replying to [comment:13 jbandlow]:\n\nThe reviewer patch looks good. I've uploaded some extra very small changes:\n\nPreviously, if you called `SemistandardTableaux(max_entry=0)`, `_repr_` would print \"Semistandard Tableaux\".\n\nAlso, if you called `SemistandardTableaux(max_entry=oo)`, `_repr_` would print \"Semistandard Tableaux with maximum entry +Infinity\" when it should just be \"Semistandard Tableaux\".\n\nI've allowed for the user to give `PlusInfinity` as well as anything that has type `PlusInfinity`\nas an infinite max_entry.\n\nSo with trac_9112_rereviewed.patch on top of the two others I'm happy. Let me know if you're happy!\n\nEric",
    "created_at": "2010-06-17T15:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84644",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Replying to [comment:13 jbandlow]:

The reviewer patch looks good. I've uploaded some extra very small changes:

Previously, if you called `SemistandardTableaux(max_entry=0)`, `_repr_` would print "Semistandard Tableaux".

Also, if you called `SemistandardTableaux(max_entry=oo)`, `_repr_` would print "Semistandard Tableaux with maximum entry +Infinity" when it should just be "Semistandard Tableaux".

I've allowed for the user to give `PlusInfinity` as well as anything that has type `PlusInfinity`
as an infinite max_entry.

So with trac_9112_rereviewed.patch on top of the two others I'm happy. Let me know if you're happy!

Eric



---

archive/issue_comments_084645.json:
```json
{
    "body": "Replying to [comment:14 QuantumKing]:\n\n> I've allowed for the user to give `PlusInfinity` as well as anything that has type `PlusInfinity`\n> as an infinite max_entry.\n\nJust curious, do you know of anything that has type `PlusInfinity` other than `PlusInfinity`?  This check looks redundant to me...",
    "created_at": "2010-06-18T16:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84645",
    "user": "https://github.com/jbandlow"
}
```

Replying to [comment:14 QuantumKing]:

> I've allowed for the user to give `PlusInfinity` as well as anything that has type `PlusInfinity`
> as an infinite max_entry.

Just curious, do you know of anything that has type `PlusInfinity` other than `PlusInfinity`?  This check looks redundant to me...



---

archive/issue_comments_084646.json:
```json
{
    "body": "Replying to [comment:15 jbandlow]:\n\nWell I'm not an expert in this, but if I do \"oo is PlusInfinity\" it gives me False so I have to do \"type(oo) is PlusInfinity\" to give me True. Also, if I do \"type(PlusInfinity) is PlusInfinity\" it gives me False...Does that make sense? Is this the way it should be?\n\nThanks,\n\n Eric",
    "created_at": "2010-06-18T19:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84646",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Replying to [comment:15 jbandlow]:

Well I'm not an expert in this, but if I do "oo is PlusInfinity" it gives me False so I have to do "type(oo) is PlusInfinity" to give me True. Also, if I do "type(PlusInfinity) is PlusInfinity" it gives me False...Does that make sense? Is this the way it should be?

Thanks,

 Eric



---

archive/issue_comments_084647.json:
```json
{
    "body": "Replying to [comment:16 QuantumKing]:\n\nI think you want `oo is PlusInfinity()` (note the parentheses).  Does that behave like you expect?",
    "created_at": "2010-06-18T21:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84647",
    "user": "https://github.com/jbandlow"
}
```

Replying to [comment:16 QuantumKing]:

I think you want `oo is PlusInfinity()` (note the parentheses).  Does that behave like you expect?



---

archive/issue_comments_084648.json:
```json
{
    "body": "Replying to [comment:17 jbandlow]:\n\nWell, its just that if someone decides to call `SemistandardTableaux`(max_entry=`PlusInfinity`) and prints _repr_ they'll get \"Semistandard Tableaux with maximum entry +Infinity\" when it should really just say \"Semistandard Tableaux\".\n\nBut I'm new here and don't know how things are usually done..So let me know what you think.\n\nThanks,\n Eric",
    "created_at": "2010-06-19T22:24:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84648",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Replying to [comment:17 jbandlow]:

Well, its just that if someone decides to call `SemistandardTableaux`(max_entry=`PlusInfinity`) and prints _repr_ they'll get "Semistandard Tableaux with maximum entry +Infinity" when it should really just say "Semistandard Tableaux".

But I'm new here and don't know how things are usually done..So let me know what you think.

Thanks,
 Eric



---

archive/issue_comments_084649.json:
```json
{
    "body": "Replying to [comment:17 jbandlow]:\n\nNevermind. That works just fine. If the user were to call that they would get an error saying max_entry must be an integer. I'll upload a replacement.",
    "created_at": "2010-06-19T22:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84649",
    "user": "https://trac.sagemath.org/admin/accounts/users/QuantumKing"
}
```

Replying to [comment:17 jbandlow]:

Nevermind. That works just fine. If the user were to call that they would get an error saying max_entry must be an integer. I'll upload a replacement.



---

archive/issue_comments_084650.json:
```json
{
    "body": "Attachment [trac_9112_rereviewed.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_rereviewed.patch) by @jbandlow created at 2010-06-28 13:49:35",
    "created_at": "2010-06-28T13:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84650",
    "user": "https://github.com/jbandlow"
}
```

Attachment [trac_9112_rereviewed.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_rereviewed.patch) by @jbandlow created at 2010-06-28 13:49:35



---

archive/issue_comments_084651.json:
```json
{
    "body": "Attachment [trac_9112_folded.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_folded.patch) by @jbandlow created at 2010-06-28 13:52:53\n\nThanks Eric, positive review!  Nice work.  I've uploaded a patch which folds all the other changes together, to make things easier on the release manager. It contains nothing new.",
    "created_at": "2010-06-28T13:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84651",
    "user": "https://github.com/jbandlow"
}
```

Attachment [trac_9112_folded.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_folded.patch) by @jbandlow created at 2010-06-28 13:52:53

Thanks Eric, positive review!  Nice work.  I've uploaded a patch which folds all the other changes together, to make things easier on the release manager. It contains nothing new.



---

archive/issue_comments_084652.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-28T13:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84652",
    "user": "https://github.com/jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084653.json:
```json
{
    "body": "The patch `trac_9112_folded_untabified.patch` uses tabs for indentation, which is against sage coding conventions. I have uploaded a version with spaces instead of tabs.",
    "created_at": "2010-06-30T17:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84653",
    "user": "https://github.com/loefflerd"
}
```

The patch `trac_9112_folded_untabified.patch` uses tabs for indentation, which is against sage coding conventions. I have uploaded a version with spaces instead of tabs.



---

archive/issue_comments_084654.json:
```json
{
    "body": "Attachment [trac_9112_folded_untabified.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_folded_untabified.patch) by @loefflerd created at 2010-06-30 18:25:54\n\nVersion without tabs - apply only this patch",
    "created_at": "2010-06-30T18:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84654",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_9112_folded_untabified.patch](tarball://root/attachments/some-uuid/ticket9112/trac_9112_folded_untabified.patch) by @loefflerd created at 2010-06-30 18:25:54

Version without tabs - apply only this patch



---

archive/issue_comments_084655.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9112#issuecomment-84655",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
