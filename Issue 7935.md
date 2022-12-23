# Issue 7935: local_data for elliptic curves over number fields

archive/issues_007935.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  cremona robertwb\n\nKeywords: elliptic curve, number fields, local data, tamagawa\n\nFirst of all, I spotted the following bug:\n\n\n```\nK.<a> = NumberField(x^2-38)\nE = EllipticCurve([a,1/2])\nE.global_integral_model()\n```\n\n\nwhich yields\n\n```\nAssertionError: bug in global_integral_model: [0, 0, 0, 4/361*a, 4/6859]\n```\n\n\nand that is easy to fix. But I also wish to add a `tamagawa_product` and improve the documentation.\n\nI will post a patch later today.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7935\n\n",
    "created_at": "2010-01-15T13:41:18Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "title": "local_data for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7935",
    "user": "wuthrich"
}
```
Assignee: cremona

CC:  cremona robertwb

Keywords: elliptic curve, number fields, local data, tamagawa

First of all, I spotted the following bug:


```
K.<a> = NumberField(x^2-38)
E = EllipticCurve([a,1/2])
E.global_integral_model()
```


which yields

```
AssertionError: bug in global_integral_model: [0, 0, 0, 4/361*a, 4/6859]
```


and that is easy to fix. But I also wish to add a `tamagawa_product` and improve the documentation.

I will post a patch later today.

Issue created by migration from https://trac.sagemath.org/ticket/7935





---

archive/issue_comments_069142.json:
```json
{
    "body": "Before I get complains, I'd better add that tamagawa_product will not be the product of tamagawa numbers, but rather it envolves also the changes to the local minimal model. It will be the term that appears in BSD. Something I always wanted to add.",
    "created_at": "2010-01-15T13:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69142",
    "user": "wuthrich"
}
```

Before I get complains, I'd better add that tamagawa_product will not be the product of tamagawa numbers, but rather it envolves also the changes to the local minimal model. It will be the term that appears in BSD. Something I always wanted to add.



---

archive/issue_comments_069143.json:
```json
{
    "body": "Thanks, I'll review it as soon as possible (I wrote the function so it is my fault!)",
    "created_at": "2010-01-15T13:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69143",
    "user": "cremona"
}
```

Thanks, I'll review it as soon as possible (I wrote the function so it is my fault!)



---

archive/issue_comments_069144.json:
```json
{
    "body": "Attachment\n\nexported against 4.3.alpha1",
    "created_at": "2010-01-15T15:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69144",
    "user": "wuthrich"
}
```

Attachment

exported against 4.3.alpha1



---

archive/issue_comments_069145.json:
```json
{
    "body": "I am not sure whether it is a good idea to have a definition of tamagawa_product for number fields that differs from the one for Q; but it is the only sensible definition. An option whould be to change the definition over Q; it would affect only non-minimal equation, but still it might break a lot of compatibility.\n\nThe very last thing in the patch, line 1024 in the new ell_number_field.py, is strange. It yields now a different global minimal model (yes they differ by a weierstrass-change with u a unit in K). If one computes this outside of this file one gets the old result. This may be linked to #7930, I don't know.",
    "created_at": "2010-01-15T15:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69145",
    "user": "wuthrich"
}
```

I am not sure whether it is a good idea to have a definition of tamagawa_product for number fields that differs from the one for Q; but it is the only sensible definition. An option whould be to change the definition over Q; it would affect only non-minimal equation, but still it might break a lot of compatibility.

The very last thing in the patch, line 1024 in the new ell_number_field.py, is strange. It yields now a different global minimal model (yes they differ by a weierstrass-change with u a unit in K). If one computes this outside of this file one gets the old result. This may be linked to #7930, I don't know.



---

archive/issue_comments_069146.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-15T15:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69146",
    "user": "wuthrich"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069147.json:
```json
{
    "body": "Thanks for all the excellent documentation!\n\nAbout the bug:  I am puzzled by this, as I still don't see how either my original code failed or how the change (of uniformiser) works best.  Here was my thinking:  if val(a_i)<0 for some i, then find the minimal e such that e*i+valuation(a_i) is >=0 for i in [1,2,3,4,6] and then replace a_i by `a_i/pi^(e*i)`.  The point about using the \"negative\" flag on the uniformiser was so ensure that dividing by a power of pi maintained integrality at all other primes.  Your new code will not do that.\n\nWould this be better:\n\n```\n        D = self.discriminant()\n        for P in D.prime_factors():\n            if not all([a.valuation(P)>=0 for a in ai]):\n                   pi=K.uniformizer(P,'negative')\n                   e  = min([(ai[i].valuation(P)/[1,2,3,4,6][i]) for i in range(5)]).floor()\n                   ai = [ai[i]/pi**(e*[1,2,3,4,6][i]) for i in range(5)]\n```\n\n? \n\nI have not looked at your last point yet.  I am not so keen on tamagawa_product() not giving the product of the Tamagawa numbers.  Are you sure that over Q when an equation is non-minimal at p that the number returned by tamagawa_number() is not the index for the minimal model?  I thought that was what Tate's algorithm would give.  I'll need to look at it more closely.\n\n\nI am leaving this as \"needs review\" as I have not actually tested it yet!",
    "created_at": "2010-01-15T16:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69147",
    "user": "cremona"
}
```

Thanks for all the excellent documentation!

About the bug:  I am puzzled by this, as I still don't see how either my original code failed or how the change (of uniformiser) works best.  Here was my thinking:  if val(a_i)<0 for some i, then find the minimal e such that e*i+valuation(a_i) is >=0 for i in [1,2,3,4,6] and then replace a_i by `a_i/pi^(e*i)`.  The point about using the "negative" flag on the uniformiser was so ensure that dividing by a power of pi maintained integrality at all other primes.  Your new code will not do that.

Would this be better:

```
        D = self.discriminant()
        for P in D.prime_factors():
            if not all([a.valuation(P)>=0 for a in ai]):
                   pi=K.uniformizer(P,'negative')
                   e  = min([(ai[i].valuation(P)/[1,2,3,4,6][i]) for i in range(5)]).floor()
                   ai = [ai[i]/pi**(e*[1,2,3,4,6][i]) for i in range(5)]
