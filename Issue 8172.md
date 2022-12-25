# Issue 8172: Support for CPLEX

archive/issues_008172.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @malb @haraldschilly\n\nThis patch enables support for Cplex, when the new package #8171 for CBC is installed. It also includes several lines of documentation to explain how CPLEX can be used, and fixes a bad docstring which I noticed while testing this package :-)\n\nNathann does have access to 't2'. Minh has made it clear the last alpha (4.3.4.alpha1) builds ok on 't2', so testing this should be possible for Nathann. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8172\n\n",
    "closed_at": "2010-04-29T05:16:38Z",
    "created_at": "2010-02-03T13:04:21Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "Support for CPLEX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8172",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

CC:  @malb @haraldschilly

This patch enables support for Cplex, when the new package #8171 for CBC is installed. It also includes several lines of documentation to explain how CPLEX can be used, and fixes a bad docstring which I noticed while testing this package :-)

Nathann does have access to 't2'. Minh has made it clear the last alpha (4.3.4.alpha1) builds ok on 't2', so testing this should be possible for Nathann. 

Issue created by migration from https://trac.sagemath.org/ticket/8172





---

archive/issue_comments_071828.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T13:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71828",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071829.json:
```json
{
    "body": "You are doctesting `solve_coin` in `solve_cplex`",
    "created_at": "2010-02-03T14:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71829",
    "user": "https://github.com/malb"
}
```

You are doctesting `solve_coin` in `solve_cplex`



---

archive/issue_comments_071830.json:
```json
{
    "body": "OOps :-)\n\nThe code from mip_cplex is a pure copy of mip_coin ( I only needed to change the types from OsiCbcSolverInterface to OsiCplexSolverInterface, etc .... )\n\nThis code has already been reviewed, by the way.....\n\nFixed ! Thank you :-)\n\nNathann",
    "created_at": "2010-02-03T14:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71830",
    "user": "https://github.com/nathanncohen"
}
```

OOps :-)

The code from mip_cplex is a pure copy of mip_coin ( I only needed to change the types from OsiCbcSolverInterface to OsiCplexSolverInterface, etc .... )

This code has already been reviewed, by the way.....

Fixed ! Thank you :-)

Nathann



---

archive/issue_comments_071831.json:
```json
{
    "body": "I wonder if we can factor out the differences and this way would make it very very easy to hook up new solvers (with say, some function pointers and such) The redundancy of copying a function does not seem very elegant to me.",
    "created_at": "2010-02-03T14:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71831",
    "user": "https://github.com/malb"
}
```

I wonder if we can factor out the differences and this way would make it very very easy to hook up new solvers (with say, some function pointers and such) The redundancy of copying a function does not seem very elegant to me.



---

archive/issue_comments_071832.json:
```json
{
    "body": "I do not like it either, but this way it answers two other difficulties :\n\n*  Coin me be compiled independently from the presence of CPLEX. So I can not be assume in mip_coin that CPLEX libraries are available and that this file *can* actually be compiled.\n\n*  Testing for the presence of a CPLEX solver amounts to try to import solve_cplex, which is nice and can only be done if the file has been compiled successfully\n\nNathann",
    "created_at": "2010-02-03T14:50:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71832",
    "user": "https://github.com/nathanncohen"
}
```

I do not like it either, but this way it answers two other difficulties :

*  Coin me be compiled independently from the presence of CPLEX. So I can not be assume in mip_coin that CPLEX libraries are available and that this file *can* actually be compiled.

*  Testing for the presence of a CPLEX solver amounts to try to import solve_cplex, which is nice and can only be done if the file has been compiled successfully

Nathann



---

archive/issue_comments_071833.json:
```json
{
    "body": "We could still reduce the amount of code duplication. Say we replace the functions `solve_*` by instances of a class `OSISolver` which would get function pointers pointing to the correct function to call for each solver and have a call method which implements the current `solve_*` function. So for each new solver we'd only need to add a new instance. All the points you raise above would be addressed.",
    "created_at": "2010-02-03T15:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71833",
    "user": "https://github.com/malb"
}
```

