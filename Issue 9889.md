# Issue 9889: A proper random_element() method for PerfectMatchings

archive/issues_009889.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @nthiery fhivert\n\nAt the moment, the method `random_element()` from PerfectMatchings computes a random matching by picking a random integer between 0 and the number of matchings on n elements, then (I presume) enumerating all the matchings according to some ordering until the `k`th has been computed. This is impressively useless.\n\n\n```\nsage: %timeit PerfectMatchings(12).random_element()\n5 loops, best of 3: 1.5 s per loop\n```\n\n\nBy the way, I was not able to write a method to obtain the list of pairs describing the matching from an PerfectMatching object.. I don't understand how this class is written, and I have no idea why it needs to be so complicated (but it would be nice to add it to this ticket during the review, if someone gets how it works).\n\nThe method random_element (and also an_element) both raise an exception when the set of elements is EMPTY. I also fixed the doctests.\n\n(I don't even get why you can build a PerfectMatchings class on an odd number of elements in the first place)\n\nI expect this ticket could be heavily modified during review, but there is a problem with these classes at the moment.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9890\n\n",
    "created_at": "2010-09-10T15:44:15Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.10",
    "title": "A proper random_element() method for PerfectMatchings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9889",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: sage-combinat

CC:  @nthiery fhivert

At the moment, the method `random_element()` from PerfectMatchings computes a random matching by picking a random integer between 0 and the number of matchings on n elements, then (I presume) enumerating all the matchings according to some ordering until the `k`th has been computed. This is impressively useless.


```
sage: %timeit PerfectMatchings(12).random_element()
5 loops, best of 3: 1.5 s per loop
```


By the way, I was not able to write a method to obtain the list of pairs describing the matching from an PerfectMatching object.. I don't understand how this class is written, and I have no idea why it needs to be so complicated (but it would be nice to add it to this ticket during the review, if someone gets how it works).

The method random_element (and also an_element) both raise an exception when the set of elements is EMPTY. I also fixed the doctests.

(I don't even get why you can build a PerfectMatchings class on an odd number of elements in the first place)

I expect this ticket could be heavily modified during review, but there is a problem with these classes at the moment.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9890





---

archive/issue_comments_097858.json:
```json
{
    "body": "I forgot to click on `needs_review` three years ago `T_T`\n\nNathann",
    "created_at": "2013-03-23T11:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97858",
    "user": "https://github.com/nathanncohen"
}
```

I forgot to click on `needs_review` three years ago `T_T`

Nathann



---

archive/issue_comments_097859.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-23T11:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97859",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097860.json:
```json
{
    "body": "Patch updated ! On the way, I also fixed this \"small problem\" :\n\n\n```\nsage: PerfectMatchings(3).an_element()\n[(1, 2)]\n```\n\n\nNathann",
    "created_at": "2013-03-23T11:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97860",
    "user": "https://github.com/nathanncohen"
}
```

Patch updated ! On the way, I also fixed this "small problem" :


```
sage: PerfectMatchings(3).an_element()
[(1, 2)]
```


Nathann



---

archive/issue_comments_097861.json:
```json
{
    "body": "Attachment [trac_9890.patch](tarball://root/attachments/some-uuid/ticket9890/trac_9890.patch) by @nathanncohen created at 2013-03-23 11:34:13",
    "created_at": "2013-03-23T11:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97861",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9890.patch](tarball://root/attachments/some-uuid/ticket9890/trac_9890.patch) by @nathanncohen created at 2013-03-23 11:34:13



---

archive/issue_comments_097862.json:
```json
{
    "body": "hello,\n\nlooks good to me.\n\nI have taken the opportunity to make a complete cosmetic clean-up of the file (using pep8 and pyflakes)\n\nif my review patch is ok for you, you can set a positive review",
    "created_at": "2013-05-17T19:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97862",
    "user": "https://github.com/fchapoton"
}
```

hello,

looks good to me.

I have taken the opportunity to make a complete cosmetic clean-up of the file (using pep8 and pyflakes)

if my review patch is ok for you, you can set a positive review



---

archive/issue_comments_097863.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-18T10:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97863",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097864.json:
```json
{
    "body": "Attachment [trac_9890_review.patch](tarball://root/attachments/some-uuid/ticket9890/trac_9890_review.patch) by @nathanncohen created at 2013-05-18 10:14:47\n\n> I have taken the opportunity to make a complete cosmetic clean-up of the file (using pep8 and pyflakes)\n> \n> if my review patch is ok for you, you can set a positive review\n\nOkayyyyyyy ! Good to go, then `:-)`\n\nBy the way, how do you use pep8 and pyflakes ? Do you run them externally on files or do you have a way to use them ?\n\nNathann",
    "created_at": "2013-05-18T10:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97864",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9890_review.patch](tarball://root/attachments/some-uuid/ticket9890/trac_9890_review.patch) by @nathanncohen created at 2013-05-18 10:14:47

> I have taken the opportunity to make a complete cosmetic clean-up of the file (using pep8 and pyflakes)
> 
> if my review patch is ok for you, you can set a positive review

Okayyyyyyy ! Good to go, then `:-)`

By the way, how do you use pep8 and pyflakes ? Do you run them externally on files or do you have a way to use them ?

Nathann



---

archive/issue_comments_097865.json:
```json
{
    "body": "Yes, I just run them on the *.py files. Pyflakes is more important, as it finds missing imports and unused variables. Pep8 is much more for the cosmetic, but can check that raise statements are in python3 syntax and find other deprecated syntax.",
    "created_at": "2013-05-18T18:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97865",
    "user": "https://github.com/fchapoton"
}
```

Yes, I just run them on the *.py files. Pyflakes is more important, as it finds missing imports and unused variables. Pep8 is much more for the cosmetic, but can check that raise statements are in python3 syntax and find other deprecated syntax.



---

archive/issue_comments_097866.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-05-22T08:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9889#issuecomment-97866",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_010014.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-22T08:18:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9889",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9889#event-10014"
}
```
