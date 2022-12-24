# Issue 6018: Confusing behaviour with Dirichlet characters

archive/issues_006018.json:
```json
{
    "body": "Assignee: craigcitro\n\nKeywords: Dirichlet characters\n\nFunny things happen if you have two Dirichlet groups with the same modulus and the same base ring, but different roots of unity. This can happen if you use base_extend:\n\n\n```\nsage: G = DirichletGroup(10, QQ).base_extend(CyclotomicField(4))\nsage: H = DirichletGroup(10, CyclotomicField(4))\n```\n\n\nNow G and H look pretty similar:\n\n```\nsage: G\nGroup of Dirichlet characters of modulus 10 over Cyclotomic Field of order 4 and degree 2\nsage: H\nGroup of Dirichlet characters of modulus 10 over Cyclotomic Field of order 4 and degree 2\n```\n\n\nBut they don't compare as equal and the generators of H don't live in G:\n\n```\nsage: G == H\nFalse\nsage: H.0 in G\nFalse\n```\n\n\nHere G only actually contains those characters which factor through its original base ring, namely QQ. This is probably going to be a bit mystifying for the end-user.\n\nSimilar phenomena can make it next to impossible to do arithmetic with characters obtained by base extension, which somehow are second-class citizens:\n\n\n```\nsage: K5 = CyclotomicField(5); K3 = CyclotomicField(3); K30 = CyclotomicField(30)\nsage: (DirichletGroup(31, K5).0).base_extend(K30) * (DirichletGroup(31, K3).0).base_extend(K30)\nTypeError: unsupported operand parent(s) for '*': \n'Group of Dirichlet characters of modulus 31 over Cyclotomic Field of order 30 and degree 8' and \n'Group of Dirichlet characters of modulus 31 over Cyclotomic Field of order 30 and degree 8'\n```\n\n\nThis is a particularly mystifying error for the uninitiated, since it's asserting that it can't find a common parent, but the string representations of the parents it already has are identical.\n\nI can see a couple of solutions:\n\n- Change base_extend for Dirichlet groups to pick a maximal order root of unity in the new base ring, rather than just base-extending the root of unity it already has. This is nice and transparent, but it could be slow in some cases, and it prevents us constructing Dirichlet characters with values in rings where the unit group isn't cyclic or we can't compute a generator (e.g. we'd lose the ability to base extend elements of `DirichletGroup(N, ZZ)` to `DirichletGroup(N, Integers(15))`).\n\n- Change the `_repr_` method for Dirichlet groups so it explicitly prints the root of unity involved. I don't like this idea much.\n\n- Some combination of the above two, with a special class for Dirichlet groups over domains where a unique root of unity of maximal order dividing `euler_phi(N)` doesn't exist or can't be calculated. This might be fiddly to write and maintain.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6018\n\n",
    "created_at": "2009-05-11T09:18:29Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "title": "Confusing behaviour with Dirichlet characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6018",
    "user": "davidloeffler"
}
```
Assignee: craigcitro

Keywords: Dirichlet characters

Funny things happen if you have two Dirichlet groups with the same modulus and the same base ring, but different roots of unity. This can happen if you use base_extend:


```
sage: G = DirichletGroup(10, QQ).base_extend(CyclotomicField(4))
sage: H = DirichletGroup(10, CyclotomicField(4))
```


Now G and H look pretty similar:

```
sage: G
Group of Dirichlet characters of modulus 10 over Cyclotomic Field of order 4 and degree 2
sage: H
Group of Dirichlet characters of modulus 10 over Cyclotomic Field of order 4 and degree 2
```


But they don't compare as equal and the generators of H don't live in G:

```
sage: G == H
False
sage: H.0 in G
False
```


Here G only actually contains those characters which factor through its original base ring, namely QQ. This is probably going to be a bit mystifying for the end-user.

Similar phenomena can make it next to impossible to do arithmetic with characters obtained by base extension, which somehow are second-class citizens:


