# Issue 7106: [with patch, needs review] Add keyboard shortcut ctrl-0 to reference manual

archive/issues_007106.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: keyboard shortcuts\n\nThe new parenthesis matching keyboard shortcut ctrl-0 introduced in\n#3646 was not documented in the doc string of config.py. Once all\ninformation is in the doc string, I would suggest to shorten the help\npage text a little.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7106\n\n",
    "created_at": "2009-10-04T05:45:59Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with patch, needs review] Add keyboard shortcut ctrl-0 to reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7106",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```
Assignee: tba

Keywords: keyboard shortcuts

The new parenthesis matching keyboard shortcut ctrl-0 introduced in
#3646 was not documented in the doc string of config.py. Once all
information is in the doc string, I would suggest to shorten the help
page text a little.

Issue created by migration from https://trac.sagemath.org/ticket/7106





---

archive/issue_comments_058716.json:
```json
{
    "body": "Attachment [trac_7106.patch](tarball://root/attachments/some-uuid/ticket7106/trac_7106.patch) by hgranath created at 2009-10-04 05:47:19\n\nDepends on #7104",
    "created_at": "2009-10-04T05:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58716",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Attachment [trac_7106.patch](tarball://root/attachments/some-uuid/ticket7106/trac_7106.patch) by hgranath created at 2009-10-04 05:47:19

Depends on #7104



---

archive/issue_comments_058717.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-10-04T06:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58717",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_058718.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-10-04T06:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58718",
    "user": "https://trac.sagemath.org/admin/accounts/users/hgranath"
}
```

Changing priority from major to minor.



---

archive/issue_comments_058719.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-07T19:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58719",
    "user": "https://github.com/maxthemouse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058720.json:
```json
{
    "body": "Works with sage -docbuild reference html. ~! Adam",
    "created_at": "2009-10-07T19:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58720",
    "user": "https://github.com/maxthemouse"
}
```

Works with sage -docbuild reference html. ~! Adam



---

archive/issue_comments_058721.json:
```json
{
    "body": "This needs to be rebased against the new sagenb project. http://nb.sagemath.org/",
    "created_at": "2009-10-19T06:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58721",
    "user": "https://github.com/williamstein"
}
```

This needs to be rebased against the new sagenb project. http://nb.sagemath.org/



---

archive/issue_comments_058722.json:
```json
{
    "body": "Changing component from documentation to notebook.",
    "created_at": "2009-10-19T06:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58722",
    "user": "https://github.com/williamstein"
}
```

Changing component from documentation to notebook.



---

archive/issue_comments_058723.json:
```json
{
    "body": "Attachment [trac_7106-paren_match_doc.patch](tarball://root/attachments/some-uuid/ticket7106/trac_7106-paren_match_doc.patch) by @qed777 created at 2009-11-01 12:12:26\n\nRebased for sagenb 0.4.  Apply only this patch to the sagenb repository.",
    "created_at": "2009-11-01T12:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58723",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7106-paren_match_doc.patch](tarball://root/attachments/some-uuid/ticket7106/trac_7106-paren_match_doc.patch) by @qed777 created at 2009-11-01 12:12:26

Rebased for sagenb 0.4.  Apply only this patch to the sagenb repository.



---

archive/issue_comments_058724.json:
```json
{
    "body": "The [attachment:trac_7106-paren_match_doc.patch new patch] applies to sagenb 0.4 (or so).",
    "created_at": "2009-11-01T12:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58724",
    "user": "https://github.com/qed777"
}
```

The [attachment:trac_7106-paren_match_doc.patch new patch] applies to sagenb 0.4 (or so).



---

archive/issue_comments_058725.json:
```json
{
    "body": "Attachment [trac_7106-paren_match_doc_v2.patch](tarball://root/attachments/some-uuid/ticket7106/trac_7106-paren_match_doc_v2.patch) by @qed777 created at 2009-11-01 13:29:47\n\nFix Sphinx warning, better spacing. Apply only this patch to the sagenb repository.",
    "created_at": "2009-11-01T13:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58725",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7106-paren_match_doc_v2.patch](tarball://root/attachments/some-uuid/ticket7106/trac_7106-paren_match_doc_v2.patch) by @qed777 created at 2009-11-01 13:29:47

Fix Sphinx warning, better spacing. Apply only this patch to the sagenb repository.



---

archive/issue_comments_058726.json:
```json
{
    "body": "Version 2:\n\n* Fixes a Sphinx warning.\n* Inserts space between the list items.",
    "created_at": "2009-11-01T13:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58726",
    "user": "https://github.com/qed777"
}
```

Version 2:

* Fixes a Sphinx warning.
* Inserts space between the list items.



---

archive/issue_comments_058727.json:
```json
{
    "body": "The files look good to me. Silly question: where do these parts show up in the docbuild or in the help?\n\nCheers,\nAdam",
    "created_at": "2009-11-03T18:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58727",
    "user": "https://github.com/maxthemouse"
}
```

The files look good to me. Silly question: where do these parts show up in the docbuild or in the help?

Cheers,
Adam



---

archive/issue_comments_058728.json:
```json
{
    "body": "I apologize, if I'm misinterpreting your question.  The changes to\n\n* `config.py` should appear on [\"this\" page](http://www.sagemath.org/doc/reference/notebook.html).\n* `tutorial.py` should appear on the main notebook help page, e.g., http://www.sagenb.org/help/ .\n\nTo rebuild the docs after applying a patch to the `sage` repository (i.e., the main Sage library), try, e.g.,\n\n* `sage -b`\n* `sage -docbuild reference html -j`\n* Browse to `$SAGE_ROOT/devel/sage/doc/output/html/en/reference/index.html`\n\nPlease see `sage -docbuild -H` for more options.  If/after #7367 merges, the post-patch procedure for the `sagenb` repository could be\n\n* `cd sagenb-0.4/`\n* `sage -python setup.py install`\n* `sage -docbuild reference html -j`\n\nShould we move `tutorial.notebook_help` to a HTML page or template?",
    "created_at": "2009-11-04T04:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58728",
    "user": "https://github.com/qed777"
}
```

I apologize, if I'm misinterpreting your question.  The changes to

* `config.py` should appear on ["this" page](http://www.sagemath.org/doc/reference/notebook.html).
* `tutorial.py` should appear on the main notebook help page, e.g., http://www.sagenb.org/help/ .

To rebuild the docs after applying a patch to the `sage` repository (i.e., the main Sage library), try, e.g.,

* `sage -b`
* `sage -docbuild reference html -j`
* Browse to `$SAGE_ROOT/devel/sage/doc/output/html/en/reference/index.html`

Please see `sage -docbuild -H` for more options.  If/after #7367 merges, the post-patch procedure for the `sagenb` repository could be

* `cd sagenb-0.4/`
* `sage -python setup.py install`
* `sage -docbuild reference html -j`

Should we move `tutorial.notebook_help` to a HTML page or template?



---

archive/issue_comments_058729.json:
```json
{
    "body": "Thanks! That more or less answers my question. I had run the docbuild but was having difficulty finding where the exact changes were. I am still looking but I have a better idea where to look. ~ Adam",
    "created_at": "2009-11-04T14:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58729",
    "user": "https://github.com/maxthemouse"
}
```

Thanks! That more or less answers my question. I had run the docbuild but was having difficulty finding where the exact changes were. I am still looking but I have a better idea where to look. ~ Adam



---

archive/issue_comments_058730.json:
```json
{
    "body": "I'm merging this.  Note that it says \"only python comments\" and I think Python should be capitalized.  I made this one trivial change in the official sagenb repo.",
    "created_at": "2009-11-11T19:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58730",
    "user": "https://github.com/williamstein"
}
```

I'm merging this.  Note that it says "only python comments" and I think Python should be capitalized.  I made this one trivial change in the official sagenb repo.



---

archive/issue_comments_058731.json:
```json
{
    "body": "merged into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T19:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58731",
    "user": "https://github.com/williamstein"
}
```

merged into sagenb-0.4.2 (sage-4.2.1)



---

archive/issue_comments_058732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7106#issuecomment-58732",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
