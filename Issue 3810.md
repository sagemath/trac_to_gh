# Issue 3810: make abelian group list/iter and classgroup list/iter more modern

archive/issues_003810.json:
```json
{
    "body": "Assignee: @williamstein\n\nlist/iter on abelian groups does not agree with .list().\n\nAlso, list on classgroups returned abstract group elements -- essentially useless:\n\n\n```\nsage: x = QQ['x'].0\nsage: K.<a> = NumberField(x^4 + 23)\nsage: G = K.class_group()\nsage: G\nClass group of order 3 with structure C3 of Number Field in a with defining polynomial x^4 + 23\nsage: list(G)\n[1, c, c^2]\n```\n\n\nThis actually lists representatives in the class group.\n\nApply abelian group patch before classgroup patch.\n\nPasses relevant tests:\n\n```\n/Users/ncalexan/sage-3.0.6/sage -b >/dev/null && /Users/ncalexan/sage-3.0.6/sage -t /Users/ncalexan/sage-3.0.6/devel/sage-nca/sage/groups/abelian_gps/*\n\nreal\t0m1.610s\nuser\t0m0.958s\nsys\t0m0.623s\nsage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group.py\n\t [5.3 s]\nsage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group_element.py\n\t [3.6 s]\nsage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group_morphism.py\n\t [3.0 s]\nsage -t  devel/sage-nca/sage/groups/abelian_gps/all.py      \n\t [2.2 s]\nsage -t  devel/sage-nca/sage/groups/abelian_gps/dual_abelian_group.py\n\t [3.9 s]\nsage -t  devel/sage-nca/sage/groups/abelian_gps/dual_abelian_group_element.py\n\t [3.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 20.9 seconds\n```\n\n\nand\n\n\n```\n/Users/ncalexan/sage-3.0.6/sage -b >/dev/null && /Users/ncalexan/sage-3.0.6/sage -t /Users/ncalexan/sage-3.0.6/devel/sage-nca/sage/rings/number_field/*\n\nreal\t0m1.672s\nuser\t0m0.959s\nsys\t0m0.618s\nsage -t  devel/sage-nca/sage/rings/number_field/all.py      \n\t [2.0 s]\nsage -t  devel/sage-nca/sage/rings/number_field/class_group.py\n\t [4.9 s]\nsage -t  devel/sage-nca/sage/rings/number_field/galois_group.py\n\t [3.5 s]\nsage -t  devel/sage-nca/sage/rings/number_field/maps.py     \n\t [2.9 s]\nsage -t  devel/sage-nca/sage/rings/number_field/morphism.py \n\t [4.1 s]\nsage -t  devel/sage-nca/sage/rings/number_field/number_field.py\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n\n\t [28.9 s]\nsage -t  devel/sage-nca/sage/rings/number_field/number_field_base.pyx\n\t [3.7 s]\nsage -t  devel/sage-nca/sage/rings/number_field/number_field_element.pyx\n\t [9.0 s]\nsage -t  devel/sage-nca/sage/rings/number_field/number_field_element_quadratic.pyx\n\t [4.0 s]\nsage -t  devel/sage-nca/sage/rings/number_field/number_field_ideal.py\n\t [6.6 s]\nsage -t  devel/sage-nca/sage/rings/number_field/number_field_ideal_rel.py\n\t [3.4 s]\nsage -t  devel/sage-nca/sage/rings/number_field/order.py    \n\t [10.2 s]\nsage -t  devel/sage-nca/sage/rings/number_field/small_primes_of_degree_one.py\n\t [3.5 s]\nsage -t  devel/sage-nca/sage/rings/number_field/todo.py     \n\t [2.1 s]\nsage -t  devel/sage-nca/sage/rings/number_field/totallyreal.py\n\t [3.1 s]\nsage -t  devel/sage-nca/sage/rings/number_field/totallyreal_data.pyx\n\t [2.1 s]\nsage -t  devel/sage-nca/sage/rings/number_field/totallyreal_phc.py\n\t [2.1 s]\nsage -t  devel/sage-nca/sage/rings/number_field/totallyreal_rel.py\n\t [4.3 s]\nsage -t  devel/sage-nca/sage/rings/number_field/unit_group.py\n\t [2.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 102.5 seconds\n\nsage-test finished (all test passed) at Mon Aug 11 21:53:13\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3810\n\n",
    "created_at": "2008-08-12T04:56:23Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "make abelian group list/iter and classgroup list/iter more modern",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3810",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

list/iter on abelian groups does not agree with .list().

Also, list on classgroups returned abstract group elements -- essentially useless:


```
sage: x = QQ['x'].0
sage: K.<a> = NumberField(x^4 + 23)
sage: G = K.class_group()
sage: G
Class group of order 3 with structure C3 of Number Field in a with defining polynomial x^4 + 23
sage: list(G)
[1, c, c^2]
```


This actually lists representatives in the class group.

Apply abelian group patch before classgroup patch.

Passes relevant tests:

```
/Users/ncalexan/sage-3.0.6/sage -b >/dev/null && /Users/ncalexan/sage-3.0.6/sage -t /Users/ncalexan/sage-3.0.6/devel/sage-nca/sage/groups/abelian_gps/*

real	0m1.610s
user	0m0.958s
sys	0m0.623s
sage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group.py
	 [5.3 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group_element.py
	 [3.6 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/abelian_group_morphism.py
	 [3.0 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/all.py      
	 [2.2 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/dual_abelian_group.py
	 [3.9 s]
sage -t  devel/sage-nca/sage/groups/abelian_gps/dual_abelian_group_element.py
	 [3.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 20.9 seconds
```


and


```
/Users/ncalexan/sage-3.0.6/sage -b >/dev/null && /Users/ncalexan/sage-3.0.6/sage -t /Users/ncalexan/sage-3.0.6/devel/sage-nca/sage/rings/number_field/*

real	0m1.672s
user	0m0.959s
sys	0m0.618s
sage -t  devel/sage-nca/sage/rings/number_field/all.py      
	 [2.0 s]
sage -t  devel/sage-nca/sage/rings/number_field/class_group.py
	 [4.9 s]
sage -t  devel/sage-nca/sage/rings/number_field/galois_group.py
	 [3.5 s]
sage -t  devel/sage-nca/sage/rings/number_field/maps.py     
	 [2.9 s]
sage -t  devel/sage-nca/sage/rings/number_field/morphism.py 
	 [4.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field.py
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.

	 [28.9 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_base.pyx
	 [3.7 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_element.pyx
	 [9.0 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_element_quadratic.pyx
	 [4.0 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_ideal.py
	 [6.6 s]
sage -t  devel/sage-nca/sage/rings/number_field/number_field_ideal_rel.py
	 [3.4 s]
sage -t  devel/sage-nca/sage/rings/number_field/order.py    
	 [10.2 s]
sage -t  devel/sage-nca/sage/rings/number_field/small_primes_of_degree_one.py
	 [3.5 s]
sage -t  devel/sage-nca/sage/rings/number_field/todo.py     
	 [2.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal.py
	 [3.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal_data.pyx
	 [2.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal_phc.py
	 [2.1 s]
sage -t  devel/sage-nca/sage/rings/number_field/totallyreal_rel.py
	 [4.3 s]
sage -t  devel/sage-nca/sage/rings/number_field/unit_group.py
	 [2.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 102.5 seconds

sage-test finished (all test passed) at Mon Aug 11 21:53:13
```


Issue created by migration from https://trac.sagemath.org/ticket/3810





---

archive/issue_comments_027010.json:
```json
{
    "body": "Attachment [3810-ncalexan-class-group-list.patch](tarball://root/attachments/some-uuid/ticket3810/3810-ncalexan-class-group-list.patch) by @ncalexan created at 2008-08-12 04:57:37",
    "created_at": "2008-08-12T04:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27010",
    "user": "https://github.com/ncalexan"
}
```

Attachment [3810-ncalexan-class-group-list.patch](tarball://root/attachments/some-uuid/ticket3810/3810-ncalexan-class-group-list.patch) by @ncalexan created at 2008-08-12 04:57:37



---

archive/issue_comments_027011.json:
```json
{
    "body": "Needs work.  Your fix patch introduces a bug:\n\n```\nsage: G = AbelianGroup([2,3], names = \"ab\") sage: v = G.list()\nsage: v\n[1, b, b^2, a, a*b, a*b^2]\nsage: v[0] = \"hi nick!\"\nsage: G.list()\n['hi nick!', b, b^2, a, a*b, a*b^2]\n```\n",
    "created_at": "2008-08-13T02:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27011",
    "user": "https://github.com/williamstein"
}
```

Needs work.  Your fix patch introduces a bug:

```
sage: G = AbelianGroup([2,3], names = "ab") sage: v = G.list()
sage: v
[1, b, b^2, a, a*b, a*b^2]
sage: v[0] = "hi nick!"
sage: G.list()
['hi nick!', b, b^2, a, a*b, a*b^2]
```




---

archive/issue_comments_027012.json:
```json
{
    "body": "Attachment [3810-ncalexan-abelian-group-iter-2.patch](tarball://root/attachments/some-uuid/ticket3810/3810-ncalexan-abelian-group-iter-2.patch) by @ncalexan created at 2008-08-13 21:42:44",
    "created_at": "2008-08-13T21:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27012",
    "user": "https://github.com/ncalexan"
}
```

Attachment [3810-ncalexan-abelian-group-iter-2.patch](tarball://root/attachments/some-uuid/ticket3810/3810-ncalexan-abelian-group-iter-2.patch) by @ncalexan created at 2008-08-13 21:42:44



---

archive/issue_comments_027013.json:
```json
{
    "body": "`3810-ncalexan-abelian-group-iter-2.patch` replaces `3810-ncalexan-abelian-group-iter.patch` and addresses referee comment.",
    "created_at": "2008-08-13T21:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27013",
    "user": "https://github.com/ncalexan"
}
```

`3810-ncalexan-abelian-group-iter-2.patch` replaces `3810-ncalexan-abelian-group-iter.patch` and addresses referee comment.



---

archive/issue_comments_027014.json:
```json
{
    "body": "This is functionality which I wanted a few days ago so I am pleased to see this ticket!\n\nI applied 3810-ncalexan-abelian-group-iter-2.patch and then 3810-ncalexan-class-group-list.patch in that order.  When Sage applied the second one I was surprised that it popped up an edit window as when one does a commit.  I just closed the window.\n\nSo I don't really know what it was I tested, but it seemed to work as advertised (and without the bug William pointed out).\n\nHere's an enhancement I would like:  If I create an ideal class from some random ideal, nothing really happens, and I cannot tell which class I got without testing for equality with every class.  Am I missing something?  I actually would have been happy to have class group elements display as abstract group elements (as they would in Magma), as long as functions were provided to go from fractional ideals to abstract ideal classes and back again.",
    "created_at": "2008-08-23T17:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27014",
    "user": "https://github.com/JohnCremona"
}
```

This is functionality which I wanted a few days ago so I am pleased to see this ticket!

I applied 3810-ncalexan-abelian-group-iter-2.patch and then 3810-ncalexan-class-group-list.patch in that order.  When Sage applied the second one I was surprised that it popped up an edit window as when one does a commit.  I just closed the window.

So I don't really know what it was I tested, but it seemed to work as advertised (and without the bug William pointed out).

Here's an enhancement I would like:  If I create an ideal class from some random ideal, nothing really happens, and I cannot tell which class I got without testing for equality with every class.  Am I missing something?  I actually would have been happy to have class group elements display as abstract group elements (as they would in Magma), as long as functions were provided to go from fractional ideals to abstract ideal classes and back again.



---

archive/issue_comments_027015.json:
```json
{
    "body": "With the two patches John mentioned I get the following doctest failure:\n\n```\nsage -t -long devel/sage/sage/rings/number_field/class_group.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/class_group.py\", line 117:\n    sage: list(G)\nExpected:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\nGot:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/class_group.py\", line 119:\n    sage: G.list()\nExpected:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\nGot:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n**********************************************************************\n```\n\nThe reason that trac_3810-ncalexan-class-group-list.patch popped up a window is that it is a straight diff instead of a patch. Nick: Can you post a unified patch and delete the old ones?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T02:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27015",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the two patches John mentioned I get the following doctest failure:

```
sage -t -long devel/sage/sage/rings/number_field/class_group.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/class_group.py", line 117:
    sage: list(G)
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/class_group.py", line 119:
    sage: G.list()
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
```

The reason that trac_3810-ncalexan-class-group-list.patch popped up a window is that it is a straight diff instead of a patch. Nick: Can you post a unified patch and delete the old ones?

Cheers,

Michael



---

archive/issue_comments_027016.json:
```json
{
    "body": "Those doctest differences are insignificant in that the output is mathematically identical to what is expected.  For deterministic output we need (as well as the usual sorting):  the same ideals representing each class, and the same presentation of each ideal.  Here it's just that the second ideal in the list has a different second generator.\n\nMy understanding is that these generators come from pari.  If so, it is probably safe to replace the doctest output with the new output.  Perhaps Nick could say if that sounds right to him.",
    "created_at": "2008-08-25T09:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27016",
    "user": "https://github.com/JohnCremona"
}
```

Those doctest differences are insignificant in that the output is mathematically identical to what is expected.  For deterministic output we need (as well as the usual sorting):  the same ideals representing each class, and the same presentation of each ideal.  Here it's just that the second ideal in the list has a different second generator.

My understanding is that these generators come from pari.  If so, it is probably safe to replace the doctest output with the new output.  Perhaps Nick could say if that sounds right to him.



---

archive/issue_comments_027017.json:
```json
{
    "body": "Nick, any news on this?  It might be relevant to #4061 which I am about to post a patch for.",
    "created_at": "2008-11-30T11:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27017",
    "user": "https://github.com/JohnCremona"
}
```

Nick, any news on this?  It might be relevant to #4061 which I am about to post a patch for.



---

archive/issue_comments_027018.json:
```json
{
    "body": "I think these should be applied.  The doctest output should be updated, but I don't have the original patch queue anymore to give a non-patch.",
    "created_at": "2008-12-01T04:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27018",
    "user": "https://github.com/ncalexan"
}
```

I think these should be applied.  The doctest output should be updated, but I don't have the original patch queue anymore to give a non-patch.



---

archive/issue_comments_027019.json:
```json
{
    "body": "Just one thing is stopping me giving this the ok:\n\n```\nsage: G=AbelianGroup([])\nsage: G.list()\n[]\nsage: list(G)\n[]\nsage: G.order()\n1\n```\n\nTrivial groups do have one element!  This special case is handled ok in the class groups patch, and a similar special case is needed for abelian groups.  (It happens because mrange() delivers nothing at all for an empty list of lists, that is one valid way of defining a trivial abelian group.)\n\nWhat's bugging me is that I discovered that same issue with listing trivial groups myself a few days ago, and somewhere else in trac there's a patch which does what is needed here -- but I cannot remember which one!  So this might cause some merge problems when my patch goes in.\n\nApart from this, the second and third patches apply fine to 3.2.1 and tests pass.  *Ignore the first patch which is replaced by the third!*",
    "created_at": "2008-12-06T23:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27019",
    "user": "https://github.com/JohnCremona"
}
```

Just one thing is stopping me giving this the ok:

```
sage: G=AbelianGroup([])
sage: G.list()
[]
sage: list(G)
[]
sage: G.order()
1
```

Trivial groups do have one element!  This special case is handled ok in the class groups patch, and a similar special case is needed for abelian groups.  (It happens because mrange() delivers nothing at all for an empty list of lists, that is one valid way of defining a trivial abelian group.)

What's bugging me is that I discovered that same issue with listing trivial groups myself a few days ago, and somewhere else in trac there's a patch which does what is needed here -- but I cannot remember which one!  So this might cause some merge problems when my patch goes in.

Apart from this, the second and third patches apply fine to 3.2.1 and tests pass.  *Ignore the first patch which is replaced by the third!*



---

archive/issue_comments_027020.json:
```json
{
    "body": "NB The patch at #4061 which has just been merged into 3.2.2 contains a fix for the trivial group list problem, so this ticket should be checked against that.  I hope to get to that today.  With luck it will mean that I can remove my one misgiving about this one!",
    "created_at": "2008-12-07T10:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27020",
    "user": "https://github.com/JohnCremona"
}
```

NB The patch at #4061 which has just been merged into 3.2.2 contains a fix for the trivial group list problem, so this ticket should be checked against that.  I hope to get to that today.  With luck it will mean that I can remove my one misgiving about this one!



---

archive/issue_comments_027021.json:
```json
{
    "body": "Attachment [sage-3810-combined.patch](tarball://root/attachments/some-uuid/ticket3810/sage-3810-combined.patch) by @JohnCremona created at 2008-12-07 17:07:15\n\nReplaces all previous; apply to 3.2.1 + #4061 patches",
    "created_at": "2008-12-07T17:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27021",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-3810-combined.patch](tarball://root/attachments/some-uuid/ticket3810/sage-3810-combined.patch) by @JohnCremona created at 2008-12-07 17:07:15

Replaces all previous; apply to 3.2.1 + #4061 patches



---

archive/issue_comments_027022.json:
```json
{
    "body": "I hope I have done this right.  I took a clone of 3.2.1 and applied the (already merged) patches at #4061, which included a fix for trivial abelian group list().  I merged Nick's two patches from this ticket, adapting them accordingly and fixing the trivial group thing I mentioned above, adding a doctest.  The result became the \"combined\" patch attached here.   It looks strange when you view it because the file abelian_groups.py has two successive diffs, but I tried applying this patch to a fresh clone (+#4061) and it does end up in the right state.\n\nIf this makes sense to Michael, and works for him, I hope this will finish off this one.",
    "created_at": "2008-12-07T17:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27022",
    "user": "https://github.com/JohnCremona"
}
```

I hope I have done this right.  I took a clone of 3.2.1 and applied the (already merged) patches at #4061, which included a fix for trivial abelian group list().  I merged Nick's two patches from this ticket, adapting them accordingly and fixing the trivial group thing I mentioned above, adding a doctest.  The result became the "combined" patch attached here.   It looks strange when you view it because the file abelian_groups.py has two successive diffs, but I tried applying this patch to a fresh clone (+#4061) and it does end up in the right state.

If this makes sense to Michael, and works for him, I hope this will finish off this one.



---

archive/issue_comments_027023.json:
```json
{
    "body": "I am seeing one doctest failure with this patch applied on a 64 bit Linux box:\n\n```\nsage -t -long \"devel/sage/sage/rings/number_field/class_group.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py\", line 148, in __main__.example_8\nFailed example:\n    list(G)###line 117:_sage_    >>> list(G)\nExpected:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\nGot:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py\", line 150, in __main__.example_8\nFailed example:\n    G.list()###line 119:_sage_    >>> G.list()\nExpected:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\nGot:\n    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n**********************************************************************\n```\n",
    "created_at": "2008-12-08T04:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27023",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am seeing one doctest failure with this patch applied on a 64 bit Linux box:

```
sage -t -long "devel/sage/sage/rings/number_field/class_group.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 148, in __main__.example_8
Failed example:
    list(G)###line 117:_sage_    >>> list(G)
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 150, in __main__.example_8
Failed example:
    G.list()###line 119:_sage_    >>> G.list()
Expected:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
Got:
    [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
**********************************************************************
```




---

archive/issue_comments_027024.json:
```json
{
    "body": "Replying to [comment:13 mabshoff]:\n> I am seeing one doctest failure with this patch applied on a 64 bit Linux box:\n> {{{\n> sage -t -long \"devel/sage/sage/rings/number_field/class_group.py\"\n> **********************************************************************\n> File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py\", line 148, in __main__.example_8\n> Failed example:\n>     list(G)###line 117:_sage_    >>> list(G)\n> Expected:\n>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n> Got:\n>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n> **********************************************************************\n> File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py\", line 150, in __main__.example_8\n> Failed example:\n>     G.list()###line 119:_sage_    >>> G.list()\n> Expected:\n>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n> Got:\n>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]\n> **********************************************************************\n> }}}\n\nWhat a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.\n\nWould it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?",
    "created_at": "2008-12-08T09:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27024",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:13 mabshoff]:
> I am seeing one doctest failure with this patch applied on a 64 bit Linux box:
> {{{
> sage -t -long "devel/sage/sage/rings/number_field/class_group.py"
> **********************************************************************
> File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 148, in __main__.example_8
> Failed example:
>     list(G)###line 117:_sage_    >>> list(G)
> Expected:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> Got:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> **********************************************************************
> File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/class_group.py", line 150, in __main__.example_8
> Failed example:
>     G.list()###line 119:_sage_    >>> G.list()
> Expected:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 + a - 1/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> Got:
>     [Trivial principal fractional ideal class, Fractional ideal class (2, 1/2*a^2 - a + 3/2), Fractional ideal class (2, 1/2*a^2 + 1/2)]
> **********************************************************************
> }}}

What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.

Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?



---

archive/issue_comments_027025.json:
```json
{
    "body": "Replying to [comment:14 cremona]:\n\nHi John,\n\n> What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.\n\nYes, Nick said the same thing in IRC, but I was asleep at that point.\n \n> Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?\n\nI am fine marking those two doctests with #32 bit and #64 bit output and to get the patch in. If anybody wants to have a \"prettier\" doctest that can be addressed via a followup patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-08T09:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:14 cremona]:

Hi John,

> What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.

Yes, Nick said the same thing in IRC, but I was asleep at that point.
 
> Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?

I am fine marking those two doctests with #32 bit and #64 bit output and to get the patch in. If anybody wants to have a "prettier" doctest that can be addressed via a followup patch.

Cheers,

Michael



---

archive/issue_comments_027026.json:
```json
{
    "body": "Replying to [comment:15 mabshoff]:\n> Replying to [comment:14 cremona]:\n> \n> Hi John,\n> \n> > What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.\n> \n> Yes, Nick said the same thing in IRC, but I was asleep at that point.\n>  \n> > Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?\n> \n> I am fine marking those two doctests with #32 bit and #64 bit output and to get the patch in. If anybody wants to have a \"prettier\" doctest that can be addressed via a followup patch.\n\nSounds good to me.  If it is more random than that it will be picked up by the merry horde of alpha testers....\n\nJohn\n\n> \n> Cheers,\n> \n> Michael\n>",
    "created_at": "2008-12-08T09:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27026",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:15 mabshoff]:
> Replying to [comment:14 cremona]:
> 
> Hi John,
> 
> > What a nuisance;  sorry, I only did a 32-bit test at the weekend.   The got/expected are equally valid mathematically, and my guess is that the difference comes from the pari library.
> 
> Yes, Nick said the same thing in IRC, but I was asleep at that point.
>  
> > Would it be dishonest to look for an example for the doctest where the output was identical on 32- and 64-bit machines?
> 
> I am fine marking those two doctests with #32 bit and #64 bit output and to get the patch in. If anybody wants to have a "prettier" doctest that can be addressed via a followup patch.

Sounds good to me.  If it is more random than that it will be picked up by the merry horde of alpha testers....

John

> 
> Cheers,
> 
> Michael
>



---

archive/issue_comments_027027.json:
```json
{
    "body": "Attachment [sage-3810-fix64.patch](tarball://root/attachments/some-uuid/ticket3810/sage-3810-fix64.patch) by @JohnCremona created at 2008-12-08 10:07:42",
    "created_at": "2008-12-08T10:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27027",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-3810-fix64.patch](tarball://root/attachments/some-uuid/ticket3810/sage-3810-fix64.patch) by @JohnCremona created at 2008-12-08 10:07:42



---

archive/issue_comments_027028.json:
```json
{
    "body": "New patch fixes the 32/64 problem, has been tested on both.",
    "created_at": "2008-12-08T10:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27028",
    "user": "https://github.com/JohnCremona"
}
```

New patch fixes the 32/64 problem, has been tested on both.



---

archive/issue_comments_027029.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-08T10:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27029",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027030.json:
```json
{
    "body": "Merged sage-3810-combined.patch and sage-3810-fix64.patch in Sage 3.2.2.alpha1",
    "created_at": "2008-12-08T10:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3810#issuecomment-27030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage-3810-combined.patch and sage-3810-fix64.patch in Sage 3.2.2.alpha1
