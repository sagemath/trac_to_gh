# Issue 8027: change the wiki(...) command to store data in $HOME/.sage

archive/issues_008027.json:
```json
{
    "body": "Assignee: @haraldschilly\n\nReplying to [comment:5 mpatel]:\n> Replying to [comment:2 kcrisman]:\n> > Also, why is it still in the sage_wiki folder and not in .sage/sage_wiki or something similar to what is now done with the notebook?\n> \n> I'm not sure.  We do the same with `trac()` and the [optional] Trac spkg.  It makes sense to use a default directory under `DOT_SAGE`, but I think upgrading existing MoinMoin wikis can be problematic.\n\n\nWhen I wrote the wiki and trac command, there was no .sage/* folder, and the SAge notebook was stored in sage_notebook in the current directory.   The notebook has moved over to be in .sage, but nobody moved the wiki and trac yet.   It would be reasonable to do so.  HOWEVER, note that this would break all my wiki's, since a typical situation is:\n\n\n```\nsage@sagemath:~/wiki/sage$ ls\nnohup.err  nohup.out  sage_wiki  start\nsage@sagemath:~/wiki/sage$ more start\nulimit -v 2000000; nohup echo \"wiki(port=9001, address='')\" | sage-new  > nohup.out 2>nohup.err &\nsage@sagemath:~/wiki/sage$\n```\n\n\nIf you change the wiki to be in $HOME/.sage by default, then suddenly all my wiki's will get started on top of each other (hence all but one will fail to start). \n\nSo it might be worth checking if there is a wiki directory \"sage_wiki\" in the current directory, and only if there isn't then default to $HOME/.sage/moinmoin. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8027\n\n",
    "created_at": "2010-01-21T16:58:19Z",
    "labels": [
        "component: website/wiki",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "change the wiki(...) command to store data in $HOME/.sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8027",
    "user": "https://github.com/williamstein"
}
```
Assignee: @haraldschilly

Replying to [comment:5 mpatel]:
> Replying to [comment:2 kcrisman]:
> > Also, why is it still in the sage_wiki folder and not in .sage/sage_wiki or something similar to what is now done with the notebook?
> 
> I'm not sure.  We do the same with `trac()` and the [optional] Trac spkg.  It makes sense to use a default directory under `DOT_SAGE`, but I think upgrading existing MoinMoin wikis can be problematic.


When I wrote the wiki and trac command, there was no .sage/* folder, and the SAge notebook was stored in sage_notebook in the current directory.   The notebook has moved over to be in .sage, but nobody moved the wiki and trac yet.   It would be reasonable to do so.  HOWEVER, note that this would break all my wiki's, since a typical situation is:


```
sage@sagemath:~/wiki/sage$ ls
nohup.err  nohup.out  sage_wiki  start
sage@sagemath:~/wiki/sage$ more start
ulimit -v 2000000; nohup echo "wiki(port=9001, address='')" | sage-new  > nohup.out 2>nohup.err &
sage@sagemath:~/wiki/sage$
```


If you change the wiki to be in $HOME/.sage by default, then suddenly all my wiki's will get started on top of each other (hence all but one will fail to start). 

So it might be worth checking if there is a wiki directory "sage_wiki" in the current directory, and only if there isn't then default to $HOME/.sage/moinmoin. 


Issue created by migration from https://trac.sagemath.org/ticket/8027





---

archive/issue_comments_069996.json:
```json
{
    "body": "Changing assignee from @haraldschilly to tbd.",
    "created_at": "2010-01-27T12:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8027#issuecomment-69996",
    "user": "https://github.com/haraldschilly"
}
```

Changing assignee from @haraldschilly to tbd.



---

archive/issue_comments_069997.json:
```json
{
    "body": "Changing component from website/wiki to packages.",
    "created_at": "2010-01-27T12:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8027#issuecomment-69997",
    "user": "https://github.com/haraldschilly"
}
```

Changing component from website/wiki to packages.



---

archive/issue_comments_069998.json:
```json
{
    "body": "the website/wiki component is for the actual sage website and wiki. i file this under packages because it is related to the moin-xyz.spkg.",
    "created_at": "2010-01-27T12:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8027#issuecomment-69998",
    "user": "https://github.com/haraldschilly"
}
```

the website/wiki component is for the actual sage website and wiki. i file this under packages because it is related to the moin-xyz.spkg.



---

archive/issue_events_019232.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-22T08:45:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8027#event-19232"
}
```



---

archive/issue_comments_069999.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-22T08:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8027#issuecomment-69999",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070000.json:
```json
{
    "body": "MoinMoin is no longer part of Sage.",
    "created_at": "2013-01-22T08:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8027#issuecomment-70000",
    "user": "https://github.com/jdemeyer"
}
```

MoinMoin is no longer part of Sage.



---

archive/issue_comments_070001.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-22T08:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8027#issuecomment-70001",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070002.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-01-23T15:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8027#issuecomment-70002",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_019233.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-23T15:50:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8027",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8027#event-19233"
}
```
