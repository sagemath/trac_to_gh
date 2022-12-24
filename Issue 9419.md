# Issue 9419: Update Developers Guide to state how patches should be made.

archive/issues_009419.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  leif jdemeyer pipedream\n\nAs discussed here\n\nhttp://groups.google.co.uk/group/sage-devel/browse_thread/thread/c566520374106df3\n\n[GNU patch](http://savannah.gnu.org/projects/patch/) will be added to Sage. This is ticket #9418. \n\nIn order to make use of the command, the developers guide will need to be updated to reflect a new way of making patch commands. We should sort out the details as precisely as possible, so everyone uses the exact same method.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9419\n\n",
    "created_at": "2010-07-03T08:36:32Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "Update Developers Guide to state how patches should be made.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9419",
    "user": "drkirkby"
}
```
Assignee: mvngu

CC:  leif jdemeyer pipedream

As discussed here

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/c566520374106df3

[GNU patch](http://savannah.gnu.org/projects/patch/) will be added to Sage. This is ticket #9418. 

In order to make use of the command, the developers guide will need to be updated to reflect a new way of making patch commands. We should sort out the details as precisely as possible, so everyone uses the exact same method.

Issue created by migration from https://trac.sagemath.org/ticket/9419





---

archive/issue_comments_089811.json:
```json
{
    "body": "Hopefully finished before Sage 5.0 comes out... ;-)",
    "created_at": "2010-11-21T21:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89811",
    "user": "leif"
}
```

Hopefully finished before Sage 5.0 comes out... ;-)



---

archive/issue_comments_089812.json:
```json
{
    "body": "I will do a first attempt at writing this up...",
    "created_at": "2010-11-22T20:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89812",
    "user": "jdemeyer"
}
```

I will do a first attempt at writing this up...



---

archive/issue_comments_089813.json:
```json
{
    "body": "How do you like the following high-level steps, suppose we want to create sphinx-1.0.4.p3\n\n\n```\n1) create a directory sphinx-1.0.4.p3\n2) put upstream source in sphinx-1.0.4.p3/src\nFor every ISSUE which needs to be patched, do the following:\n    3) cp -pr sphinx-1.0.4.p3 sphinx-1.0.4.p3.patched\n    4) edit sphinx-1.0.4.p3.patched/src to fix ISSUE.\n    5) diff -ur sphinx-1.0.4.p3/src sphinx-1.0.4.p3.patched/src >sphinx-1.0.4.p3/patches/ISSUE.patch\n    6) rm -r sphinx-1.0.4.p3.patched\n```\n",
    "created_at": "2010-11-22T20:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89813",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_089814.json:
```json
{
    "body": "For applying the patches in `spkg-install`:\n\n\n```\npatch -p1 <src/ISSUE.patch\n```\n",
    "created_at": "2010-11-22T20:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89814",
    "user": "jdemeyer"
}
```

For applying the patches in `spkg-install`:


```
patch -p1 <src/ISSUE.patch
```




---

archive/issue_comments_089815.json:
```json
{
    "body": "Changing keywords from \"\" to \"patch doc\".",
    "created_at": "2010-11-28T10:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89815",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "patch doc".



---

archive/issue_comments_089816.json:
```json
{
    "body": "After thinking about it some more, perhaps the following is better:\n\n```\n1) create a directory sphinx-1.0.4.p3\n2) cd sphinx-1.0.4.p3\n2) put upstream source in sphinx-1.0.4.p3/src\nFor every ISSUE which needs to be patched, do the following:\n    3) cp -pr src src.patched\n    4) edit src.patched to fix ISSUE.\n    5) diff -ur src src.patched >patches/ISSUE.patch\n    6) rm -r src.patched\n```\n\n\nTo apply the patches in `spkg-install`:\n\n```\n1) cd src\n2) patch -p1 <../patches/ISSUE.patch\n```\n",
    "created_at": "2010-11-28T10:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89816",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_089817.json:
```json
{
    "body": "So, in what order should `patches/*.patch` be applied?\n\nIt's not *that* unlikely *in principle \"unrelated\"* patches affect the same parts of code (or at least modify parts near to each other in the same file), such that multiple patches against vanilla upstream source won't apply smoothly in (arbitrary) sequence.\n\nThere should (in addition) be some documentation on what files are patched by what \"ISSUE\", I'd suggest in an `SPKG.txt` section and / or a `patches/README`[`.txt`]. (If \"ISSUE\" is almost self-explanatory, we don't need extra comments in `spkg-install`, but then other files should contain further details and references to the relevant tickets.)\n\nWhat if some patches only have to be applied on platform XY?\n\nI think creating `src-$ISSUE/` for each \"ISSUE\" and then doing `diff -ur src/ src-$ISSUE/ > patches/$ISSUE.patch` is equally valid.\n\nAnd IMHO doing e.g. `cd src/ && diff -u file.orig file > ../patches/file.patch` should be valid for \"simple\" patches as well (then using `cd src ; patch -p0 < ../patches/file.patch`, or omitting the `-p0`), though perhaps using `diff -u src/file.orig src/file ...` (and applying them from the top level spkg directory) would be better.\n\nSo I'm not convinced there is a single best way to go in all cases.",
    "created_at": "2010-11-29T17:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89817",
    "user": "leif"
}
```

So, in what order should `patches/*.patch` be applied?

It's not *that* unlikely *in principle "unrelated"* patches affect the same parts of code (or at least modify parts near to each other in the same file), such that multiple patches against vanilla upstream source won't apply smoothly in (arbitrary) sequence.

There should (in addition) be some documentation on what files are patched by what "ISSUE", I'd suggest in an `SPKG.txt` section and / or a `patches/README`[`.txt`]. (If "ISSUE" is almost self-explanatory, we don't need extra comments in `spkg-install`, but then other files should contain further details and references to the relevant tickets.)

What if some patches only have to be applied on platform XY?

I think creating `src-$ISSUE/` for each "ISSUE" and then doing `diff -ur src/ src-$ISSUE/ > patches/$ISSUE.patch` is equally valid.

And IMHO doing e.g. `cd src/ && diff -u file.orig file > ../patches/file.patch` should be valid for "simple" patches as well (then using `cd src ; patch -p0 < ../patches/file.patch`, or omitting the `-p0`), though perhaps using `diff -u src/file.orig src/file ...` (and applying them from the top level spkg directory) would be better.

So I'm not convinced there is a single best way to go in all cases.



---

archive/issue_comments_089818.json:
```json
{
    "body": "Also, the *Dependencies* section of `SPKG.txt` should explicitly contain [GNU] `patch` if it is used by an spkg.\n\n(I'd prefer *selectively* adding \"patch\" as a dependency in `spkg/standard/deps`, too.)",
    "created_at": "2010-11-29T20:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89818",
    "user": "leif"
}
```

Also, the *Dependencies* section of `SPKG.txt` should explicitly contain [GNU] `patch` if it is used by an spkg.

(I'd prefer *selectively* adding "patch" as a dependency in `spkg/standard/deps`, too.)



---

archive/issue_comments_089819.json:
```json
{
    "body": "Replying to [comment:6 leif]:\n> So, in what order should `patches/*.patch` be applied?\nThat's up to the writer of `spkg-install`.\n\n> There should (in addition) be some documentation on what files are patched by what \"ISSUE\", I'd suggest in an `SPKG.txt` section and / or a `patches/README`[`.txt`]. (If \"ISSUE\" is almost self-explanatory, we don't need extra comments in `spkg-install`, but then other files should contain further details and references to the relevant tickets.)\nAgreed.  I prefer in `SPKG.txt` because then all the information about the package is contained in one file.\n\n> What if some patches only have to be applied on platform XY?\nSame as today.  Instead of a conditional `cp`, we have a conditional `patch`.\n\n> I think creating `src-$ISSUE/` for each \"ISSUE\" and then doing `diff -ur src/ src-$ISSUE/ > patches/$ISSUE.patch` is equally valid.\nAgreed.\n\n> And IMHO doing e.g. `cd src/ && diff -u file.orig file > ../patches/file.patch` should be valid for \"simple\" patches as well (then using `cd src ; patch -p0 < ../patches/file.patch`, or omitting the `-p0`)\nI would prefer that all patches can be *applied* the same way, namely from `src/` with a `-p1` strip level.  So I disagree.\n\n> though perhaps using `diff -u src/file.orig src/file ...` (and applying them from the top level spkg directory) would be better.\nOkay for me.",
    "created_at": "2010-11-29T20:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89819",
    "user": "jdemeyer"
}
```

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
I would prefer that all patches can be *applied* the same way, namely from `src/` with a `-p1` strip level.  So I disagree.

> though perhaps using `diff -u src/file.orig src/file ...` (and applying them from the top level spkg directory) would be better.
Okay for me.



---

archive/issue_comments_089820.json:
```json
{
    "body": "Replying to [comment:2 jdemeyer]:\n> I will do a first attempt at writing this up...\n\nDid you get anywhere with this? The issue is quite important, as currently the developers guide is still advising the use of 'cp'  and saying not to use 'patch'. \n\nOne thing we need to be careful of is that when testing the patch, people don't overwrite the src directory. Which makes me think, should the write permissions for all files below src be removed? That would at least prevent that accident, though perhaps it would screw up some packages. \n\nDave",
    "created_at": "2011-04-28T05:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89820",
    "user": "drkirkby"
}
```

Replying to [comment:2 jdemeyer]:
> I will do a first attempt at writing this up...

Did you get anywhere with this? The issue is quite important, as currently the developers guide is still advising the use of 'cp'  and saying not to use 'patch'. 

One thing we need to be careful of is that when testing the patch, people don't overwrite the src directory. Which makes me think, should the write permissions for all files below src be removed? That would at least prevent that accident, though perhaps it would screw up some packages. 

Dave



---

archive/issue_comments_089821.json:
```json
{
    "body": "Also, the *Developer's Guide* should state how to check the exit code(s) of `patch`, i.e. **we should IMHO test `$?` of *every* application of `patch`** (cf. [my comment here](http://trac.sagemath.org/sage_trac/ticket/11246#comment:21)):\n\n *[...] Fortunately, we now use `patch` rather than `cp`, which at least spits out warning or error messages in case upstream and `patches/*` get out of sync (or someone made another mistake), but these messages are easily missed - even by a reviewer, which can lead to all kinds of obscure errors or misbehavior **any time later**, so we should IMHO check `$?` there. [...]*\n\nIf we apply many patches in a loop (which I don't really like since this badly documents *what* is actually patched *why*, but see documentation-related discussion above), we should at least \"accumulate\" the outcome, i.e. test once all patches were successfully applied.\n\nWe could even check if they applied seamlessly, without fuzz (which I think should be the case in spkgs; otherwise they should get rebased).\n\nOpinions?",
    "created_at": "2011-07-03T11:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89821",
    "user": "leif"
}
```

Also, the *Developer's Guide* should state how to check the exit code(s) of `patch`, i.e. **we should IMHO test `$?` of *every* application of `patch`** (cf. [my comment here](http://trac.sagemath.org/sage_trac/ticket/11246#comment:21)):

 *[...] Fortunately, we now use `patch` rather than `cp`, which at least spits out warning or error messages in case upstream and `patches/*` get out of sync (or someone made another mistake), but these messages are easily missed - even by a reviewer, which can lead to all kinds of obscure errors or misbehavior **any time later**, so we should IMHO check `$?` there. [...]*

If we apply many patches in a loop (which I don't really like since this badly documents *what* is actually patched *why*, but see documentation-related discussion above), we should at least "accumulate" the outcome, i.e. test once all patches were successfully applied.

We could even check if they applied seamlessly, without fuzz (which I think should be the case in spkgs; otherwise they should get rebased).

Opinions?



---

archive/issue_comments_089822.json:
```json
{
    "body": "Changing keywords from \"patch doc\" to \"patch doc howto spkgs diff\".",
    "created_at": "2011-07-03T11:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89822",
    "user": "leif"
}
```

Changing keywords from "patch doc" to "patch doc howto spkgs diff".



---

archive/issue_comments_089823.json:
```json
{
    "body": "Replying to [comment:9 drkirkby]:\n> One thing we need to be careful of is that when testing the patch, people don't overwrite the src directory. Which makes me think, should the write permissions for all files below src be removed? That would at least prevent that accident, though perhaps it would screw up some packages.\n\nWell, you usually *want (or need) to overwrite / modify* files in `src/` when applying patches from within `spkg-install`...\n\nNote that you don't need write permissions on a file you're going to patch, but on its containing directory.",
    "created_at": "2011-07-03T11:44:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89823",
    "user": "leif"
}
```

Replying to [comment:9 drkirkby]:
> One thing we need to be careful of is that when testing the patch, people don't overwrite the src directory. Which makes me think, should the write permissions for all files below src be removed? That would at least prevent that accident, though perhaps it would screw up some packages.

Well, you usually *want (or need) to overwrite / modify* files in `src/` when applying patches from within `spkg-install`...

Note that you don't need write permissions on a file you're going to patch, but on its containing directory.



---

archive/issue_comments_089824.json:
```json
{
    "body": "Replying to [comment:2 jdemeyer]:\n> I will do a first attempt at writing this up...\n\nJeroen, do you already have some draft of a new section for the Developer's Guide (replacing [*\"Use `cp` for patching\"*](http://www.sagemath.org/doc/developer/patching_spkgs.html#use-cp-for-patching))?",
    "created_at": "2011-07-03T14:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89824",
    "user": "leif"
}
```

Replying to [comment:2 jdemeyer]:
> I will do a first attempt at writing this up...

Jeroen, do you already have some draft of a new section for the Developer's Guide (replacing [*"Use `cp` for patching"*](http://www.sagemath.org/doc/developer/patching_spkgs.html#use-cp-for-patching))?



---

archive/issue_comments_089825.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-07-03T15:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89825",
    "user": "leif"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_089826.json:
```json
{
    "body": "Ok, I just started rewriting `doc/en/developer/{producing,patching}_spkgs.rst`.\n\n**Q:** Should patches to upstream source (also? optionally?) be documented in `patches/README.txt` or whatever it is called, or just - i.e. only - in `SPKG.txt`'s *Special Update/Build Instructions* section (or even a new one, \"*Patches*\")?",
    "created_at": "2011-07-03T15:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89826",
    "user": "leif"
}
```

Ok, I just started rewriting `doc/en/developer/{producing,patching}_spkgs.rst`.

**Q:** Should patches to upstream source (also? optionally?) be documented in `patches/README.txt` or whatever it is called, or just - i.e. only - in `SPKG.txt`'s *Special Update/Build Instructions* section (or even a new one, "*Patches*")?



---

archive/issue_comments_089827.json:
```json
{
    "body": "Here's an attempt at a patch.  (I'm tired of wanting to refer people in sage-devel to the Developer's Guide, but then hesitating because of its out-dated insistence on using 'cp' instead of 'patch', and nothing seems to be happening with this.  Plus I'm trying to avoid grading an exam.)",
    "created_at": "2011-11-23T00:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89827",
    "user": "jhpalmieri"
}
```

Here's an attempt at a patch.  (I'm tired of wanting to refer people in sage-devel to the Developer's Guide, but then hesitating because of its out-dated insistence on using 'cp' instead of 'patch', and nothing seems to be happening with this.  Plus I'm trying to avoid grading an exam.)



---

archive/issue_comments_089828.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-11-23T00:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89828",
    "user": "jhpalmieri"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_089829.json:
```json
{
    "body": "Attachment [trac_9419-use-patch.patch](tarball://root/attachments/some-uuid/ticket9419/trac_9419-use-patch.patch) by drkirkby created at 2011-12-01 06:32:06\n\nA minor typo, with \"an\" instead of \"a\". \n\n\"so if you are writing an spkg which is not part of the standard\"\n\nPersonally I would have used:\n\n\n```\ndiff -Naur\n```\n\n\nwhich seems one of the most common ways. There's some discussion in \n\nhttp://linux.die.net/man/1/patch\n\nof the best arguments to use. The main change is that this is recursive, so if one edits multiple files to make a change to sort out some problem, there can be one patch file to resolve the problem, rather than having to make one for each file. \n\nDave",
    "created_at": "2011-12-01T06:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89829",
    "user": "drkirkby"
}
```

Attachment [trac_9419-use-patch.patch](tarball://root/attachments/some-uuid/ticket9419/trac_9419-use-patch.patch) by drkirkby created at 2011-12-01 06:32:06

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

archive/issue_comments_089830.json:
```json
{
    "body": "Replying to [comment:15 drkirkby]:\n> A minor typo, with \"an\" instead of \"a\". \n> \n> \"so if you are writing an spkg which is not part of the standard\"\n\nI will fix that, thanks.\n\n> Personally I would have used:\n> \n {{{\n diff -Naur\n }}}\n> \n> which seems one of the most common ways.  \n\nDave, I'm shocked: this doesn't seem to be Posix-standard usage :)  For example, as far as I can tell, on your machine hawk neither `-N` nor `-a` are supported.  Also, re `-r`: I think we might want to produce patches just for one file at a time, although I don't have a strong feeling about this.  At least in the spkgs that I remember, each patch is for a single file.",
    "created_at": "2011-12-04T02:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89830",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_089831.json:
```json
{
    "body": "For the \"typo\" referred to above: should we say \"a spkg\" or \"an spkg\"?  The style seems to be the latter, which is what my patch uses.  So I don't think I need to change anything.",
    "created_at": "2011-12-05T22:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89831",
    "user": "jhpalmieri"
}
```

For the "typo" referred to above: should we say "a spkg" or "an spkg"?  The style seems to be the latter, which is what my patch uses.  So I don't think I need to change anything.



---

archive/issue_comments_089832.json:
```json
{
    "body": "Replying to [comment:16 jhpalmieri]:\n> Replying to [comment:15 drkirkby]:\n> > A minor typo, with \"an\" instead of \"a\". \n> > \n> > \"so if you are writing an spkg which is not part of the standard\"\n> \n> I will fix that, thanks.\n> \n> > Personally I would have used:\n> > \n>  {{{\n>  diff -Naur\n>  }}}\n> > \n> > which seems one of the most common ways.  \n> \n> Dave, I'm shocked: this doesn't seem to be Posix-standard usage :)  \n\nAn argument for including GNU 'patch' command was that it would be consistent across all systems. The Sun 'patch' command differs significantly from the GNU one. In such a case, I think we might as well use the GNU version of diff, which is /usr/bin/gdiff on hawk. \n\n> Also, re `-r`: I think we might want to produce patches just for one file at a time, although I don't have a strong feeling about this.  At least in the spkgs that I remember, each patch is for a single file.\n\nThat could get quite messy if for example you update configure.ac, and then generate the 'configure' script. It would seem logical to keep one patch file for any changes that are made to resolve a particular problem. But I don't have a strong feeling about it. \n\ndave",
    "created_at": "2011-12-06T21:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89832",
    "user": "drkirkby"
}
```

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

archive/issue_comments_089833.json:
```json
{
    "body": "Replying to [comment:17 jhpalmieri]:\n> For the \"typo\" referred to above: should we say \"a spkg\" or \"an spkg\"?  The style seems to be the latter, which is what my patch uses.  So I don't think I need to change anything.\n\nThis is another thing I don't have a strong feeling about. \n\nhttp://grammar.quickanddirtytips.com/a-versus-an.aspx\n\nsays:\n*The rule is  that you use a before words that start with a consonant sound and an before words that start with a vowel sound (1).*\n\n\nhttp://en.wikipedia.org/wiki/English_articles#Discrimination_between_a_and_an\n\nbasically says the same thing, but is less clear about it. \n\nThe letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been \"a spkg\" and not \"an spkg\". But it's not a big deal. \n\nDave \n\nI guess 'spkg' is not a word, and I don't know if its an abbreviation for something.",
    "created_at": "2011-12-06T22:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89833",
    "user": "drkirkby"
}
```

Replying to [comment:17 jhpalmieri]:
> For the "typo" referred to above: should we say "a spkg" or "an spkg"?  The style seems to be the latter, which is what my patch uses.  So I don't think I need to change anything.

This is another thing I don't have a strong feeling about. 

http://grammar.quickanddirtytips.com/a-versus-an.aspx

says:
*The rule is  that you use a before words that start with a consonant sound and an before words that start with a vowel sound (1).*


http://en.wikipedia.org/wiki/English_articles#Discrimination_between_a_and_an

basically says the same thing, but is less clear about it. 

The letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been "a spkg" and not "an spkg". But it's not a big deal. 

Dave 

I guess 'spkg' is not a word, and I don't know if its an abbreviation for something.



---

archive/issue_comments_089834.json:
```json
{
    "body": "This is great stuff, John.  Once this is in I will actually be able to change a few spkgs to use `patch` correctly, and to more easily review them - since the syntax is there.\n\nAs a non-expert in shell syntax I will not give this a positive review, but everything I do know about seems good, and the examples are more informative.  One tiny request.  In \n\n```\nNow provide a high-level explanation of your changes in \n``SPKG.txt``. Once you are satisfied with your changes, use Mercurial \nto check in your changes with a meaningful commit message. Next,\n```\n\nI wonder if you could put two more comments.\n* One with the syntax for the changes in SPKG.txt (the `=== pkg-name 1.4.5.p3 (John Palmieri, Octember 33 2011) ===` thing)\n* One to tell people they might as well tag the tip with the new spkg version number.  I know Jeroen currently does this anyway when merging, but it would make things easier for him (and for any new release manager eventually).",
    "created_at": "2011-12-18T03:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89834",
    "user": "kcrisman"
}
```

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

archive/issue_comments_089835.json:
```json
{
    "body": "Replying to [comment:20 kcrisman]:\n> One tiny request.  \n\nOkay, here's part 2 of the patch, which addresses your suggestions.",
    "created_at": "2011-12-19T19:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89835",
    "user": "jhpalmieri"
}
```

Replying to [comment:20 kcrisman]:
> One tiny request.  

Okay, here's part 2 of the patch, which addresses your suggestions.



---

archive/issue_comments_089836.json:
```json
{
    "body": "> > One tiny request.  \n> \n> Okay, here's part 2 of the patch, which addresses your suggestions.\n\nWow, great!  Looks good, applies to alpha4 fine, builds and doc looks great.  \n\nAs I said, I don't feel comfortable addressing the shell stuff, but I like this.  Here are a few tiny things.\n* Syntax:\n\n```\nsage -f /URL/to/package-x.y.z.spkg\n```\n\n   Maybe, just to be pedantic, \n\n```\nsage -f http://URL/to/package-x.y.z.spkg\n```\n\n   Or maybe that will cause more confusion than the original one...\n* One actual error I found, I think.\n\n```\nmatplotlib-1.0.1.p0/src/lib/matplotlib/finance.py.patch\n```\n\n   I think that should just be finance.py, right?   Should be easy to refresh the `part2.patch`, I hope.  Sorry.\n\n* And a teensy teensy thing:\n\n```\nA main message of this section is\n```\n \n   should that be `The main`?  I realize this is \"legacy documentation\", but might as well spruce it up.\n\n* A question, probably due to ignorance:\n\n```\ndiff -u src/configure src-patched/configure > patches/configure.patch \n```\n\n   will that make a patch that actually applies correctly?  I feel like this will produce one with a header that says\n\n```\n--- a/src/configure\n+++ b/src-patched/configure\n```\n\n   that wouldn't apply, as opposed to \n\n```\n--- a/src/configure\n+++ b/src/configure\n```\n\n\n----\nOtherwise, here are things that need to be reviewed that I don't feel comfortable doing, though I'm sure they are right.\n* the argument about `diff -u` versus `diff -Naur`\n* the `[This is the Trac macro *-z \"$SAGE_LOCAL\" * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-z \"$SAGE_LOCAL\" -macro)` change \n* Changing to `--` instead of `-` for options to commands, like `sage --pkg`.\n* `cp -pR`\n* `patch -p1 <\"$patch\"` versus `patch -p1 < \"$patch\"` (the latter is probably just my imagination, but I know that shell script cares about spaces at times) and in general verifying that that is the correct syntax, though I'm sure it is based on seeing various of Leif's spkgs\n\nAnyone who uses these a lot can check them off as correct and this can go in.\n\n----\nRegarding \"a\" versus \"an\".\n> The letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been \"a spkg\" and not \"an spkg\". But it's not a big deal.\nAh, but I've never heard \"spkg\" pronounced other than as \"esspackage\".  Vowel sound.  Sort of like how different people will say \"an (h)istorical\" or \"a historical\", and both are right.",
    "created_at": "2011-12-19T20:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89836",
    "user": "kcrisman"
}
```

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
```
 
   should that be `The main`?  I realize this is "legacy documentation", but might as well spruce it up.

* A question, probably due to ignorance:

```
diff -u src/configure src-patched/configure > patches/configure.patch 
```

   will that make a patch that actually applies correctly?  I feel like this will produce one with a header that says

```
--- a/src/configure
+++ b/src-patched/configure
```

   that wouldn't apply, as opposed to 

```
--- a/src/configure
+++ b/src/configure
```


----
Otherwise, here are things that need to be reviewed that I don't feel comfortable doing, though I'm sure they are right.
* the argument about `diff -u` versus `diff -Naur`
* the `[This is the Trac macro *-z "$SAGE_LOCAL" * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-z "$SAGE_LOCAL" -macro)` change 
* Changing to `--` instead of `-` for options to commands, like `sage --pkg`.
* `cp -pR`
* `patch -p1 <"$patch"` versus `patch -p1 < "$patch"` (the latter is probably just my imagination, but I know that shell script cares about spaces at times) and in general verifying that that is the correct syntax, though I'm sure it is based on seeing various of Leif's spkgs

Anyone who uses these a lot can check them off as correct and this can go in.

----
Regarding "a" versus "an".
> The letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been "a spkg" and not "an spkg". But it's not a big deal.
Ah, but I've never heard "spkg" pronounced other than as "esspackage".  Vowel sound.  Sort of like how different people will say "an (h)istorical" or "a historical", and both are right.



---

archive/issue_comments_089837.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-19T20:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89837",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089838.json:
```json
{
    "body": "> Ah, but I've never heard \"spkg\" pronounced other than as \"esspackage\".  Vowel sound.  Sort of like how different people will say \"an (h)istorical\" or \"a historical\", and both are right.\n\nSee e.g. [this book by John McWhorter](http://www.npr.org/books/titles/138991857/what-language-is-and-what-it-isnt-and-what-it-could-be) on some of these issues.  Not that I agree with everything he has to say, but it's a nice \"field guide to practical linguistics\".",
    "created_at": "2011-12-19T20:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89838",
    "user": "kcrisman"
}
```

> Ah, but I've never heard "spkg" pronounced other than as "esspackage".  Vowel sound.  Sort of like how different people will say "an (h)istorical" or "a historical", and both are right.

See e.g. [this book by John McWhorter](http://www.npr.org/books/titles/138991857/what-language-is-and-what-it-isnt-and-what-it-could-be) on some of these issues.  Not that I agree with everything he has to say, but it's a nice "field guide to practical linguistics".



---

archive/issue_comments_089839.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-19T21:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89839",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089840.json:
```json
{
    "body": "Replying to [comment:22 kcrisman]:\n> > > One tiny request.  \n> > \n> > Okay, here's part 2 of the patch, which addresses your suggestions.\n> \n> Wow, great!  Looks good, applies to alpha4 fine, builds and doc looks great.  \n> \n> As I said, I don't feel comfortable addressing the shell stuff, but I like this.  Here are a few tiny things.\n\nGreat, thanks for catching these.  I've updated the \"part2\" patch.\n\n>  * A question, probably due to ignorance:\n {{{\n diff -u src/configure src-patched/configure > patches/configure.patch \n }}}\n>    will that make a patch that actually applies correctly?  I feel like this will produce one with a header that says\n {{{\n --- a/src/configure\n +++ b/src-patched/configure\n }}}\n>    that wouldn't apply, as opposed to \n\nWhen you run \"patch -p1 file.patch\", it strips the file names up to the first slash (\"-pN\" strips up to the Nth slash), so it will patch a file \"configure\" in the current directory.  (So this patch command should be run after cd'ing to `src`.  I've added such a cd command to one of the examples.)\n\n> Regarding \"a\" versus \"an\".\n> > The letter 's' is certainly a consonant, and not a vowel, and I don't think 'spkg' sounds like a vowel (as for example 'hour' does, despite it starting with a consonant). So I would have thought it should have been \"a spkg\" and not \"an spkg\". But it's not a big deal.\n> Ah, but I've never heard \"spkg\" pronounced other than as \"esspackage\".  Vowel sound.  Sort of like how different people will say \"an (h)istorical\" or \"a historical\", and both are right.\n\nMe too.",
    "created_at": "2011-12-19T21:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89840",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_089841.json:
```json
{
    "body": "Attachment [trac_9419-part2.patch](tarball://root/attachments/some-uuid/ticket9419/trac_9419-part2.patch) by jhpalmieri created at 2011-12-19 21:21:22",
    "created_at": "2011-12-19T21:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89841",
    "user": "jhpalmieri"
}
```

Attachment [trac_9419-part2.patch](tarball://root/attachments/some-uuid/ticket9419/trac_9419-part2.patch) by jhpalmieri created at 2011-12-19 21:21:22



---

archive/issue_comments_089842.json:
```json
{
    "body": "Ok, that clarifies `patch`.\n\nI also did a *lot* of reading of man pages and searches, and the shell stuff checks out.  I agree than `diff -u` is totally appropriate for this particular context of creating spkg patches (not in general!).  \n\nLast question (but positive review!) - why\n\n```\n[[ -z \"$SAGE_LOCAL\" ]]\n```\n\nand not \n\n```\n[ -z \"$SAGE_LOCAL\" ]\n```\n\nsince it seems like in this situation (no 'and's) they behave identically?",
    "created_at": "2011-12-20T02:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89842",
    "user": "kcrisman"
}
```

Ok, that clarifies `patch`.

I also did a *lot* of reading of man pages and searches, and the shell stuff checks out.  I agree than `diff -u` is totally appropriate for this particular context of creating spkg patches (not in general!).  

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

archive/issue_comments_089843.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-20T02:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89843",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089844.json:
```json
{
    "body": "Replying to [comment:25 kcrisman]:\n> Ok, that clarifies `patch`.\n> \n> I also did a *lot* of reading of man pages and searches, and the shell stuff checks out. \n\nGreat!  Thanks for doing that work.\n\n> Last question (but positive review!) - why\n {{{\n [This is the Trac macro *-z \"$SAGE_LOCAL\" * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-z \"$SAGE_LOCAL\" -macro)\n }}}\n>and not \n {{{\n [ -z \"$SAGE_LOCAL\" ]\n }}}\n> since it seems like in this situation (no 'and's) they behave identically?\n\nI think they do behave identically.  The double bracket version calls a bash built-in function, whereas the single bracket version runs another program.  So the double bracket version is faster, although it doesn't matter too much here of course.  I think that if we're using bash scripts, using double brackets is slightly preferable to single ones: double brackets are faster and have some extra functionality.  I found [this link](http://stackoverflow.com/questions/2188199/bash-double-or-single-bracket-parentheses-curly-braces) and [this one](http://stackoverflow.com/questions/669452/is-preferable-over-in-bash-scripts), which seem like good explanations.",
    "created_at": "2011-12-20T06:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89844",
    "user": "jhpalmieri"
}
```

Replying to [comment:25 kcrisman]:
> Ok, that clarifies `patch`.
> 
> I also did a *lot* of reading of man pages and searches, and the shell stuff checks out. 

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

archive/issue_comments_089845.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-24T01:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89845",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_089846.json:
```json
{
    "body": "http://www.sagemath.org/doc/developer/patching_spkgs.html still says to use cp and not patch.",
    "created_at": "2011-12-24T04:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89846",
    "user": "pipedream"
}
```

http://www.sagemath.org/doc/developer/patching_spkgs.html still says to use cp and not patch.



---

archive/issue_comments_089847.json:
```json
{
    "body": "Replying to [comment:29 pipedream]:\n> http://www.sagemath.org/doc/developer/patching_spkgs.html still says to use cp and not patch.\n\nThe patch was merged into 4.8.alpha6, a prerelease.  Once 4.8 is released, the on-line documentation should get updated.",
    "created_at": "2011-12-24T05:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9419",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9419#issuecomment-89847",
    "user": "jhpalmieri"
}
```

Replying to [comment:29 pipedream]:
> http://www.sagemath.org/doc/developer/patching_spkgs.html still says to use cp and not patch.

The patch was merged into 4.8.alpha6, a prerelease.  Once 4.8 is released, the on-line documentation should get updated.
