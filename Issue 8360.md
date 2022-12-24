# Issue 8360: Add an interface to Jean-Eric Pin's Semigroupe package

archive/issues_008360.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat jean-eric.pin@liafa.jussieu.fr abmasse tscrim\n\nKeywords: Semigroupes\n\nAdd an interface to Jean-Eric Pin's Semigroupe package\n\nhttp://www.liafa.jussieu.fr/~jep/semigroupes.html\n\nPatch and spkg under development on the Sage-Combinat server.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8360\n\n",
    "created_at": "2010-02-25T09:00:20Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "Add an interface to Jean-Eric Pin's Semigroupe package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8360",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat jean-eric.pin@liafa.jussieu.fr abmasse tscrim

Keywords: Semigroupes

Add an interface to Jean-Eric Pin's Semigroupe package

http://www.liafa.jussieu.fr/~jep/semigroupes.html

Patch and spkg under development on the Sage-Combinat server.

Issue created by migration from https://trac.sagemath.org/ticket/8360





---

archive/issue_comments_074698.json:
```json
{
    "body": "Attachment [Semigroupe-2.0.spkg](tarball://root/attachments/some-uuid/ticket8360/Semigroupe-2.0.spkg) by nthiery created at 2010-03-16 13:04:44",
    "created_at": "2010-03-16T13:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74698",
    "user": "nthiery"
}
```

