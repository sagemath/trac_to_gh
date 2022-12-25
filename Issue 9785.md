# Issue 9785: Subsets(list, submultiset=True): wrong output

archive/issues_009785.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  @hivert brunellus @jasongrout\n\nKeywords: multiset\n\n```\nsage: S = Subsets(['a','a','b','b'], 2, submultiset=True); S.list()\n[['a', 'a'], ['a', 'b'], ['b', 'b']]\nsage: S = Subsets(['a','b','a','b'], 2, submultiset=True); S.list()\n[['a', 'a'], ['a', 'a'], ['a', 'a']]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9786\n\n",
    "created_at": "2010-08-23T12:57:41Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "Subsets(list, submultiset=True): wrong output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9785",
    "user": "https://github.com/mezzarobba"
}
```
Assignee: sage-combinat

CC:  @hivert brunellus @jasongrout

Keywords: multiset

```
sage: S = Subsets(['a','a','b','b'], 2, submultiset=True); S.list()
[['a', 'a'], ['a', 'b'], ['b', 'b']]
sage: S = Subsets(['a','b','a','b'], 2, submultiset=True); S.list()
[['a', 'a'], ['a', 'a'], ['a', 'a']]
```

Issue created by migration from https://trac.sagemath.org/ticket/9786





---

archive/issue_comments_095887.json:
```json
{
    "body": "I think the problem is that the _indices list was created before input sorting, so after the sort its elements pointed to the wrong locations. For example in the case [\"a\", \"b\", \"a\", \"b\"] indices looked like [0, 1] what corresponds to the original data (0->a, 1->b), but after the sort the content of _s was [\"a\", \"a\", \"b\", \"b\"], so 0 and 1 both pointed to \"a\".",
    "created_at": "2011-12-12T20:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9785#issuecomment-95887",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

I think the problem is that the _indices list was created before input sorting, so after the sort its elements pointed to the wrong locations. For example in the case ["a", "b", "a", "b"] indices looked like [0, 1] what corresponds to the original data (0->a, 1->b), but after the sort the content of _s was ["a", "a", "b", "b"], so 0 and 1 both pointed to "a".



---

archive/issue_comments_095888.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-12T20:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9785#issuecomment-95888",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095889.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-18T13:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9785#issuecomment-95889",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095890.json:
```json
{
    "body": "Attachment [trac_9786_submultiset_fix.patch](tarball://root/attachments/some-uuid/ticket9786/trac_9786_submultiset_fix.patch) by @mwhansen created at 2011-12-18 13:26:47\n\nLooks good to me.",
    "created_at": "2011-12-18T13:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9785#issuecomment-95890",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_9786_submultiset_fix.patch](tarball://root/attachments/some-uuid/ticket9786/trac_9786_submultiset_fix.patch) by @mwhansen created at 2011-12-18 13:26:47

Looks good to me.



---

archive/issue_comments_095891.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-22T13:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9785#issuecomment-95891",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_024529.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-22T13:06:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9785",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9785#event-24529"
}
```
