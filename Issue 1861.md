# Issue 1861: better document sage.el

archive/issues_001861.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe page here http://www.sagemath.org/emacs has a file sage.el that is slightly modified from the ipython.el file.   The documentation of this fact should be clearly stated in the file sage.el, along with some instructions about how to use it and the above URL. \n\nSomebody could fix this and attach the fixed sage.el to this ticket. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1861\n\n",
    "created_at": "2008-01-20T02:41:36Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.2",
    "title": "better document sage.el",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1861",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The page here http://www.sagemath.org/emacs has a file sage.el that is slightly modified from the ipython.el file.   The documentation of this fact should be clearly stated in the file sage.el, along with some instructions about how to use it and the above URL. 

Somebody could fix this and attach the fixed sage.el to this ticket. 

Issue created by migration from https://trac.sagemath.org/ticket/1861





---

archive/issue_comments_011744.json:
```json
{
    "body": "By the way, this bug was reported by Dan Grayson.",
    "created_at": "2008-01-20T02:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11744",
    "user": "https://github.com/williamstein"
}
```

By the way, this bug was reported by Dan Grayson.



---

archive/issue_comments_011745.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11745",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_011746.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-25T18:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11746",
    "user": "https://github.com/gvol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011747.json:
```json
{
    "body": "This has been superseded by the optional sage-mode spkg.",
    "created_at": "2012-05-25T18:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11747",
    "user": "https://github.com/gvol"
}
```

This has been superseded by the optional sage-mode spkg.



---

archive/issue_comments_011748.json:
```json
{
    "body": "Plus, there isn't even an emacs page at sagemath.org any more.  [http://wiki.sagemath.org/sage-mode](http://wiki.sagemath.org/sage-mode) is the new place to go.  It does have a lot better documentation.\n\nTo be pedantic, I *would* point out that the current (0.6) spkg doesn't actually say that this is inherited from ipython.el.  It is sort of implied in sage-mode-0.6/old/README.txt; is that enough?",
    "created_at": "2012-06-28T13:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11748",
    "user": "https://github.com/kcrisman"
}
```

Plus, there isn't even an emacs page at sagemath.org any more.  [http://wiki.sagemath.org/sage-mode](http://wiki.sagemath.org/sage-mode) is the new place to go.  It does have a lot better documentation.

To be pedantic, I *would* point out that the current (0.6) spkg doesn't actually say that this is inherited from ipython.el.  It is sort of implied in sage-mode-0.6/old/README.txt; is that enough?



---

archive/issue_comments_011749.json:
```json
{
    "body": "Since we don't use the old directory anymore (I'm planning to remove it in the next release), and I'm pretty sure the new stuff isn't derived from ipython.el I think this should be closed as won't fix.",
    "created_at": "2012-06-28T16:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11749",
    "user": "https://github.com/gvol"
}
```

Since we don't use the old directory anymore (I'm planning to remove it in the next release), and I'm pretty sure the new stuff isn't derived from ipython.el I think this should be closed as won't fix.



---

archive/issue_comments_011750.json:
```json
{
    "body": "Okay, I'll say that's okay as long as (to honor this ticket) *somewhere* in the documentation, wiki, bitbucket, whatever, there is a place that says this was inspired by ipython.el originally.  Sound good?  I'll put that on #13176, which is for upgrading to 0.7.",
    "created_at": "2012-06-28T16:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11750",
    "user": "https://github.com/kcrisman"
}
```

Okay, I'll say that's okay as long as (to honor this ticket) *somewhere* in the documentation, wiki, bitbucket, whatever, there is a place that says this was inspired by ipython.el originally.  Sound good?  I'll put that on #13176, which is for upgrading to 0.7.



---

archive/issue_comments_011751.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-28T16:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11751",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011752.json:
```json
{
    "body": "I updated the wiki, and SPKG.txt.",
    "created_at": "2012-06-29T11:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11752",
    "user": "https://github.com/gvol"
}
```

I updated the wiki, and SPKG.txt.



---

archive/issue_comments_011753.json:
```json
{
    "body": "Great, this is an immediate improvement on the wiki, and 0.8 has this as well.  Putting back to a \"normal\" milestone since #13176 is slightly more complex.",
    "created_at": "2012-06-29T12:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11753",
    "user": "https://github.com/kcrisman"
}
```

Great, this is an immediate improvement on the wiki, and 0.8 has this as well.  Putting back to a "normal" milestone since #13176 is slightly more complex.



---

archive/issue_comments_011754.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-06-29T12:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11754",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_011755.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Great, this is an immediate improvement on the wiki, and 0.8 has this as well.  Putting back to a \"normal\" milestone since #13176 is slightly more complex.\n\nSo, this has positive_review but no patch and not a duplicate?  What is it then?",
    "created_at": "2012-06-29T14:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11755",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:8 kcrisman]:
> Great, this is an immediate improvement on the wiki, and 0.8 has this as well.  Putting back to a "normal" milestone since #13176 is slightly more complex.

So, this has positive_review but no patch and not a duplicate?  What is it then?



---

archive/issue_comments_011756.json:
```json
{
    "body": "It's sort of like when someone opens a ticket to do something on Trac itself (create a new report, let's say).  Here, updating [the wiki](http://wiki.sagemath.org/sage-mode) and having [upstream](https://bitbucket.org/gvol/sage-mode/changeset/b08a6d64faea) incorporate this last thing in all future versions was sufficient.  After all, the original ticket was just to change a webpage - no patch was really required there.  \n\nIf you'd really like, I can make a patch *from* the changeset and [these](https://bitbucket.org/gvol/sage-mode/changeset/63452ed4dee9) [others](https://bitbucket.org/gvol/sage-mode/changeset/5d9ae431a7c7), attach them here, and we can wait until Ivan actually releases another one or something, but according to the *original* issue, the changes at the wiki are already more than sufficient.  Basically, I figure that the person who actually makes things easier to figure out deserves at least some credit.",
    "created_at": "2012-06-29T14:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11756",
    "user": "https://github.com/kcrisman"
}
```

It's sort of like when someone opens a ticket to do something on Trac itself (create a new report, let's say).  Here, updating [the wiki](http://wiki.sagemath.org/sage-mode) and having [upstream](https://bitbucket.org/gvol/sage-mode/changeset/b08a6d64faea) incorporate this last thing in all future versions was sufficient.  After all, the original ticket was just to change a webpage - no patch was really required there.  

If you'd really like, I can make a patch *from* the changeset and [these](https://bitbucket.org/gvol/sage-mode/changeset/63452ed4dee9) [others](https://bitbucket.org/gvol/sage-mode/changeset/5d9ae431a7c7), attach them here, and we can wait until Ivan actually releases another one or something, but according to the *original* issue, the changes at the wiki are already more than sufficient.  Basically, I figure that the person who actually makes things easier to figure out deserves at least some credit.



---

archive/issue_comments_011757.json:
```json
{
    "body": "Okay, that's clear.",
    "created_at": "2012-06-29T15:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11757",
    "user": "https://github.com/jdemeyer"
}
```

Okay, that's clear.



---

archive/issue_events_002019.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-29T15:35:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1861#event-2019"
}
```



---

archive/issue_comments_011758.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-29T15:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1861#issuecomment-11758",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
