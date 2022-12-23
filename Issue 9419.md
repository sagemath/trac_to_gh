# Issue 9419: Update Developers Guide to state how patches should be made.

Issue created by migration from https://trac.sagemath.org/ticket/9419

Original creator: drkirkby

Original creation time: 2010-07-03 08:36:32

Assignee: mvngu

CC:  leif jdemeyer pipedream

As discussed here

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/c566520374106df3

[GNU patch](http://savannah.gnu.org/projects/patch/) will be added to Sage. This is ticket #9418. 

In order to make use of the command, the developers guide will need to be updated to reflect a new way of making patch commands. We should sort out the details as precisely as possible, so everyone uses the exact same method.


---

Comment by leif created at 2010-11-21 21:50:07

Hopefully finished before Sage 5.0 comes out... ;-)


---

Comment by jdemeyer created at 2010-11-22 20:36:09

I will do a first attempt at writing this up...


---

Comment by jdemeyer created at 2010-11-22 20:54:54

How do you like the following high-level steps, suppose we want to create sphinx-1.0.4.p3


```
1) create a directory sphinx-1.0.4.p3
2) put upstream source in sphinx-1.0.4.p3/src
For every ISSUE which needs to be patched, do the following:
    3) cp -pr sphinx-1.0.4.p3 sphinx-1.0.4.p3.patched
    4) edit sphinx-1.0.4.p3.patched/src to fix ISSUE.
    5) diff -ur sphinx-1.0.4.p3/src sphinx-1.0.4.p3.patched/src >sphinx-1.0.4.p3/patches/ISSUE.patch
    6) rm -r sphinx-1.0.4.p3.patched
```



---

Comment by jdemeyer created at 2010-11-22 20:59:41

For applying the patches in `spkg-install`:


```
patch -p1 <src/ISSUE.patch
```



---

Comment by jdemeyer created at 2010-11-28 10:37:44

Changing keywords from "" to "patch doc".


---

Comment by jdemeyer created at 2010-11-28 10:37:44

After thinking about it some more, perhaps the following is better:

```
1) create a directory sphinx-1.0.4.p3
2) cd sphinx-1.0.4.p3
2) put upstream source in sphinx-1.0.4.p3/src
For every ISSUE which needs to be patched, do the following:
    3) cp -pr src src.patched
    4) edit src.patched to fix ISSUE.
    5) diff -ur src src.patched >patches/ISSUE.patch
    6) rm -r src.patched
```


To apply the patches in `spkg-install`:

```
1) cd src
2) patch -p1 <../patches/ISSUE.patch
```



---

Comment by leif created at 2010-11-29 17:35:17

So, in what order should `patches/*.patch` be applied?

It's not _that_ unlikely _in principle "unrelated"_ patches affect the same parts of code (or at least modify parts near to each other in the same file), such that multiple patches against vanilla upstream source won't apply smoothly in (arbitrary) sequence.

There should (in addition) be some documentation on what files are patched by what "ISSUE", I'd suggest in an `SPKG.txt` section and / or a `patches/README`[`.txt`]. (If "ISSUE" is almost self-explanatory, we don't need extra comments in `spkg-install`, but then other files should contain further details and references to the relevant tickets.)

What if some patches only have to be applied on platform XY?

I think creating `src-$ISSUE/` for each "ISSUE" and then doing `diff -ur src/ src-$ISSUE/ > patches/$ISSUE.patch` is equally valid.

And IMHO doing e.g. `cd src/ && diff -u file.orig file > ../patches/file.patch` should be valid for "simple" patches as well (then using `cd src ; patch -p0 < ../patches/file.patch`, or omitting the `-p0`), though perhaps using `diff -u src/file.orig src/file ...` (and applying them from the top level spkg directory) would be better.

So I'm not convinced there is a single best way to go in all cases.


---

Comment by leif created at 2010-11-29 20:07:17

Also, the _Dependencies_ section of `SPKG.txt` should explicitly contain [GNU] `patch` if it is used by an spkg.

