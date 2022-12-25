# Issue 7830: function for floating point representation of a number

archive/issues_007830.json:
```json
{
    "body": "Assignee: @aghitza\n\nHere's a function that answers the question posed in http://groups.google.com/group/sage-devel/browse_thread/thread/c8c75b483f2c47f6 -- give the sign, mantissa, and exponent of a floating point number.\n\nI also cleaned up a few minor other things.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7830\n\n",
    "created_at": "2010-01-03T07:37:21Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "function for floating point representation of a number",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7830",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @aghitza

Here's a function that answers the question posed in http://groups.google.com/group/sage-devel/browse_thread/thread/c8c75b483f2c47f6 -- give the sign, mantissa, and exponent of a floating point number.

I also cleaned up a few minor other things.

Issue created by migration from https://trac.sagemath.org/ticket/7830





---

archive/issue_comments_067683.json:
```json
{
    "body": "Attachment [trac-7830-floating_point_representation.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-floating_point_representation.patch) by @jasongrout created at 2010-01-03 07:41:58",
    "created_at": "2010-01-03T07:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67683",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7830-floating_point_representation.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-floating_point_representation.patch) by @jasongrout created at 2010-01-03 07:41:58



---

archive/issue_comments_067684.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T07:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67684",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067685.json:
```json
{
    "body": "Looks good. I don't like the name `representation()` either--maybe `parts()`?",
    "created_at": "2010-01-07T07:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67685",
    "user": "https://github.com/robertwb"
}
```

Looks good. I don't like the name `representation()` either--maybe `parts()`?



---

archive/issue_comments_067686.json:
```json
{
    "body": "parts() seems too vague.  Maybe ieee_754_parts(), except that we support arbitrary precision, not just the set precisions they mention.  Maybe floating_point_representation(), or sign_mantissa_exponent().\n\nI'm willing to concede on the naming to make sure this gets in before I start my numerical analysis class in two weeks :).",
    "created_at": "2010-01-07T16:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67686",
    "user": "https://github.com/jasongrout"
}
```

parts() seems too vague.  Maybe ieee_754_parts(), except that we support arbitrary precision, not just the set precisions they mention.  Maybe floating_point_representation(), or sign_mantissa_exponent().

I'm willing to concede on the naming to make sure this gets in before I start my numerical analysis class in two weeks :).



---

archive/issue_comments_067687.json:
```json
{
    "body": "Lets go with `sign_mantissa_exponent()`. Verbose but clear, and one doesn't even have to look at the docstring every time to remember what order the tuple comes in :)",
    "created_at": "2010-01-07T19:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67687",
    "user": "https://github.com/robertwb"
}
```

Lets go with `sign_mantissa_exponent()`. Verbose but clear, and one doesn't even have to look at the docstring every time to remember what order the tuple comes in :)



---

archive/issue_comments_067688.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-01-08T12:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67688",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_067689.json:
```json
{
    "body": "Attachment [trac-7830-change-name.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-change-name.patch) by @jasongrout created at 2010-01-08 12:28:29\n\nOkay, I added a patch which changes the name.  This is hopefully ready for a positive review now :).",
    "created_at": "2010-01-08T12:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67689",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7830-change-name.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-change-name.patch) by @jasongrout created at 2010-01-08 12:28:29

Okay, I added a patch which changes the name.  This is hopefully ready for a positive review now :).



---

archive/issue_comments_067690.json:
```json
{
    "body": "I see that you have only added this method to mpfr.  Should we not preserve as much consistency as possible between the different real types by also adding it to real_double?",
    "created_at": "2010-01-11T20:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67690",
    "user": "https://github.com/JohnCremona"
}
```

I see that you have only added this method to mpfr.  Should we not preserve as much consistency as possible between the different real types by also adding it to real_double?



---

archive/issue_comments_067691.json:
```json
{
    "body": "Very good point.  I'll look at this.  I might just end up creating an RR number and calling this method behind the scenes",
    "created_at": "2010-01-11T22:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67691",
    "user": "https://github.com/jasongrout"
}
```

Very good point.  I'll look at this.  I might just end up creating an RR number and calling this method behind the scenes



---

archive/issue_comments_067692.json:
```json
{
    "body": "Attachment [trac-7830-sign_m_e.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-sign_m_e.patch) by @jasongrout created at 2010-01-20 08:41:38\n\napply on top of previous patches",
    "created_at": "2010-01-20T08:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67692",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7830-sign_m_e.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-sign_m_e.patch) by @jasongrout created at 2010-01-20 08:41:38

