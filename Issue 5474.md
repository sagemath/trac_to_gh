# Issue 5474: [with patch, needs review] delimiters for LaTeX representation of matrices

archive/issues_005474.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThere was a request on [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/f12feafb8e4285ce) for the option to change how matrices are displayed, from parentheses to square brackets.  William made this suggestion:\n\n```\nHow about adding a function to matrix0.pyx that sets a global variable\nin that file to the left and right delimiters for matrices?\n\nsage.matrix.matrix0.set_latex_delimiters('[',']')\n\nwould set them.  That's minimally intrusive.  Later on somebody could\ncome up with some grand scheme for customizing latex output, but\nplease don't until there are a few more use cases. \n```\n\nThe attached patch implements \"set_matrix_latex_delimiters\". (I changed the name slightly.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5474\n\n",
    "created_at": "2009-03-10T21:23:00Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] delimiters for LaTeX representation of matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5474",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

There was a request on [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/f12feafb8e4285ce) for the option to change how matrices are displayed, from parentheses to square brackets.  William made this suggestion:

```
How about adding a function to matrix0.pyx that sets a global variable
in that file to the left and right delimiters for matrices?

sage.matrix.matrix0.set_latex_delimiters('[',']')

would set them.  That's minimally intrusive.  Later on somebody could
come up with some grand scheme for customizing latex output, but
please don't until there are a few more use cases. 
```

The attached patch implements "set_matrix_latex_delimiters". (I changed the name slightly.)


Issue created by migration from https://trac.sagemath.org/ticket/5474





---

archive/issue_comments_042466.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-10T21:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5474#issuecomment-42466",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_042467.json:
```json
{
    "body": "Here's a vector version, too.",
    "created_at": "2009-03-10T21:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5474#issuecomment-42467",
    "user": "jhpalmieri"
}
```

Here's a vector version, too.



---

archive/issue_comments_042468.json:
```json
{
    "body": "Frickin' awesome!   NIce!",
    "created_at": "2009-03-10T22:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5474#issuecomment-42468",
    "user": "was"
}
```

Frickin' awesome!   NIce!



---

archive/issue_comments_042469.json:
```json
{
    "body": "Merged both patches in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-11T00:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5474#issuecomment-42469",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.final.

Cheers,

Michael



---

archive/issue_comments_042470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-11T00:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5474#issuecomment-42470",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042471.json:
```json
{
    "body": "Thank you!  This has been a minor annoyance when using Sage in class, since we use different delimiters than Sage...",
    "created_at": "2009-03-11T00:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5474#issuecomment-42471",
    "user": "jason"
}
```

Thank you!  This has been a minor annoyance when using Sage in class, since we use different delimiters than Sage...



---

archive/issue_comments_042472.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> Thank you!  This has been a minor annoyance when using Sage in class, since we use different delimiters than Sage...\n\nYou're welcome! I hope it works well for you.",
    "created_at": "2009-03-11T01:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5474#issuecomment-42472",
    "user": "jhpalmieri"
}
```

Replying to [comment:4 jason]:
> Thank you!  This has been a minor annoyance when using Sage in class, since we use different delimiters than Sage...

You're welcome! I hope it works well for you.