(I'd prefer _selectively_ adding "patch" as a dependency in `spkg/standard/deps`, too.)


---

Comment by jdemeyer created at 2010-11-29 20:11:26

Replying to [comment:6 leif]:
> So, in what order should `patches/*.patch` be applied?
That's up to the writer of `spkg-install`.

> There should (in addition) be some documentation on what files are patched by what "ISSUE", I'd suggest in an `SPKG.txt` section and / or a `patches/README`[`.txt`]. (If "ISSUE" is almost self-explanatory, we don't need extra comments in `spkg-install`, but then other files should contain further details and references to the relevant tickets.)
Agreed.  I prefer in `SPKG.txt` because then all the information about the package is contained in one file.

> What if some patches only have to be applied on platform XY?
Same as today.  Instead of a conditional `cp`, we have a conditional `patch`.

> I think creating `src-$ISSUE/` for each "ISSUE" and then doing `diff -ur src/ src-$ISSUE/ > patches/$ISSUE.patch` is equally valid.
Agreed.

> And IMHO doing e.g. `cd src/ && diff -u file.orig file > ../patches/file.patch` should be valid for "simple" patches as well (then using `cd src ; patch -p0 < ../patches/file.patch`, or omitting the `-p0`)
I would prefer that all patches can be _applied_ the same way, namely from `src/` with a `-p1` strip level.  So I disagree.

> though perhaps using `diff -u src/file.orig src/file ...` (and applying them from the top level spkg directory) would be better.
Okay for me.


---

Comment by drkirkby created at 2011-04-28 05:26:22

Replying to [comment:2 jdemeyer]:
> I will do a first attempt at writing this up...

Did you get anywhere with this? The issue is quite important, as currently the developers guide is still advising the use of 'cp'  and saying not to use 'patch'. 

One thing we need to be careful of is that when testing the patch, people don't overwrite the src directory. Which makes me think, should the write permissions for all files below src be removed? That would at least prevent that accident, though perhaps it would screw up some packages. 

Dave


---

Comment by leif created at 2011-07-03 11:25:35

Also, the _Developer's Guide_ should state how to check the exit code(s) of `patch`, i.e. *we should IMHO test `$?` of _every_ application of `patch`* (cf. [my comment here](http://trac.sagemath.org/sage_trac/ticket/11246#comment:21)):

 _[...] Fortunately, we now use `patch` rather than `cp`, which at least spits out warning or error messages in case upstream and `patches/*` get out of sync (or someone made another mistake), but these messages are easily missed - even by a reviewer, which can lead to all kinds of obscure errors or misbehavior *any time later*, so we should IMHO check `$?` there. [...]_

If we apply many patches in a loop (which I don't really like since this badly documents _what_ is actually patched _why_, but see documentation-related discussion above), we should at least "accumulate" the outcome, i.e. test once all patches were successfully applied.

We could even check if they applied seamlessly, without fuzz (which I think should be the case in spkgs; otherwise they should get rebased).

Opinions?


---

Comment by leif created at 2011-07-03 11:25:35

Changing keywords from "patch doc" to "patch doc howto spkgs diff".


---

Comment by leif created at 2011-07-03 11:44:42

Replying to [comment:9 drkirkby]:
> One thing we need to be careful of is that when testing the patch, people don't overwrite the src directory. Which makes me think, should the write permissions for all files below src be removed? That would at least prevent that accident, though perhaps it would screw up some packages.

Well, you usually _want (or need) to overwrite / modify_ files in `src/` when applying patches from within `spkg-install`...

Note that you don't need write permissions on a file you're going to patch, but on its containing directory.


---

Comment by leif created at 2011-07-03 14:26:36

Replying to [comment:2 jdemeyer]:
> I will do a first attempt at writing this up...

Jeroen, do you already have some draft of a new section for the Developer's Guide (replacing [_"Use `cp` for patching"_](http://www.sagemath.org/doc/developer/patching_spkgs.html#use-cp-for-patching))?


---

Comment by leif created at 2011-07-03 15:46:34

Changing status from new to needs_info.


---

Comment by leif created at 2011-07-03 15:46:34

Ok, I just started rewriting `doc/en/developer/{producing,patching}_spkgs.rst`.

*Q:* Should patches to upstream source (also? optionally?) be documented in `patches/README.txt` or whatever it is called, or just - i.e. only - in `SPKG.txt`'s _Special Update/Build Instructions_ section (or even a new one, "_Patches_")?


---

Comment by jhpalmieri created at 2011-11-23 00:16:39

Here's an attempt at a patch.  (I'm tired of wanting to refer people in sage-devel to the Developer's Guide, but then hesitating because of its out-dated insistence on using 'cp' instead of 'patch', and nothing seems to be happening with this.  Plus I'm trying to avoid grading an exam.)


