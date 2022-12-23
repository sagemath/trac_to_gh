# Issue 4329: class numbers of non-maximal orders -- should return NotImplementedError for now

Issue created by migration from https://trac.sagemath.org/ticket/4329

Original creator: was

Original creation time: 2008-10-20 13:36:36

Assignee: was

This is just wrong (and easy to fix):

```
sage: R = ZZ[3*sqrt(-3)]
sage: R.class_number??
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method AbsoluteOrder.class_number of Order in Number Field in a with defining polynomial x^2 + 27>
Namespace:      Interactive
File:           /home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/number_field/order.py
Definition:     R.class_number(self, proof=None)
Source:
    def class_number(self, proof=None):
        """
        EXAMPLES:
            sage: ZZ[2^(1/3)].class_number()
            1
            sage: ZZ[sqrt(-23)].class_number()
            3
        """
        return self.number_field().class_number(proof=proof)   
```


For a non-maximal order, the class_number (and class group) commands should return NotImplementedError, rather than give a wrong or meaningless answer.

To fix this, all you have to do is make these function raise NotImplementedError, except in the case of the maximal order.


---

Attachment

Code looks good.
Confirmed that it worked.
Confirmed that it passes tests.


---

Comment by mabshoff created at 2008-11-15 02:21:51

Replying to [comment:2 shumow]:
> Code looks good.
> Confirmed that it worked.
> Confirmed that it passes tests.

Is that a positive review?

Cheers,

Michael


---

Comment by shumow created at 2008-11-15 08:31:09

Replying to [comment:3 mabshoff]:
> Replying to [comment:2 shumow]:
> > Code looks good.
> > Confirmed that it worked.
> > Confirmed that it passes tests.
> 
> Is that a positive review?
> 
Affirmative


---

Comment by mabshoff created at 2008-11-15 09:53:03

Resolution: fixed


---

Comment by mabshoff created at 2008-11-15 09:53:03

Merged in Sage 3.2.rc1
