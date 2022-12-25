# Issue 7205: fix the list of old sage releases website

archive/issues_007205.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @haraldschilly\n\n1. If I go to http://sagemath.org/src/ there is only the last release.\n\n   2. If I click on \"up one directory level\", I'm just dumped to\nhttp://sagemath.org, which makes no sense.\n\n3. Clicking on changelogs gives\nhttp://sagemath.org/src/changelogs/index.html which does indeed list\nchangelogs.  But it also lists  a file \"OLD_VERSIONS_HERE.txt\",\nrandomly right in the middle.  Looking at that file I find the\ncompletely wrong statement: \"These are archived old versions.  For the\nnew versions see the main SAGE website. http://modular.ucsd.edu/sage\".\n\n4. There is a random \"README.txt\" for no reason also in the middle\nof http://sagemath.org/src/changelogs/\n\n5. Finally, logging into the server I find that\nhttp://sagemath.org/src-old/ has the old versions.  But how could I\nfind that otherwise?   Also, the description at the top of src-old\ndoesn't explain what it is accurately.  It would be better to say\n\"Here you can download the source code for any past version of Sage so\nyou can build it from source.\"\n\n6. This listing at http://sagemath.org/src-old/ also has various\nrandom files like README.txt.in and install.html mixed in.\n\nIt would also be worth mentioning that we have many old sage install on sage.math. \n\nI wonder if it would also be good to archive bdists for one specific Linux release, e.g., 32-bit x86 Ubuntu 8.04 LTS?  Since then one can easily get a virtual machine and drop our binary in it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7205\n\n",
    "created_at": "2009-10-14T02:40:54Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix the list of old sage releases website",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7205",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @haraldschilly

1. If I go to http://sagemath.org/src/ there is only the last release.

   2. If I click on "up one directory level", I'm just dumped to
http://sagemath.org, which makes no sense.

3. Clicking on changelogs gives
http://sagemath.org/src/changelogs/index.html which does indeed list
changelogs.  But it also lists  a file "OLD_VERSIONS_HERE.txt",
randomly right in the middle.  Looking at that file I find the
completely wrong statement: "These are archived old versions.  For the
new versions see the main SAGE website. http://modular.ucsd.edu/sage".

4. There is a random "README.txt" for no reason also in the middle
of http://sagemath.org/src/changelogs/

5. Finally, logging into the server I find that
http://sagemath.org/src-old/ has the old versions.  But how could I
find that otherwise?   Also, the description at the top of src-old
doesn't explain what it is accurately.  It would be better to say
"Here you can download the source code for any past version of Sage so
you can build it from source."

6. This listing at http://sagemath.org/src-old/ also has various
random files like README.txt.in and install.html mixed in.

It would also be worth mentioning that we have many old sage install on sage.math. 

I wonder if it would also be good to archive bdists for one specific Linux release, e.g., 32-bit x86 Ubuntu 8.04 LTS?  Since then one can easily get a virtual machine and drop our binary in it.

Issue created by migration from https://trac.sagemath.org/ticket/7205





---

archive/issue_comments_059673.json:
```json
{
    "body": "Harald has fixed the problems involving finding the old source.  Some of the directory listing and header problems remain.",
    "created_at": "2009-10-14T16:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59673",
    "user": "https://github.com/williamstein"
}
```

Harald has fixed the problems involving finding the old source.  Some of the directory listing and header problems remain.



---

archive/issue_comments_059674.json:
```json
{
    "body": "Seems to me that almost every problem except the 6th problem is solved. There are still some random files at http://www.sagemath.org/src-old/",
    "created_at": "2009-10-25T19:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59674",
    "user": "https://github.com/TimDumol"
}
```

Seems to me that almost every problem except the 6th problem is solved. There are still some random files at http://www.sagemath.org/src-old/



---

archive/issue_comments_059675.json:
```json
{
    "body": "Harald, it seems to me that none of this is still relevant.  Do you agree?",
    "created_at": "2012-05-17T22:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59675",
    "user": "https://github.com/jdemeyer"
}
```

Harald, it seems to me that none of this is still relevant.  Do you agree?



---

archive/issue_comments_059676.json:
```json
{
    "body": "Changing component from distribution to website/wiki.",
    "created_at": "2012-05-17T22:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59676",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from distribution to website/wiki.



---

archive/issue_comments_059677.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-17T22:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59677",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059678.json:
```json
{
    "body": "`@`jdemeyer: honestly, i have no memory of that. a short introduction note for the src-old files is the only thing that is still open. we can close it, i'll add a note.",
    "created_at": "2012-05-17T22:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59678",
    "user": "https://github.com/haraldschilly"
}
```

`@`jdemeyer: honestly, i have no memory of that. a short introduction note for the src-old files is the only thing that is still open. we can close it, i'll add a note.



---

archive/issue_comments_059679.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-18T09:58:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59679",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007426.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-21T08:06:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7205#event-7426"
}
```



---

archive/issue_comments_059680.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-05-21T08:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7205",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7205#issuecomment-59680",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
