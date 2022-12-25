# Issue 1083: [with patch, with positive review] Bug in degree 1 number fields; manifests itself in element.matrix(), .trace(), .norm(), etc

archive/issues_001083.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: number fields matrix trace norm extension\n\nThe following is not correct:\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')\nsage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')\nsage: L\nNumber Field in b with defining polynomial x - a over its base field\nsage: L(a)\n0\n```\nThis is the root of the following bugs:\n\n```\nsage: a.trace(K)\nsage: a.norm(K)\nsage: a.matrix(K)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n... (snipped) ...\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in relativize(self, alpha, names)\n   2902                     # self --> M that sends alpha to\n   2903                     # the generator of the intermediate field.\n-> 2904                     from_M = M.hom([self.gen()], self, check=True)\n   2905                     M._set_structure(from_M, to_M)  # don't have to\n   2906                                                     # worry about caching since relative number fields aren't cached.\n\n/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()\n\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gen, base_hom, check)\n    172         if check:\n    173             im_gen = self.codomain()(im_gen)\n--> 174         return self._from_im(im_gen, base_hom)\n    175 \n    176     def _coerce_impl(self, x):\n\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in _from_im(self, im_gen, base_hom)\n    197         f = R([base_hom(x) for x in a.list()])\n    198         b = f(im_gen)\n--> 199         abs_hom = K.hom([b])\n    200         return RelativeNumberFieldHomomorphism_from_abs(self, abs_hom)\n    201 \n\n/Users/ncalexan/Documents/School/MATH235/groebner/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens.hom()\n\n/Users/ncalexan/sage/local/lib/python2.5/site-packages/sage/rings/number_field/morphism.py in __call__(self, im_gens, check)\n     30                 return self._coerce_impl(im_gens)\n     31             except TypeError:\n---> 32                 raise TypeError, \"images do not define a valid homomorphism\"\n     33         \n     34     def _coerce_impl(self, x):\n\n<type 'exceptions.TypeError'>: images do not define a valid homomorphism\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1083\n\n",
    "closed_at": "2008-01-27T05:14:26Z",
    "created_at": "2007-11-03T20:06:48Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, with positive review] Bug in degree 1 number fields; manifests itself in element.matrix(), .trace(), .norm(), etc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1083",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @craigcitro

Keywords: number fields matrix trace norm extension

The following is not correct:

```
sage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')
sage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')
sage: L
Number Field in b with defining polynomial x - a over its base field
sage: L(a)
0
```
This is the root of the following bugs:

```
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
```

Issue created by migration from https://trac.sagemath.org/ticket/1083





---

archive/issue_comments_006524.json:
```json
{
    "body": "Argh, that should be\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^2 + 2, 'a')\nsage: L.<b> = K.extension(ZZ['x'].0 - a, 'b')\nsage: L\nNumber Field in b with defining polynomial x - a over its base field\nsage: L(a)\n0\n```",
    "created_at": "2007-11-03T20:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6524",
    "user": "https://github.com/ncalexan"
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

