# Issue 8315: Reference manual layout: toggles, sidebar links

archive/issues_008315.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  hivert jhpalmieri nthiery klee\n\nJavaScript additions to `layout.html` that transform a reference manual HTML page on display.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a34a80097ad47805/2e57eb60d7f9881d?#2e57eb60d7f9881d) for some background.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8315\n\n",
    "created_at": "2010-02-20T21:02:10Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Reference manual layout: toggles, sidebar links",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8315",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  hivert jhpalmieri nthiery klee

JavaScript additions to `layout.html` that transform a reference manual HTML page on display.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a34a80097ad47805/2e57eb60d7f9881d?#2e57eb60d7f9881d) for some background.

Issue created by migration from https://trac.sagemath.org/ticket/8315





---

archive/issue_comments_073740.json:
```json
{
    "body": "Reference manual toggles and sidebar links.  sage repo.",
    "created_at": "2010-02-21T06:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73740",
    "user": "mpatel"
}
```

Reference manual toggles and sidebar links.  sage repo.



---

archive/issue_comments_073741.json:
```json
{
    "body": "Attachment [trac_8315-doc_sidebar.patch](tarball://root/attachments/some-uuid/ticket8315/trac_8315-doc_sidebar.patch) by mpatel created at 2010-02-21 07:13:01\n\nI've attached a first take.  Remarks:\n\n* I haven't tested this extensively.\n* The sticky sidebar doesn't work in the live docs.\n* All of the transformations are done in the browser when it renders the page.\n* Feel free to change the colors or suggest other changes!",
    "created_at": "2010-02-21T07:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73741",
    "user": "mpatel"
}
```

Attachment [trac_8315-doc_sidebar.patch](tarball://root/attachments/some-uuid/ticket8315/trac_8315-doc_sidebar.patch) by mpatel created at 2010-02-21 07:13:01

I've attached a first take.  Remarks:

* I haven't tested this extensively.
* The sticky sidebar doesn't work in the live docs.
* All of the transformations are done in the browser when it renders the page.
* Feel free to change the colors or suggest other changes!



---

archive/issue_comments_073742.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-21T07:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73742",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073743.json:
```json
{
    "body": "Oops!\u00a0 Time for a break.",
    "created_at": "2010-02-21T07:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73743",
    "user": "mpatel"
}
```

Oops!  Time for a break.



---

archive/issue_comments_073744.json:
```json
{
    "body": "To do:\n\n* Disable or fix the sticky sidebar in the live docs.\n* Add hide / show / toggle controls for \"all.\"\n* Add a color, etc., for attributes (e.g., aliases), data, exceptions, modules, i.e., the other `autodocumenters`.\n* Fix uniform over-indentation in live docs.\n* Make (sub)section headings toggle (sub)section display.  We can use this in the other docs.\n* Add \"larger\" and \"smaller\" font size controls.\n* When it's necessary, extend the main content to match the sidebar in length.\n\nMost of these are straightforward to implement, I think.",
    "created_at": "2010-02-21T19:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73744",
    "user": "mpatel"
}
```

To do:

* Disable or fix the sticky sidebar in the live docs.
* Add hide / show / toggle controls for "all."
* Add a color, etc., for attributes (e.g., aliases), data, exceptions, modules, i.e., the other `autodocumenters`.
* Fix uniform over-indentation in live docs.
* Make (sub)section headings toggle (sub)section display.  We can use this in the other docs.
* Add "larger" and "smaller" font size controls.
* When it's necessary, extend the main content to match the sidebar in length.

Most of these are straightforward to implement, I think.



---

archive/issue_comments_073745.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-06-23T01:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73745",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_073746.json:
```json
{
    "body": "I'm changing this to \"needs info\" until I can determine which improvements to make.",
    "created_at": "2010-06-23T01:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73746",
    "user": "mpatel"
}
```

I'm changing this to "needs info" until I can determine which improvements to make.



---

archive/issue_comments_073747.json:
```json
{
    "body": "[Here](http://sage.math.washington.edu/home/mpatel/projects/sage_doc/reference/index.html) is the Sage 4.5.rc1 HTML reference manual built with the patch above.  See, for example, [2D Plotting](http://sage.math.washington.edu/home/mpatel/projects/sage_doc/reference/sage/plot/plot.html).  Comments are welcome!",
    "created_at": "2010-07-14T22:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73747",
    "user": "mpatel"
}
```

[Here](http://sage.math.washington.edu/home/mpatel/projects/sage_doc/reference/index.html) is the Sage 4.5.rc1 HTML reference manual built with the patch above.  See, for example, [2D Plotting](http://sage.math.washington.edu/home/mpatel/projects/sage_doc/reference/sage/plot/plot.html).  Comments are welcome!



---

archive/issue_comments_073748.json:
```json
{
    "body": "Wow, I haven't tried it intensively, but for what I saw, it's going to be a great improvement in usability of the doc! Thanks!",
    "created_at": "2010-07-15T01:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73748",
    "user": "nthiery"
}
```

Wow, I haven't tried it intensively, but for what I saw, it's going to be a great improvement in usability of the doc! Thanks!



---

archive/issue_comments_073749.json:
```json
{
    "body": "Oh, by the way: would it be hard to add a pointer to the corresponding live documentation, when available?",
    "created_at": "2010-07-15T01:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73749",
    "user": "nthiery"
}
```

Oh, by the way: would it be hard to add a pointer to the corresponding live documentation, when available?



---

archive/issue_comments_073750.json:
```json
{
    "body": "Replying to [comment:7 nthiery]:\n> Oh, by the way: would it be hard to add a pointer to the corresponding live documentation, when available?\nGood idea!  This should be straightforward.  It may be better to include the link in just the \"fast static\" documentation.  In this case, we have the server address and port number, so we can insert an analogous \"Go live!\" link on the fly.\n\nOf course, this only works if the server is still running and works best when the user is logged into the server.  I'm not aware of an easy way for a page to check whether a link is valid before deciding whether to display it or hide it.\n\nFor the \"offline\" docs (e.g., those accessed via `file:///`), perhaps we could prompt for a working server address (and save it in a cookie) or direct the user to `sagenb.org`?",
    "created_at": "2010-07-15T05:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73750",
    "user": "mpatel"
}
```

Replying to [comment:7 nthiery]:
> Oh, by the way: would it be hard to add a pointer to the corresponding live documentation, when available?
Good idea!  This should be straightforward.  It may be better to include the link in just the "fast static" documentation.  In this case, we have the server address and port number, so we can insert an analogous "Go live!" link on the fly.

Of course, this only works if the server is still running and works best when the user is logged into the server.  I'm not aware of an easy way for a page to check whether a link is valid before deciding whether to display it or hide it.

For the "offline" docs (e.g., those accessed via `file:///`), perhaps we could prompt for a working server address (and save it in a cookie) or direct the user to `sagenb.org`?



---

archive/issue_comments_073751.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2022-10-26T05:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73751",
    "user": "mkoeppe"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_073752.json:
```json
{
    "body": "likely outdated",
    "created_at": "2022-10-26T05:15:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73752",
    "user": "mkoeppe"
}
```

likely outdated



---

archive/issue_comments_073753.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-10-26T05:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73753",
    "user": "klee"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073754.json:
```json
{
    "body": "I agree. We moved to furo.",
    "created_at": "2022-10-26T05:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73754",
    "user": "klee"
}
```

I agree. We moved to furo.



---

archive/issue_comments_073755.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-11-14T19:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8315#issuecomment-73755",
    "user": "mkoeppe"
}
```

Resolution: invalid
