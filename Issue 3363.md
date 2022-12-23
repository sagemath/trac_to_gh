# Issue 3363: Use Applescript to start Sage on OSX (step 4-6 from README)

archive/issues_003363.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nHi\nI just read the installation readme and built my own application to\nstart the sageserver:\n\nJust start the Apple-ScriptEditor and enter the following code:\n\ntell application \"Terminal\"\n        do script \"/Applications/sage/sage -notebook\"\nend tell\n\nWell, that's all. Now only save the script as a program-bundle. After\nthat, you can assign the .app file a nice icon and put it in your\ndock, click it, see firefox coming up and have fun.\n\nI'd propose that this app could be part of the sage-install\nbundle... ;-)\n\nHope, you like this tip\n\ngreeting,\nKai-Philipp \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3363\n\n",
    "created_at": "2008-06-04T16:23:07Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "Use Applescript to start Sage on OSX (step 4-6 from README)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3363",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
Hi
I just read the installation readme and built my own application to
start the sageserver:

Just start the Apple-ScriptEditor and enter the following code:

tell application "Terminal"
        do script "/Applications/sage/sage -notebook"
end tell

Well, that's all. Now only save the script as a program-bundle. After
that, you can assign the .app file a nice icon and put it in your
dock, click it, see firefox coming up and have fun.

I'd propose that this app could be part of the sage-install
bundle... ;-)

Hope, you like this tip

greeting,
Kai-Philipp 
```


Issue created by migration from https://trac.sagemath.org/ticket/3363





---

archive/issue_comments_023531.json:
```json
{
    "body": "I believe this issue is invalid now that we have a Sage.app.",
    "created_at": "2009-11-27T21:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3363#issuecomment-23531",
    "user": "iandrus"
}
```

I believe this issue is invalid now that we have a Sage.app.



---

archive/issue_comments_023532.json:
```json
{
    "body": "To release manager: Yes, this should be closed.  Although the app is still not default (sigh).",
    "created_at": "2010-05-26T20:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3363#issuecomment-23532",
    "user": "kcrisman"
}
```

To release manager: Yes, this should be closed.  Although the app is still not default (sigh).



---

archive/issue_comments_023533.json:
```json
{
    "body": "On OS X, we can create an app bundle from a newly compiled source tarball:\n\n\n```\nexport SAGE_APP_BUNDLE=yes\n./sage -bdist version\n```\n\n\nSo close as invalid.",
    "created_at": "2010-06-12T18:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3363#issuecomment-23533",
    "user": "mvngu"
}
```

On OS X, we can create an app bundle from a newly compiled source tarball:


```
export SAGE_APP_BUNDLE=yes
./sage -bdist version
```


So close as invalid.



---

archive/issue_comments_023534.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-06-12T18:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3363",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3363#issuecomment-23534",
    "user": "mvngu"
}
```

Resolution: invalid
