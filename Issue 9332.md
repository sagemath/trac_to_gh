# Issue 9332: S_class_group() should return a group

archive/issues_009332.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  adeines @JohnCremona jeremywest\n\nThe title says it all. I have a fix ready to go\n\nIssue created by migration from https://trac.sagemath.org/ticket/9332\n\n",
    "created_at": "2010-06-24T21:23:42Z",
    "labels": [
        "component: number fields"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "S_class_group() should return a group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9332",
    "user": "https://trac.sagemath.org/admin/accounts/users/stankewicz"
}
```
Assignee: @loefflerd

CC:  adeines @JohnCremona jeremywest

The title says it all. I have a fix ready to go

Issue created by migration from https://trac.sagemath.org/ticket/9332





---

archive/issue_comments_087890.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-24T23:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87890",
    "user": "https://trac.sagemath.org/admin/accounts/users/stankewicz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087891.json:
```json
{
    "body": "I don't think there's a point to adding a TestSuite doctest that doesn't work. We can always add that in once #7945 is fixed. You also need to make good on your IOU. I would also suggest a shorter `repr` string-- you don't want it line-wrapping on the terminal unnecessarily.",
    "created_at": "2010-06-25T03:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87891",
    "user": "https://github.com/rlmill"
}
```

I don't think there's a point to adding a TestSuite doctest that doesn't work. We can always add that in once #7945 is fixed. You also need to make good on your IOU. I would also suggest a shorter `repr` string-- you don't want it line-wrapping on the terminal unnecessarily.



---

archive/issue_comments_087892.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-25T03:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87892",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087893.json:
```json
{
    "body": "There are still some doctest failures in number_field.py, but we've added documentation and improved the way S_class_groups print.  Joint work with Erin Beyerstedt, Robert Miller, H.",
    "created_at": "2010-06-25T06:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87893",
    "user": "https://github.com/annahaensch"
}
```

There are still some doctest failures in number_field.py, but we've added documentation and improved the way S_class_groups print.  Joint work with Erin Beyerstedt, Robert Miller, H.



---

archive/issue_comments_087894.json:
```json
{
    "body": "Good work so far!\n\nI think the repr string for a (s-)class group should not mention its order or structure at all.  The user can always ask for that.\n\nI'm not sure about the S() function returning None for a straight class group.  I would be happy with it returning [] when S is None.\n\nIn the number field file, there is no need to add the parameter None for straght class groups, since that is the default value;  so take those out.\n\nI will now try the patches out...",
    "created_at": "2010-06-25T06:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87894",
    "user": "https://github.com/JohnCremona"
}
```

Good work so far!

I think the repr string for a (s-)class group should not mention its order or structure at all.  The user can always ask for that.

I'm not sure about the S() function returning None for a straight class group.  I would be happy with it returning [] when S is None.

In the number field file, there is no need to add the parameter None for straght class groups, since that is the default value;  so take those out.

I will now try the patches out...



---

archive/issue_comments_087895.json:
```json
{
    "body": "(After testing)  When you have simplified the string output of an S-class group you can adjust the doctest outputs in number_field.py.  (Don't worry about those Minkowski warnings -- they will disappear when the doctest passes!)",
    "created_at": "2010-06-25T06:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87895",
    "user": "https://github.com/JohnCremona"
}
```

(After testing)  When you have simplified the string output of an S-class group you can adjust the doctest outputs in number_field.py.  (Don't worry about those Minkowski warnings -- they will disappear when the doctest passes!)



---

archive/issue_comments_087896.json:
```json
{
    "body": "For me the 3rd patch does not apply on top of the first two.  It also looks strange -- does it mix tabs and spaces?  (You should use only spaces, some editors put tabs in).",
    "created_at": "2010-06-26T05:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87896",
    "user": "https://github.com/JohnCremona"
}
```

For me the 3rd patch does not apply on top of the first two.  It also looks strange -- does it mix tabs and spaces?  (You should use only spaces, some editors put tabs in).



---

archive/issue_comments_087897.json:
```json
{
    "body": "The newest patch is something that I've been working on for the last several days, but I'm making no progress. There's a phantom attribute error which comes up under the following code:\n\n\n```\nsage: K.<a> = QuadraticField(-14)                             \nsage: K.testSclassgroup(tuple([K.ideal(2,a)]))                \nClass group of order 2 with structure C2 of Number Field in a with defining polynomial x^2 + 14\nsage: K.testSclassgroup(tuple([K.ideal(2,a)]))(K.ideal(3,a+1))\nERROR: An unexpected error occurred ...\n```\n\n\nPerhaps there's something stupid I'm missing and someone else can point it out. Otherwise, I'm going to work on something else for a while and come back to this with a fresh head.",
    "created_at": "2010-06-30T04:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87897",
    "user": "https://trac.sagemath.org/admin/accounts/users/stankewicz"
}
```

The newest patch is something that I've been working on for the last several days, but I'm making no progress. There's a phantom attribute error which comes up under the following code:


```
sage: K.<a> = QuadraticField(-14)                             
sage: K.testSclassgroup(tuple([K.ideal(2,a)]))                
Class group of order 2 with structure C2 of Number Field in a with defining polynomial x^2 + 14
sage: K.testSclassgroup(tuple([K.ideal(2,a)]))(K.ideal(3,a+1))
ERROR: An unexpected error occurred ...
```


Perhaps there's something stupid I'm missing and someone else can point it out. Otherwise, I'm going to work on something else for a while and come back to this with a fresh head.



---

archive/issue_comments_087898.json:
```json
{
    "body": "The AttributeError comes up because attributes whose names start with an underscore are private, and ones with two underscores are \"very private\" -- so private that they aren't even accessible to subclasses. So when code in `FractionalIdealClass` sets `__ideal`, code in the subclass `SFractionalIdealClass`. In fact it is still accessible but under a mangled name: see [http://docs.python.org/tutorial/classes.html#private-variables](http://docs.python.org/tutorial/classes.html#private-variables).\n\nBut there is another, deeper, bug which will be uncovered when you fix this. After my changes at #9244, a `FractionalIdealClass` stores both a representing ideal of that class, accessed via `self.ideal()`, and an expression for self in terms of the generators of its parent class group, accessed via `self.list()`. The way you've set this up, elements of an S-class group use the same data structure, but the data which `list()` uses is set completely wrongly: it's set to the exponents of the given ideal in terms of the generators of the class group, but it should be in terms of the generators of the **S-class group**. What you need to do is to store somewhere the expressions for the generators of the S-class group in terms of the generators of the class group (i.e. the matrix of the quotient map) and then multiply the output of `_ideal_class_log` by this.\n\nThis is the sort of stuff that #6449 was intended to solve: quotients of abelian groups should be automatically handled by general code, rather than having to do it by hand in every specific example.",
    "created_at": "2010-06-30T11:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87898",
    "user": "https://github.com/loefflerd"
}
```

The AttributeError comes up because attributes whose names start with an underscore are private, and ones with two underscores are "very private" -- so private that they aren't even accessible to subclasses. So when code in `FractionalIdealClass` sets `__ideal`, code in the subclass `SFractionalIdealClass`. In fact it is still accessible but under a mangled name: see [http://docs.python.org/tutorial/classes.html#private-variables](http://docs.python.org/tutorial/classes.html#private-variables).

But there is another, deeper, bug which will be uncovered when you fix this. After my changes at #9244, a `FractionalIdealClass` stores both a representing ideal of that class, accessed via `self.ideal()`, and an expression for self in terms of the generators of its parent class group, accessed via `self.list()`. The way you've set this up, elements of an S-class group use the same data structure, but the data which `list()` uses is set completely wrongly: it's set to the exponents of the given ideal in terms of the generators of the class group, but it should be in terms of the generators of the **S-class group**. What you need to do is to store somewhere the expressions for the generators of the S-class group in terms of the generators of the class group (i.e. the matrix of the quotient map) and then multiply the output of `_ideal_class_log` by this.

This is the sort of stuff that #6449 was intended to solve: quotients of abelian groups should be automatically handled by general code, rather than having to do it by hand in every specific example.



---

archive/issue_comments_087899.json:
```json
{
    "body": "Replying to [comment:9 davidloeffler]:\n> The AttributeError comes up because attributes whose names start with an underscore are private, and ones with two underscores are \"very private\" -- so private that they aren't even accessible to subclasses. So when code in `FractionalIdealClass` sets `__ideal`, code in the subclass `SFractionalIdealClass`. In fact it is still accessible but under a mangled name: see [http://docs.python.org/tutorial/classes.html#private-variables](http://docs.python.org/tutorial/classes.html#private-variables).\n> \n> But there is another, deeper, bug which will be uncovered when you fix this. After my changes at #9244, a `FractionalIdealClass` stores both a representing ideal of that class, accessed via `self.ideal()`, and an expression for self in terms of the generators of its parent class group, accessed via `self.list()`. The way you've set this up, elements of an S-class group use the same data structure, but the data which `list()` uses is set completely wrongly: it's set to the exponents of the given ideal in terms of the generators of the class group, but it should be in terms of the generators of the **S-class group**. What you need to do is to store somewhere the expressions for the generators of the S-class group in terms of the generators of the class group (i.e. the matrix of the quotient map) and then multiply the output of `_ideal_class_log` by this.\n> \n> This is the sort of stuff that #6449 was intended to solve: quotients of abelian groups should be automatically handled by general code, rather than having to do it by hand in every specific example.\n\nDavid, you should have been at Sage Days!",
    "created_at": "2010-06-30T11:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87899",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:9 davidloeffler]:
