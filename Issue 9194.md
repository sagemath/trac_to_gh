# Issue 9194: Expose and extend the thematic tutorial on symmetric functions

archive/issues_009194.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: symmetric functions\n\nSage needs a good thematic tutorial on symmetric functions. An embryo is in sage.combinat.sf.symmetric_functions, but it's quite indigent (I wrote it, and take the blame):\n\n- Reference it from doc/en/reference/combinat/symmetric_functions.rst and highlight it as the *main* entry point for symmetric functions\n- Make sure `sage.combinat.sf?` points to this tutorial\n- Extend it! (for general use, but also for kschur and the like)\n\nReferences:\n\n- [MuPAD-Combinat's tutorial on Symmetric functions](http://mupad-combinat.sourceforge.net/doc/en/index/guidedTour-predefinedCombinatorialAlgebras.html#index-guidedTour-symmetricFunctions) ([Sources](http://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/DOC/guidedTour-predefinedCombinatorialAlgebras.mupdoc))\n\n- [Francois's advanced tutorial for MuPAD-Combinat](http://mupad-combinat.sourceforge.net/Papers/TutorialSymFcts.pdf)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9194\n\n",
    "created_at": "2010-06-09T07:52:41Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Expose and extend the thematic tutorial on symmetric functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9194",
    "user": "https://github.com/nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: symmetric functions

Sage needs a good thematic tutorial on symmetric functions. An embryo is in sage.combinat.sf.symmetric_functions, but it's quite indigent (I wrote it, and take the blame):

- Reference it from doc/en/reference/combinat/symmetric_functions.rst and highlight it as the *main* entry point for symmetric functions
- Make sure `sage.combinat.sf?` points to this tutorial
- Extend it! (for general use, but also for kschur and the like)

References:

- [MuPAD-Combinat's tutorial on Symmetric functions](http://mupad-combinat.sourceforge.net/doc/en/index/guidedTour-predefinedCombinatorialAlgebras.html#index-guidedTour-symmetricFunctions) ([Sources](http://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/DOC/guidedTour-predefinedCombinatorialAlgebras.mupdoc))

- [Francois's advanced tutorial for MuPAD-Combinat](http://mupad-combinat.sourceforge.net/Papers/TutorialSymFcts.pdf)


Issue created by migration from https://trac.sagemath.org/ticket/9194





---

archive/issue_comments_085883.json:
```json
{
    "body": "I've put a first version on the sage-combinat queue.  It can be built with `sage -docbuild thematic_tutorials html`.  Currently no effort has been made to coordinate with #8533, which will have to be done eventually.  I will continue to work on this, but suggestions and advice are welcome here.",
    "created_at": "2010-06-28T15:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9194#issuecomment-85883",
    "user": "https://github.com/jbandlow"
}
```

I've put a first version on the sage-combinat queue.  It can be built with `sage -docbuild thematic_tutorials html`.  Currently no effort has been made to coordinate with #8533, which will have to be done eventually.  I will continue to work on this, but suggestions and advice are welcome here.



---

archive/issue_comments_085884.json:
```json
{
    "body": "This ticket can be closed as soon as #14900 is merged. #5457 took care of providing a nice tutorial, and #14090 exposes it nicely in the thematic tutorials.",
    "created_at": "2013-02-09T23:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9194#issuecomment-85884",
    "user": "https://github.com/nthiery"
}
```

This ticket can be closed as soon as #14900 is merged. #5457 took care of providing a nice tutorial, and #14090 exposes it nicely in the thematic tutorials.



---

archive/issue_comments_085885.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-09T23:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9194#issuecomment-85885",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085886.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-09T23:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9194#issuecomment-85886",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085887.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-03-06T13:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9194#issuecomment-85887",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