```

? 

I have not looked at your last point yet.  I am not so keen on tamagawa_product() not giving the product of the Tamagawa numbers.  Are you sure that over Q when an equation is non-minimal at p that the number returned by tamagawa_number() is not the index for the minimal model?  I thought that was what Tate's algorithm would give.  I'll need to look at it more closely.


I am leaving this as "needs review" as I have not actually tested it yet!



---

archive/issue_comments_069148.json:
```json
{
    "body": "Maybe you make a little sign error ? In the bug-example, the valuation of a6 at P = (a) is -2. So e is -1. So you are really multiplying the ais by pi<sup>+i</sup>. So pi should be integral away from P.\n\nAs to your comment on `tamagawa_product()`, we have\n\n\n```\nsage: E = EllipticCurve('11a2')\nsage: E.tamagawa_product()\n1\n\nsage: E2 = E.change_weierstrass_model([1/11,0,0,1])\nsage: E2\nElliptic Curve defined by y^2 + 3993*y = x^3 - 121*x^2 - 114492620*x - 466951591502 over Rational Field\nsage: E2.tamagawa_product()\n1\n```\n\n\nSo it is defined to be the product of the Tamagawa numbers (i.e. the index of E<sup>0</sup> (K_v)) on the minimal model.\n\nMy definition (and that is the only sensible over number fields) of `tamagawa_product()` changes as one changes the chosen invariant differential in such a way that the product of it with the periods is invariant under this choice. In particular it is not the product of the Tamagawa numbers despite the name.",
    "created_at": "2010-01-15T17:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69148",
    "user": "wuthrich"
}
```

Maybe you make a little sign error ? In the bug-example, the valuation of a6 at P = (a) is -2. So e is -1. So you are really multiplying the ais by pi<sup>+i</sup>. So pi should be integral away from P.

As to your comment on `tamagawa_product()`, we have


```
sage: E = EllipticCurve('11a2')
sage: E.tamagawa_product()
1