We could still reduce the amount of code duplication. Say we replace the functions `solve_*` by instances of a class `OSISolver` which would get function pointers pointing to the correct function to call for each solver and have a call method which implements the current `solve_*` function. So for each new solver we'd only need to add a new instance. All the points you raise above would be addressed.



---

archive/issue_comments_071834.json:
```json
{
    "body": "Hmm.. It is almost done, but I have a few problems with cimporting in mip_cplex the c_solve function defined in mip_coin.... :-)",
    "created_at": "2010-02-03T17:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71834",
    "user": "https://github.com/nathanncohen"
}
```

Hmm.. It is almost done, but I have a few problems with cimporting in mip_cplex the c_solve function defined in mip_coin.... :-)



---

archive/issue_comments_071835.json:
```json
{
    "body": "Ok, I have spent 3 or 4 hours dealing with this bug, if you want to give it a try it is almost finished : we but have to find a way to import this *********** function...\n\nI'm sorry for my rudeness, but I can not stand these stupid error messages anymore !\n\nNathann",
    "created_at": "2010-02-05T17:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71835",
    "user": "https://github.com/nathanncohen"
}
```

Ok, I have spent 3 or 4 hours dealing with this bug, if you want to give it a try it is almost finished : we but have to find a way to import this *********** function...

I'm sorry for my rudeness, but I can not stand these stupid error messages anymore !

Nathann



---

archive/issue_comments_071836.json:
```json
{
    "body": "If you can fix it, I will obviously finish to clean the patch....\n\nNathann",
    "created_at": "2010-02-05T17:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71836",
    "user": "https://github.com/nathanncohen"
}
```

If you can fix it, I will obviously finish to clean the patch....

Nathann



---

