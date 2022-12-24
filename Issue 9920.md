# Issue 9920: nose testing suite as an optional spkg

archive/issues_009920.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby @jhpalmieri\n\nSeveral projects we depend on use nose to do self-tests.  In order to test these packages, we'd have to have nose installed.\n\nThis is fairly simple without an spkg:\n\n\n```\nwget http://somethingaboutorange.com/mrl/projects/nose/nose-0.11.2.tar.gz\ntar xzvf nose-0.11.2.tar.gz\ncd nose-0.11.2\nsage -python setup.py install  \n```\n\n\nHowever, it might make sense to have nose be an optional spkg.\n\nMatplotlib relies on nose to do tests (http://matplotlib.sourceforge.net/devel/coding_guide.html#testing), as well as numpy/scipy (http://projects.scipy.org/numpy/wiki/TestingGuidelines).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9921\n\n",
    "created_at": "2010-09-16T17:32:19Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.7",
    "title": "nose testing suite as an optional spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9920",
    "user": "@jasongrout"
}
```
Assignee: tbd

CC:  drkirkby @jhpalmieri

Several projects we depend on use nose to do self-tests.  In order to test these packages, we'd have to have nose installed.

This is fairly simple without an spkg:


```
wget http://somethingaboutorange.com/mrl/projects/nose/nose-0.11.2.tar.gz
tar xzvf nose-0.11.2.tar.gz
cd nose-0.11.2
sage -python setup.py install  
```


However, it might make sense to have nose be an optional spkg.

Matplotlib relies on nose to do tests (http://matplotlib.sourceforge.net/devel/coding_guide.html#testing), as well as numpy/scipy (http://projects.scipy.org/numpy/wiki/TestingGuidelines).

Issue created by migration from https://trac.sagemath.org/ticket/9921





---

archive/issue_comments_098737.json:
```json
{
    "body": "The current website for nose is: http://code.google.com/p/python-nose/",
    "created_at": "2010-09-16T17:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98737",
    "user": "@jasongrout"
}
```

The current website for nose is: http://code.google.com/p/python-nose/



---

archive/issue_comments_098738.json:
```json
{
    "body": "IMHO it would be sensible to have nose as a **standard** package. \n\nI suggested that once, and it got a luke warm reception. Having to install an optional item to test a standard package seems a bad idea to me. \n\nPerhaps if a list of packages which make use of 'nose' could be produced, it might be possible to argue for it to be standard. \n\nDave",
    "created_at": "2010-09-16T18:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98738",
    "user": "drkirkby"
}
```

IMHO it would be sensible to have nose as a **standard** package. 

I suggested that once, and it got a luke warm reception. Having to install an optional item to test a standard package seems a bad idea to me. 

Perhaps if a list of packages which make use of 'nose' could be produced, it might be possible to argue for it to be standard. 

Dave



---

archive/issue_comments_098739.json:
```json
{
    "body": "Yes, I'm thinking (according to guidelines) optional for now, standard after a probationary period.",
    "created_at": "2010-09-16T18:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98739",
    "user": "@jasongrout"
}
```

Yes, I'm thinking (according to guidelines) optional for now, standard after a probationary period.



---

archive/issue_comments_098740.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> Yes, I'm thinking (according to guidelines) optional for now, standard after a probationary period.\n\nYes, according to guidelines it should be optional for a while. But there have been exceptions to that. Since it does not actually link to anything in Sage, and would only be called when running spkg-check, I think one could argue the risk is minimal. In contrast it would allow a number of packages to be checked. \n\nI think any such argument would have to be based on how many packages could benefit from it. \n\nIt must be an incredibly low risk package to add. \n\nDave",
    "created_at": "2010-09-16T19:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98740",
    "user": "drkirkby"
}
```

Replying to [comment:4 jason]:
> Yes, I'm thinking (according to guidelines) optional for now, standard after a probationary period.

Yes, according to guidelines it should be optional for a while. But there have been exceptions to that. Since it does not actually link to anything in Sage, and would only be called when running spkg-check, I think one could argue the risk is minimal. In contrast it would allow a number of packages to be checked. 

I think any such argument would have to be based on how many packages could benefit from it. 

It must be an incredibly low risk package to add. 

Dave



---

archive/issue_comments_098741.json:
```json
{
    "body": "Whether or not it should be standard, I agree that we need to at least have it optional so that it becomes more 'Sage-ic' (totally not the right adjective, but I'm groping here) to test several fundamental python packages from within Sage.  Also, it is needed to test some potential other packages, such as Brian (#9675), which is where I originally found out about this.",
    "created_at": "2010-09-17T00:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98741",
    "user": "@kcrisman"
}
```

