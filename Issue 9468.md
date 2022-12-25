# Issue 9468: Extend ClasscallMetaclass to allow for membership testing

archive/issues_009468.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  sage-combinat\n\nFrom the doc:\n\n```\n        Let ``cls`` be a class in :class:`ClasscallMetaclass`, and consider\n        a call of the form:\n\n            ``x in cls``\n\n        If ``cls`` defines a method ``__classcontains__``, then this\n        results in a call to::\n\n         - ``cls.__classcontains__(cls, x)``\n\n        EXAMPLES:\n\n        We construct a class which implements membership testing, and\n        which contains ``1`` and no other x::\n\n            sage: from sage.misc.classcall_metaclass import ClasscallMetaclass\n            sage: class Foo(object):\n            ...       __metaclass__ = ClasscallMetaclass\n            ...       @staticmethod\n            ...       def __classcontains__(cls, x):\n            ...           return x == 1\n            sage: 1 in Foo\n            True\n            sage: 2 in Foo\n            False\n```\n\n\nThis patch also fixes some typos and such in the documentation of ClassCallMetaclass\n\nIssue created by migration from https://trac.sagemath.org/ticket/9468\n\n",
    "created_at": "2010-07-10T02:38:16Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Extend ClasscallMetaclass to allow for membership testing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9468",
    "user": "https://github.com/nthiery"
}
```
Assignee: @jasongrout

CC:  sage-combinat

From the doc:

```
        Let ``cls`` be a class in :class:`ClasscallMetaclass`, and consider
        a call of the form:

            ``x in cls``

        If ``cls`` defines a method ``__classcontains__``, then this
        results in a call to::

         - ``cls.__classcontains__(cls, x)``

        EXAMPLES:

        We construct a class which implements membership testing, and
        which contains ``1`` and no other x::

            sage: from sage.misc.classcall_metaclass import ClasscallMetaclass
            sage: class Foo(object):
            ...       __metaclass__ = ClasscallMetaclass
            ...       @staticmethod
            ...       def __classcontains__(cls, x):
            ...           return x == 1
            sage: 1 in Foo
            True
            sage: 2 in Foo
            False
```


This patch also fixes some typos and such in the documentation of ClassCallMetaclass

Issue created by migration from https://trac.sagemath.org/ticket/9468





---

archive/issue_comments_090665.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-10T03:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9468#issuecomment-90665",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090666.json:
```json
{
    "body": "Florent: the documentation should really include the __*__ methods. Here, this makes the link for __get__ wrongly point to the corresponding Python doc (with the intersphinx option).",
    "created_at": "2010-07-10T03:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9468#issuecomment-90666",
    "user": "https://github.com/nthiery"
}
```

Florent: the documentation should really include the __*__ methods. Here, this makes the link for __get__ wrongly point to the corresponding Python doc (with the intersphinx option).



---

archive/issue_comments_090667.json:
```json
{
    "body": "Replying to [comment:2 nthiery]:\n\nI just pushed on sage-combinat a trivial doc-fix patch. Otherwise it is ready to go.",
    "created_at": "2011-04-22T22:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9468#issuecomment-90667",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:2 nthiery]:

I just pushed on sage-combinat a trivial doc-fix patch. Otherwise it is ready to go.



---

archive/issue_comments_090668.json:
```json
{
    "body": "Final version including review patch by Florent",
    "created_at": "2011-04-23T01:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9468#issuecomment-90668",
    "user": "https://github.com/nthiery"
}
```

Final version including review patch by Florent



---

archive/issue_comments_090669.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-23T01:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9468#issuecomment-90669",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090670.json:
```json
{
    "body": "Attachment [trac_9468-classcallmetaclass-classcontains-nt.patch](tarball://root/attachments/some-uuid/ticket9468/trac_9468-classcallmetaclass-classcontains-nt.patch) by @nthiery created at 2011-04-23 01:47:27\n\nChecked, folded, posted. Thanks!",
    "created_at": "2011-04-23T01:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9468#issuecomment-90670",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_9468-classcallmetaclass-classcontains-nt.patch](tarball://root/attachments/some-uuid/ticket9468/trac_9468-classcallmetaclass-classcontains-nt.patch) by @nthiery created at 2011-04-23 01:47:27

Checked, folded, posted. Thanks!



---

archive/issue_comments_090671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-08T07:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9468#issuecomment-90671",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
