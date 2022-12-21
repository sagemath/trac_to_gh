# Issue 1680: Unusual behaviour of the built-in complex numbers

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-01-04 17:17:29

Assignee: malb

CC:  mhansen mvngu

SAGE has a built-in copy of the complex numbers, so it knows what I is. However, one gets slightly odd behaviour from this:

`sage: (1+I)^2 - 2*I`

`(1+I)^2 - 2*I`

and one has to use the .expand() command to get the correct answer 2*I. This is not the behaviour of a user-defined quadratic field, which automatically evaluates such things. I think that the computation should resolve to 0 without having to be expanded.


---

Comment by was created at 2008-01-14 05:39:31

This behavior of the symbolic I is imposed by Maxima.  I do not know if there is any way to change it to behave like you want.   You might want to use the I of the number field QQ(sqrt(-1))...  


```
sage: I = NumberField(x^2 + 1, 'I').gen()
sage: (1+I)^2 - 2*I
0
```


Some day (who knows when) probably the Sage "I" will be the number field I, but where the number field is equipped with a canonical embedding in the symbolic ring, and then your example above will work as you want.  I don't know when this will happen.  It might not be too hard to implement. 

William


---

Comment by robertwb created at 2008-01-15 06:13:07

This is certainly on the TODO list... currently for a number field 


```
sage: I = NumberField(x^2 + 1, 'I').gen()
```


it doesn't know whether to send I to -I or I in `CC`, and a mechanism for this needs to be implemented.


---

Comment by robertwb created at 2008-01-15 06:13:07

Changing assignee from malb to robertwb.


---

Comment by robertwb created at 2009-05-18 22:20:43

Number fields now have embedddings, and these are used by the Pynac Symbolics. When that goes in, this ticket should be closed.


---

Comment by jhpalmieri created at 2009-07-22 02:26:43

I think this can be closed now.


---

Comment by jason created at 2009-10-06 19:28:45

Please note the request to close this.


---

Comment by mhansen created at 2009-10-07 04:03:58

Yep, this has been fixed.


---

Comment by mhansen created at 2009-10-07 04:03:58

Resolution: fixed