Attachment [Semigroupe-2.0.spkg](tarball://root/attachments/some-uuid/ticket8360/Semigroupe-2.0.spkg) by nthiery created at 2010-03-16 13:04:44



---

archive/issue_comments_074699.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-16T13:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74699",
    "user": "nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_074700.json:
```json
{
    "body": "Superceedes the previous spkg",
    "created_at": "2010-03-17T20:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74700",
    "user": "nthiery"
}
```

Superceedes the previous spkg



---

archive/issue_comments_074701.json:
```json
{
    "body": "Attachment [semigroupe-2.0.spkg](tarball://root/attachments/some-uuid/ticket8360/semigroupe-2.0.spkg) by nthiery created at 2010-03-17 20:26:28",
    "created_at": "2010-03-17T20:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74701",
    "user": "nthiery"
}
```

Attachment [semigroupe-2.0.spkg](tarball://root/attachments/some-uuid/ticket8360/semigroupe-2.0.spkg) by nthiery created at 2010-03-17 20:26:28



---

archive/issue_comments_074702.json:
```json
{
    "body": "There seems to be a problem on a 64bit machine. After installing the spkg, the following commands will cause Sage to segfault:\n\n```\nsage: W = CoxeterGroup([\"H\",4])\nsage: S = semigroupe.AutomaticSemigroup(W.semigroup_generators(), W.one(), category = FiniteCoxeterGroups())\nsage: S.cardinality()\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in Sage.\n...\n```\n\n\nThe problem seems to be with compiling Semigroupe on a 64bit machine. After installing the package, the following segfaults:\n\n```\nkarkwa: cd $SAGE_ROOT/local/bin\nkarkwa: Semigroupe\nkarkwa: ./Semigroupe\nSegmentation fault\nkarkwa: ./SelfContainedTest \nToto\na | 2  3  1 \nb | 2  1  3 \nc | 1  2  1 \n\nSegmentation fault\nkarkwa: ./SemigroupeModuleTest \n\na | 2  1 \nb | 1  1 \n\nSegmentation fault \n```\n\nI think that the two test suites (I think they are test suites...) should be run by the `spkg-check` script.",
    "created_at": "2010-05-11T20:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74702",
    "user": "saliola"
}
```

There seems to be a problem on a 64bit machine. After installing the spkg, the following commands will cause Sage to segfault:

```
sage: W = CoxeterGroup(["H",4])
sage: S = semigroupe.AutomaticSemigroup(W.semigroup_generators(), W.one(), category = FiniteCoxeterGroups())
sage: S.cardinality()
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in Sage.
...
```


The problem seems to be with compiling Semigroupe on a 64bit machine. After installing the package, the following segfaults:

```
karkwa: cd $SAGE_ROOT/local/bin
karkwa: Semigroupe
karkwa: ./Semigroupe
Segmentation fault
karkwa: ./SelfContainedTest 
Toto
a | 2  3  1 
b | 2  1  3 
c | 1  2  1 

Segmentation fault
karkwa: ./SemigroupeModuleTest 

a | 2  1 
b | 1  1 

Segmentation fault 
```

I think that the two test suites (I think they are test suites...) should be run by the `spkg-check` script.



---

archive/issue_comments_074703.json:
```json
{
    "body": "On a 32-bit machine, I obtain the following error:\n\nsage: S = semigroupe.AutomaticSemigroup(W.semigroup_generators(), W.one(), category = FiniteCoxeterGroups())\nsage: S.cardinality()\npython(24860) malloc: *** vm_allocate(size=262144) failed (error code=3)\npython(24860) malloc: *** error: can't allocate region\npython(24860) malloc: *** set a breakpoint in szone_error to debug\nmemory allocation failed\nmemory usage :\n\nsize : 2^       used/allocated \n  0              310/312       \n  1               21/22        \n  2              109/109       \n  3               73/73        \n  4               49/50        \n  5                5/6         \n  6                9/9         \n  7                3/3         \n  8                1/1         \n  9                1/1         \n 10                1/2         \n 11                0/1         \n 12                0/0         \n 13                0/1         \n 14                1/1         \n 15            25959/25959     \n 16                0/0         \n 17                0/0         \n 18                0/0         \n 19                0/0         \n 20                0/0         \n 21                0/0         \n 22                0/0         \n 23                0/0         \n 24                0/0         \n 25                0/0         \n 26                0/0         \n 27                0/0         \n 28                0/0         \n 29                0/0         \n 30                0/0         \n 31                0/0         \n\ntotal :  850645964/850657280  4-byte units used/allocated\n.../Applications/sage-4.4/devel/sage-combinat/sage/combinat/crystals$ \n\nAnne",
    "created_at": "2010-05-12T02:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74703",
    "user": "aschilling"
}
```

On a 32-bit machine, I obtain the following error:

sage: S = semigroupe.AutomaticSemigroup(W.semigroup_generators(), W.one(), category = FiniteCoxeterGroups())
sage: S.cardinality()
python(24860) malloc: *** vm_allocate(size=262144) failed (error code=3)
python(24860) malloc: *** error: can't allocate region
python(24860) malloc: *** set a breakpoint in szone_error to debug
memory allocation failed
memory usage :

size : 2^       used/allocated 
  0              310/312       
  1               21/22        
  2              109/109       
  3               73/73        
  4               49/50        
  5                5/6         
  6                9/9         
  7                3/3         
  8                1/1         
  9                1/1         
 10                1/2         
 11                0/1         
 12                0/0         
 13                0/1         
 14                1/1         
 15            25959/25959     
 16                0/0         
 17                0/0         
 18                0/0         
 19                0/0         
 20                0/0         
 21                0/0         
 22                0/0         
 23                0/0         
 24                0/0         
 25                0/0         
 26                0/0         
 27                0/0         
 28                0/0         
 29                0/0         
 30                0/0         
 31                0/0         

total :  850645964/850657280  4-byte units used/allocated
.../Applications/sage-4.4/devel/sage-combinat/sage/combinat/crystals$ 

Anne



---

archive/issue_comments_074704.json:
```json
{
    "body": "In case this helps track down the issue: things seem to be working correctly in a 32bit virtual machine. I created a 32bit VirtualBox virtual machine, installed Ubuntu 10.04, then I installed the sage-4.4.1 binary, the gap3 spkg from #8906, and the semigroupe spkg here.",
    "created_at": "2010-05-13T16:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74704",
    "user": "saliola"
}
```

In case this helps track down the issue: things seem to be working correctly in a 32bit virtual machine. I created a 32bit VirtualBox virtual machine, installed Ubuntu 10.04, then I installed the sage-4.4.1 binary, the gap3 spkg from #8906, and the semigroupe spkg here.



---

archive/issue_comments_074705.json:
```json
{
    "body": "> I think that the two test suites (I think they are test suites...) should be run by the `spkg-check` script.\n\nThose are little self contained test programs we had written with Florent to understand how semigroupe was working. Yes, they eventually should be turned into test suites, and run from `spkg-check`.",
    "created_at": "2010-05-26T19:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74705",
    "user": "nthiery"
}
```

> I think that the two test suites (I think they are test suites...) should be run by the `spkg-check` script.

Those are little self contained test programs we had written with Florent to understand how semigroupe was working. Yes, they eventually should be turned into test suites, and run from `spkg-check`.



---

archive/issue_comments_074706.json:
```json
{
    "body": "Attachment [semigroupe-2.0-2.spkg](tarball://root/attachments/some-uuid/ticket8360/semigroupe-2.0-2.spkg) by nthiery created at 2011-03-02 11:53:17\n\nSame as previous one, working on both 32bits and 64bits, but managing the patches on the semigroupe sources in a mercurial queue",
    "created_at": "2011-03-02T11:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74706",
    "user": "nthiery"
}
```

Attachment [semigroupe-2.0-2.spkg](tarball://root/attachments/some-uuid/ticket8360/semigroupe-2.0-2.spkg) by nthiery created at 2011-03-02 11:53:17

Same as previous one, working on both 32bits and 64bits, but managing the patches on the semigroupe sources in a mercurial queue



---

archive/issue_comments_074707.json:
```json
{
    "body": "Note that semigroupe is now part of the experimental packages:\n\nhttp://www.sagemath.org/packages/experimental/\n\nOne can install it with the usual `sage -i semigroupe-2.0-2.spkg`.\n\nnext step is to make the code in sage-combinat go into sage...",
    "created_at": "2014-02-06T12:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74707",
    "user": "slabbe"
}
```

Note that semigroupe is now part of the experimental packages:

http://www.sagemath.org/packages/experimental/

One can install it with the usual `sage -i semigroupe-2.0-2.spkg`.

next step is to make the code in sage-combinat go into sage...



---

archive/issue_comments_074708.json:
```json
{
    "body": "Great, thanks S\u00e9bastien for taking care of this!\n\nThe next step is actually just to make a branch out of the patch. I am not sure about actually getting this branch into Sage until Semigroupe will be fixed one way or the other to support several semigroups simultaneously.\n\nCheers,\n                                Nicolas",
    "created_at": "2014-02-06T13:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74708",
    "user": "nthiery"
}
```

Great, thanks Sébastien for taking care of this!

The next step is actually just to make a branch out of the patch. I am not sure about actually getting this branch into Sage until Semigroupe will be fixed one way or the other to support several semigroups simultaneously.

Cheers,
                                Nicolas



---

archive/issue_comments_074709.json:
```json
{
    "body": "Replying to [comment:12 nthiery]:\n> Great, thanks S\u00e9bastien for taking care of this!\n> \n> The next step is actually just to make a branch out of the patch.\n\nyou mean a git branch?\n\nwhich patch? is it finite_semigroup-nt.patch ?\n\nI don't see how this patch uses semigroupe.\n\n> I am not sure about actually getting this branch into Sage until \n> Semigroupe will be fixed one way or the other to support several \n> semigroups simultaneously.\n\nI think I don't agree. I think the goal of the actual ticket #8360 is to make the actual semigroup into sage as it is. semigroupe was written for something no? Let's first make this available!\n\nThen I suggest to open a ticket showing with sage command line code illustrating how the bug for creating two semigroup simultaneously is obtained. The new ticket would ask for an upstream fix.\n\nS\u00e9bastien",
    "created_at": "2014-02-06T13:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74709",
    "user": "slabbe"
}
```

Replying to [comment:12 nthiery]:
> Great, thanks Sébastien for taking care of this!
> 
> The next step is actually just to make a branch out of the patch.

you mean a git branch?

which patch? is it finite_semigroup-nt.patch ?

I don't see how this patch uses semigroupe.

> I am not sure about actually getting this branch into Sage until 
> Semigroupe will be fixed one way or the other to support several 
> semigroups simultaneously.

I think I don't agree. I think the goal of the actual ticket #8360 is to make the actual semigroup into sage as it is. semigroupe was written for something no? Let's first make this available!

Then I suggest to open a ticket showing with sage command line code illustrating how the bug for creating two semigroup simultaneously is obtained. The new ticket would ask for an upstream fix.

Sébastien



---

archive/issue_comments_074710.json:
```json
{
    "body": "Replying to [comment:13 slabbe]:\n> Replying to [comment:12 nthiery]:\n> > The next step is actually just to make a branch out of the patch.\n> you mean a git branch?\n\nYup.\n\n> which patch? is it finite_semigroup-nt.patch ?\n> I don't see how this patch uses semigroupe.\n\ntrac_8360_semigroupe-interface-nt.patch\n\n> > I am not sure about actually getting this branch into Sage until \n> > Semigroupe will be fixed one way or the other to support several \n> > semigroups simultaneously.\n> I think I don't agree. I think the goal of the actual ticket #8360\n> is to make the actual semigroup into sage as it is. semigroupe was\n> written for something no? Let's first make this available!\n\nIndeed, the interface was written for something. But in practice, even\nif I spent quite some time on it, I am actually seldom using it\nbecause that misfeature is making it relatively unusable (at least in\nmy use-cases).\n\n> Then I suggest to open a ticket showing with sage command line code\n> illustrating how the bug for creating two semigroup simultaneously\n> is obtained. The new ticket would ask for an upstream fix.\n\nThat's an option. If you are convinced that:\n\n- At some point not to far in the future the bug will be fixed upstream (upstream meaning possibly us taking the time to do the fix).\n\n- The current code won't need serious interface change then.\n\nThen let's go ahead. I'd love to have this code always under my fingertips. Otherwise I am a bit reluctant to put in Sage some code that we might need to remove (because unused) or change a\nlot later on.\n\nAt the end of the day, this would actually be best handled by putting\nthe interface code in the spkg and not in the Sage library. I haven't\nchecked how hard/easy it would be to handle.\n\nCheers,\n                            Nicolas",
    "created_at": "2014-02-06T14:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74710",
    "user": "nthiery"
}
```

Replying to [comment:13 slabbe]:
> Replying to [comment:12 nthiery]:
> > The next step is actually just to make a branch out of the patch.
> you mean a git branch?

Yup.

> which patch? is it finite_semigroup-nt.patch ?
> I don't see how this patch uses semigroupe.

trac_8360_semigroupe-interface-nt.patch

> > I am not sure about actually getting this branch into Sage until 
> > Semigroupe will be fixed one way or the other to support several 
> > semigroups simultaneously.
> I think I don't agree. I think the goal of the actual ticket #8360
> is to make the actual semigroup into sage as it is. semigroupe was
> written for something no? Let's first make this available!

Indeed, the interface was written for something. But in practice, even
if I spent quite some time on it, I am actually seldom using it
because that misfeature is making it relatively unusable (at least in
my use-cases).

> Then I suggest to open a ticket showing with sage command line code
> illustrating how the bug for creating two semigroup simultaneously
> is obtained. The new ticket would ask for an upstream fix.

That's an option. If you are convinced that:

- At some point not to far in the future the bug will be fixed upstream (upstream meaning possibly us taking the time to do the fix).

- The current code won't need serious interface change then.

Then let's go ahead. I'd love to have this code always under my fingertips. Otherwise I am a bit reluctant to put in Sage some code that we might need to remove (because unused) or change a
lot later on.

At the end of the day, this would actually be best handled by putting
the interface code in the spkg and not in the Sage library. I haven't
checked how hard/easy it would be to handle.

Cheers,
                            Nicolas



---

archive/issue_comments_074711.json:
```json
{
    "body": "Attachment [trac_8360_semigroupe-interface-nt.patch](tarball://root/attachments/some-uuid/ticket8360/trac_8360_semigroupe-interface-nt.patch) by nthiery created at 2016-12-05 20:46:03",
    "created_at": "2016-12-05T20:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8360#issuecomment-74711",
    "user": "nthiery"
}
```

Attachment [trac_8360_semigroupe-interface-nt.patch](tarball://root/attachments/some-uuid/ticket8360/trac_8360_semigroupe-interface-nt.patch) by nthiery created at 2016-12-05 20:46:03
