# Issue 3905: [with patch, needs review] revision of programming guide

Issue created by migration from https://trac.sagemath.org/ticket/3905

Original creator: jhpalmieri

Original creation time: 2008-08-20 00:35:45

Assignee: tba

CC:  robertwb mhansen

Keywords: programming guide

I've edited the programming guide; this has involved a fair amount of reorganization, some rewriting, some deleting, and some new stuff.  I hope I haven't removed anyone's favorite part.

The coercion section is unchanged, because of comments by craigcitro in #3738: I hope he produces a new coercion section for this document.

The section after coercion, on mutability, is unchanged, although it needs to be expanded.  I don't really understand the issues involved, so I don't think I'm the right person to do this.

The new version also has nothing on benchmarking or profiling.  Feel free to write something and produce a patch.

Meanwhile, in addition to the patch, you can look at a PDF version of the guide here:
[http://www.math.washington.edu/~palmieri/Sage/prog.pdf](http://www.math.washington.edu/~palmieri/Sage/prog.pdf)


---

Comment by jhpalmieri created at 2008-08-20 00:38:34

(By the way, this patch also fixes the issue raised in #3393.  If this patch gets merged into Sage, we should close that ticket, too.)


---

Attachment


---

Comment by malb created at 2008-08-20 15:01:54

Page 1

 * either the list of authors should be extended (to include John
   for example) or replaced by "The Sage Group" or something

Page 2

 * Copyright 2008

Page 3

 * "Sage is a free mathematics software system. It is implemented
   using Python, Cython, and C++, and uses GAP, GSL, Matplotlib,
   Maxima, MWRANK, NetworkX, NTL, Numpy, PARI, Singular and many
   specialized smaller systems and library. It is free and open
   source, and is available under the terms of the GNU Public License
   and compatible licenses."

Page 9

 * Mention list of all available standard packages:
   http://www.sagemath.org/links-components.html

 * "Notably absent from this triad is a good system for exact linear
   algebra (something MAGMA does extremely well), but this gap is
   being ﬁlled by code written for Sage or covered by specialsed
   libraries like LinBox, IML and M4RI."

 * Again John needs to be added.

Page 11

 * It might be worth mentioning that some methods do have uppercase
   names, e.g. Matrix_integer_dense.LLL since it makes sense there.

Page 12
 
 * I'm not sure about the encouragement of TXT files. It seems to be
   hardly used and gets old quickly.

 * The AUTHORS block in the example doesn't contain dates and
   descriptions of what the authors did

Page 13

 * page overflow

Page 14

 * right now it is actually GPLv2+

 * it might be a good idea to point to
   http://www.sagemath.org/development-map.html

 * OUTPUT blocks are rarly present in practice, should that be fixed?

 * "The EXAMPLES block doubles as doctests and each new function for
   the Sage library must contain doctests."

 * In the example: strictly speaking, self isn't passed in explicitly
   so I'd say it doesn't belong in the INPUT block. Discussions of
   presupposed properties of self could/should be discussed in the
   running text.

Page 15

 * I think it is now valid to put LaTeX in the INPUT/OUTPUT blocks

Page 16

 * again a strong emphasis: "New code without examples/doctests will
   not be accepted."

 * the randgen framework should be described in this document since
   most random stuff doesn't need "#random".

Page 17

 * page overflow

Page 18

 * I think the numbers shown by the doctest framework are actually
   correct

Page 19

 * Do we actually run randomized tests regularly?

Page 22

 * Maybe add: "Do not include opening and closing $'s"

 * It might be a good idea to showcase some special macros used in
   Sage here.

 * the docstring is lacking the leading r"""

Page 23

 * explain why we don't do __repr__

 * the "am = adjancency_matrix" contradicts the Python Zen: "There
   should be one|and preferably only one|obvious way to do". It
   shouldn't be encouraged in the development manual.

 * maybe the Python Zen should be cited? In any case: How about a link
   to good Python docs?

Page 24

 * these days Python ints are not much more efficient anymore,
   sometimes more efficient yes, but not that badly.

 * The claim is not true anymore:
   sage: time v = [ 2*i for i in range(1000000)]
   CPU times: user 2.01 s, sys: 0.08 s, total: 2.09 s
   Wall time: 2.12 s
   
   sage: time v = [ 2*i for i in range(1000000r)]
   CPU times: user 2.15 s, sys: 0.10 s, total: 2.26 s
   Wall time: 2.29 s

Page 27

 * an example for a factory function + weakref is PolynomialRing in
   sage.rings.polynomial.polynomial_ring

Page 29

 * catching every exception might also hide a genuine error

 * page overflow

Page 30

 * to avoid circular imports, maybe the "late_import" 'technique'
   should be explained/outlined.

 * sage -optional is optional_packages() from within Sage.

Page 31

 * what about Lisp?

 * one gets to use all C/C++ libraries shipped with Sage.

Page 32

 * the extension also must be added to the packages list in setup.py

Page 33

 * The timings aren't that different anymore (on my 2.6 Ghz Opteron):

    sage: time [n for n in range(10^6) if is2pow(n)]
    CPU times: user 0.60 s, sys: 0.00 s, total: 0.60 s
    Wall time: 0.60 s

    sage: time [n for n in range(10^6) if is2pow_slow(n)]
    CPU times: user 1.01 s, sys: 0.04 s, total: 1.05 s
    Wall time: 1.05 s

 * It is not necessarily true anymore that Pari does all of the heavy
   lifting for matrices over ZZ. NTL, LinBox, IML and custom code took
   over a fair part.

Page 34
 
 * it needs to be explained why matfrobenius didn't need to be added
   to a decl.pxi file.

 * the docstring of the matfrobenius method isn't up to Sage's
   standards and should be fixed before being put in the Developer's
   manual.

 * "def matfrobenius" doesn't have a docstring at all.

 * "def frobenius" has a bad docstring.

Page 35

 * page overflow

Page 38

 * are these examples still hard/valid?

 * Singular section needs update since we have libSingular now

Page 41

 * program -> function

Page 45

 * I'd suggest to only keep the "Alternative" version, since we want
   users to use the convenience functions we added. No point in doing
   it by hand if there are nice functions to help.

Page 49

 * Programming manual -> Developer's manual

Page 53

 * I don't think we need to cite ourselves when it comes to describing
   the mailing lists. We can just leave out the quotes.

 * [sage-devel] is also used to discuss development issues and the
   overall project direction

 * the IRC channels are missing: #sage-support and #sage-devel

 * the inclusion rules only apply to new SPKGs and not necessarily to
   code in the Sage library

Page 54

 * It would be good to describe what a SPKG is earlier and then give
   the rules for inclusion of new SPKGs.

Page 55

 * Mercurial doesn't need a password or am I missing something here?

 * Explain that HG mainly applies to the Sage library as opposed to  SPKGs

Page 56

 * hg_sage.serve() listens on http://localhost:8000

Page 60

 * maybe reproduce the skeleton of spkg-install scripts from:
   http://wiki.sagemath.org/SPKG_Audit

 * mention/discussion of .hg repositories and SPKG.txt in SPKGs is
   missing.

 * the proposed check for GAP is bad practice. Instead one should
   check in SAGE_ROOT/spkgs/installed/ with "latest_version".

 * the spkg-install script given as an example is bad practice,
   instead the skeleton from the Wiki should be used/fleshed out.

Page 63

 * explain that the application for a Trac account is only to prevent
   Spam, i.e. that everybody can have an account: entry barrier is low.

 * maybe link to the Google search pages to search in [sage-support]
   and [sage-devel]

Page 65
 
 * sage -ba is hardly needed. Its mention should be removed.

Page 66

 * "Sage administrator" -> "release manager"


---

Comment by malb created at 2008-08-20 15:03:41

Hi, I've posted my notes above. Please be soft on me w.r.t. to the wording which might be perceived as rude/commanding. I don't mean it that way rather these are just short notes with suggestions/impressions etc. I hope you don't take offense.


---

Comment by jhpalmieri created at 2008-08-20 17:31:59

Thanks for the comments. I will be busy with some other work for a while, and then I'll have time to try to deal with these. I will probably have questions about some of them, because I don't understand everything that I probably should.

Meanwhile, if you have more comments, please let me know.


---

Comment by malb created at 2008-08-23 22:49:58

my comments from trac as a patch


---

Attachment

Hi there, I made my comments into a patch which ought to be applied after John's patch. This is not perfect or release quality and it still needs some heavy editing. Maybe someone can get through the new prog.tex and make sure it is not worse than what we currently ship and then we can apply both patches? Then, mhansen can convert the Developer's guide to Sphinx and we can go on editing it afterwards?


---

Comment by jhpalmieri created at 2008-08-24 16:24:20

As I said earlier, I don't have time to work on this right now, so thanks for doing this.  After a quick glance, malb's patch looks good to me (although I just looked at the diff, I didn't apply it and build the new documentation).  I was sort of thinking that the authors could be "The Sage Hive Mind" :), but the "The Sage Group" is okay, too.  I wonder if the lines

```
This document was authored by William Stein, David Joyner, John Palmieri 
and others with the editorial help of Iftikhar Burhanuddin and Martin Albrecht. 
```

should be deleted altogether? Or replaced with (a footnote?)

```
The first version of this document was authored by William Stein and David 
Joyner with the editorial help of ...; various members of the Sage group have 
contributed to later editions, following the procedures outlined in 
Chapters ?? and ??
```

I don't care that much about attribution, since I feel like I just reorganized and edited: I'm not sure that I added enough content to distinguish me from the rest of the Sage Group.  But I won't fight it if you want to keep my name there.  (The important thing from my point of view is that we're getting a more-or-less up-to-date version of this documentation, and that seems to be happening.)

In any case, I'm happy other people are working on this, too, and I'm looking forward to seeing the Sphinx version.


---

Comment by malb created at 2008-08-24 23:18:42

Replying to [comment:7 jhpalmieri]:
> In any case, I'm happy other people are working on this, too, and I'm looking forward to seeing the Sphinx version.

Lets sort out the attribution thing after the Sphinx-isation? But I also don't mind getting rid of that sentence.


---

Comment by jhpalmieri created at 2008-08-25 21:21:31

By the way, do the patches here take care of #1647 and #1648? How about #2078? #2422?  (And I already pointed out #3393.)

If this is closed, I think those others should be as well.  (It's always fun to close a lot of tickets, right?)


---

Comment by mabshoff created at 2008-08-25 21:33:53

Thanks for pointing that out. I mentioned this ticket on the tickets you mentioned.

Cheers,

Michael


---

Comment by rlm created at 2008-08-31 00:20:21

`mabshoff` is looking at the first patch, I've looked over the second patch, and the only complaint I have is that approx. line 312 isn't grammatical:


```
It is {\em very important} that you include your name in
the AUTHOR log, since everybody who submits code to \sage
to receive proper credit...
```


They *should* receive proper credit...


---

Comment by mabshoff created at 2008-08-31 06:55:38

Replying to [comment:11 rlm]:
> They *should* receive proper credit...

That section is being deleted, so no harm done :)

rlm and I read over the patches and it is better to get them in (even if they are slighly imperfect) than to let them bitrot. The remaining issues can be addressed via follow up tickets. This work by John and Martin is certainly long needed and a great improvement to the documentation.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 07:42:21

Unfortunately Martin's patch breaks the doctests. Some of them can be fixed by adding 

```
sage: K.<x> = QQ[]
sage: G = PermutationGroup([[(1,2,3),(4,5)], [(1,2)]])
sage: rgp = Gp()
sage: def gap_randstring(n):
...       current_randstate().set_seed_gap()
...       return gap(n).SCRRandomString()
sage: def rtest():
...       current_randstate().set_seed_gp(rgp)
...       return (ZZ.random_element(1000), RR.random_element(),
...               K.random_element(), G.random_element(),
...               gap_randstring(5),
...               rgp.random(), ntl.ZZ_random(99999),
...               random())
```

to a bunch of the randgen examples, but I consider that too ugly a solution to do it. 


We could take out the randgen chapter for now and deal with it at a later ticket. Thoughts?

Cheers,

Michael


---

Comment by rlm created at 2008-08-31 07:47:10

The PRNG stuff is very well documented in the relevant modules. Perhaps a pointer in that direction is enough?


---

Comment by mabshoff created at 2008-08-31 07:53:50

Replying to [comment:14 rlm]:
> The PRNG stuff is very well documented in the relevant modules. Perhaps a pointer in that direction is enough?

I definitely agree, so I am merging malb's patch without the PRNG section. We will deal with that problem down the road. Time to get alpha3 out.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 07:54:40

Merged both patches in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-31 07:54:40

Resolution: fixed
