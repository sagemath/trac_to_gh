# Issue 4497: Implement the function log10

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-11-11 23:19:57

Assignee: somebody

"very useful for those who use a lot logarithmic scale" - Ronan Paixão


---

Comment by mabshoff created at 2008-11-12 14:17:28

Why this ticket? We already have

```
sage: log_b?
Type:		function
Base Class:	<type 'function'>
String Form:	<function log at 0x29b33f0>
Namespace:	Interactive
File:		/Users/michaelabshoff/Desktop/sage-3.1.3.rc0/local/lib/python2.5/site-packages/sage/misc/functional.py
Definition:	log_b(x, b=None)
Docstring:
    
        Return the log of x to the base b.  The default base is e.
    
        INPUT:
            x -- number
            b -- base (default: None, which means natural log)
            
        OUTPUT:
            number
    
        NOTE: In Magma, the order of arguments is reversed from in
        SAGE, i.e., the base is given first.  We use the opposite
        ordering, so the base can be viewed as an optional second
        argument.
```

One could obviously implement log10, but why pollute the global namespace even more?

Cheers,

Michael


---

Comment by was created at 2008-11-12 17:09:38

Pari, Maple, and Mathematica all don't do this.   We should not do this in Sage either. It is trivial to implement in terms of existing functions.


---

Comment by was created at 2008-11-12 17:09:38

Resolution: invalid