apply on top of previous patches



---

archive/issue_comments_067693.json:
```json
{
    "body": "I've added a similar function to RDF now.",
    "created_at": "2010-01-20T08:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67693",
    "user": "https://github.com/jasongrout"
}
```

I've added a similar function to RDF now.



---

archive/issue_comments_067694.json:
```json
{
    "body": "http://en.wikipedia.org/wiki/IEEE_754-1985\n\nThe exponent for 0 should be 0. This also avoids the issue of platform dependance for that value, and `RDF(0)`'s exponent being unrealistically small. \n\nAlso, sage/rings/real_mpfr.pyx, line 1890 should be EXAMPLES::",
    "created_at": "2010-01-20T09:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67694",
    "user": "https://github.com/robertwb"
}
```

http://en.wikipedia.org/wiki/IEEE_754-1985

The exponent for 0 should be 0. This also avoids the issue of platform dependance for that value, and `RDF(0)`'s exponent being unrealistically small. 

Also, sage/rings/real_mpfr.pyx, line 1890 should be EXAMPLES::



---

archive/issue_comments_067695.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T09:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67695",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067696.json:
```json
{
    "body": "Attachment [trac-7830-fixes.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-fixes.patch) by @jasongrout created at 2010-01-20 09:32:08\n\napply on top of previous patches",
    "created_at": "2010-01-20T09:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67696",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7830-fixes.patch](tarball://root/attachments/some-uuid/ticket7830/trac-7830-fixes.patch) by @jasongrout created at 2010-01-20 09:32:08

apply on top of previous patches



---

archive/issue_comments_067697.json:
```json
{
    "body": "The last patch fixes a few other documentation errors and an error in multiplicative_order too.  For free.",
    "created_at": "2010-01-20T09:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67697",
    "user": "https://github.com/jasongrout"
}
```

The last patch fixes a few other documentation errors and an error in multiplicative_order too.  For free.



---

archive/issue_comments_067698.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T09:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67698",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067699.json:
```json
{
    "body": "all four of the above folded into one",
    "created_at": "2010-01-20T09:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67699",
    "user": "https://github.com/robertwb"
}
```

all four of the above folded into one



---

archive/issue_comments_067700.json:
```json
{
    "body": "Attachment [7830-real-rep-all.patch](tarball://root/attachments/some-uuid/ticket7830/7830-real-rep-all.patch) by @robertwb created at 2010-01-20 09:40:55\n\nLooks good.",
    "created_at": "2010-01-20T09:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67700",
    "user": "https://github.com/robertwb"
}
```

Attachment [7830-real-rep-all.patch](tarball://root/attachments/some-uuid/ticket7830/7830-real-rep-all.patch) by @robertwb created at 2010-01-20 09:40:55

Looks good.



---

archive/issue_comments_067701.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T09:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67701",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067702.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T21:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67702",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_018729.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-22T21:11:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7830#event-18729"
}
```



---

archive/issue_comments_067703.json:
```json
{
    "body": "The mantissa and exponent for MPFR is not the same as the mantissa and exponent for IEEE 754.  So I'm a little doubtful about the choice to follow IEEE 754 conventions for the exponent value of 0.  (but I'm not doubtful enough to change it).  I just thought I'd point out that the values from MPFR are different than the conventions from IEEE 754 for the same floating point number.",
    "created_at": "2010-01-26T21:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7830#issuecomment-67703",
    "user": "https://github.com/jasongrout"
}
```

The mantissa and exponent for MPFR is not the same as the mantissa and exponent for IEEE 754.  So I'm a little doubtful about the choice to follow IEEE 754 conventions for the exponent value of 0.  (but I'm not doubtful enough to change it).  I just thought I'd point out that the values from MPFR are different than the conventions from IEEE 754 for the same floating point number.
