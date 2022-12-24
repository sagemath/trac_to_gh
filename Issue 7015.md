# Issue 7015: [with patch; needs review] cygwin port -- ratpoints -- don't build executable since we don't need it (and fails on cygwin)

archive/issues_007015.json:
```json
{
    "body": "Assignee: mabshoff\n\nthe ratpoints spkg builds an executable we just throw away.  On Cygwin it fails though changing the link order from\n\n```\n\t    -lgmp -lm -lratpoints\n\tto\n\t    -lm -lratpoints -lgmp\n```\n\nwould fix the problem. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7015\n\n",
    "created_at": "2009-09-25T22:15:09Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch; needs review] cygwin port -- ratpoints -- don't build executable since we don't need it (and fails on cygwin)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7015",
    "user": "was"
}
```
Assignee: mabshoff

the ratpoints spkg builds an executable we just throw away.  On Cygwin it fails though changing the link order from

```
	    -lgmp -lm -lratpoints
	to
	    -lm -lratpoints -lgmp
```

would fix the problem. 

Issue created by migration from https://trac.sagemath.org/ticket/7015





---

archive/issue_comments_058059.json:
```json
{
    "body": "Here is the spkg:\n\n  http://sage.math.washington.edu/home/wstein/patches/ratpoints-2.1.2.p3.spkg",
    "created_at": "2009-09-25T22:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7015#issuecomment-58059",
    "user": "was"
}
```

Here is the spkg:

  http://sage.math.washington.edu/home/wstein/patches/ratpoints-2.1.2.p3.spkg



---

archive/issue_comments_058060.json:
```json
{
    "body": "The only change in the spkg package is:\n\n\n```\n-make\n+make libratpoints.a\n```\n\n\nsince this is all that is needed, it's +1 from me.",
    "created_at": "2009-09-25T22:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7015#issuecomment-58060",
    "user": "certik"
}
```

The only change in the spkg package is:


```
-make
+make libratpoints.a
```


since this is all that is needed, it's +1 from me.



---

archive/issue_comments_058061.json:
```json
{
    "body": "Here's an updated spkg\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/ratpoints-2.1.2.p4.spkg\n\nChanges from William's version include:\n\n* Remove the junk files `spkg-install~` and `SPKG.txt~`.\n* Make `spkg-install` executable using \"`chmod +x spkg-install`\".\n* Use about 75 characters for each line in the file `SPKG.txt`. Any longer than that and it would be difficult to read on a standard terminal width, i.e. 80 characters wide.",
    "created_at": "2009-09-28T07:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7015#issuecomment-58061",
    "user": "mvngu"
}
```

Here's an updated spkg

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ratpoints-2.1.2.p4.spkg

Changes from William's version include:

* Remove the junk files `spkg-install~` and `SPKG.txt~`.
* Make `spkg-install` executable using "`chmod +x spkg-install`".
* Use about 75 characters for each line in the file `SPKG.txt`. Any longer than that and it would be difficult to read on a standard terminal width, i.e. 80 characters wide.



---

archive/issue_comments_058062.json:
```json
{
    "body": "Looks good to me.  I included the changes that Minh made to William's spkg and left the version at p3.",
    "created_at": "2009-10-16T08:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7015#issuecomment-58062",
    "user": "mhansen"
}
```

Looks good to me.  I included the changes that Minh made to William's spkg and left the version at p3.



---

archive/issue_comments_058063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T08:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7015#issuecomment-58063",
    "user": "mhansen"
}
```

Resolution: fixed
