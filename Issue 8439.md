# Issue 8439: maxima interface hangs gcl and/or clisp backends

archive/issues_008439.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @orlitzky @fchapoton\n\nThis is a possible problem when using an external maxima, that uses a backend other then ecl.\n\nclisp has some peculiar ways to figure out there is an associated pty, that is created by pty.py from pexpect interface.\n\ngcl hangs due to an \"unexcaped\" ecl specific command at the start of maxima interface; this took quite some time to find, as I was thinking it was a clisp like related issue, and tried to correct the problem in gcl and/or sage-maxima.lisp.\n\nAlso, probably not related, or a know issue, any lisp backend will hang with a command as simple as:\n\n    sage: maxima.eval('1+1;;')\n\nthat is, two sequential semicolons will apparently confuse the expect interface.\n\nWith the attached patch, going to be used in mandriva rpm, all currently maxima backends works in sage. (When installing sagemath, unless using --auto-select, the installation process will ask what package that provides maxima-backend the user wants, and the options are sbcl, clisp, gcl and ecl).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8439\n\n",
    "created_at": "2010-03-04T22:37:40Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "maxima interface hangs gcl and/or clisp backends",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8439",
    "user": "pcpa"
}
```
Assignee: @williamstein

CC:  @orlitzky @fchapoton

This is a possible problem when using an external maxima, that uses a backend other then ecl.

clisp has some peculiar ways to figure out there is an associated pty, that is created by pty.py from pexpect interface.

gcl hangs due to an "unexcaped" ecl specific command at the start of maxima interface; this took quite some time to find, as I was thinking it was a clisp like related issue, and tried to correct the problem in gcl and/or sage-maxima.lisp.

Also, probably not related, or a know issue, any lisp backend will hang with a command as simple as:

    sage: maxima.eval('1+1;;')

that is, two sequential semicolons will apparently confuse the expect interface.

With the attached patch, going to be used in mandriva rpm, all currently maxima backends works in sage. (When installing sagemath, unless using --auto-select, the installation process will ask what package that provides maxima-backend the user wants, and the options are sbcl, clisp, gcl and ecl).

Issue created by migration from https://trac.sagemath.org/ticket/8439





---

archive/issue_comments_075760.json:
```json
{
    "body": "I asked in http://lists.gnu.org/archive/html/gcl-devel/2010-03/msg00000.html about some possible solution for the issue of gcl backend hanging, but now I believe I found a better workaround, so that, maxima gcl backend has the same behavior as other lisps.\n\nThe problem is that adapting the solution used for clisp in `$SAGE_LOCAL/bin/sage-maxima.lisp `was not enough, as for some reason, the predicate `(output-stream-p *standard-input*) `was still true in the maxima parsing error message code.\n\nThe new patch should correct the issue, or at least, now it doesn't hang in the doctect\n\n`sage: maxima.eval('sage0: x == x;')`",
    "created_at": "2010-03-17T20:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75760",
    "user": "pcpa"
}
```

I asked in http://lists.gnu.org/archive/html/gcl-devel/2010-03/msg00000.html about some possible solution for the issue of gcl backend hanging, but now I believe I found a better workaround, so that, maxima gcl backend has the same behavior as other lisps.

The problem is that adapting the solution used for clisp in `$SAGE_LOCAL/bin/sage-maxima.lisp `was not enough, as for some reason, the predicate `(output-stream-p *standard-input*) `was still true in the maxima parsing error message code.

The new patch should correct the issue, or at least, now it doesn't hang in the doctect

`sage: maxima.eval('sage0: x == x;')`



---

archive/issue_comments_075761.json:
```json
{
    "body": "sage-4.3.3-maxima.patch",
    "created_at": "2010-03-17T20:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75761",
    "user": "pcpa"
}
```

sage-4.3.3-maxima.patch



---

archive/issue_comments_075762.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-16T02:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75762",
    "user": "@orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075763.json:
```json
{
    "body": "Attachment [sage-4.3.3-maxima.patch](tarball://root/attachments/some-uuid/ticket8439/sage-4.3.3-maxima.patch) by @orlitzky created at 2012-01-16 02:55:39",
    "created_at": "2012-01-16T02:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75763",
    "user": "@orlitzky"
}
```

Attachment [sage-4.3.3-maxima.patch](tarball://root/attachments/some-uuid/ticket8439/sage-4.3.3-maxima.patch) by @orlitzky created at 2012-01-16 02:55:39



---

archive/issue_comments_075764.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-01-28T02:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75764",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_075765.json:
```json
{
    "body": "Umm... is this even valid anymore?  Putting 'needs info'.  \n\nI certainly can't believe that this would apply properly any more... and it doesn't.",
    "created_at": "2012-01-28T02:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75765",
    "user": "@kcrisman"
}
```

Umm... is this even valid anymore?  Putting 'needs info'.  

I certainly can't believe that this would apply properly any more... and it doesn't.



---

archive/issue_comments_075766.json:
```json
{
    "body": "Actually, I took a look at this when I was looking for tickets that might be fixed by maxima-5.24. Right now on my machine, it hangs:\n\n\n```\n$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nLoading Sage library. Current Mercurial branch is: devel\nsage: maxima.eval('1+1;;')\n```\n\n| Sage Version 5.0.beta1, Release Date: 2012-01-22                   |\n| Type notebook() for the GUI, and license() for information.        |\n(I've waited a good minute.)",
    "created_at": "2012-01-28T02:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75766",
    "user": "@orlitzky"
}
```

Actually, I took a look at this when I was looking for tickets that might be fixed by maxima-5.24. Right now on my machine, it hangs:


```
$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: devel
sage: maxima.eval('1+1;;')
```

| Sage Version 5.0.beta1, Release Date: 2012-01-22                   |
| Type notebook() for the GUI, and license() for information.        |
(I've waited a good minute.)



---

archive/issue_comments_075767.json:
```json
{
    "body": "Here's what happens in Maxima.\n\n```\n\n(%i4) 1+1;;\n\n(%o4) 2\n\nstdin:76667:incorrect syntax: Premature termination of input at ;.\n;\n ^\n```\n\nI'm just going to make a ticket for that - it's #12372.\n\nThis is still a somewhat weird ticket.  I didn't even know we allowed other Maxima backends officially.",
    "created_at": "2012-01-28T03:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75767",
    "user": "@kcrisman"
}
```

Here's what happens in Maxima.

```

