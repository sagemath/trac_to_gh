# Issue 7830: function for floating point representation of a number

archive/issues_007830.json:
```json
{
    "body": "Assignee: @aghitza\n\nHere's a function that answers the question posed in http://groups.google.com/group/sage-devel/browse_thread/thread/c8c75b483f2c47f6 -- give the sign, mantissa, and exponent of a floating point number.\n\nI also cleaned up a few minor other things.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7830\n\n",
    "created_at": "2010-01-03T07:37:21Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "function for floating point representation of a number",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7830",
    "user": "@jasongrout"
}
```
Assignee: @aghitza

Here's a function that answers the question posed in http://groups.google.com/group/sage-devel/browse_thread/thread/c8c75b483f2c47f6 -- give the sign, mantissa, and exponent of a floating point number.

I also cleaned up a few minor other things.

Issue created by migration from https://trac.sagemath.org/ticket/7830





---

archive/issue_comments_067800.json:
```json
{
    "body": "Attachment [trac-7830-floating_point_representation.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-floating_point_representation.patch) by @jasongrout created at 2010-01-03 07:41:58",
    "created_at": "2010-01-03T07:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67800",
    "user": "@jasongrout"
}
```

Attachment [trac-7830-floating_point_representation.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-floating_point_representation.patch) by @jasongrout created at 2010-01-03 07:41:58



---

archive/issue_comments_067801.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T07:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67801",
    "user": "@jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067802.json:
```json
{
    "body": "Looks good. I don't like the name `representation()` either--maybe `parts()`?",
    "created_at": "2010-01-07T07:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67802",
    "user": "@robertwb"
}
```

Looks good. I don't like the name `representation()` either--maybe `parts()`?



---

archive/issue_comments_067803.json:
```json
{
    "body": "parts() seems too vague.  Maybe ieee_754_parts(), except that we support arbitrary precision, not just the set precisions they mention.  Maybe floating_point_representation(), or sign_mantissa_exponent().\n\nI'm willing to concede on the naming to make sure this gets in before I start my numerical analysis class in two weeks :).",
    "created_at": "2010-01-07T16:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67803",
    "user": "@jasongrout"
}
```

parts() seems too vague.  Maybe ieee_754_parts(), except that we support arbitrary precision, not just the set precisions they mention.  Maybe floating_point_representation(), or sign_mantissa_exponent().

I'm willing to concede on the naming to make sure this gets in before I start my numerical analysis class in two weeks :).



---

archive/issue_comments_067804.json:
```json
{
    "body": "Lets go with `sign_mantissa_exponent()`. Verbose but clear, and one doesn't even have to look at the docstring every time to remember what order the tuple comes in :)",
    "created_at": "2010-01-07T19:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67804",
    "user": "@robertwb"
}
```

Lets go with `sign_mantissa_exponent()`. Verbose but clear, and one doesn't even have to look at the docstring every time to remember what order the tuple comes in :)



---

archive/issue_comments_067805.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-01-08T12:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67805",
    "user": "@jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_067806.json:
```json
{
    "body": "Attachment [trac-7830-change-name.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-change-name.patch) by @jasongrout created at 2010-01-08 12:28:29\n\nOkay, I added a patch which changes the name.  This is hopefully ready for a positive review now :).",
    "created_at": "2010-01-08T12:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67806",
    "user": "@jasongrout"
}
```

Attachment [trac-7830-change-name.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-change-name.patch) by @jasongrout created at 2010-01-08 12:28:29

Okay, I added a patch which changes the name.  This is hopefully ready for a positive review now :).



---

archive/issue_comments_067807.json:
```json
{
    "body": "I see that you have only added this method to mpfr.  Should we not preserve as much consistency as possible between the different real types by also adding it to real_double?",
    "created_at": "2010-01-11T20:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67807",
    "user": "@JohnCremona"
}
```

I see that you have only added this method to mpfr.  Should we not preserve as much consistency as possible between the different real types by also adding it to real_double?



---

archive/issue_comments_067808.json:
```json
{
    "body": "Very good point.  I'll look at this.  I might just end up creating an RR number and calling this method behind the scenes",
    "created_at": "2010-01-11T22:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67808",
    "user": "@jasongrout"
}
```

