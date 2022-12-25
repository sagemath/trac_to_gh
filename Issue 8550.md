# Issue 8550: Infinite matrix groups over QQ fail for is_finite()

archive/issues_008550.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @videlec\n\n\n```\nsage: H=SL(2,QQ)\nsage: H.is_finite()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/sage/dev/<ipython console> in <module>()\n\n/sage/dev/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in is_finite(self)\n    343         if self.base_ring().is_finite():\n    344             return True\n--> 345         return self._gap_().IsFinite().bool()\n    346\n    347     def cardinality(self):\n\n/sage/dev/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in _gap_(self, G)\n    217             return SageObject._gap_(self, G)\n    218         except TypeError:\n--> 219             raise NotImplementedError, \"Matrix group over %s not implemented.\"%self.__R\n    220\n    221     def __cmp__(self, H):\n\nNotImplementedError: Matrix group over Rational Field not implemented.\n```\n\n\nGL fails similarly.  Other rings (ZZ, finite fields) seem to work OK, so perhaps this is restricted to something peculiar to the rationals?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8550\n\n",
    "created_at": "2010-03-17T05:17:38Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "Infinite matrix groups over QQ fail for is_finite()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8550",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @aghitza

CC:  @videlec


```
sage: H=SL(2,QQ)
sage: H.is_finite()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/sage/dev/<ipython console> in <module>()

/sage/dev/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in is_finite(self)
    343         if self.base_ring().is_finite():
    344             return True
--> 345         return self._gap_().IsFinite().bool()
    346
    347     def cardinality(self):

/sage/dev/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in _gap_(self, G)
    217             return SageObject._gap_(self, G)
    218         except TypeError:
--> 219             raise NotImplementedError, "Matrix group over %s not implemented."%self.__R
    220
    221     def __cmp__(self, H):

NotImplementedError: Matrix group over Rational Field not implemented.
```


GL fails similarly.  Other rings (ZZ, finite fields) seem to work OK, so perhaps this is restricted to something peculiar to the rationals?

Issue created by migration from https://trac.sagemath.org/ticket/8550





---

archive/issue_comments_077192.json:
```json
{
    "body": "From the Gap manual, I get the impression that Gap won't allow you to construct a group unless it is finitely generated (and it knows how to calculate a set of generators). That's why Gap will allow you to work with GL(2, ZZ) but not GL(2, QQ).",
    "created_at": "2010-09-23T14:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77192",
    "user": "https://github.com/loefflerd"
}
```

From the Gap manual, I get the impression that Gap won't allow you to construct a group unless it is finitely generated (and it knows how to calculate a set of generators). That's why Gap will allow you to work with GL(2, ZZ) but not GL(2, QQ).



---

archive/issue_comments_077193.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-11-30T14:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77193",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_077194.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-11-30T14:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77194",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077195.json:
```json
{
    "body": "green bot, please review",
    "created_at": "2017-11-30T21:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77195",
    "user": "https://github.com/fchapoton"
}
```

green bot, please review



---

archive/issue_comments_077196.json:
```json
{
    "body": "LGTM.",
    "created_at": "2017-11-30T23:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77196",
    "user": "https://github.com/tscrim"
}
```

LGTM.



---

archive/issue_comments_077197.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-11-30T23:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77197",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077198.json:
```json
{
    "body": "thanks",
    "created_at": "2017-12-01T07:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77198",
    "user": "https://github.com/fchapoton"
}
```

thanks



---

archive/issue_comments_077199.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-12-14T12:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8550#issuecomment-77199",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
