# Issue 7626: delete PBUILD code in local/bin/sage-sage script

archive/issues_007626.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nI noticed code like this in the sage-sage script:\n\n```\n \t\t    if [ \"$SAGE_PBUILD\" == \"yes\" ]; then \n \t\t        echo 'Pbuild is currently broken -- defaulting to serial build.' \n \t\t        # if [ \"$@\" ]; then \n \t\t        #     ln -snf \"$SAGE_ROOT\"/devel/sage-\"$@\" \"$SAGE_ROOT\"/devel/sage \n \t\t        # fi \n \t\t        # time python \"$SAGE_ROOT\"/devel/sage/build.py -b \n \t\t        sage-build \"$@\" \n```\n\n\nNot only is SAGE_PBUILD \"broken\", it has long since been replaced by something better.  So we should just delete this stuff from sage-sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7626\n\n",
    "created_at": "2009-12-08T19:22:39Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "delete PBUILD code in local/bin/sage-sage script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7626",
    "user": "@williamstein"
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

archive/issue_comments_065161.json:
```json
{
    "body": "This is already deleted some time ago.",
    "created_at": "2012-03-06T09:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7626#issuecomment-65161",
    "user": "@jdemeyer"
}
```

This is already deleted some time ago.



---

archive/issue_comments_065162.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-03-06T09:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7626#issuecomment-65162",
    "user": "@jdemeyer"
}
```

Resolution: worksforme
