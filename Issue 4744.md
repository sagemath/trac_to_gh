# Issue 4744: [with patch, needs review] congruence number for elliptic curves

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-12-08 22:44:35

Assignee: tbd

CC:  was


```
            sage: E = EllipticCurve('37a')
            sage: E.congruence_number()
            2
            sage: E = EllipticCurve('54b')
            sage: E.congruence_number()
            6
            sage: E.modular_degree()
            2
            sage: E = EllipticCurve('242a1')
            sage: E.modular_degree()
            16
            sage: E.congruence_number()  # long time
            176
```



---

Comment by wuthrich created at 2008-12-09 00:17:16

Changing component from algebra to number theory.


---

Comment by wuthrich created at 2008-12-09 00:17:16

I think that the docstring should at least contain the definition of congruence_number, not only a conjecture of what it should be and some examples.


---

Comment by wuthrich created at 2008-12-09 00:17:16

Changing assignee from tbd to was.


---

Comment by wuthrich created at 2008-12-09 00:17:16

Changing type from defect to enhancement.


---

Comment by was created at 2008-12-09 22:17:40

Get rid of "$0 \le " in the conjecture, since that part of the inequality is an old theorem of ribet, i.e., that modular degree divides congruence modulus.


---

Comment by robertwb created at 2008-12-10 03:37:31

I updated the patch as per both of your recommendations. I also fixed a bug that prevented one from computing the (trivial) congruence_number when E was the only thing in the decomposition of J_0(N).


---

Comment by mabshoff created at 2008-12-10 09:11:59

With this patch applied there is one tiny cosmetic doctest failure:

```
sage -t  "devel/sage/sage/modular/modsym/space.py"          
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/modular/modsym/space.py", line 784, in __main__.example_27
Failed example:
    V._q_expansion_module_integral(Integer(5))###line 905:_sage_    >>> V._q_expansion_module_integral(5)
Expected:
    Free module of degree 5 and rank 0 over Integer Ring
    Echelon basis matrix:
    [ ]
Got:
    Free module of degree 5 and rank 0 over Integer Ring
    Echelon basis matrix:
    []
**********************************************************************
```


Cheers,

Michael


---

Comment by was created at 2008-12-10 12:21:09

Since the modular degree is insanely fast to compute, maybe you could also throw in a check that it divides the congruence number?  I.e., in the code, right after computing the congruence number, actually compute the modular degree and check divisibility. 

Also, in the square-free case, since it is *theorem* that the modular degree equals the congruence modulus, and the modular degree can be computed a bazillion times faster, maybe just return it instead?  I.e., don't do the modular symbols computation at all in the non-square-free case.  One could have an optional algorithm= flag that could force doing the super-slow modular symbols calculation in all cases, but it is silly to have it as the default.


---

Attachment

OK, I've updated the patch again.


---

Comment by was created at 2008-12-12 17:41:06

REFEREE REPORT:

Perfect, aside from one typo, where "Ribit" should be "Ribet".

Once that typo is fixed, "positive review"!


---

Attachment

The only change to this patch vs. Robert's is fixing the typo. All credit still goes to RobertWB


---

Comment by mabshoff created at 2008-12-12 17:45:42

I fixed the typo in 4744-congruence-number.2.patch, so positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-12 17:49:45

Resolution: fixed


---

Comment by mabshoff created at 2008-12-12 17:49:45

Merged in Sage 3.2.2.alpha2


---

Comment by craigcitro created at 2008-12-13 10:21:31

One more small typo: it's Petersson, not Peterson.


---

Comment by mabshoff created at 2008-12-13 10:33:40

Typo fix by Craig Citro


---

Attachment

Merged trac_4744-typo-fix.patch in Sage 3.2.2 to fix the typo pointed out by Craig Citro.

Cheers,

Michael
