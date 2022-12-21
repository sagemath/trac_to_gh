# Issue 3398: make "sage -c" load init.sage on startup

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-11 05:59:08

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

