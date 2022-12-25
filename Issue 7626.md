# Issue 7626: delete PBUILD code in local/bin/sage-sage script

archive/issues_007626.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nI noticed code like this in the sage-sage script:\n\n```\n \t\t    if [ \"$SAGE_PBUILD\" == \"yes\" ]; then \n \t\t        echo 'Pbuild is currently broken -- defaulting to serial build.' \n \t\t        # if [ \"$@\" ]; then \n \t\t        #     ln -snf \"$SAGE_ROOT\"/devel/sage-\"$@\" \"$SAGE_ROOT\"/devel/sage \n \t\t        # fi \n \t\t        # time python \"$SAGE_ROOT\"/devel/sage/build.py -b \n \t\t        sage-build \"$@\" \n```\n\nNot only is SAGE_PBUILD \"broken\", it has long since been replaced by something better.  So we should just delete this stuff from sage-sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7626\n\n",
    "created_at": "2009-12-08T19:22:39Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "delete PBUILD code in local/bin/sage-sage script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7626",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

I noticed code like this in the sage-sage script:

```
 		    if [ "$SAGE_PBUILD" == "yes" ]; then 
 		        echo 'Pbuild is currently broken -- defaulting to serial build.' 
 		        # if [ "$@" ]; then 
 		        #     ln -snf "$SAGE_ROOT"/devel/sage-"$@" "$SAGE_ROOT"/devel/sage 
 		        # fi 
 		        # time python "$SAGE_ROOT"/devel/sage/build.py -b 
 		        sage-build "$@" 
```

Not only is SAGE_PBUILD "broken", it has long since been replaced by something better.  So we should just delete this stuff from sage-sage.

Issue created by migration from https://trac.sagemath.org/ticket/7626





---

archive/issue_comments_065045.json:
```json
{
    "body": "This is already deleted some time ago.",
    "created_at": "2012-03-06T09:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7626#issuecomment-65045",
    "user": "https://github.com/jdemeyer"
}
```

This is already deleted some time ago.



---

archive/issue_comments_065046.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-03-06T09:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7626#issuecomment-65046",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_018128.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-06T09:20:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7626",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7626#event-18128"
}
```



---

archive/issue_events_018129.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-06T09:28:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7626",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7626#event-18129"
}
```
