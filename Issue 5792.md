# Issue 5792: Dirichlet character bug

archive/issues_005792.json:
```json
{
    "body": "Assignee: craigcitro\n\nKeywords: dirichlet characters\n\nThis is pretty worrying:\n\n\n```\nsage: half_integral_weight_modform_basis(trivial_character(16), 9, 10)\n---------------------------------------------------------------------------\nKeyError                                  Traceback (most recent call last)\n\n/home/david/.sage/temp/groke/13438/_home_david__sage_init_sage_0.py in <module>()\n\n/home/david/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/modular/modform/half_integral.pyc in half_integral_weight_modform_basis(chi, k, prec)\n    115     chi = chi.minimize_base_ring()\n    116     psi = chi.parent()(DirichletGroup(4, chi.base_ring()).gen())\n--> 117     eps = chi*psi**((k+1) // 2)\n    118     eps = eps.minimize_base_ring()\n    119     M   = constructor.ModularForms(eps, (k+1)//2)\n\n/home/david/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/modular/dirichlet.pyc in __pow__(self, n)\n    463             [1, -1]\n    464         \"\"\"\n--> 465         return DirichletCharacter(self.parent(), n * self.element(), check=False)\n    466\n    467     def _repr_(self):\n\n/home/david/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/modular/dirichlet.pyc in element(self)\n   1447             M    = P._module\n   1448             dlog = P._zeta_dlog\n-> 1449             v = M([dlog[x] for x in self.values_on_gens()])\n   1450             self.__element = v\n   1451             return v\n\nKeyError: -1\n```\n\n\nSo something is going a bit wrong when multiplying trivial_character(16) by another character.\n\nI thought I had fixed this one, as part of #5648: there was a bug with arithmetic operations on characters whose parents had the same moduli but different zeta orders. But it looks like it isn't fixed after all.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5792\n\n",
    "created_at": "2009-04-15T15:55:06Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Dirichlet character bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5792",
    "user": "davidloeffler"
}
```
Assignee: craigcitro

Keywords: dirichlet characters

This is pretty worrying:


```
sage: half_integral_weight_modform_basis(trivial_character(16), 9, 10)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/david/.sage/temp/groke/13438/_home_david__sage_init_sage_0.py in <module>()

/home/david/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/modular/modform/half_integral.pyc in half_integral_weight_modform_basis(chi, k, prec)
    115     chi = chi.minimize_base_ring()
    116     psi = chi.parent()(DirichletGroup(4, chi.base_ring()).gen())
