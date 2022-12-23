# Issue 3255: Add support for generic backtracking algorithms

Issue created by migration from https://trac.sagemath.org/ticket/3255

Original creator: mhansen

Original creation time: 2008-05-19 13:31:44

Assignee: mhansen

CC:  sage-combinat




---

Comment by mhansen created at 2008-05-19 13:59:10

Changing status from new to assigned.


---

Comment by wdj created at 2008-05-19 17:10:13

This patch should be refereed by someone else but it seems like an extremely useful direction of work, so I wanted to help out in a small way. I applied this to sage 3.0.2.alpha1. It applies cleanly and has the same sage -testall failures that the unpatched build has (doctest failures). In other words, this patch "passed" sage -testall.


---

Comment by mabshoff created at 2008-05-19 19:45:01

From http://blog.phasing.org/?p=6, i.e. Mike Hansen's new blog:

Another place that the comes in handy is in the generation of non-attacking fillings of augmented lattice diagrams. These are used to compute the non-symmetric Macdonald polynomials in type A.

Here are some timings of the new code.

Before:

```
sage: time Permutations(8, avoiding=[[1,3,2],[2,1,3]]).count()
CPU times: user 11.44 s, sys: 0.01 s, total: 11.45 s
Wall time: 12.35
128
sage: time NonattackingFillings([3,2,1,2]).count() 
CPU times: user 17.02 s, sys: 0.02 s, total: 17.04 s
Wall time: 17.36
4
sage: time NonattackingFillings([1,2,3,2]).count() 
CPU times: user 16.78 s, sys: 0.00 s, total: 16.78 s
Wall time: 16.80
24
```

After:

```
sage: time Permutations(8, avoiding=[[1,3,2],[2,1,3]]).count()
CPU times: user 1.58 s, sys: 0.00 s, total: 1.58 s
Wall time: 1.58
128
sage: sage: time NonattackingFillings([3,2,1,2]).count() 
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
4
sage: sage: time NonattackingFillings([1,2,3,2]).count() 
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
24
```



---

Comment by ddrake created at 2008-05-23 05:07:42

I'm giving this a tentative positive review. Tentative only because my knowledge of these algorithms and methods isn't complete. Someone else should look this over!

That said, the basic backtracker class is very simple and looks good. Fast algorithms for pattern avoidance in permutations are very desirable.


---

Attachment

I'm changing this to a positive review because I now understand this patch well enough to have written code which uses it, and it makes things super easy and fast. This should get into Sage right away.

Here's the code for making Dyck paths. It may not be the fastest or best way to do it, but it literally worked the very first time I loaded it.

```
class DyckPaths(GenericBacktracker):
  def __init__(self, n):
    GenericBacktracker.__init__(self, [], (0, 0))
    self._n = n

  def _rec(self, path, state):
    if is_odd(self._n):
      return

    len, ht = state

    if len < self._n:
      # if length is less than n, we need to keep building the path, so
      # new length will be 1 longer, and we don't yield the path yet.
      newlen = len + 1

      # if we're not touching the x-axis, we can yield a path with a
      # downstep at the end
      if ht > 0:
        yield path + [-1], (newlen, ht - 1), False

      # if the path isn't too high, it can also take an upstep
      if ht < (self._n - len):
        yield path + [1], (newlen, ht + 1), False
    else:
      # if length is n, set state to None so we stop trying to make new
      # paths, and yield what we've got
      yield path, None, True
```


Now, let's say you want Dyck paths with no peaks at even height. (This is an example I came up with off the top off my head in IRC; unsurprisingly, [the number of such paths is already known](http://www.ams.org/mathscinet-getitem?mr=2004242).) You only need to change the "`if ht > 0`" block to the following:

```
      # if we're not touching the x-axis, we can yield a path with a
      # downstep at the end, provided we don't make a peak at even
      # height
      if ht > 0:
        if is_odd(ht) or (path[-1] != 1):
          yield path + [-1], (newlen, ht - 1), False
```

This also worked the very first time I tried it!


---

Comment by mabshoff created at 2008-05-26 05:19:53

Resolution: fixed


---

Comment by mabshoff created at 2008-05-26 05:19:53

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-26 05:36:25

Hello sage-combinat-devel, 

I see that the CC notification works. So if you open/see a ticket that is relevant to sage-combinat please add "sage-combinat" in the CC field at the bottom of the ticket page. In case there already are other accounts listed just append it and separate entries by a comma. If you want to remove notification from a ticket just remove "sage-combinat" form the CC field. 

As is you will get email notifications on all changes, including comments, status changes and so on. The only action not resulting in an email is the attachment of a patch.

This specific ticket is Mike Hansen's generic backtracking code which has been merged into Sage 3.0.3.alpha0.

Let me know if there are any questions.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-26 05:55:21

Ok, this message should show up on sage-combinat-commits.

Cheers,

Michael


---

Comment by mhansen created at 2008-05-26 06:00:39

Testing sage-combinat-commits.
