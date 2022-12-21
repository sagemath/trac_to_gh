# Issue 876: Implement or wrap Braid Groups

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-10-13 09:03:20

Assignee: was




---

Comment by robertwb created at 2007-10-13 09:03:24

Changing assignee from was to robertwb.


---

Comment by mabshoff created at 2008-12-05 22:25:12

This looks very much like a wish list item. Moved.

Cheers,

Michael


---

Comment by wdj created at 2008-12-05 22:34:58

BTW, in gap_packages there is a GPL'd package called braid that might help here. It was packaged before GPLv3 came out (I actually did the packaging but did not write any of the code).


---

Comment by kcrisman created at 2009-12-30 05:06:29

Incidentally, apparently the braid package is now autoloaded, though it doesn't seem to be used anywhere.  This is improperly documented in interfaces/gap.py, though:

```
    The packages sonata, guava, factint, gapdoc, grape, design, toric,
    and laguna are loaded in all cases before the workspace is saved,
    if they are available.
```


```
    g = Gap(use_workspace_cache=False, max_workspace_size=None)
    for pkg in ['ctbllib', 'sonata', 'guava', 'factint', \
                'gapdoc', 'grape', 'design', \
                'toric', 'laguna', 'braid']:   # NOTE: Do *not* autoload hap - it screws up PolynomialRing(Rationals,2)
        try:
            g.load_package(pkg, verbose=verbose)
```



---

Comment by wdj created at 2009-12-30 12:21:13

Replying to [comment:5 kcrisman]:
> Incidentally, apparently the braid package is now autoloaded, though it doesn't seem to be used anywhere.  This is improperly documented in interfaces/gap.py, though:
> {{{
>     The packages sonata, guava, factint, gapdoc, grape, design, toric,
>     and laguna are loaded in all cases before the workspace is saved,
>     if they are available.
> }}}
> {{{
>     g = Gap(use_workspace_cache=False, max_workspace_size=None)
>     for pkg in ['ctbllib', 'sonata', 'guava', 'factint', \
>                 'gapdoc', 'grape', 'design', \
>                 'toric', 'laguna', 'braid']:   # NOTE: Do *not* autoload hap - it screws up PolynomialRing(Rationals,2)
>         try:
>             g.load_package(pkg, verbose=verbose)
> }}}

I think this problem with HAP was fixed long ago.

Also, I think I had to repackage braid recently because of some loading problems it had. I don't remember the details. Maybe it was because of a problem with gap 4.4.12 and since we use 4.4.10, it is not an issue?


---

Comment by kcrisman created at 2012-07-07 03:01:18

Looks like this is now much further along at #12339.


---

Comment by kcrisman created at 2012-07-07 03:01:18

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-07-07 03:01:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-07-17 08:34:38

Resolution: duplicate
