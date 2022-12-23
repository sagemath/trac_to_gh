# Issue 6837: Implementation of twisting modular forms by Dirichlet characters

Issue created by migration from https://trac.sagemath.org/ticket/6837

Original creator: ljpk

Original creation time: 2009-08-28 15:38:45

Assignee: craigcitro

In Koblitz's book "Introduction to Elliptic Curves and Modular Forms", Proposition III.3.17, it is proved that if f(q)=sum_{n=0}^infinity a_n q^n is the Fourier expansion of a modular form in M_k(Gamma_0(M),chi) and chi_1 is a primitive Dirichlet character modulo N, then f_chi(q)=sum_{n=0}^infinity \chi_1(n) a_n q^n is a modular form in M_k(\Gamma_0(MN<sup>2),\chi\chi_1</sup>2). This is a proposed method for objects of type 'sage.modular.modform.element.ModularFormElement' which will create f_\chi given f and chi.


```
def twist(f,chi):
        r"""
        This function returns the twist of the modular form f by the Dirichlet character chi

        INPUT:

        - ``f`` - a modular form

        - ``chi`` - a Dirichlet character

        OUTPUT:

        f_\chi, the twist of f by chi; if f(q)=sum_{n=0}^infty a_n q^n, then f_chi(q)=sum_{n=0}^infty chi(n) a_n q^n ([Koblitz]).

        EXAMPLES:

        Here is a basic example:

        ::

                sage: f=CuspForms(11,2).0
                sage: f.q_expansion(6)
                q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
                sage: eps=DirichletGroup(3).0
                sage: f.twist(eps)
                q + 2*q^2 + 2*q^4 - q^5 + O(q^6)

        ::

        NOTES:
        This function is rather slow when chi is not a quadratic character; this may be improved with a new definition of the Sturm bound.

        REFERENCES:

        - [Koblitz], Neal Koblitz, "Introduction to Elliptic Curves and Modular Forms", Springer GTM 97, 1993, Proposition III.3.17.

        AUTHORS:

        - L. J. P. Kilford (2009-08-28)

        """
        DG_MNsq=DirichletGroup(f.level()*chi.modulus()^2)
        basering=DG_MNsq.base_ring()
        M_k_MNsq=ModularForms(DG_MNsq(self.character())*DG_MNsq(chi)^2,self.weight(),base_ring=basering)
        bound=M_k_MNsq.sturm_bound()+1
        PSR.<q>=PowerSeriesRing(DG_MNsq.base_ring())
        f_twist=PSR([self[i]*chi(i) for i in xrange(0,bound+2)])+O(q^bound)
        return M_k_MNsq(f_twist)


---

Comment by AlexGhitza created at 2010-01-03 11:27:24

I have taken Lloyd's code, modified it so it can be run from the Sage library and for readability, and put it in the attached patch.


---

Comment by AlexGhitza created at 2010-01-03 11:27:24

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-01-03 11:27:24

Changing keywords from "" to "modular form twist character".


---

Attachment


---

Comment by AlexGhitza created at 2010-01-04 03:31:06

Note that the code is indeed rather slow, even with the patch at #6836.  But since this is new functionality, I think it's ok to first get it in like this and then speed it up if possible.


---

Comment by wuthrich created at 2010-02-01 17:18:28

* There should be an empty line before `... math:`.

 * I don't know why, but Lloyd's first names are transformed into 12. 10. 16. in the reference page.

 * I think one should catch the case when the conductor of the character is not coprime to the level of the modular form. Note that the if you twist a form that has been twisted by chi with chi again, the level should go down not up. I believe that the correct assumption are in [Mazur-Tate-Teitelbaum].


```
sage: M = CuspForms(11,2)
sage: f = M.0
sage: chi = DirichletGroup(3).0
sage: fchi = f.twist(chi)
sage: fchi
q + 2*q^2 + 2*q^4 - q^5 + O(q^6)
sage: fchi.twist(chi)
```



 * If the form is on Gamma_0(N) and one twists with a character modulo N, I think it should change the Nebetypus, no ?


---

Comment by wuthrich created at 2010-02-01 17:18:28

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-04-12 15:10:20

Replying to [comment:3 wuthrich]:

>  * I think one should catch the case when the conductor of the character is not coprime to the level of the modular form. Note that the if you twist a form that has been twisted by chi with chi again, the level should go down not up. I believe that the correct assumption are in [Mazur-Tate-Teitelbaum].

I don't agree: twisting by chi and then by chi<sup>-1</sup> shouldn't give the original answer back again, it should give some oldform at possibly higher level, whose q-expansion has zeros at coefficients that aren't prime to the conductor of chi. Looking for some associated minimal-level form is tempting, but it's not going to make sense when the original form f is not an eigenform.

There is a question, however, as to what level the answer should be returned at when M and N are not coprime. I would contend that the answer should be returned as an element of the modular forms space of level LCM(N, N'M, M<sup>2</sup>) where N is the level of f, N' is the conductor of the character of f, and M is the conductor of the character we're twisting by. This is more or less the best bound you can get without knowing more about f; see Atkin and Li, "Twists of newforms and pseudo-eigenvalues of W-operators". (Perhaps there should be an optional argument for what level to look in, so the user can override the default.)

>  * If the form is on Gamma_0(N) and one twists with a character modulo N, I think it should change the Nebetypus, no ?

It does, see line 460 of the patch. This is just a notational issue, one man's M_k(Gamma_0(N), chi) is another man's M_k(Gamma_1(N), chi).


---

Comment by pbruin created at 2015-03-30 08:22:48

Converted the patch into a Git branch.


---

Comment by git created at 2015-03-30 09:06:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-30 12:09:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2015-03-30 12:11:35

I think Chris's comment:3 and David's comment:4 are adressed by the latest series of commits.


---

Comment by pbruin created at 2015-03-30 12:11:35

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2015-03-30 13:02:53

Follow-up ticket: #18086 (Twists of newforms).


---

Comment by git created at 2015-03-30 15:31:31

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-04-02 19:37:30

bad use of unicode dash in one reference : 

```
Inventiones math. 48 (1978), 221â€“243.
```

should just be

```
Inventiones Math. 48 (1978), 221-243.
```



---

Comment by pbruin created at 2015-04-02 19:45:26

Replying to [comment:16 chapoton]:
> bad use of unicode dash in one reference
I can fix this of course, but why is it bad?  The file is declared as utf-8 on the first line.


---

Comment by chapoton created at 2015-04-02 20:00:46

Oh, well, this is not *that* bad. My bot just found that, so I reported it. I understand that unicode is justified sometimes (say for Poincaré) but not here.

And sometimes also this kind of dash confuses the doc bulding, but apparently not here.


---

Comment by git created at 2015-04-02 20:16:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by wuthrich created at 2015-04-08 11:58:09

Changing status from needs_review to needs_work.


---

Comment by wuthrich created at 2015-04-08 11:58:09

I tested this and all test passed. However, I am not sure about the implementation. There is only one (rather trivial) test in the documentations. So I played around a bit.

Currently it fails if the form is a `NewForm` as explained in  #18086 .

It also fails if f does not have a neben character:

```
sage: M = CuspForms(Gamma1(13),4)
sage: f = M.basis()[13]
sage: G = DirichletGroup(11)
sage: chi = G.0
sage: f.twist(chi)
```


gives `ValueError: Form is not an eigenvector for <2>`

Similarly it fails when the character has values outside the field of coefficients of f:


```
sage: M = CuspForms(Gamma0(37),2)
sage: f = M.0
sage: G = DirichletGroup(11)
sage: chi = G.0
sage: chi
Dirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta10
sage: f.twist(chi)
```


returns `ValueError: No coercion defined`.

Now some of these problems may be due to user choosing bad input. But that should be checked in the function or (at the least) be documented. Alas, I revert it to needs work.

However I do thank you for picking up this old ticket and working on it. I really would like to see this work in Sage. Thanks for picking up on David Loeffler's comments.


---

Comment by git created at 2015-04-09 09:50:16

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2015-04-09 09:53:11

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2015-04-09 09:53:11

Replying to [comment:20 wuthrich]:
> I tested this and all test passed. However, I am not sure about the implementation. There is only one (rather trivial) test in the documentations. So I played around a bit.
Thanks!

> Currently it fails if the form is a `NewForm` as explained in  #18086 .
I moved the method to the class `ModularFormElement`, so that `Newform` does not even have a `twist` method anymore until #18086.

> It also fails if f does not have a neben character:
> [...]
> Similarly it fails when the character has values outside the field of coefficients of f:
> [...]
Both of these should now be fixed.  I added different examples to the doctests than the ones you gave because they seemed to take forever.


---

Comment by wuthrich created at 2015-04-09 14:53:44

Excellent. Thanks a lot that was what I was hoping for.

All fine and tests pass.


---

Comment by wuthrich created at 2015-04-09 14:53:44

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-15 06:07:23

Resolution: fixed