Whether or not it should be standard, I agree that we need to at least have it optional so that it becomes more 'Sage-ic' (totally not the right adjective, but I'm groping here) to test several fundamental python packages from within Sage.  Also, it is needed to test some potential other packages, such as Brian (#9675), which is where I originally found out about this.



---

archive/issue_comments_098742.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> Whether or not it should be standard, I agree that we need to at least have it optional so that it becomes more 'Sage-ic' (totally not the right adjective, but I'm groping here) to test several fundamental python packages from within Sage.  Also, it is needed to test some potential other packages, such as Brian (#9675), which is where I originally found out about this.\n\nI installed the package and tried it to test Brian, and it worked perfectly. However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. (see the page [Producing New Sage Packages](http://www.sagemath.org/doc/developer/producing_spkgs.html) to see how it should be).",
    "created_at": "2010-09-19T18:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98742",
    "user": "uri"
}
```

Replying to [comment:6 kcrisman]:
> Whether or not it should be standard, I agree that we need to at least have it optional so that it becomes more 'Sage-ic' (totally not the right adjective, but I'm groping here) to test several fundamental python packages from within Sage.  Also, it is needed to test some potential other packages, such as Brian (#9675), which is where I originally found out about this.

I installed the package and tried it to test Brian, and it worked perfectly. However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. (see the page [Producing New Sage Packages](http://www.sagemath.org/doc/developer/producing_spkgs.html) to see how it should be).



---

archive/issue_comments_098743.json:
```json
{
    "body": "Replying to [comment:7 uri]:\n> [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]\n\n? Of course we first have to produce an spkg, be it optional or (later) standard.\n\nOr did I miss something?",
    "created_at": "2010-09-20T02:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98743",
    "user": "@nexttime"
}
```

Replying to [comment:7 uri]:
> [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]

? Of course we first have to produce an spkg, be it optional or (later) standard.

Or did I miss something?



---

archive/issue_comments_098744.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-20T02:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98744",
    "user": "@nexttime"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_098745.json:
```json
{
    "body": "> > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]\n> \n> ? Of course we first have to produce an spkg, be it optional or (later) standard.\n> \n> Or did I miss something?\n\nNo, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.  No harm done in reminding us of the official rules, though :)",
    "created_at": "2010-09-20T02:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98745",
    "user": "@kcrisman"
}
```

> > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]
> 
> ? Of course we first have to produce an spkg, be it optional or (later) standard.
> 
> Or did I miss something?

No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.  No harm done in reminding us of the official rules, though :)



---

archive/issue_comments_098746.json:
```json
{
    "body": "Replying to [comment:9 kcrisman]:\n> No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.\n\nYeah, an spkg just containing `spkg-install` which is\n\n```\nwget http://code.google.com/p/python-nose/downloads/detail?name=nose-0.11.3.tar.gz\ntar xzvf nose-0.11.3.tar.gz\ncd nose-0.11.3\nsage -python setup.py install  \n```\n\n\n:D",
    "created_at": "2010-09-20T03:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98746",
    "user": "@nexttime"
}
```

Replying to [comment:9 kcrisman]:
> No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.

Yeah, an spkg just containing `spkg-install` which is

```
wget http://code.google.com/p/python-nose/downloads/detail?name=nose-0.11.3.tar.gz
tar xzvf nose-0.11.3.tar.gz
cd nose-0.11.3
sage -python setup.py install  
```


:D



---

archive/issue_comments_098747.json:
```json
{
    "body": "Ok, we should concatenate the lines with `&&` to make it more robust...",
    "created_at": "2010-09-20T03:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98747",
    "user": "@nexttime"
}
```

Ok, we should concatenate the lines with `&&` to make it more robust...



---

archive/issue_comments_098748.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Replying to [comment:7 uri]:\n> > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]\n> \n> ? Of course we first have to produce an spkg, be it optional or (later) standard.\n> \n> Or did I miss something?\n\nOh, right, I missunderstood... sorry :)",
    "created_at": "2010-09-20T08:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98748",
    "user": "uri"
}
```

Replying to [comment:8 leif]:
> Replying to [comment:7 uri]:
> > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]
> 
> ? Of course we first have to produce an spkg, be it optional or (later) standard.
> 
> Or did I miss something?

Oh, right, I missunderstood... sorry :)



---

