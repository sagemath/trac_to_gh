# Issue 7783: 3d graphics (viewed with jmol) do not work from the command line on OS X 10.6 sage-4.3

archive/issues_007783.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: sphere()\n```\n\n\ndoesn't work.  The same from the Sage notebook works fine. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7783\n\n",
    "created_at": "2009-12-29T06:28:44Z",
    "labels": [
        "component: graphics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "3d graphics (viewed with jmol) do not work from the command line on OS X 10.6 sage-4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7783",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: sphere()
```


doesn't work.  The same from the Sage notebook works fine. 

Issue created by migration from https://trac.sagemath.org/ticket/7783





---

archive/issue_comments_066996.json:
```json
{
    "body": "Actually, all command line 3d graphics are broken in sage-4.3.   I just tried on one of the linux binaries and found this too:\n\n\n```\nwstein@ubuntu910-64:/tmp/wstein/farm/sage-4.3$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: !sage-native-execute local/bin/jmol\nJmol.jar not found\n```\n\n| Sage Version 4.3, Release Date: 2009-12-24                         |\n| Type notebook() for the GUI, and license() for information.        |\nThis is yet more fallout from changing the sagenb to use setuptools instead of distutils. The problem is that the jmol script says this:\n\n```/bin/sh\nJMOL_HOME=\"$SAGE_LOCAL/lib/python/site-packages/sagenb/data/jmol\"\n...\n```\n\n\nHowever, look at site-packages now:\n\n```\n...\nsagenb-0.4.8-py2.6.egg\n...\n```\n\n\nDoing this makes the problem disappear:\n\n```\n$  cd sage-4.3/local/lib/python/site-packages\n$  ln -s sagenb-0.4.8-py2.6.egg/sagenb .\n```\n",
    "created_at": "2009-12-29T07:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-66996",
    "user": "https://github.com/williamstein"
}
```

Actually, all command line 3d graphics are broken in sage-4.3.   I just tried on one of the linux binaries and found this too:


```
wstein@ubuntu910-64:/tmp/wstein/farm/sage-4.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: !sage-native-execute local/bin/jmol
Jmol.jar not found
```

| Sage Version 4.3, Release Date: 2009-12-24                         |
| Type notebook() for the GUI, and license() for information.        |
This is yet more fallout from changing the sagenb to use setuptools instead of distutils. The problem is that the jmol script says this:

```/bin/sh
JMOL_HOME="$SAGE_LOCAL/lib/python/site-packages/sagenb/data/jmol"
...
```


However, look at site-packages now:

```
...
sagenb-0.4.8-py2.6.egg
...
```


Doing this makes the problem disappear:

```
$  cd sage-4.3/local/lib/python/site-packages
$  ln -s sagenb-0.4.8-py2.6.egg/sagenb .
```




---

archive/issue_comments_066997.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2009-12-29T07:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-66997",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_066998.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-29T07:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-66998",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066999.json:
```json
{
    "body": "Attachment [sagenb_7783.patch](tarball://root/attachments/some-uuid/ticket7783/sagenb_7783.patch) by @TimDumol created at 2009-12-29 08:40:50\n\nApply this patch alone to the sagenb repo. Updates scripts to use pkg_resources to look for sagenb.",
    "created_at": "2009-12-29T08:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-66999",
    "user": "https://github.com/TimDumol"
}
```

Attachment [sagenb_7783.patch](tarball://root/attachments/some-uuid/ticket7783/sagenb_7783.patch) by @TimDumol created at 2009-12-29 08:40:50

Apply this patch alone to the sagenb repo. Updates scripts to use pkg_resources to look for sagenb.



---

archive/issue_comments_067000.json:
```json
{
    "body": "Attachment [trac_7783-sage-scripts.patch](tarball://root/attachments/some-uuid/ticket7783/trac_7783-sage-scripts.patch) by @TimDumol created at 2009-12-29 08:41:26\n\nApply this patch alone to the sage scripts repo. Adds a script that uses pkg_resources to find the location of a given package.",
    "created_at": "2009-12-29T08:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-67000",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7783-sage-scripts.patch](tarball://root/attachments/some-uuid/ticket7783/trac_7783-sage-scripts.patch) by @TimDumol created at 2009-12-29 08:41:26

Apply this patch alone to the sage scripts repo. Adds a script that uses pkg_resources to find the location of a given package.



---

archive/issue_comments_067001.json:
```json
{
    "body": "Unfortunately the solution in sagenb_7783.patch does not play well with `setup.py develop`. Any changes made to the packages in that mode will not be propagated. These two new patches use `pkg_resources` to find the location of the sagenb package.",
    "created_at": "2009-12-29T08:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-67001",
    "user": "https://github.com/TimDumol"
}
```

Unfortunately the solution in sagenb_7783.patch does not play well with `setup.py develop`. Any changes made to the packages in that mode will not be propagated. These two new patches use `pkg_resources` to find the location of the sagenb package.



---

archive/issue_comments_067002.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-29T09:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-67002",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067003.json:
```json
{
    "body": "Your solution is better in the long run.  \n\nPositive review. \n\n**IMPORTANT NOTE TO Release MANAGER**\n\nApply trac_7783-sage-scripts.patch then \n\n```\nchmod +x local/bin/sage-pypkg-location \n```\n\n\n!!\n\nI have applied trac_7783-sagenb-scripts.patch to the official sagenb repo and merged it into sagenb-0.4.9.",
    "created_at": "2009-12-29T09:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-67003",
    "user": "https://github.com/williamstein"
}
```

Your solution is better in the long run.  

Positive review. 

**IMPORTANT NOTE TO Release MANAGER**

Apply trac_7783-sage-scripts.patch then 

```
chmod +x local/bin/sage-pypkg-location 
```


!!

I have applied trac_7783-sagenb-scripts.patch to the official sagenb repo and merged it into sagenb-0.4.9.



---

archive/issue_comments_067004.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T20:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7783#issuecomment-67004",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007999.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-03T20:44:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7783",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7783#event-7999"
}
```