Very good point.  I'll look at this.  I might just end up creating an RR number and calling this method behind the scenes



---

archive/issue_comments_067809.json:
```json
{
    "body": "Attachment [trac-7830-sign_m_e.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-sign_m_e.patch) by @jasongrout created at 2010-01-20 08:41:38\n\napply on top of previous patches",
    "created_at": "2010-01-20T08:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67809",
    "user": "@jasongrout"
}
```

Attachment [trac-7830-sign_m_e.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-sign_m_e.patch) by @jasongrout created at 2010-01-20 08:41:38

apply on top of previous patches



---

archive/issue_comments_067810.json:
```json
{
    "body": "I've added a similar function to RDF now.",
    "created_at": "2010-01-20T08:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67810",
    "user": "@jasongrout"
}
```

I've added a similar function to RDF now.



---

archive/issue_comments_067811.json:
```json
{
    "body": "http://en.wikipedia.org/wiki/IEEE_754-1985\n\nThe exponent for 0 should be 0. This also avoids the issue of platform dependance for that value, and `RDF(0)`'s exponent being unrealistically small. \n\nAlso, sage/rings/real_mpfr.pyx, line 1890 should be EXAMPLES::",
    "created_at": "2010-01-20T09:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67811",
    "user": "@robertwb"
}
```

http://en.wikipedia.org/wiki/IEEE_754-1985

The exponent for 0 should be 0. This also avoids the issue of platform dependance for that value, and `RDF(0)`'s exponent being unrealistically small. 

Also, sage/rings/real_mpfr.pyx, line 1890 should be EXAMPLES::



---

archive/issue_comments_067812.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T09:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67812",
    "user": "@robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067813.json:
```json
{
    "body": "Attachment [trac-7830-fixes.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-fixes.patch) by @jasongrout created at 2010-01-20 09:32:08\n\napply on top of previous patches",
    "created_at": "2010-01-20T09:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67813",
    "user": "@jasongrout"
}
```

Attachment [trac-7830-fixes.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-fixes.patch) by @jasongrout created at 2010-01-20 09:32:08

apply on top of previous patches



---

archive/issue_comments_067814.json:
```json
{
    "body": "The last patch fixes a few other documentation errors and an error in multiplicative_order too.  For free.",
    "created_at": "2010-01-20T09:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67814",
    "user": "@jasongrout"
}
```

The last patch fixes a few other documentation errors and an error in multiplicative_order too.  For free.



---

archive/issue_comments_067815.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T09:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67815",
    "user": "@jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067816.json:
```json
{
    "body": "all four of the above folded into one",
    "created_at": "2010-01-20T09:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67816",
    "user": "@robertwb"
}
```

all four of the above folded into one



---

archive/issue_comments_067817.json:
```json
{
    "body": "Attachment [7830-real-rep-all.patch](tarball://root/attachments/some-uuid/ticket7830/7830-real-rep-all.patch) by @robertwb created at 2010-01-20 09:40:55\n\nLooks good.",
    "created_at": "2010-01-20T09:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67817",
    "user": "@robertwb"
}
```

Attachment [7830-real-rep-all.patch](tarball://root/attachments/some-uuid/ticket7830/7830-real-rep-all.patch) by @robertwb created at 2010-01-20 09:40:55

Looks good.



---

archive/issue_comments_067818.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T09:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67818",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T21:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67819",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_067820.json:
```json
{
    "body": "The mantissa and exponent for MPFR is not the same as the mantissa and exponent for IEEE 754.  So I'm a little doubtful about the choice to follow IEEE 754 conventions for the exponent value of 0.  (but I'm not doubtful enough to change it).  I just thought I'd point out that the values from MPFR are different than the conventions from IEEE 754 for the same floating point number.",
    "created_at": "2010-01-26T21:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67820",
    "user": "@jasongrout"
}
```

The mantissa and exponent for MPFR is not the same as the mantissa and exponent for IEEE 754.  So I'm a little doubtful about the choice to follow IEEE 754 conventions for the exponent value of 0.  (but I'm not doubtful enough to change it).  I just thought I'd point out that the values from MPFR are different than the conventions from IEEE 754 for the same floating point number.
