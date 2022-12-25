# Issue 5579: preparsing error in recursive load of .sage files

archive/issues_005579.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nHi all,\n\nI ran into the following unexpected behavior, which I assume is because\nthe preparser does not work with nested loads.  I have two files,\nfoo.sage and bar.sage.  Their contents are as follows:\n\nfoo.sage\n--------\ndef foo():\n return (-1)**(-1)\n\n\nbar.sage\n--------\nload foo.sage\n\n\nThe following sage session works as expected:\n       sage: load foo.sage\n       sage: type(foo())\n       <type 'sage.rings.rational.Rational'>\n\nThe following session does not:\n       sage: load bar.sage\n       sage: type(foo())\n       <type 'float'>\n\nI'm guessing that in the second session the file foo.sage is not getting\npreparsed (and so foo() returns a Python object and not a Sage object).\n Is this correct? If so, is there a way to force it to be preparsed?  I\nlike to have lots of little files with different functions, and then a\nfile which loads whichever of these happen to be working/relevant at the\nmoment.  That way I only have to load one file at the start of my session.\n\nAny advice is much appreciated!\n```\n\n\nI can confirm this bug in Sage-3.4. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5579\n\n",
    "created_at": "2009-03-21T17:08:22Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "preparsing error in recursive load of .sage files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5579",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty


```
Hi all,

I ran into the following unexpected behavior, which I assume is because
the preparser does not work with nested loads.  I have two files,
foo.sage and bar.sage.  Their contents are as follows:

foo.sage
--------
def foo():
 return (-1)**(-1)


bar.sage
--------
load foo.sage


The following sage session works as expected:
       sage: load foo.sage
       sage: type(foo())
       <type 'sage.rings.rational.Rational'>

The following session does not:
       sage: load bar.sage
       sage: type(foo())
       <type 'float'>

I'm guessing that in the second session the file foo.sage is not getting
preparsed (and so foo() returns a Python object and not a Sage object).
 Is this correct? If so, is there a way to force it to be preparsed?  I
like to have lots of little files with different functions, and then a
file which loads whichever of these happen to be working/relevant at the
moment.  That way I only have to load one file at the start of my session.

Any advice is much appreciated!
```


I can confirm this bug in Sage-3.4. 

Issue created by migration from https://trac.sagemath.org/ticket/5579





---

archive/issue_comments_043416.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-03-21T17:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5579#issuecomment-43416",
    "user": "https://github.com/williamstein"
}
```

Resolution: duplicate



---

archive/issue_comments_043417.json:
```json
{
    "body": "stupid trac...",
    "created_at": "2009-03-21T17:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5579#issuecomment-43417",
    "user": "https://github.com/williamstein"
}
```

stupid trac...



---

archive/issue_events_005824.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-03-21T17:09:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5579",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5579#event-5824"
}
```
