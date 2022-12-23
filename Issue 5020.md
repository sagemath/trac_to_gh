# Issue 5020: auto-cells do not automaticall evaluate (or at least update)

archive/issues_005020.json:
```json
{
    "body": "Assignee: boothby\n\nNotebook cells that start with \"#auto\" do not automatically evaluate on the when a worksheet is opened.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5020\n\n",
    "created_at": "2009-01-19T04:17:47Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "auto-cells do not automaticall evaluate (or at least update)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5020",
    "user": "mhansen"
}
```
Assignee: boothby

Notebook cells that start with "#auto" do not automatically evaluate on the when a worksheet is opened.

Issue created by migration from https://trac.sagemath.org/ticket/5020





---

archive/issue_comments_038240.json:
```json
{
    "body": "They do on sagenb, which is running sage-3.2.3, but do not seem to on my laptop (also running sage-3.2.3)...?",
    "created_at": "2009-01-19T04:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38240",
    "user": "mhampton"
}
```

They do on sagenb, which is running sage-3.2.3, but do not seem to on my laptop (also running sage-3.2.3)...?



---

archive/issue_comments_038241.json:
```json
{
    "body": "As a clarification, #auto seems totally broken for me on an unpatched sage-3.2.3 (on intel OS X 10.5).  That install does have a lot of optional spkgs and the tinymce spkgs, but Dan Drake reports it working with the tinymce patches+spkgs, so I don't know what's going on.",
    "created_at": "2009-01-19T04:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38241",
    "user": "mhampton"
}
```

As a clarification, #auto seems totally broken for me on an unpatched sage-3.2.3 (on intel OS X 10.5).  That install does have a lot of optional spkgs and the tinymce spkgs, but Dan Drake reports it working with the tinymce patches+spkgs, so I don't know what's going on.



---

archive/issue_comments_038242.json:
```json
{
    "body": "Attachment\n\nI've add a test to the notebook selenium test suite which tests this.",
    "created_at": "2009-01-19T05:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38242",
    "user": "mhansen"
}
```

Attachment

I've add a test to the notebook selenium test suite which tests this.



---

archive/issue_comments_038243.json:
```json
{
    "body": "I should mention why this fixes things :-)\n\nThe cells are evaluated when .sage() is called, but the HTML send to the web browser was generated before that.",
    "created_at": "2009-01-19T05:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38243",
    "user": "mhansen"
}
```

I should mention why this fixes things :-)

The cells are evaluated when .sage() is called, but the HTML send to the web browser was generated before that.



---

archive/issue_comments_038244.json:
```json
{
    "body": "Looks good. Positive review.",
    "created_at": "2009-01-19T05:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38244",
    "user": "ddrake"
}
```

Looks good. Positive review.



---

archive/issue_comments_038245.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T06:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38245",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_038246.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T06:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5020#issuecomment-38246",
    "user": "mabshoff"
}
```

Resolution: fixed
