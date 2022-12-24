# Issue 2367: [with patch, needs review] Extend invariant_generators to the case of Matrix Groups over number fields

archive/issues_002367.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @wdjoyner\n\nKeywords: invariant ring, matrix group\n\nThis ticket is strongly related with ticket #2348. I fix here a doc test failure that is introduced by the patch from #2348, and the new functionality that i introduce here relies on the patch from #2348.\n\nProblem: Let G be a finite matrix group. So far, G.invariant_generators() worked only if G was defined over the rationals or over GF(prime). \nSolution: Singular also provides simple algebraic extensions over these fields, so, it just requires a more careful definition of a singular ring inside the function.\n\nAfter first applying the patch from #2348 and then applying the new patch, the doc tests of matrix_group.py should pass, and the following should work:\n\n```\nsage: F=CyclotomicField(8)\nsage: z=F.gen()\nsage: a=z+1/z\nsage: b=z^2\nsage: MS=MatrixSpace(F,2,2)\nsage: g1=MS([[1/a,1/a],[1/a,-1/a]])\nsage: g2=MS([[1,0],[0,b]])\nsage: g3=MS([[b,0],[0,1]])\nsage: G=MatrixGroup([g1,g2,g3])\nsage: G.invariant_generators()\n[x1^8 + 14*x1^4*x2^4 + x2^8,\n x1^24 + 10626/1025*x1^20*x2^4 + 735471/1025*x1^16*x2^8 + 2704156/1025*x1^12*x2^12 + 735471/1025*x1^8*x2^16 + 10626/1025*x1^4*x2^20 + x2^24]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2367\n\n",
    "created_at": "2008-03-02T14:06:04Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, needs review] Extend invariant_generators to the case of Matrix Groups over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2367",
    "user": "@simon-king-jena"
}
```
Assignee: joyner

CC:  @wdjoyner

Keywords: invariant ring, matrix group

This ticket is strongly related with ticket #2348. I fix here a doc test failure that is introduced by the patch from #2348, and the new functionality that i introduce here relies on the patch from #2348.

Problem: Let G be a finite matrix group. So far, G.invariant_generators() worked only if G was defined over the rationals or over GF(prime). 
Solution: Singular also provides simple algebraic extensions over these fields, so, it just requires a more careful definition of a singular ring inside the function.

After first applying the patch from #2348 and then applying the new patch, the doc tests of matrix_group.py should pass, and the following should work:

```
sage: F=CyclotomicField(8)
sage: z=F.gen()
sage: a=z+1/z
sage: b=z^2
sage: MS=MatrixSpace(F,2,2)
sage: g1=MS([[1/a,1/a],[1/a,-1/a]])
sage: g2=MS([[1,0],[0,b]])
sage: g3=MS([[b,0],[0,1]])
sage: G=MatrixGroup([g1,g2,g3])
sage: G.invariant_generators()
[x1^8 + 14*x1^4*x2^4 + x2^8,
 x1^24 + 10626/1025*x1^20*x2^4 + 735471/1025*x1^16*x2^8 + 2704156/1025*x1^12*x2^12 + 735471/1025*x1^8*x2^16 + 10626/1025*x1^4*x2^20 + x2^24]
```



Issue created by migration from https://trac.sagemath.org/ticket/2367





---

archive/issue_comments_015967.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-02T14:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15967",
    "user": "@simon-king-jena"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_015968.json:
```json
{
    "body": "The patches (first 2348 then this one) applied cleanly and the above code ran. However, sage -testall failed. Here is one failure:\n\n\n```\nwdj@wooster:~/wdj/sagefiles/sage-2.10.3.rc0$ ./sage -t \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py\"\nsage -t  devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py**********************************************************************\nFile \"matrix_group_element.py\", line 122:\n    sage: g._gap_init_()\nExpected:\n    '[[Z(7)^0,0*Z(7)],[0*Z(7),Z(7)^2]]'\nGot:\n    '[[Z(7)^0,0*Z(7)],[0*Z(7),Z(7)^2]]*One(GF(7))'\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_4\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_matrix_group_element.py\n         [5.2 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py\nTotal time for all tests: 5.2 seconds\n```\n\n\nThis would be easy to fix of course but, for the failure I cannot recommend\nacceptance at this time.\n\nThere were other failures,\n\n\n```\n        sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py\n        sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py\n        sage -t  devel/sage-matgp3/sage/plot/plot.py\n```\n\nbut they may be unrelated since they were already reported by Jaap Spies\non sage-devel for a clean install.",
    "created_at": "2008-03-02T16:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15968",
    "user": "@wdjoyner"
}
```

The patches (first 2348 then this one) applied cleanly and the above code ran. However, sage -testall failed. Here is one failure:


```
wdj@wooster:~/wdj/sagefiles/sage-2.10.3.rc0$ ./sage -t "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py"
sage -t  devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py**********************************************************************
File "matrix_group_element.py", line 122:
    sage: g._gap_init_()
