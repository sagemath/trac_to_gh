# Issue 589: improve doctesting of sage-sage script

archive/issues_000589.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nOn 9/4/07, Jonathan Bober <jwbober@gmail.com> wrote:\n> My memory could be wrong, but I feel that this exact problem has\n> occurred before. (The problem of running scripts on the command line not\n> working -- not necessarily the exact same underlying cause for the\n> problem.)\n>\n> This kind of basic functionality should probably be tested somewhere\n> automatically. Maybe a doctect with a line like\n>\n> sage: os.system('.\\sage something_or_other.sage')\n>\n> might work. Or maybe this would need to be somehow tested outside the\n> doctest framework. I don't know. Just a thought.\n\nTrue.\n\nImplement some doctests like that  and post a patch to trac. :-)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/589\n\n",
    "created_at": "2007-09-05T14:14:31Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "improve doctesting of sage-sage script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/589",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
On 9/4/07, Jonathan Bober <jwbober@gmail.com> wrote:
> My memory could be wrong, but I feel that this exact problem has
> occurred before. (The problem of running scripts on the command line not
> working -- not necessarily the exact same underlying cause for the
> problem.)
>
> This kind of basic functionality should probably be tested somewhere
> automatically. Maybe a doctect with a line like
>
> sage: os.system('.\sage something_or_other.sage')
>
> might work. Or maybe this would need to be somehow tested outside the
> doctest framework. I don't know. Just a thought.

True.

Implement some doctests like that  and post a patch to trac. :-)
```


Issue created by migration from https://trac.sagemath.org/ticket/589





---

archive/issue_comments_003037.json:
```json
{
    "body": "This seems not too hard.  In what file would such doctests live?",
    "created_at": "2009-12-30T04:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/589#issuecomment-3037",
    "user": "@kcrisman"
}
```

This seems not too hard.  In what file would such doctests live?



---

archive/issue_comments_003038.json:
```json
{
    "body": "Note that this is now `$SAGE_ROOT/spkg/bin/sage`.  If this ticket is still valid.",
    "created_at": "2012-07-07T04:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/589#issuecomment-3038",
    "user": "@kcrisman"
}
```

Note that this is now `$SAGE_ROOT/spkg/bin/sage`.  If this ticket is still valid.



---

archive/issue_comments_003039.json:
```json
{
    "body": "Duplicate of #10300 + #10326 + #12249 + #9191.",
    "created_at": "2013-02-08T13:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/589#issuecomment-3039",
    "user": "@jdemeyer"
}
```

Duplicate of #10300 + #10326 + #12249 + #9191.



---

archive/issue_comments_003040.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-02-08T13:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/589#issuecomment-3040",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
