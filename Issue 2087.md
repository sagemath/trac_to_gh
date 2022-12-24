# Issue 2087: make the final output of "sage -i" more user friendly (easy to fix)

archive/issues_002087.json:
```json
{
    "body": "Assignee: was\n\n\n```\nWhen I install an optional package via\n\n ./sage -i [optional package]\n\nthe last line of output is \"Making script relocatable\".\n\nI frequently do the install in the background, redirecting\nthe output to a file\nand then use \"tail -f\" to monitor the output (and then go off\nand do something else).   When I come back, it is unclear\nto me whether the install has finished.  Perhaps something\nlike \"install finished\" could be added as a last line.\n\nJust a suggestion.\nKate\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2087\n\n",
    "created_at": "2008-02-07T18:58:42Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "make the final output of \"sage -i\" more user friendly (easy to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2087",
    "user": "was"
}
```
Assignee: was


```
When I install an optional package via

 ./sage -i [optional package]

the last line of output is "Making script relocatable".

I frequently do the install in the background, redirecting
the output to a file
and then use "tail -f" to monitor the output (and then go off
and do something else).   When I come back, it is unclear
to me whether the install has finished.  Perhaps something
like "install finished" could be added as a last line.

Just a suggestion.
Kate
```


Issue created by migration from https://trac.sagemath.org/ticket/2087





---

archive/issue_comments_013509.json:
```json
{
    "body": "The patch I will attach shortly does print the following at the end of an install:\n\n```\nSuccessfully installed valgrind_3.3.0\nNow cleaning up tmp files.\nMaking SAGE/Python scripts relocatable...\nMaking script relocatable\nFinished installing valgrind_3.3.0.spkg\n```\n\nwhere valgrind_3.3.0.spkg in this case was `$PKG_NAME.spkg`\n\nCheers,\n\nMichael",
    "created_at": "2008-02-25T18:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2087#issuecomment-13509",
    "user": "mabshoff"
}
```

The patch I will attach shortly does print the following at the end of an install:

```
Successfully installed valgrind_3.3.0
Now cleaning up tmp files.
Making SAGE/Python scripts relocatable...
Making script relocatable
Finished installing valgrind_3.3.0.spkg
```

where valgrind_3.3.0.spkg in this case was `$PKG_NAME.spkg`

Cheers,

Michael



---

archive/issue_comments_013510.json:
```json
{
    "body": "Attachment [trac_2087.patch](tarball://root/attachments/some-uuid/ticket2087/trac_2087.patch) by mabshoff created at 2008-02-25 18:41:22",
    "created_at": "2008-02-25T18:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2087#issuecomment-13510",
    "user": "mabshoff"
}
```

Attachment [trac_2087.patch](tarball://root/attachments/some-uuid/ticket2087/trac_2087.patch) by mabshoff created at 2008-02-25 18:41:22



---

archive/issue_comments_013511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2087#issuecomment-13511",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013512.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-25T19:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2087#issuecomment-13512",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
