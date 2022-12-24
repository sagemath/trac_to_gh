# Issue 8116: cython fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set to -m64 globally

archive/issues_008116.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  robertwb\n\nIf $SAGE64 = \"yes\" we need CFLAGS=-m64 on Open Solaris.\n\nPatch coming up.\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/8116\n\n",
    "created_at": "2010-01-29T12:53:27Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "cython fails to build in Open Solaris x64 as 64 bit if CFLAGS is not set to -m64 globally",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8116",
    "user": "jsp"
}
```
Assignee: drkirkby

CC:  robertwb

If $SAGE64 = "yes" we need CFLAGS=-m64 on Open Solaris.

Patch coming up.

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/8116





---

archive/issue_comments_071288.json:
```json
{
    "body": "Attachment [cython-0.12.p0.patch](tarball://root/attachments/some-uuid/ticket8116/cython-0.12.p0.patch) by jsp created at 2010-01-29 13:23:27\n\n[http://boxen.math.washington.edu/home/jsp/ports/cython-0.12.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/cython-0.12.p0.spkg)\n\nThis spkg needs testing on OSX with $SAGE64 = \"yes\"\n\nJaap",
    "created_at": "2010-01-29T13:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71288",
    "user": "jsp"
}
```

Attachment [cython-0.12.p0.patch](tarball://root/attachments/some-uuid/ticket8116/cython-0.12.p0.patch) by jsp created at 2010-01-29 13:23:27

[http://boxen.math.washington.edu/home/jsp/ports/cython-0.12.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/cython-0.12.p0.spkg)

This spkg needs testing on OSX with $SAGE64 = "yes"

Jaap



---

archive/issue_comments_071289.json:
```json
{
    "body": "Changing assignee from drkirkby to jsp.",
    "created_at": "2010-01-29T13:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71289",
    "user": "jsp"
}
```

Changing assignee from drkirkby to jsp.



---

archive/issue_comments_071290.json:
```json
{
    "body": "Changing assignee from jsp to drkirkby.",
    "created_at": "2010-01-29T16:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71290",
    "user": "jsp"
}
```

Changing assignee from jsp to drkirkby.



---

archive/issue_comments_071291.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-29T16:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71291",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071292.json:
```json
{
    "body": "I would not do this. It was setting of CFLAGS in sage-env which caused cython to mis-compile code. This is probably why it was not done in OS X. I do not know how to get cython to build 64-bit, but I do not believe you should set CFLAGS to do so.",
    "created_at": "2010-01-29T18:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71292",
    "user": "drkirkby"
}
```

I would not do this. It was setting of CFLAGS in sage-env which caused cython to mis-compile code. This is probably why it was not done in OS X. I do not know how to get cython to build 64-bit, but I do not believe you should set CFLAGS to do so.



---

archive/issue_comments_071293.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-29T18:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71293",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071294.json:
```json
{
    "body": "Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library?",
    "created_at": "2010-01-29T19:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71294",
    "user": "robertwb"
}
```

Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library?



---

archive/issue_comments_071295.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? \n\nSo if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.\n\nWhy not unset CFLAGS in the Cython spkg-install?\n\nWithout CFLAGS set building cython failes on Open Solaris x64!\n\n*.pyx files? I don't get sage-4.3.1.alpha build :)!\n\nSo let's get Python build correctly on Open Solaris x64!\n\nJaap",
    "created_at": "2010-01-29T20:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71295",
    "user": "jsp"
}
```

Replying to [comment:6 robertwb]:
> Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? 

So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.

Why not unset CFLAGS in the Cython spkg-install?

Without CFLAGS set building cython failes on Open Solaris x64!

*.pyx files? I don't get sage-4.3.1.alpha build :)!

So let's get Python build correctly on Open Solaris x64!

Jaap



---

archive/issue_comments_071296.json:
```json
{
    "body": "Replying to [comment:7 jsp]:\n> Replying to [comment:6 robertwb]:\n> > Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? \n> \n> So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.\n\nYes. Worrying about Cython working before Python is set up correctly is probably going to be an exercise in futility. \n\n> Why not unset CFLAGS in the Cython spkg-install?\n\nFor fear of breaking things. I am not an expert on distutils or building stuff, so for me the safest path is to not change stuff. \n\n> Without CFLAGS set building cython failes on Open Solaris x64!\n\nDo you get a working Cython with CFLAGS set? (If so, it might just be lucky...) What errors do you get otherwise? (I think Cython's supposed to fall back to a pure Python setup if the compile fails, but I could be remembering wrong.)\n\n> *.pyx files? I don't get sage-4.3.1.alpha build :)!\n\nYet :)\n\nI'm just pointing out that whatever issues we're running into here, we'll be running into later with the sage library. \n\n> So let's get Python build correctly on Open Solaris x64!\n\nSounds like the best course of action.",
    "created_at": "2010-01-29T21:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71296",
    "user": "robertwb"
}
```

Replying to [comment:7 jsp]:
> Replying to [comment:6 robertwb]:
> > Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? 
> 
> So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.

Yes. Worrying about Cython working before Python is set up correctly is probably going to be an exercise in futility. 

> Why not unset CFLAGS in the Cython spkg-install?