--> 117     eps = chi*psi**((k+1) // 2)
    118     eps = eps.minimize_base_ring()
    119     M   = constructor.ModularForms(eps, (k+1)//2)

/home/david/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/modular/dirichlet.pyc in __pow__(self, n)
    463             [1, -1]
    464         """
--> 465         return DirichletCharacter(self.parent(), n * self.element(), check=False)
    466
    467     def _repr_(self):

/home/david/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/modular/dirichlet.pyc in element(self)
   1447             M    = P._module
   1448             dlog = P._zeta_dlog
-> 1449             v = M([dlog[x] for x in self.values_on_gens()])
   1450             self.__element = v
   1451             return v

KeyError: -1
```


So something is going a bit wrong when multiplying trivial_character(16) by another character.

I thought I had fixed this one, as part of #5648: there was a bug with arithmetic operations on characters whose parents had the same moduli but different zeta orders. But it looks like it isn't fixed after all.

Issue created by migration from https://trac.sagemath.org/ticket/5792





---

archive/issue_comments_045357.json:
```json
{
    "body": "Well, I've tracked down the problem, but I'm not sure what the \"right\" fix is. (There are several possibilities.)\n\nAmusingly, it's not actually the trivial character that causes trouble directly -- it's the other character here. (The exception gets raised trying to raise `psi` above to a power.) Here's what's going on ... the trivial character gets created in the group of characters of conductor 16 and whose only value can be 1:\n\n\n```\nsage: id = trivial_character(16)\nsage: id.parent()\nGroup of Dirichlet characters of modulus 16 over Rational Field\nsage: id.parent().zeta_order()\n1\n```\n\n\nThen the nontrivial character of conductor 4 gets coerced in, which actually works -- but that's the character that causes trouble: \n\n\n```\nsage: H = DirichletGroup(4,base_ring=QQ)\nsage: psi = id.parent()(H.0)\nsage: psi.values()\nBOOM!\n```\n\n\nIn some sense, this is silly: it should at least have `zeta_order` give 2, since there are two roots of unity in `QQ`. However, the other issue is that coercing `H.0` into `id.parent()` should never have worked -- its order doesn't divide the `zeta_order` of `id.parent()`, so it should have died there. Then step 1 is to make the call `id.parent()(H.0)` fail. \n\nOf course, now that just makes the call to `half_integral_weight_modform_basis` fail -- so we need to do something there. We have (at least) two choices:\n\n* change the `trivial_character` call to give `zeta_order=2`\n* change `half_integral.py` so that it calls differently.\n\nI think the first is probably the more pragmatic choice, though maybe less \"philosophically correct\"?\n\nI've attached a patch that does the former.",
    "created_at": "2009-04-16T01:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45357",
    "user": "craigcitro"
}
```

Well, I've tracked down the problem, but I'm not sure what the "right" fix is. (There are several possibilities.)

Amusingly, it's not actually the trivial character that causes trouble directly -- it's the other character here. (The exception gets raised trying to raise `psi` above to a power.) Here's what's going on ... the trivial character gets created in the group of characters of conductor 16 and whose only value can be 1:


```
sage: id = trivial_character(16)
sage: id.parent()
Group of Dirichlet characters of modulus 16 over Rational Field
sage: id.parent().zeta_order()
1
```


Then the nontrivial character of conductor 4 gets coerced in, which actually works -- but that's the character that causes trouble: 


```
sage: H = DirichletGroup(4,base_ring=QQ)
sage: psi = id.parent()(H.0)
sage: psi.values()
BOOM!
```


In some sense, this is silly: it should at least have `zeta_order` give 2, since there are two roots of unity in `QQ`. However, the other issue is that coercing `H.0` into `id.parent()` should never have worked -- its order doesn't divide the `zeta_order` of `id.parent()`, so it should have died there. Then step 1 is to make the call `id.parent()(H.0)` fail. 

Of course, now that just makes the call to `half_integral_weight_modform_basis` fail -- so we need to do something there. We have (at least) two choices:

* change the `trivial_character` call to give `zeta_order=2`
* change `half_integral.py` so that it calls differently.

I think the first is probably the more pragmatic choice, though maybe less "philosophically correct"?

I've attached a patch that does the former.



---

archive/issue_comments_045358.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-16T01:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45358",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_045359.json:
```json
{
    "body": "There is a bit more too this, though.\n\nBasically, the whole Dirichlet character machinery goes a bit mad whenever you have two Dirichlet characters with the same modulus and base ring, but where the zeta orders aren't the same. For a start, the parent DirichletGroups compare as equal but their elements are different -- or at least they will be if we fix the !__call!__ method properly.\n\nSimilarly, arithmetic coercion is screwed up, in some interesting ways:\n\n\n```\nsage: K.<w> = NumberField(x^2 + x + 1)\nsage: G2 = DirichletGroup(7, K, zeta_order=2, zeta=K(-1))\nsage: G3 = DirichletGroup(7, K, zeta_order=3, zeta=w)\nsage: G2.0 * G3.0\n```\n\n\nHere the coercion model will fail miserably to find the right parent. \n\nOne option would be to prevent Dirichlet groups ever being created for which the zeta order is not maximal for the given base ring. This would sort of work, but would restrict us to Dirichlet groups over integral domains (so we can guarantee that the group of roots of unity in the ring is cyclic) and it would make it a pain to implement base extension (at present the base_extend method for DirichletGroup_class just base extends the zeta element it already knows about.\n\nThe alternative is to be \"honest\" and make Dirichlet groups with the same modulus and base ring but different zeta order into genuinely different objects, comparing as unequal and with different string representations. One can then sort out coercion arithmetic using the machinery from sage.categories.pushout; I coded this up as an experiment (creating a class \"DirichletGroupExtensionFunctor\" whose effect was to extend Dirichlet groups by adding an nth root of unity into their value group). But it's a bit of a cheat since my \"functors\" aren't actually functors in any natural category I can think of.",
    "created_at": "2009-04-16T09:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45359",
    "user": "davidloeffler"
}
```

There is a bit more too this, though.

Basically, the whole Dirichlet character machinery goes a bit mad whenever you have two Dirichlet characters with the same modulus and base ring, but where the zeta orders aren't the same. For a start, the parent DirichletGroups compare as equal but their elements are different -- or at least they will be if we fix the !__call!__ method properly.

Similarly, arithmetic coercion is screwed up, in some interesting ways:


```
sage: K.<w> = NumberField(x^2 + x + 1)
sage: G2 = DirichletGroup(7, K, zeta_order=2, zeta=K(-1))
sage: G3 = DirichletGroup(7, K, zeta_order=3, zeta=w)
sage: G2.0 * G3.0
```


Here the coercion model will fail miserably to find the right parent. 

One option would be to prevent Dirichlet groups ever being created for which the zeta order is not maximal for the given base ring. This would sort of work, but would restrict us to Dirichlet groups over integral domains (so we can guarantee that the group of roots of unity in the ring is cyclic) and it would make it a pain to implement base extension (at present the base_extend method for DirichletGroup_class just base extends the zeta element it already knows about.

The alternative is to be "honest" and make Dirichlet groups with the same modulus and base ring but different zeta order into genuinely different objects, comparing as unequal and with different string representations. One can then sort out coercion arithmetic using the machinery from sage.categories.pushout; I coded this up as an experiment (creating a class "DirichletGroupExtensionFunctor" whose effect was to extend Dirichlet groups by adding an nth root of unity into their value group). But it's a bit of a cheat since my "functors" aren't actually functors in any natural category I can think of.



---

archive/issue_comments_045360.json:
```json
{
    "body": "I agree -- the business of `zeta_order` causes all sorts of confusion. However, I'm leaning the other direction -- I say we just eliminate it altogether from the defining data for a `DirichletGroup`. We could just avoid computing the zeta order in the ring until we need to, and when forced, just bite the bullet and do it. There will be several bonuses from doing this, and in particular, we can neatly clean up the trouble with basically-the-same-but-not-really-the-same groups, which is nice. The only potential downside I see is what you bring up in your comment -- if someone gives us a pretty ugly non-domain as the ring to work over (other than integers mod some `N`, where we can use other tricks to figure out the zeta order), we might spend time computing the zeta order. But that really seems like a rare case in my mind ... that said, it's 3am, so I won't make any promises about how my mind is operating. `:)`\n\nSo my vote: we commit this patch, and then open a new ticket to clean up this `zeta_order` business.",
    "created_at": "2009-05-08T09:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45360",
    "user": "craigcitro"
}
```

I agree -- the business of `zeta_order` causes all sorts of confusion. However, I'm leaning the other direction -- I say we just eliminate it altogether from the defining data for a `DirichletGroup`. We could just avoid computing the zeta order in the ring until we need to, and when forced, just bite the bullet and do it. There will be several bonuses from doing this, and in particular, we can neatly clean up the trouble with basically-the-same-but-not-really-the-same groups, which is nice. The only potential downside I see is what you bring up in your comment -- if someone gives us a pretty ugly non-domain as the ring to work over (other than integers mod some `N`, where we can use other tricks to figure out the zeta order), we might spend time computing the zeta order. But that really seems like a rare case in my mind ... that said, it's 3am, so I won't make any promises about how my mind is operating. `:)`

So my vote: we commit this patch, and then open a new ticket to clean up this `zeta_order` business.



---

archive/issue_comments_045361.json:
```json
{
    "body": "Attachment\n\nreplaces previous patch, apply over #4357 and #5250",
    "created_at": "2009-05-11T08:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45361",
    "user": "davidloeffler"
}
```

Attachment

replaces previous patch, apply over #4357 and #5250



---

archive/issue_comments_045362.json:
```json
{
    "body": "OK, I'm convinced. Positive review.\n\nThe patch has bit-rotted slightly, because I added some more doctests to dirichlet.py in #5727 and then edited it again in #5250. Also I am seeing a doctest failure in modform/ambient_eps.py -- nothing serious, the code expects a TypeError and gets a ValueError. I have done a rebased version which changes the doctest.",
    "created_at": "2009-05-11T08:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45362",
    "user": "davidloeffler"
}
```

OK, I'm convinced. Positive review.

The patch has bit-rotted slightly, because I added some more doctests to dirichlet.py in #5727 and then edited it again in #5250. Also I am seeing a doctest failure in modform/ambient_eps.py -- nothing serious, the code expects a TypeError and gets a ValueError. I have done a rebased version which changes the doctest.



---

archive/issue_comments_045363.json:
```json
{
    "body": "Merged trac_5792_rebase.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T09:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45363",
    "user": "mabshoff"
}
```

Merged trac_5792_rebase.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_045364.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T09:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5792#issuecomment-45364",
    "user": "mabshoff"
}
```

Resolution: fixed
