# Issue 1971: notebook/jsmath -- make an optional spkg with the image fonts

archive/issues_001971.json:
```json
{
    "body": "Assignee: boothby\n\nFrom the jsmath author:\n\n\n```\nThe real solution is, of course, to install the jsMath TeX fonts and\navoid the whole issue.  For a private installation (like I expect most\nsage installations are), where you are the only person looking at the\nweb pages that use jsMath, it is reasonable not to install the image\nfonts because once you have the jsMath TeX fonts, there is no need for\nanything else.  On the other hand, if you are hosting a public site,\nwhere you don't know whether your reader has installed the fonts or\nnot, then you have to decide whether it is worth the space in order to\ngive those users a better view of the mathematics on your site.  My\nown feeling is that the image fonts are so much superior to the\nunicode results that it is worth it to me (because I know that most\npeople won't install the TeX fonts, so image-font mode turns out to be\nthe primary mode used by most viewers).  While I would like a method\nwith a smaller footprint on the server, I haven't found one that is as\nreliable and maintainable as the image fonts.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1971\n\n",
    "created_at": "2008-01-29T12:21:42Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "notebook/jsmath -- make an optional spkg with the image fonts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1971",
    "user": "@williamstein"
}
```
Assignee: boothby

From the jsmath author:


```
The real solution is, of course, to install the jsMath TeX fonts and
avoid the whole issue.  For a private installation (like I expect most
sage installations are), where you are the only person looking at the
web pages that use jsMath, it is reasonable not to install the image
fonts because once you have the jsMath TeX fonts, there is no need for
anything else.  On the other hand, if you are hosting a public site,
where you don't know whether your reader has installed the fonts or
not, then you have to decide whether it is worth the space in order to
give those users a better view of the mathematics on your site.  My
own feeling is that the image fonts are so much superior to the
unicode results that it is worth it to me (because I know that most
people won't install the TeX fonts, so image-font mode turns out to be
the primary mode used by most viewers).  While I would like a method
with a smaller footprint on the server, I haven't found one that is as
reliable and maintainable as the image fonts.
```


Issue created by migration from https://trac.sagemath.org/ticket/1971





---

archive/issue_comments_012754.json:
```json
{
    "body": "Attachment [jsmath-fonts.patch](tarball://root/attachments/some-uuid/ticket1971/jsmath-fonts.patch) by @jasongrout created at 2008-02-09 04:46:12\n\nNecessary patch for the jsmath-image-fonts spkg to work.  Relies on #2116",
    "created_at": "2008-02-09T04:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12754",
    "user": "@jasongrout"
}
```

Attachment [jsmath-fonts.patch](tarball://root/attachments/some-uuid/ticket1971/jsmath-fonts.patch) by @jasongrout created at 2008-02-09 04:46:12

Necessary patch for the jsmath-image-fonts spkg to work.  Relies on #2116



---

archive/issue_comments_012755.json:
```json
{
    "body": "The spkg is up at http://sage.math.washington.edu/home/jason/jsmath-image-fonts-1.3.spkg",
    "created_at": "2008-02-09T04:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12755",
    "user": "@jasongrout"
}
```

The spkg is up at http://sage.math.washington.edu/home/jason/jsmath-image-fonts-1.3.spkg



---

archive/issue_comments_012756.json:
```json
{
    "body": "jsmath-fonts.patch looks good to me. I will upload the optional spkg to the repo shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12756",
    "user": "mabshoff"
}
```

jsmath-fonts.patch looks good to me. I will upload the optional spkg to the repo shortly.

Cheers,

Michael



---

archive/issue_comments_012757.json:
```json
{
    "body": "I am somewhat concerned about performance for this patch. On sage.math I get:\n\n```\nsage: %timeit is_package_installed(\"jsmath-image-fonts\")\n10 loops, best of 3: 87.9 ms per loop\n```\n\nWe can easily cache the values and invalidate the catch every time we install a new package. The performance issues isn't critical in case the above code path is only called once per notebook session instantiation, but I don't know the notebook code well enough to make that call.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T02:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12757",
    "user": "mabshoff"
}
```

I am somewhat concerned about performance for this patch. On sage.math I get:

```
sage: %timeit is_package_installed("jsmath-image-fonts")
10 loops, best of 3: 87.9 ms per loop
```

We can easily cache the values and invalidate the catch every time we install a new package. The performance issues isn't critical in case the above code path is only called once per notebook session instantiation, but I don't know the notebook code well enough to make that call.

Cheers,

Michael



---

archive/issue_comments_012758.json:
```json
{
    "body": "Added jsmath-image-fonts-1.3.spkg to the optional spkg repo and mirrored it out.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T02:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12758",
    "user": "mabshoff"
}
```

Added jsmath-image-fonts-1.3.spkg to the optional spkg repo and mirrored it out.

Cheers,

Michael



---

archive/issue_comments_012759.json:
```json
{
    "body": "Attachment [is-installed-cached.patch](tarball://root/attachments/some-uuid/ticket1971/is-installed-cached.patch) by @jasongrout created at 2008-02-16 04:12:44\n\nspeeds up is-installed with a cache.",
    "created_at": "2008-02-16T04:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12759",
    "user": "@jasongrout"
}
```

Attachment [is-installed-cached.patch](tarball://root/attachments/some-uuid/ticket1971/is-installed-cached.patch) by @jasongrout created at 2008-02-16 04:12:44

speeds up is-installed with a cache.



---

archive/issue_comments_012760.json:
```json
{
    "body": "The is-installed-cache.patch file makes is_package_installed cached, like Michael suggested.  This patch should be applied *on top of* #2116.\n\nBefore:\n\n\n```\nsage: %timeit is_package_installed(\"jsmath-image\")\n10 loops, best of 3: 193 ms per loop\n```\n\n\nAfter:\n\n\n```\nsage: %timeit is_package_installed(\"jsmath-image\")\n10000 loops, best of 3: 111 \u00b5s per loop\n```\n\n\nI didn't cache the other functions (standard packages, experimental packages, etc.) because I don't know if they are used enough to make a difference.",
    "created_at": "2008-02-16T04:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12760",
    "user": "@jasongrout"
}
```

The is-installed-cache.patch file makes is_package_installed cached, like Michael suggested.  This patch should be applied *on top of* #2116.

Before:


```
sage: %timeit is_package_installed("jsmath-image")
10 loops, best of 3: 193 ms per loop
```


After:


```
sage: %timeit is_package_installed("jsmath-image")
10000 loops, best of 3: 111 µs per loop
```


I didn't cache the other functions (standard packages, experimental packages, etc.) because I don't know if they are used enough to make a difference.



---

archive/issue_comments_012761.json:
```json
{
    "body": "Apply instead of first jsmath-fonts.patch",
    "created_at": "2008-02-16T04:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12761",
    "user": "@jasongrout"
}
```

Apply instead of first jsmath-fonts.patch



---

archive/issue_comments_012762.json:
```json
{
    "body": "Attachment [jsmath-fonts.2.patch](tarball://root/attachments/some-uuid/ticket1971/jsmath-fonts.2.patch) by @jasongrout created at 2008-02-16 04:31:26\n\nThe jsmath-fonts.2.patch also takes the installed package testing out of the page creation loop and just does the test once.  It should be (very marginally) faster, but theoretically better.\n\nThe jsmath-fonts.2.patch should be applied instead of the jsmath-fonts.patch.",
    "created_at": "2008-02-16T04:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12762",
    "user": "@jasongrout"
}
```

Attachment [jsmath-fonts.2.patch](tarball://root/attachments/some-uuid/ticket1971/jsmath-fonts.2.patch) by @jasongrout created at 2008-02-16 04:31:26

The jsmath-fonts.2.patch also takes the installed package testing out of the page creation loop and just does the test once.  It should be (very marginally) faster, but theoretically better.

The jsmath-fonts.2.patch should be applied instead of the jsmath-fonts.patch.



---

archive/issue_comments_012763.json:
```json
{
    "body": "I like both new patches, so positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T14:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12763",
    "user": "mabshoff"
}
```

I like both new patches, so positive review.

Cheers,

Michael



---

archive/issue_comments_012764.json:
```json
{
    "body": "Merged is-installed-cached.patch and jsmath-fonts.2.patch in Sage 2.10.2.alpha1",
    "created_at": "2008-02-16T14:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12764",
    "user": "mabshoff"
}
```

Merged is-installed-cached.patch and jsmath-fonts.2.patch in Sage 2.10.2.alpha1



---

archive/issue_comments_012765.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-16T14:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1971",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1971#issuecomment-12765",
    "user": "mabshoff"
}
```

Resolution: fixed
