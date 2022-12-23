# Issue 3406: [with patch, needs review] improve TermOrder class

Issue created by migration from https://trac.sagemath.org/ticket/3406

Original creator: malb

Original creation time: 2008-06-12 22:40:27

Assignee: malb

CC:  cremona wstein

** doctest coverage 100%
 * improved documentation
 * more Python-ic interface
 * warning issued if an unknown term ordering is used (this addresses parts of #3383)


---

Comment by craigcitro created at 2008-06-15 21:53:44

Changing keywords from "" to "editor_mhansen".


---

Comment by mabshoff created at 2008-06-23 08:46:34

I am seeing doctest failures:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 11 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 12 doctests failed
```


I am seeing similar issues in #3407.

Cheers,

Michael


---

Comment by malb created at 2008-06-23 17:39:29

fixes the doctest issues in ell_...


---

Attachment

The updated patch fixes the doctest issue. Elliptic curves used an unknown term ordering and the old -- buggy! -- code fell back to 'lex' silently. Now it is 'lex' explicitly, please speak up if that is not what is wanted.


---

Comment by mabshoff created at 2008-06-25 00:07:20

With the last new hunk doctests do pass. Since we are computing GBs in Lex anyway I am giving this a positive review again. 

John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-25 00:14:47

Merged in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-25 00:14:47

Resolution: fixed


---

Comment by cremona created at 2008-06-25 07:46:58

Replying to [comment:6 mabshoff]:
> With the last new hunk doctests do pass. Since we are computing GBs in Lex anyway I am giving this a positive review again. 
> 
> John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.

I think we will not need to use any GB code at all once I have finished.  That was used in code William wrote, which I am rewriting having decided that it was just too much to have three different versions of something (in this case, division polynomials for elliptic curves).

So I see no reason to block 3.0.4 -- unless I have misunderstood the point here!

> 
> Cheers,
> 
> Michael


---

Comment by mabshoff created at 2008-06-25 07:51:34

Replying to [comment:8 cremona]:
> Replying to [comment:6 mabshoff]:

> > John: Should you not intend to compute the GBs with Lex please open a blocker ticket against 3.0.4.
> 
> I think we will not need to use any GB code at all once I have finished.  That was used in code William wrote, which I am rewriting having decided that it was just too much to have three different versions of something (in this case, division polynomials for elliptic curves).
> 
> So I see no reason to block 3.0.4 -- unless I have misunderstood the point here!

John,

I am sure we do understand each other 100% in this case.

Cheers,

Michael
