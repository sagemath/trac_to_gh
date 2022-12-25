# Issue 5580: preparsing error in recursive load of .sage files

archive/issues_005580.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  mvngu\n\n\n```\nHi all,\n\nI ran into the following unexpected behavior, which I assume is because\nthe preparser does not work with nested loads.  I have two files,\nfoo.sage and bar.sage.  Their contents are as follows:\n\nfoo.sage\n--------\ndef foo():\n return (-1)**(-1)\n\n\nbar.sage\n--------\nload foo.sage\n\n\nThe following sage session works as expected:\n       sage: load foo.sage\n       sage: type(foo())\n       <type 'sage.rings.rational.Rational'>\n\nThe following session does not:\n       sage: load bar.sage\n       sage: type(foo())\n       <type 'float'>\n\nI'm guessing that in the second session the file foo.sage is not getting\npreparsed (and so foo() returns a Python object and not a Sage object).\n Is this correct? If so, is there a way to force it to be preparsed?  I\nlike to have lots of little files with different functions, and then a\nfile which loads whichever of these happen to be working/relevant at the\nmoment.  That way I only have to load one file at the start of my session.\n\nAny advice is much appreciated!\n\n  -- Jason Bandlow\n```\n\n\nI can confirm this bug in Sage-3.4. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5580\n\n",
    "created_at": "2009-03-21T17:08:40Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "preparsing error in recursive load of .sage files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5580",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

CC:  mvngu


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

  -- Jason Bandlow
```


I can confirm this bug in Sage-3.4. 

Issue created by migration from https://trac.sagemath.org/ticket/5580





---

archive/issue_comments_043418.json:
```json
{
    "body": "The example in the description works for me.\u00a0 I suggest closing this ticket as fixed (probably by #7514) but reopening it, if I'm wrong.",
    "created_at": "2010-02-01T08:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5580#issuecomment-43418",
    "user": "https://github.com/qed777"
}
```

The example in the description works for me.  I suggest closing this ticket as fixed (probably by #7514) but reopening it, if I'm wrong.



---

archive/issue_comments_043419.json:
```json
{
    "body": "Close as fixed:\n\n```\n[mvngu@mod sage-4.3.2.alpha1-sage.math]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: load foo.sage\nsage: type(foo())\n<type 'sage.rings.rational.Rational'>\nsage: load bar.sage\nsage: type(foo())\n<type 'sage.rings.rational.Rational'>\nsage: !more foo.sage\ndef foo():\n    return (-1)**(-1)\nsage: !more bar.sage\nload foo.sage\n```\n",
    "created_at": "2010-02-01T08:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5580#issuecomment-43419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed:

```
[mvngu@mod sage-4.3.2.alpha1-sage.math]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: load foo.sage
sage: type(foo())
<type 'sage.rings.rational.Rational'>
sage: load bar.sage
sage: type(foo())
<type 'sage.rings.rational.Rational'>
sage: !more foo.sage
def foo():
    return (-1)**(-1)
sage: !more bar.sage
load foo.sage
```




---

archive/issue_comments_043420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-01T08:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5580#issuecomment-43420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_043421.json:
```json
{
    "body": "One can measure the importance of a scientific work by the number of earlier publications rendered superfluous by it. - D. Hilbert",
    "created_at": "2010-02-01T10:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5580#issuecomment-43421",
    "user": "https://github.com/qed777"
}
```

One can measure the importance of a scientific work by the number of earlier publications rendered superfluous by it. - D. Hilbert
