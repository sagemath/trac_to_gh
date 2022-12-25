# Issue 9925: Doctest error in sage/schemes/generic/toric_divisor.py on OS X

archive/issues_009925.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @novoselt @vbraun mhampton\n\nI get this reproducible doctest error with a trial 4.6.alpha1 (32-bit build) on bsd.math (OS X 10.6):\n\n```python\nsage -t -long \"devel/sage/sage/schemes/generic/toric_divisor.py\"\n**********************************************************************\nFile \"/Users/mpatel/tmp/bb/slave/bsd_scratch/build/sage-4.6.alpha1/devel/sage/sage/schemes/generic/toric_divisor.py\", line 1522:\n    sage: supp.Vrepresentation()\nExpected:\n    [A vertex at (-1, 1), A vertex at (0, 2), A vertex at (0, -1), A vertex at (3, -1)]\nGot:\n    [A vertex at (-1, 1), A vertex at (0, 2), A vertex at (3, -1), A vertex at (0, -1)]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9926\n\n",
    "created_at": "2010-09-17T00:46:23Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Doctest error in sage/schemes/generic/toric_divisor.py on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9925",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @novoselt @vbraun mhampton

I get this reproducible doctest error with a trial 4.6.alpha1 (32-bit build) on bsd.math (OS X 10.6):

```python
sage -t -long "devel/sage/sage/schemes/generic/toric_divisor.py"
**********************************************************************
File "/Users/mpatel/tmp/bb/slave/bsd_scratch/build/sage-4.6.alpha1/devel/sage/sage/schemes/generic/toric_divisor.py", line 1522:
    sage: supp.Vrepresentation()
Expected:
    [A vertex at (-1, 1), A vertex at (0, 2), A vertex at (0, -1), A vertex at (3, -1)]
Got:
    [A vertex at (-1, 1), A vertex at (0, 2), A vertex at (3, -1), A vertex at (0, -1)]
