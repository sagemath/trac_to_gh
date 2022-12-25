# Issue 7489: Integrate GeoGebra into SageNB

archive/issues_007489.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @kcrisman\n\nKeywords: geogebra java education teaching interactive\n\n[GeoGebra](http://www.geogebra.org/cms/) is free, interactive program for learning and teaching mathematics.  It can run as an [unsigned](http://www.geogebra.org/en/wiki/index.php/Unsigned_GeoGebra_Applets) Java applet in a capable web browser.  It also has a [JavaScript API](http://www.geogebra.org/en/wiki/index.php/GeoGebra_Applet_Methods).  Some links:\n\n* [Screenshots](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=72&Itemid=58).\n* [Examples](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=69&Itemid=56), [more (En)](http://www.geogebra.org/en/wiki/index.php/English), [more (Fr)](http://www.geogebra.org/en/wiki/index.php/French).\n* [Documentation](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=75&Itemid=61), [Know How](http://www.geogebra.org/en/wiki/index.php/GeoGebra_Know_How).\n* [Forums](http://www.geogebra.org/forum/).\n* [Wiki](http://www.geogebra.org/en/wiki/index.php/Main_Page).\n\n\nGiven its features, maturity, and popularity, we should consider integrating GeoGebra into [Sage](http://www.sagemath.org/).\n\nSee, e.g., [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e791fb1c8665c862/f10f8eb92919ad8f?#f10f8eb92919ad8f).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7489\n\n",
    "created_at": "2009-11-18T22:05:36Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Integrate GeoGebra into SageNB",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7489",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @kcrisman

Keywords: geogebra java education teaching interactive

[GeoGebra](http://www.geogebra.org/cms/) is free, interactive program for learning and teaching mathematics.  It can run as an [unsigned](http://www.geogebra.org/en/wiki/index.php/Unsigned_GeoGebra_Applets) Java applet in a capable web browser.  It also has a [JavaScript API](http://www.geogebra.org/en/wiki/index.php/GeoGebra_Applet_Methods).  Some links:

* [Screenshots](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=72&Itemid=58).
* [Examples](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=69&Itemid=56), [more (En)](http://www.geogebra.org/en/wiki/index.php/English), [more (Fr)](http://www.geogebra.org/en/wiki/index.php/French).
* [Documentation](http://www.geogebra.org/cms/index.php?option=com_content&task=blogcategory&id=75&Itemid=61), [Know How](http://www.geogebra.org/en/wiki/index.php/GeoGebra_Know_How).
* [Forums](http://www.geogebra.org/forum/).
* [Wiki](http://www.geogebra.org/en/wiki/index.php/Main_Page).


Given its features, maturity, and popularity, we should consider integrating GeoGebra into [Sage](http://www.sagemath.org/).

See, e.g., [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e791fb1c8665c862/f10f8eb92919ad8f?#f10f8eb92919ad8f).

Issue created by migration from https://trac.sagemath.org/ticket/7489





---

archive/issue_comments_063130.json:
```json
{
    "body": "Just creating a ticket.",
    "created_at": "2009-11-18T22:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63130",
    "user": "https://github.com/qed777"
}
```

Just creating a ticket.



---

archive/issue_comments_063131.json:
```json
{
    "body": "Attachment [sageogebra.py](tarball://root/attachments/some-uuid/ticket7489/sageogebra.py) by @miguelmarco created at 2011-03-04 18:54:46",
    "created_at": "2011-03-04T18:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63131",
    "user": "https://github.com/miguelmarco"
}
```

Attachment [sageogebra.py](tarball://root/attachments/some-uuid/ticket7489/sageogebra.py) by @miguelmarco created at 2011-03-04 18:54:46



---

archive/issue_comments_063132.json:
```json
{
    "body": "I send a proof of concept. It is a class called geogebra_applet that can show geogebra applets and (limited, and only working in ideal conditions now) interact with them.\n\nBy default it uses the .jar files of the geogebra site, but another ones can be passed as parameters. It can also be passed a ggb as a parameter to be loaded.\n\nIf you want to see what it is capable of doing, do the following:\n\nattach('path-to-sageogebra.py')\nA=geogebra_applet()\nA.show()\nA.eval_command('P = (1,1)')",
    "created_at": "2011-03-04T19:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63132",
    "user": "https://github.com/miguelmarco"
}
```

I send a proof of concept. It is a class called geogebra_applet that can show geogebra applets and (limited, and only working in ideal conditions now) interact with them.

By default it uses the .jar files of the geogebra site, but another ones can be passed as parameters. It can also be passed a ggb as a parameter to be loaded.

If you want to see what it is capable of doing, do the following:

attach('path-to-sageogebra.py')
A=geogebra_applet()
A.show()
A.eval_command('P = (1,1)')



---

archive/issue_comments_063133.json:
```json
{
    "body": "Attachment [sageogebra.2.py](tarball://root/attachments/some-uuid/ticket7489/sageogebra.2.py) by jhicks created at 2011-03-05 16:39:53\n\nNow supports multiple applets on a single worksheet",
    "created_at": "2011-03-05T16:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63133",
    "user": "https://trac.sagemath.org/admin/accounts/users/jhicks"
}
```

Attachment [sageogebra.2.py](tarball://root/attachments/some-uuid/ticket7489/sageogebra.2.py) by jhicks created at 2011-03-05 16:39:53

Now supports multiple applets on a single worksheet



---

archive/issue_comments_063134.json:
```json
{
    "body": "See also [Geogebra's GSOC mention of this idea](http://www.geogebra.org/trac/wiki/Gsoc2010).",
    "created_at": "2011-04-19T14:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63134",
    "user": "https://github.com/kcrisman"
}
```

See also [Geogebra's GSOC mention of this idea](http://www.geogebra.org/trac/wiki/Gsoc2010).



---

archive/issue_comments_063135.json:
```json
{
    "body": "Changing keywords from \"geogebra java education teaching interactive\" to \"geogebra java education teaching interactive sd31\".",
    "created_at": "2011-06-14T03:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63135",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "geogebra java education teaching interactive" to "geogebra java education teaching interactive sd31".



---

archive/issue_comments_063136.json:
```json
{
    "body": "#11489 about using iframe is also probably relevant, particularly the examples showing Geogebra use from within Sage.  This is not the same as this ticket, since those would depend on an internet connection and don't actually put GG in Sage, but it's still worth mentioning here.",
    "created_at": "2011-10-13T16:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63136",
    "user": "https://github.com/kcrisman"
}
```

#11489 about using iframe is also probably relevant, particularly the examples showing Geogebra use from within Sage.  This is not the same as this ticket, since those would depend on an internet connection and don't actually put GG in Sage, but it's still worth mentioning here.



---

archive/issue_comments_063137.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-02-16T14:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63137",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063138.json:
```json
{
    "body": "it can be closed - sagenb is not going to be updated one way or another",
    "created_at": "2020-02-16T14:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63138",
    "user": "https://github.com/dimpase"
}
```

it can be closed - sagenb is not going to be updated one way or another



---

archive/issue_comments_063139.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-02-16T14:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63139",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063140.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2020-02-16T18:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7489#issuecomment-63140",
    "user": "https://github.com/fchapoton"
}
```

Resolution: wontfix
