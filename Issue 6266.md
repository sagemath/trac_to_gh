# Issue 6266: Build problem of sqlite on Solaris 10 with gcc	4.4.0

archive/issues_006266.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: solaris sqlite\n\nThe sqlite in Sage 4.0.1-alpha0 (sqlite-3.5.3.p3) fails to build on t2, which runs Solaris 10 update 4, if gcc 4.4.0 is used as the compiler. Error messages are:\n\n\n```\n\n./.libs/libsqlite3.so: undefined reference to `write@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `pthread_create@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `fcntl@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `pthread_join@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `pthread_equal@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `close@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to \n`pthread_mutexattr_settype@SUNW_1.2'\n./.libs/libsqlite3.so: undefined reference to `read@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `sleep@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `pthread_self@SUNW_0.9'\n./.libs/libsqlite3.so: undefined reference to `fsync@SUNW_0.9'\n```\n\nI've downloaded both sqlite 3.5.3 and the latest (3.6.14.2) and find the build fails with similar (but fewer) error messages to those in Sage, so I don't  believe updating to the latest sqlite will solve this. The error messages building the latest sqlite are:\n\n\n```\n\n./.libs/libsqlite3.so: undefined reference to `dlerror@SUNW_1.22'\n./.libs/libsqlite3.so: undefined reference to `dlopen@SUNW_1.22'\n./.libs/libsqlite3.so: undefined reference to `dlsym@SUNW_1.22'\n./.libs/libsqlite3.so: undefined reference to `dlclose@SUNW_1.22'\n\n```\n\n\nA search of the web shows the sort of error messages have existed a long time in lots of software, going as far back as at least 2005. The culprit is often indicated to be libtool. \n\nThe developers of sqlite appear to be using a 3-year old version of libtool (1.5.24). \n\nI've downloaded that old version of libtool and found it fails 4 self-tests on t2. The latest version of libtool fails one test, suggesting sqlite would have more chance of working on Solaris if its developers used a later version of libtool. \n\nIf it's possible to get the developers of sqlite to use a later version of libtool, then an update of sqlite might be sensible, but at present it will not achieve anything very useful for Solaris. I'm in the process of trying to get this fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6266\n\n",
    "created_at": "2009-06-12T10:14:59Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Build problem of sqlite on Solaris 10 with gcc\t4.4.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6266",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Keywords: solaris sqlite

The sqlite in Sage 4.0.1-alpha0 (sqlite-3.5.3.p3) fails to build on t2, which runs Solaris 10 update 4, if gcc 4.4.0 is used as the compiler. Error messages are:


```

./.libs/libsqlite3.so: undefined reference to `write@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `pthread_create@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `fcntl@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `pthread_join@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `pthread_equal@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `close@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to 
`pthread_mutexattr_settype@SUNW_1.2'
./.libs/libsqlite3.so: undefined reference to `read@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `sleep@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `pthread_self@SUNW_0.9'
./.libs/libsqlite3.so: undefined reference to `fsync@SUNW_0.9'
```

I've downloaded both sqlite 3.5.3 and the latest (3.6.14.2) and find the build fails with similar (but fewer) error messages to those in Sage, so I don't  believe updating to the latest sqlite will solve this. The error messages building the latest sqlite are:


```

./.libs/libsqlite3.so: undefined reference to `dlerror@SUNW_1.22'
./.libs/libsqlite3.so: undefined reference to `dlopen@SUNW_1.22'
./.libs/libsqlite3.so: undefined reference to `dlsym@SUNW_1.22'
./.libs/libsqlite3.so: undefined reference to `dlclose@SUNW_1.22'

```


A search of the web shows the sort of error messages have existed a long time in lots of software, going as far back as at least 2005. The culprit is often indicated to be libtool. 

The developers of sqlite appear to be using a 3-year old version of libtool (1.5.24). 

I've downloaded that old version of libtool and found it fails 4 self-tests on t2. The latest version of libtool fails one test, suggesting sqlite would have more chance of working on Solaris if its developers used a later version of libtool. 

If it's possible to get the developers of sqlite to use a later version of libtool, then an update of sqlite might be sensible, but at present it will not achieve anything very useful for Solaris. I'm in the process of trying to get this fixed.

Issue created by migration from https://trac.sagemath.org/ticket/6266





---

archive/issue_comments_049944.json:
```json
{
    "body": "I've now fixed this. The problem was related to linking both libpthread and libc in the wrong order, due to what is probably a bug in libtool. \n\nNicolas Williams  (Nicolas.Williams`@`sun.com) has pointed out to me that there is no longer any need to link libpthread, as its functionality has been moved to libc. \n\nThe following code simply stops libpthread being linked. I've put the revised SPKG.txt and spkg-install at the following (there's also another .spkg file). \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite/",
    "created_at": "2009-06-13T13:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49944",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've now fixed this. The problem was related to linking both libpthread and libc in the wrong order, due to what is probably a bug in libtool. 

Nicolas Williams  (Nicolas.Williams`@`sun.com) has pointed out to me that there is no longer any need to link libpthread, as its functionality has been moved to libc. 

The following code simply stops libpthread being linked. I've put the revised SPKG.txt and spkg-install at the following (there's also another .spkg file). 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite/



