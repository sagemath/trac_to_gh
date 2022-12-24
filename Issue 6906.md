# Issue 6906: [with spkg, needs review] update Mercurial to version 1.3.1

archive/issues_006906.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nAs the summary says.  The spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/mercurial-1.3.1.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/mercurial-1.3.1.p0.spkg).  Please test thoroughly.\n\nThis fixes the problem at #6440, by the way.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6906\n\n",
    "created_at": "2009-09-08T23:23:33Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with spkg, needs review] update Mercurial to version 1.3.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6906",
    "user": "@jhpalmieri"
}
```
Assignee: @jhpalmieri

As the summary says.  The spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/mercurial-1.3.1.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/mercurial-1.3.1.p0.spkg).  Please test thoroughly.

This fixes the problem at #6440, by the way.


Issue created by migration from https://trac.sagemath.org/ticket/6906





---

archive/issue_comments_057055.json:
```json
{
    "body": "Last year, mabshoff did:\n\n* Disable inotify extenion since it is broken on Itanium\n\nI noticed you don't use the setup.py patch anymore.  Does inotify work on Itanium now?\n\nIf patches/setup.py is not needed, then it needs to be deleted from the repository.",
    "created_at": "2009-09-22T16:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6906#issuecomment-57055",
    "user": "@jasongrout"
}
```

Last year, mabshoff did:

* Disable inotify extenion since it is broken on Itanium

I noticed you don't use the setup.py patch anymore.  Does inotify work on Itanium now?

If patches/setup.py is not needed, then it needs to be deleted from the repository.



---

archive/issue_comments_057056.json:
```json
{
    "body": "Sorry about that.  I created the patch and then didn't copy setup.py.  The spkg-install file now includes a line\n\n```\n$CP patches/setup.py src/setup.py\n```\n",
    "created_at": "2009-09-22T18:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6906#issuecomment-57056",
    "user": "@jhpalmieri"
}
```

Sorry about that.  I created the patch and then didn't copy setup.py.  The spkg-install file now includes a line

```
$CP patches/setup.py src/setup.py
```




---

archive/issue_comments_057057.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-05T18:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6906#issuecomment-57057",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_057058.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6906",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6906#issuecomment-57058",
    "user": "@mwhansen"
}
```

Resolution: fixed
