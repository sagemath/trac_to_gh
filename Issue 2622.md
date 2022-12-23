# Issue 2622: [with patches, need review] add PolyBoRi to reference manual

Issue created by migration from https://trac.sagemath.org/ticket/2622

Original creator: malb

Original creation time: 2008-03-20 23:57:57

Assignee: malb

CC:  burcin

These patches depend on #2619 and basically add some babel to the top of `sage.rings.polynomial.pbori`


---

Attachment

polybori-refman-sage.patch looks good to me: One small typo did sneak in: "This quptient ring"

polybori-refman-doc.patch ought to be rebased since it has some unrelated changes included:

```
patch -p1 --dry-run < polybori-refman-doc.patch\?format\=raw
patching file .hgtags
Hunk #1 FAILED at 122.
1 out of 1 hunk FAILED -- saving rejects to file .hgtags.rej
patching file commontex/patchlevel.tex
Hunk #1 FAILED at 1.
1 out of 1 hunk FAILED -- saving rejects to file commontex/patchlevel.tex.rej
patching file ref/combinat.tex
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
2 out of 2 hunks ignored -- saving rejects to file ref/combinat.tex.rej
patching file ref/files
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
4 out of 4 hunks ignored -- saving rejects to file ref/files.rej
patching file ref/hecke.tex
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
1 out of 1 hunk ignored -- saving rejects to file ref/hecke.tex.rej
patching file ref/polynomial-rings.tex
patching file ref/update_script.py
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
2 out of 2 hunks ignored -- saving rejects to file ref/update_script.py.rej
```


Cheers,

Michael


---

Comment by malb created at 2008-03-21 01:18:45

That is odd because I started with a vanilla doc repository. But I'll rebase.


---

Comment by mabshoff created at 2008-03-21 01:26:34

Replying to [comment:2 malb]:
> That is odd because I started with a vanilla doc repository. But I'll rebase.

For the record: That was my 2.11.alpha0 build on sage.math which has a binary in /home/mabshoff/release-cycles-2.11/. I can throw out the hunks from the patch that are already there. 

Another small issue I forgot: Are we going with Gröbner now or will be stick with Groebner. Since we merged your various UTF-8 patches all those should work. Umlaute über alles!

Mike Hansen will be reviewing the other patches in this series, so they should be merged tonight assuming the get positive reviews.

Cheers,

Michael


---

Attachment

fixed typo


---

Attachment

cleaned up version of the patch


---

Comment by mabshoff created at 2008-03-21 02:21:36

All issues I had have been resolved.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-21 02:22:15

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 02:22:15

Merged in Sage 2.11.alpha1
