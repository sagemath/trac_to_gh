# Issue 8201: Fortran not found on Linux if gfortran not present

archive/issues_008201.json:
```json
{
    "body": "Assignee: Martin Raum\n\nCC:  mvngu\n\nKeywords: fortran\n\nThe spkg-install script on Linux first checks \"which gfortran\" and if no instance is found it aborts. This is a problem if for example the binary is gfortran-4.3. Then sage won't build.\n\nEven then scipy won't build, because as soon as compiler flags are passed in scipy's setup.py, the fortran compiler is not found anymore. This happens because \"sage_fortran\" is our binary/script but it should be a stardard name. Scipy will have to care for the -fPIC flags.\n\nThis is related to #8049 !\n\nIssue created by migration from https://trac.sagemath.org/ticket/8201\n\n",
    "created_at": "2010-02-06T19:09:33Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fortran not found on Linux if gfortran not present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8201",
    "user": "mraum"
}
```
Assignee: Martin Raum

CC:  mvngu

Keywords: fortran

The spkg-install script on Linux first checks "which gfortran" and if no instance is found it aborts. This is a problem if for example the binary is gfortran-4.3. Then sage won't build.

Even then scipy won't build, because as soon as compiler flags are passed in scipy's setup.py, the fortran compiler is not found anymore. This happens because "sage_fortran" is our binary/script but it should be a stardard name. Scipy will have to care for the -fPIC flags.

This is related to #8049 !

Issue created by migration from https://trac.sagemath.org/ticket/8201





---

archive/issue_comments_072329.json:
```json
{
    "body": "Reorganized spkg-install",
    "created_at": "2010-02-06T19:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72329",
    "user": "mraum"
}
```

Reorganized spkg-install



---

archive/issue_comments_072330.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-06T19:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72330",
    "user": "mraum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072331.json:
```json
{
    "body": "Attachment [trac-8201-fortran_spkg_install.patch](tarball://root/attachments/some-uuid/ticket8201/trac-8201-fortran_spkg_install.patch) by mraum created at 2010-02-06 19:11:06",
    "created_at": "2010-02-06T19:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72331",
    "user": "mraum"
}
```

