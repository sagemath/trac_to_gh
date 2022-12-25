# Issue 4678: hg_sage.commit() Error on OS X 10.5.5. Conflict in libPng.dylib?

archive/issues_004678.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: hg, libpng\n\nWhen trying hg_sage.commit() on OS X 10.5.5. I get the following error\n\n``` \nsage: hg_sage.commit()\ncd \"/Users/tjlahey/sage/devel/sage\" && hg diff  | less\ncd \"/Users/tjlahey/sage/devel/sage\" && hg commit  \ndyld: Symbol not found: __cg_png_create_info_struct\n  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO\n  Expected in: /Users/tjlahey/sage/local/lib//libPng.dylib\n\ntransaction abort!\nrollback completed\nabort: edit failed: mate killed by signal 5\n```\n\nSo, for some reason, there is a conflict with the system frameworks. Unfortunately, this can't be commented out like Macports or Fink.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4678\n\n",
    "created_at": "2008-12-02T18:14:53Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "hg_sage.commit() Error on OS X 10.5.5. Conflict in libPng.dylib?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4678",
    "user": "https://github.com/tjl"
}
```
Assignee: cwitty

Keywords: hg, libpng

When trying hg_sage.commit() on OS X 10.5.5. I get the following error

``` 
sage: hg_sage.commit()
cd "/Users/tjlahey/sage/devel/sage" && hg diff  | less
cd "/Users/tjlahey/sage/devel/sage" && hg commit  
dyld: Symbol not found: __cg_png_create_info_struct
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Users/tjlahey/sage/local/lib//libPng.dylib

transaction abort!
rollback completed
abort: edit failed: mate killed by signal 5
```

So, for some reason, there is a conflict with the system frameworks. Unfortunately, this can't be commented out like Macports or Fink.

Issue created by migration from https://trac.sagemath.org/ticket/4678





---

archive/issue_comments_035175.json:
```json
{
    "body": "Can you supply some more info, i.e. how did you build Sage, i.e. is this a FrameWork build for example. What is EDITOR set to in your environment.\n\nIn general do not open tickets unless it is clear what the bug is. This case is clearly such a case since we will need some discussion what is wrong and trac is the wrong place to do that. For that you should use sage-support instead.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T19:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4678#issuecomment-35175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Can you supply some more info, i.e. how did you build Sage, i.e. is this a FrameWork build for example. What is EDITOR set to in your environment.

In general do not open tickets unless it is clear what the bug is. This case is clearly such a case since we will need some discussion what is wrong and trac is the wrong place to do that. For that you should use sage-support instead.

Cheers,

Michael



---

archive/issue_comments_035176.json:
```json
{
    "body": "This is just a regular build of Sage on OS X 10.5.5 (using make) after moving /opt out of the way. EDITOR is set to:\n\n``` \nEDITOR=mate -w\n```\n\nwhich calls TextMate, but it is crashing before then. If I use a Macports build of mercurial, I can run hg commit just fine (which is what I did after this crashed).\n\nI'll keep your statements about tickets in mind for the future. Sorry.",
    "created_at": "2008-12-02T19:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4678#issuecomment-35176",
    "user": "https://github.com/tjl"
}
```

This is just a regular build of Sage on OS X 10.5.5 (using make) after moving /opt out of the way. EDITOR is set to:

``` 
EDITOR=mate -w
```

which calls TextMate, but it is crashing before then. If I use a Macports build of mercurial, I can run hg commit just fine (which is what I did after this crashed).

I'll keep your statements about tickets in mind for the future. Sorry.



---

archive/issue_comments_035177.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-12-02T19:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4678#issuecomment-35177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_events_004924.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-02T19:43:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4678",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4678#event-4924"
}
```



---

archive/issue_comments_035178.json:
```json
{
    "body": "Yep, mate crahes since when mercurial executes EDITOR for some stupid reason when applying patches it picks up the libpng.dylib provided by Sage. There are two solutions here: \n\n* patch hg to use sage-native-execute\n* you add a dummy script into $SAGE_LOCAL/bin called mate that passes all options to the real mate, but set DYLD_LIBRARY_PATH to the original.\n\nThis should be discussed on sage-devel if we want to patch hg to use sage-native-execute for its EDITOR command, but this ticket is closed as wontfix.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T19:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4678#issuecomment-35178",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yep, mate crahes since when mercurial executes EDITOR for some stupid reason when applying patches it picks up the libpng.dylib provided by Sage. There are two solutions here: 

* patch hg to use sage-native-execute
* you add a dummy script into $SAGE_LOCAL/bin called mate that passes all options to the real mate, but set DYLD_LIBRARY_PATH to the original.

This should be discussed on sage-devel if we want to patch hg to use sage-native-execute for its EDITOR command, but this ticket is closed as wontfix.

Cheers,

Michael



---

archive/issue_comments_035179.json:
```json
{
    "body": "Sorry I forgot: In case we decide to patch hg this would be a new ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T19:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4678#issuecomment-35179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sorry I forgot: In case we decide to patch hg this would be a new ticket.

Cheers,

Michael
