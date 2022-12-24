# Issue 3916: Make a %wiki cell mode for the notebook

archive/issues_003916.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timothyclemans\n\nCurrently it seems that the only way to get nice text between cells is to do a %html cell or to edit the worksheet directly.  Either way, you have to write html code by hand.\n\nIt would be nice if there was a %wiki cell mode, like %html, but let you put in wiki markup which would then be converted to HTML to display.\n\nHere are some CREOLE parsers (with examples that convert to html):\n\n[http://creoleparser.googlepages.com/](http://creoleparser.googlepages.com/)\n\n[http://wiki.sheep.art.pl/Wiki%20Creole%20Parser%20in%20Python](http://wiki.sheep.art.pl/Wiki%20Creole%20Parser%20in%20Python)\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3916\n\n",
    "created_at": "2008-08-20T20:36:08Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Make a %wiki cell mode for the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3916",
    "user": "jason"
}
```
Assignee: boothby

CC:  timothyclemans

Currently it seems that the only way to get nice text between cells is to do a %html cell or to edit the worksheet directly.  Either way, you have to write html code by hand.

It would be nice if there was a %wiki cell mode, like %html, but let you put in wiki markup which would then be converted to HTML to display.

Here are some CREOLE parsers (with examples that convert to html):

[http://creoleparser.googlepages.com/](http://creoleparser.googlepages.com/)

[http://wiki.sheep.art.pl/Wiki%20Creole%20Parser%20in%20Python](http://wiki.sheep.art.pl/Wiki%20Creole%20Parser%20in%20Python)





Issue created by migration from https://trac.sagemath.org/ticket/3916





---

archive/issue_comments_028014.json:
```json
{
    "body": "Also, see the python section of [http://www.wikicreole.org/wiki/Converters](http://www.wikicreole.org/wiki/Converters)",
    "created_at": "2008-08-20T20:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28014",
    "user": "jason"
}
```

Also, see the python section of [http://www.wikicreole.org/wiki/Converters](http://www.wikicreole.org/wiki/Converters)



---

archive/issue_comments_028015.json:
```json
{
    "body": "Other options include Markdown ([http://www.freewisdom.org/projects/python-markdown/](http://www.freewisdom.org/projects/python-markdown/)) or reST ([http://docutils.sourceforge.net/rst.html](http://docutils.sourceforge.net/rst.html)).",
    "created_at": "2008-08-20T20:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28015",
    "user": "jason"
}
```

Other options include Markdown ([http://www.freewisdom.org/projects/python-markdown/](http://www.freewisdom.org/projects/python-markdown/)) or reST ([http://docutils.sourceforge.net/rst.html](http://docutils.sourceforge.net/rst.html)).



---

archive/issue_comments_028016.json:
```json
{
    "body": "Attachment [trac3916-creole.patch](tarball://root/attachments/some-uuid/ticket3916/trac3916-creole.patch) by AlexGhitza created at 2009-01-23 02:51:10",
    "created_at": "2009-01-23T02:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28016",
    "user": "AlexGhitza"
}
```

Attachment [trac3916-creole.patch](tarball://root/attachments/some-uuid/ticket3916/trac3916-creole.patch) by AlexGhitza created at 2009-01-23 02:51:10



---

archive/issue_comments_028017.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28017",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_028018.json:
```json
{
    "body": "Since we already have text cells, is this still relevant?",
    "created_at": "2009-12-06T12:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28018",
    "user": "timdumol"
}
```

Since we already have text cells, is this still relevant?



---

archive/issue_comments_028019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T16:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28019",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_028020.json:
```json
{
    "body": "Nope, this isn't relevant.",
    "created_at": "2009-12-09T16:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28020",
    "user": "was"
}
```

Nope, this isn't relevant.



---

archive/issue_comments_028021.json:
```json
{
    "body": "Resolution changed from fixed to invalid",
    "created_at": "2009-12-09T16:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28021",
    "user": "was"
}
```

Resolution changed from fixed to invalid



---

archive/issue_comments_028022.json:
```json
{
    "body": "wait, how do text cells enable me to use markdown syntax?\n\ni'd like to be able to write the in-between text in markdown, run it through sage and markdown, and get a nicely-formatted html page. How could this be accomplished?",
    "created_at": "2010-02-04T00:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28022",
    "user": "edrex"
}
```

wait, how do text cells enable me to use markdown syntax?

i'd like to be able to write the in-between text in markdown, run it through sage and markdown, and get a nicely-formatted html page. How could this be accomplished?



---

archive/issue_comments_028023.json:
```json
{
    "body": "Replying to [comment:9 edrex]:\n> wait, how do text cells enable me to use markdown syntax?\n> \n> i'd like to be able to write the in-between text in markdown, run it through sage and markdown, and get a nicely-formatted html page. How could this be accomplished? \n\nI agree-- text cells are nice, but I don't want to spend half my day pointing-and-click around to get something formatted.  Markdown allows you to format without breaking the flow of writing.",
    "created_at": "2010-02-16T01:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3916#issuecomment-28023",
    "user": "Sharpie"
}
```

Replying to [comment:9 edrex]:
> wait, how do text cells enable me to use markdown syntax?
> 
> i'd like to be able to write the in-between text in markdown, run it through sage and markdown, and get a nicely-formatted html page. How could this be accomplished? 

I agree-- text cells are nice, but I don't want to spend half my day pointing-and-click around to get something formatted.  Markdown allows you to format without breaking the flow of writing.
