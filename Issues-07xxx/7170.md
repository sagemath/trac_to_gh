# Issue 7170: HP-UX failure of rubiks as no 'install' program.

archive/issues_007170.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  david.kirkby@onetel.ne @dimpase\n\nKeywords: HP-UX install\n\nI think we should either \n\n* check for the program 'install' in a modifed 'prereq' script\n* Make use of 'cp' installed. \n* include an 'install'  \n\n\n```\n       gcc -O2 -g twist.c  -o twist\n        mkdir -p /home/drkirkby/sage-4.1.2.rc0/local/bin\n        no install in /home/drkirkby/sage-4.1.2.rc0 /home/drkirkby/sage-4.1.2.rc0/local/bin /home/drkirkby/sage-4.1.2.rc0 /home/drkirkby/sage-4.1.2.rc0/local/bin /usr/local/bin /usr/bin /opt/ansic/bin /usr/ccs/bin /usr/contrib/bin /opt/mpi/bin /opt/hparray/bin /opt/nettladm/bin /opt/upgrade/bin /opt/fcms/bin /usr/bin/X11 /usr/contrib/bin/X11 /opt/graphics/common/bin /opt/pd/bin /opt/resmon/bin /opt/mozilla /opt/netscape /usr/local/bin /opt/gnome/bin /opt/graphics/phigs/bin /opt/OpenSource/bin /usr/sbin/diag/contrib /opt/wbem/bin /opt/wbem/sbin /opt/hp-gcc/bin /opt/aCC/bin /opt/cadvise/bin /opt/sentinel/bin /opt/langtools/bin . /opt/kirkby/bin reid/optimal /home/drkirkby/sage-4.1.2.rc0/local/bin\nMake: Cannot load no.  Stop.\n*** Error exit code 1\n\nStop.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7170\n\n",
    "closed_at": "2020-04-26T07:25:34Z",
    "created_at": "2009-10-10T07:43:05Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "HP-UX failure of rubiks as no 'install' program.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7170",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  david.kirkby@onetel.ne @dimpase

Keywords: HP-UX install

I think we should either 

* check for the program 'install' in a modifed 'prereq' script
* Make use of 'cp' installed. 
* include an 'install'  


```
       gcc -O2 -g twist.c  -o twist
        mkdir -p /home/drkirkby/sage-4.1.2.rc0/local/bin
        no install in /home/drkirkby/sage-4.1.2.rc0 /home/drkirkby/sage-4.1.2.rc0/local/bin /home/drkirkby/sage-4.1.2.rc0 /home/drkirkby/sage-4.1.2.rc0/local/bin /usr/local/bin /usr/bin /opt/ansic/bin /usr/ccs/bin /usr/contrib/bin /opt/mpi/bin /opt/hparray/bin /opt/nettladm/bin /opt/upgrade/bin /opt/fcms/bin /usr/bin/X11 /usr/contrib/bin/X11 /opt/graphics/common/bin /opt/pd/bin /opt/resmon/bin /opt/mozilla /opt/netscape /usr/local/bin /opt/gnome/bin /opt/graphics/phigs/bin /opt/OpenSource/bin /usr/sbin/diag/contrib /opt/wbem/bin /opt/wbem/sbin /opt/hp-gcc/bin /opt/aCC/bin /opt/cadvise/bin /opt/sentinel/bin /opt/langtools/bin . /opt/kirkby/bin reid/optimal /home/drkirkby/sage-4.1.2.rc0/local/bin
Make: Cannot load no.  Stop.
*** Error exit code 1

Stop.

```


Issue created by migration from https://trac.sagemath.org/ticket/7170





---

archive/issue_comments_059316.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-10-10T07:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7170#issuecomment-59316",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_059317.json:
```json
{
    "body": "It should be noted, Solaris comes with no install program either, except one in /usr/sbin, which would not be in a normal users path (only root).",
    "created_at": "2009-10-10T07:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7170#issuecomment-59317",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It should be noted, Solaris comes with no install program either, except one in /usr/sbin, which would not be in a normal users path (only root).



---

archive/issue_comments_059318.json:
```json
{
    "body": "Changing component from porting to AIX or HP-UX ports.",
    "created_at": "2011-02-16T22:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7170#issuecomment-59318",
    "user": "https://github.com/kcrisman"
}
```

Changing component from porting to AIX or HP-UX ports.



---

archive/issue_events_016960.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-04-25T02:59:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7170#event-16960"
}
```



---

archive/issue_comments_059319.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-25T02:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7170#issuecomment-59319",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059320.json:
```json
{
    "body": "outdated, should be closed",
    "created_at": "2020-04-25T02:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7170#issuecomment-59320",
    "user": "https://github.com/mkoeppe"
}
```

outdated, should be closed



---

archive/issue_comments_059321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-04-25T04:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7170#issuecomment-59321",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059322.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-26T07:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7170#issuecomment-59322",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_016961.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-04-26T07:25:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7170",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7170#event-16961"
}
```