archive/issue_comments_098749.json:
```json
{
    "body": "Replying to [comment:9 kcrisman]:\n> > > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]\n> > \n> > ? Of course we first have to produce an spkg, be it optional or (later) standard.\n> > \n> > Or did I miss something?\n> \n> No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.  No harm done in reminding us of the official rules, though :)\n\nYep, the point of the instructions was to show that even without an spkg, using nose \"is fairly simple without an spkg\".  Of course, you can't download something in the spkg, so those instructions would not work for an spkg.  However, it would be a very generic spkg-install file that would basically do the normal standard checks and then run \"python setup.py install\".",
    "created_at": "2010-09-20T11:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98749",
    "user": "@jasongrout"
}
```

Replying to [comment:9 kcrisman]:
> > > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]
> > 
> > ? Of course we first have to produce an spkg, be it optional or (later) standard.
> > 
> > Or did I miss something?
> 
> No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.  No harm done in reminding us of the official rules, though :)

Yep, the point of the instructions was to show that even without an spkg, using nose "is fairly simple without an spkg".  Of course, you can't download something in the spkg, so those instructions would not work for an spkg.  However, it would be a very generic spkg-install file that would basically do the normal standard checks and then run "python setup.py install".



---

archive/issue_comments_098750.json:
```json
{
    "body": "I tried using nose, and it was very interesting.  Tested Brian on two different boxes, and then tested both numpy and scipy on OS X 10.6 - discovered no errors on the first, and a fair number on the second!  So I think that there should be no doubt this could go straight to optional if an spkg was made.\n\nI couldn't do\n\n```\nimport matplotlib\nmatplotlib.test()\n```\n\nbecause for some reason our matplotlib doesn't have this method.\n\nMuch less importantly, I should also point out that on OS X `wget` is not a builtin, though I have an alias `curl -O` that seems to accomplish the same purpose.  I just downloaded and double-clicked, actually :)",
    "created_at": "2010-09-21T01:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98750",
    "user": "@kcrisman"
}
```

I tried using nose, and it was very interesting.  Tested Brian on two different boxes, and then tested both numpy and scipy on OS X 10.6 - discovered no errors on the first, and a fair number on the second!  So I think that there should be no doubt this could go straight to optional if an spkg was made.

I couldn't do

```
import matplotlib
matplotlib.test()
```

because for some reason our matplotlib doesn't have this method.

Much less importantly, I should also point out that on OS X `wget` is not a builtin, though I have an alias `curl -O` that seems to accomplish the same purpose.  I just downloaded and double-clicked, actually :)



---

archive/issue_comments_098751.json:
```json
{
    "body": "Nose is now on Github: [https://github.com/nose-devs/nose](https://github.com/nose-devs/nose).",
    "created_at": "2012-05-26T20:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98751",
    "user": "@kcrisman"
}
```

