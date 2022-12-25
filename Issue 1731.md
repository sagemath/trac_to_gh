# Issue 1731: SAge mac app

archive/issues_001731.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom NASA:\n\n\n```\nHi,\n\nThanks for Sage - it's awesome. I need to convince my coworkers to\nswitch from their proprietary programs to Sage.\n\nI've attached a little script that uses the Platypus program\n(http://www.sveinbjorn.org/software) to bundle the sage directory\ninto a clickable Mac application. It has some code to update the\nSAGE_ROOT variable so that things still work if a user drags the\nprogram around.\n\nMy code is public domain, so feel free to use it if you like it.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1731\n\n",
    "created_at": "2008-01-09T06:54:44Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "SAge mac app",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1731",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

From NASA:


```
Hi,

Thanks for Sage - it's awesome. I need to convince my coworkers to
switch from their proprietary programs to Sage.

I've attached a little script that uses the Platypus program
(http://www.sveinbjorn.org/software) to bundle the sage directory
into a clickable Mac application. It has some code to update the
SAGE_ROOT variable so that things still work if a user drags the
program around.

My code is public domain, so feel free to use it if you like it.
```


Issue created by migration from https://trac.sagemath.org/ticket/1731





---

archive/issue_events_004205.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-09T14:46:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1731#event-4205"
}
```



---

archive/issue_comments_010929.json:
```json
{
    "body": "Attachment [sageMac.tgz](tarball://root/attachments/some-uuid/ticket1731/sageMac.tgz) by mabshoff created at 2008-01-09 14:46:57",
    "created_at": "2008-01-09T14:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1731#issuecomment-10929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sageMac.tgz](tarball://root/attachments/some-uuid/ticket1731/sageMac.tgz) by mabshoff created at 2008-01-09 14:46:57



---

archive/issue_comments_010930.json:
```json
{
    "body": "Some more info from http://groups.google.com/group/sage-devel/t/c181f8ccde549cdd:\n\n```\n rpmuller@gmail.com     \t\nView profile\n\t More options Feb 9, 3:20 am\nFrom: \"rpmul...@gmail.com\" <rpmul...@gmail.com>\nDate: Fri, 8 Feb 2008 18:20:32 -0800 (PST)\nLocal: Sat, Feb 9 2008 3:20 am\nSubject: Mac-like application for Sage on Mac\nReply | Reply to author | Forward | Print | Individual message | Show original | Remove | Report this message | Find messages by this author\nI remember reading somewhere when I downloaded a version of Sage that\nthe program was soliciting help from mac-experts in making the binary\nversion of Sage a little more mac-like.\n\nI'm certainly not a mac expert. However, I got Sage working through a\nmac-like icon using the Platypus program (http://www.sveinbjorn.org/\nplatypus). There's a good article here (http://www.tuaw.com/2007/05/08/\nplatypus-create-mac-binaries-from-ruby-perl-shell-scripts-et/) about\nhow to use the program here. But it's kinda nice. Among other\nprograms, the Gimp.app program uses Sage for it's Mac application\nbundle.\n\nI created a shell script that looks like this:\n\n#!/bin/sh\ncat > startsage << EOF\nnotebook()\nEOF\n/Users/rmuller/Programs/sage-2.10/sage < sage\n\nand had Platypus run it, putting the output into a text window. This\nruns the notebook() function and the twisted server, and pops open the\nbrowser with the Sage notebook.\n\nThe drawback is that the script needs to know the path to my sage\ninstallation. I think that the workaround to this is to actually put\nthe entire Sage installation in the folder that Platypus creates for\nthe application. OS X applications on the Mac are actually folders\n(unix directories).\n\nDoes this sound like it would be useful to the Sage community if I\ncould get it working? \n```\n",
    "created_at": "2008-02-10T10:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1731#issuecomment-10930",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Some more info from http://groups.google.com/group/sage-devel/t/c181f8ccde549cdd:

```
 rpmuller@gmail.com     	
View profile
	 More options Feb 9, 3:20 am
From: "rpmul...@gmail.com" <rpmul...@gmail.com>
Date: Fri, 8 Feb 2008 18:20:32 -0800 (PST)
Local: Sat, Feb 9 2008 3:20 am
Subject: Mac-like application for Sage on Mac
Reply | Reply to author | Forward | Print | Individual message | Show original | Remove | Report this message | Find messages by this author
I remember reading somewhere when I downloaded a version of Sage that
the program was soliciting help from mac-experts in making the binary
version of Sage a little more mac-like.

I'm certainly not a mac expert. However, I got Sage working through a
mac-like icon using the Platypus program (http://www.sveinbjorn.org/
platypus). There's a good article here (http://www.tuaw.com/2007/05/08/
platypus-create-mac-binaries-from-ruby-perl-shell-scripts-et/) about
how to use the program here. But it's kinda nice. Among other
programs, the Gimp.app program uses Sage for it's Mac application
bundle.

I created a shell script that looks like this:

#!/bin/sh
cat > startsage << EOF
notebook()
EOF
/Users/rmuller/Programs/sage-2.10/sage < sage

and had Platypus run it, putting the output into a text window. This
runs the notebook() function and the twisted server, and pops open the
browser with the Sage notebook.

The drawback is that the script needs to know the path to my sage
installation. I think that the workaround to this is to actually put
the entire Sage installation in the folder that Platypus creates for
the application. OS X applications on the Mac are actually folders
(unix directories).

Does this sound like it would be useful to the Sage community if I
could get it working? 
```




---

archive/issue_comments_010931.json:
```json
{
    "body": "Please check out http://wiki.sagemath.org/SageMacApplication for more information on the whole \"Sage Application on OSX\" issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1731#issuecomment-10931",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please check out http://wiki.sagemath.org/SageMacApplication for more information on the whole "Sage Application on OSX" issue.

Cheers,

Michael



---

archive/issue_comments_010932.json:
```json
{
    "body": "In https://groups.google.com/group/sage-support/t/9bff2799e1ae4885 Greg Landweber suggested:\n\n```\nYou don't need any fancy droplets or applets. You can just use the\nfollowing AppleScript to activate Sage (take this script and save it\nas an AppleScript application, then put it in the same directory as\nthe \"sage\" UNIX executable):\n\ntell application \"Finder\"\n        set myFolder to container of (path to me) as string\nend tell\n\ntell application \"Terminal\"\n        activate\n        do script (POSIX path of myFolder) & \"sage\"\nend tell\n\nIf on the other hand you want to start the notebook and don't need the\nterminal window in front, you can use the following AppleScript to\nopen a terminal window in the background and start Sage in notebook\nmode:\n\ntell application \"Finder\"\n        set myFolder to container of (path to me) as string\nend tell\n\ntell application \"Terminal\"\n        do script (POSIX path of myFolder) & \"sage --notebook\"\nend tell\n\nWhat else did you folks have in mind in terms of Mac OS X integration?\n\n-- Greg \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-30T06:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1731#issuecomment-10932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

In https://groups.google.com/group/sage-support/t/9bff2799e1ae4885 Greg Landweber suggested:

```
You don't need any fancy droplets or applets. You can just use the
following AppleScript to activate Sage (take this script and save it
as an AppleScript application, then put it in the same directory as
the "sage" UNIX executable):

tell application "Finder"
        set myFolder to container of (path to me) as string
end tell

tell application "Terminal"
        activate
        do script (POSIX path of myFolder) & "sage"
end tell

If on the other hand you want to start the notebook and don't need the
terminal window in front, you can use the following AppleScript to
open a terminal window in the background and start Sage in notebook
mode:

tell application "Finder"
        set myFolder to container of (path to me) as string
end tell

tell application "Terminal"
        do script (POSIX path of myFolder) & "sage --notebook"
end tell

What else did you folks have in mind in terms of Mac OS X integration?

-- Greg 
```


Cheers,

Michael



---

archive/issue_comments_010933.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T22:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1731#issuecomment-10933",
    "user": "https://github.com/malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_004206.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-08T03:20:23Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1731#event-4206"
}
```



---

archive/issue_events_004207.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-08T03:20:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1731#event-4207"
}
```



---

archive/issue_comments_010934.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-08T03:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1731#issuecomment-10934",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004208.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-08T03:20:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1731#event-4208"
}
```



---

archive/issue_comments_010935.json:
```json
{
    "body": "Fixed via #4817. Improvement should be done on top of that codebase.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T03:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1731#issuecomment-10935",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via #4817. Improvement should be done on top of that codebase.

Cheers,

Michael
