# Issue 3398: make "sage -c" load init.sage on startup

archive/issues_003398.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\n> I have defined a function that starts up the notebook server with my\n> desired preferences and placed the function definition into my\n> init.sage script, so that whenever I use the command line, I don't\n> have to remember the whole thing to start it up. Works fine.\n>\n> Since I usually go straight to the notebook, I figured just running:\n> sage -c \"snote()\"\n> would do the trick. But apparently init.sage isn't executed before the\n> -c command.\n>\n> I already know ways to start the notebook conveniently from the\n> command line so I'm not worried about that, but I was wondering if\n> that was the correct and desired behavior of -c. Perhaps we could have\n> another similar argument ( -C ?) that executes init.sage before\n> executing the command?\n\nI think it's a bug that 'sage -c' doesn't load init.sage first.\n\nDoes anybody think differently?  If nobody disagrees, I'll\nadd a trac ticket.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3398\n\n",
    "created_at": "2008-06-11T05:59:08Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "make \"sage -c\" load init.sage on startup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3398",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty


```
> I have defined a function that starts up the notebook server with my
> desired preferences and placed the function definition into my
> init.sage script, so that whenever I use the command line, I don't
> have to remember the whole thing to start it up. Works fine.
>
> Since I usually go straight to the notebook, I figured just running:
> sage -c "snote()"
> would do the trick. But apparently init.sage isn't executed before the
> -c command.
>
> I already know ways to start the notebook conveniently from the
> command line so I'm not worried about that, but I was wondering if
> that was the correct and desired behavior of -c. Perhaps we could have
> another similar argument ( -C ?) that executes init.sage before
> executing the command?

I think it's a bug that 'sage -c' doesn't load init.sage first.

Does anybody think differently?  If nobody disagrees, I'll
add a trac ticket.
```


Issue created by migration from https://trac.sagemath.org/ticket/3398