Nose is now on Github: [https://github.com/nose-devs/nose](https://github.com/nose-devs/nose).



---

archive/issue_comments_098752.json:
```json
{
    "body": "I've posted an spkg. It builds well enough for me, but I haven't actually used it to test anything except for itself (in spkg-check).",
    "created_at": "2012-06-14T23:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98752",
    "user": "@jhpalmieri"
}
```

I've posted an spkg. It builds well enough for me, but I haven't actually used it to test anything except for itself (in spkg-check).



---

archive/issue_comments_098753.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-14T23:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98753",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098754.json:
```json
{
    "body": "scripts repo",
    "created_at": "2012-06-14T23:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98754",
    "user": "@jhpalmieri"
}
```

scripts repo



---

archive/issue_comments_098755.json:
```json
{
    "body": "Attachment [trac_9921-nose-scripts.patch](tarball://root/attachments/some-uuid/ticket9921/trac_9921-nose-scripts.patch) by @jhpalmieri created at 2012-06-14 23:20:18",
    "created_at": "2012-06-14T23:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98755",
    "user": "@jhpalmieri"
}
```

Attachment [trac_9921-nose-scripts.patch](tarball://root/attachments/some-uuid/ticket9921/trac_9921-nose-scripts.patch) by @jhpalmieri created at 2012-06-14 23:20:18



---

archive/issue_comments_098756.json:
```json
{
    "body": "By the way, version 1.1.2 was the most recent version for which I could find a tar ball. Or we could use the version from github; would that be better?",
    "created_at": "2012-06-14T23:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98756",
    "user": "@jhpalmieri"
}
```

By the way, version 1.1.2 was the most recent version for which I could find a tar ball. Or we could use the version from github; would that be better?



---

archive/issue_comments_098757.json:
```json
{
    "body": "I've now also prepared a version from git. This one fails its own self tests, though ;)",
    "created_at": "2012-06-14T23:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98757",
    "user": "@jhpalmieri"
}
```

I've now also prepared a version from git. This one fails its own self tests, though ;)



---

archive/issue_comments_098758.json:
```json
{
    "body": "patch for spkg, for review only",
    "created_at": "2012-06-14T23:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98758",
    "user": "@jhpalmieri"
}
```

patch for spkg, for review only



---

archive/issue_comments_098759.json:
```json
{
    "body": "Attachment [trac_9921-nose-spkg.git.patch](tarball://root/attachments/some-uuid/ticket9921/trac_9921-nose-spkg.git.patch) by @jhpalmieri created at 2012-06-14 23:39:24\n\npatch for spkg, for review only (version 1.1.3)",
    "created_at": "2012-06-14T23:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98759",
    "user": "@jhpalmieri"
}
```

Attachment [trac_9921-nose-spkg.git.patch](tarball://root/attachments/some-uuid/ticket9921/trac_9921-nose-spkg.git.patch) by @jhpalmieri created at 2012-06-14 23:39:24

patch for spkg, for review only (version 1.1.3)



---

archive/issue_comments_098760.json:
```json
{
    "body": "> I've now also prepared a version from git. This one fails its own self tests, though ;)\nInteresting!\n\nYou can try using it with the brian optional spkg, and I believe numpy and mpl also use this?",
    "created_at": "2012-06-15T01:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98760",
    "user": "@kcrisman"
}
```

> I've now also prepared a version from git. This one fails its own self tests, though ;)
Interesting!

You can try using it with the brian optional spkg, and I believe numpy and mpl also use this?



---

archive/issue_comments_098761.json:
```json
{
    "body": "ipython also uses nose.",
    "created_at": "2012-06-15T04:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98761",
    "user": "@jasongrout"
}
```

ipython also uses nose.



---

archive/issue_comments_098762.json:
```json
{
    "body": "I tried running self-tests with numpy, using `python -c 'import numpy; numpy.test()'`. The good news: tests ran. The bad news: some tests failed. More bad news: this exited with a return code of zero, so it's hard to tell (within spkg-check, for example), that tests failed. I have the same issue with IPython.",
    "created_at": "2012-06-15T17:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98762",
    "user": "@jhpalmieri"
}
```

I tried running self-tests with numpy, using `python -c 'import numpy; numpy.test()'`. The good news: tests ran. The bad news: some tests failed. More bad news: this exited with a return code of zero, so it's hard to tell (within spkg-check, for example), that tests failed. I have the same issue with IPython.



---

archive/issue_comments_098763.json:
```json
{
    "body": "So is that a problem with nose or a problem with the numpy/ipython test suites?  Sounds like nose is ready from this point of view :)",
    "created_at": "2012-06-15T17:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98763",
    "user": "@kcrisman"
}
```

So is that a problem with nose or a problem with the numpy/ipython test suites?  Sounds like nose is ready from this point of view :)



---

archive/issue_comments_098764.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd41\".",
    "created_at": "2012-06-15T23:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98764",
    "user": "@jhpalmieri"
}
```

Changing keywords from "" to "sd41".



---

archive/issue_comments_098765.json:
```json
{
    "body": "This is ridiculous.  Nose works fine at testing things on sage.math.   It certainly finds various errors and warnings - apparently scipy generates a number as well, I just tried it.\n\nThe issue with it not passing its own tests is not so good, and I can confirm this in both cases.  On the plus side, it only breaks the Sage installation process in the 1.1.3, so I would say let's go with the 1.1.2 for now.\n\n----\n\nI do get something weird, hopefully unrelated to nose itself, but instead related to our defaults for matplotlib.\n\n```\n\nkcrisman@sage:~/sage-5.1.beta1-boxen-x86_64-Linux$ ./sage -c 'import matplotlib; matplotlib.test()'\n======================================================================\nERROR: Failure: OSError (No such file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/import matplotlib; matplotlib.test())\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/failure.py\", line 39, in runTest\n    raise self.exc_class(self.exc_val)\nOSError: No such file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/import matplotlib; matplotlib.test()\n\n----------------------------------------------------------------------\nRan 1 test in 0.001s\n\nFAILED (errors=1)\n\nsage: import matplotlib  \nsage: matplotlib.test()\n======================================================================\nERROR: Failure: ValueError (Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/loader.py\", line 213, in loadTestsFromFile\n    % filename)\nValueError: Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage\n\n----------------------------------------------------------------------\nRan 1 test in 0.001s\n\nFAILED (errors=1)\nFalse\n```\n\n\n\nOn a computer without nose:\n\n```\n\nsage: matplotlib.test()\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/Users/karl-dietercrisman/Downloads/sage-5.1.beta6/<ipython console> in <module>()\n\n/Users/.../sage-5.1.beta6/local/lib/python2.7/site-packages/matplotlib/__init__.pyc in test(verbosity)\n    986 def test(verbosity=0):\n    987     \"\"\"run the matplotlib test suite\"\"\"\n--> 988     import nose\n    989     import nose.plugins.builtin\n    990     from testing.noseclasses import KnownFailure\n\nImportError: No module named nose\n```\n\n\nI think that in matplotlib's lib/__init__.py\n\n```\n\n    success = nose.run( defaultTest=default_test_modules,\n                        config=config,\n                        )\n```\n\nwe aren't using the right default modules, they aren't imported or something.  So it goes back to just looking at `.` for the default test module - I get the same thing.\n\n```\n\nsage: nose.run(defaultTest='.')                 \nE\n======================================================================\nERROR: Failure: ValueError (Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/loader.py\", line 213, in loadTestsFromFile\n    % filename)\nValueError: Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage\n\n----------------------------------------------------------------------\nRan 1 test in 0.001s\n\nFAILED (errors=1)\nFalse\n```\n\n\nCan you see a reason why this shouldn't have positive review?  I just think this must be a problem in how we're dealing with mpl.  I'm surprised it does this; we only removed the baseline images, not the testing scripts!",
    "created_at": "2012-07-05T17:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98765",
    "user": "@kcrisman"
}
```

This is ridiculous.  Nose works fine at testing things on sage.math.   It certainly finds various errors and warnings - apparently scipy generates a number as well, I just tried it.

The issue with it not passing its own tests is not so good, and I can confirm this in both cases.  On the plus side, it only breaks the Sage installation process in the 1.1.3, so I would say let's go with the 1.1.2 for now.

----

I do get something weird, hopefully unrelated to nose itself, but instead related to our defaults for matplotlib.

```

kcrisman@sage:~/sage-5.1.beta1-boxen-x86_64-Linux$ ./sage -c 'import matplotlib; matplotlib.test()'
======================================================================
ERROR: Failure: OSError (No such file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/import matplotlib; matplotlib.test())
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/failure.py", line 39, in runTest
    raise self.exc_class(self.exc_val)
OSError: No such file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/import matplotlib; matplotlib.test()

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)

