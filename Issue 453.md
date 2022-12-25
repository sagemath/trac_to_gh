# Issue 453: singuname.sh support for Nexenta OS

archive/issues_000453.json:
```json
{
    "body": "Assignee: @malb\n\nHello Martin, \n\ncan you merge the following?\n\nFrom Didier Deshommes:\n\nAnd for singular to find ix86-nexentaos, singuname.sh has to have the following:\n\n```\nelif (echo $uname_a | $egrep \"SunOS\" >$devnull)\n    then\n        # NexentaOS ###############\n        if (echo $uname_a | $egrep \"NexentaOS\" > $devnull)\n            then\n               #echo \"----------------------------------------------------\"\n               echo ${prefix}-nexentaos\n               #echo \"----------------------------------------------------\"\n               #exit 0\n        else\n            echo ix86-SunOS\n            #exit 0\n        fi\n        exit 0\n```\n\n\nThis might also be interesting for the official Singular upstream.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/453\n\n",
    "created_at": "2007-08-19T08:27:02Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "singuname.sh support for Nexenta OS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/453",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

Hello Martin, 

can you merge the following?

From Didier Deshommes:

And for singular to find ix86-nexentaos, singuname.sh has to have the following:

```
elif (echo $uname_a | $egrep "SunOS" >$devnull)
    then
        # NexentaOS ###############
        if (echo $uname_a | $egrep "NexentaOS" > $devnull)
            then
               #echo "----------------------------------------------------"
               echo ${prefix}-nexentaos
               #echo "----------------------------------------------------"
               #exit 0
        else
            echo ix86-SunOS
            #exit 0
        fi
        exit 0
```


This might also be interesting for the official Singular upstream.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/453





---

archive/issue_comments_002249.json:
```json
{
    "body": "fixed in /home/malb/pkgs/singular-3-0-3-20070819.spkg.",
    "created_at": "2007-08-19T15:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/453#issuecomment-2249",
    "user": "https://github.com/malb"
}
```

fixed in /home/malb/pkgs/singular-3-0-3-20070819.spkg.



---

archive/issue_events_000482.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-08-19T15:35:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/453",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/453#event-482"
}
```



---

archive/issue_comments_002250.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T15:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/453#issuecomment-2250",
    "user": "https://github.com/malb"
}
```

Resolution: fixed
