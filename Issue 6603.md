# Issue 6603: [with SPKG, need review] COIN-OR / CBC for SAGE

archive/issues_006603.json:
```json
{
    "body": "Assignee: jkantor\n\nCBC is a Free ( though not GPL-compatible ) Linear Program and Mixed Integer Program Solver from the COIN-OR suite.\n\nEven though it is not Free and will have to remain an optional package, COIN-OR has performances way above GLPK which is to be used by default in SAGE ( see http://trac.sagemath.org/sage_trac/ticket/6502 and http://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f )\n\nThis SPKG contains the last version of CBC and a Cython class to make it available through numerical.mip when installed.\n\nThe SPKG can be found at this address :\nhttp://www-sop.inria.fr/members/Nathann.Cohen/cbc.spkg\n\nI hope you will like it ! ;-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6603\n\n",
    "created_at": "2009-07-23T14:35:48Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with SPKG, need review] COIN-OR / CBC for SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6603",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

CBC is a Free ( though not GPL-compatible ) Linear Program and Mixed Integer Program Solver from the COIN-OR suite.

Even though it is not Free and will have to remain an optional package, COIN-OR has performances way above GLPK which is to be used by default in SAGE ( see http://trac.sagemath.org/sage_trac/ticket/6502 and http://groups.google.com/group/sage-devel/browse_thread/thread/9da47e06bcdfc49f )

This SPKG contains the last version of CBC and a Cython class to make it available through numerical.mip when installed.

The SPKG can be found at this address :
http://www-sop.inria.fr/members/Nathann.Cohen/cbc.spkg

I hope you will like it ! ;-)

Issue created by migration from https://trac.sagemath.org/ticket/6603





---

archive/issue_comments_053946.json:
```json
{
    "body": "ON an amd64 ubuntu 9.04 machine, I got an error in installationof cbc. Here is the tail:\n\n\n```\n\nmake[2]: Leaving directory `/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3/src'\nmake[1]: Leaving directory `/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3/src'\npython: can't open file 'setup.py': [Errno 2] No such file or directory\n\nreal    12m35.674s\nuser    10m40.044s\nsys     1m53.819s\nsage: An error occurred while installing cbc-2.3\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /home/wdj/sagefiles/sage-4.1.1.alpha0/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3 and type 'make'.\nInstead type \"/home/wdj/sagefiles/sage-4.1.1.alpha0/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n```\n\n\nAny idea what the problem is?",
    "created_at": "2009-07-25T14:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53946",
    "user": "https://github.com/wdjoyner"
}
```

ON an amd64 ubuntu 9.04 machine, I got an error in installationof cbc. Here is the tail:


```

make[2]: Leaving directory `/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3/src'
make[1]: Leaving directory `/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3/src'
python: can't open file 'setup.py': [Errno 2] No such file or directory

real    12m35.674s
user    10m40.044s
sys     1m53.819s
sage: An error occurred while installing cbc-2.3
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wdj/sagefiles/sage-4.1.1.alpha0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3 and type 'make'.
Instead type "/home/wdj/sagefiles/sage-4.1.1.alpha0/sage -sh"
in order to set all environment variables correctly, then cd to
/home/wdj/sagefiles/sage-4.1.1.alpha0/spkg/build/cbc-2.3
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


Any idea what the problem is?



---

archive/issue_comments_053947.json:
```json
{
    "body": "It comes from the fact that I stupidly forgot to add a \"cd ..\" somewhere... I just updated the spkg, it should work a bit better now ;-)",
    "created_at": "2009-07-26T00:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53947",
    "user": "https://github.com/nathanncohen"
}
```

It comes from the fact that I stupidly forgot to add a "cd .." somewhere... I just updated the spkg, it should work a bit better now ;-)



---

archive/issue_comments_053948.json:
```json
{
    "body": "This installs fine on an amd64 ubuntu 9.04 machine and passes sage -testall.\n\nUnless there are further tests to run, I give this a positive review as an optional package.",
    "created_at": "2009-07-27T01:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53948",
    "user": "https://github.com/wdjoyner"
}
```

This installs fine on an amd64 ubuntu 9.04 machine and passes sage -testall.

Unless there are further tests to run, I give this a positive review as an optional package.



---

archive/issue_comments_053949.json:
```json
{
    "body": "This spkg creates a class numerical.MIPCoin, but it is an extension to numerical.MIP ( see http://trac.sagemath.org/sage_trac/ticket/6502 ), and I think the reviewing process of these two files should go in paralell ;-)\n\n( And I also hope there will be nothing to change :-) )",
    "created_at": "2009-07-27T05:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53949",
    "user": "https://github.com/nathanncohen"
}
```

This spkg creates a class numerical.MIPCoin, but it is an extension to numerical.MIP ( see http://trac.sagemath.org/sage_trac/ticket/6502 ), and I think the reviewing process of these two files should go in paralell ;-)

( And I also hope there will be nothing to change :-) )



---

archive/issue_comments_053950.json:
```json
{
    "body": "I just updated the SPKG, which now raises exceptions when the computations are wrong for some reason, and added some bugfixes ;-)",
    "created_at": "2009-07-28T12:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53950",
    "user": "https://github.com/nathanncohen"
}
```

I just updated the SPKG, which now raises exceptions when the computations are wrong for some reason, and added some bugfixes ;-)



---

archive/issue_comments_053951.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-28T12:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53951",
    "user": "https://github.com/nathanncohen"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_053952.json:
```json
{
    "body": "Regarding the problems in #6502, the last thing you said was \"I suggest we wait until 4.1.1 is out.\" \n\nWe are now at 4.1.1.rc0. Would you like more checking done on this ticket? On #6502? Wait for 4.1.1.final to \nretest both?",
    "created_at": "2009-07-30T19:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53952",
    "user": "https://github.com/wdjoyner"
}
```