> The AttributeError comes up because attributes whose names start with an underscore are private, and ones with two underscores are "very private" -- so private that they aren't even accessible to subclasses. So when code in `FractionalIdealClass` sets `__ideal`, code in the subclass `SFractionalIdealClass`. In fact it is still accessible but under a mangled name: see [http://docs.python.org/tutorial/classes.html#private-variables](http://docs.python.org/tutorial/classes.html#private-variables).
> 
> But there is another, deeper, bug which will be uncovered when you fix this. After my changes at #9244, a `FractionalIdealClass` stores both a representing ideal of that class, accessed via `self.ideal()`, and an expression for self in terms of the generators of its parent class group, accessed via `self.list()`. The way you've set this up, elements of an S-class group use the same data structure, but the data which `list()` uses is set completely wrongly: it's set to the exponents of the given ideal in terms of the generators of the class group, but it should be in terms of the generators of the **S-class group**. What you need to do is to store somewhere the expressions for the generators of the S-class group in terms of the generators of the class group (i.e. the matrix of the quotient map) and then multiply the output of `_ideal_class_log` by this.
> 
> This is the sort of stuff that #6449 was intended to solve: quotients of abelian groups should be automatically handled by general code, rather than having to do it by hand in every specific example.

David, you should have been at Sage Days!



