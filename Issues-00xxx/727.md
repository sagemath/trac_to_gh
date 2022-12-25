# Issue 727: find rational points on plane conic curves

archive/issues_000727.json:
```json
{
    "body": "Assignee: @mstreng\n\nCC:  @ncalexan justin @mstreng @rlmill @pjbruin\n\nKeywords: rational point points conic quadratic form\n\nImplement a Conic class that is able to\n\n* find rational points on plane conic curves over QQ, finite fields, RR, CC.\n\n* given a conic with a point over a field, compute a parametrization.\n\nIssue created by migration from https://trac.sagemath.org/ticket/727\n\n",
    "closed_at": "2011-01-25T08:13:28Z",
    "created_at": "2007-09-21T08:45:15Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "find rational points on plane conic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/727",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mstreng

CC:  @ncalexan justin @mstreng @rlmill @pjbruin

Keywords: rational point points conic quadratic form

Implement a Conic class that is able to

* find rational points on plane conic curves over QQ, finite fields, RR, CC.

* given a conic with a point over a field, compute a parametrization.

Issue created by migration from https://trac.sagemath.org/ticket/727





---

archive/issue_comments_004221.json:
```json
{
    "body": "Changing component from basic arithmetic to algebraic geometry.",
    "created_at": "2008-01-27T05:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4221",
    "user": "https://github.com/aghitza"
}
```

Changing component from basic arithmetic to algebraic geometry.



---

archive/issue_comments_004222.json:
```json
{
    "body": "Changing assignee from somebody to @williamstein.",
    "created_at": "2008-01-27T05:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4222",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from somebody to @williamstein.



---

archive/issue_comments_004223.json:
```json
{
    "body": "This is so random -- I have written code to do this.  We already distribute Denis Simon's code to solve such systems, and I have have integrated a little of it.  Patch coming up.  Please talk to me before implementing this.",
    "created_at": "2008-02-29T08:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4223",
    "user": "https://github.com/ncalexan"
}
```

This is so random -- I have written code to do this.  We already distribute Denis Simon's code to solve such systems, and I have have integrated a little of it.  Patch coming up.  Please talk to me before implementing this.



---

archive/issue_comments_004224.json:
```json
{
    "body": "Changing keywords from \"\" to \"rational point points conic quadratic form\".",
    "created_at": "2008-02-29T08:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4224",
    "user": "https://github.com/ncalexan"
}
```

Changing keywords from "" to "rational point points conic quadratic form".



---

archive/issue_comments_004225.json:
```json
{
    "body": "Changing assignee from @williamstein to justin.",
    "created_at": "2008-11-08T21:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to justin.



---

archive/issue_comments_004226.json:
```json
{
    "body": "Changing component from algebraic geometry to quadratic forms.",
    "created_at": "2008-11-08T21:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4226",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebraic geometry to quadratic forms.



---

archive/issue_comments_004227.json:
```json
{
    "body": "Define a Conic class with an interface to Denis Simon's qfsolve",
    "created_at": "2009-06-18T18:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4227",
    "user": "https://github.com/mstreng"
}
```

Define a Conic class with an interface to Denis Simon's qfsolve



---

archive/issue_comments_004228.json:
```json
{
    "body": "Changing assignee from justin to mhampton.",
    "created_at": "2009-06-18T18:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4228",
    "user": "https://github.com/mstreng"
}
```

Changing assignee from justin to mhampton.



---

archive/issue_comments_004229.json:
```json
{
    "body": "Attachment [trac_727-conic.patch](tarball://root/attachments/some-uuid/ticket727/trac_727-conic.patch) by @mstreng created at 2009-06-18 18:15:53\n\nThe patches I just uploaded were part of ncalexan's patch for ticket 6341, implementing Mestre's algorithm. They implement a Conic class and allow one to find points over the rationals. This Conic class needs to be expanded to provide much more functionality, such as finding points and/or rational parametrizations over other fields. If the original question is only for the rationals, then that at least is answered.",
    "created_at": "2009-06-18T18:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4229",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727-conic.patch](tarball://root/attachments/some-uuid/ticket727/trac_727-conic.patch) by @mstreng created at 2009-06-18 18:15:53

The patches I just uploaded were part of ncalexan's patch for ticket 6341, implementing Mestre's algorithm. They implement a Conic class and allow one to find points over the rationals. This Conic class needs to be expanded to provide much more functionality, such as finding points and/or rational parametrizations over other fields. If the original question is only for the rationals, then that at least is answered.



---

archive/issue_comments_004230.json:
```json
{
    "body": "Changing component from quadratic forms to geometry.",
    "created_at": "2009-06-18T18:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4230",
    "user": "https://github.com/mstreng"
}
```

Changing component from quadratic forms to geometry.



---

archive/issue_comments_004231.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-23T12:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4231",
    "user": "https://github.com/mstreng"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004232.json:
```json
{
    "body": "Changing assignee from mhampton to @mstreng.",
    "created_at": "2009-06-23T12:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4232",
    "user": "https://github.com/mstreng"
}
```

Changing assignee from mhampton to @mstreng.



---

archive/issue_comments_004233.json:
```json
{
    "body": "I'll work on the Conic class.",
    "created_at": "2009-06-23T12:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4233",
    "user": "https://github.com/mstreng"
}
```

I'll work on the Conic class.



---

archive/issue_comments_004234.json:
```json
{
    "body": "Attachment [trac_727_more_conic_files.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files.patch) by @mstreng created at 2010-07-06 14:23:12",
    "created_at": "2010-07-06T14:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4234",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_more_conic_files.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files.patch) by @mstreng created at 2010-07-06 14:23:12



---

archive/issue_comments_004235.json:
```json
{
    "body": "* this is being revived at Sage Days 23\n\n* trac_727-conic-extcode.patch should be removed: it updates Denis Simon's code from 2005 to 2007, while 2009 is already shipped with the latest Sage\n\n* trac_727_more_conic_files.patch implements a Conic class that uses Denis Simon's code and can find points on conics over number fields and finite fields. It includes most of trac_727-conic.patch and works by itself on 4.4.4. Some doctests fail. It includes an incomplete and incorrect implementation of Hilbert symbols that should be replaced by the Hilbert symbols of #9334",
    "created_at": "2010-07-06T14:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4235",
    "user": "https://github.com/mstreng"
}
```

* this is being revived at Sage Days 23

* trac_727-conic-extcode.patch should be removed: it updates Denis Simon's code from 2005 to 2007, while 2009 is already shipped with the latest Sage

* trac_727_more_conic_files.patch implements a Conic class that uses Denis Simon's code and can find points on conics over number fields and finite fields. It includes most of trac_727-conic.patch and works by itself on 4.4.4. Some doctests fail. It includes an incomplete and incorrect implementation of Hilbert symbols that should be replaced by the Hilbert symbols of #9334



---

archive/issue_comments_004236.json:
```json
{
    "body": "* see http://wiki.sagemath.org/days23/conics\n\n  * I missed the file sage/schemes/plane_conics/__init__.py (which is empty), so the patch in its current form doesn't work",
    "created_at": "2010-07-06T16:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4236",
    "user": "https://github.com/mstreng"
}
```

* see http://wiki.sagemath.org/days23/conics

  * I missed the file sage/schemes/plane_conics/__init__.py (which is empty), so the patch in its current form doesn't work



---

archive/issue_comments_004237.json:
```json
{
    "body": "Attachment [trac_727_more_conic_files2.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files2.patch) by @mstreng created at 2010-07-07 10:15:19\n\napply this patch and the one without \"2\" to get something that almost works",
    "created_at": "2010-07-07T10:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4237",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_more_conic_files2.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files2.patch) by @mstreng created at 2010-07-07 10:15:19

apply this patch and the one without "2" to get something that almost works



---

archive/issue_comments_004238.json:
```json
{
    "body": "Attachment [trac_727_more_conic_files3.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files3.patch) by @mstreng created at 2010-07-08 09:43:41\n\nneeds two previous tickets trac_727_more... and trac_9334-hilbert.patch",
    "created_at": "2010-07-08T09:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4238",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_more_conic_files3.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files3.patch) by @mstreng created at 2010-07-08 09:43:41

needs two previous tickets trac_727_more... and trac_9334-hilbert.patch



---

archive/issue_comments_004239.json:
```json
{
    "body": "apply after trac_727_more_conic_files1,2,3; requires trac_9334-hilbert.patch to work",
    "created_at": "2010-07-12T12:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4239",
    "user": "https://github.com/mstreng"
}
```

apply after trac_727_more_conic_files1,2,3; requires trac_9334-hilbert.patch to work



---

archive/issue_comments_004240.json:
```json
{
    "body": "Attachment [trac_727_more_conic_files4.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files4.patch) by @mstreng created at 2010-07-16 18:58:09\n\napply on sage 4.4.4 after trac_727_more_conic_files1,2,3,4, shouldn't require trac_9334-hilbert.patch",
    "created_at": "2010-07-16T18:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4240",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_more_conic_files4.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files4.patch) by @mstreng created at 2010-07-16 18:58:09

apply on sage 4.4.4 after trac_727_more_conic_files1,2,3,4, shouldn't require trac_9334-hilbert.patch



---

archive/issue_comments_004241.json:
```json
{
    "body": "Attachment [trac_727_more_conic_files5.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files5.patch) by @mstreng created at 2010-07-18 21:41:18\n\napply on sage 4.4.4 after trac_727_more_conic_files1,2,3,4,5",
    "created_at": "2010-07-18T21:41:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4241",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_more_conic_files5.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files5.patch) by @mstreng created at 2010-07-18 21:41:18

apply on sage 4.4.4 after trac_727_more_conic_files1,2,3,4,5



---

archive/issue_comments_004242.json:
```json
{
    "body": "Attachment [trac_727_conic_combined_1-6.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conic_combined_1-6.patch) by @mstreng created at 2010-07-18 21:51:27\n\napply only this latest file",
    "created_at": "2010-07-18T21:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4242",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_conic_combined_1-6.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conic_combined_1-6.patch) by @mstreng created at 2010-07-18 21:51:27

apply only this latest file



---

archive/issue_comments_004243.json:
```json
{
    "body": "Attachment [trac_727_more_conic_files7.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files7.patch) by @mstreng created at 2010-07-20 12:41:49\n\napply the 1-6 patch on sage 4.5.1, then apply this one",
    "created_at": "2010-07-20T12:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4243",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_more_conic_files7.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files7.patch) by @mstreng created at 2010-07-20 12:41:49

apply the 1-6 patch on sage 4.5.1, then apply this one



---

archive/issue_comments_004244.json:
```json
{
    "body": "Attachment [trac_727_more_conic_files9.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files9.patch) by @mstreng created at 2010-07-20 12:42:32\n\napply after 7 (there is no 8)",
    "created_at": "2010-07-20T12:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4244",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_more_conic_files9.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_more_conic_files9.patch) by @mstreng created at 2010-07-20 12:42:32

apply after 7 (there is no 8)



---

archive/issue_comments_004245.json:
```json
{
    "body": "I'm running a doctest right now. I'll fold them when I get the time. Who wants to review it?",
    "created_at": "2010-07-20T12:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4245",
    "user": "https://github.com/mstreng"
}
```

I'm running a doctest right now. I'll fold them when I get the time. Who wants to review it?



---

archive/issue_comments_004246.json:
```json
{
    "body": "apply only this latest file (works on sage 4.4.4 and on 4.5.1)",
    "created_at": "2010-07-20T20:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4246",
    "user": "https://github.com/mstreng"
}
```

apply only this latest file (works on sage 4.4.4 and on 4.5.1)



---

archive/issue_comments_004247.json:
```json
{
    "body": "Attachment [trac_727_conic_combined_1-9.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conic_combined_1-9.patch) by @mstreng created at 2010-07-20 20:42:15\n\n\"All tests passed!\", and I combined the patches into one file",
    "created_at": "2010-07-20T20:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4247",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_conic_combined_1-9.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conic_combined_1-9.patch) by @mstreng created at 2010-07-20 20:42:15

"All tests passed!", and I combined the patches into one file



---

archive/issue_comments_004248.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-20T20:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4248",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004249.json:
```json
{
    "body": "Those `[with patch, needs review]` bits in the description are no longer necessary, thanks to the workflow.",
    "created_at": "2010-07-20T21:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4249",
    "user": "https://github.com/rlmill"
}
```

Those `[with patch, needs review]` bits in the description are no longer necessary, thanks to the workflow.



---

archive/issue_comments_004250.json:
```json
{
    "body": "The patch applies fine to 4.6.alpha0, but not all the tests in the new directory pass:\n\n```\n\tsage -t -long \"devel/sage-main/sage/schemes/plane_conics/con_field.py\"\n\tsage -t -long \"devel/sage-main/sage/schemes/plane_conics/con_number_field.py\"\n\tsage -t -long \"devel/sage-main/sage/schemes/plane_conics/con_rational_field.py\"\n\tsage -t -long \"devel/sage-main/sage/schemes/plane_conics/rnfisnorm.py\"\n```\nI feared that it would be worse after the new Pari upgrade (which is in 4.6.alpha0).  But it does need looking into.",
    "created_at": "2010-09-11T17:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4250",
    "user": "https://github.com/JohnCremona"
}
```

The patch applies fine to 4.6.alpha0, but not all the tests in the new directory pass:

```
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/con_field.py"
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/con_number_field.py"
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/con_rational_field.py"
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/rnfisnorm.py"
```
I feared that it would be worse after the new Pari upgrade (which is in 4.6.alpha0).  But it does need looking into.



---

archive/issue_comments_004251.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-11T17:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4251",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_004252.json:
```json
{
    "body": "It worked just fine on my 4.5.something. I guess the problems are all in \"devel/sage-main/sage/schemes/plane_conics/rnfisnorm.py\", which we can get rid of after #2329 is finished. So let's do #2329 first.",
    "created_at": "2010-11-03T09:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4252",
    "user": "https://github.com/mstreng"
}
```

It worked just fine on my 4.5.something. I guess the problems are all in "devel/sage-main/sage/schemes/plane_conics/rnfisnorm.py", which we can get rid of after #2329 is finished. So let's do #2329 first.



---

archive/issue_comments_004253.json:
```json
{
    "body": "Attachment [trac_727_conics.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conics.patch) by @mstreng created at 2010-12-08 17:28:59\n\nApply trac_727_conics.patch to sage 4.6 after #2329 and #9334",
    "created_at": "2010-12-08T17:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4253",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_conics.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conics.patch) by @mstreng created at 2010-12-08 17:28:59

Apply trac_727_conics.patch to sage 4.6 after #2329 and #9334



---

archive/issue_comments_004254.json:
```json
{
    "body": "Here's a version that uses hilbert symbols and rnfisnorm from resp. #9334 and #2329. This patch provides motivation and testcases for those two other tickets.",
    "created_at": "2010-12-08T17:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4254",
    "user": "https://github.com/mstreng"
}
```

Here's a version that uses hilbert symbols and rnfisnorm from resp. #9334 and #2329. This patch provides motivation and testcases for those two other tickets.



---

archive/issue_comments_004255.json:
```json
{
    "body": "Attachment [trac_727_conics_without_number_fields.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conics_without_number_fields.patch) by @mstreng created at 2011-01-13 14:33:08\n\nApply only this latest file (works on sage 4.6.1.rc0 without any other patches)",
    "created_at": "2011-01-13T14:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4255",
    "user": "https://github.com/mstreng"
}
```

Attachment [trac_727_conics_without_number_fields.patch](tarball://root/attachments/some-uuid/ticket727/trac_727_conics_without_number_fields.patch) by @mstreng created at 2011-01-13 14:33:08

Apply only this latest file (works on sage 4.6.1.rc0 without any other patches)



---

archive/issue_comments_004256.json:
```json
{
    "body": "I moved all number field functionality to #10621. Because of this, no patches from other tickets are needed, you only need to apply trac_727_conics_without_number_fields.patch",
    "created_at": "2011-01-13T14:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4256",
    "user": "https://github.com/mstreng"
}
```

I moved all number field functionality to #10621. Because of this, no patches from other tickets are needed, you only need to apply trac_727_conics_without_number_fields.patch



---

archive/issue_comments_004257.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-13T14:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4257",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004258.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-22T15:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4258",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004259.json:
```json
{
    "body": "This looks really good. It's embarrassing that we've been shipping Denis Simon's scripts with Sage for years but nobody's sat down and written the interface code necessary to make it accessible.\n\nPatch applied fine to 4.6.2.alpha1, all doctests in sage/schemes passed, the ref manual built OK, and all the examples I tried worked.\n\nI have one minor gripe: there are one or two cases where the new Conic classes inherit methods from the generic plane curve classes that perhaps ought to be replaced with more appropriate conic-specific implementations (e.g the method \"rational_points\"). But that can come in future tickets if people feel it's needed.",
    "created_at": "2011-01-22T15:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4259",
    "user": "https://github.com/loefflerd"
}
```

This looks really good. It's embarrassing that we've been shipping Denis Simon's scripts with Sage for years but nobody's sat down and written the interface code necessary to make it accessible.

Patch applied fine to 4.6.2.alpha1, all doctests in sage/schemes passed, the ref manual built OK, and all the examples I tried worked.

I have one minor gripe: there are one or two cases where the new Conic classes inherit methods from the generic plane curve classes that perhaps ought to be replaced with more appropriate conic-specific implementations (e.g the method "rational_points"). But that can come in future tickets if people feel it's needed.



---

archive/issue_events_001968.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-25T08:13:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/727#event-1968"
}
```



---

archive/issue_comments_004260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/727#issuecomment-4260",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
