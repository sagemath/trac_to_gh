# Issue 3122: after make install, sage tries to write in /usr/local

archive/issues_003122.json:
```json
{
    "body": "Assignee: cwitty\n\nI compiled sage-3.0 on the machines of my lab, and installed it under /usr/local/sage-3.0 with make install DESTDIR=/usr/local/sage-3.0.\nI am the Unix owner of the files under /usr/local/sage-3.0. When I run sage myself, it is ok. However, when other people in my lab run it, they get:\n\n```\n< bissogae@hector:~$ sage\n< ----------------------------------------------------------------------\n< | SAGE Version 3.0, Release Date: 2008-04-23                         |\n< | Type notebook() for the GUI, and license() for information.        |\n< ----------------------------------------------------------------------\n< Traceback (most recent call last):\n<   File \"/usr/local/sage-3.0/sage/local/bin/sage-location\", line 66, in <module>\n<     t, R = install_moved()\n<   File \"/usr/local/sage-3.0/sage/local/bin/sage-location\", line 11, in install_moved\n<     O = open(location_file,'w')\n< IOError: [Errno 13] Permission denied: '/usr/local/sage-3.0/sage/local/lib/sage-current-location.txt'\n<\n< sage:\n```\n\nI'm not sure it is ok that SAGE writes in /usr/local...\n\nIssue created by migration from https://trac.sagemath.org/ticket/3122\n\n",
    "created_at": "2008-05-07T12:46:05Z",
    "labels": [
        "relocation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "after make install, sage tries to write in /usr/local",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3122",
    "user": "zimmerma"
}
```
Assignee: cwitty

I compiled sage-3.0 on the machines of my lab, and installed it under /usr/local/sage-3.0 with make install DESTDIR=/usr/local/sage-3.0.
I am the Unix owner of the files under /usr/local/sage-3.0. When I run sage myself, it is ok. However, when other people in my lab run it, they get:

```
< bissogae@hector:~$ sage
< ----------------------------------------------------------------------
< | SAGE Version 3.0, Release Date: 2008-04-23                         |
< | Type notebook() for the GUI, and license() for information.        |
< ----------------------------------------------------------------------
< Traceback (most recent call last):
<   File "/usr/local/sage-3.0/sage/local/bin/sage-location", line 66, in <module>
<     t, R = install_moved()
<   File "/usr/local/sage-3.0/sage/local/bin/sage-location", line 11, in install_moved
<     O = open(location_file,'w')
< IOError: [Errno 13] Permission denied: '/usr/local/sage-3.0/sage/local/lib/sage-current-location.txt'
<
< sage:
```

I'm not sure it is ok that SAGE writes in /usr/local...

Issue created by migration from https://trac.sagemath.org/ticket/3122





---

archive/issue_comments_021630.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-07T12:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21630",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021631.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2008-05-07T12:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21631",
    "user": "mabshoff"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_021632.json:
```json
{
    "body": "Hi Paul,\n\nI am curious if you started Sage after running \"make install\". Starting Sage once after running the make install is needed so that the pyc files are recreated. After that Sage should not need to have write access to anything outside `~/.sage`. So I consider this a blocker. We must make the deployment of Sage as simple as possible and this includes having Sage in multi user environments.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-07T12:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21632",
    "user": "mabshoff"
}
```

Hi Paul,

I am curious if you started Sage after running "make install". Starting Sage once after running the make install is needed so that the pyc files are recreated. After that Sage should not need to have write access to anything outside `~/.sage`. So I consider this a blocker. We must make the deployment of Sage as simple as possible and this includes having Sage in multi user environments.

Cheers,

Michael



---

archive/issue_comments_021633.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-05-07T12:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21633",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_021634.json:
```json
{
    "body": "It seems the touching /usr/local is caused by the \"Sage moved\" script, so I assume that the best \"fix\" is to print a better error message?",
    "created_at": "2008-08-16T23:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21634",
    "user": "malb"
}
```

It seems the touching /usr/local is caused by the "Sage moved" script, so I assume that the best "fix" is to print a better error message?



---

archive/issue_comments_021635.json:
```json
{
    "body": "I agree this issue seems closely related to #1830. So fixing this issue will also likely solve that ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-15T04:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21635",
    "user": "mabshoff"
}
```

I agree this issue seems closely related to #1830. So fixing this issue will also likely solve that ticket.

Cheers,

Michael



---

archive/issue_comments_021636.json:
```json
{
    "body": "This patch is to the main makefile and is a classic patch, i.e. no hg here",
    "created_at": "2008-12-01T08:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21636",
    "user": "mabshoff"
}
```

This patch is to the main makefile and is a classic patch, i.e. no hg here



---

archive/issue_comments_021637.json:
```json
{
    "body": "Attachment [trac_3122.patch](tarball://root/attachments/some-uuid/ticket3122/trac_3122.patch) by mabshoff created at 2008-12-01 08:45:19\n\nThe hopefully final patch for 3.2.1.rc1 :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T08:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21637",
    "user": "mabshoff"
}
```

Attachment [trac_3122.patch](tarball://root/attachments/some-uuid/ticket3122/trac_3122.patch) by mabshoff created at 2008-12-01 08:45:19

The hopefully final patch for 3.2.1.rc1 :)

Cheers,

Michael



---

archive/issue_comments_021638.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-01T08:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21638",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021639.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-12-01T08:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21639",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc1



---

archive/issue_comments_021640.json:
```json
{
    "body": "Looking at the problem again it seems that there might be another problem here. Several possibilities\n\n* other people ran sage before Paul did, hence sage-location was executed. We fixed that bug\n* somebody else has mounted the directory with sage in a different location than Paul in which case sage_location will cause the above error. There is nothing we can do in that case since the pyc files have to be recreated\n\nPaul: If this is still a problem please let us know and open a new ticket with specific steps to reproduce and plenty of information.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T09:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3122#issuecomment-21640",
    "user": "mabshoff"
}
```

Looking at the problem again it seems that there might be another problem here. Several possibilities

* other people ran sage before Paul did, hence sage-location was executed. We fixed that bug
* somebody else has mounted the directory with sage in a different location than Paul in which case sage_location will cause the above error. There is nothing we can do in that case since the pyc files have to be recreated

Paul: If this is still a problem please let us know and open a new ticket with specific steps to reproduce and plenty of information.

Cheers,

Michael
