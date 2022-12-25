# Issue 9675: New package: Brian, a simulator for spiking neural networks

archive/issues_009675.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mwhansen mvngu @haraldschilly\n\nKeywords: brian brain simulator neuronal dynamics\n\nI've created a Sage package from an already existing Python package called Brian (see http://www.briansimulator.org/ for more information). The description that is provided in this webpage is the following:\n\n*Brian is a simulator for spiking neural networks available on almost all platforms. The motivation for this project is that a simulator should not only save the time of processors, but also the time of scientists. It is easy to learn and use, highly flexible and easily extensible. The Brian package itself and simulations using it are all written in the Python programming language.*\n\nI'm not sure whether this package should be proposed as experimental or optional. For the moment I've put it as an experimental package. However, I think it could be optional, because as a Python package it has been widely tested and works perfectly, so I don't think there'll be a lot of problems as a Sage package. Please, let me know your opinion on that.\n\nI must say I detected some problems with Brian units related to the Sage classes 'RealNumber' and 'Integer', so I created a patch so that when Brian is imported these two classes are redefined as follows:\n\n```\nRealNumber=float\nInteger=int\n```\n\nThis solves the problems. \n\nI attach the .spkg here (I know it's better just to provide a link, but I don't have anywhere else to upload it to).\n\nPlease, let me know what you think!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9675\n\n",
    "created_at": "2010-08-03T16:02:16Z",
    "labels": [
        "component: packages: experimental",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "New package: Brian, a simulator for spiking neural networks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9675",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```
Assignee: tbd

CC:  @mwhansen mvngu @haraldschilly

Keywords: brian brain simulator neuronal dynamics

I've created a Sage package from an already existing Python package called Brian (see http://www.briansimulator.org/ for more information). The description that is provided in this webpage is the following:

*Brian is a simulator for spiking neural networks available on almost all platforms. The motivation for this project is that a simulator should not only save the time of processors, but also the time of scientists. It is easy to learn and use, highly flexible and easily extensible. The Brian package itself and simulations using it are all written in the Python programming language.*

I'm not sure whether this package should be proposed as experimental or optional. For the moment I've put it as an experimental package. However, I think it could be optional, because as a Python package it has been widely tested and works perfectly, so I don't think there'll be a lot of problems as a Sage package. Please, let me know your opinion on that.

I must say I detected some problems with Brian units related to the Sage classes 'RealNumber' and 'Integer', so I created a patch so that when Brian is imported these two classes are redefined as follows:

```
RealNumber=float
Integer=int
```

This solves the problems. 

I attach the .spkg here (I know it's better just to provide a link, but I don't have anywhere else to upload it to).

Please, let me know what you think!

Issue created by migration from https://trac.sagemath.org/ticket/9675





---

archive/issue_comments_093860.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-03T16:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93860",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093861.json:
```json
{
    "body": "Cool!  \nYou may also want to see [this](http://groups.google.com/group/sage-devel/browse_thread/thread/9cec3d5595044b4f/ef8474417a60fbfa?show_docid=ef8474417a60fbfa) thread on sage-devel about where to put spkgs.  \n\nAs to the redefining, that seems... problematic.  There are other Sage Python packages that must encounter the same problems - you may want to ask on the list about how they deal with this.  (I suppose numpy and matplotlib would be likely candidates for this.)\n\nWhat platforms does Brian work on out of the box?",
    "created_at": "2010-08-03T17:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93861",
    "user": "https://github.com/kcrisman"
}
```

Cool!  
You may also want to see [this](http://groups.google.com/group/sage-devel/browse_thread/thread/9cec3d5595044b4f/ef8474417a60fbfa?show_docid=ef8474417a60fbfa) thread on sage-devel about where to put spkgs.  

As to the redefining, that seems... problematic.  There are other Sage Python packages that must encounter the same problems - you may want to ask on the list about how they deal with this.  (I suppose numpy and matplotlib would be likely candidates for this.)

What platforms does Brian work on out of the box?



---

archive/issue_comments_093862.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Cool!  \n> You may also want to see [this](http://groups.google.com/group/sage-devel/browse_thread/thread/9cec3d5595044b4f/ef8474417a60fbfa?show_docid=ef8474417a60fbfa) thread on sage-devel about where to put spkgs.  \n\n\nThanks, I didn't know about Google Code!\n\n> As to the redefining, that seems... problematic.  There are other Sage Python packages that must encounter the same problems - you may want to ask on the list about how they deal with this.  (I suppose numpy and matplotlib would be likely candidates for this.)\n\nYes, I'll give it a try, but I'm not sure if I'll be able to find another solution. I'll let you know.\n\n> What platforms does Brian work on out of the box?   \n\nWell, in the website they say: *All platforms running Python, so at least Windows, Linux and Mac*. I can't say more than that, as I've tried it just on Linux.",
    "created_at": "2010-08-04T14:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93862",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Replying to [comment:2 kcrisman]:
> Cool!  
> You may also want to see [this](http://groups.google.com/group/sage-devel/browse_thread/thread/9cec3d5595044b4f/ef8474417a60fbfa?show_docid=ef8474417a60fbfa) thread on sage-devel about where to put spkgs.  


Thanks, I didn't know about Google Code!

> As to the redefining, that seems... problematic.  There are other Sage Python packages that must encounter the same problems - you may want to ask on the list about how they deal with this.  (I suppose numpy and matplotlib would be likely candidates for this.)

Yes, I'll give it a try, but I'm not sure if I'll be able to find another solution. I'll let you know.

> What platforms does Brian work on out of the box?   

Well, in the website they say: *All platforms running Python, so at least Windows, Linux and Mac*. I can't say more than that, as I've tried it just on Linux.



---

archive/issue_comments_093863.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> As to the redefining, that seems... problematic.\n\n\nAnd turning of the preparser via:\n\n```\npreparser(false)\n```\n\nwould also be problematic?",
    "created_at": "2010-08-04T19:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93863",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Replying to [comment:2 kcrisman]:
> As to the redefining, that seems... problematic.


And turning of the preparser via:

```
preparser(false)
```

would also be problematic?



---

archive/issue_comments_093864.json:
```json
{
    "body": "Replying to [comment:4 uri]:\n> Replying to [comment:2 kcrisman]:\n> > As to the redefining, that seems... problematic.\n\n> \n> And turning of the preparser via:\n> \n> \n> ```\n> preparser(false)\n> ```\n> \n> would also be problematic?\n\nWell, the issues is that a lot of Sage would no longer work as advertised.  That is fine if one is only using Brian, but presumably the point of having Brian as an optional package is that one could go back and forth with other parts of Sage.  I don't know exactly what other such packages do, though.  I highly suggest just emailing sage-devel (perhaps in reply to your original message) and asking what ways around this there are; I assume they exist.  Good luck!",
    "created_at": "2010-08-04T19:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93864",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:4 uri]:
> Replying to [comment:2 kcrisman]:
> > As to the redefining, that seems... problematic.

> 
> And turning of the preparser via:
> 
> 
> ```
> preparser(false)
> ```
> 
> would also be problematic?

Well, the issues is that a lot of Sage would no longer work as advertised.  That is fine if one is only using Brian, but presumably the point of having Brian as an optional package is that one could go back and forth with other parts of Sage.  I don't know exactly what other such packages do, though.  I highly suggest just emailing sage-devel (perhaps in reply to your original message) and asking what ways around this there are; I assume they exist.  Good luck!



---

archive/issue_comments_093865.json:
```json
{
    "body": "Finally, Brian developers helped me to find a way to solve the problem without needing to redefine any Sage class nor to turn off the preparser. I've upload it on Google Code, you can download it [here](http://spkg-upload.googlecode.com/files/brian-1.2.1.p0.spkg). However, I'll re-upload it here in Trac page to avoid confusions.",
    "created_at": "2010-08-09T15:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93865",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Finally, Brian developers helped me to find a way to solve the problem without needing to redefine any Sage class nor to turn off the preparser. I've upload it on Google Code, you can download it [here](http://spkg-upload.googlecode.com/files/brian-1.2.1.p0.spkg). However, I'll re-upload it here in Trac page to avoid confusions.



---

archive/issue_comments_093866.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-18T15:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93866",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024140.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2010-08-18T15:04:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9675#event-24140"
}
```



---

archive/issue_comments_093867.json:
```json
{
    "body": "This seems to build fine, the script is ok.   In terms of experimental, positive review - it didn't crash anything, and commands actually do things and give output that is consistent with it.\n\nTo release manager - what happens now?  It gets uploaded to the Sage mirrors as experimental package, maybe?  Who does that?\n\nBut in the interests of improving it - I don't see why this couldn't be an optional package, if you can find another potential maintainer (different ticket).  If so, you'd definitely want to have a SPKG-TEST file or whatever, since there are builtin tests.  But...\n\nWhen I do\n\n```\nsage: import brian\nsage: brian.tests()\n```\nI get that I'm missing `nose`.    I doubt that `nose` will be a Sage package anytime soon - or should it, if it makes tests that much easier?  Perhaps upstream would consider having a non-`nose` option for testing.\n\nWhen I try the brian website examples, it tells me that the Sage matplotlib backend doesn't support `show()`.  That would be another thing to figure out.",
    "created_at": "2010-08-18T15:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93867",
    "user": "https://github.com/kcrisman"
}
```

This seems to build fine, the script is ok.   In terms of experimental, positive review - it didn't crash anything, and commands actually do things and give output that is consistent with it.

To release manager - what happens now?  It gets uploaded to the Sage mirrors as experimental package, maybe?  Who does that?

But in the interests of improving it - I don't see why this couldn't be an optional package, if you can find another potential maintainer (different ticket).  If so, you'd definitely want to have a SPKG-TEST file or whatever, since there are builtin tests.  But...

When I do

```
sage: import brian
sage: brian.tests()
```
I get that I'm missing `nose`.    I doubt that `nose` will be a Sage package anytime soon - or should it, if it makes tests that much easier?  Perhaps upstream would consider having a non-`nose` option for testing.

When I try the brian website examples, it tells me that the Sage matplotlib backend doesn't support `show()`.  That would be another thing to figure out.



---

archive/issue_comments_093868.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-24T07:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93868",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093869.json:
```json
{
    "body": "The package has unchecked-in changes:\n\n```sh\n$ hg stat\n? .hgignore\n? SPKG.txt\n? patches/units.py\n? patches/units.py.patch\n? spkg-install\n```\nOriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.\n\nAlso, could you please add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?  Thanks!",
    "created_at": "2010-08-24T07:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93869",
    "user": "https://github.com/qed777"
}
```

The package has unchecked-in changes:

```sh
$ hg stat
? .hgignore
? SPKG.txt
? patches/units.py
? patches/units.py.patch
? spkg-install
```
Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.

Also, could you please add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?  Thanks!



---

archive/issue_comments_093870.json:
```json
{
    "body": "Oh, I'm so sorry, Mitesh - here I was checking whether the spkg worked but forgot to actually rebuild the spkg from its constituents.  If I ran sage-pkg on it would it have shown this?",
    "created_at": "2010-08-24T11:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93870",
    "user": "https://github.com/kcrisman"
}
```

Oh, I'm so sorry, Mitesh - here I was checking whether the spkg worked but forgot to actually rebuild the spkg from its constituents.  If I ran sage-pkg on it would it have shown this?



---

archive/issue_comments_093871.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> The package has unchecked-in changes:\n> \n> ```\n> #!sh\n> $ hg stat\n> ? .hgignore\n> ? SPKG.txt\n> ? patches/units.py\n> ? patches/units.py.patch\n> ? spkg-install\n> ```\n> Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.\n\n\nOk, done. Please, let me know if it's allright, it's the first time I added files to the repository and I want to be sure I did everything correctly.\n\n> Also, could you please add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?  \n\nDone!\n\n> Thanks!\n\nThanks to you for your commments!!",
    "created_at": "2010-08-31T10:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93871",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Replying to [comment:8 mpatel]:
> The package has unchecked-in changes:
> 
> ```
> #!sh
> $ hg stat
> ? .hgignore
> ? SPKG.txt
> ? patches/units.py
> ? patches/units.py.patch
> ? spkg-install
> ```
> Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.


Ok, done. Please, let me know if it's allright, it's the first time I added files to the repository and I want to be sure I did everything correctly.

> Also, could you please add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?  

Done!

> Thanks!

Thanks to you for your commments!!



---

archive/issue_comments_093872.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> But in the interests of improving it - I don't see why this couldn't be an optional package, if you can find another potential maintainer (different ticket).  If so, you'd definitely want to have a SPKG-TEST file or whatever, since there are builtin tests.  But...\n> \n> When I do\n> \n> ```\n> sage: import brian\n> sage: brian.tests()\n> ```\n> I get that I'm missing `nose`.    I doubt that `nose` will be a Sage package anytime soon - or should it, if it makes tests that much easier?  Perhaps upstream would consider having a non-`nose` option for testing.\n\n\nI don't really know what to say about that... I don't know `nose` and haven't looked at these tests much. I'll think about it, though. However, is it really necessary to include tests on the packages, in order to be set as optional instead of experimental?\n\n> When I try the brian website examples, it tells me that the Sage matplotlib backend doesn't support `show()`.  That would be another thing to figure out.\n\n\nYes, I had already seen that. The problem is not in Brian but in the matplotlib package itself... there're other ways to see the images, for example replacing the show() command for:\n\n```\nsage: savefig('figure.png')\n```\nwhich creates the file *figure.png* in the working directory. Maybe that should be specified in the documentation. What do you think?",
    "created_at": "2010-08-31T11:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93872",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Replying to [comment:7 kcrisman]:
> But in the interests of improving it - I don't see why this couldn't be an optional package, if you can find another potential maintainer (different ticket).  If so, you'd definitely want to have a SPKG-TEST file or whatever, since there are builtin tests.  But...
> 
> When I do
> 
> ```
> sage: import brian
> sage: brian.tests()
> ```
> I get that I'm missing `nose`.    I doubt that `nose` will be a Sage package anytime soon - or should it, if it makes tests that much easier?  Perhaps upstream would consider having a non-`nose` option for testing.


I don't really know what to say about that... I don't know `nose` and haven't looked at these tests much. I'll think about it, though. However, is it really necessary to include tests on the packages, in order to be set as optional instead of experimental?

> When I try the brian website examples, it tells me that the Sage matplotlib backend doesn't support `show()`.  That would be another thing to figure out.


Yes, I had already seen that. The problem is not in Brian but in the matplotlib package itself... there're other ways to see the images, for example replacing the show() command for:

```
sage: savefig('figure.png')
```
which creates the file *figure.png* in the working directory. Maybe that should be specified in the documentation. What do you think?



---

archive/issue_comments_093873.json:
```json
{
    "body": "Replying to [comment:10 uri]:\n> Replying to [comment:8 mpatel]:\n> > Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.\n\n> \n> Ok, done. Please, let me know if it's allright, it's the first time I added files to the repository and I want to be sure I did everything correctly.\n\n\nI apologize if I've missed it, but is there a link to the updated package?",
    "created_at": "2010-08-31T21:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93873",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:10 uri]:
> Replying to [comment:8 mpatel]:
> > Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.

> 
> Ok, done. Please, let me know if it's allright, it's the first time I added files to the repository and I want to be sure I did everything correctly.


I apologize if I've missed it, but is there a link to the updated package?



---

archive/issue_comments_093874.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> I apologize if I've missed it, but is there a link to the updated package?\n\n\nYou can download it clicking [here](http://spkg-upload.googlecode.com/files/brian-1.2.1.p0.spkg), but it's the same link I provided before (there's been no update, I just added the files to the repository).",
    "created_at": "2010-09-01T09:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93874",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Replying to [comment:12 mpatel]:
> I apologize if I've missed it, but is there a link to the updated package?


You can download it clicking [here](http://spkg-upload.googlecode.com/files/brian-1.2.1.p0.spkg), but it's the same link I provided before (there's been no update, I just added the files to the repository).



---

archive/issue_comments_093875.json:
```json
{
    "body": "Replying to [comment:13 uri]:\n> ..but it's the same link I provided before (there's been no update, I just added the files to the repository).\n\n\nok, just to avoid confusions, what I mean by that is that the link is the same because I didn't change the name of the package (from brian-1.2.1.p0 to  brian-1.2.1.p1) because there's been no update. So you'll download the right file with the old link.",
    "created_at": "2010-09-01T09:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93875",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Replying to [comment:13 uri]:
> ..but it's the same link I provided before (there's been no update, I just added the files to the repository).


ok, just to avoid confusions, what I mean by that is that the link is the same because I didn't change the name of the package (from brian-1.2.1.p0 to  brian-1.2.1.p1) because there's been no update. So you'll download the right file with the old link.



---

archive/issue_comments_093876.json:
```json
{
    "body": "Brian package (.spkg  file)",
    "created_at": "2010-09-01T09:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93876",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Brian package (.spkg  file)



---

archive/issue_comments_093877.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-01T09:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93877",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093878.json:
```json
{
    "body": "Attachment [brian-1.2.1.p0.spkg](tarball://root/attachments/some-uuid/ticket9675/brian-1.2.1.p0.spkg) by @qed777 created at 2010-09-01 09:36:14",
    "created_at": "2010-09-01T09:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93878",
    "user": "https://github.com/qed777"
}
```

Attachment [brian-1.2.1.p0.spkg](tarball://root/attachments/some-uuid/ticket9675/brian-1.2.1.p0.spkg) by @qed777 created at 2010-09-01 09:36:14



---

archive/issue_comments_093879.json:
```json
{
    "body": "# 9221 is related (making nose an optional/standard package).",
    "created_at": "2010-09-17T00:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93879",
    "user": "https://github.com/kcrisman"
}
```

# 9221 is related (making nose an optional/standard package).



---

archive/issue_comments_093880.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T20:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93880",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093881.json:
```json
{
    "body": "Okay, I checked this all out again, and now the HG is fine, and I can't find any garbage files, and it still applies fine to Sage 4.5.3, and I think this is more than ready to be an experimental package. \n\nIf you want, you can find people to test it on a couple other platforms to make sure it's ready for optional package status - I'm not sure exactly what the protocol for that is, though it seems to me that it's more than ready compared to other denizens of http://www.sagemath.org/packages/optional/.  But that could also be another ticket.  At the very least it should get loaded up to the mirrors.  Make it so!",
    "created_at": "2010-09-17T20:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93881",
    "user": "https://github.com/kcrisman"
}
```

Okay, I checked this all out again, and now the HG is fine, and I can't find any garbage files, and it still applies fine to Sage 4.5.3, and I think this is more than ready to be an experimental package. 

If you want, you can find people to test it on a couple other platforms to make sure it's ready for optional package status - I'm not sure exactly what the protocol for that is, though it seems to me that it's more than ready compared to other denizens of http://www.sagemath.org/packages/optional/.  But that could also be another ticket.  At the very least it should get loaded up to the mirrors.  Make it so!



---

archive/issue_comments_093882.json:
```json
{
    "body": "Harald, Mike, or Minh, could one of you add [attachment:brian-1.2.1.p0.spkg] to the experimental / contributed package repository?",
    "created_at": "2010-09-17T20:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93882",
    "user": "https://github.com/qed777"
}
```

Harald, Mike, or Minh, could one of you add [attachment:brian-1.2.1.p0.spkg] to the experimental / contributed package repository?



---

archive/issue_comments_093883.json:
```json
{
    "body": "Replying to [comment:16 kcrisman]:\n> # 9221 is related (making nose an optional/standard package).\n\n\nSmall correction: #9921 is about this, though there is a discussion about nose at #9221.",
    "created_at": "2010-09-17T20:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93883",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:16 kcrisman]:
> # 9221 is related (making nose an optional/standard package).


Small correction: #9921 is about this, though there is a discussion about nose at #9221.



---

archive/issue_comments_093884.json:
```json
{
    "body": "Replying to [comment:19 mpatel]:\n> Replying to [comment:16 kcrisman]:\n> > # 9221 is related (making nose an optional/standard package).\n\n> \n> Small correction: #9921 is about this, though there is a discussion about nose at #9221.\n\nAagh!  That's the same mistake Jason made on #9221 in referring (or not) to #9921... sorry.",
    "created_at": "2010-09-18T00:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93884",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:19 mpatel]:
> Replying to [comment:16 kcrisman]:
> > # 9221 is related (making nose an optional/standard package).

> 
> Small correction: #9921 is about this, though there is a discussion about nose at #9221.

Aagh!  That's the same mistake Jason made on #9221 in referring (or not) to #9921... sorry.



---

archive/issue_comments_093885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-19T06:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_024141.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-09-19T06:27:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9675#event-24141"
}
```



---

archive/issue_comments_093886.json:
```json
{
    "body": "Replying to [comment:18 mpatel]:\n> Harald, Mike, or Minh, could one of you add [attachment:brian-1.2.1.p0.spkg] to the experimental / contributed package repository?\n\n\nDone. See\n\nhttp://www.sagemath.org/packages/experimental/",
    "created_at": "2010-09-19T06:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:18 mpatel]:
> Harald, Mike, or Minh, could one of you add [attachment:brian-1.2.1.p0.spkg] to the experimental / contributed package repository?


Done. See

http://www.sagemath.org/packages/experimental/



---

archive/issue_comments_093887.json:
```json
{
    "body": "Thanks, Minh!",
    "created_at": "2010-09-19T06:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93887",
    "user": "https://github.com/qed777"
}
```

Thanks, Minh!



---

archive/issue_comments_093888.json:
```json
{
    "body": "Great, thank you all!\nI'll open a new ticket to see if it can be accepted as an optional package.",
    "created_at": "2010-09-19T17:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93888",
    "user": "https://trac.sagemath.org/admin/accounts/users/uri"
}
```

Great, thank you all!
I'll open a new ticket to see if it can be accepted as an optional package.



---

archive/issue_comments_093889.json:
```json
{
    "body": "There's been some discussion on other tickets about the virtues of nose, so it might not be that unlikely to make it standard in Sage.",
    "created_at": "2010-10-01T02:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9675#issuecomment-93889",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

There's been some discussion on other tickets about the virtues of nose, so it might not be that unlikely to make it standard in Sage.
