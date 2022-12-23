# Issue 8619: add check for SELinux to sage prereq script

archive/issues_008619.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\n\n```\nSELINUX\n--------\n\nOn Linux, if you get this error message:\n\n    \" restore segment prot after reloc: Permission denied \"\n\nthe problem is probably related to SELinux. See the following URL for\nfurther information:\n\n```\n\n\n    http://www.ittvis.com/services/techtip.asp?ttid=3092\n\nIt would be better if the prereq script when sage first builds were to check for selinux.   This could be done possibly following the above link which says to look at /etc/sysconfig/selinux.  \n\nThere are some relevant emails in late March 2010 from John Bussoletti in sage-support about this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8619\n\n",
    "created_at": "2010-03-28T19:09:54Z",
    "labels": [
        "build",
        "minor",
        "enhancement"
    ],
    "title": "add check for SELinux to sage prereq script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8619",
    "user": "was"
}
```
Assignee: GeorgSWeber


```
SELINUX
--------

On Linux, if you get this error message:

    " restore segment prot after reloc: Permission denied "

the problem is probably related to SELinux. See the following URL for
further information:

```


    http://www.ittvis.com/services/techtip.asp?ttid=3092

It would be better if the prereq script when sage first builds were to check for selinux.   This could be done possibly following the above link which says to look at /etc/sysconfig/selinux.  

There are some relevant emails in late March 2010 from John Bussoletti in sage-support about this.

Issue created by migration from https://trac.sagemath.org/ticket/8619





---

archive/issue_comments_078108.json:
```json
{
    "body": "\n```\nThe command \"sestatus\" returns the following text on my system:\n       SELinux Status:                 enabled\n       SELinuxfs mount:                /selinux\n       Current mode:                   permissive\n       Mode from config file:          permissive\n       Policy version:                 24\n       Policy from config file:                targeted\n\nSo it seems that if you grep for \"Current mode\" and find either \"disabled\"\nor \"permissive\", sage should build, but if you encounter \"enabled\" then it\nmay fail to build those apps that make the stack executable.\n\nOn my system sestatus is in /usr/sbin.\n\nJohn Bussoletti\n```\n",
    "created_at": "2010-03-29T04:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8619#issuecomment-78108",
    "user": "was"
}
```


```
The command "sestatus" returns the following text on my system:
       SELinux Status:                 enabled
       SELinuxfs mount:                /selinux
       Current mode:                   permissive
       Mode from config file:          permissive
       Policy version:                 24
       Policy from config file:                targeted

So it seems that if you grep for "Current mode" and find either "disabled"
or "permissive", sage should build, but if you encounter "enabled" then it
may fail to build those apps that make the stack executable.

On my system sestatus is in /usr/sbin.

John Bussoletti
```




---

archive/issue_comments_078109.json:
```json
{
    "body": "Given that I have never seen any complaints about SELinux (and the solution seems to be to compile with `-fPIC` which we already do), this can be closed as \"worksforme\".",
    "created_at": "2013-12-29T11:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8619#issuecomment-78109",
    "user": "jdemeyer"
}
```

Given that I have never seen any complaints about SELinux (and the solution seems to be to compile with `-fPIC` which we already do), this can be closed as "worksforme".



---

archive/issue_comments_078110.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-29T11:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8619#issuecomment-78110",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078111.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-29T11:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8619#issuecomment-78111",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078112.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2014-01-04T02:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8619#issuecomment-78112",
    "user": "vbraun"
}
```

Resolution: worksforme
