# Issue 1636: jmol 3d graphics -- make 3d output dynamically resizable

archive/issues_001636.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\n\n```\nRobert,\n\nIt is possible to have _very_ nice dynamically resizable 3d jmol applets embedded in the Sage\nnotebook.  The attached demo Sage worksheet illustrates this.  To try it, do the following:\n\n(1) Upload the worksheet.\n\n(2) Evaluate the cell with the Torus plot in it.\n\n(3) Refresh and view source to find the path to the actual jmol data file that defines the Torus plot.\n\n(4) In Edit mode put that path where this is:\n\n<script>jmolApplet([\"100%\",\"100%\"], \"script /home/admin/27/cells/2/sage0-size400.jmol?\");</script>\n\n(5) Use the worksheet (and maybe press refresh).  You'll get a 2-torus plot in the upper left with \ngrey bars on the bottom and right of the plot -- resize them to resize the torus plot.  This even \nworks fine if you start the plot spinning, view it stereographically, etc.  I.e., it is very robust.\n\nThis is just a neat proof of concept though.  To really do this right, search\nfor other possible resize javascript libraries, or modify the code in the sws\nto be more generic. \n\nThis resizing stuff could also be very nice for notebook output cells :-).\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1636\n\n",
    "created_at": "2007-12-29T06:33:53Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "jmol 3d graphics -- make 3d output dynamically resizable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1636",
    "user": "was"
}
```
Assignee: was

CC:  jason


```
Robert,

It is possible to have _very_ nice dynamically resizable 3d jmol applets embedded in the Sage
notebook.  The attached demo Sage worksheet illustrates this.  To try it, do the following:

(1) Upload the worksheet.

(2) Evaluate the cell with the Torus plot in it.

(3) Refresh and view source to find the path to the actual jmol data file that defines the Torus plot.

(4) In Edit mode put that path where this is:

<script>jmolApplet(["100%","100%"], "script /home/admin/27/cells/2/sage0-size400.jmol?");</script>

(5) Use the worksheet (and maybe press refresh).  You'll get a 2-torus plot in the upper left with 
grey bars on the bottom and right of the plot -- resize them to resize the torus plot.  This even 
works fine if you start the plot spinning, view it stereographically, etc.  I.e., it is very robust.

This is just a neat proof of concept though.  To really do this right, search
for other possible resize javascript libraries, or modify the code in the sws
to be more generic. 

This resizing stuff could also be very nice for notebook output cells :-).

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/1636





---

archive/issue_comments_010409.json:
```json
{
    "body": "Attachment [resize.sws](tarball://root/attachments/some-uuid/ticket1636/resize.sws) by jason created at 2009-02-16 16:53:16",
    "created_at": "2009-02-16T16:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1636#issuecomment-10409",
    "user": "jason"
}
```

Attachment [resize.sws](tarball://root/attachments/some-uuid/ticket1636/resize.sws) by jason created at 2009-02-16 16:53:16