```
sage: K5 = CyclotomicField(5); K3 = CyclotomicField(3); K30 = CyclotomicField(30)
sage: (DirichletGroup(31, K5).0).base_extend(K30) * (DirichletGroup(31, K3).0).base_extend(K30)
TypeError: unsupported operand parent(s) for '*': 
'Group of Dirichlet characters of modulus 31 over Cyclotomic Field of order 30 and degree 8' and 
'Group of Dirichlet characters of modulus 31 over Cyclotomic Field of order 30 and degree 8'
```


This is a particularly mystifying error for the uninitiated, since it's asserting that it can't find a common parent, but the string representations of the parents it already has are identical.

I can see a couple of solutions:

- Change base_extend for Dirichlet groups to pick a maximal order root of unity in the new base ring, rather than just base-extending the root of unity it already has. This is nice and transparent, but it could be slow in some cases, and it prevents us constructing Dirichlet characters with values in rings where the unit group isn't cyclic or we can't compute a generator (e.g. we'd lose the ability to base extend elements of `DirichletGroup(N, ZZ)` to `DirichletGroup(N, Integers(15))`).

- Change the `_repr_` method for Dirichlet groups so it explicitly prints the root of unity involved. I don't like this idea much.

- Some combination of the above two, with a special class for Dirichlet groups over domains where a unique root of unity of maximal order dividing `euler_phi(N)` doesn't exist or can't be calculated. This might be fiddly to write and maintain.

Issue created by migration from https://trac.sagemath.org/ticket/6018





---

archive/issue_comments_047879.json:
```json
{
    "body": "David, I like your analysis of the situation a lot.  I'm going to do what you suggest first.  Regarding performance issues, I think if the user really is worried about that in some case, they can be explicit about the relevant spaces and zeta's.",
    "created_at": "2010-01-19T02:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47879",
    "user": "was"
}
```

David, I like your analysis of the situation a lot.  I'm going to do what you suggest first.  Regarding performance issues, I think if the user really is worried about that in some case, they can be explicit about the relevant spaces and zeta's.



---

archive/issue_comments_047880.json:
```json
{
    "body": "Attachment [trac_6018.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018.patch) by was created at 2010-01-19 03:56:40",
    "created_at": "2010-01-19T03:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47880",
    "user": "was"
}
```

Attachment [trac_6018.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018.patch) by was created at 2010-01-19 03:56:40



---

archive/issue_comments_047881.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T03:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47881",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047882.json:
```json
{
    "body": "This looks like a nice clean fix -- my only worry would be that a few subtle choices cause mayhem with some random modular symbols code. William, did you run doctests on the `modular/` directory? \n\nAlso, one potentially silly comment: your fix assumes that the constructor for `DirichletGroup` always chooses a maximal order and an appropriate zeta if one isn't given. While I can't imagine us ever changing that constructor to do anything different, should we either (1) explicitly choose the maximal order or (2) check and/or document this in some way? I think it's unlikely, but should it ever come up, a comment near that line of code pointing someone in the right direction could be a huge help ...",
    "created_at": "2010-01-19T05:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47882",
    "user": "craigcitro"
}
```

This looks like a nice clean fix -- my only worry would be that a few subtle choices cause mayhem with some random modular symbols code. William, did you run doctests on the `modular/` directory? 

Also, one potentially silly comment: your fix assumes that the constructor for `DirichletGroup` always chooses a maximal order and an appropriate zeta if one isn't given. While I can't imagine us ever changing that constructor to do anything different, should we either (1) explicitly choose the maximal order or (2) check and/or document this in some way? I think it's unlikely, but should it ever come up, a comment near that line of code pointing someone in the right direction could be a huge help ...



---

archive/issue_comments_047883.json:
```json
{
    "body": "I am running sage -testall on this patch at the moment. \n\nThe key question, I think, is what we want to happen in the following situation:\n\n```\nsage: f = DirichletGroup(17, ZZ).0\nsage: f.base_extend(Integers(15))\n```\n\nThis worked under the old approach, because the parent of the base-extended thing was the Dirichlet group of modulus 17 and `zeta = ZZ(15)(-1)`, of order 2. But I suspect that with this patch it will fail now, with an error message about not being able to compute roots of unity mod 15.\n\nI suggest a further modification which makes the constructor raise a more intelligent error message if the root of unity isn't specified and the base ring is one where we can't do factorisation. If the tests pass I will write such a patch, and give William's patch a positive review conditional on that.",
    "created_at": "2010-01-20T18:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47883",
    "user": "davidloeffler"
}
```

I am running sage -testall on this patch at the moment. 

The key question, I think, is what we want to happen in the following situation:

```
sage: f = DirichletGroup(17, ZZ).0
sage: f.base_extend(Integers(15))
```

This worked under the old approach, because the parent of the base-extended thing was the Dirichlet group of modulus 17 and `zeta = ZZ(15)(-1)`, of order 2. But I suspect that with this patch it will fail now, with an error message about not being able to compute roots of unity mod 15.

I suggest a further modification which makes the constructor raise a more intelligent error message if the root of unity isn't specified and the base ring is one where we can't do factorisation. If the tests pass I will write such a patch, and give William's patch a positive review conditional on that.



---

archive/issue_comments_047884.json:
```json
{
    "body": "Attachment [trac_6018-2.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018-2.patch) by davidloeffler created at 2010-01-20 19:21:15\n\napply over previous patch",
    "created_at": "2010-01-20T19:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47884",
    "user": "davidloeffler"
}
```

Attachment [trac_6018-2.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018-2.patch) by davidloeffler created at 2010-01-20 19:21:15

apply over previous patch



---

archive/issue_comments_047885.json:
```json
{
    "body": "As promised, here is a second patch. This takes a compromise approach where base_extend tries to calculate a maximal order root of unity in the new base ring if it's an integral domain, but otherwise uses the base-extension. I've added a couple of doctests, including one to illustrate the perils of the `zeta_order` argument.\n\nIf someone else can approve the new patch I think we're sorted.",
    "created_at": "2010-01-20T19:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47885",
    "user": "davidloeffler"
}
```

As promised, here is a second patch. This takes a compromise approach where base_extend tries to calculate a maximal order root of unity in the new base ring if it's an integral domain, but otherwise uses the base-extension. I've added a couple of doctests, including one to illustrate the perils of the `zeta_order` argument.

If someone else can approve the new patch I think we're sorted.



---

archive/issue_comments_047886.json:
```json
{
    "body": "This looks good -- I just have two questions:\n\n* In the last example, you show that weirdness ensues when the provided `zeta` doesn't have order `zeta_order`. Couldn't we (optionally, with a `check=...` parameter) check this? Having it on by default definitely seems like it'd stop users from shooting themselves in the foot.\n\n* Is it possible for the call to `base_ring(zeta)` to raise an exception? If so, do we want to catch that and provide a more direct error message, or just let it go?",
    "created_at": "2010-01-20T19:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47886",
    "user": "craigcitro"
}
```

This looks good -- I just have two questions:

* In the last example, you show that weirdness ensues when the provided `zeta` doesn't have order `zeta_order`. Couldn't we (optionally, with a `check=...` parameter) check this? Having it on by default definitely seems like it'd stop users from shooting themselves in the foot.

* Is it possible for the call to `base_ring(zeta)` to raise an exception? If so, do we want to catch that and provide a more direct error message, or just let it go?



---

archive/issue_comments_047887.json:
```json
{
    "body": "The docs state several times that you don't actually need to supply zeta_order, so nobody's going to use the option in the first place unless they've got a pretty good reason to do so. I'd rather not make the code still more complicated! (Would it actually cause that much harm to get rid of the zeta_order argument entirely?)\n\nIf base_ring(zeta) raises an exception, the error message will say something like \"Unable to coerce foo into bar\", and it should be reasonably clear what the problem is. With these patches, the constructor will almost always be getting called without specifying zeta and zeta_order anyway.\n\nDavid",
    "created_at": "2010-01-20T21:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47887",
    "user": "davidloeffler"
}
```

The docs state several times that you don't actually need to supply zeta_order, so nobody's going to use the option in the first place unless they've got a pretty good reason to do so. I'd rather not make the code still more complicated! (Would it actually cause that much harm to get rid of the zeta_order argument entirely?)

If base_ring(zeta) raises an exception, the error message will say something like "Unable to coerce foo into bar", and it should be reasonably clear what the problem is. With these patches, the constructor will almost always be getting called without specifying zeta and zeta_order anyway.

David



---

archive/issue_comments_047888.json:
```json
{
    "body": "I'm a big fan of just removing the `zeta_order` argument -- looking at the code, there's no real reason to specify it, and it'll clean up a few statements in the constructor.",
    "created_at": "2010-01-20T22:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47888",
    "user": "craigcitro"
}
```

I'm a big fan of just removing the `zeta_order` argument -- looking at the code, there's no real reason to specify it, and it'll clean up a few statements in the constructor.



---

archive/issue_comments_047889.json:
```json
{
    "body": "Attachment [trac_6018-3.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018-3.patch) by davidloeffler created at 2010-01-20 22:22:43",
    "created_at": "2010-01-20T22:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47889",
    "user": "davidloeffler"
}
```

Attachment [trac_6018-3.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018-3.patch) by davidloeffler created at 2010-01-20 22:22:43



---

archive/issue_comments_047890.json:
```json
{
    "body": "Here's a third patch that kills zeta_order. All doctests in modular/ pass, I'm running a full test cycle now.",
    "created_at": "2010-01-20T22:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47890",
    "user": "davidloeffler"
}
```

Here's a third patch that kills zeta_order. All doctests in modular/ pass, I'm running a full test cycle now.



---

archive/issue_comments_047891.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T22:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47891",
    "user": "craigcitro"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047892.json:
```json
{
    "body": "Two thumbs up! Apply all three.",
    "created_at": "2010-01-20T22:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47892",
    "user": "craigcitro"
}
```

Two thumbs up! Apply all three.



---

archive/issue_comments_047893.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-01-20T23:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47893",
    "user": "davidloeffler"
}
```

apply only this patch



---

archive/issue_comments_047894.json:
```json
{
    "body": "Attachment [trac_6018_folded.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018_folded.patch) by was created at 2010-01-20 23:57:21\n\nHey, why, wait, what happens if you create a zeta such that zeta.multiplicative_order() doesn't work?!\n\n```\nsage: a = CDF(CyclotomicField(5).0)\nsage: G = DirichletGroup(11, base_ring=a.parent(), zeta=a, zeta_order=5)\nsage: G\nGroup of Dirichlet characters of modulus 11 over Complex Double Field\nsage: G.0\n[0.309016994375 + 0.951056516295*I]\nsage: G.0(2)\n0.309016994375 + 0.951056516295*I\n```\n\n\nPlease revert getting rid of zeta_order and make that part of another ticket, keeping in mind that you can't exactly do that, since it is important.  The above doctest should be put in that ticket since this problem wouldn't have happened if I had included the above test.",
    "created_at": "2010-01-20T23:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47894",
    "user": "was"
}
```

Attachment [trac_6018_folded.patch](tarball://root/attachments/some-uuid/ticket6018/trac_6018_folded.patch) by was created at 2010-01-20 23:57:21

Hey, why, wait, what happens if you create a zeta such that zeta.multiplicative_order() doesn't work?!

```
sage: a = CDF(CyclotomicField(5).0)
sage: G = DirichletGroup(11, base_ring=a.parent(), zeta=a, zeta_order=5)
sage: G
Group of Dirichlet characters of modulus 11 over Complex Double Field
sage: G.0
[0.309016994375 + 0.951056516295*I]
sage: G.0(2)
0.309016994375 + 0.951056516295*I
```


Please revert getting rid of zeta_order and make that part of another ticket, keeping in mind that you can't exactly do that, since it is important.  The above doctest should be put in that ticket since this problem wouldn't have happened if I had included the above test.



---

archive/issue_comments_047895.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-20T23:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47895",
    "user": "was"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_047896.json:
```json
{
    "body": "OK, so would you be happy with applying just the first two patches? \n\nDavid",
    "created_at": "2010-01-21T09:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47896",
    "user": "davidloeffler"
}
```

OK, so would you be happy with applying just the first two patches? 

David



---

archive/issue_comments_047897.json:
```json
{
    "body": "On reflection, the issue is surprisingly subtle.\n\nConsider taking a Dirichlet group with values in the integers of a cyclotomic field K, and base_extending to: (1) the complex double field; (2) the residue field of a prime of K.\n\nIn case (1), your example shows that we can't expect the constructor of the new group to calculate the order of a given zeta. But case (2) shows that the order of the base-extended zeta might not be the same as the order of the original zeta, and one can easily get nonsense if one assumes this.\n\nCase (1) is actually OK if we don't pass zeta as an argument at all, because we can factor polynomials in CDF. This is more or less what applying Craig's patch and mine will give: zeta_order is still available as an argument, but it's not used by the base extension code, which relies on the base ring supporting *either* polynomial factoring or `multiplicative_order`.",
    "created_at": "2010-01-21T09:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47897",
    "user": "davidloeffler"
}
```

On reflection, the issue is surprisingly subtle.

Consider taking a Dirichlet group with values in the integers of a cyclotomic field K, and base_extending to: (1) the complex double field; (2) the residue field of a prime of K.

In case (1), your example shows that we can't expect the constructor of the new group to calculate the order of a given zeta. But case (2) shows that the order of the base-extended zeta might not be the same as the order of the original zeta, and one can easily get nonsense if one assumes this.

Case (1) is actually OK if we don't pass zeta as an argument at all, because we can factor polynomials in CDF. This is more or less what applying Craig's patch and mine will give: zeta_order is still available as an argument, but it's not used by the base extension code, which relies on the base ring supporting *either* polynomial factoring or `multiplicative_order`.



---

archive/issue_comments_047898.json:
```json
{
    "body": "Here is a branch implementing a solution which is somewhat like the third option in the ticket description.  The idea is to introduce two different variants of `DirichletGroup`:\n- `DirichletGroup(N, base_ring)`, corresponding to the group Hom((**Z**/*N***Z**)<sup>*</sup>, *R*<sup>*</sup>);\n- `DirichletGroup(N, base_ring, zeta[, zeta_order])` corresponding to the group Hom((**Z**/*N***Z**)<sup>*</sup>, \u3008\u03b6\u3009).\nIf *R* is a domain, we also allow the user to only specify `zeta_order`, in which case the `DirichletGroup` factory tries to compute a suitable `zeta`.\n\nThe difference between the two variants is visible from the string representation:\n\n```\nsage: R.<x> = PolynomialRing(QQ)\nsage: K.<a> = NumberField(x^4 + 1)\nsage: DirichletGroup(5, K)\nGroup of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1\nsage: DirichletGroup(5, K, a)\nGroup of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a\n```\n\n\nBecause it is no longer mandatory to have a distinguished `zeta`, Dirichlet characters are by default specified by their values instead of a vector of integers modulo the order of `zeta`.  For efficiency reasons, this vector is still used whenever a `zeta` is known (whether it has been specified as in the second syntax above or has been computed at a later stage).\n\nBesides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.  This is because `zeta` is only computed when needed, and hence factoring cyclotomic polynomials is avoided.  This factoring will still happen when one asks for things like generators or a list of all elements.\n\nDavid: part of the branch (including some doctests) is based on your patches; I hope you don't mind me adding you as an author.",
    "created_at": "2015-06-05T12:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47898",
    "user": "pbruin"
}
```

Here is a branch implementing a solution which is somewhat like the third option in the ticket description.  The idea is to introduce two different variants of `DirichletGroup`:
- `DirichletGroup(N, base_ring)`, corresponding to the group Hom((**Z**/*N***Z**)<sup>*</sup>, *R*<sup>*</sup>);
- `DirichletGroup(N, base_ring, zeta[, zeta_order])` corresponding to the group Hom((**Z**/*N***Z**)<sup>*</sup>, 〈ζ〉).
If *R* is a domain, we also allow the user to only specify `zeta_order`, in which case the `DirichletGroup` factory tries to compute a suitable `zeta`.

The difference between the two variants is visible from the string representation:

```
sage: R.<x> = PolynomialRing(QQ)
sage: K.<a> = NumberField(x^4 + 1)
sage: DirichletGroup(5, K)
Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1
sage: DirichletGroup(5, K, a)
Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a
```


Because it is no longer mandatory to have a distinguished `zeta`, Dirichlet characters are by default specified by their values instead of a vector of integers modulo the order of `zeta`.  For efficiency reasons, this vector is still used whenever a `zeta` is known (whether it has been specified as in the second syntax above or has been computed at a later stage).

Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.  This is because `zeta` is only computed when needed, and hence factoring cyclotomic polynomials is avoided.  This factoring will still happen when one asks for things like generators or a list of all elements.

David: part of the branch (including some doctests) is based on your patches; I hope you don't mind me adding you as an author.



---

archive/issue_comments_047899.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-05T12:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47899",
    "user": "pbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047900.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-05T14:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47900",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047901.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-22T19:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47901",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047902.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-16T08:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47902",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047903.json:
```json
{
    "body": "This is just a detail, but instead of\n\n```\nGroup of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a\n```\n\nI would prefer\n\n```\nGroup of Dirichlet characters of modulus 5 with values in the group of order 8 generated by a over Number Field in a with defining polynomial x^4 + 1\n```\n",
    "created_at": "2015-07-17T20:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47903",
    "user": "jdemeyer"
}
```

This is just a detail, but instead of

```
Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a
```

I would prefer

```
Group of Dirichlet characters of modulus 5 with values in the group of order 8 generated by a over Number Field in a with defining polynomial x^4 + 1
```




---

archive/issue_comments_047904.json:
```json
{
    "body": "Replying to [comment:18 pbruin]:\n> Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.\n\nI assume that this is the main motivation for making `zeta` optional, right? I am not really convinced though that this extra complexity is needed...\n\nIt is true that `zeta()` for number fields is slow, but that can easily be improved (#18917).",
    "created_at": "2015-07-17T20:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47904",
    "user": "jdemeyer"
}
```

Replying to [comment:18 pbruin]:
> Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.

I assume that this is the main motivation for making `zeta` optional, right? I am not really convinced though that this extra complexity is needed...

It is true that `zeta()` for number fields is slow, but that can easily be improved (#18917).



---

archive/issue_comments_047905.json:
```json
{
    "body": "Replying to [comment:24 jdemeyer]:\n> Replying to [comment:18 pbruin]:\n> > Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.\n> \n> I assume that this is the main motivation for making `zeta` optional, right? I am not really convinced though that this extra complexity is needed...\nThis is not really true; it also makes more sense conceptually if one does not have to make a choice of root of unity.  I think the problems related to base extension do deserve to be solved and are at least as important as the speed-up.\n> It is true that `zeta()` for number fields is slow, but that can easily be improved (#18917).\nIt would be great if it could, but when making a speed improvement to `zeta()` in #15486, I found out that it was necessary to avoid calling PARI's `nfinit()`, because it was too slow for the number fields involved.  This unfortunately precludes using PARI's `nfrootsof1()`...",
    "created_at": "2015-07-18T10:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47905",
    "user": "pbruin"
}
```

Replying to [comment:24 jdemeyer]:
> Replying to [comment:18 pbruin]:
> > Besides solving the problems in the ticket description, this ticket greatly speeds up constructing Dirichlet groups over number fields.
> 
> I assume that this is the main motivation for making `zeta` optional, right? I am not really convinced though that this extra complexity is needed...
This is not really true; it also makes more sense conceptually if one does not have to make a choice of root of unity.  I think the problems related to base extension do deserve to be solved and are at least as important as the speed-up.
> It is true that `zeta()` for number fields is slow, but that can easily be improved (#18917).
It would be great if it could, but when making a speed improvement to `zeta()` in #15486, I found out that it was necessary to avoid calling PARI's `nfinit()`, because it was too slow for the number fields involved.  This unfortunately precludes using PARI's `nfrootsof1()`...



---

archive/issue_comments_047906.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-07-20T16:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47906",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047907.json:
```json
{
    "body": "Replying to [comment:23 jdemeyer]:\n> This is just a detail, but instead of\n> {{{\n> Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a\n> }}}\n> I would prefer\n> {{{\n> Group of Dirichlet characters of modulus 5 with values in the group of order 8 generated by a over Number Field in a with defining polynomial x^4 + 1\n> }}}\nI took the opportunity to make a more general improvement to the wording; the format is now\n\n```\nGroup of Dirichlet characters modulo N with values in [the group of order M generated by Z in ]R",
    "created_at": "2015-07-20T16:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47907",
    "user": "pbruin"
}
```

Replying to [comment:23 jdemeyer]:
> This is just a detail, but instead of
> {{{
> Group of Dirichlet characters of modulus 5 over Number Field in a with defining polynomial x^4 + 1 with values in the group of order 8 generated by a
> }}}
> I would prefer
> {{{
> Group of Dirichlet characters of modulus 5 with values in the group of order 8 generated by a over Number Field in a with defining polynomial x^4 + 1
> }}}
I took the opportunity to make a more general improvement to the wording; the format is now

```
Group of Dirichlet characters modulo N with values in [the group of order M generated by Z in ]R



