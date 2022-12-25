# Issue 6832: [with patch, positive review] bug in inverse_mod for number field elements

archive/issues_006832.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @JohnCremona\n\nKeywords: number fields\n\nIn the documentation for inverse_mod for (integral) elements of a number field says that the input may be \"an ideal, or an element or list of elements generating a nonzero ideal\" which is not true right now.\n\n```\nsage: k.<a> = NumberField(x^2 + 23)\nsage: d = a + 3\nsage: d.inverse_mod(a)\nTraceback (most recent call last)\n...\nAttributeError: ...\n```\n\nI fixed that and added an example in the doctest (patch based on 4.1.1) \n\nIssue created by migration from https://trac.sagemath.org/ticket/6832\n\n",
    "closed_at": "2009-09-23T04:08:35Z",
    "created_at": "2009-08-27T12:50:26Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] bug in inverse_mod for number field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6832",
    "user": "https://trac.sagemath.org/admin/accounts/users/mtaranes"
}
```
Assignee: somebody

CC:  @JohnCremona

Keywords: number fields

In the documentation for inverse_mod for (integral) elements of a number field says that the input may be "an ideal, or an element or list of elements generating a nonzero ideal" which is not true right now.

```
sage: k.<a> = NumberField(x^2 + 23)
sage: d = a + 3
sage: d.inverse_mod(a)
Traceback (most recent call last)
...
AttributeError: ...
```

I fixed that and added an example in the doctest (patch based on 4.1.1) 

Issue created by migration from https://trac.sagemath.org/ticket/6832





---

archive/issue_comments_056245.json:
```json
{
    "body": "Attachment [inverse_mod.patch](tarball://root/attachments/some-uuid/ticket6832/inverse_mod.patch) by mtaranes created at 2009-08-27 12:50:42",
    "created_at": "2009-08-27T12:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6832#issuecomment-56245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mtaranes"
}
```

Attachment [inverse_mod.patch](tarball://root/attachments/some-uuid/ticket6832/inverse_mod.patch) by mtaranes created at 2009-08-27 12:50:42



---

archive/issue_events_016083.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-23T04:08:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6832",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6832#event-16083"
}
```



---

archive/issue_comments_056246.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T04:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6832#issuecomment-56246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056247.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6832#issuecomment-56247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
