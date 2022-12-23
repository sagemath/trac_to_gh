# Issue 3959: [with patch bundle] General group algebras class

archive/issues_003959.json:
```json
{
    "body": "Assignee: tbd\n\nI've attempted to write a generic class for group algebras R[G] where R is any commutative ring and G is any group; it derives from the existing Algebra class, and most of the work is done by the existing FormalSums class.\n\nIn the process I've uncovered a bizarre coercion wrinkle: if we try and make elements of R and elements of G coerce into R[G] automatically, it breaks, because (for example) 2 might coerce into G (e.g. if G = GL(n, ZZ)) and the compositions of the obvious maps ZZ -> G -> R[G] and ZZ -> R -> R[G] aren't the same! [*]\n\nI've got around this by not adding automatic coercion from G to R[G], but I'm not sure if this is the right thing. In fact I'd very much appreciate any input on whether or not I've understood Sage's coercion framework and other \"house rules\" generally, as this is my first attempt to contribute anything where that's relevant.\n\nNote: this is rather orthogonal to David Joyner's PermutationGroupRing class deriving from CombinatorialAlgebra -- what I'm trying to do is much more general but has almost no methods, and PermutationGroupRing might work well as a subclass of my general GroupAlgebra.\n\n([*] I seem to recall mentioning this as a theoretical example in a discussion at Sage Days 6, but I can't remember what came of it at the time.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3959\n\n",
    "created_at": "2008-08-26T17:48:49Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch bundle] General group algebras class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3959",
    "user": "davidloeffler"
}
```
Assignee: tbd

I've attempted to write a generic class for group algebras R[G] where R is any commutative ring and G is any group; it derives from the existing Algebra class, and most of the work is done by the existing FormalSums class.

In the process I've uncovered a bizarre coercion wrinkle: if we try and make elements of R and elements of G coerce into R[G] automatically, it breaks, because (for example) 2 might coerce into G (e.g. if G = GL(n, ZZ)) and the compositions of the obvious maps ZZ -> G -> R[G] and ZZ -> R -> R[G] aren't the same! [*]

I've got around this by not adding automatic coercion from G to R[G], but I'm not sure if this is the right thing. In fact I'd very much appreciate any input on whether or not I've understood Sage's coercion framework and other "house rules" generally, as this is my first attempt to contribute anything where that's relevant.

Note: this is rather orthogonal to David Joyner's PermutationGroupRing class deriving from CombinatorialAlgebra -- what I'm trying to do is much more general but has almost no methods, and PermutationGroupRing might work well as a subclass of my general GroupAlgebra.

([*] I seem to recall mentioning this as a theoretical example in a discussion at Sage Days 6, but I can't remember what came of it at the time.)

Issue created by migration from https://trac.sagemath.org/ticket/3959





---

archive/issue_comments_028432.json:
```json
{
    "body": "hg bundle (includes several small changesets) - against Sage 3.1.1",
    "created_at": "2008-08-26T17:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28432",
    "user": "davidloeffler"
}
```

hg bundle (includes several small changesets) - against Sage 3.1.1



---

archive/issue_comments_028433.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-26T17:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28433",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028434.json:
```json
{
    "body": "Attachment\n\n(The above hg changeset bundle works fine for me but the trac browser doesn't seem to like it -- not sure what's going on there.)",
    "created_at": "2008-08-26T17:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28434",
    "user": "davidloeffler"
}
```

Attachment

(The above hg changeset bundle works fine for me but the trac browser doesn't seem to like it -- not sure what's going on there.)



---

archive/issue_comments_028435.json:
```json
{
    "body": "Changing assignee from tbd to davidloeffler.",
    "created_at": "2008-08-26T17:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28435",
    "user": "davidloeffler"
}
```

Changing assignee from tbd to davidloeffler.



---

archive/issue_comments_028436.json:
```json
{
    "body": "This looks very interesting but I can't get it to pull/apply/import_patch etc. Can you please use the commit/log/export commands to create a regular patch (see http://www.sagemath.org/doc/prog/node72.html for details)?\n\nAlso, if R is a ring and G is a group then R[G] is a group ring and (in general) not an algebra. (An algebra, stripped of its multiplicative structure, is a vector space over a field. In general, a group ring such as R[G] does not have this property.)",
    "created_at": "2008-08-26T22:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28436",
    "user": "wdj"
}
```

This looks very interesting but I can't get it to pull/apply/import_patch etc. Can you please use the commit/log/export commands to create a regular patch (see http://www.sagemath.org/doc/prog/node72.html for details)?

Also, if R is a ring and G is a group then R[G] is a group ring and (in general) not an algebra. (An algebra, stripped of its multiplicative structure, is a vector space over a field. In general, a group ring such as R[G] does not have this property.)



---

archive/issue_comments_028437.json:
```json
{
    "body": "Attachment\n\nOK, here's a single patch. \n\nAs for the naming convention: I thought an algebra over a ring R was any ring S with a fixed homomorphism R->S. This is what Sage's generic Algebra class does -- it doesn't require that its base_ring is a field. My class derives from that. Compare the existing FreeAlgebra class, which also derives from Algebra and also can be defined over any ring (one of the FreeAlgebra doctest examples is over ZZ).",
    "created_at": "2008-08-27T14:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28437",
    "user": "davidloeffler"
}
```

Attachment

OK, here's a single patch. 

As for the naming convention: I thought an algebra over a ring R was any ring S with a fixed homomorphism R->S. This is what Sage's generic Algebra class does -- it doesn't require that its base_ring is a field. My class derives from that. Compare the existing FreeAlgebra class, which also derives from Algebra and also can be defined over any ring (one of the FreeAlgebra doctest examples is over ZZ).



---

archive/issue_comments_028438.json:
```json
{
    "body": "This applies cleanly to sage 3.1.1 and passes sage -testall. I read over the diff file and played with some of the functionality. I think this is a really good basic patch and should be applied. There are lots of additions I'd like. For example, there are special methods if R[G] is finite or if R is a field, so special classes could be written for these. However, this is a great start.\n\nAbout the terminology (group algebra vs group ring), I have no serious objection and it is fine with me if it stays as is.",
    "created_at": "2008-08-27T22:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28438",
    "user": "wdj"
}
```

This applies cleanly to sage 3.1.1 and passes sage -testall. I read over the diff file and played with some of the functionality. I think this is a really good basic patch and should be applied. There are lots of additions I'd like. For example, there are special methods if R[G] is finite or if R is a field, so special classes could be written for these. However, this is a great start.

About the terminology (group algebra vs group ring), I have no serious objection and it is fine with me if it stays as is.



---

archive/issue_comments_028439.json:
```json
{
    "body": "By the way: I am not ignoring this patch, but Mike Hansen has a couple fixes for this patch that he is working on and will be done hopefully this weekend.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-19T16:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28439",
    "user": "mabshoff"
}
```

By the way: I am not ignoring this patch, but Mike Hansen has a couple fixes for this patch that he is working on and will be done hopefully this weekend.

Cheers,

Michael



---

archive/issue_comments_028440.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T15:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28440",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028441.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0. \n\nMike: Feel free to submit a patch on top of this one.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T15:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3959#issuecomment-28441",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha0. 

Mike: Feel free to submit a patch on top of this one.

Cheers,

Michael
