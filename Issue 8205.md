# Issue 8205: sagenb -- the url for published worksheets that's displayed right after publishing is still wrong

archive/issues_008205.json:
```json
{
    "body": "Assignee: was\n\nCC:  acleone timdumol\n\nI upgraded sagenb.org to sagenb-0.7.4, and excitedly hoped that when I click publish to publish a worksheet it would give me the correct URL.    Now it says:\n\n\"Worksheet is publicly viewable at http://localhost:8888/home/pub/1153\"\n\nThis is wrong.  This might even be considered worse than before, since before it did \"... http://:8888/home/pub/1153\" which was obviously wrong.  The above looks less obviously wrong. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8205\n\n",
    "created_at": "2010-02-07T05:19:27Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sagenb -- the url for published worksheets that's displayed right after publishing is still wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8205",
    "user": "was"
}
```
Assignee: was

CC:  acleone timdumol

I upgraded sagenb.org to sagenb-0.7.4, and excitedly hoped that when I click publish to publish a worksheet it would give me the correct URL.    Now it says:

"Worksheet is publicly viewable at http://localhost:8888/home/pub/1153"

This is wrong.  This might even be considered worse than before, since before it did "... http://:8888/home/pub/1153" which was obviously wrong.  The above looks less obviously wrong. 

Issue created by migration from https://trac.sagemath.org/ticket/8205





---

archive/issue_comments_072366.json:
```json
{
    "body": "I think the most robust fix may be to just add another option to the notebook command that specifies the correct URL base instead of trying to cleverly figure it out.",
    "created_at": "2010-02-07T05:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8205#issuecomment-72366",
    "user": "was"
}
```

I think the most robust fix may be to just add another option to the notebook command that specifies the correct URL base instead of trying to cleverly figure it out.



---

archive/issue_comments_072367.json:
```json
{
    "body": "Adding [ProxyPreserveHost On](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#proxypreservehost) to the notebook server `VirtualHost`s in `/etc/apache2/httpd.conf` on `boxen` seems to work.\u00a0 If it works well, we should mention it in the `notebook?` docstring.",
    "created_at": "2010-02-07T16:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8205#issuecomment-72367",
    "user": "mpatel"
}
```

Adding [ProxyPreserveHost On](http://httpd.apache.org/docs/2.2/mod/mod_proxy.html#proxypreservehost) to the notebook server `VirtualHost`s in `/etc/apache2/httpd.conf` on `boxen` seems to work.  If it works well, we should mention it in the `notebook?` docstring.



---

archive/issue_comments_072368.json:
```json
{
    "body": "This now works properly on sagenb.org, anyway\n> Worksheet is publicly viewable at http://sagenb.org/home/pub/5051\n\nI tested it on another server as well, not sure where this was fixed.",
    "created_at": "2014-12-10T21:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8205#issuecomment-72368",
    "user": "kcrisman"
}
```

This now works properly on sagenb.org, anyway
> Worksheet is publicly viewable at http://sagenb.org/home/pub/5051

I tested it on another server as well, not sure where this was fixed.



---

archive/issue_comments_072369.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-10T21:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8205#issuecomment-72369",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072370.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-10T21:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8205#issuecomment-72370",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-12-11T18:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8205#issuecomment-72371",
    "user": "vbraun"
}
```

Resolution: fixed
