# Issue 6385: Python relative import messes up Sage command line arguments

archive/issues_006385.json:
```json
{
    "body": "Assignee: tbd\n\nFrom: \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a9e80289571de40e\n\nOn Mon, Jun 22, 2009 at 6:38 PM, Robert Miller<rlmills...`@`gmail.com> wrote:\n\n> I tried running the Sage notebook as follows, from SAGE_ROOT/devel/\n> sage-main:\n\n> $ ../../sage -notebook\n\n> And I get the following error:\n\n> Please wait while the Sage Notebook server starts...\n> Traceback (most recent call last):\n>  File \"/Users/rlmill/sage-4.0.2/local/bin/sage-notebook\", line 9, in\n> <module>\n>    from sage.server.notebook.all import notebook\n>  File \"/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/\n> all.py\", line 15, in <module>\n>    from notebook_object import notebook, inotebook\n>  File \"/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/\n> notebook_object.py\", line 19, in <module>\n>    import notebook as _notebook\n>  File \"/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/\n> notebook.py\", line 22, in <module>\n>    from   sage.structure.sage_object import SageObject, load\n> ImportError: No module named sage_object\n\n> Can anyone reproduce this?\n\nIn python imports are relative by default, so \"import sage\" does not\nmean what you think.   I think long ago I hacked around this problem\nfor just typing \"sage\" to start sage, by making it change to a\ndifferent directory during startup.   (I vaguely recall doing that\nspecifically to get Sage to work on Cygwin, actually.)\n\nSo I think the above should be considered a bug, and you should\ndefinitely report it to trac.  Probably the fix is to change the\ndirectory during part of Sage startup, to thwart Python's relative\nimport system.\n\nWilliam \n\nIssue created by migration from https://trac.sagemath.org/ticket/6385\n\n",
    "created_at": "2009-06-22T17:58:12Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Python relative import messes up Sage command line arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6385",
    "user": "@rlmill"
}
```
Assignee: tbd

From: 

http://groups.google.com/group/sage-devel/browse_thread/thread/a9e80289571de40e

On Mon, Jun 22, 2009 at 6:38 PM, Robert Miller<rlmills...`@`gmail.com> wrote:

> I tried running the Sage notebook as follows, from SAGE_ROOT/devel/
> sage-main:

> $ ../../sage -notebook

> And I get the following error:

> Please wait while the Sage Notebook server starts...
> Traceback (most recent call last):
>  File "/Users/rlmill/sage-4.0.2/local/bin/sage-notebook", line 9, in
> <module>
>    from sage.server.notebook.all import notebook
>  File "/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/
> all.py", line 15, in <module>
>    from notebook_object import notebook, inotebook
>  File "/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/
> notebook_object.py", line 19, in <module>
>    import notebook as _notebook
>  File "/Users/rlmill/sage-4.0.2/devel/sage-main/sage/server/notebook/
> notebook.py", line 22, in <module>
>    from   sage.structure.sage_object import SageObject, load
> ImportError: No module named sage_object

> Can anyone reproduce this?

In python imports are relative by default, so "import sage" does not
mean what you think.   I think long ago I hacked around this problem
for just typing "sage" to start sage, by making it change to a
different directory during startup.   (I vaguely recall doing that
specifically to get Sage to work on Cygwin, actually.)

So I think the above should be considered a bug, and you should
definitely report it to trac.  Probably the fix is to change the
directory during part of Sage startup, to thwart Python's relative
import system.

William 

Issue created by migration from https://trac.sagemath.org/ticket/6385





---

archive/issue_comments_051120.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-06-22T13:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6385#issuecomment-51120",
    "user": "@a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051121.json:
```json
{
    "body": "Is it still a problem?",
    "created_at": "2014-06-22T13:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6385#issuecomment-51121",
    "user": "@a-andre"
}
```

Is it still a problem?



---

archive/issue_comments_051122.json:
```json
{
    "body": "I think it's no longer an issue (although I cannot explain why the problem no longer occurs).",
    "created_at": "2014-10-01T12:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6385#issuecomment-51122",
    "user": "@jdemeyer"
}
```

I think it's no longer an issue (although I cannot explain why the problem no longer occurs).



---

archive/issue_comments_051123.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-10-01T12:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6385#issuecomment-51123",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051124.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-10-13T15:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6385#issuecomment-51124",
    "user": "@vbraun"
}
```

Resolution: fixed
