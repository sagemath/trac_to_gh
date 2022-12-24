# Issue 1083: Bug in degree 0 number fields; manifests itself in element.matrix(), .trace(), .norm(), etc

archive/issues_001083.json:
```json
{
    "body": "Assignee: was\n\nKeywords: number fields matrix trace norm extension\n\nThe following is not correct:\n\nsage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')\nsage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')\nsage: L\nNumber Field in b with defining polynomial x - a over its base field\nsage: L(a)\n0\n\nThis is the root of the following bugs:\n\nsage: a.trace(K)\nsage: a.norm(K)\nsage: a.matrix(K)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n... (snipped) ...\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in relativize(self, alpha, names)\n   2902                     # self --> M that sends alpha to\n   2903                     # the generator of the intermediate field.\n-> 2904                     from_M = M.hom([self.gen()], self, check=True)\n   2905                     M._set_structure(from_M, to_M)  # don't have to\n   2906                                                     # worry about caching since relative number fields aren't cached.\n\n/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()\n\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gen, base_hom, check)\n    172         if check:\n    173             im_gen = self.codomain()(im_gen)\n--> 174         return self._from_im(im_gen, base_hom)\n    175 \n    176     def _coerce_impl(self, x):\n\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in _from_im(self, im_gen, base_hom)\n    197         f = R([base_hom(x) for x in a.list()])\n    198         b = f(im_gen)\n--> 199         abs_hom = K.hom([b])\n    200         return RelativeNumberFieldHomomorphism_from_abs(self, abs_hom)\n    201 \n\n/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()\n\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gens, check)\n     30                 return self._coerce_impl(im_gens)\n     31             except TypeError:\n---> 32                 raise TypeError, \"images do not define a valid homomorphism\"\n     33         \n     34     def _coerce_impl(self, x):\n\n<type 'exceptions.TypeError'>: images do not define a valid homomorphism\n\nIssue created by migration from https://trac.sagemath.org/ticket/1083\n\n",
    "created_at": "2007-11-03T20:06:48Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Bug in degree 0 number fields; manifests itself in element.matrix(), .trace(), .norm(), etc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1083",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: number fields matrix trace norm extension

The following is not correct:

sage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')
sage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')
sage: L
Number Field in b with defining polynomial x - a over its base field
sage: L(a)
0

This is the root of the following bugs:

sage: a.trace(K)
sage: a.norm(K)
sage: a.matrix(K)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
... (snipped) ...
/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in relativize(self, alpha, names)
   2902                     # self --> M that sends alpha to
   2903                     # the generator of the intermediate field.
-> 2904                     from_M = M.hom([self.gen()], self, check=True)
   2905                     M._set_structure(from_M, to_M)  # don't have to
   2906                                                     # worry about caching since relative number fields aren't cached.

/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()

/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gen, base_hom, check)
    172         if check:
    173             im_gen = self.codomain()(im_gen)
--> 174         return self._from_im(im_gen, base_hom)
    175 
    176     def _coerce_impl(self, x):

/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in _from_im(self, im_gen, base_hom)
    197         f = R([base_hom(x) for x in a.list()])
    198         b = f(im_gen)
--> 199         abs_hom = K.hom([b])
    200         return RelativeNumberFieldHomomorphism_from_abs(self, abs_hom)
    201 

/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()

/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gens, check)
     30                 return self._coerce_impl(im_gens)
     31             except TypeError:
---> 32                 raise TypeError, "images do not define a valid homomorphism"
     33         
     34     def _coerce_impl(self, x):

<type 'exceptions.TypeError'>: images do not define a valid homomorphism

Issue created by migration from https://trac.sagemath.org/ticket/1083





---

archive/issue_comments_006544.json:
```json
{
    "body": "Argh, that should be\n\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')\nsage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')\nsage: L\nNumber Field in b with defining polynomial x - a over its base field\nsage: L(a)\n0\n```\n",
    "created_at": "2007-11-03T20:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6544",
    "user": "ncalexan"
}
```

Argh, that should be


```
sage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')
sage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')
sage: L
Number Field in b with defining polynomial x - a over its base field
sage: L(a)
0
```




---

archive/issue_comments_006545.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-01-21T11:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6545",
    "user": "craigcitro"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_006546.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-21T11:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6546",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006547.json:
```json
{
    "body": "Man, this was a *bugger* to find. Here's the issue: at some point, we ask Pari to turn an absolute element into a relative element in a relative extension of degree n for us, and then we loop over the resulting polynomial from indices 0 to n-1 and add up some stuff. In the case that the relative extension is degree 1, Pari fails to do this correctly -- they don't reduce the polynomial below degree 1, which is what causes the trouble. The code proceeds to loop over just the 0th coefficient, which is just 0 in the example above. \n\nInterestingly, the problem here only occurs when you try to *print* your element -- you can create the element just fine, it's only when you try and print it that this zeroing occurs. (This was why I had so much trouble finding it.)\n\nI have a fix for this, but I've also reported the bug to the Pari folks -- given that this doesn't seem terribly pressing, if they're going to fix it upstream, it seems like just waiting would be the best approach. If I don't hear anything from them in a few days, I'll post a patch.",
    "created_at": "2008-01-21T11:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6547",
    "user": "craigcitro"
}
```

Man, this was a *bugger* to find. Here's the issue: at some point, we ask Pari to turn an absolute element into a relative element in a relative extension of degree n for us, and then we loop over the resulting polynomial from indices 0 to n-1 and add up some stuff. In the case that the relative extension is degree 1, Pari fails to do this correctly -- they don't reduce the polynomial below degree 1, which is what causes the trouble. The code proceeds to loop over just the 0th coefficient, which is just 0 in the example above. 

Interestingly, the problem here only occurs when you try to *print* your element -- you can create the element just fine, it's only when you try and print it that this zeroing occurs. (This was why I had so much trouble finding it.)

I have a fix for this, but I've also reported the bug to the Pari folks -- given that this doesn't seem terribly pressing, if they're going to fix it upstream, it seems like just waiting would be the best approach. If I don't hear anything from them in a few days, I'll post a patch.



---

archive/issue_comments_006548.json:
```json
{
    "body": "I just looked at the title of this, and noticed the 0 should be a 1.",
    "created_at": "2008-01-22T03:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6548",
    "user": "craigcitro"
}
```

I just looked at the title of this, and noticed the 0 should be a 1.



---

archive/issue_comments_006549.json:
```json
{
    "body": "Good work, Craig Citro!  I spent hours tracking it as far as I did, too -- it was a strange bug, that's for sure.",
    "created_at": "2008-01-22T18:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6549",
    "user": "ncalexan"
}
```

Good work, Craig Citro!  I spent hours tracking it as far as I did, too -- it was a strange bug, that's for sure.



---

archive/issue_comments_006550.json:
```json
{
    "body": "Attachment [craigcitro-1083.patch](tarball://root/attachments/some-uuid/ticket1083/craigcitro-1083.patch) by craigcitro created at 2008-01-23 11:19:48\n\nSo I got a response from the pari team that the problem on their end is fixed in svn. However, given the fact that the Pari release cycle is slower than ours, I've added a workaround to Sage. Looking at the other tests Nick had above, I noticed that for any NumberFieldElement a, a.matrix(QQ) didn't work. I fixed this while I was there, and added a few doctests.",
    "created_at": "2008-01-23T11:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6550",
    "user": "craigcitro"
}
```

Attachment [craigcitro-1083.patch](tarball://root/attachments/some-uuid/ticket1083/craigcitro-1083.patch) by craigcitro created at 2008-01-23 11:19:48

So I got a response from the pari team that the problem on their end is fixed in svn. However, given the fact that the Pari release cycle is slower than ours, I've added a workaround to Sage. Looking at the other tests Nick had above, I noticed that for any NumberFieldElement a, a.matrix(QQ) didn't work. I fixed this while I was there, and added a few doctests.



---

archive/issue_comments_006551.json:
```json
{
    "body": "Apply!  My only worry is that there is no reference, in the code, to the PARI bug, but maybe that is better?",
    "created_at": "2008-01-27T04:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6551",
    "user": "ncalexan"
}
```

Apply!  My only worry is that there is no reference, in the code, to the PARI bug, but maybe that is better?



---

archive/issue_comments_006552.json:
```json
{
    "body": "#1891 is the ticket to remove the work around once the fix is in upstream pari.",
    "created_at": "2008-01-27T04:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6552",
    "user": "mabshoff"
}
```

#1891 is the ticket to remove the work around once the fix is in upstream pari.



---

archive/issue_comments_006553.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T05:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6553",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006554.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T05:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6554",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc1
