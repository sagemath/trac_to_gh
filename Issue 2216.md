# Issue 2216: Creating an order in a number field --> infinite loop?

Issue created by migration from https://trac.sagemath.org/ticket/2216

Original creator: craigcitro

Original creation time: 2008-02-20 01:57:12

Assignee: was

So I just tried the following:


```
sage: F.<alpha> = NumberField(x**4+3)
sage: F.order([alpha**2], allow_subfield=True)
```


and it seemed to go into an infinite loop. (Maybe I'm impatient, but it doesn't seem like it should take more than 2 seconds to do this, nevermind the minute I waited.) I haven't looked to see what the problem is at all.


---

Comment by AlexGhitza created at 2008-04-25 01:52:16

It was indeed an infinite loop in absolute_order_from_module_generators().  See the attached patch.


---

Comment by craigcitro created at 2008-04-26 11:32:31

Looks good, with one trivial change: I think we should take out the line that says "This shows that trac #2216 has been fixed." This is useful to people editing the code, but not to the user -- and that's who the docstring *should* be for ...


---

Comment by AlexGhitza created at 2008-04-26 13:40:56

revised patch


---

Attachment

I've replaced the patch with one in which "trac #2216 has been fixed" is changed into something more informative for the user ("an order in a subfield").


---

Comment by mabshoff created at 2008-04-26 22:42:25

I still think that mentioning the trac ticket when adding a specific doctest is a good thing. So combining both, i.e. a description that is useful for the user as well as (fixes #2216) in a good compromise.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-26 22:58:52

Resolution: fixed


---

Comment by mabshoff created at 2008-04-26 22:58:52

Merged in Sage 3.0.1.alpha0
