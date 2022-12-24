# Issue 8588: list(SL(2,2)) is inconsistent with SL(2,2).list()

archive/issues_008588.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  sage-combinat\n\nKeywords: Special linear group, TestSuite\n\n\n```\nsage: G = SL(2,2)\nsage: TestSuite(G).run()\nFailure in _test_enumerated_set_iter_list:\nTraceback (most recent call last):\n...\nAssertionError: [1 1]\n[0 1] != [1 0]\n[0 1]\n------------------------------------------------------------\nThe following tests failed: _test_enumerated_set_iter_list\n\nsage: list(G)[2]\n[1 1]\n[0 1]\nsage: G.list()[2]\n[1 0]\n[0 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8588\n\n",
    "created_at": "2010-03-23T16:29:31Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "list(SL(2,2)) is inconsistent with SL(2,2).list()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8588",
    "user": "@nthiery"
}
```
Assignee: @aghitza

CC:  sage-combinat

Keywords: Special linear group, TestSuite


```
sage: G = SL(2,2)
sage: TestSuite(G).run()
Failure in _test_enumerated_set_iter_list:
Traceback (most recent call last):
...
AssertionError: [1 1]
[0 1] != [1 0]
[0 1]
------------------------------------------------------------
The following tests failed: _test_enumerated_set_iter_list

sage: list(G)[2]
[1 1]
[0 1]
sage: G.list()[2]
[1 0]
[0 1]
```


Issue created by migration from https://trac.sagemath.org/ticket/8588





---

archive/issue_comments_077775.json:
```json
{
    "body": "Attachment [trac-8588](tarball://root/attachments/some-uuid/ticket8588/trac-8588) by @itaibn created at 2012-05-30 00:39:37",
    "created_at": "2012-05-30T00:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77775",
    "user": "@itaibn"
}
```

Attachment [trac-8588](tarball://root/attachments/some-uuid/ticket8588/trac-8588) by @itaibn created at 2012-05-30 00:39:37



---

archive/issue_comments_077776.json:
```json
{
    "body": "Just attached a fix.",
    "created_at": "2012-05-30T00:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77776",
    "user": "@itaibn"
}
```

Just attached a fix.



---

archive/issue_comments_077777.json:
```json
{
    "body": "Attachment [trac-8588-2](tarball://root/attachments/some-uuid/ticket8588/trac-8588-2) by @itaibn created at 2012-06-04 22:14:41\n\nFixed a typo and improved the formatting.",
    "created_at": "2012-06-04T22:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77777",
    "user": "@itaibn"
}
```

Attachment [trac-8588-2](tarball://root/attachments/some-uuid/ticket8588/trac-8588-2) by @itaibn created at 2012-06-04 22:14:41

Fixed a typo and improved the formatting.



---

archive/issue_comments_077778.json:
```json
{
    "body": "Are you sure this is a wise fix? This way, even starting to iterate on the elements of a matrix group involves constructing all its elements. The iterator method on matrix groups previously was the one inherited from `sage.combinat.backtrack.TransitiveIdeal.__iter__`, which seems a little more conservative.\n\nIn principle, people can write `iter(SL(next_prime(10^5),2)).next()` to get an example of a determinant 1 matrix. This doesn't need to be expensive (with the current code it is, though. It seems the `semigroup_generators` method is horribly inefficient). With the present patch it's guaranteed to be very expensive.\n\nIterators and lists have different use cases, so why should G.list() and list(G) give the same result? I think structures should be allowed to choose different enumeration methods depending on the application. G.list() knows it returns a list of all elements, so it can concentrate on speed and not worry about storage. list(G), which is just [g for g in G] asks G to produce an iterator over its elements, which can choose an enumeration method that saves memory and/or ensures that it's fast even when only a couple of elements are consumed.\n\nIt seems to me the correct fix is to amend `TestSuite` to not enforce that iter(G.list()) and iter(G) produce the elements in the same order.",
    "created_at": "2012-06-04T23:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77778",
    "user": "@nbruin"
}
```

Are you sure this is a wise fix? This way, even starting to iterate on the elements of a matrix group involves constructing all its elements. The iterator method on matrix groups previously was the one inherited from `sage.combinat.backtrack.TransitiveIdeal.__iter__`, which seems a little more conservative.

In principle, people can write `iter(SL(next_prime(10^5),2)).next()` to get an example of a determinant 1 matrix. This doesn't need to be expensive (with the current code it is, though. It seems the `semigroup_generators` method is horribly inefficient). With the present patch it's guaranteed to be very expensive.

Iterators and lists have different use cases, so why should G.list() and list(G) give the same result? I think structures should be allowed to choose different enumeration methods depending on the application. G.list() knows it returns a list of all elements, so it can concentrate on speed and not worry about storage. list(G), which is just [g for g in G] asks G to produce an iterator over its elements, which can choose an enumeration method that saves memory and/or ensures that it's fast even when only a couple of elements are consumed.

It seems to me the correct fix is to amend `TestSuite` to not enforce that iter(G.list()) and iter(G) produce the elements in the same order.



---

archive/issue_comments_077779.json:
```json
{
    "body": "The reason I this fix is that I assumed that whoever made that test knew what they were doing and had a good reason. I guess I should have checked if such a reason existed. I actually checked and found out that the test was made in #5891, a large patch where such a mistake could've slipped through.",
    "created_at": "2012-06-05T00:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77779",
    "user": "@itaibn"
}
```

The reason I this fix is that I assumed that whoever made that test knew what they were doing and had a good reason. I guess I should have checked if such a reason existed. I actually checked and found out that the test was made in #5891, a large patch where such a mistake could've slipped through.



---

archive/issue_comments_077780.json:
```json
{
    "body": "Attachment [trac-8588-3](tarball://root/attachments/some-uuid/ticket8588/trac-8588-3) by @a-andre created at 2014-08-18 21:50:01\n\nI got\n\n```\nsage: G = SL(2,2)\nsage: TestSuite(G).run()\nsage: list(G)[2]\n[0 1]\n[1 1]\nsage: G.list()[2]\n[0 1]\n[1 1]\n\n```\n",
    "created_at": "2014-08-18T21:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77780",
    "user": "@a-andre"
}
```

Attachment [trac-8588-3](tarball://root/attachments/some-uuid/ticket8588/trac-8588-3) by @a-andre created at 2014-08-18 21:50:01

I got

```
sage: G = SL(2,2)
sage: TestSuite(G).run()
sage: list(G)[2]
[0 1]
[1 1]
sage: G.list()[2]
[0 1]
[1 1]

```




---

archive/issue_comments_077781.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-18T21:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77781",
    "user": "@a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077782.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-10-25T21:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8588#issuecomment-77782",
    "user": "@vbraun"
}
```

Resolution: fixed
