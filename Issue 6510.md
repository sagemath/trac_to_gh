# Issue 6510: Adds __nonzero__ method to abelian groups

Issue created by migration from Trac.

Original creator: tsutton

Original creation time: 2009-07-10 21:57:38

Assignee: tbd

Keywords: abelian groups


```
 sage: E=EllipticCurve([0,82])
 sage: tor=E.torsion_subgroup()
 sage: if tor:
 ...       print tor.order()
 1
```


We'd like to have tor evaluate to false in boolean context.


---

Attachment


---

Comment by roed created at 2009-07-10 22:12:06

Needs a doctest.


---

Attachment


---

Comment by roed created at 2009-07-11 00:02:19

Looks good.  All tests pass for me.


---

Comment by ylchapuy created at 2009-07-11 12:39:43

Still needs a doctest!


---

Comment by roed created at 2009-07-12 08:13:29

Now includes #indirect doctest


---

Comment by mvngu created at 2009-07-16 14:39:48

What's the real name of tsutton? The real name should be used so we can give proper credit to contributors.


---

Comment by mvngu created at 2009-07-16 14:53:07

I assume that I only need to apply the patch `trac_6510.3.patch`. But why are there three functions `__nonzero__(self)` all of which are the same and reside in the same module, but each block of definition contains different stuff? For example, after applying `trac_6510.3.patch`, I get the following in `sage/groups/abelian_gps/abelian_group.py`:

```
    def __nonzero__(self):
        return len(self.invariants()) != 0

    def __nonzero__(self):
        """                                                                     
        Returns True if this group is nontrivial.                               
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: E = EllipticCurve([0,82])                                     
            sage: T = E.torsion_subgroup()                                      
            sage: bool(T)                                                       
            False                                                               
        """
        return len(self.invariants()) != 0

    def __nonzero__(self):
        """                                                                     
        Returns True if this group is nontrivial.                               
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: E = EllipticCurve([0,82])                                     
            sage: T = E.torsion_subgroup()                                      
            sage: bool(T) # indirect doctest                                    
            False                                                               
        """
        return len(self.invariants()) != 0
```

Choose which block of function definition you want, and upload a new patch. Preferrably, you should replace `trac_6510.3.patch` with your new patch. I'm marking this as needs work. After a new patch is uploaded, positive review can be reinstated.


---

Attachment


---

Comment by roed created at 2009-07-16 18:21:50

Fixed.  tsutton's real name is Taylor Sutton.


---

Comment by mvngu created at 2009-07-16 19:12:27

Merged the patch `trac_6510.3.patch` in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:11:46

Resolution: fixed
