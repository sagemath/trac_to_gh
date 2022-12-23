# Issue 1897: %latex -- bug in passing in predefined sage variables (serious but probably very easy to fix)

Issue created by migration from https://trac.sagemath.org/ticket/1897

Original creator: was

Original creation time: 2008-01-23 21:05:16

Assignee: boothby


```
12:46 < ianxek> hi there
12:47 < ianxek> A Latex question in sage : if I define a variable say x=3 and later on use the
                %latex environment and use $\sage{x}$ then it says x is unknown
12:48 < ianxek> How do I tell sage to access the previously defined x ?
13:03 < sage> This is a bug in Sage!
13:03 < sage> However, here is a workaround until it gets fixed.
13:03 < sage> ianxek.
13:03 < sage> latex.eval('$2+\sage{a}$', locals=globals())
13:03 < sage> I.e., instead of typing %latex in the cell, do 
13:04 < sage> latex.eval("A latex string", locals=globals())
13:04 < sage> And you'll see the variables properly.
13:04 < sage> Thanks for asking this question.
```


I think the problem involves system.eval not getting passed the
globals() dictionary correctly...


---

Comment by mhansen created at 2009-01-19 13:50:11

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2009-01-19 13:50:11

Changing status from new to assigned.


---

Attachment

The problem was caused by syseval in sage.server.support needing the second positional argument to be an argument for global variables.


---

Comment by TimothyClemans created at 2009-01-21 07:00:43

With %latex in notebook I'm getting 

```
An error occured.
Error latexing slide.
```



---

Comment by jason created at 2009-01-22 14:44:30

This fixes the problem for me.  TimothyClemans, you need a bunch of things for this to work, like dvipng, etc.  Can you latex any slides at all?


---

Comment by mabshoff created at 2009-01-23 09:39:30

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 09:39:30

Resolution: fixed
