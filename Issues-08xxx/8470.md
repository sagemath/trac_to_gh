# Issue 8470: new documentation categories "FAQ" and "Thematic Tutorials"

archive/issues_008470.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @wdjoyner @rlmill @nathanncohen @rbeezer sage-combinat @dwbump @jhpalmieri @jasongrout\n\nKeywords: FAQ, HOWTO, tutorial\n\nThis is a meta-ticket that helps in organizing changes and additions to the Sage standard documentation. On [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc), it is proposed that we create two new documentation categories called:\n\n* FAQ --- a collection of answers to frequently asked questions.\n* Thematic Tutorials --- a collection of in-depth tutorials on specific topics.\n\nSee [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/e94b8f3dc6f503af) on sage-devel for further discussion about more accessible documentation. For starters, here is a list of tickets with enhancements for those two new documentation categories:\n\n* #8442 Lie Methods and Related Combinatorics\n* #8464 FAQ\n* #8465 Python Functional Programming for Mathematicians\n* #8466 Sage and Coding Theory\n* #8467 Linear Programming in Sage\n* #8468 Group Theory and Sage: A Primer\n* #8469 Number Theory and the RSA Public Key Cryptosystem\n* #8886 tutorial on Python object and classes\n\nOnce all the above tickets are closed, the current ticket can be closed as fixed.\n\n\n\n**Prerequisites:** \n\n1. #8480 stylistic clean-ups on web page of standard documentation\n2. #8468 Group Theory and Sage\n3. #8464 add FAQ to standard documentation\n4. #8533 browse thematic tutorials from command line and within notebook\n5. #8465 Functional Programming for Mathematicians\n6. #8469 Number Theory and the RSA Public Key Cryptosystem\n7. #8442 Lie Methods and Related Combinatorics\n\nIssue created by migration from https://trac.sagemath.org/ticket/8470\n\n",
    "closed_at": "2014-08-29T18:33:49Z",
    "created_at": "2010-03-07T02:38:29Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "new documentation categories \"FAQ\" and \"Thematic Tutorials\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @wdjoyner @rlmill @nathanncohen @rbeezer sage-combinat @dwbump @jhpalmieri @jasongrout

Keywords: FAQ, HOWTO, tutorial

This is a meta-ticket that helps in organizing changes and additions to the Sage standard documentation. On [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc), it is proposed that we create two new documentation categories called:

* FAQ --- a collection of answers to frequently asked questions.
* Thematic Tutorials --- a collection of in-depth tutorials on specific topics.

See [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/e94b8f3dc6f503af) on sage-devel for further discussion about more accessible documentation. For starters, here is a list of tickets with enhancements for those two new documentation categories:

* #8442 Lie Methods and Related Combinatorics
* #8464 FAQ
* #8465 Python Functional Programming for Mathematicians
* #8466 Sage and Coding Theory
* #8467 Linear Programming in Sage
* #8468 Group Theory and Sage: A Primer
* #8469 Number Theory and the RSA Public Key Cryptosystem
* #8886 tutorial on Python object and classes

Once all the above tickets are closed, the current ticket can be closed as fixed.



**Prerequisites:** 

1. #8480 stylistic clean-ups on web page of standard documentation
2. #8468 Group Theory and Sage
3. #8464 add FAQ to standard documentation
4. #8533 browse thematic tutorials from command line and within notebook
5. #8465 Functional Programming for Mathematicians
6. #8469 Number Theory and the RSA Public Key Cryptosystem
7. #8442 Lie Methods and Related Combinatorics

Issue created by migration from https://trac.sagemath.org/ticket/8470





---

archive/issue_comments_076169.json:
```json
{
    "body": "This sounds very good! Should the following appear there as well?\n\n- the category primer (sage.categories.primer)\n- the \"implementing a parent\" tutorial (sage.categories.tutorial); this needs further work!\n\nFor the record, in the Sage-Combinat queue, some work is being done on:\n\n- A tutorial on iterators\n- A tutorial on combinatorics",
    "created_at": "2010-03-08T10:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76169",
    "user": "https://github.com/nthiery"
}
```

