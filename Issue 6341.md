# Issue 6341: implement Mestre's algorithm for constructing genus 2 hyperelliptic curves

archive/issues_006341.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan @mstreng jpflori lassina @fredstro\n\nKeywords: mestre algorithm genus 2 hyperelliptic curves\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6341\n\n",
    "created_at": "2009-06-16T19:48:36Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.13",
    "title": "implement Mestre's algorithm for constructing genus 2 hyperelliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6341",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @ncalexan @mstreng jpflori lassina @fredstro

Keywords: mestre algorithm genus 2 hyperelliptic curves



Issue created by migration from https://trac.sagemath.org/ticket/6341





---

archive/issue_comments_050527.json:
```json
{
    "body": "Attachment [trac_6341-mestre-extcode.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-extcode.patch) by @ncalexan created at 2009-06-16 19:53:15",
    "created_at": "2009-06-16T19:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50527",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6341-mestre-extcode.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-extcode.patch) by @ncalexan created at 2009-06-16 19:53:15



---

archive/issue_comments_050528.json:
```json
{
    "body": "Attachment [trac_6341-mestre.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre.patch) by @ncalexan created at 2009-06-16 19:55:08\n\nHere's a work in progress version.  The extcode patch\n\n* updates Denis Simon's pari qfsolve program;\n* and incorporates Paul van Wamelen's pari genus 2 package.\n\nThe main devel patch integrates everything, or at least starts to.",
    "created_at": "2009-06-16T19:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50528",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6341-mestre.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre.patch) by @ncalexan created at 2009-06-16 19:55:08

Here's a work in progress version.  The extcode patch

* updates Denis Simon's pari qfsolve program;
* and incorporates Paul van Wamelen's pari genus 2 package.

The main devel patch integrates everything, or at least starts to.



---

archive/issue_comments_050529.json:
```json
{
    "body": "Attachment [trac_6341-mestre-without-conic.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-without-conic.patch) by @mstreng created at 2009-06-18 18:31:26",
    "created_at": "2009-06-18T18:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50529",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_6341-mestre-without-conic.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-without-conic.patch) by @mstreng created at 2009-06-18 18:31:26



---

archive/issue_comments_050530.json:
```json
{
    "body": "Attachment [trac_6341-mestre-extcode-without-qfsolve.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-extcode-without-qfsolve.patch) by @mstreng created at 2009-06-18 18:36:09\n\nThe files \"-without...\" are the same as ncalexan's files, but with the Conic class removed and put in a separate patch at ticket 727. They still need the Conic class, but it may be better to view this as a separate enhancement.",
    "created_at": "2009-06-18T18:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50530",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_6341-mestre-extcode-without-qfsolve.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-extcode-without-qfsolve.patch) by @mstreng created at 2009-06-18 18:36:09

The files "-without..." are the same as ncalexan's files, but with the Conic class removed and put in a separate patch at ticket 727. They still need the Conic class, but it may be better to view this as a separate enhancement.



---

archive/issue_comments_050531.json:
```json
{
    "body": "This will be revived as part of a student project in August 2011.",
    "created_at": "2011-06-06T08:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50531",
    "user": "https://github.com/mstreng"
}
```

This will be revived as part of a student project in August 2011.



---

archive/issue_comments_050532.json:
```json
{
    "body": "Changing keywords from \"mestre algorithm genus 2 hyperelliptic curves\" to \"mestre algorithm genus 2 hyperelliptic curves sd35\".",
    "created_at": "2011-12-17T14:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50532",
    "user": "https://github.com/mstreng"
}
```

Changing keywords from "mestre algorithm genus 2 hyperelliptic curves" to "mestre algorithm genus 2 hyperelliptic curves sd35".



---

archive/issue_comments_050533.json:
```json
{
    "body": "Code was written by Florian Bouyer in September 2011, it works very nicely. Now it is a coding sprint at [Sage Days 35](http://wiki.sagemath.org/SageFlintDays/) to put this in.",
    "created_at": "2011-12-17T14:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50533",
    "user": "https://github.com/mstreng"
}
```

