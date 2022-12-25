# Issue 9977: Add a test for the maths library in the 'prereq' script.

archive/issues_009977.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jhpalmieri @nthiery\n\nThe 'prereq' script in `$SAGE_ROOT/spkg/base` is currently version 0.7. This does not check that the maths library `libm` exists. I thought that was pretty much a formality, but it is not on AIX, where the shared maths library `/usr/lib/libm.a` does not get installed by default. \n\n\n```\n-bash-4.1$ ls /usr/lib/libm*\n/usr/lib/libmbx.a\n```\n\n\nThe maths library is part of the `bos.adt` fileset. Hence a test for the maths library should be added. After installing `bos.adt`, so the maths library exists:\n\n\n```\n-bash-4.1$ ls /usr/lib/libm*\n/usr/lib/libm.a       /usr/lib/libmbx.a     /usr/lib/libm_r.a     /usr/lib/libmsaa.a    /usr/lib/libmsaa_r.a\n```\n\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9978\n\n",
    "created_at": "2010-09-23T13:46:47Z",
    "labels": [
        "component: aix or hp-ux ports",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Add a test for the maths library in the 'prereq' script.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9977",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jhpalmieri @nthiery

The 'prereq' script in `$SAGE_ROOT/spkg/base` is currently version 0.7. This does not check that the maths library `libm` exists. I thought that was pretty much a formality, but it is not on AIX, where the shared maths library `/usr/lib/libm.a` does not get installed by default. 


```
-bash-4.1$ ls /usr/lib/libm*
/usr/lib/libmbx.a
```


The maths library is part of the `bos.adt` fileset. Hence a test for the maths library should be added. After installing `bos.adt`, so the maths library exists:


```
-bash-4.1$ ls /usr/lib/libm*
/usr/lib/libm.a       /usr/lib/libmbx.a     /usr/lib/libm_r.a     /usr/lib/libmsaa.a    /usr/lib/libmsaa_r.a
```


Dave

Issue created by migration from https://trac.sagemath.org/ticket/9978





---

archive/issue_comments_100127.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2011-03-28T18:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100127",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_100128.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-28T18:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100128",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_100129.json:
```json
{
    "body": "Changing component from AIX or HP-UX ports to build.",
    "created_at": "2011-03-28T18:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100129",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from AIX or HP-UX ports to build.



---

archive/issue_comments_100130.json:
```json
{
    "body": "I read the patch and it looks good. I haven't tested it, though.",
    "created_at": "2011-03-29T08:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100130",
    "user": "https://github.com/malb"
}
```

I read the patch and it looks good. I haven't tested it, though.



---

archive/issue_comments_100131.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> I read the patch and it looks good. I haven't tested it, though.\nThank you.",
    "created_at": "2011-03-29T08:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100131",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:2 malb]:
> I read the patch and it looks good. I haven't tested it, though.
Thank you.



---

archive/issue_comments_100132.json:
```json
{
    "body": "Here is some results when installed on my IBM RS/6000, which runs AIX 5.3. \n\n\n```\n-bash-4.1$ uname\nAIX\n```\n\n\nHere's the output after running \"make\" on the AIX system, which has the maths library installed, since the bos.adt fileset was installed. \n\n\n```\n-bash-4.1$ uname \nAIX\n-bash-4.1$ make\n\n<snip irrelevant output>\n\nStarting prerequisite check.\nMachine: AIX aixbox 3 5 000245984C00\nprereq-0.8/\nprereq-0.8/install-sh\nprereq-0.8/aclocal.m4\n\n<snip out irrelevant output>\n\nchecking for sqrt in -lm... yes\nchecking for sqrtl in -lm... yes\nconfigure: creating ./config.status\nconfig.status: creating Makefile\nconfig.status: creating config.h\nconfig.status: executing depfiles commands\n```\n\n\nThen I removed the maths library, /usr/lib/libm.a.\n\n\n```\n-bash-4.1$ su\nroot's Password:\n# mv /usr/lib/libm.a /usr/lib/foo\n# exit\n```\n\n\nThen after running make, we see that the 'prereq' script exits with an error. \n\n\n```\nchecking for sqrt in -lm... no\nconfigure: This system has no maths library installed.\nconfigure: On AIX, this is in the bos.adt.libm fileset.\nconfigure: Actually, we recommend to install the complete bos.adt fileset.\nconfigure: This needs to be performed by a system administrator.\nconfigure: error: Exiting, since a maths library was not found.\n ERROR: You do not have all of the prerequisites needed\n to build Sage from source.  See the errors above.\nmake[1]: *** [installed/prereq-0.8] Error 1\nmake[1]: Leaving directory `/home/users/drkirkby/sage-4.7.alpha1/spkg'\n\nreal    0m54.880s\nuser    0m29.577s\nsys     0m10.611s\nError building Sage.\nmake: *** [build] Error 1\n```\n\n\nFinally, I did manage to remember to restore my maths library!\n\n\n```\n-bash-4.1$ su\nroot's Password:\n# mv /usr/lib/foo /usr/lib/libm.a\n# exit\n-bash-4.1$ \n```\n",
    "created_at": "2011-03-29T09:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100132",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Here is some results when installed on my IBM RS/6000, which runs AIX 5.3. 


```
-bash-4.1$ uname
AIX
```


Here's the output after running "make" on the AIX system, which has the maths library installed, since the bos.adt fileset was installed. 


```
-bash-4.1$ uname 
AIX
-bash-4.1$ make

<snip irrelevant output>

Starting prerequisite check.
Machine: AIX aixbox 3 5 000245984C00
prereq-0.8/
prereq-0.8/install-sh
prereq-0.8/aclocal.m4

<snip out irrelevant output>

checking for sqrt in -lm... yes
checking for sqrtl in -lm... yes
configure: creating ./config.status
config.status: creating Makefile
config.status: creating config.h
config.status: executing depfiles commands
```


Then I removed the maths library, /usr/lib/libm.a.


```
-bash-4.1$ su
root's Password:
# mv /usr/lib/libm.a /usr/lib/foo
# exit
```


Then after running make, we see that the 'prereq' script exits with an error. 


```
checking for sqrt in -lm... no
configure: This system has no maths library installed.
configure: On AIX, this is in the bos.adt.libm fileset.
configure: Actually, we recommend to install the complete bos.adt fileset.
configure: This needs to be performed by a system administrator.
configure: error: Exiting, since a maths library was not found.
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.8] Error 1
make[1]: Leaving directory `/home/users/drkirkby/sage-4.7.alpha1/spkg'

real    0m54.880s
user    0m29.577s
sys     0m10.611s
Error building Sage.
make: *** [build] Error 1
```


Finally, I did manage to remember to restore my maths library!


```
-bash-4.1$ su
root's Password:
# mv /usr/lib/foo /usr/lib/libm.a
# exit
-bash-4.1$ 
```




---

archive/issue_comments_100133.json:
```json
{
    "body": "Nicolas M. Thi\u00e9ry wrote on sage-devel\n\n\n```\nI did not actually run the code, especially on AIX, but trust you did\n(both with and without libm installed). Reading it sounds very\nreasonable; I am thus ready to give it a positive review.\n\nQuick variant:\n\n    # On AIX libm is not installed by default - strange as that might seem -\n    # While we are it, bos.adt is likely to contain other useful things for Sage\n    if test \"x`uname`\" = 'xAIX'\n    then\n       AC_MSG_NOTICE([On AIX, libm is contained in the bos.adt.libm fileset.]) \n       AC_MSG_NOTICE([Actually, we recommend to install the complete bos.adt fileset.]) \n\nCheers,\n\t\t\t\tNicolas\n```\n\n\nThe patch has been changed to include Nicolas's revised wording on the error message that is generated.",
    "created_at": "2011-03-29T23:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100133",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Nicolas M. Thiéry wrote on sage-devel


```
I did not actually run the code, especially on AIX, but trust you did
(both with and without libm installed). Reading it sounds very
reasonable; I am thus ready to give it a positive review.

Quick variant:

    # On AIX libm is not installed by default - strange as that might seem -
    # While we are it, bos.adt is likely to contain other useful things for Sage
    if test "x`uname`" = 'xAIX'
    then
       AC_MSG_NOTICE([On AIX, libm is contained in the bos.adt.libm fileset.]) 
       AC_MSG_NOTICE([Actually, we recommend to install the complete bos.adt fileset.]) 

Cheers,
				Nicolas
```


The patch has been changed to include Nicolas's revised wording on the error message that is generated.



---

archive/issue_comments_100134.json:
```json
{
    "body": "Somehow I managed to remove John. I've put him back!",
    "created_at": "2011-03-29T23:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100134",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Somehow I managed to remove John. I've put him back!



---

archive/issue_comments_100135.json:
```json
{
    "body": "Attachment [9978-Changes-to-configure.ac.diff](tarball://root/attachments/some-uuid/ticket9978/9978-Changes-to-configure.ac.diff) by drkirkby created at 2011-03-30 16:21:29\n\nChanges to the configure.ac file which check that sqrt exists in the maths library.",
    "created_at": "2011-03-30T16:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100135",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9978-Changes-to-configure.ac.diff](tarball://root/attachments/some-uuid/ticket9978/9978-Changes-to-configure.ac.diff) by drkirkby created at 2011-03-30 16:21:29

Changes to the configure.ac file which check that sqrt exists in the maths library.



---

archive/issue_comments_100136.json:
```json
{
    "body": "New tar file. This does not need reviewing. Changes from prereq-0.7.tar are due to changes in the configure.ac file, which is in the tar file",
    "created_at": "2011-03-30T16:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100136",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

New tar file. This does not need reviewing. Changes from prereq-0.7.tar are due to changes in the configure.ac file, which is in the tar file



---

archive/issue_comments_100137.json:
```json
{
    "body": "Attachment [prereq-0.8.tar](tarball://root/attachments/some-uuid/ticket9978/prereq-0.8.tar) by drkirkby created at 2011-03-30 16:39:32\n\nI realised that I had not used Nicolas's exact wording for one of the messages, which was better than my own. Hence I have rebuilt the tar file. I checked again on AIX, and this is what it produced when I temporarily removed the maths library `/usr/lib/libm.a`\n\n\n\n```\nchecking for sqrt in -lm... no\nconfigure: This system has no maths library installed.\nconfigure: On AIX, libm is contained in the bos.adt.libm fileset.\nconfigure: Actually, we recommend to install the complete bos.adt fileset.\nconfigure: This needs to be performed by a system administrator.\nconfigure: error: Exiting, since a maths library was not found.\n ERROR: You do not have all of the prerequisites needed\n to build Sage from source.  See the errors above.\nmake[1]: *** [installed/prereq-0.8] Error 1\nmake[1]: Leaving directory `/home/users/drkirkby/sage-4.7.alpha1/spkg'\n\nreal    0m55.207s\nuser    0m29.541s\nsys     0m10.628s\nError building Sage.\nmake: *** [build] Error 1\n```\n",
    "created_at": "2011-03-30T16:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100137",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [prereq-0.8.tar](tarball://root/attachments/some-uuid/ticket9978/prereq-0.8.tar) by drkirkby created at 2011-03-30 16:39:32

I realised that I had not used Nicolas's exact wording for one of the messages, which was better than my own. Hence I have rebuilt the tar file. I checked again on AIX, and this is what it produced when I temporarily removed the maths library `/usr/lib/libm.a`



```
checking for sqrt in -lm... no
configure: This system has no maths library installed.
configure: On AIX, libm is contained in the bos.adt.libm fileset.
configure: Actually, we recommend to install the complete bos.adt fileset.
configure: This needs to be performed by a system administrator.
configure: error: Exiting, since a maths library was not found.
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.8] Error 1
make[1]: Leaving directory `/home/users/drkirkby/sage-4.7.alpha1/spkg'

real    0m55.207s
user    0m29.541s
sys     0m10.628s
Error building Sage.
make: *** [build] Error 1
```




---

archive/issue_comments_100138.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-30T17:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100138",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_010104.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-05T11:59:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9977#event-10104"
}
```



---

archive/issue_comments_100139.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-05T11:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9977#issuecomment-100139",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