---

archive/issue_comments_047908.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-22T00:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47908",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047909.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-22T08:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47909",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047910.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-01-22T14:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47910",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047911.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-25T23:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47911",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_047912.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-25T00:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47912",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047913.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2016-03-25T00:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47913",
    "user": "aly.deines"
}
```

Looks good to me.



---

archive/issue_comments_047914.json:
```json
{
    "body": "Changing keywords from \"Dirichlet characters\" to \"Dirichlet characters, days71\".",
    "created_at": "2016-03-25T00:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47914",
    "user": "aly.deines"
}
```

Changing keywords from "Dirichlet characters" to "Dirichlet characters, days71".



---

archive/issue_comments_047915.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2016-03-25T17:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47915",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_047916.json:
```json
{
    "body": "Doctests fail",
    "created_at": "2016-03-25T17:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47916",
    "user": "vbraun"
}
```

Doctests fail



---

archive/issue_comments_047917.json:
```json
{
    "body": "http://build.sagedev.org/release/builders/%20%20slow%20AIMS%20%20%28Debian%207%2032%20bit%29%20incremental/builds/439/steps/shell_4/logs/stdio",
    "created_at": "2016-03-25T17:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47917",
    "user": "vbraun"
}
```

http://build.sagedev.org/release/builders/%20%20slow%20AIMS%20%20%28Debian%207%2032%20bit%29%20incremental/builds/439/steps/shell_4/logs/stdio



---

archive/issue_comments_047918.json:
```json
{
    "body": "Replying to [comment:34 vbraun]:\n> http://build.sagedev.org/release/builders/%20%20slow%20AIMS%20%20%28Debian%207%2032%20bit%29%20incremental/builds/439/steps/shell_4/logs/stdio\nFrom the failing doctest in `cachefunc.pyx`, it seems that #15692 is also merged in that branch; I suspect the failure is actually due to that ticket (cf. comment:48:ticket:15692).",
    "created_at": "2016-03-26T09:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47918",
    "user": "pbruin"
}
```

Replying to [comment:34 vbraun]:
> http://build.sagedev.org/release/builders/%20%20slow%20AIMS%20%20%28Debian%207%2032%20bit%29%20incremental/builds/439/steps/shell_4/logs/stdio
From the failing doctest in `cachefunc.pyx`, it seems that #15692 is also merged in that branch; I suspect the failure is actually due to that ticket (cf. comment:48:ticket:15692).



---

archive/issue_comments_047919.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2016-03-26T09:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47919",
    "user": "pbruin"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_047920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-03-27T07:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6018#issuecomment-47920",
    "user": "vbraun"
}
```

Resolution: fixed