```

Issue created by migration from https://trac.sagemath.org/ticket/9926





---

archive/issue_comments_098665.json:
```json
{
    "body": "If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000.",
    "created_at": "2010-09-17T00:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98665",
    "user": "https://github.com/qed777"
}
```

If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000.



---

archive/issue_comments_098666.json:
```json
{
    "body": "By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.",
    "created_at": "2010-09-17T00:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98666",
    "user": "https://github.com/qed777"
}
```

By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.



---

archive/issue_comments_098667.json:
```json
{
    "body": "Volker, what's the correct way to sort vertices? And what does their order in `Vrepresentation` depend on?",
    "created_at": "2010-09-17T04:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98667",
    "user": "https://github.com/novoselt"
}
```

Volker, what's the correct way to sort vertices? And what does their order in `Vrepresentation` depend on?



---

archive/issue_comments_098668.json:
```json
{
    "body": "The output order should be deterministic: `_sheaf_cohomology_support()` does nothing that could randomize the order of `chamber_vertices` and `Polyhedron` takes the ordering of the vertices to be whatever `cddlib` returns. I don't have access to an OSX machine nor an account on bsd.math, so someone else will have to debug this.",
    "created_at": "2010-09-17T11:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98668",
    "user": "https://github.com/vbraun"
}
```

The output order should be deterministic: `_sheaf_cohomology_support()` does nothing that could randomize the order of `chamber_vertices` and `Polyhedron` takes the ordering of the vertices to be whatever `cddlib` returns. I don't have access to an OSX machine nor an account on bsd.math, so someone else will have to debug this.



---

archive/issue_comments_098669.json:
```json
{
    "body": "Marshall, is there any chance you can settle this, since I don't understand the guts of Polyhedron? Does cddlib have any specific ordering of vertices? (IMHO, taking convex hull should delete extra points and otherwise leave the order the same.) Even if cddlib does not care about any particular order I find it strange that it can depend on architecture...\n\nOf course, an easy fix to this is to put \"#random output\" comment in the doctest, but it does not feel satisfactory in this case.",
    "created_at": "2010-09-17T14:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98669",
    "user": "https://github.com/novoselt"
}
```

Marshall, is there any chance you can settle this, since I don't understand the guts of Polyhedron? Does cddlib have any specific ordering of vertices? (IMHO, taking convex hull should delete extra points and otherwise leave the order the same.) Even if cddlib does not care about any particular order I find it strange that it can depend on architecture...

Of course, an easy fix to this is to put "#random output" comment in the doctest, but it does not feel satisfactory in this case.



---

archive/issue_comments_098670.json:
```json
{
    "body": "I'll try to check this out but I don't have much time today, it might take me a few.",
    "created_at": "2010-09-17T15:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I'll try to check this out but I don't have much time today, it might take me a few.



---

archive/issue_comments_098671.json:
```json
{
    "body": "This is not as pleasant, but what about something like:\n\n```\nsage: all([v in supp.vertices() for v in [[-1, 1], [0, 2], [3, -1], [0, -1]]])\nTrue\n```",
    "created_at": "2010-09-20T05:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98671",
    "user": "https://github.com/jhpalmieri"
}
```

This is not as pleasant, but what about something like:

```
sage: all([v in supp.vertices() for v in [[-1, 1], [0, 2], [3, -1], [0, -1]]])
True
```



---

archive/issue_comments_098672.json:
```json
{
    "body": "That would work, although as an example it seems harder to understand.  I think I would prefer:\n\n```\nsage: vertices = supp.vertices()\nsage: vertices.sort()\nsage: vertices\n[[-1, 1], [0, -1], [0, 2], [3, -1]]\n```\n\nat least as a temporary workaround.  It would be nice if the Polyhedron class produced a specific output, but that will require some significant additions that I won't have time for before this release.",
    "created_at": "2010-09-20T13:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98672",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

That would work, although as an example it seems harder to understand.  I think I would prefer:

```
sage: vertices = supp.vertices()
sage: vertices.sort()
sage: vertices
[[-1, 1], [0, -1], [0, 2], [3, -1]]
```

at least as a temporary workaround.  It would be nice if the Polyhedron class produced a specific output, but that will require some significant additions that I won't have time for before this release.



---

archive/issue_comments_098673.json:
```json
{
    "body": "I think the problem is that `cddlib` uses `rand()` to sometimes make random initial choices while searching for generating sets. Although `cddlib` fixes the seed, there is no guarantee that different platforms implement `rand()` in the same way.\n\nTo make sure this is indeed the problem, can you run\n\n```\nsage: Polyhedron(vertices=[(0, 1), (1, 1), (0, 1), (-1, 1), (0, 2), (0, -1), (0, 0), (0, 0), (3, -1), (0, 2), (0, -1), (1, -1), (0, 0)], verbose=True)\nV-representation\nbegin\n 13 3 rational\n 1 0 1\n 1 1 1\n 1 0 1\n 1 -1 1\n 1 0 2\n 1 0 -1\n 1 0 0\n 1 0 0\n 1 3 -1\n 1 0 2\n 1 0 -1\n 1 1 -1\n 1 0 0\nend\n\nV-representation\nbegin\n 4 3 rational\n 1 -1 1\n 1 0 2\n 1 0 -1\n 1 3 -1\nend\n\nH-representation\nbegin\n 4 3 rational\n 2 1 -1\n 1 2 1\n 1 0 1\n 2 -1 -1\nend\nA 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices.\n```\non the OSX machine and paste the output? I can then rip out the `rand()` from the `cddlib.spkg`...",
    "created_at": "2010-09-20T16:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98673",
    "user": "https://github.com/vbraun"
}
```

I think the problem is that `cddlib` uses `rand()` to sometimes make random initial choices while searching for generating sets. Although `cddlib` fixes the seed, there is no guarantee that different platforms implement `rand()` in the same way.

To make sure this is indeed the problem, can you run

```
sage: Polyhedron(vertices=[(0, 1), (1, 1), (0, 1), (-1, 1), (0, 2), (0, -1), (0, 0), (0, 0), (3, -1), (0, 2), (0, -1), (1, -1), (0, 0)], verbose=True)
V-representation
begin
 13 3 rational
 1 0 1
 1 1 1
 1 0 1
 1 -1 1
 1 0 2
 1 0 -1
 1 0 0
 1 0 0
 1 3 -1
 1 0 2
 1 0 -1
 1 1 -1
 1 0 0
end

V-representation
begin
 4 3 rational
 1 -1 1
 1 0 2
 1 0 -1
 1 3 -1
end

H-representation
begin
 4 3 rational
 2 1 -1
 1 2 1
 1 0 1
 2 -1 -1
end
A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices.
```
on the OSX machine and paste the output? I can then rip out the `rand()` from the `cddlib.spkg`...



---

archive/issue_comments_098674.json:
```json
{
    "body": "Changing assignee from mvngu to mhampton.",
    "created_at": "2010-09-20T19:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from mvngu to mhampton.



---

archive/issue_comments_098675.json:
```json
{
    "body": "I'm confused by \"rip out the rand() from the cddlib.spkg\" - are you going to patch the source code?\n\nAnyway on OS X 10.6 I get:\n\n```\nV-representation\nbegin\n 13 3 rational\n 1 0 1\n 1 1 1\n 1 0 1\n 1 -1 1\n 1 0 2\n 1 0 -1\n 1 0 0\n 1 0 0\n 1 3 -1\n 1 0 2\n 1 0 -1\n 1 1 -1\n 1 0 0\nend\n\n\nV-representation\nbegin\n 4 3 rational\n 1 -1 1\n 1 0 2\n 1 3 -1\n 1 0 -1\nend\n\nH-representation\nbegin\n 4 3 rational\n 2 1 -1\n 1 2 1\n 1 0 1\n 2 -1 -1\nend\n\nVertex graph\nbegin\n  4    4\n 1 2 : 2 4 \n 2 2 : 1 3 \n 3 2 : 2 4 \n 4 2 : 1 3 \nend\n\nFacet graph\nbegin\n  4    4\n 1 2 : 2 4 \n 2 2 : 1 3 \n 3 2 : 2 4 \n 4 \n```",
    "created_at": "2010-09-20T19:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98675",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I'm confused by "rip out the rand() from the cddlib.spkg" - are you going to patch the source code?

Anyway on OS X 10.6 I get:

```
V-representation
begin
 13 3 rational
 1 0 1
 1 1 1
 1 0 1
 1 -1 1
 1 0 2
 1 0 -1
 1 0 0
 1 0 0
 1 3 -1
 1 0 2
 1 0 -1
 1 1 -1
 1 0 0
end


V-representation
begin
 4 3 rational
 1 -1 1
 1 0 2
 1 3 -1
 1 0 -1
end

H-representation
begin
 4 3 rational
 2 1 -1
 1 2 1
 1 0 1
 2 -1 -1
end

Vertex graph
begin
  4    4
 1 2 : 2 4 
 2 2 : 1 3 
 3 2 : 2 4 
 4 2 : 1 3 
end

Facet graph
begin
  4    4
 1 2 : 2 4 
 2 2 : 1 3 
 3 2 : 2 4 
 4 
```



---

archive/issue_comments_098676.json:
```json
{
    "body": "Changing assignee from mhampton to mvngu.",
    "created_at": "2010-09-20T19:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98676",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from mhampton to mvngu.



---

archive/issue_comments_098677.json:
```json
{
    "body": "Yes, thats what I'm planning to do: patch the `cddlib` source code to use a portable random number generator. I already have an updated spkg for #9798, so I'll patch this issue at the same time if you don't object.",
    "created_at": "2010-09-20T20:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98677",
    "user": "https://github.com/vbraun"
}
```

Yes, thats what I'm planning to do: patch the `cddlib` source code to use a portable random number generator. I already have an updated spkg for #9798, so I'll patch this issue at the same time if you don't object.



---

archive/issue_comments_098678.json:
```json
{
    "body": "same failure on PPC MacOSX 10.5, just in case...\nDima",
    "created_at": "2010-09-21T04:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98678",
    "user": "https://github.com/dimpase"
}
```

same failure on PPC MacOSX 10.5, just in case...
Dima



---

archive/issue_comments_098679.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-09-21T13:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98679",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_098680.json:
```json
{
    "body": "Updated spkg is at #9798, please test on your OSX machines. Note: also needs patch to the sage library which you can find on the same ticket.",
    "created_at": "2010-09-21T13:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98680",
    "user": "https://github.com/vbraun"
}
```

Updated spkg is at #9798, please test on your OSX machines. Note: also needs patch to the sage library which you can find on the same ticket.



---

archive/issue_comments_098681.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-09-21T15:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98681",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_098682.json:
```json
{
    "body": "Replying to [comment:14 vbraun]:\n> Updated spkg is at #9798, please test on your OSX machines. Note: also needs patch to the sage library which you can find on the same ticket.\n> \n\n\nI just did, please see the other ticket...\nDima",
    "created_at": "2010-09-21T15:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98682",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:14 vbraun]:
> Updated spkg is at #9798, please test on your OSX machines. Note: also needs patch to the sage library which you can find on the same ticket.
> 


I just did, please see the other ticket...
Dima



---

archive/issue_comments_098683.json:
```json
{
    "body": "Replying to [comment:12 vbraun]:\n> Yes, thats what I'm planning to do: patch the `cddlib` source code to use a portable random number generator. I already have an updated spkg for #9798, so I'll patch this issue at the same time if you don't object.\n> \n\n\nI'm curious; are you planning on using Sage's framework for interfacing to random number generators?  See sage/devel/sage/sage/misc/randstate.pyx, and examples for setting the random seed in gap, pari, the libc generator, etc., or see http://sagemath.org/doc/reference/sage/misc/randstate.html#generating-random-numbers-in-library-code",
    "created_at": "2010-10-11T17:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98683",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:12 vbraun]:
> Yes, thats what I'm planning to do: patch the `cddlib` source code to use a portable random number generator. I already have an updated spkg for #9798, so I'll patch this issue at the same time if you don't object.
> 


I'm curious; are you planning on using Sage's framework for interfacing to random number generators?  See sage/devel/sage/sage/misc/randstate.pyx, and examples for setting the random seed in gap, pari, the libc generator, etc., or see http://sagemath.org/doc/reference/sage/misc/randstate.html#generating-random-numbers-in-library-code



---

archive/issue_comments_098684.json:
```json
{
    "body": "My plan is described in #10039. So I'm not interested in adding more to cddlib than what we absolutely have to.",
    "created_at": "2010-10-11T19:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98684",
    "user": "https://github.com/vbraun"
}
```

My plan is described in #10039. So I'm not interested in adding more to cddlib than what we absolutely have to.



---

archive/issue_comments_098685.json:
```json
{
    "body": "Update: I also get the problem in the description with a *64-bit* build of 4.6.alpha3 on bsd.math (OS X 10.6).",
    "created_at": "2010-10-17T03:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98685",
    "user": "https://github.com/qed777"
}
```

Update: I also get the problem in the description with a *64-bit* build of 4.6.alpha3 on bsd.math (OS X 10.6).



---

archive/issue_comments_098686.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-18T10:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98686",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098687.json:
```json
{
    "body": "I've fixed the bug in #9798. That ticket will fix the issue in this ticket, too.",
    "created_at": "2010-10-18T10:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98687",
    "user": "https://github.com/vbraun"
}
```

I've fixed the bug in #9798. That ticket will fix the issue in this ticket, too.



---

archive/issue_comments_098688.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-18T14:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98688",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098689.json:
```json
{
    "body": "Replying to [comment:19 vbraun]:\n> I've fixed the bug in #9798. That ticket will fix the issue in this ticket, too.\n\n\ntested on Debian x64 and on MacOSX 10.5 PPC. Positive!",
    "created_at": "2010-10-18T14:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98689",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:19 vbraun]:
> I've fixed the bug in #9798. That ticket will fix the issue in this ticket, too.


tested on Debian x64 and on MacOSX 10.5 PPC. Positive!



---

archive/issue_events_025028.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-21T08:39:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9925#event-25028"
}
```



---

archive/issue_comments_098690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-21T08:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9925",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9925#issuecomment-98690",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