archive/issue_comments_071837.json:
```json
{
    "body": "What platforms has this been tested on? It needs to work on OS X, Linux and Solaris. It's not clear from reading this that anyone has actually checked it works on Solaris. \n\nThere's general information about building on Solaris at\n\n  http://wiki.sagemath.org/solaris\n\n Information specifically for 't2' at\n\n  http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\n Both the source (4.3.0.1 is the latest to build on Solaris) and a binary\n which will run on any SPARC can be found at http://www.sagemath.org\n /download-source.html\n\n Dave",
    "created_at": "2010-02-22T00:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71837",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

What platforms has this been tested on? It needs to work on OS X, Linux and Solaris. It's not clear from reading this that anyone has actually checked it works on Solaris. 

There's general information about building on Solaris at

  http://wiki.sagemath.org/solaris

 Information specifically for 't2' at

  http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

 Both the source (4.3.0.1 is the latest to build on Solaris) and a binary
 which will run on any SPARC can be found at http://www.sagemath.org
 /download-source.html

 Dave



---

archive/issue_comments_071838.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-22T00:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71838",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_071839.json:
```json
{
    "body": "Here is a new *WORKING* version of the patch :-)\n\nI received plenty of help, and it can finally be used !!\n\nI can not test this piece of code on all these platforms. Anyway, CPLEX will be used by very few users of Sage as it already requires one to have a licence, which is pretty expensive ! ;-)\n\nNathann",
    "created_at": "2010-02-22T17:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71839",
    "user": "https://github.com/nathanncohen"
}
```

Here is a new *WORKING* version of the patch :-)

I received plenty of help, and it can finally be used !!

I can not test this piece of code on all these platforms. Anyway, CPLEX will be used by very few users of Sage as it already requires one to have a licence, which is pretty expensive ! ;-)

Nathann



---

archive/issue_comments_071840.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-22T17:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71840",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071841.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-25T17:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71841",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071842.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-26T11:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71842",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071843.json:
```json
{
    "body": "New version of this patch... \n\n* It now handles exceptions\n* I added options to have Cbc work multithread when the user wants it\n* I refactored some code which is now much more readable\n* I rounded some values in the docstrings, as Cplex behaves a bit differently from it friends concerning numerical noise\n\nThis patch can now be reviewed, and will be a nice addition whether one uses Cplex or not because of the multithread ! :-)\n\nNathann",
    "created_at": "2010-02-26T11:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71843",
    "user": "https://github.com/nathanncohen"
}
```

New version of this patch... 

* It now handles exceptions
* I added options to have Cbc work multithread when the user wants it
* I refactored some code which is now much more readable
* I rounded some values in the docstrings, as Cplex behaves a bit differently from it friends concerning numerical noise

This patch can now be reviewed, and will be a nice addition whether one uses Cplex or not because of the multithread ! :-)

Nathann



---

archive/issue_comments_071844.json:
```json
{
    "body": "Cplex seems to be freely available for academics and students :\n\nhttp://www.ibm.com/developerworks/forums/thread.jspa?threadID=319342&tstart=0\n\nNathann",
    "created_at": "2010-03-08T15:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71844",
    "user": "https://github.com/nathanncohen"
}
```

Cplex seems to be freely available for academics and students :

http://www.ibm.com/developerworks/forums/thread.jspa?threadID=319342&tstart=0

Nathann



---

archive/issue_comments_071845.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-03-08T16:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71845",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_071846.json:
```json
{
    "body": "I understand you feel this would be useful, especially given CPLEX is available free for academics and students. (I'm neither a student or academic, so can't get a copy free myself). Given CPLEX is available for OSX, Solaris on both SPARC and x86, I believe it would be wise that you test it on those platforms.\n\nYou do have access to 't2' (Solaris) and 'bsd' (OS X) I assume. \n\nTesting on Solaris or OS X is not necessary for an experimental package (I'm not sure about optional), but certainly it would never be accepted as standard if it did not build on Solaris or OS X. I'm not quite sure where this package aims to fit (standard/experiemental/optional). That would dictate whether it needs to build on Solaris and OS X. \n\nI've put to 'need info' so you can clarify this for us. \n\nDave",
    "created_at": "2010-03-08T16:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71846",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I understand you feel this would be useful, especially given CPLEX is available free for academics and students. (I'm neither a student or academic, so can't get a copy free myself). Given CPLEX is available for OSX, Solaris on both SPARC and x86, I believe it would be wise that you test it on those platforms.

You do have access to 't2' (Solaris) and 'bsd' (OS X) I assume. 

Testing on Solaris or OS X is not necessary for an experimental package (I'm not sure about optional), but certainly it would never be accepted as standard if it did not build on Solaris or OS X. I'm not quite sure where this package aims to fit (standard/experiemental/optional). That would dictate whether it needs to build on Solaris and OS X. 

I've put to 'need info' so you can clarify this for us. 

Dave



---

archive/issue_comments_071847.json:
```json
{
    "body": "* it seems you define `ctypedef struct c_OsiSolverInterface \"OsiSolverInterface\"` a few times in a few different files. Why?\n  * CPLEX has a few `# optional - requires Cbc`\n  * Why did you change `log=False` to `log=0`? Also the docstring does not match anymore.\n  * `# a hand-made memset` why don't you just call memset?",
    "created_at": "2010-03-09T16:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71847",
    "user": "https://github.com/malb"
}
```

* it seems you define `ctypedef struct c_OsiSolverInterface "OsiSolverInterface"` a few times in a few different files. Why?
  * CPLEX has a few `# optional - requires Cbc`
  * Why did you change `log=False` to `log=0`? Also the docstring does not match anymore.
  * `# a hand-made memset` why don't you just call memset?



---

archive/issue_comments_071848.json:
```json
{
    "body": "Btw. applies cleanly and builds fine on sage.math",
    "created_at": "2010-03-09T16:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71848",
    "user": "https://github.com/malb"
}
```

Btw. applies cleanly and builds fine on sage.math



---

archive/issue_comments_071849.json:
```json
{
    "body": "Hello !!!\n\n* ctypedef repeated : fixed\n* optional cbc : fixed\n* because Cbc has several levels of output. Cplex too, perhaps, nce I will know how to tune it :-)\n* because I did not know where to find the memset function : fixed\n\nThank you very much for your help ! I just updated the patch :-)\n\nNathann",
    "created_at": "2010-03-09T20:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71849",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

* ctypedef repeated : fixed
* optional cbc : fixed
* because Cbc has several levels of output. Cplex too, perhaps, nce I will know how to tune it :-)
* because I did not know where to find the memset function : fixed

Thank you very much for your help ! I just updated the patch :-)

Nathann



---

archive/issue_comments_071850.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-03-09T20:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71850",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071851.json:
```json
{
    "body": "About tests on other platforms : Cbc, GLPK and obviously CPLEX will never be made standard packages because of license incompatibilities. I am still looking for a totally free solver but haven't found one yet, nor do I hope to ever find (an efficient) one.\n\nI am really sorry but I can not say I will find the time to test them on these platforms. I do not know them, and even if it worked I have no idea of how to make platform-dependent fixes... :-/\n\nNathann",
    "created_at": "2010-03-09T20:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71851",
    "user": "https://github.com/nathanncohen"
}
```

About tests on other platforms : Cbc, GLPK and obviously CPLEX will never be made standard packages because of license incompatibilities. I am still looking for a totally free solver but haven't found one yet, nor do I hope to ever find (an efficient) one.

I am really sorry but I can not say I will find the time to test them on these platforms. I do not know them, and even if it worked I have no idea of how to make platform-dependent fixes... :-/

Nathann



---

archive/issue_comments_071852.json:
```json
{
    "body": "I just ran doctests on OSX (32-bit I think, its bsd.math). I think we should only worry about the patch on all platforms. If the optional package fails on say Solaris we can deal with this later.",
    "created_at": "2010-03-10T11:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71852",
    "user": "https://github.com/malb"
}
```

I just ran doctests on OSX (32-bit I think, its bsd.math). I think we should only worry about the patch on all platforms. If the optional package fails on say Solaris we can deal with this later.



---

archive/issue_comments_071853.json:
```json
{
    "body": "Can we allow the same number of threads parameter for CPLEX?",
    "created_at": "2010-03-10T11:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71853",
    "user": "https://github.com/malb"
}
```

Can we allow the same number of threads parameter for CPLEX?



---

archive/issue_comments_071854.json:
```json
{
    "body": "I have to admit I do not know... The function I use to set Coin to n threads is Coin-specific. Cplex is used through the Osi interface, which is a good way to quickly add new solvers, but also means that I can not access a solver-specific function when the interface does not let me do it.\n\nOn the other side, Cplex is not free, and the multithreaded version is even more expensive. I have no access to a multithreaded version, but I sent a request for a free licence and I am still waiting for the answer ... With a bit of luck, the licence will let me use this mode and I will be able to take a more serious look at it :-)\n\nNathann",
    "created_at": "2010-03-10T11:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71854",
    "user": "https://github.com/nathanncohen"
}
```

I have to admit I do not know... The function I use to set Coin to n threads is Coin-specific. Cplex is used through the Osi interface, which is a good way to quickly add new solvers, but also means that I can not access a solver-specific function when the interface does not let me do it.

On the other side, Cplex is not free, and the multithreaded version is even more expensive. I have no access to a multithreaded version, but I sent a request for a free licence and I am still waiting for the answer ... With a bit of luck, the licence will let me use this mode and I will be able to take a more serious look at it :-)

Nathann



---

archive/issue_comments_071855.json:
```json
{
    "body": "Dave, do you object if we give this ticket a positive review?",
    "created_at": "2010-03-10T12:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71855",
    "user": "https://github.com/malb"
}
```

Dave, do you object if we give this ticket a positive review?



---

archive/issue_comments_071856.json:
```json
{
    "body": "Replying to [comment:23 malb]:\n> Dave, do you object if we give this ticket a positive review?\n\n\nSince it is optional, I think this can go without it building on Solaris. But I would draw Nathann's attention to the developers guide, in particular:\n\nhttp://www.sagemath.org/doc/developer/inclusion.html?highlight=solaris\n\n**Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden.**\n\nHowever, since this is not a standard package, then I think it can go. \n\nIt was not clear to me on the #8171 whether that was intended to be experimental or optional. I believe the requirements for optional are more stringent than experimental, but I don't know exactly that they are. I believe Building on Solaris and OS X might be a requirement for optional, but are certainly not for experimental. I think that point needs clarification at some point in the future. \n\nI'm feel unable to review this, as it is outside my area, so if Micheal feels it deserves a positive review, then go ahead, but do not put my name on it. \n\nNote also the \"Author\" field is not completed.\n\nDave",
    "created_at": "2010-03-10T23:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71856",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:23 malb]:
> Dave, do you object if we give this ticket a positive review?


Since it is optional, I think this can go without it building on Solaris. But I would draw Nathann's attention to the developers guide, in particular:

http://www.sagemath.org/doc/developer/inclusion.html?highlight=solaris

**Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden.**

However, since this is not a standard package, then I think it can go. 

It was not clear to me on the #8171 whether that was intended to be experimental or optional. I believe the requirements for optional are more stringent than experimental, but I don't know exactly that they are. I believe Building on Solaris and OS X might be a requirement for optional, but are certainly not for experimental. I think that point needs clarification at some point in the future. 

I'm feel unable to review this, as it is outside my area, so if Micheal feels it deserves a positive review, then go ahead, but do not put my name on it. 

Note also the "Author" field is not completed.

Dave



---

archive/issue_comments_071857.json:
```json
{
    "body": "A couple of points which I believe are important before this gets a positive review. \n\n* The patch is based on #8171, which at the very least needs clarification as to whether it is optional or experimental. Despite being a new package, it starts with .p2. I've asked for clarification on whether #8171 is expected to be 'experimental' or 'optional'. \n\n* I've asked on sage-devel for clarification of whether building on Solaris is a requirement for optional packages. If so, (as I expect it is), then I believe that package (and this patch) should be checked on Solaris before getting a positive review.",
    "created_at": "2010-03-11T11:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71857",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

A couple of points which I believe are important before this gets a positive review. 

* The patch is based on #8171, which at the very least needs clarification as to whether it is optional or experimental. Despite being a new package, it starts with .p2. I've asked for clarification on whether #8171 is expected to be 'experimental' or 'optional'. 

* I've asked on sage-devel for clarification of whether building on Solaris is a requirement for optional packages. If so, (as I expect it is), then I believe that package (and this patch) should be checked on Solaris before getting a positive review.



---

archive/issue_comments_071858.json:
```json
{
    "body": "Hello !!\n\nAs Martin mentionned it on #8171, the Cbc package is to be optional, exactly as it currently is. After all, #8171 is just an update. The .p2 is present precisely because it is an update. I hesitated before writing it, though, as the version of Cbc also changed. Do we increase the p# when the version of the source is fixed, and change it otherwise ? As the source changed (I updated it), do I need to \"go back\" to p0 ?\n\nTo be frank, I have in the end no idea of what exactly Solaris is. I know I can check it on the internet very quickly, and this is exactly what I intend to do, but in the end this is where my knowledge of it will stop. I have absolutely no idea how to deal with it...\n\nNathann",
    "created_at": "2010-03-11T12:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71858",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!

As Martin mentionned it on #8171, the Cbc package is to be optional, exactly as it currently is. After all, #8171 is just an update. The .p2 is present precisely because it is an update. I hesitated before writing it, though, as the version of Cbc also changed. Do we increase the p# when the version of the source is fixed, and change it otherwise ? As the source changed (I updated it), do I need to "go back" to p0 ?

To be frank, I have in the end no idea of what exactly Solaris is. I know I can check it on the internet very quickly, and this is exactly what I intend to do, but in the end this is where my knowledge of it will stop. I have absolutely no idea how to deal with it...

Nathann



---

archive/issue_comments_071859.json:
```json
{
    "body": "Replying to [comment:26 ncohen]:\n> Hello !!\n> \n> As Martin mentionned it on #8171, the Cbc package is to be optional, exactly as it currently is. After all, #8171 is just an update. The .p2 is present precisely because it is an update. I hesitated before writing it, though, as the version of Cbc also changed. Do we increase the p# when the version of the source is fixed, and change it otherwise ? As the source changed (I updated it), do I need to \"go back\" to p0 ?\n\n\nNeither. See:\n\nhttp://www.sagemath.org/doc/developer/patching_spkgs.html\n\nIf the version is changed from the upstream source code, then the new package should be called by that version number, and nothing else - not even p0. Once the first patch to that is made, it becomes p0. \n\n> \n> To be frank, I have in the end no idea of what exactly Solaris is. I know I can check it on the internet very quickly, and this is exactly what I intend to do, but in the end this is where my knowledge of it will stop. I have absolutely no idea how to deal with it...\n> \n> Nathann\n\n\nSolaris is a Unix operating system. Unlike Linux, which is a Unix-like operating system, Solaris is officially classified as a POSIX compliant Unix operating system. It was created by Sun, who were recently bought by Oracle for $7 billion. Sage builds on Solaris 10 and soon will be an officially supported operating system, just as some linux distributions are. \n\n't2', which people refer to is a Sun T5240 machine with two SPARC processors. (The SPARC processor is similar to the Intel/AMD processors, though not identical). Each processor has 64-threads (128 in total). \n\nFor any package to become a standard part of Sage, then it will need to build on Solaris 10 on SPARC. I'm unsure of the situation with optional packages. I don't mind helping if you have specific problems, but I am not going to do all the testing for you. \n\nWhen I checked the IBM web site, the library was available for Solaris. \n\ndave",
    "created_at": "2010-03-11T14:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71859",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:26 ncohen]:
> Hello !!
> 
> As Martin mentionned it on #8171, the Cbc package is to be optional, exactly as it currently is. After all, #8171 is just an update. The .p2 is present precisely because it is an update. I hesitated before writing it, though, as the version of Cbc also changed. Do we increase the p# when the version of the source is fixed, and change it otherwise ? As the source changed (I updated it), do I need to "go back" to p0 ?


Neither. See:

http://www.sagemath.org/doc/developer/patching_spkgs.html

If the version is changed from the upstream source code, then the new package should be called by that version number, and nothing else - not even p0. Once the first patch to that is made, it becomes p0. 

> 
> To be frank, I have in the end no idea of what exactly Solaris is. I know I can check it on the internet very quickly, and this is exactly what I intend to do, but in the end this is where my knowledge of it will stop. I have absolutely no idea how to deal with it...
> 
> Nathann


Solaris is a Unix operating system. Unlike Linux, which is a Unix-like operating system, Solaris is officially classified as a POSIX compliant Unix operating system. It was created by Sun, who were recently bought by Oracle for $7 billion. Sage builds on Solaris 10 and soon will be an officially supported operating system, just as some linux distributions are. 

't2', which people refer to is a Sun T5240 machine with two SPARC processors. (The SPARC processor is similar to the Intel/AMD processors, though not identical). Each processor has 64-threads (128 in total). 

For any package to become a standard part of Sage, then it will need to build on Solaris 10 on SPARC. I'm unsure of the situation with optional packages. I don't mind helping if you have specific problems, but I am not going to do all the testing for you. 

When I checked the IBM web site, the library was available for Solaris. 

dave



---

archive/issue_comments_071860.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-11T18:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71860",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071861.json:
```json
{
    "body": "Hello !\n\nI just tried to log on t2 but my password was refused. This is a bit weird as I should not even be asked for a password as I set my ssh key in authorized_keys, but it looks like this server does not know me. Is there something special to do to log on it which is different from the procedure applied for sage.math ?\n\nNathann",
    "created_at": "2010-03-12T08:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71861",
    "user": "https://github.com/nathanncohen"
}
```

Hello !

I just tried to log on t2 but my password was refused. This is a bit weird as I should not even be asked for a password as I set my ssh key in authorized_keys, but it looks like this server does not know me. Is there something special to do to log on it which is different from the procedure applied for sage.math ?

Nathann



---

archive/issue_comments_071862.json:
```json
{
    "body": "Hi,\ndo you understand how to request an \"academic\" license for CPLEX?\n\nI went to the IBM website and registered as an academic user and downloaded\nthe stuff, and can even compile and link CPLEX examples, but I cannot figure out where and how to get a licence (it does not come with the download...)\nThanks,\nDima",
    "created_at": "2010-03-20T04:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71862",
    "user": "https://github.com/dimpase"
}
```

Hi,
do you understand how to request an "academic" license for CPLEX?

I went to the IBM website and registered as an academic user and downloaded
the stuff, and can even compile and link CPLEX examples, but I cannot figure out where and how to get a licence (it does not come with the download...)
Thanks,
Dima



---

archive/issue_comments_071863.json:
```json
{
    "body": "Replying to [comment:30 dimpase]:\n> Hi,\n> do you understand how to request an \"academic\" license for CPLEX?\n\n\nOK, I figured it out:\nhere are the details:\n\n[http://download.boulder.ibm.com/ibmdl/pub/software/dw/university/support/ILOGQuickStart.pdf](http://download.boulder.ibm.com/ibmdl/pub/software/dw/university/support/ILOGQuickStart.pdf)\n\nFirst, one has to register here:\n[https://www.ibm.com/developerworks/university/software/get_software.html](https://www.ibm.com/developerworks/university/software/get_software.html)\n\nand after somewhat tedious registration get to download a zip archive, that\ncontains tarballs of several Linux, MacOS, and Solaris binary installations.\nInstall the right tarball somewhere.\n\nLicence can be requested here:\n[https://www.ibm.com/developerworks/university/support/ilog.html](https://www.ibm.com/developerworks/university/support/ilog.html)\n\nyou will get a file named access.ilm that you e.g. can place into /usr/ilog/ilm/\n(or you can go for a custom location and an environment variable to hold it (see the quickstart pdf linked above)\n\nDima",
    "created_at": "2010-03-20T05:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71863",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:30 dimpase]:
> Hi,
> do you understand how to request an "academic" license for CPLEX?


OK, I figured it out:
here are the details:

[http://download.boulder.ibm.com/ibmdl/pub/software/dw/university/support/ILOGQuickStart.pdf](http://download.boulder.ibm.com/ibmdl/pub/software/dw/university/support/ILOGQuickStart.pdf)

First, one has to register here:
[https://www.ibm.com/developerworks/university/software/get_software.html](https://www.ibm.com/developerworks/university/software/get_software.html)

and after somewhat tedious registration get to download a zip archive, that
contains tarballs of several Linux, MacOS, and Solaris binary installations.
Install the right tarball somewhere.

Licence can be requested here:
[https://www.ibm.com/developerworks/university/support/ilog.html](https://www.ibm.com/developerworks/university/support/ilog.html)

you will get a file named access.ilm that you e.g. can place into /usr/ilog/ilm/
(or you can go for a custom location and an environment variable to hold it (see the quickstart pdf linked above)

Dima



---

archive/issue_comments_071864.json:
```json
{
    "body": "From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.\n\nNathann",
    "created_at": "2010-03-20T11:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71864",
    "user": "https://github.com/nathanncohen"
}
```

From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.

Nathann



---

archive/issue_comments_071865.json:
```json
{
    "body": "Replying to [comment:32 ncohen]:\n> From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.\n> \n> Nathann\n\n\nworks for me with the free academic CPLEX license on Linux x86_64 Debian!",
    "created_at": "2010-04-09T05:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71865",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:32 ncohen]:
> From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.
> 
> Nathann


works for me with the free academic CPLEX license on Linux x86_64 Debian!



---

archive/issue_comments_071866.json:
```json
{
    "body": "fixed few places where \"Mixed Integer\" was omitted",
    "created_at": "2010-04-09T06:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71866",
    "user": "https://github.com/dimpase"
}
```

fixed few places where "Mixed Integer" was omitted



---

archive/issue_comments_071867.json:
```json
{
    "body": "Attachment [trac_8172-updated.patch](tarball://root/attachments/some-uuid/ticket8172/trac_8172-updated.patch) by @dimpase created at 2010-04-09 06:38:28\n\nReplying to [comment:33 dimpase]:\n> Replying to [comment:32 ncohen]:\n> > From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.\n> > \n> > Nathann\n\n> \n> works for me with the free academic CPLEX license on Linux x86_64 Debian!\n\n\nGood work!\nI am giving it a positive review, subject to the patch being updated to the one I just uploaded (that adds Mixed Integer here and there, to avoid a confusion stemming from the fact that Sage does have an LP solver, from cvxopt)\n\nDima",
    "created_at": "2010-04-09T06:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71867",
    "user": "https://github.com/dimpase"
}
```

Attachment [trac_8172-updated.patch](tarball://root/attachments/some-uuid/ticket8172/trac_8172-updated.patch) by @dimpase created at 2010-04-09 06:38:28

Replying to [comment:33 dimpase]:
> Replying to [comment:32 ncohen]:
> > From the tests done in my lab since we are using this new license ( we were using CPLEX 10 before ), this one is *much* faster, especially for integer multiflows.
> > 
> > Nathann

> 
> works for me with the free academic CPLEX license on Linux x86_64 Debian!


Good work!
I am giving it a positive review, subject to the patch being updated to the one I just uploaded (that adds Mixed Integer here and there, to avoid a confusion stemming from the fact that Sage does have an LP solver, from cvxopt)

Dima



---

archive/issue_comments_071868.json:
```json
{
    "body": "Excellent ! I looked at the result of \"diff\" on the two patches, and I agree with your changes ! :-)\n\nNathann",
    "created_at": "2010-04-09T07:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71868",
    "user": "https://github.com/nathanncohen"
}
```

Excellent ! I looked at the result of "diff" on the two patches, and I agree with your changes ! :-)

Nathann



---

archive/issue_comments_071869.json:
```json
{
    "body": "Now the two patches are the same, just to avoid confusion... ;-)\n\nNathann",
    "created_at": "2010-04-09T07:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71869",
    "user": "https://github.com/nathanncohen"
}
```

Now the two patches are the same, just to avoid confusion... ;-)

Nathann



---

archive/issue_events_019573.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-29T05:16:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8172#event-19573"
}
```



---

archive/issue_comments_071870.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71870",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_071871.json:
```json
{
    "body": "Attachment [trac_8172.patch](tarball://root/attachments/some-uuid/ticket8172/trac_8172.patch) by @williamstein created at 2010-04-29 05:16:38",
    "created_at": "2010-04-29T05:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8172#issuecomment-71871",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8172.patch](tarball://root/attachments/some-uuid/ticket8172/trac_8172.patch) by @williamstein created at 2010-04-29 05:16:38