---

archive/issue_comments_087900.json:
```json
{
    "body": "Here's a patch that does the equivalent of `_ideal_class_log` for S-class groups; you might find it useful.",
    "created_at": "2010-06-30T13:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87900",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch that does the equivalent of `_ideal_class_log` for S-class groups; you might find it useful.



---

archive/issue_comments_087901.json:
```json
{
    "body": "Here's patch that finally makes the S-class-group work as a group, on top of Loeffler's patch(in this ticket). Soon to come will be a single patch that gets it all done, and actually has acceptable documentation.",
    "created_at": "2010-07-01T15:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87901",
    "user": "https://trac.sagemath.org/admin/accounts/users/stankewicz"
}
```

Here's patch that finally makes the S-class-group work as a group, on top of Loeffler's patch(in this ticket). Soon to come will be a single patch that gets it all done, and actually has acceptable documentation.



---

archive/issue_comments_087902.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T20:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87902",
    "user": "https://github.com/annahaensch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087903.json:
```json
{
    "body": "Correction: trac_9332_v3 should be applied only on trac_9244_ver4.  Sorry for the confusion, trac_9332_v3 includes changes made in previous patches, so there's no need to apply them.  Cheers.",
    "created_at": "2010-07-02T20:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87903",
    "user": "https://github.com/annahaensch"
}
```

Correction: trac_9332_v3 should be applied only on trac_9244_ver4.  Sorry for the confusion, trac_9332_v3 includes changes made in previous patches, so there's no need to apply them.  Cheers.



---

archive/issue_comments_087904.json:
```json
{
    "body": "Let's clean up this ticket. Shall I delete the patches other than `trac_9332_v3` and `trac_9244_ver4`?",
    "created_at": "2010-07-02T21:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87904",
    "user": "https://github.com/rlmill"
}
```

Let's clean up this ticket. Shall I delete the patches other than `trac_9332_v3` and `trac_9244_ver4`?



---

archive/issue_comments_087905.json:
```json
{
    "body": "All patches here can be deleted except `trac_9332_v3`. (`trac_9244_ver4` is from another ticket. )",
    "created_at": "2010-07-02T21:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87905",
    "user": "https://github.com/loefflerd"
}
```

All patches here can be deleted except `trac_9332_v3`. (`trac_9244_ver4` is from another ticket. )



---

archive/issue_comments_087906.json:
```json
{
    "body": "Cleaned up the other one as well.",
    "created_at": "2010-07-02T21:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87906",
    "user": "https://github.com/rlmill"
}
```

Cleaned up the other one as well.



---

archive/issue_comments_087907.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-31T21:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87907",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087908.json:
```json
{
    "body": "Can we get this ticket moving again?  The one and only patch still here does not apply cleanly to 4.6.rc0, so the first step is to fix that.",
    "created_at": "2010-10-31T21:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87908",
    "user": "https://github.com/JohnCremona"
}
```

Can we get this ticket moving again?  The one and only patch still here does not apply cleanly to 4.6.rc0, so the first step is to fix that.



---

archive/issue_comments_087909.json:
```json
{
    "body": "I'm uploading a rebased (on sage-4.6) patch which modifies printing in class fields to not print the structure when size is 1, fixes some caching bugs, updates several doctests, etc...\n\nHowever, this happens, and I'm not sure whether this is okay or not:\n\n\n```\nsage -t sage/rings/number_field/number_field_ideal.py\n**********************************************************************\nFile \"/home/rlmill/sage-4.6/devel/sage-main/sage/rings/number_field/number_field\n_ideal.py\", line 1017:\n    sage: I._S_ideal_class_log([])\nExpected:\n    [3]\nGot:\n    [1]\n**********************************************************************\n```\n",
    "created_at": "2010-11-25T00:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87909",
    "user": "https://github.com/rlmill"
}
```

I'm uploading a rebased (on sage-4.6) patch which modifies printing in class fields to not print the structure when size is 1, fixes some caching bugs, updates several doctests, etc...

However, this happens, and I'm not sure whether this is okay or not:


```
sage -t sage/rings/number_field/number_field_ideal.py
**********************************************************************
File "/home/rlmill/sage-4.6/devel/sage-main/sage/rings/number_field/number_field
_ideal.py", line 1017:
    sage: I._S_ideal_class_log([])