This sounds very good! Should the following appear there as well?

- the category primer (sage.categories.primer)
- the "implementing a parent" tutorial (sage.categories.tutorial); this needs further work!

For the record, in the Sage-Combinat queue, some work is being done on:

- A tutorial on iterators
- A tutorial on combinatorics



---

archive/issue_comments_076170.json:
```json
{
    "body": "Changing keywords from \"FAQ, HOWTO\" to \"FAQ, HOWTO, tutorial\".",
    "created_at": "2010-03-09T21:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76170",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing keywords from "FAQ, HOWTO" to "FAQ, HOWTO, tutorial".



---

archive/issue_comments_076171.json:
```json
{
    "body": "Here is a more complete list of patches that are relevant\nto this metaticket:\n\n```\ntrac_8480-clean-up.patch\ntrac_8464-faq-general.patch\ntrac_8464-faq-usage.patch\ntrac_8464-faq-contribute.patch\ntrac_8464-ref.patch\ntrac_8465-functional.patch\ntrac_8469-rsa.patch\ntrac_8468-groups.patch\ntrac_8411_branching_rules.patch\ntrac_8414_weyl_group_space.patch\ntrac_8442-lie-rebased.patch\ntrac_8442-reviewer.patch\ntrac_8492-ref.patch\n```\n\nIn addition three .png files from #8442 need to be copied into \n`doc/en/thematic_tutorials/static`.\n\nWith this preparation, the pdf and html documentation build and look very good.",
    "created_at": "2010-03-15T23:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76171",
    "user": "https://github.com/dwbump"
}
```

Here is a more complete list of patches that are relevant
to this metaticket:

```
trac_8480-clean-up.patch
trac_8464-faq-general.patch
trac_8464-faq-usage.patch
trac_8464-faq-contribute.patch
trac_8464-ref.patch
trac_8465-functional.patch
trac_8469-rsa.patch
trac_8468-groups.patch
trac_8411_branching_rules.patch
trac_8414_weyl_group_space.patch
trac_8442-lie-rebased.patch
trac_8442-reviewer.patch
trac_8492-ref.patch
```

In addition three .png files from #8442 need to be copied into 
`doc/en/thematic_tutorials/static`.

With this preparation, the pdf and html documentation build and look very good.



---

archive/issue_events_020330.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20330"
}
```



---

archive/issue_events_020331.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20331"
}
```



---

archive/issue_events_020332.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20332"
}
```



---

archive/issue_events_020333.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20333"
}
```



---

archive/issue_events_020334.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20334"
}
```



---

archive/issue_events_020335.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20335"
}
```



---

archive/issue_events_020336.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20336"
}
```



---

archive/issue_comments_076172.json:
```json
{
    "body": "All done!",
    "created_at": "2014-08-18T05:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76172",
    "user": "https://github.com/rwst"
}
```

All done!



---

archive/issue_comments_076173.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-18T05:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76173",
    "user": "https://github.com/rwst"
}
```

Changing status from new to needs_review.



---

archive/issue_events_020337.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2014-08-18T05:34:31Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20337"
}
```



---

archive/issue_events_020338.json:
```json
{
    "actor": "https://github.com/rwst",
    "created_at": "2014-08-18T05:34:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20338"
}
```



---

archive/issue_comments_076174.json:
```json
{
    "body": "We certainly need better organization of documentation, but this ticket has achieved its purpose, you are right.  Too bad #8533 isn't finished yet, but oh well.",
    "created_at": "2014-08-27T15:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76174",
    "user": "https://github.com/kcrisman"
}
```

We certainly need better organization of documentation, but this ticket has achieved its purpose, you are right.  Too bad #8533 isn't finished yet, but oh well.



---

archive/issue_comments_076175.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-27T15:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76175",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076176.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-29T18:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8470#issuecomment-76176",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_020339.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-08-29T18:33:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8470",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8470#event-20339"
}
```
