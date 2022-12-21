# Issue 264: Coercion of axiom Float to python float

Issue created by migration from Trac.

Original creator: gvanuxem

Original creation time: 2007-02-15 22:32:46

Assignee: was

Here is the output of this type of coercion:

sage: float axiom(1.7)
----> float(axiom(RealNumber('1.7')))
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/greg/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py in __float__(self)
    422 
    423     def __float__(self):
--> 424         return float(str(self.numer()))
    425 
    426     def __len__(self):

<type 'exceptions.ValueError'>: invalid literal for float(): float(250875719402449901978,-67,2)

The problem is that the Axiom Float is coerced to InputForm and in this format (actually) the internal representation of this Float is obtained : 250875719402449901978*2**-67.


---

Comment by was created at 2007-10-21 02:01:27

Resolution: fixed


---

Comment by was created at 2007-10-21 02:01:27

This works fine in sage-2.8.8.
