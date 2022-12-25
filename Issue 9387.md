# Issue 9387: Add method for elliptic curves over number fields

archive/issues_009387.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: elliptic curve, tamagawa number\n\nElliptic curves over the rationals have a method that returns a list of tamagawa numbers for the curve.  There is no such method in the case of number fields.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9387\n\n",
    "created_at": "2010-06-29T23:32:43Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Add method for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9387",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @JohnCremona

Keywords: elliptic curve, tamagawa number

Elliptic curves over the rationals have a method that returns a list of tamagawa numbers for the curve.  There is no such method in the case of number fields.


Issue created by migration from https://trac.sagemath.org/ticket/9387





---

archive/issue_comments_089197.json:
```json
{
    "body": "Added patch with the method tamagawa_numbers(), essentially a duplication of the code for the rational case.",
    "created_at": "2010-06-29T23:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89197",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Added patch with the method tamagawa_numbers(), essentially a duplication of the code for the rational case.



---

archive/issue_comments_089198.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T23:39:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89198",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089199.json:
```json
{
    "body": "Updated the patch with a corrected doctest (run and passed).",
    "created_at": "2010-06-29T23:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89199",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Updated the patch with a corrected doctest (run and passed).



---

archive/issue_comments_089200.json:
```json
{
    "body": "Just a suggestion: why duplicate the code? Since `EllipticCurve_rational_field` inherits from `EllipticCurve_number_field`, you could just *move* the code. Then we don't have the overhead of maintaining two routines doing exactly the same, and the likelihood of bugs is halved. Compare John's regulator patch at #9372.",
    "created_at": "2010-06-30T08:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89200",
    "user": "https://github.com/loefflerd"
}
```

Just a suggestion: why duplicate the code? Since `EllipticCurve_rational_field` inherits from `EllipticCurve_number_field`, you could just *move* the code. Then we don't have the overhead of maintaining two routines doing exactly the same, and the likelihood of bugs is halved. Compare John's regulator patch at #9372.



---

archive/issue_comments_089201.json:
```json
{
    "body": "That's a good idea.  Justin, all that's needed is (a) delete the version in ell_rational_field, (b) make sure that the code in ell_number_field works over Q (say by moving the old doctest into the new function -- it should have examples over Q and over another field.\n\nThere might be other functions like this.  If you notice any, make a ticket!",
    "created_at": "2010-06-30T11:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89201",
    "user": "https://github.com/JohnCremona"
}
```

That's a good idea.  Justin, all that's needed is (a) delete the version in ell_rational_field, (b) make sure that the code in ell_number_field works over Q (say by moving the old doctest into the new function -- it should have examples over Q and over another field.

There might be other functions like this.  If you notice any, make a ticket!



---

archive/issue_comments_089202.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-30T11:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89202",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089203.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-30T22:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89203",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089204.json:
```json
{
    "body": "\n```\nsage -t  ell_number_field.py\n**********************************************************************\nFile \"/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py\", line 1049:\n    sage: K=NumberField(x^2+3)\nException raised:\n    Traceback (most recent call last):\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_22[5]>\", line 1, in <module>\n        K=NumberField(x**Integer(2)+Integer(3))###line 1049:\n    sage: K=NumberField(x^2+3)\n      File \"/storage/masiao/sage-4.5.alpha1/local/lib/python/site-packages/sage/rings/number_field/number_field.py\", line 431, in NumberField\n        raise TypeError, \"You must specify the name of the generator.\"\n    TypeError: You must specify the name of the generator.\n**********************************************************************                           \n```\n\n\nYou should also probably delete, rather than comment out, the code in ell_rational_field.",
    "created_at": "2010-07-02T20:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89204",
    "user": "https://github.com/loefflerd"
}
```


```
sage -t  ell_number_field.py
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py", line 1049:
    sage: K=NumberField(x^2+3)
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[5]>", line 1, in <module>
        K=NumberField(x**Integer(2)+Integer(3))###line 1049:
    sage: K=NumberField(x^2+3)
      File "/storage/masiao/sage-4.5.alpha1/local/lib/python/site-packages/sage/rings/number_field/number_field.py", line 431, in NumberField
        raise TypeError, "You must specify the name of the generator."
    TypeError: You must specify the name of the generator.
**********************************************************************                           
```


You should also probably delete, rather than comment out, the code in ell_rational_field.



---

archive/issue_comments_089205.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-02T20:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89205",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089206.json:
```json
{
    "body": "OK, that's weird.  Turns out I popped when I should have pushed, so I was testing unmodified code.  I'll be back.",
    "created_at": "2010-07-02T22:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89206",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

OK, that's weird.  Turns out I popped when I should have pushed, so I was testing unmodified code.  I'll be back.



---

archive/issue_comments_089207.json:
```json
{
    "body": "Attachment [9387.patch](tarball://root/attachments/some-uuid/ticket9387/9387.patch) by justin created at 2010-07-02 23:15:09\n\nNew version of patch following DavidL's suggestion",
    "created_at": "2010-07-02T23:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89207",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Attachment [9387.patch](tarball://root/attachments/some-uuid/ticket9387/9387.patch) by justin created at 2010-07-02 23:15:09

New version of patch following DavidL's suggestion



---

archive/issue_comments_089208.json:
```json
{
    "body": "New patch, replacing previous one.  This time, with some luck, I verified the patch against both 4.4.4 and 4.5.a1.\n\nComments, brickbats, scotch all welcome.",
    "created_at": "2010-07-02T23:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89208",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

New patch, replacing previous one.  This time, with some luck, I verified the patch against both 4.4.4 and 4.5.a1.

Comments, brickbats, scotch all welcome.



---

archive/issue_comments_089209.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T23:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89209",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089210.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-03T08:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89210",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089211.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-07-03T08:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89211",
    "user": "https://github.com/loefflerd"
}
```

Looks good to me.



---

archive/issue_events_023164.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T07:17:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9387#event-23164"
}
```



---

archive/issue_comments_089212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9387#issuecomment-89212",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
