# Issue 265: Coercion of maxima float with positive exponent to python float

Issue created by migration from Trac.

Original creator: gvanuxem

Original creation time: 2007-02-15 22:39:39

Assignee: was

Here is the output:


sage: maxima("1.7e-17")
 1.7E-17

sage: float (_)
 1.6999999999999999e-17

sage: maxima("1.7e+17")
 1.7E + 17

sage: float (_)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/greg/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in __float__(self)
   1267 
   1268     def __float__(self):
-> 1269         return float(str(self.numer()))
   1270 
   1271     def __len__(self):

<type 'exceptions.ValueError'>: invalid literal for float(): 1.7E + 17


---

Comment by gvanuxem created at 2007-02-15 22:40:38

Changing component from algebraic geometry to interfaces.


---

Comment by was created at 2007-08-18 19:28:47

this works fine in sage-2.8.1.


---

Comment by was created at 2007-08-18 19:28:47

Resolution: fixed