---

Comment by jhpalmieri created at 2011-11-23 00:16:39

Changing status from needs_info to needs_review.


---

Attachment

A minor typo, with "an" instead of "a". 

"so if you are writing an spkg which is not part of the standard"

Personally I would have used:


```
diff -Naur
```


which seems one of the most common ways. There's some discussion in 

http://linux.die.net/man/1/patch

of the best arguments to use. The main change is that this is recursive, so if one edits multiple files to make a change to sort out some problem, there can be one patch file to resolve the problem, rather than having to make one for each file. 

Dave


---

Comment by jhpalmieri created at 2011-12-04 02:32:42

Replying to [comment:15 drkirkby]:
> A minor typo, with "an" instead of "a". 
> 
> "so if you are writing an spkg which is not part of the standard"

I will fix that, thanks.

> Personally I would have used:
> 
 {{{
 diff -Naur
 }}}
> 
> which seems one of the most common ways.  

Dave, I'm shocked: this doesn't seem to be Posix-standard usage :)  For example, as far as I can tell, on your machine hawk neither `-N` nor `-a` are supported.  Also, re `-r`: I think we might want to produce patches just for one file at a time, although I don't have a strong feeling about this.  At least in the spkgs that I remember, each patch is for a single file.


---

Comment by jhpalmieri created at 2011-12-05 22:49:16

For the "typo" referred to above: should we say "a spkg" or "an spkg"?  The style seems to be the latter, which is what my patch uses.  So I don't think I need to change anything.


---

Comment by drkirkby created at 2011-12-06 21:42:46

Replying to [comment:16 jhpalmieri]:
> Replying to [comment:15 drkirkby]:
> > A minor typo, with "an" instead of "a". 
> > 
> > "so if you are writing an spkg which is not part of the standard"
> 
> I will fix that, thanks.
> 
> > Personally I would have used:
> > 
>  {{{
>  diff -Naur
>  }}}
> > 
> > which seems one of the most common ways.  
> 
> Dave, I'm shocked: this doesn't seem to be Posix-standard usage :)  

An argument for including GNU 'patch' command was that it would be consistent across all systems. The Sun 'patch' command differs significantly from the GNU one. In such a case, I think we might as well use the GNU version of diff, which is /usr/bin/gdiff on hawk. 

> Also, re `-r`: I think we might want to produce patches just for one file at a time, although I don't have a strong feeling about this.  At least in the spkgs that I remember, each patch is for a single file.

That could get quite messy if for example you update configure.ac, and then generate the 'configure' script. It would seem logical to keep one patch file for any changes that are made to resolve a particular problem. But I don't have a strong feeling about it. 

dave


---

Comment by drkirkby created at 2011-12-06 22:04:13

Replying to [comment:17 jhpalmieri]:
> For the "typo" referred to above: should we say "a spkg" or "an spkg"?  The style seems to be the latter, which is what my patch uses.  So I don't think I need to change anything.

This is another thing I don't have a strong feeling about. 

http://grammar.quickanddirtytips.com/a-versus-an.aspx

says:
_The rule is  that you use a before words that start with a consonant sound and an before words that start with a vowel sound (1)._


