# Issue 6837: Implementation of twisting modular forms by Dirichlet characters

archive/issues_006837.json:
```json
{
    "body": "Assignee: @craigcitro\n\nIn Koblitz's book \"Introduction to Elliptic Curves and Modular Forms\", Proposition III.3.17, it is proved that if f(q)=sum_{n=0}^infinity a_n q^n is the Fourier expansion of a modular form in M_k(Gamma_0(M),chi) and chi_1 is a primitive Dirichlet character modulo N, then f_chi(q)=sum_{n=0}^infinity \\chi_1(n) a_n q^n is a modular form in M_k(\\Gamma_0(MN<sup>2),\\chi\\chi_1</sup>2). This is a proposed method for objects of type 'sage.modular.modform.element.ModularFormElement' which will create f_\\chi given f and chi.\n\n\n```\ndef twist(f,chi):\n        r\"\"\"\n        This function returns the twist of the modular form f by the Dirichlet character chi\n\n        INPUT:\n\n        - ``f`` - a modular form\n\n        - ``chi`` - a Dirichlet character\n\n        OUTPUT:\n\n        f_\\chi, the twist of f by chi; if f(q)=sum_{n=0}^infty a_n q^n, then f_chi(q)=sum_{n=0}^infty chi(n) a_n q^n ([Koblitz]).\n\n        EXAMPLES:\n\n        Here is a basic example:\n\n        ::\n\n                sage: f=CuspForms(11,2).0\n                sage: f.q_expansion(6)\n                q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)\n                sage: eps=DirichletGroup(3).0\n                sage: f.twist(eps)\n                q + 2*q^2 + 2*q^4 - q^5 + O(q^6)\n\n        ::\n\n        NOTES:\n        This function is rather slow when chi is not a quadratic character; this may be improved with a new definition of the Sturm bound.\n\n        REFERENCES:\n\n        - [Koblitz], Neal Koblitz, \"Introduction to Elliptic Curves and Modular Forms\", Springer GTM 97, 1993, Proposition III.3.17.\n\n        AUTHORS:\n\n        - L. J. P. Kilford (2009-08-28)\n\n        \"\"\"\n        DG_MNsq=DirichletGroup(f.level()*chi.modulus()^2)\n        basering=DG_MNsq.base_ring()\n        M_k_MNsq=ModularForms(DG_MNsq(self.character())*DG_MNsq(chi)^2,self.weight(),base_ring=basering)\n        bound=M_k_MNsq.sturm_bound()+1\n        PSR.<q>=PowerSeriesRing(DG_MNsq.base_ring())\n        f_twist=PSR([self[i]*chi(i) for i in xrange(0,bound+2)])+O(q^bound)\n        return M_k_MNsq(f_twist)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6837\n\n",
    "created_at": "2009-08-28T15:38:45Z",
    "labels": [
        "component: modular forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.6",
    "title": "Implementation of twisting modular forms by Dirichlet characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6837",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
}
```
Assignee: @craigcitro

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

Issue created by migration from https://trac.sagemath.org/ticket/6837





---

archive/issue_comments_056270.json:
```json
{
    "body": "I have taken Lloyd's code, modified it so it can be run from the Sage library and for readability, and put it in the attached patch.",
    "created_at": "2010-01-03T11:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56270",
    "user": "https://github.com/aghitza"
}
```

I have taken Lloyd's code, modified it so it can be run from the Sage library and for readability, and put it in the attached patch.



---

archive/issue_comments_056271.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T11:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56271",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056272.json:
```json
{
    "body": "Changing keywords from \"\" to \"modular form twist character\".",
    "created_at": "2010-01-03T11:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56272",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "modular form twist character".



---

archive/issue_comments_056273.json:
```json
{
    "body": "Attachment [trac_6837.patch](tarball://root/attachments/some-uuid/ticket6837/trac_6837.patch) by @aghitza created at 2010-01-03 11:27:50",
    "created_at": "2010-01-03T11:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56273",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_6837.patch](tarball://root/attachments/some-uuid/ticket6837/trac_6837.patch) by @aghitza created at 2010-01-03 11:27:50



---

archive/issue_comments_056274.json:
```json
{
    "body": "Note that the code is indeed rather slow, even with the patch at #6836.  But since this is new functionality, I think it's ok to first get it in like this and then speed it up if possible.",
    "created_at": "2010-01-04T03:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56274",
    "user": "https://github.com/aghitza"
}
```

Note that the code is indeed rather slow, even with the patch at #6836.  But since this is new functionality, I think it's ok to first get it in like this and then speed it up if possible.



---

archive/issue_comments_056275.json:
```json
{
    "body": "* There should be an empty line before `... math:`.\n\n  * I don't know why, but Lloyd's first names are transformed into 12. 10. 16. in the reference page.\n\n  * I think one should catch the case when the conductor of the character is not coprime to the level of the modular form. Note that the if you twist a form that has been twisted by chi with chi again, the level should go down not up. I believe that the correct assumption are in [Mazur-Tate-Teitelbaum].\n\n\n```\nsage: M = CuspForms(11,2)\nsage: f = M.0\nsage: chi = DirichletGroup(3).0\nsage: fchi = f.twist(chi)\nsage: fchi\nq + 2*q^2 + 2*q^4 - q^5 + O(q^6)\nsage: fchi.twist(chi)\n```\n\n\n\n* If the form is on Gamma_0(N) and one twists with a character modulo N, I think it should change the Nebetypus, no ?",
    "created_at": "2010-02-01T17:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56275",
    "user": "https://github.com/categorie"
}
```

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

archive/issue_comments_056276.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-01T17:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56276",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056277.json:
```json
{
    "body": "Replying to [comment:3 wuthrich]:\n\n>  * I think one should catch the case when the conductor of the character is not coprime to the level of the modular form. Note that the if you twist a form that has been twisted by chi with chi again, the level should go down not up. I believe that the correct assumption are in [Mazur-Tate-Teitelbaum].\n\nI don't agree: twisting by chi and then by chi<sup>-1</sup> shouldn't give the original answer back again, it should give some oldform at possibly higher level, whose q-expansion has zeros at coefficients that aren't prime to the conductor of chi. Looking for some associated minimal-level form is tempting, but it's not going to make sense when the original form f is not an eigenform.\n\nThere is a question, however, as to what level the answer should be returned at when M and N are not coprime. I would contend that the answer should be returned as an element of the modular forms space of level LCM(N, N'M, M<sup>2</sup>) where N is the level of f, N' is the conductor of the character of f, and M is the conductor of the character we're twisting by. This is more or less the best bound you can get without knowing more about f; see Atkin and Li, \"Twists of newforms and pseudo-eigenvalues of W-operators\". (Perhaps there should be an optional argument for what level to look in, so the user can override the default.)\n\n>  * If the form is on Gamma_0(N) and one twists with a character modulo N, I think it should change the Nebetypus, no ?\n\nIt does, see line 460 of the patch. This is just a notational issue, one man's M_k(Gamma_0(N), chi) is another man's M_k(Gamma_1(N), chi).",
    "created_at": "2010-04-12T15:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56277",
    "user": "https://github.com/loefflerd"
}
```

Replying to [comment:3 wuthrich]:

>  * I think one should catch the case when the conductor of the character is not coprime to the level of the modular form. Note that the if you twist a form that has been twisted by chi with chi again, the level should go down not up. I believe that the correct assumption are in [Mazur-Tate-Teitelbaum].

I don't agree: twisting by chi and then by chi<sup>-1</sup> shouldn't give the original answer back again, it should give some oldform at possibly higher level, whose q-expansion has zeros at coefficients that aren't prime to the conductor of chi. Looking for some associated minimal-level form is tempting, but it's not going to make sense when the original form f is not an eigenform.

There is a question, however, as to what level the answer should be returned at when M and N are not coprime. I would contend that the answer should be returned as an element of the modular forms space of level LCM(N, N'M, M<sup>2</sup>) where N is the level of f, N' is the conductor of the character of f, and M is the conductor of the character we're twisting by. This is more or less the best bound you can get without knowing more about f; see Atkin and Li, "Twists of newforms and pseudo-eigenvalues of W-operators". (Perhaps there should be an optional argument for what level to look in, so the user can override the default.)

>  * If the form is on Gamma_0(N) and one twists with a character modulo N, I think it should change the Nebetypus, no ?

It does, see line 460 of the patch. This is just a notational issue, one man's M_k(Gamma_0(N), chi) is another man's M_k(Gamma_1(N), chi).



---

archive/issue_comments_056278.json:
```json
{
    "body": "Converted the patch into a Git branch.",
    "created_at": "2015-03-30T08:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56278",
    "user": "https://github.com/pjbruin"
}
```

Converted the patch into a Git branch.



---

archive/issue_comments_056279.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-30T09:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56279",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056280.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-30T12:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56280",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056281.json:
```json
{
    "body": "I think Chris's comment:3 and David's comment:4 are adressed by the latest series of commits.",
    "created_at": "2015-03-30T12:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56281",
    "user": "https://github.com/pjbruin"
}
```

I think Chris's comment:3 and David's comment:4 are adressed by the latest series of commits.



---

archive/issue_comments_056282.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-03-30T12:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56282",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056283.json:
```json
{
    "body": "Follow-up ticket: #18086 (Twists of newforms).",
    "created_at": "2015-03-30T13:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56283",
    "user": "https://github.com/pjbruin"
}
```

Follow-up ticket: #18086 (Twists of newforms).



---

archive/issue_comments_056284.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-30T15:31:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56284",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056285.json:
```json
{
    "body": "bad use of unicode dash in one reference : \n\n```\nInventiones math. 48 (1978), 221\u00e2\u20ac\u201c243.\n```\n\nshould just be\n\n```\nInventiones Math. 48 (1978), 221-243.\n```\n",
    "created_at": "2015-04-02T19:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56285",
    "user": "https://github.com/fchapoton"
}
```

bad use of unicode dash in one reference : 

```
Inventiones math. 48 (1978), 221â€“243.
```

should just be

```
Inventiones Math. 48 (1978), 221-243.
```




---

archive/issue_comments_056286.json:
```json
{
    "body": "Replying to [comment:16 chapoton]:\n> bad use of unicode dash in one reference\nI can fix this of course, but why is it bad?  The file is declared as utf-8 on the first line.",
    "created_at": "2015-04-02T19:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56286",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:16 chapoton]:
> bad use of unicode dash in one reference
I can fix this of course, but why is it bad?  The file is declared as utf-8 on the first line.



---

archive/issue_comments_056287.json:
```json
{
    "body": "Oh, well, this is not *that* bad. My bot just found that, so I reported it. I understand that unicode is justified sometimes (say for Poincar\u00e9) but not here.\n\nAnd sometimes also this kind of dash confuses the doc bulding, but apparently not here.",
    "created_at": "2015-04-02T20:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56287",
    "user": "https://github.com/fchapoton"
}
```

Oh, well, this is not *that* bad. My bot just found that, so I reported it. I understand that unicode is justified sometimes (say for Poincaré) but not here.

And sometimes also this kind of dash confuses the doc bulding, but apparently not here.



---

archive/issue_comments_056288.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-02T20:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56288",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056289.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-04-08T11:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56289",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056290.json:
```json
{
    "body": "I tested this and all test passed. However, I am not sure about the implementation. There is only one (rather trivial) test in the documentations. So I played around a bit.\n\nCurrently it fails if the form is a `NewForm` as explained in  #18086 .\n\nIt also fails if f does not have a neben character:\n\n```\nsage: M = CuspForms(Gamma1(13),4)\nsage: f = M.basis()[13]\nsage: G = DirichletGroup(11)\nsage: chi = G.0\nsage: f.twist(chi)\n```\n\n\ngives `ValueError: Form is not an eigenvector for <2>`\n\nSimilarly it fails when the character has values outside the field of coefficients of f:\n\n\n```\nsage: M = CuspForms(Gamma0(37),2)\nsage: f = M.0\nsage: G = DirichletGroup(11)\nsage: chi = G.0\nsage: chi\nDirichlet character modulo 11 of conductor 11 mapping 2 |--> zeta10\nsage: f.twist(chi)\n```\n\n\nreturns `ValueError: No coercion defined`.\n\nNow some of these problems may be due to user choosing bad input. But that should be checked in the function or (at the least) be documented. Alas, I revert it to needs work.\n\nHowever I do thank you for picking up this old ticket and working on it. I really would like to see this work in Sage. Thanks for picking up on David Loeffler's comments.",
    "created_at": "2015-04-08T11:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56290",
    "user": "https://github.com/categorie"
}
```

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

archive/issue_comments_056291.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-09T09:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56291",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_056292.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-04-09T09:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56292",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056293.json:
```json
{
    "body": "Replying to [comment:20 wuthrich]:\n> I tested this and all test passed. However, I am not sure about the implementation. There is only one (rather trivial) test in the documentations. So I played around a bit.\nThanks!\n\n> Currently it fails if the form is a `NewForm` as explained in  #18086 .\nI moved the method to the class `ModularFormElement`, so that `Newform` does not even have a `twist` method anymore until #18086.\n\n> It also fails if f does not have a neben character:\n> [...]\n> Similarly it fails when the character has values outside the field of coefficients of f:\n> [...]\nBoth of these should now be fixed.  I added different examples to the doctests than the ones you gave because they seemed to take forever.",
    "created_at": "2015-04-09T09:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56293",
    "user": "https://github.com/pjbruin"
}
```

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

archive/issue_comments_056294.json:
```json
{
    "body": "Excellent. Thanks a lot that was what I was hoping for.\n\nAll fine and tests pass.",
    "created_at": "2015-04-09T14:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56294",
    "user": "https://github.com/categorie"
}
```

Excellent. Thanks a lot that was what I was hoping for.

All fine and tests pass.



---

archive/issue_comments_056295.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-09T14:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56295",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007070.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-04-15T06:07:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6837#event-7070"
}
```



---

archive/issue_comments_056296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-15T06:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6837#issuecomment-56296",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
