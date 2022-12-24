# Issue 6676: DeprecationWarning on twisted after starting notebook().

archive/issues_006676.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen I start Sage on Solaris, as soon as I type notebook(), I get a 'DeprecationWarning'. It does not give a good impression to get this after the running the first command one is likely to want to run. It says 'the md5 module is deprecated; use hashlib instead'.\n\nHence I suggest this is fixed asap, as its going to be the first impression someone gets of Sage.\n\nDave\n\nkirkby`@`t2:[/scratch/kirkby/sage-4.1.1.rc0] $ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: notebook()\nThe notebook files are stored in: /rootpool2/local/kirkby/.sage//sage_notebook\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n/scratch/kirkby/sage-4.1.1.rc0/local/lib/python2.6/site-packages/twisted/persisted/sob.py:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead\n  import os, md5, sys\n2009-08-06 00:48:56-0700 [-] Log opened.\n2009-08-06 00:48:56-0700 [-] twistd 8.2.0 (/scratch/kirkby/sage-4.1.1.rc0/local/bin/python 2.6.2) starting up.\n2009-08-06 00:48:56-0700 [-] reactor class: twisted.internet.selectreactor.SelectReactor.\n2009-08-06 00:48:56-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8000\n2009-08-06 00:48:56-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x3e00328>\n/scratch/kirkby/sage-4.1.1.rc0/local/bin/sage-native-execute: xdg-open: not found\n| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |\n| Type notebook() for the GUI, and license() for information.        |\n \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6676\n\n",
    "created_at": "2009-08-06T07:53:58Z",
    "labels": [
        "user interface",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "DeprecationWarning on twisted after starting notebook().",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6676",
    "user": "drkirkby"
}
```
Assignee: @williamstein

When I start Sage on Solaris, as soon as I type notebook(), I get a 'DeprecationWarning'. It does not give a good impression to get this after the running the first command one is likely to want to run. It says 'the md5 module is deprecated; use hashlib instead'.

Hence I suggest this is fixed asap, as its going to be the first impression someone gets of Sage.

Dave

kirkby`@`t2:[/scratch/kirkby/sage-4.1.1.rc0] $ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: notebook()
The notebook files are stored in: /rootpool2/local/kirkby/.sage//sage_notebook
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
/scratch/kirkby/sage-4.1.1.rc0/local/lib/python2.6/site-packages/twisted/persisted/sob.py:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import os, md5, sys
2009-08-06 00:48:56-0700 [-] Log opened.
2009-08-06 00:48:56-0700 [-] twistd 8.2.0 (/scratch/kirkby/sage-4.1.1.rc0/local/bin/python 2.6.2) starting up.
2009-08-06 00:48:56-0700 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
2009-08-06 00:48:56-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8000
2009-08-06 00:48:56-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x3e00328>
/scratch/kirkby/sage-4.1.1.rc0/local/bin/sage-native-execute: xdg-open: not found
| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |
| Type notebook() for the GUI, and license() for information.        |
 


Issue created by migration from https://trac.sagemath.org/ticket/6676





---

archive/issue_comments_054872.json:
```json
{
    "body": "This appears to be a duplicate of #6555",
    "created_at": "2009-09-15T02:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6676#issuecomment-54872",
    "user": "flawrence"
}
```

This appears to be a duplicate of #6555



---

archive/issue_comments_054873.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-07T04:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6676#issuecomment-54873",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054874.json:
```json
{
    "body": "This fixes the problem:\n\n   http://wstein.org/home/wstein/patches/twisted-8.2.0.p1.spkg",
    "created_at": "2009-11-07T04:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6676#issuecomment-54874",
    "user": "@williamstein"
}
```

This fixes the problem:

   http://wstein.org/home/wstein/patches/twisted-8.2.0.p1.spkg



---

archive/issue_comments_054875.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-07T05:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6676#issuecomment-54875",
    "user": "@mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054876.json:
```json
{
    "body": "Looks good to me.  I also added the .patch files for the two new changes.  The merged spkg can be found at http://sage.math.washington.edu/home/mhansen/twisted-8.2.0.p1.spkg",
    "created_at": "2009-11-07T05:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6676#issuecomment-54876",
    "user": "@mwhansen"
}
```

Looks good to me.  I also added the .patch files for the two new changes.  The merged spkg can be found at http://sage.math.washington.edu/home/mhansen/twisted-8.2.0.p1.spkg



---

archive/issue_comments_054877.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-07T05:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6676#issuecomment-54877",
    "user": "@mwhansen"
}
```

Resolution: fixed