http://en.wikipedia.org/wiki/English_articles#Discrimination_between_a_and_an

basically says the same thing, but is less clear about it. 

The letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been "a spkg" and not "an spkg". But it's not a big deal. 

Dave 

I guess 'spkg' is not a word, and I don't know if its an abbreviation for something.


---

Comment by kcrisman created at 2011-12-18 03:05:39

This is great stuff, John.  Once this is in I will actually be able to change a few spkgs to use `patch` correctly, and to more easily review them - since the syntax is there.

As a non-expert in shell syntax I will not give this a positive review, but everything I do know about seems good, and the examples are more informative.  One tiny request.  In 

```
Now provide a high-level explanation of your changes in 
``SPKG.txt``. Once you are satisfied with your changes, use Mercurial 
to check in your changes with a meaningful commit message. Next,
```

I wonder if you could put two more comments.
 * One with the syntax for the changes in SPKG.txt (the `=== pkg-name 1.4.5.p3 (John Palmieri, Octember 33 2011) ===` thing)
 * One to tell people they might as well tag the tip with the new spkg version number.  I know Jeroen currently does this anyway when merging, but it would make things easier for him (and for any new release manager eventually).


---

Comment by jhpalmieri created at 2011-12-19 19:59:01

Replying to [comment:20 kcrisman]:
> One tiny request.  

Okay, here's part 2 of the patch, which addresses your suggestions.


---

Comment by kcrisman created at 2011-12-19 20:43:08

> > One tiny request.  
> 
> Okay, here's part 2 of the patch, which addresses your suggestions.

Wow, great!  Looks good, applies to alpha4 fine, builds and doc looks great.  

As I said, I don't feel comfortable addressing the shell stuff, but I like this.  Here are a few tiny things.
 * Syntax:

```
sage -f /URL/to/package-x.y.z.spkg
```

   Maybe, just to be pedantic, 

```
sage -f http://URL/to/package-x.y.z.spkg
```

   Or maybe that will cause more confusion than the original one...
 * One actual error I found, I think.

```
matplotlib-1.0.1.p0/src/lib/matplotlib/finance.py.patch
```

   I think that should just be finance.py, right?   Should be easy to refresh the `part2.patch`, I hope.  Sorry.

 * And a teensy teensy thing:

