# Issue 5377: weird output for trivial class group

Issue created by migration from https://trac.sagemath.org/ticket/5377

Original creator: dmharvey

Original creation time: 2009-02-26 00:53:26

Assignee: was


```
sage: K.<a> = NumberField(x^2 + 1)
sage: K.class_group()
Class group of order 1 with structure  of Number Field in a with defining polynomial x^2 + 1
```


There is something missing after "structure".

This is possibly related to #2574 (which is marked as fixed...)



---

Comment by davidloeffler created at 2009-07-21 08:08:06

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:08:06

Changing assignee from was to davidloeffler.


---

Comment by jdemeyer created at 2011-10-09 10:47:31

Seems to be fixed in sage-4.7.2.alpha3.


---

Comment by jdemeyer created at 2011-10-09 10:47:31

Resolution: worksforme
