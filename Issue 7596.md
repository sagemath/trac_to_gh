# Issue 7596: QQ.number_field() does not behave like any other NumberField

archive/issues_007596.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @slel\n\nHere's an example:\n\n\n```\nsage: K.<a> = NumberField(x)\nsage: K.ideal(5)\nFractional ideal (5)\nsage: QQ.ideal(5)\nPrincipal ideal (1) of Rational Field\nsage: QQ.number_field().ideal(5)\nPrincipal ideal (1) of Rational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7596\n\n",
    "created_at": "2009-12-03T20:06:43Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "QQ.number_field() does not behave like any other NumberField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7596",
    "user": "@rlmill"
}
```
Assignee: @loefflerd

CC:  @slel

Here's an example:


```
sage: K.<a> = NumberField(x)
sage: K.ideal(5)
Fractional ideal (5)
sage: QQ.ideal(5)
Principal ideal (1) of Rational Field
sage: QQ.number_field().ideal(5)
Principal ideal (1) of Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/7596





---

archive/issue_comments_064789.json:
```json
{
    "body": "sorry modified the wrong ticket, i meant to edit #9414 which is a duplicate of this one",
    "created_at": "2011-02-10T14:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64789",
    "user": "@koffie"
}
```

sorry modified the wrong ticket, i meant to edit #9414 which is a duplicate of this one



---

archive/issue_comments_064790.json:
```json
{
    "body": "Attachment [trac_7596_places_for_QQ.patch](tarball://root/attachments/some-uuid/ticket7596/trac_7596_places_for_QQ.patch) by @fchapoton created at 2013-07-25 14:17:23\n\nhere is already a ticket for the easy part : a method \"places\" for QQ",
    "created_at": "2013-07-25T14:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64790",
    "user": "@fchapoton"
}
```