(%i4) 1+1;;

(%o4) 2

stdin:76667:incorrect syntax: Premature termination of input at ;.
;
 ^
```

I'm just going to make a ticket for that - it's #12372.

This is still a somewhat weird ticket.  I didn't even know we allowed other Maxima backends officially.



---

archive/issue_comments_075768.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-01-28T03:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75768",
    "user": "@kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_075769.json:
```json
{
    "body": "I do not remember the exact reason I used the \"1+1;;\" example. Maybe as a hint to show that the interface was very fragile.\n\nI did the initial work to make maxima clisp backend functional because at the time I worked in the first sagemath package it was the lisp used by sage.\n\nI just tested, and all backends (clisp, gcl, ecl, and sbcl) appear functional in my sagemath package.\n\nThe patch used is still sage-4.3.3-maxima.patch (renamed/rediffed) and the related maxima patch is http://svn.mandriva.com/viewvc/packages/cooker/maxima/current/SOURCES/maxima-5.23.0-clisp-noreadline.patch?view=markup that should need a somewhat recent clisp, that understands the -disable-readline option (it was added upstream due to my bug report about this same issue).\n\nIn the case of my sagemath rpm package, for quite some time it requires maxima-runtime-ecl, so, only experienced users should usually install other backends in normal conditions due to never being asked to choose one, at least when installing sagemath.",
    "created_at": "2012-01-28T04:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75769",
    "user": "pcpa"
}
```

I do not remember the exact reason I used the "1+1;;" example. Maybe as a hint to show that the interface was very fragile.

I did the initial work to make maxima clisp backend functional because at the time I worked in the first sagemath package it was the lisp used by sage.

I just tested, and all backends (clisp, gcl, ecl, and sbcl) appear functional in my sagemath package.

The patch used is still sage-4.3.3-maxima.patch (renamed/rediffed) and the related maxima patch is http://svn.mandriva.com/viewvc/packages/cooker/maxima/current/SOURCES/maxima-5.23.0-clisp-noreadline.patch?view=markup that should need a somewhat recent clisp, that understands the -disable-readline option (it was added upstream due to my bug report about this same issue).

In the case of my sagemath rpm package, for quite some time it requires maxima-runtime-ecl, so, only experienced users should usually install other backends in normal conditions due to never being asked to choose one, at least when installing sagemath.



---

archive/issue_comments_075770.json:
```json
{
    "body": "This is very interesting.  Is there any documentation about this backend business?  I'm not as familiar with Mandriva as I ought to be - is this something like the Gentoo idea, where Sage is used with system versions of the programs?",
    "created_at": "2012-01-28T05:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75770",
    "user": "@kcrisman"
}
```

This is very interesting.  Is there any documentation about this backend business?  I'm not as familiar with Mandriva as I ought to be - is this something like the Gentoo idea, where Sage is used with system versions of the programs?



---

archive/issue_comments_075771.json:
```json
{
    "body": "Yes. It is a rpm package installing a sagemath that uses (mostly) system packages. The first working package (at least notebook and most interfaces) I had was for sage 3.2.3. But update after update, it got only good when updating to sage 4.0.1.\n\nAbout maxima backends, I think the proper term is maxima runtime. Just the lisps enabled at compile time. Example:\n\n\n```\n$ maxima --list-avail\nAvailable versions:\nversion 5.24.0, lisp ecl\nversion 5.24.0, lisp clisp\nversion 5.24.0, lisp sbcl\n\n```\n",
    "created_at": "2012-01-28T05:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75771",
    "user": "pcpa"
}
```

Yes. It is a rpm package installing a sagemath that uses (mostly) system packages. The first working package (at least notebook and most interfaces) I had was for sage 3.2.3. But update after update, it got only good when updating to sage 4.0.1.

About maxima backends, I think the proper term is maxima runtime. Just the lisps enabled at compile time. Example:


```
$ maxima --list-avail
Available versions:
version 5.24.0, lisp ecl
version 5.24.0, lisp clisp
version 5.24.0, lisp sbcl

```




---

archive/issue_comments_075772.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2020-06-28T19:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75772",
    "user": "@mkoeppe"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_075773.json:
```json
{
    "body": "This ticket is outdated and should be closed.",
    "created_at": "2020-06-28T19:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75773",
    "user": "@mkoeppe"
}
```

This ticket is outdated and should be closed.



---

archive/issue_comments_075774.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-28T19:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8439#issuecomment-75774",
    "user": "@fchapoton"
}
```

Resolution: invalid