For fear of breaking things. I am not an expert on distutils or building stuff, so for me the safest path is to not change stuff. 

> Without CFLAGS set building cython failes on Open Solaris x64!

Do you get a working Cython with CFLAGS set? (If so, it might just be lucky...) What errors do you get otherwise? (I think Cython's supposed to fall back to a pure Python setup if the compile fails, but I could be remembering wrong.)

> *.pyx files? I don't get sage-4.3.1.alpha build :)!

Yet :)

I'm just pointing out that whatever issues we're running into here, we'll be running into later with the sage library. 

> So let's get Python build correctly on Open Solaris x64!

Sounds like the best course of action.



---

archive/issue_comments_071297.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> Replying to [comment:7 jsp]:\n> > Replying to [comment:6 robertwb]:\n> > > Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? \n> > \n> > So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.\n> \n> Yes. Worrying about Cython working before Python is set up correctly is probably going to be an exercise in futility. \n>\n\nI do have a working Python! But I don't know it is setup properly :(\n\n\n```\nPython 2.6.4 (r264:75706, Jan 27 2010, 22:37:41) \n[GCC 4.4.2] on sunos5\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\n>>> \n\n```\n\n\n \n> > Why not unset CFLAGS in the Cython spkg-install?\n> \n> For fear of breaking things. I am not an expert on distutils or building stuff, so for me the safest path is to not change stuff. \n> \n\nIf you don't accept CFLAGS set globally, why not?\n\n> > Without CFLAGS set building cython failes on Open Solaris x64!\n> \n> Do you get a working Cython with CFLAGS set? (If so, it might just be lucky...) What errors do you get otherwise? (I think Cython's supposed to fall back to a pure Python setup if the compile fails, but I could be remembering wrong.)\n> \n\nI don't know. It just says it installed successfully :)\n\n\n\n> I'm just pointing out that whatever issues we're running into here, we'll be running into later with the sage library. \n> \n> > So let's get Python build correctly on Open Solaris x64!\n> \n> Sounds like the best course of action. \n\n\nLet's go for it!\n\nJaap",
    "created_at": "2010-01-29T22:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71297",
    "user": "jsp"
}
```

Replying to [comment:8 robertwb]:
> Replying to [comment:7 jsp]:
> > Replying to [comment:6 robertwb]:
> > > Cython gets the flags it needs from distutils (which, if I understand correctly, tries to use the flags that Python itself was built with). Just setting CFLAGS directly can mess this up. Can you post the log of running cython -f with this option? Also, Cython won't compile, do you have any luck with all the .pyx files in the Sage library? 
> > 
> > So if I understand you correctly we need a properly installed Python. I have to hack a bit to get a working Python in Open Solaris.
> 
> Yes. Worrying about Cython working before Python is set up correctly is probably going to be an exercise in futility. 
>

I do have a working Python! But I don't know it is setup properly :(


```
Python 2.6.4 (r264:75706, Jan 27 2010, 22:37:41) 
[GCC 4.4.2] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```


 
> > Why not unset CFLAGS in the Cython spkg-install?
> 
> For fear of breaking things. I am not an expert on distutils or building stuff, so for me the safest path is to not change stuff. 
> 

If you don't accept CFLAGS set globally, why not?

> > Without CFLAGS set building cython failes on Open Solaris x64!
> 
> Do you get a working Cython with CFLAGS set? (If so, it might just be lucky...) What errors do you get otherwise? (I think Cython's supposed to fall back to a pure Python setup if the compile fails, but I could be remembering wrong.)
> 

I don't know. It just says it installed successfully :)



> I'm just pointing out that whatever issues we're running into here, we'll be running into later with the sage library. 
> 
> > So let's get Python build correctly on Open Solaris x64!
> 
> Sounds like the best course of action. 


Let's go for it!

Jaap



---

archive/issue_comments_071298.json:
```json
{
    "body": "Replying to [comment:9 jsp]:\n> If you don't accept CFLAGS set globally, why not?\n\nThis is a distutils question, nothing specific to Cython. Hopefully we can get to the root of the issue, as many packages are \"python setup.py install\"",
    "created_at": "2010-01-29T22:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71298",
    "user": "robertwb"
}
```

Replying to [comment:9 jsp]:
> If you don't accept CFLAGS set globally, why not?

This is a distutils question, nothing specific to Cython. Hopefully we can get to the root of the issue, as many packages are "python setup.py install"



---

archive/issue_comments_071299.json:
```json
{
    "body": "I rebuilt python with in the spkg-install Darwin changed to SunOS.\n\nPython buidls ok now with the right CFLAGS set.\n\nRebuilding cython was ok.\n\nSo in principle problem solved!\n\nI close the ticket as invalid.\n\nJaap",
    "created_at": "2010-01-30T12:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71299",
    "user": "jsp"
}
```

I rebuilt python with in the spkg-install Darwin changed to SunOS.

Python buidls ok now with the right CFLAGS set.

Rebuilding cython was ok.

So in principle problem solved!

I close the ticket as invalid.

Jaap



---

archive/issue_comments_071300.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-30T12:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8116#issuecomment-71300",
    "user": "jsp"
}
```

Resolution: invalid