Attachment [trac_7596_places_for_QQ.patch](tarball://root/attachments/some-uuid/ticket7596/trac_7596_places_for_QQ.patch) by @fchapoton created at 2013-07-25 14:17:23

here is already a ticket for the easy part : a method "places" for QQ



---

archive/issue_comments_064791.json:
```json
{
    "body": "I have imported a patch trying to have QQ and number fields in the same categories:\n\n```\nsage: K.<phi> = NumberField(x**2-x-1)\nsage: K.categories() == QQ.categories()\nTrue\n```\n\nbut this breaks the lcm and gcd in a bad way..",
    "created_at": "2013-07-26T12:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64791",
    "user": "@fchapoton"
}
```

I have imported a patch trying to have QQ and number fields in the same categories:

```
sage: K.<phi> = NumberField(x**2-x-1)
sage: K.categories() == QQ.categories()
True
```

but this breaks the lcm and gcd in a bad way..



---

archive/issue_comments_064792.json:
```json
{
    "body": "Attachment [trac_7596_number_fields_are_quotient_fields.patch](tarball://root/attachments/some-uuid/ticket7596/trac_7596_number_fields_are_quotient_fields.patch) by @fchapoton created at 2013-07-26 12:23:42",
    "created_at": "2013-07-26T12:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64792",
    "user": "@fchapoton"
}
```

Attachment [trac_7596_number_fields_are_quotient_fields.patch](tarball://root/attachments/some-uuid/ticket7596/trac_7596_number_fields_are_quotient_fields.patch) by @fchapoton created at 2013-07-26 12:23:42



---

archive/issue_comments_064793.json:
```json
{
    "body": "As of 9.3.beta3, certainly QQ.places() does work.  What I usually do is, when I find a method which QQ does not have but a general number field does have, in the course of implementing something, I just add an aimplementation for QQ.  I think this is more efficient than trying to make QQ work like a number field.  There will be a large number of users who get to see QQ who never use more general number fields.  For such people it does not matter at all to have methods like QQ.places() whose use they may not know.  There were many arguments about what QQ.ideal(5) should return, since the pedantic aswer (as for any field, with a nonzero generator) is that it has to be \"Principal ideal (1) of ...\".  Number theorists are quite happy to have K.ideal(...) meaning K.fractional_ideal(...).\n\nIs there any reason not to mark this as invalid/won't fix?",
    "created_at": "2021-02-08T13:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64793",
    "user": "@JohnCremona"
}
```

As of 9.3.beta3, certainly QQ.places() does work.  What I usually do is, when I find a method which QQ does not have but a general number field does have, in the course of implementing something, I just add an aimplementation for QQ.  I think this is more efficient than trying to make QQ work like a number field.  There will be a large number of users who get to see QQ who never use more general number fields.  For such people it does not matter at all to have methods like QQ.places() whose use they may not know.  There were many arguments about what QQ.ideal(5) should return, since the pedantic aswer (as for any field, with a nonzero generator) is that it has to be "Principal ideal (1) of ...".  Number theorists are quite happy to have K.ideal(...) meaning K.fractional_ideal(...).

Is there any reason not to mark this as invalid/won't fix?



---

archive/issue_comments_064794.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-02-09T11:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64794",
    "user": "@JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064795.json:
```json
{
    "body": "-1 for closing. I think comment:11 discloses a serious problem, though not exactly what is emphasized in the ticket description.  Number fields are rings:\n\n```\nsage: K.<a> = NumberField(x)\nsage: isinstance(K, Ring)\nTrue\n```\n\nThus, the `ideal` method of a number field needs to return an ideal of `self` (not an ideal of some subring of `self`), because that is what is expected by the `ideal` method of a `Ring`. Otherwise, well-written code involving rings will be buggy. \n\nI think that if number theorists are not willing to accept this, then `NumberField` should not inherit from `Ring`. But I think it would be better to introduce a new method (maybe `integer_ideal`) to the `NumberField` class, or add a keyword flag to the `ideal` method.",
    "created_at": "2021-02-09T20:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64795",
    "user": "@DaveWitteMorris"
}
```

-1 for closing. I think comment:11 discloses a serious problem, though not exactly what is emphasized in the ticket description.  Number fields are rings:

```
sage: K.<a> = NumberField(x)
sage: isinstance(K, Ring)
True
```

Thus, the `ideal` method of a number field needs to return an ideal of `self` (not an ideal of some subring of `self`), because that is what is expected by the `ideal` method of a `Ring`. Otherwise, well-written code involving rings will be buggy. 

I think that if number theorists are not willing to accept this, then `NumberField` should not inherit from `Ring`. But I think it would be better to introduce a new method (maybe `integer_ideal`) to the `NumberField` class, or add a keyword flag to the `ideal` method.



---

archive/issue_comments_064796.json:
```json
{
    "body": "We have had this discussion many times over the years.  I think I first had it in Jan 2008.  There are correct term for these: \"integral ideals\" and \"fractional ideals\". Calling them \"ideals\" is an abuse of language (agreed), just a common one.  There is no reason at all not to use \"fractional_ideal\" as the method name -- the class name is already `NumberFieldFractionalIdeal`.  But it would break a lot of users' code (including mine) so it is not a high priority for me.\n\nThis ticket has been open for 11 years...",
    "created_at": "2021-02-10T10:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64796",
    "user": "@JohnCremona"
}
```

We have had this discussion many times over the years.  I think I first had it in Jan 2008.  There are correct term for these: "integral ideals" and "fractional ideals". Calling them "ideals" is an abuse of language (agreed), just a common one.  There is no reason at all not to use "fractional_ideal" as the method name -- the class name is already `NumberFieldFractionalIdeal`.  But it would break a lot of users' code (including mine) so it is not a high priority for me.

This ticket has been open for 11 years...



---

archive/issue_comments_064797.json:
```json
{
    "body": "I think I can live with the practical effect of the implementation of `is_prime` on number field elements, but note that its documentation says:\n\n```\n        Is ``self`` a prime element?\n\n        A *prime* element is a non-zero, non-unit element `p` such that,\n        whenever `p` divides `ab` for some `a` and `b`, then `p`\n        divides `a` or `p` divides `b`.\n...\n        In fields, an element is never prime::\n...\n```\n\nso its documentation directly contradicts its behaviour. This is due to the fact that the method is inherited from `Ring`, but the `ideal` protocol is not compatibly implemented. That obviously needs fixing. In this case, it probably means equipping number field elements with a fresh implementation of `is_prime` with appropriate doc.\n\nReassigning this ticket to a milestone, because having documentation directly contradict behaviour is obviously something that not just generic \"low priority\" or \"not a bug\".",
    "created_at": "2021-08-02T16:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64797",
    "user": "@nbruin"
}
```

I think I can live with the practical effect of the implementation of `is_prime` on number field elements, but note that its documentation says:

```
        Is ``self`` a prime element?

        A *prime* element is a non-zero, non-unit element `p` such that,
        whenever `p` divides `ab` for some `a` and `b`, then `p`
        divides `a` or `p` divides `b`.
...
        In fields, an element is never prime::
...
```

so its documentation directly contradicts its behaviour. This is due to the fact that the method is inherited from `Ring`, but the `ideal` protocol is not compatibly implemented. That obviously needs fixing. In this case, it probably means equipping number field elements with a fresh implementation of `is_prime` with appropriate doc.

Reassigning this ticket to a milestone, because having documentation directly contradict behaviour is obviously something that not just generic "low priority" or "not a bug".



---

archive/issue_comments_064798.json:
```json
{
    "body": "Replying to [comment:15 nbruin]:\n> In this case, it probably means equipping number field elements with a fresh implementation of `is_prime` with appropriate doc.\n\nI had a shot at this over at #32340.",
    "created_at": "2021-08-12T05:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64798",
    "user": "@yyyyx4"
}
```

Replying to [comment:15 nbruin]:
> In this case, it probably means equipping number field elements with a fresh implementation of `is_prime` with appropriate doc.

I had a shot at this over at #32340.



---

archive/issue_comments_064799.json:
```json
{
    "body": "Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.",
    "created_at": "2021-12-18T19:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64799",
    "user": "@mkoeppe"
}
```

Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.



---

archive/issue_comments_064800.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2022-03-01T22:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7596#issuecomment-64800",
    "user": "@slel"
}
```

Changing status from needs_review to needs_work.
