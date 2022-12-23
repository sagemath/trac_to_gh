# Issue 4880: [with spkg, needs review] Improved experimental spkg vtk-5.2

archive/issues_004880.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  schilly\n\nMade vtk-5.2 more fashionable:\n\n* moved VTK and VTKData to src/\n\n* test for the installation of cmake-2.4.8 If it is not installed, we install it.\n\n[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.spkg)\n\nNo changes IN VTK and VTKData\n\nSomebody should look into spkg-install and make it work on OSX.\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/4880\n\n",
    "created_at": "2008-12-26T15:15:28Z",
    "labels": [
        "packages: experimental",
        "minor",
        "enhancement"
    ],
    "title": "[with spkg, needs review] Improved experimental spkg vtk-5.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4880",
    "user": "jsp"
}
```
Assignee: mabshoff

CC:  schilly

Made vtk-5.2 more fashionable:

* moved VTK and VTKData to src/

* test for the installation of cmake-2.4.8 If it is not installed, we install it.

[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.spkg)

No changes IN VTK and VTKData

Somebody should look into spkg-install and make it work on OSX.

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/4880





---

archive/issue_comments_036958.json:
```json
{
    "body": "This worked great for me, and I belive for Jason Grout.  I vote in favor of promoting this version to experimental  (I compiled and used the package, but did not look at the spkg.)",
    "created_at": "2009-02-04T05:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36958",
    "user": "cwitty"
}
```

This worked great for me, and I belive for Jason Grout.  I vote in favor of promoting this version to experimental  (I compiled and used the package, but did not look at the spkg.)



---

archive/issue_comments_036959.json:
```json
{
    "body": "Harald, \n\nwhat is the status of adding spkgs to the repo? Should I wait until we switch before uploading this?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-07T01:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36959",
    "user": "mabshoff"
}
```

Harald, 

what is the status of adding spkgs to the repo? Should I wait until we switch before uploading this?

Cheers,

Michael



---

archive/issue_comments_036960.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> what is the status of adding spkgs to the repo? Should I wait until we switch before uploading this?\n> \n\nwell, i'm not sure, the new server shouldn't change any more so i would suggest to upload it on the new server, same place and everything like with the old one, and it just takes some days until it is public. (or upload it on both?)",
    "created_at": "2009-02-07T11:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36960",
    "user": "schilly"
}
```

Replying to [comment:2 mabshoff]:
> what is the status of adding spkgs to the repo? Should I wait until we switch before uploading this?
> 

well, i'm not sure, the new server shouldn't change any more so i would suggest to upload it on the new server, same place and everything like with the old one, and it just takes some days until it is public. (or upload it on both?)



---

archive/issue_comments_036961.json:
```json
{
    "body": "This is taking way to long!\n\nRemember this is experimental!!!!\n\nThe spkg only change is spkg-install and SPKG.txt, no changes in src!\n\nIn the mean time I have a vtk-5.2.1.spkg\n\nSee:\n[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg)\n\nShould we close this ticket and open a new one?\n\nJaap",
    "created_at": "2009-02-26T19:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36961",
    "user": "jsp"
}
```

This is taking way to long!

Remember this is experimental!!!!

The spkg only change is spkg-install and SPKG.txt, no changes in src!

In the mean time I have a vtk-5.2.1.spkg

See:
[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg)

Should we close this ticket and open a new one?

Jaap



---

archive/issue_comments_036962.json:
```json
{
    "body": "Replying to [comment:4 jsp]:\n\nHi Jaap,\n\n> This is taking way to long!\n\nThe problem was that due to the transition from modular to the new image spkg uploads were frozen. Now that the new server has stabilized things should be moving again and this ticket has been looking accusingly at me to get moving every time I skim the tickets with positive review :)\n\n> Remember this is experimental!!!!\n\nSee above - it has nothing to do with experimental.\n\n> The spkg only change is spkg-install and SPKG.txt, no changes in src!\n> \n> In the mean time I have a vtk-5.2.1.spkg\n> \n> See:\n> [http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg)\n> \n> Should we close this ticket and open a new one?\n\nNo, I just changed the summary and will upload this once I get started merging tonight.\n\n> Jaap\n> \n\nSorry for the delay, it should get better soon and you should have complained more ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T22:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36962",
    "user": "mabshoff"
}
```

Replying to [comment:4 jsp]:

Hi Jaap,

> This is taking way to long!

The problem was that due to the transition from modular to the new image spkg uploads were frozen. Now that the new server has stabilized things should be moving again and this ticket has been looking accusingly at me to get moving every time I skim the tickets with positive review :)

> Remember this is experimental!!!!

See above - it has nothing to do with experimental.

> The spkg only change is spkg-install and SPKG.txt, no changes in src!
> 
> In the mean time I have a vtk-5.2.1.spkg
> 
> See:
> [http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/vtk-5.2.1.spkg)
> 
> Should we close this ticket and open a new one?

No, I just changed the summary and will upload this once I get started merging tonight.

> Jaap
> 

Sorry for the delay, it should get better soon and you should have complained more ;)

Cheers,

Michael



---

archive/issue_comments_036963.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> Replying to [comment:4 jsp]:\n[...]\n> \n> No, I just changed the summary and will upload this once I get started merging tonight.\n> \n> > Jaap\n> > \n> \n> Sorry for the delay, it should get better soon and you should have complained more ;)\n> \n\n\nLet me complain once more!\n\nJaap",
    "created_at": "2009-03-16T13:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36963",
    "user": "jsp"
}
```

Replying to [comment:5 mabshoff]:
> Replying to [comment:4 jsp]:
[...]
> 
> No, I just changed the summary and will upload this once I get started merging tonight.
> 
> > Jaap
> > 
> 
> Sorry for the delay, it should get better soon and you should have complained more ;)
> 


Let me complain once more!

Jaap



---

archive/issue_comments_036964.json:
```json
{
    "body": "Merged in the Sage 3.4.1 release cycle by uploading the vtk-5.2.1.spkg to the experimental spkg repo.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T05:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36964",
    "user": "mabshoff"
}
```

Merged in the Sage 3.4.1 release cycle by uploading the vtk-5.2.1.spkg to the experimental spkg repo.

Cheers,

Michael



---

archive/issue_comments_036965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-01T05:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4880#issuecomment-36965",
    "user": "mabshoff"
}
```

Resolution: fixed
