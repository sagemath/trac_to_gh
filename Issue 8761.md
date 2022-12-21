# Issue 8761: sage notebook: make a new interact control (like selector) that really works like a button

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-25 01:11:12

Assignee: jason, was

CC:  kcrisman jhpalmieri boothby

First, see this screenshot:
   http://sage.math.washington.edu/home/wstein/tmp/button.png

Now imagine that when you push either of the buttons, the interact is triggered and the button comes back up (it does not get *stuck* down as a selector).  

When the interact triggers calling of the function, if this is triggered by a button being clicked then the corresponding variable is set to the value of that button (usually the text label).  Otherwise, the variable is set to None.  Then interact applications can tell if a button being pushed triggered the function being called based on whether or not the variable is None.


```
`@`interact
def f(X = button(['Ok', 'Cancel', "Continue"])):
    print X
```


Notice that button is much like selector with buttons=True...


---

Comment by chapoton created at 2020-04-04 06:13:38

ancient ticket about deprecated sagenb, can we close ?


---

Comment by chapoton created at 2020-04-04 06:13:38

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2020-04-04 21:44:18

Yes, I think so.


---

Comment by jhpalmieri created at 2020-04-04 21:44:18

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-05 06:14:52

Resolution: wontfix
