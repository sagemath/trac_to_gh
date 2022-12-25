# Issue 9477: jmol shows a black screen in the notebook, it works fine in the reference manual

archive/issues_009477.json:
```json
{
    "body": "Assignee: olazo\n\nKeywords: jmol\n\nI get the following error message in the log of my notebook when I try to show a 3d plot with jmol:\n\n\n```\nscript compiler ERROR: se esperaba una instrucci\u00f3n\n----line 1 command 1 of /home/admin/0/cells/30/sage0-size500.jmol?1278886612:\n          >>>> <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\"> <<<<\nERROR en gui\u00f3n: script compiler ERROR: se esperaba una instrucci\u00f3n\n----line 1 command 1 of /home/admin/0/cells/30/sage0-size500.jmol?1278886612:\n          >>>> <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\"> <<<<\neval ERROR: \n----line 1 command 1:\n         script >> \"/home/admin/0/cells/30/sage0-size500.jmol?1278886612\" <<\n```\n\n\nJmol loads, and shows a black screen instead of the actual plot.\n\nIf I try the exact same plot in the cells in the reference manual, the plot shows perfectly and no error message appears in the log.\n\nThis seems to me rather like the opposite to #3167 in which things worked fine in the notebook but not in the help\n\nIssue created by migration from https://trac.sagemath.org/ticket/9477\n\n",
    "created_at": "2010-07-11T22:24:13Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "jmol shows a black screen in the notebook, it works fine in the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9477",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: olazo

Keywords: jmol

I get the following error message in the log of my notebook when I try to show a 3d plot with jmol:


```
script compiler ERROR: se esperaba una instrucción
----line 1 command 1 of /home/admin/0/cells/30/sage0-size500.jmol?1278886612:
          >>>> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"> <<<<
ERROR en guión: script compiler ERROR: se esperaba una instrucción
----line 1 command 1 of /home/admin/0/cells/30/sage0-size500.jmol?1278886612:
          >>>> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"> <<<<
eval ERROR: 
----line 1 command 1:
         script >> "/home/admin/0/cells/30/sage0-size500.jmol?1278886612" <<
```


Jmol loads, and shows a black screen instead of the actual plot.

If I try the exact same plot in the cells in the reference manual, the plot shows perfectly and no error message appears in the log.

This seems to me rather like the opposite to #3167 in which things worked fine in the notebook but not in the help

Issue created by migration from https://trac.sagemath.org/ticket/9477





---

archive/issue_comments_090831.json:
```json
{
    "body": "It may be important to mention that the following command does not popup a jmol window in the command line:\n\n\n```\nsage: a=point3d([0,0,0])\nsage: a.show()\n```\n\n\nBut, if I use:\n\n\n```\nsage: a.export_jmol('/home/oscar/point')\n```\n\n\na zip file containing a SCRIPT file appears there, and I can use:\n\n\n```\nsage: !java -jar /home/cwitty/sage-4.4.4/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/Jmol.jar}}}\n\nto make jmol open in my desktop, and I can then use it to open the SCRIPT file, and it shows the point just fine.",
    "created_at": "2010-07-11T22:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9477#issuecomment-90831",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

It may be important to mention that the following command does not popup a jmol window in the command line:


```
sage: a=point3d([0,0,0])
sage: a.show()
```


But, if I use:


```
sage: a.export_jmol('/home/oscar/point')
```


a zip file containing a SCRIPT file appears there, and I can use:


```
sage: !java -jar /home/cwitty/sage-4.4.4/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/Jmol.jar}}}

to make jmol open in my desktop, and I can then use it to open the SCRIPT file, and it shows the point just fine.



---

archive/issue_comments_090832.json:
```json
{
    "body": "Oscar, can you verify whether this is still happening for you?   Given how much the notebook has changed in the meantime it might be hard to track this down, and it looks like something akin to #3167 [is back](https://github.com/sagemath/sagenb/issues/179).  I think this would be worth closing unless we have more information.",
    "created_at": "2014-05-28T00:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9477#issuecomment-90832",
    "user": "https://github.com/kcrisman"
}
```

Oscar, can you verify whether this is still happening for you?   Given how much the notebook has changed in the meantime it might be hard to track this down, and it looks like something akin to #3167 [is back](https://github.com/sagemath/sagenb/issues/179).  I think this would be worth closing unless we have more information.



---

archive/issue_comments_090833.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Oscar, can you verify whether this is still happening for you?   Given how much the notebook has changed in the meantime it might be hard to track this down, and it looks like something akin to #3167 [is back](https://github.com/sagemath/sagenb/issues/179).  I think this would be worth closing unless we have more information.\n\nThis no longer happens to me. I am currently using sage version 5.0 (though I expect it to be safe to assume that sage 6 won't make the problem come back). If I remember correctly this had to do more with the implementation of java in firefox than with jmol or sage at all. I think I fixed this by using the privative version of the java plugin for firefox. However, icedtea works just fine now that I use a more recent version of it. I suggest this ticket to be closed. Cheers!",
    "created_at": "2014-05-28T01:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9477#issuecomment-90833",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Replying to [comment:5 kcrisman]:
> Oscar, can you verify whether this is still happening for you?   Given how much the notebook has changed in the meantime it might be hard to track this down, and it looks like something akin to #3167 [is back](https://github.com/sagemath/sagenb/issues/179).  I think this would be worth closing unless we have more information.

This no longer happens to me. I am currently using sage version 5.0 (though I expect it to be safe to assume that sage 6 won't make the problem come back). If I remember correctly this had to do more with the implementation of java in firefox than with jmol or sage at all. I think I fixed this by using the privative version of the java plugin for firefox. However, icedtea works just fine now that I use a more recent version of it. I suggest this ticket to be closed. Cheers!



---

archive/issue_comments_090834.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-05-28T15:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9477#issuecomment-90834",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090835.json:
```json
{
    "body": "Thanks!  Very helpful.",
    "created_at": "2014-05-28T15:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9477#issuecomment-90835",
    "user": "https://github.com/kcrisman"
}
```

Thanks!  Very helpful.



---

archive/issue_comments_090836.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-28T15:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9477#issuecomment-90836",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090837.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-05-29T11:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9477#issuecomment-90837",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
