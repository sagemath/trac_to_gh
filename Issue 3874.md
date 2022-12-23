# Issue 3874: Moebius plot bug

archive/issues_003874.json:
```json
{
    "body": "Assignee: was\n\nplot(moebius) plots the Moebius function nicely from 0 to 50.\nplot(moebius,50,100) plots the y-values of the Moebius function nicely from 50 to 100. Unfortunately, the x-values are still from 0 to 50!\n\nIssue created by migration from https://trac.sagemath.org/ticket/3874\n\n",
    "created_at": "2008-08-15T13:20:01Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "Moebius plot bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3874",
    "user": "kcrisman"
}
```
Assignee: was

plot(moebius) plots the Moebius function nicely from 0 to 50.
plot(moebius,50,100) plots the y-values of the Moebius function nicely from 50 to 100. Unfortunately, the x-values are still from 0 to 50!

Issue created by migration from https://trac.sagemath.org/ticket/3874





---

archive/issue_comments_027628.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-15T13:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3874#issuecomment-27628",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_027629.json:
```json
{
    "body": "Changing assignee from was to kcrisman.",
    "created_at": "2008-08-15T13:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3874#issuecomment-27629",
    "user": "kcrisman"
}
```

Changing assignee from was to kcrisman.



---

archive/issue_comments_027630.json:
```json
{
    "body": "\n```\n\nCan you throw in a call to\n\n  p.xmin(xmin)\n\nbefore returning p?  The plot of  plot(moebius, 500,550) would look\nmuch nicer as a result. \n```\n",
    "created_at": "2008-08-15T16:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3874#issuecomment-27630",
    "user": "was"
}
```


```

Can you throw in a call to

  p.xmin(xmin)

before returning p?  The plot of  plot(moebius, 500,550) would look
much nicer as a result. 
```




---

archive/issue_comments_027631.json:
```json
{
    "body": "\n```\n> William,\n>\n> If you are referring to the viewing window starting around x=-1, my\n> understanding was that this is taken care of by the patches to\n> http://trac.sagemath.org/sage_trac/ticket/3806, which will be in 3.1.\n> I attach the output of\n> sage: plot(moebius,500,550)\n> on my system, with those patches included.\n>\n> If that's not what you mean, let me know what the problem with the\n> plot is and I will be happy to have the code reset the xmin. Thanks\n> for the feedback!\n>\n> - kcrisman\n\nWith the excellent work at #3806, I immediately change my opinion to\npositive review for your patch as is. \n\n```\n",
    "created_at": "2008-08-15T17:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3874#issuecomment-27631",
    "user": "was"
}
```


```
> William,
>
> If you are referring to the viewing window starting around x=-1, my
> understanding was that this is taken care of by the patches to
> http://trac.sagemath.org/sage_trac/ticket/3806, which will be in 3.1.
> I attach the output of
> sage: plot(moebius,500,550)
> on my system, with those patches included.
>
> If that's not what you mean, let me know what the problem with the
> plot is and I will be happy to have the code reset the xmin. Thanks
> for the feedback!
>
> - kcrisman

With the excellent work at #3806, I immediately change my opinion to
positive review for your patch as is. 

```




---

archive/issue_comments_027632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-18T23:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3874#issuecomment-27632",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027633.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-18T23:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3874#issuecomment-27633",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha0
