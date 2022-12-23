# Issue 1400: QuadraticFields and ClassGroups

Issue created by migration from https://trac.sagemath.org/ticket/1400

Original creator: ljpk

Original creation time: 2007-12-04 23:10:59

Assignee: was

SAGE can compute the class group of a quadratic field, but it has issues with computing the order of elements within that class group:

QF.<x>=QuadraticField(-39)
CF=QF.class_group()
CF(QF.ideal(1+x)).order()

gives

NotImplementedErrorTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server2/sage_notebook/worksheets/ljpk/0/code/6.py", line 6, in <module>
    CF(QF.ideal(Integer(1)+x)).order()
  File "/home/sage10/", line 1, in <module>
    
  File "element.pyx", line 1190, in sage.structure.element.MultiplicativeGroupElement.order
  File "element.pyx", line 1130, in sage.structure.element.MonoidElement.multiplicative_order
NotImplementedError


---

Attachment


---

Comment by AlexGhitza created at 2008-04-25 02:49:10

The attached patch adds this functionality for fractional ideals and for their representatives in class groups.


---

Comment by ncalexan created at 2008-04-28 02:29:31

This uses an O(n) algorithm to compute orders.  Don't we have generic BSGS O(sqrt(n)) that would be better here?


---

Comment by craigcitro created at 2008-06-20 04:26:45

Changing keywords from "" to "editor_craigcitro".


---

Comment by mabshoff created at 2008-08-27 07:37:49

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 07:37:49

Fixed via #3913.

Cheers,

Michael
