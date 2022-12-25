# Issue 7229: jsmath-image-fonts spkg installs to wrong directory

archive/issues_007229.json:
```json
{
    "body": "Assignee: boothby\n\nWith the update to the new sage notebook, the jsmath-image-fonts spkg now installs to the wrong directory.\n\n\n```\n> >  * Install *all* jsMath image fonts on sagenb.org\n> >  * Silently fall back to using image fonts if TeX fonts are not available\n\n\nThis is what was done in the sage notebook a few days ago.  William had \ninstalled the optional jsmath-image-fonts spkg a long time ago.  What \nprobably happened is that no one rebased the jsmath-image-fonts to copy \nto the right javascript directory, and since these all moved around with \nthe new notebook code, everything is broken with respect to this spkg now.\n\nA solution is to modify the spkg to install to the right location, and \ninstall it again on sagenb.org.\n```\n\n\nRobert replies:\n\nInstalled 4.1.2. and the old spkg file with image fonts.\nI got this error\nI copied the image fonts from /opt/sage/local/notebook/javascript/\njsmath to /opt/sage/local/lib/python2.6/site-packages/sagenb/data/\njavascript/jsmath and everything works fine.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7229\n\n",
    "created_at": "2009-10-15T15:54:26Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "jsmath-image-fonts spkg installs to wrong directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7229",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

With the update to the new sage notebook, the jsmath-image-fonts spkg now installs to the wrong directory.


```
> >  * Install *all* jsMath image fonts on sagenb.org
> >  * Silently fall back to using image fonts if TeX fonts are not available


This is what was done in the sage notebook a few days ago.  William had 
installed the optional jsmath-image-fonts spkg a long time ago.  What 
probably happened is that no one rebased the jsmath-image-fonts to copy 
to the right javascript directory, and since these all moved around with 
the new notebook code, everything is broken with respect to this spkg now.

A solution is to modify the spkg to install to the right location, and 
install it again on sagenb.org.
```


Robert replies:

Installed 4.1.2. and the old spkg file with image fonts.
I got this error
I copied the image fonts from /opt/sage/local/notebook/javascript/
jsmath to /opt/sage/local/lib/python2.6/site-packages/sagenb/data/
javascript/jsmath and everything works fine.


Issue created by migration from https://trac.sagemath.org/ticket/7229





---

archive/issue_comments_059851.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-15T21:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59851",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059852.json:
```json
{
    "body": "The fixed spkg file is at http://user.mendelu.cz/marik/temp/jsmath-image-fonts-1.4.spkg\n(cannot upload to trac server due to the filesize limit)\n\nThe description of the change is at \nhttp://groups.google.cz/group/sage-devel/browse_thread/thread/3bce4bbe7ace0dc0",
    "created_at": "2009-10-15T21:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59852",
    "user": "https://github.com/robert-marik"
}
```

The fixed spkg file is at http://user.mendelu.cz/marik/temp/jsmath-image-fonts-1.4.spkg
(cannot upload to trac server due to the filesize limit)

The description of the change is at 
http://groups.google.cz/group/sage-devel/browse_thread/thread/3bce4bbe7ace0dc0



---

archive/issue_comments_059853.json:
```json
{
    "body": "The spkg didn't have the changed checked in. Also, it had some old bash-isms that would make it not work with some /bin/sh's.  Also, it would fail on any sage before 4.1.2, so I decided to fix it by (1) making it work on older sage's still, and (2) checkin the repo. I also updated the spkg name to .p1.   The new spkg is here:\n\nhttp://sage.math.washington.edu/home/wstein/patches/jsmath-image-fonts-1.4.p1.spkg\n\nSo instead of me giving this a positive review, somebody else should look at it.",
    "created_at": "2009-10-15T21:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59853",
    "user": "https://github.com/williamstein"
}
```

The spkg didn't have the changed checked in. Also, it had some old bash-isms that would make it not work with some /bin/sh's.  Also, it would fail on any sage before 4.1.2, so I decided to fix it by (1) making it work on older sage's still, and (2) checkin the repo. I also updated the spkg name to .p1.   The new spkg is here:

http://sage.math.washington.edu/home/wstein/patches/jsmath-image-fonts-1.4.p1.spkg

So instead of me giving this a positive review, somebody else should look at it.



---

archive/issue_comments_059854.json:
```json
{
    "body": "How should we deal with #7196?  A special `JSMATH_HOME` variable?\n\nAlso: Should we add the [extra fonts](http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/welcome.html)?",
    "created_at": "2009-10-15T21:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59854",
    "user": "https://github.com/qed777"
}
```

How should we deal with #7196?  A special `JSMATH_HOME` variable?

Also: Should we add the [extra fonts](http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/welcome.html)?



---

archive/issue_comments_059855.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> How should we deal with #7196?\nI updated `spkg-install` to handle post-#7196 new notebooks.  For another reviewer:\n\nhttp://sage.math.washington.edu/home/mpatel/trac/7229/jsmath-image-fonts-1.4.p2.spkg",
    "created_at": "2009-10-15T22:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59855",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 mpatel]:
> How should we deal with #7196?
I updated `spkg-install` to handle post-#7196 new notebooks.  For another reviewer:

http://sage.math.washington.edu/home/mpatel/trac/7229/jsmath-image-fonts-1.4.p2.spkg



---

archive/issue_comments_059856.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> I updated `spkg-install` to handle post-#7196 new notebooks.  For another reviewer:\n> \n> http://sage.math.washington.edu/home/mpatel/trac/7229/jsmath-image-fonts-1.4.p2.spkg\n\nWorks fine on fresh install of Sage 4.1.2. \nHowever (as new) I give up the closing of this ticket to some more skilled Sage user/developer.\nThank you for the fix.\nRobert",
    "created_at": "2009-10-16T07:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59856",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:4 mpatel]:
> I updated `spkg-install` to handle post-#7196 new notebooks.  For another reviewer:
> 
> http://sage.math.washington.edu/home/mpatel/trac/7229/jsmath-image-fonts-1.4.p2.spkg

Works fine on fresh install of Sage 4.1.2. 
However (as new) I give up the closing of this ticket to some more skilled Sage user/developer.
Thank you for the fix.
Robert



---

archive/issue_comments_059857.json:
```json
{
    "body": "Positive review -- looks good to me.  I've posted the spkg here and closed the ticket.\nhttp://sagemath.org/packages/optional/",
    "created_at": "2009-10-18T01:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59857",
    "user": "https://github.com/williamstein"
}
```

Positive review -- looks good to me.  I've posted the spkg here and closed the ticket.
http://sagemath.org/packages/optional/



---

archive/issue_comments_059858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-18T01:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7229#issuecomment-59858",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
