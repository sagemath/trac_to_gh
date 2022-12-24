# Issue 9856: Upgrade biopython to version 1.55 (released Augest 31, 2010)

archive/issues_009856.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mhansen mvngu schilly\n\nKeywords: biopython\n\nBiopython is actively maintained and this latest release comes closer to supporting python 3.0.  It also improves some command-line utilities and other miscellaneous improvements.\n\nAn spkg is available at:\nhttp://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/9857\n\n",
    "created_at": "2010-09-04T20:31:05Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Upgrade biopython to version 1.55 (released Augest 31, 2010)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9856",
    "user": "mhampton"
}
```
Assignee: tbd

CC:  mhansen mvngu schilly

Keywords: biopython

Biopython is actively maintained and this latest release comes closer to supporting python 3.0.  It also improves some command-line utilities and other miscellaneous improvements.

An spkg is available at:
http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg

Issue created by migration from https://trac.sagemath.org/ticket/9857





---

archive/issue_comments_097296.json:
```json
{
    "body": "Hi,\n\nThe patch is no longer needed and should be removed. The test in the src/Bio/Wise/__init__.py has been improved to test if the test is being run from a tty. The tests now passes when run using export SAGE_CHECK=\"yes\". \n\nAdam",
    "created_at": "2010-09-16T14:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97296",
    "user": "awebb"
}
```

Hi,

The patch is no longer needed and should be removed. The test in the src/Bio/Wise/__init__.py has been improved to test if the test is being run from a tty. The tests now passes when run using export SAGE_CHECK="yes". 

Adam



---

archive/issue_comments_097297.json:
```json
{
    "body": "Thanks for looking at this.  I removed the patch directory, removed the change from the spkg-install, and updated SPKG.txt to note this.  I also added you as a spkg maintainer.  \n\nI just over-wrote the same file at [http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg](http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg) with these changes.",
    "created_at": "2010-09-16T18:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97297",
    "user": "mhampton"
}
```

Thanks for looking at this.  I removed the patch directory, removed the change from the spkg-install, and updated SPKG.txt to note this.  I also added you as a spkg maintainer.  

I just over-wrote the same file at [http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg](http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg) with these changes.



---

archive/issue_comments_097298.json:
```json
{
    "body": "I just ran the tests and got the old failures from the Wise module, so this doesn't seem to be fixed after all unless I'm missing something.",
    "created_at": "2010-09-16T20:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97298",
    "user": "mhampton"
}
```

I just ran the tests and got the old failures from the Wise module, so this doesn't seem to be fixed after all unless I'm missing something.



---

archive/issue_comments_097299.json:
```json
{
    "body": "Unfortunately, I haven't been able to duplicate that. I get:\n\n```\ntest_Wise ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.\ntest_psw ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.\n```\n\nbut I think this is expected as I don't have Wise2 installed. I also get:\n\n```\nBio.Wise docstring test ... ok\nBio.Wise.psw docstring test ... ok\n```\n\nWhat I did was to run the commands:\n\n```\nexport SAGE_CHECK=\"yes\"\nsage -f biopython-1.55.p0.spkg\n```\n\nI noticed that that previous installed version was not overwritten. I then removed the directory and did the install again. This time the new file was present. The tests again passed. \n\nHow did you run the tests?\n\nAdam",
    "created_at": "2010-09-17T12:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97299",
    "user": "awebb"
}
```

Unfortunately, I haven't been able to duplicate that. I get:

```
test_Wise ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.
test_psw ... skipping. Install Wise2 (dnal) if you want to use Bio.Wise.
```

but I think this is expected as I don't have Wise2 installed. I also get:

```
Bio.Wise docstring test ... ok
Bio.Wise.psw docstring test ... ok
```

What I did was to run the commands:

```
export SAGE_CHECK="yes"
sage -f biopython-1.55.p0.spkg
```

I noticed that that previous installed version was not overwritten. I then removed the directory and did the install again. This time the new file was present. The tests again passed. 

How did you run the tests?

Adam



---

archive/issue_comments_097300.json:
```json
{
    "body": "I tried this from scratch and it worked as expected (as you reported above).  So it must have been a problem with not over-writing something.  I will double-check on a different machine today but I think things are OK as is.",
    "created_at": "2010-09-17T12:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97300",
    "user": "mhampton"
}
```

I tried this from scratch and it worked as expected (as you reported above).  So it must have been a problem with not over-writing something.  I will double-check on a different machine today but I think things are OK as is.



---

archive/issue_comments_097301.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T12:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97301",
    "user": "mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097302.json:
```json
{
    "body": "I have had this sort of problem with python distutils before. Old versions are not written over even though the files have changed. My guess is that the root of the problem is that the old version is not removed first. It is very easy to end up with an install that is a mixture of versions this way.",
    "created_at": "2010-09-17T13:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97302",
    "user": "awebb"
}
```

I have had this sort of problem with python distutils before. Old versions are not written over even though the files have changed. My guess is that the root of the problem is that the old version is not removed first. It is very easy to end up with an install that is a mixture of versions this way.



---

archive/issue_comments_097303.json:
```json
{
    "body": "The package looks fine to me. I guess I should I have an email; maxthemouse at googlemail dot com.",
    "created_at": "2010-09-18T12:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97303",
    "user": "awebb"
}
```

The package looks fine to me. I guess I should I have an email; maxthemouse at googlemail dot com.



---

archive/issue_comments_097304.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-21T10:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97304",
    "user": "awebb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097305.json:
```json
{
    "body": "Mike, Minh, or Harald, could one of you please merge \n\n http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg\n\ninto the optional packages repository?",
    "created_at": "2010-09-28T09:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97305",
    "user": "mpatel"
}
```

Mike, Minh, or Harald, could one of you please merge 

 http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg

into the optional packages repository?



---

archive/issue_comments_097306.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> Mike, Minh, or Harald, could one of you please merge \n> http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg\n> into the optional packages repository?\n\nDone.",
    "created_at": "2010-09-28T09:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97306",
    "user": "schilly"
}
```

Replying to [comment:10 mpatel]:
> Mike, Minh, or Harald, could one of you please merge 
> http://sage.math.washington.edu/home/mhampton/biopython-1.55.p0.spkg
> into the optional packages repository?

Done.



---

archive/issue_comments_097307.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-09-28T09:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97307",
    "user": "mpatel"
}
```

Thanks!



---

archive/issue_comments_097308.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9856#issuecomment-97308",
    "user": "mpatel"
}
```

Resolution: fixed
