# Issue 7959: the docstring for the associated_primes method on multivariate polynomial ideals is wrong

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-17 00:13:29

Assignee: malb

The docstring for associated_primes claims it returns a list of pairs (I,P), but in fact it *just* returns the P.  So this is wrong. 


```
    `@`require_field
    `@`redSB
    def associated_primes(self, algorithm='sy'):
        r"""
        Return a list of primary ideals (and their associated primes) such
        that their intersection is `I` = ``self``.
        
        An ideal `Q` is called primary if it is a proper ideal of
        the ring `R` and if whenever `ab \in Q` and
        `a \not\in Q` then `b^n \in Q` for some
        `n \in \ZZ`.
        
        If `Q` is a primary ideal of the ring `R`, then the
        radical ideal `P` of `Q`, i.e.
        `P = \{a \in R, a^n \in Q\}` for some
        `n \in \ZZ`, is called the
        *associated prime* of `Q`.
        
        If `I` is a proper ideal of the ring `R` then there
        exists a decomposition in primary ideals `Q_i` such that
        
        
        -  their intersection is `I`
        
        -  none of the `Q_i` contains the intersection of the
           rest, and
        
        -  the associated prime ideals of `Q_i` are pairwise
           different.
        
        
        This method returns the associated primes of the `Q_i`.
        
        INPUT:
        
        
        -  ``algorithm`` - string:
        
        -  ``'sy'`` - (default) use the shimoyama-yokoyama algorithm
        
        -  ``'gtz'`` - use the gianni-trager-zacharias algorithm
        
        
        OUTPUT:
        
        -  ``list`` - a list of primary ideals and their
           associated primes [(primary ideal, associated prime), ...]
        
        EXAMPLES::
        
            sage: R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
            sage: p = z^2 + 1; q = z^3 + 2
            sage: I = (p*q^2, y-z^2)*R
            sage: pd = I.associated_primes(); pd
            [Ideal (z^3 + 2, y - z^2) of Multivariate Polynomial Ring in x, y, z over Rational Field,
             Ideal (z^2 + 1, y + 1) of Multivariate Polynomial Ring in x, y, z over Rational Field]
```



---

Attachment

Your patch seems to leave the wrong objects in the docstring. I'm attaching a new patch that inverts that, and also changes a second occurence of the description of the output.


---

Comment by wjp created at 2010-01-17 22:12:01

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-01-18 10:16:26

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-18 23:52:50

Resolution: fixed