---

archive/issue_comments_049945.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-06-13T13:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49945",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_049946.json:
```json
{
    "body": "I've just added \"[with patch; needs review]\" to the title. \n\nThe revised files are at \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite/SPKG.txt",
    "created_at": "2009-06-13T18:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49946",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've just added "[with patch; needs review]" to the title. 

The revised files are at 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite/SPKG.txt



---

archive/issue_comments_049947.json:
```json
{
    "body": "Oops, the link I gave first time was correct. The last link was only to one file. \n\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite/",
    "created_at": "2009-06-13T18:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49947",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Oops, the link I gave first time was correct. The last link was only to one file. 


http://sage.math.washington.edu/home/kirkby/Solaris-fixes/sqlite/



---

archive/issue_comments_049948.json:
```json
{
    "body": "This looks good, but I do have a comment about SPKG.txt: the stars are for an itemized list, so you just need one star for a single list item:\n\n```\n\n * Fixed a bug that prevented sqlite building on the Sun T5240\n t2.math.washington.edu running Solaris 10 update 4 with gcc version 4.4.0.\n \n Linking libpthread before libc caused the problem. Changing the \n order of linking avoided it, but is not easy to do, as the \n order is determined by libtool. \n However, libpthread is not necessary on Solaris 10. \n There is *probably* a libtool bug that is the real cause. \n The bug fix is implemented by striping libpthread out of the \n Makefile with sed. \n \n Thanks are due to Nicolas Williams (Nicolas.Williams@sun.com)\n who made me aware libpthread was not necessary, as its functionality\n was moved to libc in Solaris 10, with libpthread\n only provided for backwards compatibility. \n```\n\nIt also seems necessary to line up all the text below the star to get it all put into one item.",
    "created_at": "2009-06-14T07:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49948",
    "user": "https://github.com/dandrake"
}
```

This looks good, but I do have a comment about SPKG.txt: the stars are for an itemized list, so you just need one star for a single list item:

```

 * Fixed a bug that prevented sqlite building on the Sun T5240
 t2.math.washington.edu running Solaris 10 update 4 with gcc version 4.4.0.
 
 Linking libpthread before libc caused the problem. Changing the 
 order of linking avoided it, but is not easy to do, as the 
 order is determined by libtool. 
 However, libpthread is not necessary on Solaris 10. 
 There is *probably* a libtool bug that is the real cause. 
 The bug fix is implemented by striping libpthread out of the 
 Makefile with sed. 
 
 Thanks are due to Nicolas Williams (Nicolas.Williams@sun.com)
 who made me aware libpthread was not necessary, as its functionality
 was moved to libc in Solaris 10, with libpthread
 only provided for backwards compatibility. 
```

It also seems necessary to line up all the text below the star to get it all put into one item.



---

archive/issue_comments_049949.json:
```json
{
    "body": "My laptop battery is just about to give out, but with your spkg-install, sqlite did build fine on the t2 machine. I imagine this should be a positive review, then, but perhaps someone else should take a look.",
    "created_at": "2009-06-14T08:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49949",
    "user": "https://github.com/dandrake"
}
```

My laptop battery is just about to give out, but with your spkg-install, sqlite did build fine on the t2 machine. I imagine this should be a positive review, then, but perhaps someone else should take a look.



---

archive/issue_comments_049950.json:
```json
{
    "body": "Can you please post a link to the spkg?  I.e., you should make an sqlite-3.5.3.p4 spkg that has your updated spkg-install, SPKG.txt, and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory.  \n\nGiven that both you and ddrake claim to have tested this, both of you must have made a sqlite-3.5.3.p4.spkg.\n\nWilliam",
    "created_at": "2009-06-14T10:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49950",
    "user": "https://github.com/williamstein"
}
```

Can you please post a link to the spkg?  I.e., you should make an sqlite-3.5.3.p4 spkg that has your updated spkg-install, SPKG.txt, and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory.  

Given that both you and ddrake claim to have tested this, both of you must have made a sqlite-3.5.3.p4.spkg.

William



---

archive/issue_comments_049951.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> Can you please post a link to the spkg?  I.e., you should make an sqlite-3.5.3.p4 spkg that has your updated spkg-install, SPKG.txt, and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory.  \n> \n> Given that both you and ddrake claim to have tested this, both of you must have made a sqlite-3.5.3.p4.spkg.\n\nUpdated spkg is at http://sage.math.washington.edu/home/drake/sqlite-3.5.3.p4.spkg .",
    "created_at": "2009-06-14T23:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49951",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:6 was]:
> Can you please post a link to the spkg?  I.e., you should make an sqlite-3.5.3.p4 spkg that has your updated spkg-install, SPKG.txt, and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory.  
> 
> Given that both you and ddrake claim to have tested this, both of you must have made a sqlite-3.5.3.p4.spkg.

Updated spkg is at http://sage.math.washington.edu/home/drake/sqlite-3.5.3.p4.spkg .



---

archive/issue_comments_049952.json:
```json
{
    "body": "Thank you everyone for testing this. Sorry it was not in the exact format needed. Can someone explain what \"and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory.\" I'm not sure of the process there, so it would be good to know. Has someone actually done this stage now, or do I still need to do that bit? \n\nDave",
    "created_at": "2009-06-15T07:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49952",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you everyone for testing this. Sorry it was not in the exact format needed. Can someone explain what "and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory." I'm not sure of the process there, so it would be good to know. Has someone actually done this stage now, or do I still need to do that bit? 

Dave



---

archive/issue_comments_049953.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n> Thank you everyone for testing this. Sorry it was not in the exact format needed. Can someone explain what \"and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory.\" I'm not sure of the process there, so it would be good to know. Has someone actually done this stage now, or do I still need to do that bit? \n\n\"has them ci'd into the .hg repo\" means \"has them committed into the Mercurial repository\". I'm not sure how much you know about revision control software, but the idea is to record (\"commit\") the changes you've made. In the spkg I linked to above, I did that.\n\nWhen you're working on spkgs (patches, spkg-install, etc), the algorithm is more or less:\n\n* make your changes\n* increment the \"p number\" (here, 3.5.3.p3 -> 3.5.3.p4)\n* document them in SPKG.txt\n* do \"hg commit\" to commit the changes\n* tar up the directory with something like `tar jcf foo-1.2.3.p4.spkg foo-1.2.3.p4/`\n* post a link in a trac ticket for review\n\n(Anyone who knows more should correct me if there's a mistake there.)\n\nIf you'd like to learn more about Mercurial and source control, I recommend http://hgbook.red-bean.com/read/.",
    "created_at": "2009-06-15T09:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49953",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:8 drkirkby]:
> Thank you everyone for testing this. Sorry it was not in the exact format needed. Can someone explain what "and has them ci'd into the .hg repo that is in the sqlite-3.5.3.p3 directory." I'm not sure of the process there, so it would be good to know. Has someone actually done this stage now, or do I still need to do that bit? 

"has them ci'd into the .hg repo" means "has them committed into the Mercurial repository". I'm not sure how much you know about revision control software, but the idea is to record ("commit") the changes you've made. In the spkg I linked to above, I did that.

When you're working on spkgs (patches, spkg-install, etc), the algorithm is more or less:

* make your changes
* increment the "p number" (here, 3.5.3.p3 -> 3.5.3.p4)
* document them in SPKG.txt
* do "hg commit" to commit the changes
* tar up the directory with something like `tar jcf foo-1.2.3.p4.spkg foo-1.2.3.p4/`
* post a link in a trac ticket for review

(Anyone who knows more should correct me if there's a mistake there.)

If you'd like to learn more about Mercurial and source control, I recommend http://hgbook.red-bean.com/read/.



---

archive/issue_comments_049954.json:
```json
{
    "body": "Thank you, \n\nYou obviously checked the patch, made a few minor layout changes in SPKG.txt and created an updated .spkg file. I've just downloaded your spkg file and it works fine for me. So can this be changed to a positive review?  \n\nI've used CVS before, so am somewhat familiar with version control systems. There needs to be a server though, which tracks the changes. What's the username/password/location for the server? \n\nSo would you in this case have typed\n\n$ cd /home/drake/\n$ hg commit sqlite-3.5.3.p4.spkg\n\nThe other thing is, where is hg? I don't see it in my path anywhere. I could obviously build it from source. \n\nSorry to be so ignorant. \n\nDave",
    "created_at": "2009-06-15T23:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49954",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you, 

You obviously checked the patch, made a few minor layout changes in SPKG.txt and created an updated .spkg file. I've just downloaded your spkg file and it works fine for me. So can this be changed to a positive review?  

I've used CVS before, so am somewhat familiar with version control systems. There needs to be a server though, which tracks the changes. What's the username/password/location for the server? 

So would you in this case have typed

$ cd /home/drake/
$ hg commit sqlite-3.5.3.p4.spkg

The other thing is, where is hg? I don't see it in my path anywhere. I could obviously build it from source. 

Sorry to be so ignorant. 

Dave



---

archive/issue_comments_049955.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-06-15T23:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49955",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_049956.json:
```json
{
    "body": "The other thing is, who does the commit - the person creating the patch, or the reviewer?",
    "created_at": "2009-06-15T23:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49956",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The other thing is, who does the commit - the person creating the patch, or the reviewer?



---

archive/issue_comments_049957.json:
```json
{
    "body": "Just added my name as author.",
    "created_at": "2009-06-15T23:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49957",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Just added my name as author.



---

archive/issue_comments_049958.json:
```json
{
    "body": "positive review, and merged into 4.0.2.rc1",
    "created_at": "2009-06-15T23:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49958",
    "user": "https://github.com/williamstein"
}
```

positive review, and merged into 4.0.2.rc1



---

archive/issue_events_014671.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-06-15T23:40:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6266#event-14671"
}
```



---

archive/issue_comments_049959.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-15T23:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49959",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_049960.json:
```json
{
    "body": "Replying to [comment:10 drkirkby]:\n> I've used CVS before, so am somewhat familiar with version control systems. There needs to be a server though, which tracks the changes. What's the username/password/location for the server? \n> \n> So would you in this case have typed\n> \n> $ cd /home/drake/\n> $ hg commit sqlite-3.5.3.p4.spkg\n> \n> The other thing is, where is hg? I don't see it in my path anywhere. I could obviously build it from source. \n\nMercurial is a \"distributed version control system\", which doesn't require a central server. I'll build it on t2 and see if one of the admins can install it system-wide.",
    "created_at": "2009-06-16T00:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49960",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:10 drkirkby]:
> I've used CVS before, so am somewhat familiar with version control systems. There needs to be a server though, which tracks the changes. What's the username/password/location for the server? 
> 
> So would you in this case have typed
> 
> $ cd /home/drake/
> $ hg commit sqlite-3.5.3.p4.spkg
> 
> The other thing is, where is hg? I don't see it in my path anywhere. I could obviously build it from source. 

Mercurial is a "distributed version control system", which doesn't require a central server. I'll build it on t2 and see if one of the admins can install it system-wide.



---

archive/issue_comments_049961.json:
```json
{
    "body": "Thanks. \n\nIf its not installed on t2, how have you been doing updating before? \n\nBTW, I do have admin rights on t2 anyway. \n\nDave",
    "created_at": "2009-06-16T11:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49961",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thanks. 

If its not installed on t2, how have you been doing updating before? 

BTW, I do have admin rights on t2 anyway. 

Dave



---

archive/issue_comments_049962.json:
```json
{
    "body": "Replying to [comment:16 drkirkby]:\n> Thanks. \n> \n> If its not installed on t2, how have you been doing updating before? \n\nI just used a different machine; everyone has the same home directory on sage.math as on t2.\n\nAnd some admin person installed Mercurial, so it's now in /usr/local/bin...although it doesn't work unless you do \"`export  PYTHONPATH=/usr/local/lib/python2.4/site-packages/`\". Or some enterprising admin could edit /usr/local/bin/hg to have this before the first \"try:\" line:\n\n```\nimport sys\nsys.path.append('/usr/local/lib/python2.4/site-packages')\n```\n\nand then delete the \"import sys\" below.",
    "created_at": "2009-06-16T13:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6266#issuecomment-49962",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:16 drkirkby]:
> Thanks. 
> 
> If its not installed on t2, how have you been doing updating before? 

I just used a different machine; everyone has the same home directory on sage.math as on t2.

And some admin person installed Mercurial, so it's now in /usr/local/bin...although it doesn't work unless you do "`export  PYTHONPATH=/usr/local/lib/python2.4/site-packages/`". Or some enterprising admin could edit /usr/local/bin/hg to have this before the first "try:" line:

```
import sys
sys.path.append('/usr/local/lib/python2.4/site-packages')
```

and then delete the "import sys" below.
