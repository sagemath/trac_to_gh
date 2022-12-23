# Issue 9332: S_class_group() should return a group

Issue created by migration from https://trac.sagemath.org/ticket/9332

Original creator: stankewicz

Original creation time: 2010-06-24 21:23:42

Assignee: davidloeffler

CC:  adeines cremona jeremywest

The title says it all. I have a fix ready to go


---

Comment by stankewicz created at 2010-06-24 23:10:21

Changing status from new to needs_review.


---

Comment by rlm created at 2010-06-25 03:15:35

I don't think there's a point to adding a TestSuite doctest that doesn't work. We can always add that in once #7945 is fixed. You also need to make good on your IOU. I would also suggest a shorter `repr` string-- you don't want it line-wrapping on the terminal unnecessarily.


---

Comment by rlm created at 2010-06-25 03:15:35

Changing status from needs_review to needs_work.


---

Comment by annahaensch created at 2010-06-25 06:09:26

There are still some doctest failures in number_field.py, but we've added documentation and improved the way S_class_groups print.  Joint work with Erin Beyerstedt, Robert Miller, H.


---

Comment by cremona created at 2010-06-25 06:28:35

Good work so far!

I think the repr string for a (s-)class group should not mention its order or structure at all.  The user can always ask for that.

I'm not sure about the S() function returning None for a straight class group.  I would be happy with it returning [] when S is None.

In the number field file, there is no need to add the parameter None for straght class groups, since that is the default value;  so take those out.

I will now try the patches out...


---

Comment by cremona created at 2010-06-25 06:35:58

(After testing)  When you have simplified the string output of an S-class group you can adjust the doctest outputs in number_field.py.  (Don't worry about those Minkowski warnings -- they will disappear when the doctest passes!)


---

Comment by cremona created at 2010-06-26 05:53:48

For me the 3rd patch does not apply on top of the first two.  It also looks strange -- does it mix tabs and spaces?  (You should use only spaces, some editors put tabs in).


---

Comment by stankewicz created at 2010-06-30 04:35:37

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

Comment by davidloeffler created at 2010-06-30 11:26:35

The AttributeError comes up because attributes whose names start with an underscore are private, and ones with two underscores are "very private" -- so private that they aren't even accessible to subclasses. So when code in `FractionalIdealClass` sets `__ideal`, code in the subclass `SFractionalIdealClass`. In fact it is still accessible but under a mangled name: see [http://docs.python.org/tutorial/classes.html#private-variables](http://docs.python.org/tutorial/classes.html#private-variables).

But there is another, deeper, bug which will be uncovered when you fix this. After my changes at #9244, a `FractionalIdealClass` stores both a representing ideal of that class, accessed via `self.ideal()`, and an expression for self in terms of the generators of its parent class group, accessed via `self.list()`. The way you've set this up, elements of an S-class group use the same data structure, but the data which `list()` uses is set completely wrongly: it's set to the exponents of the given ideal in terms of the generators of the class group, but it should be in terms of the generators of the **S-class group**. What you need to do is to store somewhere the expressions for the generators of the S-class group in terms of the generators of the class group (i.e. the matrix of the quotient map) and then multiply the output of `_ideal_class_log` by this.

This is the sort of stuff that #6449 was intended to solve: quotients of abelian groups should be automatically handled by general code, rather than having to do it by hand in every specific example.


---

Comment by cremona created at 2010-06-30 11:38:29

Replying to [comment:9 davidloeffler]:
> The AttributeError comes up because attributes whose names start with an underscore are private, and ones with two underscores are "very private" -- so private that they aren't even accessible to subclasses. So when code in `FractionalIdealClass` sets `__ideal`, code in the subclass `SFractionalIdealClass`. In fact it is still accessible but under a mangled name: see [http://docs.python.org/tutorial/classes.html#private-variables](http://docs.python.org/tutorial/classes.html#private-variables).
> 
> But there is another, deeper, bug which will be uncovered when you fix this. After my changes at #9244, a `FractionalIdealClass` stores both a representing ideal of that class, accessed via `self.ideal()`, and an expression for self in terms of the generators of its parent class group, accessed via `self.list()`. The way you've set this up, elements of an S-class group use the same data structure, but the data which `list()` uses is set completely wrongly: it's set to the exponents of the given ideal in terms of the generators of the class group, but it should be in terms of the generators of the **S-class group**. What you need to do is to store somewhere the expressions for the generators of the S-class group in terms of the generators of the class group (i.e. the matrix of the quotient map) and then multiply the output of `_ideal_class_log` by this.
> 
> This is the sort of stuff that #6449 was intended to solve: quotients of abelian groups should be automatically handled by general code, rather than having to do it by hand in every specific example.

David, you should have been at Sage Days!


---

Comment by davidloeffler created at 2010-06-30 13:47:03

Here's a patch that does the equivalent of `_ideal_class_log` for S-class groups; you might find it useful.


---

Comment by stankewicz created at 2010-07-01 15:42:09

Here's patch that finally makes the S-class-group work as a group, on top of Loeffler's patch(in this ticket). Soon to come will be a single patch that gets it all done, and actually has acceptable documentation.


---

Comment by annahaensch created at 2010-07-02 20:00:08

Changing status from needs_work to needs_review.


---

Comment by annahaensch created at 2010-07-02 20:04:42

Correction: trac_9332_v3 should be applied only on trac_9244_ver4.  Sorry for the confusion, trac_9332_v3 includes changes made in previous patches, so there's no need to apply them.  Cheers.


---

Comment by rlm created at 2010-07-02 21:20:17

Let's clean up this ticket. Shall I delete the patches other than `trac_9332_v3` and `trac_9244_ver4`?


---

Comment by davidloeffler created at 2010-07-02 21:36:27

All patches here can be deleted except `trac_9332_v3`. (`trac_9244_ver4` is from another ticket. )


---

Comment by rlm created at 2010-07-02 21:44:36

Cleaned up the other one as well.


---

Comment by cremona created at 2010-10-31 21:10:14

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-10-31 21:10:14

Can we get this ticket moving again?  The one and only patch still here does not apply cleanly to 4.6.rc0, so the first step is to fix that.


---

Comment by rlm created at 2010-11-25 00:01:47

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

Comment by cremona created at 2010-11-25 09:37:58

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

Comment by cremona created at 2010-11-25 09:37:58

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-11-25 10:15:43

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

Comment by rlm created at 2010-11-26 15:54:04

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

Comment by cremona created at 2010-12-04 18:30:20

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-12-04 18:30:20

New patch is fine!


---

Comment by jdemeyer created at 2011-01-13 06:34:12

Nice patch but you should change the commit message :-)


---

Comment by jdemeyer created at 2011-01-13 06:34:12

Changing status from positive_review to needs_work.


---

Attachment

rebased on sage-4.6.1.alpha2


---

Comment by rlm created at 2011-01-14 21:27:48

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:20:48

Resolution: fixed
