# Issue 1473: Java3D usable from command line as well as notebook

archive/issues_001473.json:
```json
{
    "body": "Assignee: was\n\nEventually we hope to have many tools (e.g. MayaVi) to help handle this, but Java3D works now and it should be easy to invoke the same code as an app rather than an applet. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1473\n\n",
    "created_at": "2007-12-12T10:49:02Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Java3D usable from command line as well as notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1473",
    "user": "robertwb"
}
```
Assignee: was

Eventually we hope to have many tools (e.g. MayaVi) to help handle this, but Java3D works now and it should be easy to invoke the same code as an app rather than an applet. 

Issue created by migration from https://trac.sagemath.org/ticket/1473





---

archive/issue_comments_009477.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-12T10:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9477",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009478.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-12-12T10:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9478",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_009479.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-14T06:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9479",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_009480.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-14T09:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9480",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_009481.json:
```json
{
    "body": "Attachment\n\nThis works fine for me.",
    "created_at": "2007-12-15T07:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9481",
    "user": "was"
}
```

Attachment

This works fine for me.



---

archive/issue_comments_009482.json:
```json
{
    "body": "If I download `java3d-1_5_1-linux-i586.zip` from the java3d web site, I can unzipit to get (among other things) `j3d-jre.zip`.  Then I can unzip `j3d-jre.zip` to get (among other things) `libj3dcore-ogl.so`.\n\nIf I put libj3dcore-ogl.so in some directory, and set my LD_LIBRARY_PATH environment variable to point to that directory before starting Sage, then the command-line java3d code works.",
    "created_at": "2007-12-15T07:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9482",
    "user": "cwitty"
}
```

If I download `java3d-1_5_1-linux-i586.zip` from the java3d web site, I can unzipit to get (among other things) `j3d-jre.zip`.  Then I can unzip `j3d-jre.zip` to get (among other things) `libj3dcore-ogl.so`.

If I put libj3dcore-ogl.so in some directory, and set my LD_LIBRARY_PATH environment variable to point to that directory before starting Sage, then the command-line java3d code works.



---

archive/issue_comments_009483.json:
```json
{
    "body": "Gluegen is supposed to take care of all of that (for applets it does) but maybe there's a way to rig it for apps too.",
    "created_at": "2007-12-15T07:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9483",
    "user": "robertwb"
}
```

Gluegen is supposed to take care of all of that (for applets it does) but maybe there's a way to rig it for apps too.



---

archive/issue_comments_009484.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T09:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9484",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009485.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T09:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1473#issuecomment-9485",
    "user": "mabshoff"
}
```

Resolution: fixed
