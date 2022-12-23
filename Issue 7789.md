# Issue 7789: Improve the arguments for the default type of a variable in MixedIntegerLinearProgram

Issue created by migration from https://trac.sagemath.org/ticket/7789

Original creator: ncohen

Original creation time: 2009-12-29 18:14:06

Assignee: jkantor

The help of MixedIntegerLinearProgram.new_variable shows a way to define a default type for new variables, but it uses the argument vtype and pre-defined constants (MixedIntegerLinearProgram.__INTEGER for example) which is really ugly.

We should accept things like :

```
p.new_variable(boolean=True)
```

or


```
p.new_variable(type="boolean")
```



---

Comment by ncohen created at 2010-01-16 16:31:23

Here it is !


---

Comment by ncohen created at 2010-01-16 16:31:23

Changing status from new to needs_review.


---

Comment by jason created at 2010-03-17 05:14:14

Changing type from defect to enhancement.


---

Comment by wdj created at 2010-04-03 13:02:05

I think this needs more examples.


---

Comment by wdj created at 2010-04-03 13:02:05

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-04-03 19:07:51

I just updated the patch to add 2 lines of test .. I am sorry but I do not really know which kind of examples you expect there... :-/ 

Please tell me and I'll add them immediately !!

Nathann


---

Comment by ncohen created at 2010-04-03 19:07:51

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-05-06 16:52:48

You current code allows `real=True` and `binary=True` and will quietly make a choice.


---

Comment by ncohen created at 2010-05-06 17:15:22

Fixed !


---

Comment by jsyri created at 2010-05-13 20:21:23

Few comments:

I think parameter 'name' should be documented. I couldn't find out any place where changing this parameter would affect at all. Also show() method lists 'binary' type variables as boolean variables, which I find bit ugly. Fixing that might be out of scope of this ticket though, as 'binary' is used extensively in code and documentation.

I'm not native English speaker so I might be wrong here, but I think this: "An exception is raised when two types are required" at the documentation should maybe say something like "An exception is raised when two types are _supplied_".


---

Comment by jsyri created at 2010-05-13 20:21:23

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-05-13 20:35:45

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-05-13 20:35:45

Sounds comments... Updated ! :-)

Nathann


---

Comment by jsyri created at 2010-05-13 21:18:27

Unfortunately indentation at documentation for 'name' is off by one, so one more update required :-( Otherwise everything seems fine. I'm running doctest now, and if they come clean it'll get positive review after that last fix.


---

Comment by jsyri created at 2010-05-13 21:18:27

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-05-13 21:22:07

Changing status from needs_work to needs_review.


---

Attachment

Done.


---

Comment by jsyri created at 2010-05-14 07:53:50

Changing status from needs_review to positive_review.


---

Comment by jsyri created at 2010-05-14 07:53:50

Everything seems to be in order. Positive review it is.


---

Comment by mhansen created at 2010-06-07 04:51:52

Resolution: fixed