```
A main message of this section is
}}} 
   should that be `The main`?  I realize this is "legacy documentation", but might as well spruce it up.

 * A question, probably due to ignorance:
{{{
diff -u src/configure src-patched/configure > patches/configure.patch 
}}}
   will that make a patch that actually applies correctly?  I feel like this will produce one with a header that says
{{{
--- a/src/configure
+++ b/src-patched/configure
}}}
   that wouldn't apply, as opposed to 
{{{
--- a/src/configure
+++ b/src/configure
}}}

----
Otherwise, here are things that need to be reviewed that I don't feel comfortable doing, though I'm sure they are right.
 * the argument about `diff -u` versus `diff -Naur`
 * the `[[ -z "$SAGE_LOCAL" ]]` change 
 * Changing to `--` instead of `-` for options to commands, like `sage --pkg`.
 * `cp -pR`
 * `patch -p1 <"$patch"` versus `patch -p1 < "$patch"` (the latter is probably just my imagination, but I know that shell script cares about spaces at times) and in general verifying that that is the correct syntax, though I'm sure it is based on seeing various of Leif's spkgs

Anyone who uses these a lot can check them off as correct and this can go in.

----
Regarding "a" versus "an".
> The letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been "a spkg" and not "an spkg". But it's not a big deal.
Ah, but I've never heard "spkg" pronounced other than as "esspackage".  Vowel sound.  Sort of like how different people will say "an (h)istorical" or "a historical", and both are right.


---

Comment by kcrisman created at 2011-12-19 20:43:08

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-12-19 20:45:33

> Ah, but I've never heard "spkg" pronounced other than as "esspackage".  Vowel sound.  Sort of like how different people will say "an (h)istorical" or "a historical", and both are right.

See e.g. [this book by John McWhorter](http://www.npr.org/books/titles/138991857/what-language-is-and-what-it-isnt-and-what-it-could-be) on some of these issues.  Not that I agree with everything he has to say, but it's a nice "field guide to practical linguistics".


---

Comment by jhpalmieri created at 2011-12-19 21:20:22

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-12-19 21:20:22

Replying to [comment:22 kcrisman]:
> > > One tiny request.  
> > 
> > Okay, here's part 2 of the patch, which addresses your suggestions.
> 
> Wow, great!  Looks good, applies to alpha4 fine, builds and doc looks great.  
> 
> As I said, I don't feel comfortable addressing the shell stuff, but I like this.  Here are a few tiny things.

Great, thanks for catching these.  I've updated the "part2" patch.

>  * A question, probably due to ignorance:
 {{{
 diff -u src/configure src-patched/configure > patches/configure.patch 
 }}}
>    will that make a patch that actually applies correctly?  I feel like this will produce one with a header that says
 {{{
 --- a/src/configure
 +++ b/src-patched/configure
 }}}
>    that wouldn't apply, as opposed to 

When you run "patch -p1 file.patch", it strips the file names up to the first slash ("-pN" strips up to the Nth slash), so it will patch a file "configure" in the current directory.  (So this patch command should be run after cd'ing to `src`.  I've added such a cd command to one of the examples.)

> Regarding "a" versus "an".
> > The letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been "a spkg" and not "an spkg". But it's not a big deal.
> Ah, but I've never heard "spkg" pronounced other than as "esspackage".  Vowel sound.  Sort of like how different people will say "an (h)istorical" or "a historical", and both are right.

Me too.


---

Attachment


---

Comment by kcrisman created at 2011-12-20 02:00:25

Ok, that clarifies `patch`.

I also did a _lot_ of reading of man pages and searches, and the shell stuff checks out.  I agree than `diff -u` is totally appropriate for this particular context of creating spkg patches (not in general!).  

Last question (but positive review!) - why

```
[[ -z "$SAGE_LOCAL" ]]
```

and not 

```
[ -z "$SAGE_LOCAL" ]
```

since it seems like in this situation (no 'and's) they behave identically?


---

Comment by kcrisman created at 2011-12-20 02:00:25

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2011-12-20 06:37:20

Replying to [comment:25 kcrisman]:
> Ok, that clarifies `patch`.
> 
> I also did a _lot_ of reading of man pages and searches, and the shell stuff checks out. 

Great!  Thanks for doing that work.

> Last question (but positive review!) - why
 {{{
 [This is the Trac macro *-z "$SAGE_LOCAL" * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-z "$SAGE_LOCAL" -macro)
 }}}
>and not 
 {{{
 [ -z "$SAGE_LOCAL" ]
 }}}
> since it seems like in this situation (no 'and's) they behave identically?

I think they do behave identically.  The double bracket version calls a bash built-in function, whereas the single bracket version runs another program.  So the double bracket version is faster, although it doesn't matter too much here of course.  I think that if we're using bash scripts, using double brackets is slightly preferable to single ones: double brackets are faster and have some extra functionality.  I found [this link](http://stackoverflow.com/questions/2188199/bash-double-or-single-bracket-parentheses-curly-braces) and [this one](http://stackoverflow.com/questions/669452/is-preferable-over-in-bash-scripts), which seem like good explanations.


---

Comment by jdemeyer created at 2011-12-24 01:03:25

Resolution: fixed


---

Comment by pipedream created at 2011-12-24 04:17:41

http://www.sagemath.org/doc/developer/patching_spkgs.html still says to use cp and not patch.


---

Comment by jhpalmieri created at 2011-12-24 05:45:26

Replying to [comment:29 pipedream]:
> http://www.sagemath.org/doc/developer/patching_spkgs.html still says to use cp and not patch.

The patch was merged into 4.8.alpha6, a prerelease.  Once 4.8 is released, the on-line documentation should get updated.
