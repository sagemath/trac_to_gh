# Issue 9258: problem with converting FriCAS domains to Sage objects

Issue created by migration from Trac.

Original creator: awebb

Original creation time: 2010-06-18 07:11:40

Assignee: tbd

Fricas seems to have an api change which breaks a few tests in fricas.py.


```

"""
        A helper function for converting FriCAS domains to the corresponding
        Sage object.
        
        EXAMPLES::
        
            sage: fricas('Integer').sage() #optional - fricas
            Integer Ring
            sage: fricas('Fraction Integer').sage() #optional - fricas
            Rational Field
            sage: fricas('DoubleFloat').sage() #optional - fricas
            Real Double Field

        """
```


These now give either a different return value or simply results in raising a NotImplementedError.


---

Attachment


---

Comment by mhansen created at 2010-06-27 20:13:41

Changing status from new to needs_review.


---

Comment by awebb created at 2010-07-02 12:01:12

Changing status from needs_review to positive_review.


---

Comment by awebb created at 2010-07-02 12:01:12

That was easier than I thought it would be. :-)

Adam


---

Comment by mpatel created at 2010-07-20 10:04:32

Resolution: fixed