sage: E2 = E.change_weierstrass_model([1/11,0,0,1])
sage: E2
Elliptic Curve defined by y^2 + 3993*y = x^3 - 121*x^2 - 114492620*x - 466951591502 over Rational Field
sage: E2.tamagawa_product()
1
```


So it is defined to be the product of the Tamagawa numbers (i.e. the index of E<sup>0</sup> (K_v)) on the minimal model.

My definition (and that is the only sensible over number fields) of `tamagawa_product()` changes as one changes the chosen invariant differential in such a way that the product of it with the periods is invariant under this choice. In particular it is not the product of the Tamagawa numbers despite the name.



---

archive/issue_comments_069149.json:
```json
{
    "body": "OK, I agree that there was a sign error...   The value of e in the code is always negative (since we skip if a is integral, hence at least one of the fractions (which are rounded down by the \"/\" operator) is negative.  Hence we divide by a negative power of pi, i.e. multiply by a positive power, so haveing pi integral is exactly what you want.  You win! \n\nSorry, it's 5.30 on a Friday after the first week of term.\n\nOn the T. products, can we come up with a different name for one of the functions since they don't agree?  Either that, of have an optional parameter in the case over Q to give the same value as if Q were treated as a number field?",
    "created_at": "2010-01-15T17:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69149",
    "user": "cremona"
}
```

OK, I agree that there was a sign error...   The value of e in the code is always negative (since we skip if a is integral, hence at least one of the fractions (which are rounded down by the "/" operator) is negative.  Hence we divide by a negative power of pi, i.e. multiply by a positive power, so haveing pi integral is exactly what you want.  You win! 

Sorry, it's 5.30 on a Friday after the first week of term.

On the T. products, can we come up with a different name for one of the functions since they don't agree?  Either that, of have an optional parameter in the case over Q to give the same value as if Q were treated as a number field?



---

archive/issue_comments_069150.json:
```json
{
    "body": "Positive review:  applies fine to 4.3.1.alpha2, all tests in sage/schemes/elliptic_curves pass, docs build well (there's a lot of useful extra documentation in the patch), and I agree with the design decisions made.\n\nThanks for fixing the bug in my code (and more!)",
    "created_at": "2010-01-15T20:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69150",
    "user": "cremona"
}
```

Positive review:  applies fine to 4.3.1.alpha2, all tests in sage/schemes/elliptic_curves pass, docs build well (there's a lot of useful extra documentation in the patch), and I agree with the design decisions made.

Thanks for fixing the bug in my code (and more!)



---

archive/issue_comments_069151.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-15T20:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69151",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069152.json:
```json
{
    "body": "\n```\nFile \"sage/schemes/elliptic_curves/ell_number_field.py\", line 1026:\n    sage: E2\nExpected:\n    Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (12289755603565800754*a-75759141535687466985)*x + (51556320144761417221790307379*a-317814501841918807353201512829) over Number Field in a with defining polynomial x^2 - 38\nGot:\n    Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (368258520200522046806318444*a-2270097978636731786720859345)*x + (8456608930173478039472018047583706316424*a-52130038506793883217874390501829588391299) over Number Field in a with defining polynomial x^2 - 38\n**********************************************************************\n```\n",
    "created_at": "2010-01-19T00:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69152",
    "user": "rlm"
}
```


```
File "sage/schemes/elliptic_curves/ell_number_field.py", line 1026:
    sage: E2
Expected:
    Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (12289755603565800754*a-75759141535687466985)*x + (51556320144761417221790307379*a-317814501841918807353201512829) over Number Field in a with defining polynomial x^2 - 38
Got:
    Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (368258520200522046806318444*a-2270097978636731786720859345)*x + (8456608930173478039472018047583706316424*a-52130038506793883217874390501829588391299) over Number Field in a with defining polynomial x^2 - 38
