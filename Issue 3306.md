# Issue 3306: [with patch; needs review] shared library for symmetrica

archive/issues_003306.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @kiwifb\n\nI've attached a patch that completely replaces the minimal symmetrica makefile with a much more standard version.  It includes a shared library with a soname (the symmetrica version number must be maintained in the package; currently its a variable in the makefile) and adds normal targets like clean, install, etc.\n\nThis probably needs to be fixed to do shared libraries correctly for non-linux; I'm not sure exactly how that is supposed to work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3306\n\n",
    "created_at": "2008-05-26T03:46:45Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch; needs review] shared library for symmetrica",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3306",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

CC:  @kiwifb

I've attached a patch that completely replaces the minimal symmetrica makefile with a much more standard version.  It includes a shared library with a soname (the symmetrica version number must be maintained in the package; currently its a variable in the makefile) and adds normal targets like clean, install, etc.

This probably needs to be fixed to do shared libraries correctly for non-linux; I'm not sure exactly how that is supposed to work.

Issue created by migration from https://trac.sagemath.org/ticket/3306





---

archive/issue_comments_022817.json:
```json
{
    "body": "Attachment [symmetrica-shared-library.patch](tarball://root/attachments/some-uuid/ticket3306/symmetrica-shared-library.patch) by mabshoff created at 2008-05-26 03:54:59\n\nThe only problem I see here is that \"install\" is generally not guaranteed to be available, i.e. on Solaris it is commonly called ginstall. I will fix this, but other than that positive review. I am also not quite sure if the Solaris ld can handle this as is, but as I am porting Sage to use the Sun Forte compiler suite I will fix those issues anyway.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-26T03:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [symmetrica-shared-library.patch](tarball://root/attachments/some-uuid/ticket3306/symmetrica-shared-library.patch) by mabshoff created at 2008-05-26 03:54:59

The only problem I see here is that "install" is generally not guaranteed to be available, i.e. on Solaris it is commonly called ginstall. I will fix this, but other than that positive review. I am also not quite sure if the Solaris ld can handle this as is, but as I am porting Sage to use the Sun Forte compiler suite I will fix those issues anyway.

Cheers,

Michael



---

archive/issue_comments_022818.json:
```json
{
    "body": "Actually on linux (and probably other unix variants) it seems we\nshould use the \"-Dunix\" flag as well. Mind you after a quick grep\nthrough the source only the file de.c make use of that directive.\nIt also has a MSDOS option there may have been a windows variant\nat some point but I cannot find traces of it on the symmetrica\nweb site.",
    "created_at": "2008-05-26T04:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22818",
    "user": "https://github.com/kiwifb"
}
```

Actually on linux (and probably other unix variants) it seems we
should use the "-Dunix" flag as well. Mind you after a quick grep
through the source only the file de.c make use of that directive.
It also has a MSDOS option there may have been a windows variant
at some point but I cannot find traces of it on the symmetrica
web site.



---

archive/issue_comments_022819.json:
```json
{
    "body": "I am still sitting here pondering whether to apply this patch or not. One issue is that on non-Linux I would need also need to add support for dynamic libraries. But that could be done later, so I will give this another spin and see if it works at least on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-29T14:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am still sitting here pondering whether to apply this patch or not. One issue is that on non-Linux I would need also need to add support for dynamic libraries. But that could be done later, so I will give this another spin and see if it works at least on OSX.

Cheers,

Michael



---

archive/issue_comments_022820.json:
```json
{
    "body": "Ok, after looking at this some more I decided that this needs fixing for OSX, Solaris and Cygwin, so I am not applying it as is.\n\nSorry Tim, but I do not have time right now to fix this properly. Hopefully in the next couple days.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-29T15:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, after looking at this some more I decided that this needs fixing for OSX, Solaris and Cygwin, so I am not applying it as is.

Sorry Tim, but I do not have time right now to fix this properly. Hopefully in the next couple days.

Cheers,

Michael



---

archive/issue_comments_022821.json:
```json
{
    "body": "Sorry for the noise: It would obviously be good for the Debianization project of Sage if this patch were applied. So I would propose that you post a patch that does not touch spkg-install and also does not change the makefile in patches/makefile, i.e. leaves the Sage build as is and moves those changes to the Debian makefile patch. Later on when things are sorted out on other platforms we can then unify the two approaches.\n\nAny such patch would be applied more or less immediately. \n\nCheers,\n\nMichael",
    "created_at": "2008-05-29T15:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sorry for the noise: It would obviously be good for the Debianization project of Sage if this patch were applied. So I would propose that you post a patch that does not touch spkg-install and also does not change the makefile in patches/makefile, i.e. leaves the Sage build as is and moves those changes to the Debian makefile patch. Later on when things are sorted out on other platforms we can then unify the two approaches.

Any such patch would be applied more or less immediately. 

Cheers,

Michael



---

archive/issue_comments_022822.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-20T04:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22822",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_022823.json:
```json
{
    "body": "Note HP-UX uses .sl for shared libaries, not .so, so I would not hard-code .so anywhere. \n\nDave",
    "created_at": "2009-12-16T22:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22823",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note HP-UX uses .sl for shared libaries, not .so, so I would not hard-code .so anywhere. 

Dave



---

archive/issue_comments_022824.json:
```json
{
    "body": "I think we should close bugs that are related to debianization of sage. The content of\nthis bug as been obsoloted by later work in any case. I suspect it may have been merged too without being closed.",
    "created_at": "2011-05-01T23:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22824",
    "user": "https://github.com/kiwifb"
}
```

I think we should close bugs that are related to debianization of sage. The content of
this bug as been obsoloted by later work in any case. I suspect it may have been merged too without being closed.



---

archive/issue_comments_022825.json:
```json
{
    "body": "As mentioned in a previous this is obsolete. Let's close it.",
    "created_at": "2012-03-10T19:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22825",
    "user": "https://github.com/kiwifb"
}
```

As mentioned in a previous this is obsolete. Let's close it.



---

archive/issue_comments_022826.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-03-10T19:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22826",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_022827.json:
```json
{
    "body": "Changing keywords from \"editor_mabshoff\" to \"\".",
    "created_at": "2012-03-11T15:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22827",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "editor_mabshoff" to "".



---

archive/issue_events_003524.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-03-16T10:53:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3306#event-3524"
}
```



---

archive/issue_comments_022828.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-03-16T10:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3306#issuecomment-22828",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
