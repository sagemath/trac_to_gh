# Issue 3106: Add an "image" link for a screenshot of the JMOL applet in the notebook

archive/issues_003106.json:
```json
{
    "body": "Assignee: boothby\n\nFrom sage-devel:\n\n\n```\n>  >>  is it possible to export the plots created by plot3d and\n> >  >>  parametric_plot3d to (say) postcript or png or whatever?\n> >  >>\n> >  >\n> >  > The easy options I know of right now:\n> >  >\n> >  > (1) Take a screen shot.\n> >  >\n> >  > (2) Use the option viewer='tachyon' to generate a\n> >  > png instead of an interactive dynamic 3d plot.  Then just save\n> >  > the png to a file.\n> >  >\n> >  > Someday there should be a 3rd option to directly export\n> >  > what jmol produces, but I don't know how to do it.\n> >  > I personally always do (1), since taking screen shots in\n> >  > OS X is so incredibly easy.   I think it is also easy\n> >  > in Linux with say GIMP.\n> >\n> >\n> >  Here are two solutions for getting images from JMOL.  One (easy)\n> >  solution is using the JMOL application (i.e., from the sage command\n> >  line); the other is using the applet and requires a bit more work.  We\n> >  could probably make the applet version a link under the image in the\n> >  notebook.\n> >\n> >  http://wiki.jmol.org/index.php/File_formats#Images\n> >\n> >  Jason\n> >\n\nI think we certainly need to implement the second method.  It's been\nrequested a _lot_.  Could you make a trac ticket for this?\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3106\n\n",
    "created_at": "2008-05-05T16:56:10Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Add an \"image\" link for a screenshot of the JMOL applet in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3106",
    "user": "jason"
}
```
Assignee: boothby

From sage-devel:


```
>  >>  is it possible to export the plots created by plot3d and
> >  >>  parametric_plot3d to (say) postcript or png or whatever?
> >  >>
> >  >
> >  > The easy options I know of right now:
> >  >
> >  > (1) Take a screen shot.
> >  >
> >  > (2) Use the option viewer='tachyon' to generate a
> >  > png instead of an interactive dynamic 3d plot.  Then just save
> >  > the png to a file.
> >  >
> >  > Someday there should be a 3rd option to directly export
> >  > what jmol produces, but I don't know how to do it.
> >  > I personally always do (1), since taking screen shots in
> >  > OS X is so incredibly easy.   I think it is also easy
> >  > in Linux with say GIMP.
> >
> >
> >  Here are two solutions for getting images from JMOL.  One (easy)
> >  solution is using the JMOL application (i.e., from the sage command
> >  line); the other is using the applet and requires a bit more work.  We
> >  could probably make the applet version a link under the image in the
> >  notebook.
> >
> >  http://wiki.jmol.org/index.php/File_formats#Images
> >
> >  Jason
> >

I think we certainly need to implement the second method.  It's been
requested a _lot_.  Could you make a trac ticket for this?

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/3106





---

archive/issue_comments_021463.json:
```json
{
    "body": "Related to this would be to make the \"Print\" link automatically take a screenshot and use the image in the printed page.",
    "created_at": "2008-05-05T16:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21463",
    "user": "jason"
}
```

Related to this would be to make the "Print" link automatically take a screenshot and use the image in the printed page.



---

archive/issue_comments_021464.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21464",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_021465.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-14T09:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21465",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_021466.json:
```json
{
    "body": "Both patches are identical;  you can delete one.",
    "created_at": "2009-02-14T09:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21466",
    "user": "jason"
}
```

Both patches are identical;  you can delete one.



---

archive/issue_comments_021467.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2009-02-14T10:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21467",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_021468.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T10:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21468",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021469.json:
```json
{
    "body": "works for me",
    "created_at": "2009-02-14T11:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21469",
    "user": "TimothyClemans"
}
```

works for me



---

archive/issue_comments_021470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T14:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21470",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021471.json:
```json
{
    "body": "Merged jmol-save-image.patch in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T14:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3106#issuecomment-21471",
    "user": "mabshoff"
}
```

Merged jmol-save-image.patch in Sage 3.3.rc1.

Cheers,

Michael