archive/issue_events_002927.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-26T02:50:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1083#event-2927"
}
```



---

archive/issue_comments_006525.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-01-21T11:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6525",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_006526.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-21T11:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6526",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006527.json:
```json
{
    "body": "Man, this was a *bugger* to find. Here's the issue: at some point, we ask Pari to turn an absolute element into a relative element in a relative extension of degree n for us, and then we loop over the resulting polynomial from indices 0 to n-1 and add up some stuff. In the case that the relative extension is degree 1, Pari fails to do this correctly -- they don't reduce the polynomial below degree 1, which is what causes the trouble. The code proceeds to loop over just the 0th coefficient, which is just 0 in the example above. \n\nInterestingly, the problem here only occurs when you try to *print* your element -- you can create the element just fine, it's only when you try and print it that this zeroing occurs. (This was why I had so much trouble finding it.)\n\nI have a fix for this, but I've also reported the bug to the Pari folks -- given that this doesn't seem terribly pressing, if they're going to fix it upstream, it seems like just waiting would be the best approach. If I don't hear anything from them in a few days, I'll post a patch.",
    "created_at": "2008-01-21T11:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6527",
    "user": "https://github.com/craigcitro"
}
```

Man, this was a *bugger* to find. Here's the issue: at some point, we ask Pari to turn an absolute element into a relative element in a relative extension of degree n for us, and then we loop over the resulting polynomial from indices 0 to n-1 and add up some stuff. In the case that the relative extension is degree 1, Pari fails to do this correctly -- they don't reduce the polynomial below degree 1, which is what causes the trouble. The code proceeds to loop over just the 0th coefficient, which is just 0 in the example above. 

Interestingly, the problem here only occurs when you try to *print* your element -- you can create the element just fine, it's only when you try and print it that this zeroing occurs. (This was why I had so much trouble finding it.)

I have a fix for this, but I've also reported the bug to the Pari folks -- given that this doesn't seem terribly pressing, if they're going to fix it upstream, it seems like just waiting would be the best approach. If I don't hear anything from them in a few days, I'll post a patch.



---

archive/issue_comments_006528.json:
```json
{
    "body": "I just looked at the title of this, and noticed the 0 should be a 1.",
    "created_at": "2008-01-22T03:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6528",
    "user": "https://github.com/craigcitro"
}
```

I just looked at the title of this, and noticed the 0 should be a 1.



---

archive/issue_comments_006529.json:
```json
{
    "body": "Good work, Craig Citro!  I spent hours tracking it as far as I did, too -- it was a strange bug, that's for sure.",
    "created_at": "2008-01-22T18:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6529",
    "user": "https://github.com/ncalexan"
}
```

Good work, Craig Citro!  I spent hours tracking it as far as I did, too -- it was a strange bug, that's for sure.



---

archive/issue_comments_006530.json:
```json
{
    "body": "Attachment [craigcitro-1083.patch](tarball://root/attachments/some-uuid/ticket1083/craigcitro-1083.patch) by @craigcitro created at 2008-01-23 11:19:48\n\nSo I got a response from the pari team that the problem on their end is fixed in svn. However, given the fact that the Pari release cycle is slower than ours, I've added a workaround to Sage. Looking at the other tests Nick had above, I noticed that for any NumberFieldElement a, a.matrix(QQ) didn't work. I fixed this while I was there, and added a few doctests.",
    "created_at": "2008-01-23T11:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6530",
    "user": "https://github.com/craigcitro"
}
```

Attachment [craigcitro-1083.patch](tarball://root/attachments/some-uuid/ticket1083/craigcitro-1083.patch) by @craigcitro created at 2008-01-23 11:19:48

So I got a response from the pari team that the problem on their end is fixed in svn. However, given the fact that the Pari release cycle is slower than ours, I've added a workaround to Sage. Looking at the other tests Nick had above, I noticed that for any NumberFieldElement a, a.matrix(QQ) didn't work. I fixed this while I was there, and added a few doctests.



---

archive/issue_comments_006531.json:
```json
{
    "body": "Apply!  My only worry is that there is no reference, in the code, to the PARI bug, but maybe that is better?",
    "created_at": "2008-01-27T04:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6531",
    "user": "https://github.com/ncalexan"
}
```

Apply!  My only worry is that there is no reference, in the code, to the PARI bug, but maybe that is better?



---

archive/issue_comments_006532.json:
```json
{
    "body": "#1891 is the ticket to remove the work around once the fix is in upstream pari.",
    "created_at": "2008-01-27T04:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

#1891 is the ticket to remove the work around once the fix is in upstream pari.



---

archive/issue_comments_006533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T05:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002928.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-27T05:14:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1083#event-2928"
}
```



---

archive/issue_comments_006534.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc1",
    "created_at": "2008-01-27T05:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1083#issuecomment-6534",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc1
