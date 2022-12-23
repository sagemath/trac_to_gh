# Issue 6741: pil interface

archive/issues_006741.json:
```json
{
    "body": "Assignee: was\n\nThe attached patch implements several functions providing a simpler interface to the Python Imaging Library. For example, you can sharpen the image of an image on the internet you have the url of and save it to Sage's tmp subdirectory.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6741\n\n",
    "created_at": "2009-08-13T23:15:11Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "pil interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6741",
    "user": "wdj"
}
```
Assignee: was

The attached patch implements several functions providing a simpler interface to the Python Imaging Library. For example, you can sharpen the image of an image on the internet you have the url of and save it to Sage's tmp subdirectory.

Issue created by migration from https://trac.sagemath.org/ticket/6741





---

archive/issue_comments_055230.json:
```json
{
    "body": "Attachment\n\nrequires pil-1.1.6, applies to 4.1.1.rc2",
    "created_at": "2009-08-13T23:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55230",
    "user": "wdj"
}
```

Attachment

requires pil-1.1.6, applies to 4.1.1.rc2



---

archive/issue_comments_055231.json:
```json
{
    "body": "Changing component from interfaces to packages.",
    "created_at": "2009-08-18T17:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55231",
    "user": "mvngu"
}
```

Changing component from interfaces to packages.



---

archive/issue_comments_055232.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2009-08-18T17:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55232",
    "user": "mvngu"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_055233.json:
```json
{
    "body": "This [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/caac9691d6fb0160) thread has a discussion about making PIL a standard spkg. The vote for doing so was carried out in that thread.",
    "created_at": "2009-08-18T17:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55233",
    "user": "mvngu"
}
```

This [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/caac9691d6fb0160) thread has a discussion about making PIL a standard spkg. The vote for doing so was carried out in that thread.



---

archive/issue_comments_055234.json:
```json
{
    "body": "This looks very nice.  However, the doctests write to SAGE_ROOT/tmp, which means that a normal user cannot run doctests on this file.  Isn't there somewhere else that we should write temporary data during a doctest?  Maybe using SAGE_TMP or something like that?",
    "created_at": "2009-09-17T09:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55234",
    "user": "jason"
}
```

This looks very nice.  However, the doctests write to SAGE_ROOT/tmp, which means that a normal user cannot run doctests on this file.  Isn't there somewhere else that we should write temporary data during a doctest?  Maybe using SAGE_TMP or something like that?



---

archive/issue_comments_055235.json:
```json
{
    "body": "I guess there isn't a SAGE_TMP.  How about a temporary directory under .sage?",
    "created_at": "2009-09-17T09:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55235",
    "user": "jason"
}
```

I guess there isn't a SAGE_TMP.  How about a temporary directory under .sage?



---

archive/issue_comments_055236.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> I guess there isn't a SAGE_TMP.  How about a temporary directory under .sage?\nYes.",
    "created_at": "2009-09-17T10:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55236",
    "user": "mvngu"
}
```

Replying to [comment:6 jason]:
> I guess there isn't a SAGE_TMP.  How about a temporary directory under .sage?
Yes.



---

archive/issue_comments_055237.json:
```json
{
    "body": "Nice work; thanks for doing this!\n\nMarking as \"needs work\" for the following reasons:\n\n* Doctests which rely on internet should be marked \"optional - requires internet\"\n* image_convert should probably let me specify an output file name, or by default write in the current directory so that we can use it easily in the notebook (e.g., we convert something and it magically appears in the cell output).\n* someone should test this on a mac and then remove the note about it not being tested on a mac\n* stylistically, it looks like there is lots of duplicated code that opens files from the internet; maybe this could be refactored into a single function (and then used for image_convert as well)?",
    "created_at": "2009-09-22T15:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55237",
    "user": "jason"
}
```

Nice work; thanks for doing this!

Marking as "needs work" for the following reasons:

* Doctests which rely on internet should be marked "optional - requires internet"
* image_convert should probably let me specify an output file name, or by default write in the current directory so that we can use it easily in the notebook (e.g., we convert something and it magically appears in the cell output).
* someone should test this on a mac and then remove the note about it not being tested on a mac
* stylistically, it looks like there is lots of duplicated code that opens files from the internet; maybe this could be refactored into a single function (and then used for image_convert as well)?



---

archive/issue_comments_055238.json:
```json
{
    "body": "Replying to [comment:8 jason]:\n> Nice work; thanks for doing this!\n> \n> Marking as \"needs work\" for the following reasons:\n> \n\nArrgghh ...\nJust saw this now, going through old emails.\n\nI will try to work on these referee comments/suggestions now. It probably needs rebasing anyway.\nSorry for the late reply.",
    "created_at": "2010-01-04T03:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55238",
    "user": "wdj"
}
```

Replying to [comment:8 jason]:
> Nice work; thanks for doing this!
> 
> Marking as "needs work" for the following reasons:
> 

Arrgghh ...
Just saw this now, going through old emails.

I will try to work on these referee comments/suggestions now. It probably needs rebasing anyway.
Sorry for the late reply.



---

archive/issue_comments_055239.json:
```json
{
    "body": "Good news: it applies fine and does not need rebasing.\n\nBad news: Now I can't even get the code to work. I've tried on an imac (which requires some extra work to get libjpeg to install) and on an ubuntu machine. Probably I'm missing something obvious, but I don't know what it is.",
    "created_at": "2010-01-08T12:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55239",
    "user": "wdj"
}
```

Good news: it applies fine and does not need rebasing.

Bad news: Now I can't even get the code to work. I've tried on an imac (which requires some extra work to get libjpeg to install) and on an ubuntu machine. Probably I'm missing something obvious, but I don't know what it is.



---

archive/issue_comments_055240.json:
```json
{
    "body": "Attachment\n\nok, here is a cleanup patch.\n\nThere is an issue with fontmanager that I do not understand",
    "created_at": "2013-08-22T20:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55240",
    "user": "chapoton"
}
```

Attachment

ok, here is a cleanup patch.

There is an issue with fontmanager that I do not understand



---

archive/issue_comments_055241.json:
```json
{
    "body": "Can one mark in some way the tests that depends on the presence of libpeg ?\n\nSomething like # optional libjpeg ?",
    "created_at": "2013-08-31T14:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55241",
    "user": "chapoton"
}
```

Can one mark in some way the tests that depends on the presence of libpeg ?

Something like # optional libjpeg ?



---

archive/issue_comments_055242.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-08T09:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55242",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_055243.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-05-19T12:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55243",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_055244.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-29T18:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6741",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6741#issuecomment-55244",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