sage: import matplotlib  
sage: matplotlib.test()
======================================================================
ERROR: Failure: ValueError (Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/loader.py", line 213, in loadTestsFromFile
    % filename)
ValueError: Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
False
```



On a computer without nose:

```

sage: matplotlib.test()
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/karl-dietercrisman/Downloads/sage-5.1.beta6/<ipython console> in <module>()

/Users/.../sage-5.1.beta6/local/lib/python2.7/site-packages/matplotlib/__init__.pyc in test(verbosity)
    986 def test(verbosity=0):
    987     """run the matplotlib test suite"""
--> 988     import nose
    989     import nose.plugins.builtin
    990     from testing.noseclasses import KnownFailure

ImportError: No module named nose
```


I think that in matplotlib's lib/__init__.py

```

    success = nose.run( defaultTest=default_test_modules,
                        config=config,
                        )
```

we aren't using the right default modules, they aren't imported or something.  So it goes back to just looking at `.` for the default test module - I get the same thing.

```

sage: nose.run(defaultTest='.')                 
E
======================================================================
ERROR: Failure: ValueError (Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/loader.py", line 213, in loadTestsFromFile
    % filename)
ValueError: Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
False
```


Can you see a reason why this shouldn't have positive review?  I just think this must be a problem in how we're dealing with mpl.  I'm surprised it does this; we only removed the baseline images, not the testing scripts!



---

archive/issue_comments_098766.json:
```json
{
    "body": "I have also reviewed this ticket, since I think it is important to have it. The matplotlib error is really a bug (or at least laxness) in matplotlib. If we waited for nosetest to be included until all spkg's pass, we would wait until the cows come home.\n\nIf nobody objects, I will set this to positive review by next week.",
    "created_at": "2013-01-24T12:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98766",
    "user": "mraum"
}
```

I have also reviewed this ticket, since I think it is important to have it. The matplotlib error is really a bug (or at least laxness) in matplotlib. If we waited for nosetest to be included until all spkg's pass, we would wait until the cows come home.

If nobody objects, I will set this to positive review by next week.



---

archive/issue_comments_098767.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-29T17:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98767",
    "user": "mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098768.json:
```json
{
    "body": "spkg is put on the servers.",
    "created_at": "2013-01-30T16:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98768",
    "user": "@haraldschilly"
}
```

spkg is put on the servers.



---

archive/issue_comments_098769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-30T16:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9920#issuecomment-98769",
    "user": "@jdemeyer"
}
```

Resolution: fixed
