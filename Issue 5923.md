# Issue 5923: Handling of magma and pari input in ModularForms

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2009-04-28 22:41:04

Assignee: craigcitro

The ModularForms command has some slightly counter-intuitive behaviour on some types of input:


```
sage: ModularForms(gp(1),12)
---------------------------------------------------------------------------
TypeError     

[much snipped error message]

TypeError: Error executing code in GP/PARI:
CODE:
        sage[4]=level(sage[3]);
GP/PARI ERROR:
  ***   expected character: ',' instead of: sage[4]=level(sage[3]);
                                                              ^-----
```


I realize that this is because the first element is supposed to be a group, although a (Sage) integer is allowed.

Would there be any support for having an if statement in the function to catch magma or pari elements and transform them into their Sage equivalents?


---

Comment by davidloeffler created at 2009-05-01 08:02:03

Changing assignee from craigcitro to davidloeffler.


---

Comment by davidloeffler created at 2009-05-01 08:02:03

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-05-01 08:02:03

Certainly this is a bug, but a very easy one to fix; I'll fix it lat


---

Comment by davidloeffler created at 2009-05-01 11:43:36

.. er. 

It turns out that the problem is that if x is a gp object, then "x.level" always *exists*: it is a microscopic function wrapper which on being called, executes "level(x)" in gp. Which of course doesn't work. Anyway, I've fixed it by rearranging the ModularForms constructor function a bit, and added a doctest to check that it's fixed.


---

Comment by davidloeffler created at 2009-05-01 11:45:03

patch against 3.4.2.rc0


---

Attachment


---

Attachment

Looks good -- I added one small patch that just slightly moved things around. (Mostly just removed cases where tests would end up getting run several times, even though this code isn't anywhere near performance-critical.)


---

Comment by mabshoff created at 2009-05-11 09:53:35

Resolution: fixed


---

Comment by mabshoff created at 2009-05-11 09:53:35

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
