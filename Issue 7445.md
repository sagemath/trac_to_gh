# Issue 7445: Have jmol export a standalone html page with 3d applet

archive/issues_007445.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: jmol, graphics, 3d, applet\n\nThis ticket is analogous to #3106, but in addition to exporting a 2d image there should be a way to export a html page with the 3d applet script embedded.  \n\nIt would be assumed that the user has a jmol/ directory in the same directory as the html file - I don't see an easy way to be more flexible about that. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7445\n\n",
    "created_at": "2009-11-12T17:10:27Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "Have jmol export a standalone html page with 3d applet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7445",
    "user": "mhampton"
}
```
Assignee: boothby

Keywords: jmol, graphics, 3d, applet

This ticket is analogous to #3106, but in addition to exporting a 2d image there should be a way to export a html page with the 3d applet script embedded.  

It would be assumed that the user has a jmol/ directory in the same directory as the html file - I don't see an easy way to be more flexible about that. 

Issue created by migration from https://trac.sagemath.org/ticket/7445





---

archive/issue_comments_062677.json:
```json
{
    "body": "\n```\nI thought this might be of some interest to people since I'm not sure\nhow well the process is documented.\n\nI wanted to make some vector field plots using Jmol and then put them\non a web page.  To do that, you have to get the zipped script file\nfrom the cell, unzip it, and put it on your web server.  The server\nalso has to have the jmol directory with the standard jmol .jar files\nand Jmol.js (downloaded from the jmol site).\n\nInstead of trying to explain it in detail, it may be more helpful to\nlook at the result:\n```\n\n\nhttp://www.d.umn.edu/~mhampton/m3298f9/vfieldplots.html\n\n```\n...for the lab the students are given a list of vector fields that\nthey must match to the plots.\n\nIt would be nice if this could be automated in some way, with some\nsort of \"export to html page\" command, analogous to the \"Get Image\"\ncommand currently supported.\n\n-Marshall Hampton\n```\n",
    "created_at": "2009-11-12T17:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7445#issuecomment-62677",
    "user": "was"
}
```


```
I thought this might be of some interest to people since I'm not sure
how well the process is documented.

I wanted to make some vector field plots using Jmol and then put them
on a web page.  To do that, you have to get the zipped script file
from the cell, unzip it, and put it on your web server.  The server
also has to have the jmol directory with the standard jmol .jar files
and Jmol.js (downloaded from the jmol site).

Instead of trying to explain it in detail, it may be more helpful to
look at the result:
```


http://www.d.umn.edu/~mhampton/m3298f9/vfieldplots.html

```
...for the lab the students are given a list of vector fields that
they must match to the plots.

It would be nice if this could be automated in some way, with some
sort of "export to html page" command, analogous to the "Get Image"
command currently supported.

-Marshall Hampton
```




---

archive/issue_comments_062678.json:
```json
{
    "body": "A suggestion for anybody who might implement this.  It might be nice to be able to add a caption, or explanatory text, as part of an automated conversion to an HTML page.  Maybe a command to use at the command line could include a \"caption\" keyword, or from the notebook a dialog might pop-up to ask?",
    "created_at": "2009-11-12T22:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7445#issuecomment-62678",
    "user": "rbeezer"
}
```

A suggestion for anybody who might implement this.  It might be nice to be able to add a caption, or explanatory text, as part of an automated conversion to an HTML page.  Maybe a command to use at the command line could include a "caption" keyword, or from the notebook a dialog might pop-up to ask?



---

archive/issue_comments_062679.json:
```json
{
    "body": "It might be a good idea to look at GeoGebra's export facility -- it's really nice. It lets you select a title, author, date, and some text above and below the applet, and then drops all the files you need in a directory. I don't know if we want to copy their method, but it's a good place to get ideas. To experiment with this, just visit http://geogebra.org and do the \"webstart\".",
    "created_at": "2009-11-12T23:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7445#issuecomment-62679",
    "user": "ddrake"
}
```

It might be a good idea to look at GeoGebra's export facility -- it's really nice. It lets you select a title, author, date, and some text above and below the applet, and then drops all the files you need in a directory. I don't know if we want to copy their method, but it's a good place to get ideas. To experiment with this, just visit http://geogebra.org and do the "webstart".



---

archive/issue_comments_062680.json:
```json
{
    "body": "See discussion at http://groups.google.com/group/sage-edu/browse_thread/thread/d497a28ac9dcac11?hl=en\n\nIn particular, in the latest versions of jmol one can set defaultdirectory to be inside the zip file, negating the need for an external script that does (only) that.",
    "created_at": "2010-01-07T06:32:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7445#issuecomment-62680",
    "user": "robertwb"
}
```

See discussion at http://groups.google.com/group/sage-edu/browse_thread/thread/d497a28ac9dcac11?hl=en

In particular, in the latest versions of jmol one can set defaultdirectory to be inside the zip file, negating the need for an external script that does (only) that.



---

archive/issue_comments_062681.json:
```json
{
    "body": "Closing deprecated notebook tickets",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7445#issuecomment-62681",
    "user": "boothby"
}
```

Closing deprecated notebook tickets



---

archive/issue_comments_062682.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T02:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7445#issuecomment-62682",
    "user": "boothby"
}
```

Resolution: invalid