Expected:
    '[[Z(7)^0,0*Z(7)],[0*Z(7),Z(7)^2]]'
Got:
    '[[Z(7)^0,0*Z(7)],[0*Z(7),Z(7)^2]]*One(GF(7))'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_matrix_group_element.py
         [5.2 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-matgp3/sage/groups/matrix_gps/matrix_group_element.py
Total time for all tests: 5.2 seconds
```


This would be easy to fix of course but, for the failure I cannot recommend
acceptance at this time.

There were other failures,


```
        sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py
        sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py
        sage -t  devel/sage-matgp3/sage/plot/plot.py
```

but they may be unrelated since they were already reported by Jaap Spies
on sage-devel for a clean install.



---

archive/issue_comments_015969.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> The patches (first 2348 then this one) applied cleanly and the above code ran. However, sage -testall failed. Here is one failure: ...\n\nClearly the doctest failure in matrix_group_element.py has a trivial fix: The doctest expects output that is incorrect as soon as one switches to an algebraic extension of the rationals:\n\n> Expected:\n>     `'[[Z(7)<sup>0,0*Z(7)],[0*Z(7),Z(7)</sup>2]]'`\n> Got:\n>     `'[[Z(7)<sup>0,0*Z(7)],[0*Z(7),Z(7)</sup>2]]*One(GF(7))'`\n\nIn gap:\n\n```\ngap> x:=Indeterminate(Rationals,\"x\");;\ngap> p:=x^4+3*x^2+1;;\ngap> e:=AlgebraicExtension(Rationals,p);\n<algebraic extension over the Rationals of degree 4>\ngap> M:=[[1,GeneratorsOfField(e)[1]^2]];\n[ [ 1, (a^2) ] ]\ngap> IsMatrix(M);\nfalse\ngap> IsMatrix(M*One(e));\ntrue\n```\n\nHence, in general the modified output is needed.\n\n> There were other failures,\n> \n> {{{\n>         sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py\n>         sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py\n>         sage -t  devel/sage-matgp3/sage/plot/plot.py\n> }}}\n> but they may be unrelated since they were already reported by Jaap Spies\n> on sage-devel for a clean install.\n\nI think so, too. I am about to provide new patches for this ticket and for #2348.",
    "created_at": "2008-03-02T16:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15969",
    "user": "@simon-king-jena"
}
```

Replying to [comment:2 wdj]:
> The patches (first 2348 then this one) applied cleanly and the above code ran. However, sage -testall failed. Here is one failure: ...

Clearly the doctest failure in matrix_group_element.py has a trivial fix: The doctest expects output that is incorrect as soon as one switches to an algebraic extension of the rationals:

> Expected:
>     `'[[Z(7)<sup>0,0*Z(7)],[0*Z(7),Z(7)</sup>2]]'`
> Got:
>     `'[[Z(7)<sup>0,0*Z(7)],[0*Z(7),Z(7)</sup>2]]*One(GF(7))'`

In gap:

```
gap> x:=Indeterminate(Rationals,"x");;
gap> p:=x^4+3*x^2+1;;
gap> e:=AlgebraicExtension(Rationals,p);
<algebraic extension over the Rationals of degree 4>
gap> M:=[[1,GeneratorsOfField(e)[1]^2]];
[ [ 1, (a^2) ] ]
gap> IsMatrix(M);
false
gap> IsMatrix(M*One(e));
true
```

Hence, in general the modified output is needed.

> There were other failures,
> 
> {{{
>         sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py
>         sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py
>         sage -t  devel/sage-matgp3/sage/plot/plot.py
> }}}
> but they may be unrelated since they were already reported by Jaap Spies
> on sage-devel for a clean install.

I think so, too. I am about to provide new patches for this ticket and for #2348.



---

archive/issue_comments_015970.json:
```json
{
    "body": "First apply the patches from #2348, then apply this patch. It extends the method invariant_generators to the case of finite matrix groups over number fields",
    "created_at": "2008-03-02T22:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15970",
    "user": "@simon-king-jena"
}
```

First apply the patches from #2348, then apply this patch. It extends the method invariant_generators to the case of finite matrix groups over number fields



---

archive/issue_comments_015971.json:
```json
{
    "body": "Attachment [invariant_generators.patch](tarball://root/attachments/some-uuid/ticket2367/invariant_generators.patch) by @simon-king-jena created at 2008-03-02 22:58:02\n\nReplying to [comment:2 wdj]:\n> The patches (first 2348 then this one) applied cleanly and the above code ran. \n\nNow i changed the patches of #2348 and of this ticket. So, a re-check is needed.\n\n> However, sage -testall failed. Here is one failure:\n>  ...\n> ----------------------------------------------------------------------\n> The following tests failed:\n> ...\n>         sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py\n>         sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py\n>         sage -t  devel/sage-matgp3/sage/plot/plot.py\n\nThese three tests fail on my system as well - with and without the patches. So, it doesn't seem to be related.\n\nBut with the patches (that partially add further doc tests), the following clearly related tests pass:\n* matrix_group.py\n* matrix_group_element.py\n* number_field.py\n* number_field_element.pyx\n* matrix1.pyx",
    "created_at": "2008-03-02T22:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15971",
    "user": "@simon-king-jena"
}
```

Attachment [invariant_generators.patch](tarball://root/attachments/some-uuid/ticket2367/invariant_generators.patch) by @simon-king-jena created at 2008-03-02 22:58:02

Replying to [comment:2 wdj]:
> The patches (first 2348 then this one) applied cleanly and the above code ran. 

Now i changed the patches of #2348 and of this ticket. So, a re-check is needed.

> However, sage -testall failed. Here is one failure:
>  ...
> ----------------------------------------------------------------------
> The following tests failed:
> ...
>         sage -t  devel/sage-matgp3/sage/rings/polynomial/groebner_fan.py
>         sage -t  devel/sage-matgp3/sage/rings/number_field/totallyreal.py
>         sage -t  devel/sage-matgp3/sage/plot/plot.py

These three tests fail on my system as well - with and without the patches. So, it doesn't seem to be related.

But with the patches (that partially add further doc tests), the following clearly related tests pass:
* matrix_group.py
* matrix_group_element.py
* number_field.py
* number_field_element.pyx
* matrix1.pyx



---

archive/issue_comments_015972.json:
```json
{
    "body": "This applies cleanly (first 2348 then this one) to 2.10.3.rc0. It also passes sage -testall (except for the usual 3 that fail, as reported first by Jaap).\nExcellent patch. Recommend acceptance.",
    "created_at": "2008-03-03T00:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15972",
    "user": "@wdjoyner"
}
```

This applies cleanly (first 2348 then this one) to 2.10.3.rc0. It also passes sage -testall (except for the usual 3 that fail, as reported first by Jaap).
Excellent patch. Recommend acceptance.



---

archive/issue_comments_015973.json:
```json
{
    "body": "This ticket, together with #2348, is now ticket #2395. First reason is that we got a new sage pre-release. Second reason is that my suggestions for fixing the gap interface (#2348) changed. Third reason is that #2348 and this ticket belong closely together, hence, they should be worked on in *one* ticket.",
    "created_at": "2008-03-05T10:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15973",
    "user": "@simon-king-jena"
}
```

This ticket, together with #2348, is now ticket #2395. First reason is that we got a new sage pre-release. Second reason is that my suggestions for fixing the gap interface (#2348) changed. Third reason is that #2348 and this ticket belong closely together, hence, they should be worked on in *one* ticket.



---

archive/issue_comments_015974.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-05T10:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2367#issuecomment-15974",
    "user": "@simon-king-jena"
}
```

Resolution: invalid