Regarding the problems in #6502, the last thing you said was "I suggest we wait until 4.1.1 is out." 

We are now at 4.1.1.rc0. Would you like more checking done on this ticket? On #6502? Wait for 4.1.1.final to 
retest both?



---

archive/issue_comments_053953.json:
```json
{
    "body": "The only thing that can be checked on this SPKG for the moment is the installation process. Most of the tests will occur during the reviewing of #6502 .\n\nIt seems you had some problems in #6502 applying the patch I posted, and I thought it may be because I was working on an old version of SAGE. If you are available to review #6502 I would be glad to install a new one and create a new patch for this version, containing all the stuff related to the class mip. It will take some time though, as I have to compile SAGE ( there is no binary version for my distribution ). Do you know how I could download the sources Sage 4.1.1.rc0 ?\n\nAs soon as it will be compiled, you will have the new patch ! ;-)\n\nThank you !",
    "created_at": "2009-07-30T19:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53953",
    "user": "https://github.com/nathanncohen"
}
```

The only thing that can be checked on this SPKG for the moment is the installation process. Most of the tests will occur during the reviewing of #6502 .

It seems you had some problems in #6502 applying the patch I posted, and I thought it may be because I was working on an old version of SAGE. If you are available to review #6502 I would be glad to install a new one and create a new patch for this version, containing all the stuff related to the class mip. It will take some time though, as I have to compile SAGE ( there is no binary version for my distribution ). Do you know how I could download the sources Sage 4.1.1.rc0 ?

As soon as it will be compiled, you will have the new patch ! ;-)

Thank you !



---

archive/issue_comments_053954.json:
```json
{
    "body": "You can find it here: http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.rc0.tar",
    "created_at": "2009-07-30T19:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53954",
    "user": "https://github.com/wdjoyner"
}
```

You can find it here: http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.rc0.tar



---

archive/issue_comments_053955.json:
```json
{
    "body": "I just gave #6502 a positive review. Does that mean this can change to positive as well?",
    "created_at": "2009-08-01T16:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53955",
    "user": "https://github.com/wdjoyner"
}
```

I just gave #6502 a positive review. Does that mean this can change to positive as well?



---

archive/issue_comments_053956.json:
```json
{
    "body": "I just updated the spkg to fix something important that I did not notice because I always worked on Integer programs. I also added an Exception in the case where the user tries to solve() a program without having defined its objective function, but that is all :-)",
    "created_at": "2009-08-01T16:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53956",
    "user": "https://github.com/nathanncohen"
}
```

I just updated the spkg to fix something important that I did not notice because I always worked on Integer programs. I also added an Exception in the case where the user tries to solve() a program without having defined its objective function, but that is all :-)



---

archive/issue_comments_053957.json:
```json
{
    "body": "This cbc-2.3.spkg package installs fine for 4.1.1.a1 on an amd64 ubuntu 9.04 machine and passes sage -testall, except for the known failures (abstract_method.py and lazy_attribute.py).\n\nNathann, can you tell me which existing Sage python or cython files (if any) your package modifies? Does it modify any files in another spkg (other than cbc, I mean)?",
    "created_at": "2009-08-01T23:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53957",
    "user": "https://github.com/wdjoyner"
}
```

This cbc-2.3.spkg package installs fine for 4.1.1.a1 on an amd64 ubuntu 9.04 machine and passes sage -testall, except for the known failures (abstract_method.py and lazy_attribute.py).

Nathann, can you tell me which existing Sage python or cython files (if any) your package modifies? Does it modify any files in another spkg (other than cbc, I mean)?



---

archive/issue_comments_053958.json:
```json
{
    "body": "This spkg just install all the Cbc-related librarires with a regular /configure && make && make install, then installs the class sage.numerical.mipCoin with a setup.py script ( which, if I make no mistake, creates no file except in the build/directory.\n\nIn the end, I'd say this package does not touch a hair of any pre-existing file in Sage ! ;-)",
    "created_at": "2009-08-02T06:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53958",
    "user": "https://github.com/nathanncohen"
}
```

This spkg just install all the Cbc-related librarires with a regular /configure && make && make install, then installs the class sage.numerical.mipCoin with a setup.py script ( which, if I make no mistake, creates no file except in the build/directory.

In the end, I'd say this package does not touch a hair of any pre-existing file in Sage ! ;-)



---

archive/issue_comments_053959.json:
```json
{
    "body": "Okay, thanks.\n\nChanging this to \"positive review\" as an optional package.",
    "created_at": "2009-08-03T14:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53959",
    "user": "https://github.com/wdjoyner"
}
```

Okay, thanks.

Changing this to "positive review" as an optional package.



---

archive/issue_comments_053960.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T08:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53960",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053961.json:
```json
{
    "body": "Merged in optional packages repository. See this page\n\n\n\nhttp://www.sagemath.org/packages/optional/\n\n\n\nand CBC is available at\n\n\n\nhttp://www.sagemath.org/packages/optional/cbc-2.3.spkg",
    "created_at": "2009-09-02T08:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged in optional packages repository. See this page



http://www.sagemath.org/packages/optional/



and CBC is available at



http://www.sagemath.org/packages/optional/cbc-2.3.spkg



---

archive/issue_comments_053962.json:
```json
{
    "body": "Changing component from numerical to optional packages.",
    "created_at": "2009-09-02T08:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53962",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from numerical to optional packages.



---

archive/issue_comments_053963.json:
```json
{
    "body": "[spring pictures](http://top20search.biz/)",
    "created_at": "2010-04-30T11:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6603#issuecomment-53963",
    "user": "https://trac.sagemath.org/admin/accounts/users/bascorp"
}
```

[spring pictures](http://top20search.biz/)
