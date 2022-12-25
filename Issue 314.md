# Issue 314: raw-input in notebook compatible with command line

archive/issues_000314.json:
```json
{
    "body": "Assignee: boothby\n\nWhile this may just simply be impossible, it would be nice if I could create interactive programs in SAGE that worked both in the command line interface and the notebook interface. The purpose of this enhancement would be for games, quizzes, wizards, etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/314\n\n",
    "created_at": "2007-03-10T23:18:05Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "title": "raw-input in notebook compatible with command line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/314",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

While this may just simply be impossible, it would be nice if I could create interactive programs in SAGE that worked both in the command line interface and the notebook interface. The purpose of this enhancement would be for games, quizzes, wizards, etc.

Issue created by migration from https://trac.sagemath.org/ticket/314





---

archive/issue_comments_001501.json:
```json
{
    "body": "This is a Python question not a SAGE question -- and yes there are billions of ways\nto create interactive Python programs.  From this point of view, SAGE is just a Python\nlibrary.",
    "created_at": "2007-03-21T23:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/314#issuecomment-1501",
    "user": "https://github.com/williamstein"
}
```

This is a Python question not a SAGE question -- and yes there are billions of ways
to create interactive Python programs.  From this point of view, SAGE is just a Python
library.



---

archive/issue_comments_001502.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-21T23:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/314#issuecomment-1502",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_001503.json:
```json
{
    "body": "Just a note because it came up on sage-devel: In the notebook, one could use JavaScript's window.prompt() function to trigger input boxes just like Python's raw_input(). To make this working, this would require an round-trip to the client triggered by something in the input program. Therefore, enhancements on the client and server side of the notebook are necessary. I leave it as closed, if somebody has a plan how to do it for real feel free to open it.",
    "created_at": "2011-03-21T15:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/314#issuecomment-1503",
    "user": "https://github.com/haraldschilly"
}
```

Just a note because it came up on sage-devel: In the notebook, one could use JavaScript's window.prompt() function to trigger input boxes just like Python's raw_input(). To make this working, this would require an round-trip to the client triggered by something in the input program. Therefore, enhancements on the client and server side of the notebook are necessary. I leave it as closed, if somebody has a plan how to do it for real feel free to open it.
