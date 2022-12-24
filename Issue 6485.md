# Issue 6485: [with patch, needs review] broken links from website index to tutorial, constructions, etc.

archive/issues_006485.json:
```json
{
    "body": "Assignee: tba\n\nBuild the HTML documentation, including the website, and navigate to `$SAGE_ROOT/devel/sage/doc/output/html/en/index.html`.  Clicking on a link to an  individual document yields a directory listing, instead of the expected index page.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6485\n\n",
    "created_at": "2009-07-08T17:32:50Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] broken links from website index to tutorial, constructions, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6485",
    "user": "@qed777"
}
```
Assignee: tba

Build the HTML documentation, including the website, and navigate to `$SAGE_ROOT/devel/sage/doc/output/html/en/index.html`.  Clicking on a link to an  individual document yields a directory listing, instead of the expected index page.

Issue created by migration from https://trac.sagemath.org/ticket/6485





---

archive/issue_comments_052450.json:
```json
{
    "body": "Attachment [trac_6485_website_links.patch](tarball://root/attachments/some-uuid/ticket6485/trac_6485_website_links.patch) by @loefflerd created at 2009-07-13 16:43:35\n\nThis ticket looks like a duplicate of #5550 to me. Since mpatel's already uploaded a patch here, I suggest we close #5550 as a duplicate and keep this one open.",
    "created_at": "2009-07-13T16:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6485#issuecomment-52450",
    "user": "@loefflerd"
}
```

Attachment [trac_6485_website_links.patch](tarball://root/attachments/some-uuid/ticket6485/trac_6485_website_links.patch) by @loefflerd created at 2009-07-13 16:43:35

This ticket looks like a duplicate of #5550 to me. Since mpatel's already uploaded a patch here, I suggest we close #5550 as a duplicate and keep this one open.



---

archive/issue_comments_052451.json:
```json
{
    "body": "Works for me.",
    "created_at": "2009-07-13T19:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6485#issuecomment-52451",
    "user": "@loefflerd"
}
```

Works for me.



---

archive/issue_comments_052452.json:
```json
{
    "body": "The patch fixes the index.html linking problem, but only for the page\n\nSAGE_ROOT/devel/sage/doc/output/html/en/index.html\n\nThere's also a \"website\" which can be built using\n\nsage -docbuild website html\n\nand the same problem is still with the page\n\nSAGE_ROOT/devel/sage/doc/output/html/en/website/index.html\n\nBut I doubt we need \"website\" at all. Its purpose is to link to the other 8 standard documents. This is already achieved with\n\nSAGE_ROOT/devel/sage/doc/output/html/en/index.html\n\nSo I'm closing this ticket as fixing the linking problem in the page \n\nSAGE_ROOT/devel/sage/doc/output/html/en/index.html\n\nFeel free to open another ticket to fix or delete the \"website\" page.",
    "created_at": "2009-07-18T21:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6485#issuecomment-52452",
    "user": "mvngu"
}
```

The patch fixes the index.html linking problem, but only for the page

SAGE_ROOT/devel/sage/doc/output/html/en/index.html

There's also a "website" which can be built using

sage -docbuild website html

and the same problem is still with the page

SAGE_ROOT/devel/sage/doc/output/html/en/website/index.html

But I doubt we need "website" at all. Its purpose is to link to the other 8 standard documents. This is already achieved with

SAGE_ROOT/devel/sage/doc/output/html/en/index.html

So I'm closing this ticket as fixing the linking problem in the page 

SAGE_ROOT/devel/sage/doc/output/html/en/index.html

Feel free to open another ticket to fix or delete the "website" page.



---

archive/issue_comments_052453.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T21:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6485#issuecomment-52453",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_052454.json:
```json
{
    "body": "I think `sage -docbuild website html` builds the top-level `index.html` in `website/` and just copies the output up one directory level.  (We could delete the original afterward.)  Perhaps I should have put \"web site\" in the summary instead of \"website.\"  I apologize, if I'm mistaken.",
    "created_at": "2009-07-19T05:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6485",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6485#issuecomment-52454",
    "user": "@qed777"
}
```

I think `sage -docbuild website html` builds the top-level `index.html` in `website/` and just copies the output up one directory level.  (We could delete the original afterward.)  Perhaps I should have put "web site" in the summary instead of "website."  I apologize, if I'm mistaken.