**********************************************************************
```




---

archive/issue_comments_069153.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-19T00:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69153",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_069154.json:
```json
{
    "body": "This is very strange.  For that curve E2, I sometimes get\n\n```\nElliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (12289755603565800754*a-75759141535687466985)*x + (51556320144761417221790307379*a-317814501841918807353201512829) over Number Field in a with defining polynomial x^2 - 38\n```\n\nbut sometimes I get\n\n```\nElliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (368258520200522046806318444*a-2270097978636731786720859345)*x + (8456608930173478039472018047583706316424*a-52130038506793883217874390501829588391299) over Number Field in a with defining polynomial x^2 - 38\n```\n\non the same machine.  (Note that both are valid, since both are models with a unit Discriminant so are certainly global minimal models.)\n\nThe only way round this I can see in the short term is to remove the line in the doctest which displays E2 itself.  What do people think?",
    "created_at": "2010-01-19T14:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69154",
    "user": "cremona"
}
```

This is very strange.  For that curve E2, I sometimes get

```
Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (12289755603565800754*a-75759141535687466985)*x + (51556320144761417221790307379*a-317814501841918807353201512829) over Number Field in a with defining polynomial x^2 - 38
```

but sometimes I get

```
Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (368258520200522046806318444*a-2270097978636731786720859345)*x + (8456608930173478039472018047583706316424*a-52130038506793883217874390501829588391299) over Number Field in a with defining polynomial x^2 - 38
```

on the same machine.  (Note that both are valid, since both are models with a unit Discriminant so are certainly global minimal models.)

The only way round this I can see in the short term is to remove the line in the doctest which displays E2 itself.  What do people think?



---

archive/issue_comments_069155.json:
```json
{
    "body": "I was afraid that this would happen. I strongly believe that this is the same bug as #7930.\nBoth answers are valid global minimal models (as mentionned earlier), I could propose that we put a #random behind it and wait for #7930 to be solved.",
    "created_at": "2010-01-19T14:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69155",
    "user": "wuthrich"
}
```

I was afraid that this would happen. I strongly believe that this is the same bug as #7930.
Both answers are valid global minimal models (as mentionned earlier), I could propose that we put a #random behind it and wait for #7930 to be solved.



---

archive/issue_comments_069156.json:
```json
{
    "body": "As we are back to review: What about another name for `tamagawa_product`. It seems not a bad name for what it is, but I admit that John objection is a fair one. What other names could we give it ?",
    "created_at": "2010-01-19T14:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69156",
    "user": "wuthrich"
}
```

As we are back to review: What about another name for `tamagawa_product`. It seems not a bad name for what it is, but I admit that John objection is a fair one. What other names could we give it ?



---

archive/issue_comments_069157.json:
```json
{
    "body": "Replying to [comment:11 wuthrich]:\n> I was afraid that this would happen. I strongly believe that this is the same bug as #7930.\n> Both answers are valid global minimal models (as mentionned earlier), I could propose that we put a #random behind it and wait for #7930 to be solved. \n\nI'll go with that.  I'll even put in a comment after the #random saying (minimal model is not unique).",
    "created_at": "2010-01-19T15:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69157",
    "user": "cremona"
}
```

Replying to [comment:11 wuthrich]:
> I was afraid that this would happen. I strongly believe that this is the same bug as #7930.
> Both answers are valid global minimal models (as mentionned earlier), I could propose that we put a #random behind it and wait for #7930 to be solved. 

I'll go with that.  I'll even put in a comment after the #random saying (minimal model is not unique).



---

archive/issue_comments_069158.json:
```json
{
    "body": "Replying to [comment:12 wuthrich]:\n> As we are back to review: What about another name for `tamagawa_product`. It seems not a bad name for what it is, but I admit that John objection is a fair one. What other names could we give it ?\n\nHowe about bsd_tamagawa_product() or minimal_tamagawa_product()?",
    "created_at": "2010-01-19T15:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69158",
    "user": "cremona"
}
```

Replying to [comment:12 wuthrich]:
> As we are back to review: What about another name for `tamagawa_product`. It seems not a bad name for what it is, but I admit that John objection is a fair one. What other names could we give it ?

Howe about bsd_tamagawa_product() or minimal_tamagawa_product()?



---

archive/issue_comments_069159.json:
```json
{
    "body": "Patch trac_7935b.patch adds the #random tag.",
    "created_at": "2010-01-19T15:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69159",
    "user": "cremona"
}
```

Patch trac_7935b.patch adds the #random tag.



---

archive/issue_comments_069160.json:
```json
{
    "body": "> How about bsd_tamagawa_product() or minimal_tamagawa_product()?\n\nthe first one would be ok, the second is missleading as it is not minimal.\n\ntamagawa_product_bsd or tamagawa_product_as_in_bsd so that the tab still\ncompletes it as before.",
    "created_at": "2010-01-19T15:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69160",
    "user": "wuthrich"
}
```

> How about bsd_tamagawa_product() or minimal_tamagawa_product()?

the first one would be ok, the second is missleading as it is not minimal.

tamagawa_product_bsd or tamagawa_product_as_in_bsd so that the tab still
completes it as before.



---

archive/issue_comments_069161.json:
```json
{
    "body": "Attachment\n\nApply after previous",
    "created_at": "2010-01-19T15:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69161",
    "user": "cremona"
}
```

Attachment

Apply after previous



---

archive/issue_comments_069162.json:
```json
{
    "body": "The new version of trac_7935b.patch changes the name to tamagawa_product_bsd .\n\nChris, if you are happy with this second patch now you can give it a positive review.",
    "created_at": "2010-01-19T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69162",
    "user": "cremona"
}
```

The new version of trac_7935b.patch changes the name to tamagawa_product_bsd .

Chris, if you are happy with this second patch now you can give it a positive review.



---

archive/issue_comments_069163.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69163",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069164.json:
```json
{
    "body": "Sorry, John, I could not apply your patch, the last hunk failed. Maybe because I did not upgrade yet. I try again later.",
    "created_at": "2010-01-20T23:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69164",
    "user": "wuthrich"
}
```

Sorry, John, I could not apply your patch, the last hunk failed. Maybe because I did not upgrade yet. I try again later.



---

archive/issue_comments_069165.json:
```json
{
    "body": "I will rebase it.  Something else must have merged since which messed up line numbers or something.",
    "created_at": "2010-01-21T11:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69165",
    "user": "cremona"
}
```

I will rebase it.  Something else must have merged since which messed up line numbers or something.



---

archive/issue_comments_069166.json:
```json
{
    "body": "second patch to be applied after the first patch, exported against 4.3.1",
    "created_at": "2010-01-21T13:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69166",
    "user": "wuthrich"
}
```

second patch to be applied after the first patch, exported against 4.3.1



---

archive/issue_comments_069167.json:
```json
{
    "body": "Attachment\n\nI have rebased it.",
    "created_at": "2010-01-21T13:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69167",
    "user": "wuthrich"
}
```

Attachment

I have rebased it.



---

archive/issue_comments_069168.json:
```json
{
    "body": "Sorry for the delay.  Apply the first and third patches to 4.3.1 -- all works.",
    "created_at": "2010-01-31T17:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69168",
    "user": "cremona"
}
```

Sorry for the delay.  Apply the first and third patches to 4.3.1 -- all works.



---

archive/issue_comments_069169.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T17:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69169",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069170.json:
```json
{
    "body": "Please update the Author and Reviewer fields, if they're wrong.",
    "created_at": "2010-02-11T15:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69170",
    "user": "mpatel"
}
```

Please update the Author and Reviewer fields, if they're wrong.



---

archive/issue_comments_069171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69171",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_069172.json:
```json
{
    "body": "I think we can leave it as it is although 99% of the work is by Chris.",
    "created_at": "2010-02-11T15:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7935#issuecomment-69172",
    "user": "cremona"
}
```

I think we can leave it as it is although 99% of the work is by Chris.