Expected:
    [3]
Got:
    [1]
**********************************************************************
```




---

archive/issue_comments_087910.json:
```json
{
    "body": "I applied the patch (no problems) to 4.6.1.alpha2.  The thing you observed does not happen:\n\n```\nsage: K.<a> = QuadraticField(-14) \nsage: S = K.primes_above(2) \nsage: S\n[Fractional ideal (2, a)]\nsage: I = K.ideal(3, a-1)\nsage: I._S_ideal_class_log(S) \n[1]\nsage: I._S_ideal_class_log([]) \n[1]\n```\n\n\nI am now testing...",
    "created_at": "2010-11-25T09:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87910",
    "user": "https://github.com/JohnCremona"
}
```

I applied the patch (no problems) to 4.6.1.alpha2.  The thing you observed does not happen:

```
sage: K.<a> = QuadraticField(-14) 
sage: S = K.primes_above(2) 
sage: S
[Fractional ideal (2, a)]
sage: I = K.ideal(3, a-1)
sage: I._S_ideal_class_log(S) 
[1]
sage: I._S_ideal_class_log([]) 
[1]
```


I am now testing...



---

archive/issue_comments_087911.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-25T09:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87911",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087912.json:
```json
{
    "body": "Two trivial doctest failures \n\n```\nsage -t -long sage/rings/polynomial/polynomial_quotient_ring.py\n**********************************************************************\nFile \"/home/jec/sage-4.6.1.alpha2/devel/sage-main/sage/rings/polynomial/polynomial_quotient_ring.py\", line 737:\n    sage: K.class_group()\nExpected:\n    Class group of order 1 with structure  of Number Field in a with defining polynomial x^2 + 3\nGot:\n    Class group of order 1 of Number Field in a with defining polynomial x^2 + 3\n```\n\nand\n\n```\nsage -t -long sage/rings/number_field/number_field_ideal.py\n**********************************************************************\nFile \"/home/jec/sage-4.6.1.alpha2/devel/sage-main/sage/rings/number_field/number_field_ideal.py\", line 1051:\n    sage: I._S_ideal_class_log([])\nExpected:\n    [3]\nGot:\n    [1]\n```\n\nwhere in both cases the \"Expected \" does not look right anyway!\n\nI am leaving this as needs review since I have not looked closely again at the code, but I can assert that apart from the above two things all (long) tests pass with 4.6.1.alpha2.",
    "created_at": "2010-11-25T10:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87912",
    "user": "https://github.com/JohnCremona"
}
```

Two trivial doctest failures 

```
sage -t -long sage/rings/polynomial/polynomial_quotient_ring.py
**********************************************************************
File "/home/jec/sage-4.6.1.alpha2/devel/sage-main/sage/rings/polynomial/polynomial_quotient_ring.py", line 737:
    sage: K.class_group()
