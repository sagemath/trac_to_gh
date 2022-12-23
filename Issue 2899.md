# Issue 2899: Make RDF round and friends return Integers

Issue created by migration from https://trac.sagemath.org/ticket/2899

Original creator: jason

Original creation time: 2008-04-12 16:09:26

Assignee: robertwb


```
> Also, round(RR(3.0)) returns an Integer...should RDF behave the same
> > way? (currently round(RDF(3.0)) returns an RDF).

We recently changed round, floor, ceiling, and trunc on RR to return
integers; yes, I think the corresponding RDF methods should change as
well.

Carl
```




---

Comment by jason created at 2008-04-13 04:39:18

The fix for #2898 will fix this.


---

Attachment

This makes floor and ceil do what I expect for RIF.  I believe that #2898 does make RDF work.


---

Comment by craigcitro created at 2008-11-27 08:11:11

I just tried to apply this against 3.2, and it fails. It's just a matter of moving the doctests around, I think.


---

Comment by robertwb created at 2009-05-18 21:45:45

Resolution: worksforme


---

Comment by robertwb created at 2009-05-18 21:45:45

This appears to have already been fixed. 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.4.2, Release Date: 2009-05-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: a = RDF(3.4)

sage: a.round(), a.floor(), a.ceil()
 (3, 3, 4)

```



---

Comment by mabshoff created at 2009-05-18 21:59:34

Did someone add a doctest? Otherwise this should not have been closed.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 04:56:59

Resolution changed from worksforme to 


---

Comment by mabshoff created at 2009-05-19 04:56:59

Reopening until someone either points to a doctests or post a doctest patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 04:56:59

Changing status from closed to reopened.


---

Comment by ncalexan created at 2009-05-19 16:31:15

There are doctests for RDF for sure:


```

    def round(self):
        """
        Given real number x, rounds up if fractional part is greater than
        .5, rounds down if fractional part is less than .5.

        EXAMPLES::
        
            sage: RDF(0.49).round()
            0
            sage: a=RDF(0.51).round(); a
            1
        """
        return Integer(round(self._value))

    def floor(self):
        """
        Returns the floor of this number
        
        EXAMPLES::
        
            sage: RDF(2.99).floor()
            2
            sage: RDF(2.00).floor()
            2
            sage: RDF(-5/2).floor()
            -3
        """
        return Integer(math.floor(self._value))

    def ceil(self):
        """
        Returns the ceiling of this number
        
        OUTPUT: integer
        
        EXAMPLES::
        
            sage: RDF(2.99).ceil()
            3
            sage: RDF(2.00).ceil()
            2
            sage: RDF(-5/2).ceil()
            -2
        """
        return Integer(math.ceil(self._value))
```



---

Comment by mabshoff created at 2009-05-19 16:33:25

Resolution: fixed


---

Comment by mabshoff created at 2009-05-19 16:33:25

Excellent. Closed as fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 20:48:17

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-05-19 20:48:17

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-05-19 20:48:17

Wait. There are doctests via Nick's ticket, but that patch has not been merged into the Sage library, but fixed in some other way, i.e. the symbolics switch in 4.0. I assume.

In that case we might still need doctests, so until this is sorted out I am reopening this again :(

Cheers,

Michael


---

Comment by robertwb created at 2010-01-16 23:47:00

There are doctests.


---

Comment by robertwb created at 2010-01-16 23:47:00

Resolution: fixed
