# Issue 6213: easy addition of an alias to eta product (trivial ticket to deal with)

Issue created by migration from https://trac.sagemath.org/ticket/6213

Original creator: was

Original creation time: 2009-06-04 21:01:26

Assignee: was

CC:  davidloeffler


```
    Hi David,

    This is inconsistent:


    sage: e =EtaProduct(3, {3:12, 1:-12})
    sage: e.qexp(10)  # but no q_expansion function

    Everywhere else in Sage we write "q_expansion" and have qexp as an alias. It thus took me a while to find e.qexp, since I expected e.q_expansion. What do you think?


Agreed. I wrote most of that class during a lunch break at a conference last summer, and at the time I didn't have much of a clue about Sage conventions (as is probably clear to anyone reading the code). Please feel free to change it!

```



---

Attachment


---

Comment by craigcitro created at 2009-06-05 06:32:57

Quick and easy fix attached.


---

Comment by was created at 2009-06-05 07:19:20

that was easy :-)


---

Comment by davidloeffler created at 2009-06-07 13:25:10

Changing component from number theory to modular forms.


---

Comment by davidloeffler created at 2009-06-07 13:25:10

This clearly belongs in component = modular forms (not that it really matters).


---

Comment by davidloeffler created at 2009-06-07 13:25:10

Changing assignee from was to craigcitro.


---

Comment by ncalexan created at 2009-06-13 21:07:51

Resolution: fixed


---

Comment by davidloeffler created at 2009-06-16 11:28:29

William should get reviewer credit for this, not me.