Expected:
    Class group of order 1 with structure  of Number Field in a with defining polynomial x^2 + 3
Got:
    Class group of order 1 of Number Field in a with defining polynomial x^2 + 3
```

and

```
sage -t -long sage/rings/number_field/number_field_ideal.py
**********************************************************************
File "/home/jec/sage-4.6.1.alpha2/devel/sage-main/sage/rings/number_field/number_field_ideal.py", line 1051:
    sage: I._S_ideal_class_log([])
Expected:
    [3]
Got:
    [1]
```

where in both cases the "Expected " does not look right anyway!

I am leaving this as needs review since I have not looked closely again at the code, but I can assert that apart from the above two things all (long) tests pass with 4.6.1.alpha2.



---

archive/issue_comments_087913.json:
```json
{
    "body": "I also believe the actual output is correct. Evidence:\n\n```\nsage: K.<a> = QuadraticField(-14)\nsage: S = K.primes_above(2)\nsage: I = K.ideal(3,a+2)\nsage: I\nFractional ideal (3, a + 2)\nsage: I._ideal_class_log()\n[1]\nsage: I._S_ideal_class_log([])\n[1]\n```\n\n\nI am uploading a fresh patch, which will fix all the above issues.",
    "created_at": "2010-11-26T15:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87913",
    "user": "https://github.com/rlmill"
}
```

I also believe the actual output is correct. Evidence:

```
sage: K.<a> = QuadraticField(-14)
sage: S = K.primes_above(2)
sage: I = K.ideal(3,a+2)
sage: I
Fractional ideal (3, a + 2)
sage: I._ideal_class_log()
[1]
sage: I._S_ideal_class_log([])
[1]
```


I am uploading a fresh patch, which will fix all the above issues.



---

archive/issue_comments_087914.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-04T18:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87914",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087915.json:
```json
{
    "body": "New patch is fine!",
    "created_at": "2010-12-04T18:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87915",
    "user": "https://github.com/JohnCremona"
}
```

New patch is fine!



---

archive/issue_comments_087916.json:
```json
{
    "body": "Nice patch but you should change the commit message :-)",
    "created_at": "2011-01-13T06:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87916",
    "user": "https://github.com/jdemeyer"
}
```

Nice patch but you should change the commit message :-)



---

archive/issue_comments_087917.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-13T06:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87917",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_087918.json:
```json
{
    "body": "Attachment [trac_9332.patch](tarball://root/attachments/some-uuid/ticket9332/trac_9332.patch) by @rlmill created at 2011-01-14 21:27:22\n\nrebased on sage-4.6.1.alpha2",
    "created_at": "2011-01-14T21:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87918",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9332.patch](tarball://root/attachments/some-uuid/ticket9332/trac_9332.patch) by @rlmill created at 2011-01-14 21:27:22

rebased on sage-4.6.1.alpha2



---

archive/issue_comments_087919.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-14T21:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87919",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_087920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9332#issuecomment-87920",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