Code was written by Florian Bouyer in September 2011, it works very nicely. Now it is a coding sprint at [Sage Days 35](http://wiki.sagemath.org/SageFlintDays/) to put this in.



---

archive/issue_comments_050534.json:
```json
{
    "body": "Attachment [trac_6341_mestre_algorithm.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341_mestre_algorithm.patch) by florian created at 2011-12-19 11:47:01\n\nAn implementation of Mestre Algorithm",
    "created_at": "2011-12-19T11:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50534",
    "user": "https://trac.sagemath.org/admin/accounts/users/florian"
}
```

Attachment [trac_6341_mestre_algorithm.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341_mestre_algorithm.patch) by florian created at 2011-12-19 11:47:01

An implementation of Mestre Algorithm



---

archive/issue_comments_050535.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-19T13:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50535",
    "user": "https://trac.sagemath.org/admin/accounts/users/florian"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050536.json:
```json
{
    "body": "apply trac_6341_mestre_algorithm.patch\n\n(this helps [patchbot](http://wiki.sagemath.org/buildbot))",
    "created_at": "2011-12-19T21:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50536",
    "user": "https://github.com/mstreng"
}
```

apply trac_6341_mestre_algorithm.patch

(this helps [patchbot](http://wiki.sagemath.org/buildbot))



---

archive/issue_comments_050537.json:
```json
{
    "body": "See also #12199, which will later fill in some special cases.",
    "created_at": "2011-12-20T11:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50537",
    "user": "https://github.com/mstreng"
}
```

See also #12199, which will later fill in some special cases.



---

archive/issue_comments_050538.json:
```json
{
    "body": "See also #12200, which will later fill in some special case",
    "created_at": "2011-12-20T13:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50538",
    "user": "https://trac.sagemath.org/admin/accounts/users/florian"
}
```

See also #12200, which will later fill in some special case



---

archive/issue_comments_050539.json:
```json
{
    "body": "minor changes to first patch",
    "created_at": "2011-12-20T16:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50539",
    "user": "https://trac.sagemath.org/admin/accounts/users/florian"
}
```

minor changes to first patch



---

archive/issue_comments_050540.json:
```json
{
    "body": "Attachment [trac_6341_mestre_algoritm_2.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341_mestre_algoritm_2.patch) by florian created at 2011-12-20 16:07:48\n\nI corrected some typos and wasted white spaces pointed out by Marco",
    "created_at": "2011-12-20T16:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50540",
    "user": "https://trac.sagemath.org/admin/accounts/users/florian"
}
```

Attachment [trac_6341_mestre_algoritm_2.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341_mestre_algoritm_2.patch) by florian created at 2011-12-20 16:07:48

I corrected some typos and wasted white spaces pointed out by Marco



---

archive/issue_comments_050541.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-22T15:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50541",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050542.json:
```json
{
    "body": "I'm reviewing and writing a reviewer's patch. Looks very good, but some small changes are needed that are easier to do than to explain.",
    "created_at": "2011-12-22T15:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50542",
    "user": "https://github.com/mstreng"
}
```

I'm reviewing and writing a reviewer's patch. Looks very good, but some small changes are needed that are easier to do than to explain.



---

archive/issue_comments_050543.json:
```json
{
    "body": "Attachment [6341_combined.patch](tarball://root/attachments/some-uuid/ticket6341/6341_combined.patch) by @mstreng created at 2011-12-27 10:16:36",
    "created_at": "2011-12-27T10:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50543",
    "user": "https://github.com/mstreng"
}
```

Attachment [6341_combined.patch](tarball://root/attachments/some-uuid/ticket6341/6341_combined.patch) by @mstreng created at 2011-12-27 10:16:36



---

archive/issue_comments_050544.json:
```json
{
    "body": "I wrapped lines and clarified / corrected documentation and corrected some formulas. I also removed functions that were not needed.\n\nTo do:\n\n- continue with wrapping lines and checking documentation for spelling or formatting problems\n- add the missing examples and possibly some more with non-trivial reduction properties\n- remove functions marked with \"to_remove\"\n- make sure stoll-cremona reduction is correctly implemented when homogenized to higher degree than the degree of the polynomial\n- add a sanity check at the end of HyperellipticCurve_from_invariants, checking if the curve has the correct invariants before outputting it (RuntimeError otherwise)\n\napply 6341_combined.patch",
    "created_at": "2011-12-27T10:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50544",
    "user": "https://github.com/mstreng"
}
```

I wrapped lines and clarified / corrected documentation and corrected some formulas. I also removed functions that were not needed.

To do:

- continue with wrapping lines and checking documentation for spelling or formatting problems
- add the missing examples and possibly some more with non-trivial reduction properties
- remove functions marked with "to_remove"
- make sure stoll-cremona reduction is correctly implemented when homogenized to higher degree than the degree of the polynomial
- add a sanity check at the end of HyperellipticCurve_from_invariants, checking if the curve has the correct invariants before outputting it (RuntimeError otherwise)

apply 6341_combined.patch



---

archive/issue_comments_050545.json:
```json
{
    "body": "With a view towards the future (number fields), it may be a good idea to move the code from lines 679 -- 732 to a separate function with input a polynomial, a valuation and a uniformizer. If the uniformizer generates the prime ideal, this gives a local reduction that does not screw up the other primes. If this is not possible (e.g. a non-principal prime of a number field) you can still get a local reduction and combine the local reductions later.",
    "created_at": "2012-02-03T11:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50545",
    "user": "https://github.com/mstreng"
}
```

With a view towards the future (number fields), it may be a good idea to move the code from lines 679 -- 732 to a separate function with input a polynomial, a valuation and a uniformizer. If the uniformizer generates the prime ideal, this gives a local reduction that does not screw up the other primes. If this is not possible (e.g. a non-principal prime of a number field) you can still get a local reduction and combine the local reductions later.



---

archive/issue_comments_050546.json:
```json
{
    "body": "Attachment [mestre.patch](tarball://root/attachments/some-uuid/ticket6341/mestre.patch) by @mstreng created at 2012-03-12 10:26:09\n\nversion under construction, apply on top of previous patch, supposed to work for number fields, requires #11455",
    "created_at": "2012-03-12T10:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50546",
    "user": "https://github.com/mstreng"
}
```

Attachment [mestre.patch](tarball://root/attachments/some-uuid/ticket6341/mestre.patch) by @mstreng created at 2012-03-12 10:26:09

version under construction, apply on top of previous patch, supposed to work for number fields, requires #11455



---

archive/issue_comments_050547.json:
```json
{
    "body": "Attachment [6341-transformations.patch](tarball://root/attachments/some-uuid/ticket6341/6341-transformations.patch) by @mstreng created at 2012-04-07 14:28:59\n\non top of previous",
    "created_at": "2012-04-07T14:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50547",
    "user": "https://github.com/mstreng"
}
```

Attachment [6341-transformations.patch](tarball://root/attachments/some-uuid/ticket6341/6341-transformations.patch) by @mstreng created at 2012-04-07 14:28:59

on top of previous



---

archive/issue_comments_050548.json:
```json
{
    "body": "Attachment [6341-lifts.patch](tarball://root/attachments/some-uuid/ticket6341/6341-lifts.patch) by @mstreng created at 2013-03-20 22:41:16",
    "created_at": "2013-03-20T22:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50548",
    "user": "https://github.com/mstreng"
}
```

Attachment [6341-lifts.patch](tarball://root/attachments/some-uuid/ticket6341/6341-lifts.patch) by @mstreng created at 2013-03-20 22:41:16



---

archive/issue_comments_050549.json:
```json
{
    "body": "Attachment [6341-some_fixes.patch](tarball://root/attachments/some-uuid/ticket6341/6341-some_fixes.patch) by @mstreng created at 2013-03-20 23:19:23",
    "created_at": "2013-03-20T23:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50549",
    "user": "https://github.com/mstreng"
}
```

Attachment [6341-some_fixes.patch](tarball://root/attachments/some-uuid/ticket6341/6341-some_fixes.patch) by @mstreng created at 2013-03-20 23:19:23



---

archive/issue_comments_050550.json:
```json
{
    "body": "Attachment [6341-mestre-only.patch](tarball://root/attachments/some-uuid/ticket6341/6341-mestre-only.patch) by @mstreng created at 2013-06-17 13:06:23\n\nonly Mestre's algorithm",
    "created_at": "2013-06-17T13:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50550",
    "user": "https://github.com/mstreng"
}
```

Attachment [6341-mestre-only.patch](tarball://root/attachments/some-uuid/ticket6341/6341-mestre-only.patch) by @mstreng created at 2013-06-17 13:06:23

only Mestre's algorithm



---

archive/issue_comments_050551.json:
```json
{
    "body": "I separated off the (huge) reduction code from this simple functionality. Hopefully that helps in finishing this ticket.",
    "created_at": "2013-06-17T13:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50551",
    "user": "https://github.com/mstreng"
}
```

I separated off the (huge) reduction code from this simple functionality. Hopefully that helps in finishing this ticket.



---

archive/issue_comments_050552.json:
```json
{
    "body": "instructions for the patchbot :\n\napply 6341-mestre-only.patch",
    "created_at": "2013-07-09T09:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50552",
    "user": "https://github.com/fchapoton"
}
```

instructions for the patchbot :

apply 6341-mestre-only.patch



---

archive/issue_comments_050553.json:
```json
{
    "body": "here is patch, just cleaning things up. There are some doctests failing..\n\napply 6341-mestre-only.patch trac_6341-mestre-only_cleanup.patch",
    "created_at": "2013-07-09T09:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50553",
    "user": "https://github.com/fchapoton"
}
```

here is patch, just cleaning things up. There are some doctests failing..

apply 6341-mestre-only.patch trac_6341-mestre-only_cleanup.patch



---

archive/issue_comments_050554.json:
```json
{
    "body": "Attachment [trac_6341-mestre-only_cleanup.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-only_cleanup.patch) by @fchapoton created at 2013-07-17 19:55:55",
    "created_at": "2013-07-17T19:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50554",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_6341-mestre-only_cleanup.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341-mestre-only_cleanup.patch) by @fchapoton created at 2013-07-17 19:55:55



---

archive/issue_comments_050555.json:
```json
{
    "body": "Changing keywords from \"mestre algorithm genus 2 hyperelliptic curves sd35\" to \"mestre algorithm genus 2 hyperelliptic curves sd35 sd51\".",
    "created_at": "2013-07-22T13:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50555",
    "user": "https://github.com/mstreng"
}
```

Changing keywords from "mestre algorithm genus 2 hyperelliptic curves sd35" to "mestre algorithm genus 2 hyperelliptic curves sd35 sd51".



---

archive/issue_comments_050556.json:
```json
{
    "body": "Attachment [trac_6341_correcttions.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341_correcttions.patch) by florian created at 2013-07-23 13:11:12",
    "created_at": "2013-07-23T13:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50556",
    "user": "https://trac.sagemath.org/admin/accounts/users/florian"
}
```

Attachment [trac_6341_correcttions.patch](tarball://root/attachments/some-uuid/ticket6341/trac_6341_correcttions.patch) by florian created at 2013-07-23 13:11:12



---

archive/issue_comments_050557.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-23T13:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50557",
    "user": "https://trac.sagemath.org/admin/accounts/users/florian"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050558.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-07-24T11:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50558",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050559.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-24T12:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50559",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050560.json:
```json
{
    "body": "apply after the other three",
    "created_at": "2013-07-24T20:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50560",
    "user": "https://github.com/mstreng"
}
```

apply after the other three



---

archive/issue_comments_050561.json:
```json
{
    "body": "Attachment [6341-more-corrections.2.patch](tarball://root/attachments/some-uuid/ticket6341/6341-more-corrections.2.patch) by @mstreng created at 2013-07-24 20:16:34",
    "created_at": "2013-07-24T20:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50561",
    "user": "https://github.com/mstreng"
}
```

Attachment [6341-more-corrections.2.patch](tarball://root/attachments/some-uuid/ticket6341/6341-more-corrections.2.patch) by @mstreng created at 2013-07-24 20:16:34



---

archive/issue_comments_050562.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-07-24T20:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50562",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050563.json:
```json
{
    "body": "Attachment [6341-more-corrections.3.patch](tarball://root/attachments/some-uuid/ticket6341/6341-more-corrections.3.patch) by @mstreng created at 2013-07-25 06:44:24\n\n(testing now)",
    "created_at": "2013-07-25T06:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50563",
    "user": "https://github.com/mstreng"
}
```

Attachment [6341-more-corrections.3.patch](tarball://root/attachments/some-uuid/ticket6341/6341-more-corrections.3.patch) by @mstreng created at 2013-07-25 06:44:24

(testing now)



---

archive/issue_comments_050564.json:
```json
{
    "body": "for patchbot:\napply 6341-mestre-only.patch and trac_6341-mestre-only_cleanup.patch and 6341-mestre-corrections.3.patch",
    "created_at": "2013-07-25T06:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50564",
    "user": "https://github.com/mstreng"
}
```

for patchbot:
apply 6341-mestre-only.patch and trac_6341-mestre-only_cleanup.patch and 6341-mestre-corrections.3.patch



---

archive/issue_comments_050565.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-25T10:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50565",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050566.json:
```json
{
    "body": "apply 6341-mestre-only.patch and trac_6341-mestre-only_cleanup.patch and 6341-more-corrections.3.patch",
    "created_at": "2013-07-25T11:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50566",
    "user": "https://github.com/mstreng"
}
```

apply 6341-mestre-only.patch and trac_6341-mestre-only_cleanup.patch and 6341-more-corrections.3.patch



---

archive/issue_comments_050567.json:
```json
{
    "body": "I combined the patches into one, for easier review. Apply only 6341.patch",
    "created_at": "2013-08-27T11:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50567",
    "user": "https://github.com/mstreng"
}
```

I combined the patches into one, for easier review. Apply only 6341.patch



---

archive/issue_comments_050568.json:
```json
{
    "body": "ascii version of what was uploaded earlier this week",
    "created_at": "2013-08-28T19:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50568",
    "user": "https://github.com/mstreng"
}
```

ascii version of what was uploaded earlier this week



---

archive/issue_comments_050569.json:
```json
{
    "body": "Attachment [6341.patch](tarball://root/attachments/some-uuid/ticket6341/6341.patch) by @fchapoton created at 2013-09-15 19:52:55\n\napply only 6341.patch",
    "created_at": "2013-09-15T19:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50569",
    "user": "https://github.com/fchapoton"
}
```

Attachment [6341.patch](tarball://root/attachments/some-uuid/ticket6341/6341.patch) by @fchapoton created at 2013-09-15 19:52:55

apply only 6341.patch



---

archive/issue_comments_050570.json:
```json
{
    "body": "This is working for me.  I've verified several more non-CM examples in Magma.",
    "created_at": "2013-09-24T13:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50570",
    "user": "https://github.com/adeines"
}
```

This is working for me.  I've verified several more non-CM examples in Magma.



---

archive/issue_comments_050571.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-09-24T13:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50571",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050572.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-10-02T06:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6341",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6341#issuecomment-50572",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
