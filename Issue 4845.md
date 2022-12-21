# Issue 4845: [with patch, needs review] sage 3.2.2 crashes on startup when init.sage present

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-12-21 09:15:09

Assignee: craigcitro

I think the title says it all -- sage seems to crash on start whenever the file `~/.sage/init.sage` is present, at least on my Mac. The attached patch fixes the issue.

I'm listing this as a blocker, partially because the fix is so short. I think that this bug has been lurking quite a while -- I think it was the fix for #4792 that exposed it ...


---

Comment by craigcitro created at 2008-12-21 09:16:12

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-12-21 09:22:59

Nice fix, "sage -gdb" and "sage -valgrind" keep working :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 09:26:22

I have created #4846 so we are more likely to catch this issue, even though it still doesn't make it 100% fool proof without adding a doctest that starts Sage completely in non-doctest mode.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 11:58:20

Resolution: fixed


---

Comment by mabshoff created at 2008-12-21 11:58:20

Merged in Sage 3.2.3.alpha0


---

Comment by was created at 2008-12-24 01:39:44

for future reference:

```
17:35 < wstein> I don't like the patch at 4845.
17:35 < wstein> better would be
17:35 < wstein> if stripped_line.startswith('#'):
17:35 < wstein> instead of 
17:36 < wstein> if stripped_line and stripped_line[0] == '#':
```



---

Attachment

I like the cleaner v2.patch. Merged in Sage 3.2.3.alpha0.

Cheers,

Michael


---

Comment by craigcitro created at 2008-12-24 04:19:13

I definitely prefer the v2 patch for the sake of readability. For the sake of it, though, should anyone look at this ticket, I want to note that the original patch seems (at a quick glance, anyway) to be faster:


```
sage: s = ""
sage: %timeit s.startswith('3')
1000000 loops, best of 3: 350 ns per loop
sage: %timeit s and s[0] == '3'
10000000 loops, best of 3: 72.2 ns per loop

sage: s = "345"
sage: %timeit s.startswith('3')
1000000 loops, best of 3: 353 ns per loop
sage: %timeit s and s[0] == '3'
1000000 loops, best of 3: 208 ns per loop

sage: s = "678"
sage: %timeit s.startswith('3')
1000000 loops, best of 3: 351 ns per loop
sage: %timeit s and s[0] == '3'
1000000 loops, best of 3: 212 ns per loop
```