Attachment [trac-8201-fortran_spkg_install.patch](tarball://root/attachments/some-uuid/ticket8201/trac-8201-fortran_spkg_install.patch) by mraum created at 2010-02-06 19:11:06



---

archive/issue_comments_072332.json:
```json
{
    "body": "Correcting a build error that occured with 4.3.2",
    "created_at": "2010-02-08T20:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72332",
    "user": "mraum"
}
```

Correcting a build error that occured with 4.3.2



---

archive/issue_comments_072333.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-21T23:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72333",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_072334.json:
```json
{
    "body": "Attachment [trac-8201-fortran_spkg_install-2.patch](tarball://root/attachments/some-uuid/ticket8201/trac-8201-fortran_spkg_install-2.patch) by drkirkby created at 2010-02-21 23:54:03\n\nWhat happens if you set SAGE_FORTRAN to /usr/local/bin/gfortran-4.3 ? \n\nYou might find that is all you need, as perhaps 'which' will not be called then. The whole idea of SAGE_FORTRAN is to specify the Fortran compiler. I do wonder if it might not be less hassle to just create a link so there is a program called 'gfortran'. \n\nHave you checked this on Solaris 10? It is the sort of thing that could screw up on there as there are lots of code changes. \n\nThere's general information about building on Solaris at\n\n http://wiki.sagemath.org/solaris\n\nInformation specifically for 't2' at\n\n http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\nBoth the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html\n\nDave",
    "created_at": "2010-02-21T23:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72334",
    "user": "drkirkby"
}
```

Attachment [trac-8201-fortran_spkg_install-2.patch](tarball://root/attachments/some-uuid/ticket8201/trac-8201-fortran_spkg_install-2.patch) by drkirkby created at 2010-02-21 23:54:03

What happens if you set SAGE_FORTRAN to /usr/local/bin/gfortran-4.3 ? 

You might find that is all you need, as perhaps 'which' will not be called then. The whole idea of SAGE_FORTRAN is to specify the Fortran compiler. I do wonder if it might not be less hassle to just create a link so there is a program called 'gfortran'. 

Have you checked this on Solaris 10? It is the sort of thing that could screw up on there as there are lots of code changes. 

There's general information about building on Solaris at

 http://wiki.sagemath.org/solaris

Information specifically for 't2' at

 http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave



---

archive/issue_comments_072335.json:
```json
{
    "body": "SAGE_FORTRAN is ignored, if gfortran doesn't exist. Namely, the script will abort. That's why I had to create a patch. Creating links for gfortran is a hack would most probably create new problems anywhere else at another time. Moreover, I don't have admin rights.\nI don't have access to Solaris; And I don't have experience with it. But if the GNU suit is installed it should work; if not it won't, but scipy has to blamed for this not fortran itself.\nIf you can test this on Soloaris I would be happy to integrate any changes you suggest.",
    "created_at": "2010-02-22T07:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72335",
    "user": "mraum"
}
```

SAGE_FORTRAN is ignored, if gfortran doesn't exist. Namely, the script will abort. That's why I had to create a patch. Creating links for gfortran is a hack would most probably create new problems anywhere else at another time. Moreover, I don't have admin rights.
I don't have access to Solaris; And I don't have experience with it. But if the GNU suit is installed it should work; if not it won't, but scipy has to blamed for this not fortran itself.
If you can test this on Soloaris I would be happy to integrate any changes you suggest.



---

archive/issue_comments_072336.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-22T07:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72336",
    "user": "mraum"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_072337.json:
```json
{
    "body": "Replying to [comment:3 mraum]:\n> SAGE_FORTRAN is ignored, if gfortran doesn't exist. \n\n> Namely, the script will abort. That's why I had to create a patch. Creating links for gfortran is a hack would most probably create new problems anywhere else at another time. \n\nWhat makes you think a symbolic link is a hack? It is very standard practice on Unix systems to create symbolic links for this very purpose. There are loads of them created in Sage. (Some people call them soft links). \n\nMany shell scripts start \n\n```/bin/sh\n```\n\n\nBut most linux distros do not have a program called /bin/sh. Rather /bin/sh is simply a link to bash, dash or some other shell. On sage.math\n\n\n```\nkirkby@sage:~$ ls -l /bin/sh\nlrwxrwxrwx 1 root root 4 2010-02-02 13:49 /bin/sh -> dash\nkirkby@sage:~$ ls -l /bin/dash\n-rwxr-xr-x 1 root root 100856 2009-03-09 06:18 /bin/dash\n```\n\n\nWhen you type 'sh' on sage.math you are really running 'dash'\n\n> Moreover, I don't have admin rights.\n\nYou don't need admin rights to create a symbolic link. Something like:\n\n\n```\n$ ln -s /usr/local/bin/gfortran-4.2 $HOME/bin/gfortran\n```\n\n\nwill do fine. Then make sure $HOME/bin is in your path before /usr/local/bin. Your will then have 'gfortran'. \n\n> I don't have access to Solaris; And I don't have experience with it. But if the GNU suit is installed it should work; if not it won't, but scipy has to blamed for this not fortran itself.\n\n\nDo you have an account on sage.math or similar? If so, you have an account on 't2' - or if not, one is easily created. For all practical purposes you will not find it significantly different from Linux. \n\n> If you can test this on Soloaris I would be happy to integrate any changes you suggest. \n\nUnfortunately, I simply do not have time to test everyones changes on Solaris - let alone generate patches if they do not work. \n\nhttp://www.sagemath.org/doc/developer/inclusion.html\n\nmakes it clear that for a package to be included in Sage, it must support Solaris. \n\n**Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden.**\n\nYour solution seems like a *sledgehammer to crack a walnut* if you know what I mean by that. A symbolic link has far greater chance of just working, without risking breaking things for everyone else. In stead you propose making changes that could impact anyone, without actually testing them. \n\n**I'm marking this as wontfix, as I believe the patch is unnecessary. You may find another reviewer see this differently, though I doubt you will find any experienced system administrator see it that way** \n\nDave",
    "created_at": "2010-02-22T17:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72337",
    "user": "drkirkby"
}
```

Replying to [comment:3 mraum]:
> SAGE_FORTRAN is ignored, if gfortran doesn't exist. 

> Namely, the script will abort. That's why I had to create a patch. Creating links for gfortran is a hack would most probably create new problems anywhere else at another time. 

What makes you think a symbolic link is a hack? It is very standard practice on Unix systems to create symbolic links for this very purpose. There are loads of them created in Sage. (Some people call them soft links). 

Many shell scripts start 

```/bin/sh
```


But most linux distros do not have a program called /bin/sh. Rather /bin/sh is simply a link to bash, dash or some other shell. On sage.math


```
kirkby@sage:~$ ls -l /bin/sh
lrwxrwxrwx 1 root root 4 2010-02-02 13:49 /bin/sh -> dash
kirkby@sage:~$ ls -l /bin/dash
-rwxr-xr-x 1 root root 100856 2009-03-09 06:18 /bin/dash
```


When you type 'sh' on sage.math you are really running 'dash'

> Moreover, I don't have admin rights.

You don't need admin rights to create a symbolic link. Something like:


```
$ ln -s /usr/local/bin/gfortran-4.2 $HOME/bin/gfortran
```


will do fine. Then make sure $HOME/bin is in your path before /usr/local/bin. Your will then have 'gfortran'. 

> I don't have access to Solaris; And I don't have experience with it. But if the GNU suit is installed it should work; if not it won't, but scipy has to blamed for this not fortran itself.


Do you have an account on sage.math or similar? If so, you have an account on 't2' - or if not, one is easily created. For all practical purposes you will not find it significantly different from Linux. 

> If you can test this on Soloaris I would be happy to integrate any changes you suggest. 

Unfortunately, I simply do not have time to test everyones changes on Solaris - let alone generate patches if they do not work. 

http://www.sagemath.org/doc/developer/inclusion.html

makes it clear that for a package to be included in Sage, it must support Solaris. 

**Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden.**

Your solution seems like a *sledgehammer to crack a walnut* if you know what I mean by that. A symbolic link has far greater chance of just working, without risking breaking things for everyone else. In stead you propose making changes that could impact anyone, without actually testing them. 

**I'm marking this as wontfix, as I believe the patch is unnecessary. You may find another reviewer see this differently, though I doubt you will find any experienced system administrator see it that way** 

Dave



---

archive/issue_comments_072338.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-22T17:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72338",
    "user": "drkirkby"
}
```

Resolution: wontfix



---

archive/issue_comments_072339.json:
```json
{
    "body": "Dave, please have a look at the trac guidelines:\n\nhttp://wiki.sagemath.org/devel/TracGuidelines\n\nMore specifically, the paragraph about closing tickets: \"No Closing Or Invalidating: Unless you have admin powers in trac (which includes all the people who have ever done releases of Sage), do not close tickets unless you are explicitly told to do so. Since we have email notification now this has become less of an issue. If you think that a ticket is invalid or has been fixed, just comment on it and the current release manager will take a look and close it if appropriate.\"",
    "created_at": "2010-02-22T22:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72339",
    "user": "@aghitza"
}
```

Dave, please have a look at the trac guidelines:

http://wiki.sagemath.org/devel/TracGuidelines

More specifically, the paragraph about closing tickets: "No Closing Or Invalidating: Unless you have admin powers in trac (which includes all the people who have ever done releases of Sage), do not close tickets unless you are explicitly told to do so. Since we have email notification now this has become less of an issue. If you think that a ticket is invalid or has been fixed, just comment on it and the current release manager will take a look and close it if appropriate."



---

archive/issue_comments_072340.json:
```json
{
    "body": "Thank you Minh. I was not aware of that. \n\nDave",
    "created_at": "2010-02-22T23:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72340",
    "user": "drkirkby"
}
```

Thank you Minh. I was not aware of that. 

Dave



---

archive/issue_comments_072341.json:
```json
{
    "body": "Minh, I just realised I left this as closed. Perhaps you can open it and select what you feel is most appropriate - needs work/ need review/ wontfix etc. \n\nSorry for the problem, but I do feel this ticket is potentially risky, untested, and is almost certainly better served by creating a symbolic link. \n\nDave",
    "created_at": "2010-02-22T23:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72341",
    "user": "drkirkby"
}
```

Minh, I just realised I left this as closed. Perhaps you can open it and select what you feel is most appropriate - needs work/ need review/ wontfix etc. 

Sorry for the problem, but I do feel this ticket is potentially risky, untested, and is almost certainly better served by creating a symbolic link. 

Dave



---

archive/issue_comments_072342.json:
```json
{
    "body": "Oops, I realised it was Alex this pointed out this policy, not Minh. \n\nAnyway, Sorry for the problem. I still stand by the fact I do not think the patch should be integrated. \n\nDave",
    "created_at": "2010-02-22T23:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72342",
    "user": "drkirkby"
}
```

Oops, I realised it was Alex this pointed out this policy, not Minh. 

Anyway, Sorry for the problem. I still stand by the fact I do not think the patch should be integrated. 

Dave



---

archive/issue_comments_072343.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> Minh, I just realised I left this as closed. Perhaps you can open it and select what you feel is most appropriate - needs work/ need review/ wontfix etc. \n\nI'm leaving this as \"wontfix\". If there's a need in the future to address this issue again, open another ticket, but refrain from reopening tickets. A few months ago, only trac administrators had power to close tickets. After some changes to trac, in particular moving to the new process for working on tickets, every suddenly has the power to close tickets. This is the source of the \"every can close tickets\" problem we're seeing right now.",
    "created_at": "2010-02-23T02:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72343",
    "user": "mvngu"
}
```

Replying to [comment:7 drkirkby]:
> Minh, I just realised I left this as closed. Perhaps you can open it and select what you feel is most appropriate - needs work/ need review/ wontfix etc. 

I'm leaving this as "wontfix". If there's a need in the future to address this issue again, open another ticket, but refrain from reopening tickets. A few months ago, only trac administrators had power to close tickets. After some changes to trac, in particular moving to the new process for working on tickets, every suddenly has the power to close tickets. This is the source of the "every can close tickets" problem we're seeing right now.



---

archive/issue_comments_072344.json:
```json
{
    "body": "Replying to [comment:9 mvngu]:\n> \"every can close tickets\" problem we're seeing right now.\n\n\"everyone\", that is.",
    "created_at": "2010-02-23T02:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8201",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8201#issuecomment-72344",
    "user": "mvngu"
}
```

Replying to [comment:9 mvngu]:
> "every can close tickets" problem we're seeing right now.

"everyone", that is.
