# Issue 8241: p-adic fields should have Witt Frobenius

archive/issues_008241.json:
```json
{
    "body": "Assignee: @roed314\n\nIf K is an unramified extension of Qp, there should be a function that computes the canonical Witt p-Frobenius:\n\n\n```\nsage: K.<a> = Qp(25)\nsage: a.witt_frobenius()\n???\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8241\n\n",
    "created_at": "2010-02-11T19:54:03Z",
    "labels": [
        "component: padics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "p-adic fields should have Witt Frobenius",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8241",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @roed314

If K is an unramified extension of Qp, there should be a function that computes the canonical Witt p-Frobenius:


```
sage: K.<a> = Qp(25)
sage: a.witt_frobenius()
???
```


Issue created by migration from https://trac.sagemath.org/ticket/8241





---

archive/issue_comments_072730.json:
```json
{
    "body": "(oops the Qp above should be Qq)",
    "created_at": "2010-02-11T19:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72730",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

(oops the Qp above should be Qq)



---

archive/issue_comments_072731.json:
```json
{
    "body": "I called the function `frobenius` rather than `witt_frobenius`.",
    "created_at": "2010-11-22T09:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72731",
    "user": "https://github.com/roed314"
}
```

I called the function `frobenius` rather than `witt_frobenius`.



---

archive/issue_comments_072732.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-22T09:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72732",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072733.json:
```json
{
    "body": "Fixed a small problem revealed by the test-bot.",
    "created_at": "2010-12-03T13:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72733",
    "user": "https://github.com/roed314"
}
```

Fixed a small problem revealed by the test-bot.



---

archive/issue_comments_072734.json:
```json
{
    "body": "For consistency, these methods should also apply to Qp, with Frobenius acting as the identity map. For instance, the following should not raise an exception:\n\n```\nsage: Qp(7)(2).frobenius()\n```\n",
    "created_at": "2011-06-17T15:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72734",
    "user": "https://github.com/kedlaya"
}
```

For consistency, these methods should also apply to Qp, with Frobenius acting as the identity map. For instance, the following should not raise an exception:

```
sage: Qp(7)(2).frobenius()
```




---

archive/issue_comments_072735.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-17T15:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72735",
    "user": "https://github.com/kedlaya"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072736.json:
```json
{
    "body": "There's now a frobenius method for p-adic base rings and fields.",
    "created_at": "2011-06-21T19:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72736",
    "user": "https://github.com/roed314"
}
```

There's now a frobenius method for p-adic base rings and fields.



---

archive/issue_comments_072737.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-21T19:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72737",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072738.json:
```json
{
    "body": "I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.",
    "created_at": "2011-06-22T07:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72738",
    "user": "https://github.com/roed314"
}
```

I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.



---

archive/issue_comments_072739.json:
```json
{
    "body": "Replying to [comment:7 roed]:\n> I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.\n\nSee #10195.",
    "created_at": "2011-08-24T22:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72739",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:7 roed]:
> I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.

See #10195.



---

archive/issue_comments_072740.json:
```json
{
    "body": "Ping. (#11586, which has positive review, depends on this one.)",
    "created_at": "2011-09-16T17:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72740",
    "user": "https://github.com/nexttime"
}
```

Ping. (#11586, which has positive review, depends on this one.)



---

archive/issue_comments_072741.json:
```json
{
    "body": "Attachment [8241.patch](tarball://root/attachments/some-uuid/ticket8241/8241.patch) by @roed314 created at 2012-02-21 12:33:12\n\nAs Sebastian Pancratz noted in his talk, it would be great if someone wrote a better implementation of this.",
    "created_at": "2012-02-21T12:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72741",
    "user": "https://github.com/roed314"
}
```

Attachment [8241.patch](tarball://root/attachments/some-uuid/ticket8241/8241.patch) by @roed314 created at 2012-02-21 12:33:12

As Sebastian Pancratz noted in his talk, it would be great if someone wrote a better implementation of this.



---

archive/issue_comments_072742.json:
```json
{
    "body": "The patchbot finds some Sphinx formatting errors in the docstrings:\n\n\n```\ndocstring of sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.\ndocstring of sage.rings.padics.padic_ZZ_pX_CA_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.\ndocstring of sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.\ndocstring of sage.rings.padics.padic_ZZ_pX_CR_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.\ndocstring of sage.rings.padics.padic_ext_element.pAdicExtElement.frobenius:6: WARNING: Inline interpreted text or phrase reference start-string without end-string.\n```\n\n\nIt's also harping on about trailing whitespace (which is apparently now a Bad Thing, although Sage has been tolerating it cheerfully for years).",
    "created_at": "2012-03-10T17:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72742",
    "user": "https://github.com/loefflerd"
}
```

The patchbot finds some Sphinx formatting errors in the docstrings:


```
docstring of sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.
docstring of sage.rings.padics.padic_ZZ_pX_CA_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.
docstring of sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.
docstring of sage.rings.padics.padic_ZZ_pX_CR_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.
docstring of sage.rings.padics.padic_ext_element.pAdicExtElement.frobenius:6: WARNING: Inline interpreted text or phrase reference start-string without end-string.
```


It's also harping on about trailing whitespace (which is apparently now a Bad Thing, although Sage has been tolerating it cheerfully for years).



---

archive/issue_comments_072743.json:
```json
{
    "body": "Here's a new patch with the docstrings straightened out and trailing whitespace removed. I've also added a doctest to show that an error is raised when \"frobenius\" is called on an element of a ramified extension. I'm happy with the rest of the code, so if David's happy with my changes we can call this that's a positive review.",
    "created_at": "2012-03-12T18:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72743",
    "user": "https://github.com/loefflerd"
}
```

Here's a new patch with the docstrings straightened out and trailing whitespace removed. I've also added a doctest to show that an error is raised when "frobenius" is called on an element of a ramified extension. I'm happy with the rest of the code, so if David's happy with my changes we can call this that's a positive review.



---

archive/issue_comments_072744.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-12T19:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72744",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072745.json:
```json
{
    "body": "Looks good to me.  I've created #12657: write a more efficient implementation of Frobenius.",
    "created_at": "2012-03-12T19:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72745",
    "user": "https://github.com/roed314"
}
```

Looks good to me.  I've created #12657: write a more efficient implementation of Frobenius.



---

archive/issue_comments_072746.json:
```json
{
    "body": "Attachment [trac_8241-frobenius.patch](tarball://root/attachments/some-uuid/ticket8241/trac_8241-frobenius.patch) by @loefflerd created at 2012-03-12 19:47:42\n\nApply only this patch. Patch against 5.0.beta7",
    "created_at": "2012-03-12T19:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72746",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8241-frobenius.patch](tarball://root/attachments/some-uuid/ticket8241/trac_8241-frobenius.patch) by @loefflerd created at 2012-03-12 19:47:42

Apply only this patch. Patch against 5.0.beta7



---

archive/issue_comments_072747.json:
```json
{
    "body": "Patchbot's grumbling about trailing whitespace again, so I removed one single space character and re-uploaded the patch.",
    "created_at": "2012-03-12T19:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72747",
    "user": "https://github.com/loefflerd"
}
```

Patchbot's grumbling about trailing whitespace again, so I removed one single space character and re-uploaded the patch.



---

archive/issue_comments_072748.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-21T22:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72748",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_008442.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-21T22:03:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8241#event-8442"
}
```
