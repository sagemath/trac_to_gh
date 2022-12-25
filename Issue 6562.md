# Issue 6562: [with patch, needs review] Unicode support in TextCells

archive/issues_006562.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: textcell unicode\n\nIn a TextCell (shift+click on the blue line) I write some letters:\n\n http://www.math.bme.hu/~morap/sage_textcell1.png\n\nafter I save it. It looks fine:\n\n http://www.math.bme.hu/~morap/sage_textcell2.png\n\nbut when I double click on it to edit, then I get:\n\n http://www.math.bme.hu/~morap/sage_textcell3.png\n\nThat's the problem. I could not find out what (Python or TinyMCE) converts the special characters to html entities (for example \u00e9 to &eacute;), but it does not convert all of them.\n\nThe patch solves the problem. Without it the html code looks like:\n\n http://www.math.bme.hu/~morap/sage_textcell4.png\n\nusing the patch everything's fine. The html code after applying the patch:\n\n http://www.math.bme.hu/~morap/sage_textcell5.png\n\nIssue created by migration from https://trac.sagemath.org/ticket/6562\n\n",
    "created_at": "2009-07-19T18:54:53Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] Unicode support in TextCells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```
Assignee: boothby

Keywords: textcell unicode

In a TextCell (shift+click on the blue line) I write some letters:

 http://www.math.bme.hu/~morap/sage_textcell1.png

after I save it. It looks fine:

 http://www.math.bme.hu/~morap/sage_textcell2.png

but when I double click on it to edit, then I get:

 http://www.math.bme.hu/~morap/sage_textcell3.png

That's the problem. I could not find out what (Python or TinyMCE) converts the special characters to html entities (for example é to &eacute;), but it does not convert all of them.

The patch solves the problem. Without it the html code looks like:

 http://www.math.bme.hu/~morap/sage_textcell4.png

using the patch everything's fine. The html code after applying the patch:

 http://www.math.bme.hu/~morap/sage_textcell5.png

Issue created by migration from https://trac.sagemath.org/ticket/6562





---

archive/issue_comments_053421.json:
```json
{
    "body": "Attachment [12659.patch](tarball://root/attachments/some-uuid/ticket6562/12659.patch) by mora created at 2009-07-19 18:55:39",
    "created_at": "2009-07-19T18:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6562#issuecomment-53421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

Attachment [12659.patch](tarball://root/attachments/some-uuid/ticket6562/12659.patch) by mora created at 2009-07-19 18:55:39



---

archive/issue_comments_053422.json:
```json
{
    "body": "The Ticket 6464 is nearly the same. I suggest the solution of 6464 to use.",
    "created_at": "2009-07-25T01:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6562#issuecomment-53422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mora"
}
```

The Ticket 6464 is nearly the same. I suggest the solution of 6464 to use.



---

archive/issue_comments_053423.json:
```json
{
    "body": "To release manager: this should be closed as a duplicate of #6464, as mentioned above.",
    "created_at": "2009-08-26T13:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6562#issuecomment-53423",
    "user": "https://github.com/kcrisman"
}
```

To release manager: this should be closed as a duplicate of #6464, as mentioned above.



---

archive/issue_comments_053424.json:
```json
{
    "body": "Closing this as a duplicate of #6464.",
    "created_at": "2009-08-26T20:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6562#issuecomment-53424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this as a duplicate of #6464.



---

archive/issue_comments_053425.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-08-26T20:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6562",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6562#issuecomment-53425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate
