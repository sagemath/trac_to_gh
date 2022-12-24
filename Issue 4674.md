# Issue 4674: use easy/load.js when loading jsmath

archive/issues_004674.json:
```json
{
    "body": "Assignee: boothby\n\nFrom http://groups.google.com/group/sage-support/t/178d0bd277044918\n\n```\nYes, that looks correct.  I'm not sure why people are getting the \nerror -7 under these conditions.  It means that something has gone \nwrong when trying to load the fallback method, and that usually means \nit can't read the image font definition files.  There are a couple of \nother possibilities as well:  perhaps the noImageFonts plugin was not \nable to be read (permission issue?) or the unicode fallback file could \nnot be read.  Given your use of noImageFonts, I suspect it may be the \nlatter.  If the users who are getting error -7 are using Firefox3, \nthat may well be it.  There were changes to the same-origin security \npolicy in Firefox3 that prevent jsMath from loading local files from \ndirectories other than the one in which the HTML file is found.  I \nworked around this in jsMath v3.6 (released Sept. 2008), so those \nusers should update to the latest version of jsMath to avoid that \nproblem. \n> I'm pretty sure we don't use the easy/load.js (and I'm not sure why). \n\nProbably because it didn't exist when jsMath support was added to \nsage.  The easy/load.js file was a relatively late addition to jsMath, \nbut certainly makes things easier for people.  You might consider \nwhether you want to use that instead. \n\nDavide\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4674\n\n",
    "created_at": "2008-12-02T15:35:23Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "use easy/load.js when loading jsmath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4674",
    "user": "mabshoff"
}
```
Assignee: boothby

From http://groups.google.com/group/sage-support/t/178d0bd277044918

```
Yes, that looks correct.  I'm not sure why people are getting the 
error -7 under these conditions.  It means that something has gone 
wrong when trying to load the fallback method, and that usually means 
it can't read the image font definition files.  There are a couple of 
other possibilities as well:  perhaps the noImageFonts plugin was not 
able to be read (permission issue?) or the unicode fallback file could 
not be read.  Given your use of noImageFonts, I suspect it may be the 
latter.  If the users who are getting error -7 are using Firefox3, 
that may well be it.  There were changes to the same-origin security 
policy in Firefox3 that prevent jsMath from loading local files from 
directories other than the one in which the HTML file is found.  I 
worked around this in jsMath v3.6 (released Sept. 2008), so those 
users should update to the latest version of jsMath to avoid that 
problem. 
> I'm pretty sure we don't use the easy/load.js (and I'm not sure why). 

Probably because it didn't exist when jsMath support was added to 
sage.  The easy/load.js file was a relatively late addition to jsMath, 
but certainly makes things easier for people.  You might consider 
whether you want to use that instead. 

Davide
```


Issue created by migration from https://trac.sagemath.org/ticket/4674





---

archive/issue_comments_035206.json:
```json
{
    "body": "jsMath is version 3.6a now: http://sourceforge.net/project/showfiles.php?group_id=172663",
    "created_at": "2008-12-02T16:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35206",
    "user": "@jasongrout"
}
```

jsMath is version 3.6a now: http://sourceforge.net/project/showfiles.php?group_id=172663



---

archive/issue_comments_035207.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-02T16:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35207",
    "user": "@jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035208.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2008-12-02T16:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35208",
    "user": "@jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_035209.json:
```json
{
    "body": "#4267 is also related.",
    "created_at": "2008-12-02T16:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35209",
    "user": "@jasongrout"
}
```

#4267 is also related.



---

archive/issue_comments_035210.json:
```json
{
    "body": "#4267 is related in that it already contains an spkg for the updated jsmath.",
    "created_at": "2008-12-02T16:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35210",
    "user": "@jasongrout"
}
```

#4267 is related in that it already contains an spkg for the updated jsmath.



---

archive/issue_comments_035211.json:
```json
{
    "body": "#3768 is the ticket for updating jsmath.",
    "created_at": "2008-12-04T18:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35211",
    "user": "@jasongrout"
}
```

#3768 is the ticket for updating jsmath.



---

archive/issue_comments_035212.json:
```json
{
    "body": "The jsmath spkgs are here: \n\nhttp://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg\n\nhttp://sage.math.washington.edu/home/jason/notebook/jsmath-image-fonts-1.3p0.spkg",
    "created_at": "2008-12-05T09:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35212",
    "user": "@jasongrout"
}
```

The jsmath spkgs are here: 

http://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg

http://sage.math.washington.edu/home/jason/notebook/jsmath-image-fonts-1.3p0.spkg



---

archive/issue_comments_035213.json:
```json
{
    "body": "The obsolete jsmath directory should be deleted out of the extcode repository as well.",
    "created_at": "2008-12-05T09:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35213",
    "user": "@jasongrout"
}
```

The obsolete jsmath directory should be deleted out of the extcode repository as well.



---

archive/issue_comments_035214.json:
```json
{
    "body": "I also cleaned up places where the JSMATH variable was set.  There is no purpose for the variable, since jsmath is a standard part of Sage (it is always installed).",
    "created_at": "2008-12-05T10:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35214",
    "user": "@jasongrout"
}
```

I also cleaned up places where the JSMATH variable was set.  There is no purpose for the variable, since jsmath is a standard part of Sage (it is always installed).



---

archive/issue_comments_035215.json:
```json
{
    "body": "See #4714 for the loading part of this ticket.",
    "created_at": "2008-12-05T10:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35215",
    "user": "@jasongrout"
}
```

See #4714 for the loading part of this ticket.



---

archive/issue_comments_035216.json:
```json
{
    "body": "> I also cleaned up places where the JSMATH variable was set. There \n> is no purpose for the variable, since jsmath is a standard part of \n> Sage (it is always installed). \n\njsmath was standard ever since we used it with the notebook.  That wasn't the point of the variable.  The point is that it gives users a way to turn of use of jsmath entirely, which may be a very good idea in some settings (e.g., low bandwidth notebook servers).   Basically, for no good reason I think you've removed functionality.  Make a new patch that just has the first change in the first version of the patch you attached above.",
    "created_at": "2008-12-06T22:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35216",
    "user": "@williamstein"
}
```

> I also cleaned up places where the JSMATH variable was set. There 
> is no purpose for the variable, since jsmath is a standard part of 
> Sage (it is always installed). 

jsmath was standard ever since we used it with the notebook.  That wasn't the point of the variable.  The point is that it gives users a way to turn of use of jsmath entirely, which may be a very good idea in some settings (e.g., low bandwidth notebook servers).   Basically, for no good reason I think you've removed functionality.  Make a new patch that just has the first change in the first version of the patch you attached above.



---

archive/issue_comments_035217.json:
```json
{
    "body": "Attachment [jsmath-spkg.patch](tarball://root/attachments/some-uuid/ticket4674/jsmath-spkg.patch) by @jasongrout created at 2008-12-20 20:51:28",
    "created_at": "2008-12-20T20:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35217",
    "user": "@jasongrout"
}
```

Attachment [jsmath-spkg.patch](tarball://root/attachments/some-uuid/ticket4674/jsmath-spkg.patch) by @jasongrout created at 2008-12-20 20:51:28



---

archive/issue_comments_035218.json:
```json
{
    "body": "Okay, I updated the jsmath-spkg.patch to address the concerns above.\n\nNote that functionality spoken of in the review has been broken for a while.  I think this is because run_notebook.py automatically sets the JSMATH variable to True, no matter what.  However, fixing this so that it works is a different issue than this ticket.",
    "created_at": "2008-12-20T20:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35218",
    "user": "@jasongrout"
}
```

Okay, I updated the jsmath-spkg.patch to address the concerns above.

Note that functionality spoken of in the review has been broken for a while.  I think this is because run_notebook.py automatically sets the JSMATH variable to True, no matter what.  However, fixing this so that it works is a different issue than this ticket.



---

archive/issue_comments_035219.json:
```json
{
    "body": "Looks good to me. Some review changes were made at\n\n* http://sage.math.washington.edu/home/mabshoff/spkgs/jsmath-3.6a.p0.spkg\n* http://sage.math.washington.edu/home/mabshoff/spkgs/jsmath-image-fonts-1.3p1.spkg\n\nPlease rereview, the changes are fairly minor. I mostly fixed stylistic issues as well as made sure that old jsmath installs (including their fonts) are cleaned out to avoid problems due to left over cruft. This means that an upgrade to jsmath deletes also the image fonts, but that seems a worthwhile price to pay.\n\nFor the record: jsmath-3.6a.p0.spkg is going into standard Sage while jsmath-image-fonts-1.3p1.spkg should go into the optional repo.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T17:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35219",
    "user": "mabshoff"
}
```

Looks good to me. Some review changes were made at

* http://sage.math.washington.edu/home/mabshoff/spkgs/jsmath-3.6a.p0.spkg
* http://sage.math.washington.edu/home/mabshoff/spkgs/jsmath-image-fonts-1.3p1.spkg

Please rereview, the changes are fairly minor. I mostly fixed stylistic issues as well as made sure that old jsmath installs (including their fonts) are cleaned out to avoid problems due to left over cruft. This means that an upgrade to jsmath deletes also the image fonts, but that seems a worthwhile price to pay.

For the record: jsmath-3.6a.p0.spkg is going into standard Sage while jsmath-image-fonts-1.3p1.spkg should go into the optional repo.

Cheers,

Michael



---

archive/issue_comments_035220.json:
```json
{
    "body": "Positive review due to #4705.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T06:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35220",
    "user": "mabshoff"
}
```

Positive review due to #4705.

Cheers,

Michael



---

archive/issue_comments_035221.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T08:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35221",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035222.json:
```json
{
    "body": "Merged jsmath-spkg.patch and jsmath-3.6a.p0.spkg in Sage 3.3.alpha0.\n\nMerged jsmath-image-fonts-1.3p1.spkg into the optional spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T08:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4674",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4674#issuecomment-35222",
    "user": "mabshoff"
}
```

Merged jsmath-spkg.patch and jsmath-3.6a.p0.spkg in Sage 3.3.alpha0.

Merged jsmath-image-fonts-1.3p1.spkg into the optional spkg repo.

Cheers,

Michael
