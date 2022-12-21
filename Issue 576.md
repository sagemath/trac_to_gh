# Issue 576: hard interrupting a Singular calculation does not kill Singular

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-03 13:59:11

Assignee: was

Consider:


```
sage: P = PolynomialRing(QQ,8,'x')
sage: I = sage.rings.ideal.Cyclic(P)
sage: I.groebner_basis() # calls Singular and takes a long time
```


Now press Ctrl-C and you'll get:


```
Interrupting Singular...
Interrupting Singular...
...
<type 'exceptions.TypeError'>: Restarting Singular 
(WARNING: all variables defined in previous session are now invalid)
```


Singular supposedly got killed but keeps running in background.




---

Comment by mabshoff created at 2007-10-19 18:51:14

I think this is fixed in current Sage due to the signal handler rewrite by Gonzalo and William.

Cheers,

Michael


---

Comment by was created at 2007-10-20 01:07:31

You're right, this is now fixed.


---

Comment by was created at 2007-10-20 01:07:31

Resolution: fixed
