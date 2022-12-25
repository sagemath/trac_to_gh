# Issue 5713: multigraph plotting bug

archive/issues_005713.json:
```json
{
    "body": "Assignee: ekirkman\n\nCC:  @rlmill\n\n\n```\nI just tried to plot a multigraph with setting positions of vertices,\n\nG=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':\n['c','d','d','d'],'d':['e']})\n\nG.show(pos={'a':[0,1],'b':[1,1],'c':[2,0],'d':[1,0],'e':[0,0]})\n\nand got an error\n\n File \"/home/alec/sage/local/lib/python2.5/site-packages/sage/graphs/\ngraph_plot.py\", line 459, in set_edges\n   odd_y = M[1] + d\nNameError: global name 'd' is not defined\n\nWithout pos both show and plot work OK.\n\nAlec Mihailovs\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5713\n\n",
    "created_at": "2009-04-08T16:07:40Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "multigraph plotting bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5713",
    "user": "https://github.com/williamstein"
}
```
Assignee: ekirkman

CC:  @rlmill


```
I just tried to plot a multigraph with setting positions of vertices,

G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':
['c','d','d','d'],'d':['e']})

G.show(pos={'a':[0,1],'b':[1,1],'c':[2,0],'d':[1,0],'e':[0,0]})

and got an error

 File "/home/alec/sage/local/lib/python2.5/site-packages/sage/graphs/
graph_plot.py", line 459, in set_edges
   odd_y = M[1] + d
NameError: global name 'd' is not defined

Without pos both show and plot work OK.

Alec Mihailovs
```


Issue created by migration from https://trac.sagemath.org/ticket/5713





---

archive/issue_comments_044566.json:
```json
{
    "body": "Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5713#issuecomment-44566",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2.

Cheers,

Michael



---

archive/issue_comments_044567.json:
```json
{
    "body": "Attachment [trac_5713.patch](tarball://root/attachments/some-uuid/ticket5713/trac_5713.patch) by @rlmill created at 2009-04-09 21:29:54",
    "created_at": "2009-04-09T21:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5713#issuecomment-44567",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5713.patch](tarball://root/attachments/some-uuid/ticket5713/trac_5713.patch) by @rlmill created at 2009-04-09 21:29:54



---

archive/issue_comments_044568.json:
```json
{
    "body": "Ok, given the scope of this patch I am capable of understanding what is going on and I am giving this patch a positive review. Even all doctests pass :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T01:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5713#issuecomment-44568",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, given the scope of this patch I am capable of understanding what is going on and I am giving this patch a positive review. Even all doctests pass :)

Cheers,

Michael



---

archive/issue_comments_044569.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-10T01:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5713#issuecomment-44569",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044570.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T01:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5713#issuecomment-44570",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
