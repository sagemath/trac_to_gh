# Issue 8593: Add Lehmer code of Permutation as an infinite enumerated set

archive/issues_008593.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat\n\nKeywords: code, permutation\n\nThe goal of this ticket is to implement Lehmer_codes as a parent (InfiniteEnumeratedSets()). One of the goal is to use this features to index Schubert evaluation points and Schubert polynomials.\n\nThere is also an iterator over all codes, and two methods for elements\nis_dominant() (easy Schubert) and is_anti_dominant() (symmetric Schubert).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8593\n\n",
    "created_at": "2010-03-23T23:37:58Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add Lehmer code of Permutation as an infinite enumerated set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8593",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```
Assignee: nborie

CC:  sage-combinat

Keywords: code, permutation

The goal of this ticket is to implement Lehmer_codes as a parent (InfiniteEnumeratedSets()). One of the goal is to use this features to index Schubert evaluation points and Schubert polynomials.

There is also an iterator over all codes, and two methods for elements
is_dominant() (easy Schubert) and is_anti_dominant() (symmetric Schubert).

Issue created by migration from https://trac.sagemath.org/ticket/8593





---

archive/issue_comments_077693.json:
```json
{
    "body": "Attachment [trac_8593_lehmer_code_schubert_step_2-nb.patch](tarball://root/attachments/some-uuid/ticket8593/trac_8593_lehmer_code_schubert_step_2-nb.patch) by nborie created at 2010-03-23 23:49:44",
    "created_at": "2010-03-23T23:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8593#issuecomment-77693",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [trac_8593_lehmer_code_schubert_step_2-nb.patch](tarball://root/attachments/some-uuid/ticket8593/trac_8593_lehmer_code_schubert_step_2-nb.patch) by nborie created at 2010-03-23 23:49:44



---

archive/issue_comments_077694.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-23T23:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8593#issuecomment-77694",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077695.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-24T20:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8593#issuecomment-77695",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077696.json:
```json
{
    "body": "Hi Nicolas,\n\nOne quick remark. Since they are many different interesting code for permutations. I'd rather call this file permutations codes and maybe make an abstract class for those. For all the other code, the bijection is different. If you are interested you can have a look at\n\n    Multivariate generalizations of the Foata-Schutzenberger equidistribition (with F. Hivert  and J.-C. Novelli), in  Fourth Colloquium on Mathematics and Computer Science: Algorithms, Trees, Combinatorics and Probabilities, DMTCS Proceedings, 2006",
    "created_at": "2010-04-10T09:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8593#issuecomment-77696",
    "user": "https://github.com/hivert"
}
```

Hi Nicolas,

One quick remark. Since they are many different interesting code for permutations. I'd rather call this file permutations codes and maybe make an abstract class for those. For all the other code, the bijection is different. If you are interested you can have a look at

    Multivariate generalizations of the Foata-Schutzenberger equidistribition (with F. Hivert  and J.-C. Novelli), in  Fourth Colloquium on Mathematics and Computer Science: Algorithms, Trees, Combinatorics and Probabilities, DMTCS Proceedings, 2006



---

archive/issue_events_020762.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8593#event-20762"
}
```



---

archive/issue_events_020763.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8593#event-20763"
}
```



---

archive/issue_events_020764.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8593#event-20764"
}
```



---

archive/issue_events_020765.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8593#event-20765"
}
```



---

archive/issue_events_020766.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8593#event-20766"
}
```



---

archive/issue_events_020767.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8593#event-20767"
}
```



---

archive/issue_events_020768.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8593",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8593#event-20768"
}
```
