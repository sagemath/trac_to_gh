# Issue 363: maxima completion list

archive/issues_000363.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\"Brandon.Barker\nshow details\n\t 8:18 am (20 minutes ago) \n\nIn sage 2.5.0.2 I'm having trouble building maxima's command list\n(tried this on a linux powerpc machine where I compiled SAGE from the\nsource, as well as an x64 machine with precompiled binaries):\n\nsage: maxima.diff\nBuilding Maxima command completion list (this takes\na few seconds only the first time you do it).\nTo force rebuild later, delete /home/brandon/.sage//\nmaxima_commandlist_cache.sobj.\n\nThe file listed is never created, and no matter how long I wait, the\nmessage above will still appear when I try to do tab completion.\nHowever, I can still execute maxima.diff ok, but not some other\ncommands (like maxima.index):\n\nsage: maxima.diff(x^2,x)\n2*x\nsage: maxima.index(x^2)\nindex(x^2)\n\nOf course, this is probably because there is no index call function in\ndevel/sage-main/sage/interfaces/maxima.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/363\n\n",
    "created_at": "2007-05-13T15:42:18Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "maxima completion list",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/363",
    "user": "was"
}
```
Assignee: was


```
"Brandon.Barker
show details
	 8:18 am (20 minutes ago) 

In sage 2.5.0.2 I'm having trouble building maxima's command list
(tried this on a linux powerpc machine where I compiled SAGE from the
source, as well as an x64 machine with precompiled binaries):

sage: maxima.diff
Building Maxima command completion list (this takes
a few seconds only the first time you do it).
To force rebuild later, delete /home/brandon/.sage//
maxima_commandlist_cache.sobj.

The file listed is never created, and no matter how long I wait, the
message above will still appear when I try to do tab completion.
However, I can still execute maxima.diff ok, but not some other
commands (like maxima.index):

sage: maxima.diff(x^2,x)
2*x
sage: maxima.index(x^2)
index(x^2)

Of course, this is probably because there is no index call function in
devel/sage-main/sage/interfaces/maxima.py
```


Issue created by migration from https://trac.sagemath.org/ticket/363





---

archive/issue_comments_001762.json:
```json
{
    "body": "the fix",
    "created_at": "2007-05-18T15:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/363#issuecomment-1762",
    "user": "was"
}
```

the fix



---

archive/issue_comments_001763.json:
```json
{
    "body": "Attachment\n\nFixed.",
    "created_at": "2007-05-18T15:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/363#issuecomment-1763",
    "user": "was"
}
```

Attachment

Fixed.



---

archive/issue_comments_001764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-18T15:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/363#issuecomment-1764",
    "user": "was"
}
```

Resolution: fixed
