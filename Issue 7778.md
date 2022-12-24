# Issue 7778: Update jsMath-image-fonts install path detection

archive/issues_007778.json:
```json
{
    "body": "Assignee: was\n\nCC:  drkirkby robert.marik timdumol was\n\nPost-#7467, the SageNB install path depends on its version, but `jsmath-image-fonts-1.4.p2.spkg` expects a slightly different format.\n\nThis ticket just updates `spkg-install`.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/82304cb7adbb22f9), [sage-devel](http://groups.google.com/group/sage-devel/msg/10b3e588e9110322).\n\nRelated tickets: #7196, #7229, #7467, #7755.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7778\n\n",
    "created_at": "2009-12-28T05:32:11Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Update jsMath-image-fonts install path detection",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7778",
    "user": "mpatel"
}
```
Assignee: was

CC:  drkirkby robert.marik timdumol was

Post-#7467, the SageNB install path depends on its version, but `jsmath-image-fonts-1.4.p2.spkg` expects a slightly different format.

This ticket just updates `spkg-install`.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/82304cb7adbb22f9), [sage-devel](http://groups.google.com/group/sage-devel/msg/10b3e588e9110322).

Related tickets: #7196, #7229, #7467, #7755.

Issue created by migration from https://trac.sagemath.org/ticket/7778





---

archive/issue_comments_067066.json:
```json
{
    "body": "There's a trial package at\n\n* [http://sage.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg](http://sage.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg)\n* [http://boxen.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg](http://boxen.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg)\n\nI've CC'd Dr. Kirkby, because I see\n\n```sh\n$ checkbashisms -x -f spkg-install\npossible bashism in spkg-install line 36 (bash arrays, ${name[0|*|@]}):\nfor DIR in ${CANDIDATES[@]}; do\npossible bashism in spkg-install line 44 (bash arrays, ${name[0|*|@]}):\n    echo \"${CANDIDATES[*]}\"\n```\n\nI don't know if these are problems on Solaris or, if they are, how to work around them.",
    "created_at": "2009-12-28T06:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67066",
    "user": "mpatel"
}
```

There's a trial package at

* [http://sage.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg](http://sage.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg)
* [http://boxen.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg](http://boxen.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg)

I've CC'd Dr. Kirkby, because I see

```sh
$ checkbashisms -x -f spkg-install
possible bashism in spkg-install line 36 (bash arrays, ${name[0|*|@]}):
for DIR in ${CANDIDATES[@]}; do
possible bashism in spkg-install line 44 (bash arrays, ${name[0|*|@]}):
    echo "${CANDIDATES[*]}"
```

I don't know if these are problems on Solaris or, if they are, how to work around them.



---

archive/issue_comments_067067.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-28T06:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67067",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067068.json:
```json
{
    "body": "Works with Sage 4.3. Positive review. Thanks for fixing.",
    "created_at": "2009-12-28T11:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67068",
    "user": "robert.marik"
}
```

Works with Sage 4.3. Positive review. Thanks for fixing.



---

archive/issue_comments_067069.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-28T11:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67069",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067070.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T02:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67070",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_067071.json:
```json
{
    "body": "I've merged this in with the optional spkgs.",
    "created_at": "2010-01-04T02:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67071",
    "user": "mhansen"
}
```

I've merged this in with the optional spkgs.



---

archive/issue_comments_067072.json:
```json
{
    "body": "Hi,\n\nI upgraded sagenb.org to use sagenb-0.5.  I then tried to install this spkg.  It definitely got confused and didn't work, for some reason (maybe because of an old sagenb from before).   I eventually *manually* copied the fonts to:\n\n/usr/local/sage/local/lib/python/site-packages/sagenb/data/jsmath/fonts\n\nwhere sagenb is a symlink to sagenb-0.5-*egg/sagenb, and this did work. \n\nNotice that:\n\n```\nroot@boxen:/usr/local/sage/local/lib/python/site-packages/sagenb/data/jsmath/fonts# python\nPython 2.5.2 (r252:60911, Jul 22 2009, 15:33:10) \n[GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu3)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> import os\n>>> from pkg_resources import Requirement, working_set\n>>> sagenb_path = working_set.find(Requirement.parse('sagenb')).location\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\nAttributeError: 'NoneType' object has no attribute 'location'\n```\n\n\nI'm really just recording this for posterity in case there really is something wrong.  I don't have time to delve deeper now.",
    "created_at": "2010-01-10T04:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67072",
    "user": "was"
}
```

Hi,

I upgraded sagenb.org to use sagenb-0.5.  I then tried to install this spkg.  It definitely got confused and didn't work, for some reason (maybe because of an old sagenb from before).   I eventually *manually* copied the fonts to:

/usr/local/sage/local/lib/python/site-packages/sagenb/data/jsmath/fonts

where sagenb is a symlink to sagenb-0.5-*egg/sagenb, and this did work. 

Notice that:

```
root@boxen:/usr/local/sage/local/lib/python/site-packages/sagenb/data/jsmath/fonts# python
Python 2.5.2 (r252:60911, Jul 22 2009, 15:33:10) 
[GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu3)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> from pkg_resources import Requirement, working_set
>>> sagenb_path = working_set.find(Requirement.parse('sagenb')).location
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'location'
```


I'm really just recording this for posterity in case there really is something wrong.  I don't have time to delve deeper now.



---

archive/issue_comments_067073.json:
```json
{
    "body": "I would not be surprised, if it really is wrong.  The Python script embedded in `spkg-install` is run with `/usr/bin/env python`.  Maybe this doesn't always use Sage's `python`?",
    "created_at": "2010-01-10T06:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7778#issuecomment-67073",
    "user": "mpatel"
}
```

I would not be surprised, if it really is wrong.  The Python script embedded in `spkg-install` is run with `/usr/bin/env python`.  Maybe this doesn't always use Sage's `python`?
