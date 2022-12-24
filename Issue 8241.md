# Issue 8241: p-adic fields should have Witt Frobenius

archive/issues_008241.json:
```json
{
    "body": "Assignee: @roed314\n\nIf K is an unramified extension of Qp, there should be a function that computes the canonical Witt p-Frobenius:\n\n\n```\nsage: K.<a> = Qp(25)\nsage: a.witt_frobenius()\n???\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8241\n\n",
    "created_at": "2010-02-11T19:54:03Z",
    "labels": [
        "padics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "p-adic fields should have Witt Frobenius",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8241",
    "user": "dmharvey"
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

archive/issue_comments_072852.json:
```json
{
    "body": "(oops the Qp above should be Qq)",
    "created_at": "2010-02-11T19:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72852",
    "user": "dmharvey"
}
```

(oops the Qp above should be Qq)



---

archive/issue_comments_072853.json:
```json
{
    "body": "I called the function `frobenius` rather than `witt_frobenius`.",
    "created_at": "2010-11-22T09:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72853",
    "user": "@roed314"
}
```

I called the function `frobenius` rather than `witt_frobenius`.



---

archive/issue_comments_072854.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-22T09:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72854",
    "user": "@roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072855.json:
```json
{
    "body": "Fixed a small problem revealed by the test-bot.",
    "created_at": "2010-12-03T13:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72855",
    "user": "@roed314"
}
```

Fixed a small problem revealed by the test-bot.



---

archive/issue_comments_072856.json:
```json
{
    "body": "For consistency, these methods should also apply to Qp, with Frobenius acting as the identity map. For instance, the following should not raise an exception:\n\n```\nsage: Qp(7)(2).frobenius()\n```\n",
    "created_at": "2011-06-17T15:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72856",
    "user": "@kedlaya"
}
```

For consistency, these methods should also apply to Qp, with Frobenius acting as the identity map. For instance, the following should not raise an exception:

```
sage: Qp(7)(2).frobenius()
```




---

archive/issue_comments_072857.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-17T15:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72857",
    "user": "@kedlaya"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072858.json:
```json
{
    "body": "There's now a frobenius method for p-adic base rings and fields.",
    "created_at": "2011-06-21T19:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72858",
    "user": "@roed314"
}
```

There's now a frobenius method for p-adic base rings and fields.



---

archive/issue_comments_072859.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-21T19:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72859",
    "user": "@roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072860.json:
```json
{
    "body": "I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.",
    "created_at": "2011-06-22T07:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72860",
    "user": "@roed314"
}
```

I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.



---

archive/issue_comments_072861.json:
```json
{
    "body": "Replying to [comment:7 roed]:\n> I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.\n\nSee #10195.",
    "created_at": "2011-08-24T22:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72861",
    "user": "@jdemeyer"
}
```

Replying to [comment:7 roed]:
> I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.

See #10195.



---

archive/issue_comments_072862.json:
```json
{
    "body": "Ping. (#11586, which has positive review, depends on this one.)",
    "created_at": "2011-09-16T17:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72862",
    "user": "@nexttime"
}
```

Ping. (#11586, which has positive review, depends on this one.)



---

archive/issue_comments_072863.json:
```json
{
    "body": "Attachment [8241.patch](tarball://root/attachments/some-uuid/ticket8241/8241.patch) by @roed314 created at 2012-02-21 12:33:12\n\nAs Sebastian Pancratz noted in his talk, it would be great if someone wrote a better implementation of this.",
    "created_at": "2012-02-21T12:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72863",
    "user": "@roed314"
}
```

Attachment [8241.patch](tarball://root/attachments/some-uuid/ticket8241/8241.patch) by @roed314 created at 2012-02-21 12:33:12

As Sebastian Pancratz noted in his talk, it would be great if someone wrote a better implementation of this.



---

archive/issue_comments_072864.json:
```json
{
    "body": "The patchbot finds some Sphinx formatting errors in the docstrings:\n\n\n```\ndocstring of sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.\ndocstring of sage.rings.padics.padic_ZZ_pX_CA_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.\ndocstring of sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.\ndocstring of sage.rings.padics.padic_ZZ_pX_CR_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.\ndocstring of sage.rings.padics.padic_ext_element.pAdicExtElement.frobenius:6: WARNING: Inline interpreted text or phrase reference start-string without end-string.\n```\n\n\nIt's also harping on about trailing whitespace (which is apparently now a Bad Thing, although Sage has been tolerating it cheerfully for years).",
    "created_at": "2012-03-10T17:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72864",
    "user": "@loefflerd"
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

archive/issue_comments_072865.json:
```json
{
    "body": "Here's a new patch with the docstrings straightened out and trailing whitespace removed. I've also added a doctest to show that an error is raised when \"frobenius\" is called on an element of a ramified extension. I'm happy with the rest of the code, so if David's happy with my changes we can call this that's a positive review.",
    "created_at": "2012-03-12T18:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72865",
    "user": "@loefflerd"
}
```

Here's a new patch with the docstrings straightened out and trailing whitespace removed. I've also added a doctest to show that an error is raised when "frobenius" is called on an element of a ramified extension. I'm happy with the rest of the code, so if David's happy with my changes we can call this that's a positive review.



---

archive/issue_comments_072866.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-12T19:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72866",
    "user": "@roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072867.json:
```json
{
    "body": "Looks good to me.  I've created #12657: write a more efficient implementation of Frobenius.",
    "created_at": "2012-03-12T19:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72867",
    "user": "@roed314"
}
```

Looks good to me.  I've created #12657: write a more efficient implementation of Frobenius.



---

archive/issue_comments_072868.json:
```json
{
    "body": "Attachment [trac_8241-frobenius.patch](tarball://root/attachments/some-uuid/ticket8241/trac_8241-frobenius.patch) by @loefflerd created at 2012-03-12 19:47:42\n\nApply only this patch. Patch against 5.0.beta7",
    "created_at": "2012-03-12T19:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72868",
    "user": "@loefflerd"
}
```

Attachment [trac_8241-frobenius.patch](tarball://root/attachments/some-uuid/ticket8241/trac_8241-frobenius.patch) by @loefflerd created at 2012-03-12 19:47:42

Apply only this patch. Patch against 5.0.beta7



---

archive/issue_comments_072869.json:
```json
{
    "body": "Patchbot's grumbling about trailing whitespace again, so I removed one single space character and re-uploaded the patch.",
    "created_at": "2012-03-12T19:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72869",
    "user": "@loefflerd"
}
```

Patchbot's grumbling about trailing whitespace again, so I removed one single space character and re-uploaded the patch.



---

archive/issue_comments_072870.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-21T22:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8241#issuecomment-72870",
    "user": "@jdemeyer"
}
```

Resolution: fixed
