# Issue 3895: sage-notebook-insecure ImportError

archive/issues_003895.json:
```json
{
    "body": "Assignee: boothby\n\nIf called from $SAGE_ROOT, everything goes fine, but if called from somewhere else:\n\n\n```\nrank4:sage-main rlmill$ ../../sage -inotebook\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.1, Release Date: 2008-08-17                       |\n| Type notebook() for the GUI, and license() for information.        |\nPlease wait while the SAGE Notebook server starts...\nTraceback (most recent call last):\n  File \"/Users/rlmill/sage-3.1.1/local/bin/sage-notebook-insecure\", line 9, in <module>\n    from sage.server.notebook.all import notebook\n  File \"/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/all.py\", line 13, in <module>\n    from notebook_object import notebook, inotebook\n  File \"/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/notebook_object.py\", line 19, in <module>\n    import notebook as _notebook\n  File \"/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/notebook.py\", line 22, in <module>\n    from   sage.structure.sage_object import SageObject, load\nImportError: No module named sage_object\nrank4:sage-main rlmill$ cd ../..\nrank4:sage-3.1.1 rlmill$ ./sage -inotebook\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.1, Release Date: 2008-08-17                       |\n| Type notebook() for the GUI, and license() for information.        |\nPlease wait while the SAGE Notebook server starts...\n...\nThe notebook files are stored in: /Users/rlmill/.sage//sage_notebook\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n<goes swimmingly>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3895\n\n",
    "created_at": "2008-08-19T03:48:07Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "sage-notebook-insecure ImportError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3895",
    "user": "rlm"
}
```
Assignee: boothby

If called from $SAGE_ROOT, everything goes fine, but if called from somewhere else:


```
rank4:sage-main rlmill$ ../../sage -inotebook
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...
Traceback (most recent call last):
  File "/Users/rlmill/sage-3.1.1/local/bin/sage-notebook-insecure", line 9, in <module>
    from sage.server.notebook.all import notebook
  File "/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/all.py", line 13, in <module>
    from notebook_object import notebook, inotebook
  File "/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/notebook_object.py", line 19, in <module>
    import notebook as _notebook
  File "/Users/rlmill/sage-3.1.1/devel/sage-main/sage/server/notebook/notebook.py", line 22, in <module>
    from   sage.structure.sage_object import SageObject, load
ImportError: No module named sage_object
rank4:sage-main rlmill$ cd ../..
rank4:sage-3.1.1 rlmill$ ./sage -inotebook
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...
...
The notebook files are stored in: /Users/rlmill/.sage//sage_notebook
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
<goes swimmingly>
```


Issue created by migration from https://trac.sagemath.org/ticket/3895





---

archive/issue_comments_027843.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3895#issuecomment-27843",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_027844.json:
```json
{
    "body": "Changing assignee from boothby to malb.",
    "created_at": "2009-01-25T19:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3895#issuecomment-27844",
    "user": "malb"
}
```

Changing assignee from boothby to malb.



---

archive/issue_comments_027845.json:
```json
{
    "body": "This is fixed (at least) in 4.1.1.",
    "created_at": "2009-08-25T19:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3895#issuecomment-27845",
    "user": "malb"
}
```

This is fixed (at least) in 4.1.1.



---

archive/issue_comments_027846.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T19:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3895#issuecomment-27846",
    "user": "malb"
}
```

Resolution: fixed
