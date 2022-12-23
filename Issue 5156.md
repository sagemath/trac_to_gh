# Issue 5156: implement computation of the conjectural (analytic) order of Sha for elliptic curves over Heegner quadratic imaginary fields

Issue created by migration from https://trac.sagemath.org/ticket/5156

Original creator: was

Original creation time: 2009-02-02 02:35:56

Assignee: was




---

Attachment


---

Attachment


---

Comment by rlm created at 2009-02-05 18:12:48

Applied to 3.3.alpha2, I get the following errors:


```
**********************************************************************
"sage/schemes/elliptic_curves/ell_rational_field.py", line 4033:
    sage: P = G(E.0) + G(E.1) + G(phi(F.0)); P
Expected:
    (-51/1058*a + 141/1058 : -1581/12167*a - 9912/12167 : 1)            
Got:
    (-867/3872*a - 3615/3872 : -18003/170368*a - 374575/170368 : 1)
**********************************************************************
"sage/schemes/elliptic_curves/ell_rational_field.py", line 4036:
    sage: P.division_points(2)
Expected:
    [(1/2*a - 1/2 : 1/2*a - 5/2 : 1)]                                   
Got:
    [(1/8*a + 5/8 : -5/16*a - 9/16 : 1)]
**********************************************************************
```



---

Comment by rlm created at 2009-02-05 20:12:53

The above errors still happen when applying the patches to 3.3.alpha5.


---

Comment by mabshoff created at 2009-02-07 06:45:21

Should this be a "needs work". Given the above trouble this will likely not make it into 3.3.

Cheers,

Michael


---

Comment by was created at 2009-02-07 19:17:09

Fyi those are harmless errors since choice of basis is not well defined; ie prob. A 64 vs 32 bit problem.  I will post update once i get computer access. Rlm, could you finish the review?


---

Comment by rlm created at 2009-02-07 23:45:46

Replying to [comment:6 was]:
> Fyi those are harmless errors since choice of basis is not well defined; ie prob. A 64 vs 32 bit problem.  I will post update once i get computer access. Rlm, could you finish the review?

Does that mean that `E.0` etc. are not canonically defined? I didn't know that 32/64 bit made a difference there...

Other than this failure, I give it a positive review.


---

Comment by was created at 2009-02-09 15:36:38

> Does that mean that E.0 etc. are not canonically defined? 

Yes. They depend on how the algorithm to compute them runs.  They're just some basis for some abstract-ish abelian group.  

> I didn't know that 32/64 bit made a difference there... 

Not surprisingly, mwrank runs differently on 32 and 64-bit computers.


---

Comment by mabshoff created at 2009-02-09 22:56:22

I changed the subject so this ticket is picked up by the right reports since it is otherwise harder to find for me.

Cheers,

Michael


---

Comment by rlm created at 2009-02-10 20:30:16

The offending doctest is this one:


```
sage: F = E.quadratic_twist(-7)
sage: K = QuadraticField(-7,'a')
sage: G = E.change_ring(K) 
sage: phi = F.change_ring(K).isomorphism_to(G)
sage: P = G(E.0) + G(E.1) + G(phi(F.0)); P
(-51/1058*a + 141/1058 : -1581/12167*a - 9912/12167 : 1)            # 32-bit
(-867/3872*a - 3615/3872 : -18003/170368*a - 374575/170368 : 1)     # 64-bit
sage: P.division_points(2)
[(1/2*a - 1/2 : 1/2*a - 5/2 : 1)]                                   # 32-bit
[(1/8*a + 5/8 : -5/16*a - 9/16 : 1)]                                # 64-bit
```


On both my 32-bit OSX install and 64-bit sage.math, I get the 64-bit answer. Are there any machines where the 32-bit answer occurs?


---

Comment by cremona created at 2009-02-15 17:54:36

On my 32-bit machine I get the so-called 64-bit answer.

I ought to be able to say what might cause mwrank to produce different gens, but I cannot.  As this curve is in the database, then IF you have the large database installed (with gens) it will use those gens and be deterministic, while ELSE it will compute them.

For this doctest I suggest killing the display of P and changing the last line into 

```
sage: len(P.division_points(2))
1
```


By the way, I am worried that part of this patch will conflict with #4274 which affects the same file, parsing the mwrank output, which I reviewed and repatched earlier today, and which mabshoff has already merged.


---

Comment by cremona created at 2009-02-15 18:00:45

PS I meant to say -- beautiful patch!  Useful functions, well implemented and documented.

The function _heegner_index_in_EK() does not really need the Heegned hypothesis, I think.  You do use the fact that K is imaginary quadratic in the algorithm, but that is all.  So you could change checking Heegner hyp. into checking D<0.  It is also tempting to suggest writing a version which works OK for real quadratic extensions, but I cannot think of a situation when that would be used (though I guess that Darmon might!)

John


---

Comment by mabshoff created at 2009-03-25 07:55:28

Any movement here? It seems easy enough to fix by adjusting the doctest.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 07:56:51

This patch needs to be rebased:

```
sage-3.4.1.alpha0/devel/sage$ patch -p1 --dry-run < trac_5156.patch 
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 FAILED at 1350.
Hunk #2 succeeded at 4683 (offset 533 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
```


Cheers,

Michael


---

Attachment

Finally the patch is ready to merge. Merge only the latest patch.


---

Comment by mabshoff created at 2009-04-09 02:09:06

Merged trac_5156-rebased_and_flattened.patch in Sage 3.4.1.rc2. There is some possibility of numerical noise issues, but I guess we can deal with that and William is happy to fix this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 02:09:06

Resolution: fixed
