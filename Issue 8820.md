# Issue 8820: elliptic_exponential broken for curves over number fields

archive/issues_008820.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @jdemeyer rwb\n\n\n```\nsage: E = EllipticCurve('37a')\nsage: K.<a> = QuadraticField(-5)\nsage: L = E.change_ring(K).period_lattice(K.places()[0])\nsage: L.elliptic_exponential(CDF(.1,.1))\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.py\", line 1390, in elliptic_exponential\n    pxy = E.pari_curve(prec+5).ellztopoint(w)\n  File \"gen.pyx\", line 9234, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44342)\nPariError: bad argument for an elliptic curve related function (43)\n```\n\n\nPerhaps Pari doesn't support curve not over Q? \n\nIssue created by migration from https://trac.sagemath.org/ticket/8820\n\n",
    "created_at": "2010-04-29T09:03:18Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "elliptic_exponential broken for curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8820",
    "user": "https://github.com/robertwb"
}
```
Assignee: @JohnCremona

CC:  @jdemeyer rwb


```
sage: E = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-5)
sage: L = E.change_ring(K).period_lattice(K.places()[0])
sage: L.elliptic_exponential(CDF(.1,.1))
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.py", line 1390, in elliptic_exponential
    pxy = E.pari_curve(prec+5).ellztopoint(w)
  File "gen.pyx", line 9234, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44342)
PariError: bad argument for an elliptic curve related function (43)
```


Perhaps Pari doesn't support curve not over Q? 

Issue created by migration from https://trac.sagemath.org/ticket/8820





---

archive/issue_comments_080816.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-04-29T09:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80816",
    "user": "https://github.com/robertwb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_080817.json:
```json
{
    "body": "Actually, this makes sense because I'm not giving Pari the embedding to use.",
    "created_at": "2010-04-29T09:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80817",
    "user": "https://github.com/robertwb"
}
```

Actually, this makes sense because I'm not giving Pari the embedding to use.



---

archive/issue_comments_080818.json:
```json
{
    "body": "Rats, I thought I had implemented this properly.  The elliptic log does have examples over number fields with complex embeddings!  This should be a lot easier...\n\nThe period lattice has an embedding into CC (or RR) stored with it.  That should be used to create a pari elliptic curve defined over RR or CC, there the pari function would work.\n\nI would much prefer to have our own Weierstrass functions implemented, but that's the situation right now.\n\nNote that this will involve some of the same code as #8815.",
    "created_at": "2010-04-29T09:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80818",
    "user": "https://github.com/JohnCremona"
}
```

Rats, I thought I had implemented this properly.  The elliptic log does have examples over number fields with complex embeddings!  This should be a lot easier...

The period lattice has an embedding into CC (or RR) stored with it.  That should be used to create a pari elliptic curve defined over RR or CC, there the pari function would work.

I would much prefer to have our own Weierstrass functions implemented, but that's the situation right now.

Note that this will involve some of the same code as #8815.



---

archive/issue_comments_080819.json:
```json
{
    "body": "I am working on this right now.",
    "created_at": "2010-08-27T09:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80819",
    "user": "https://github.com/JohnCremona"
}
```

I am working on this right now.



---

archive/issue_comments_080820.json:
```json
{
    "body": "applies to 4.5.3.alpha2",
    "created_at": "2010-08-29T14:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80820",
    "user": "https://github.com/JohnCremona"
}
```

applies to 4.5.3.alpha2



---

archive/issue_comments_080821.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-29T14:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80821",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080822.json:
```json
{
    "body": "Attachment [trac_8820-elliptic-exp.patch](tarball://root/attachments/some-uuid/ticket8820/trac_8820-elliptic-exp.patch) by @JohnCremona created at 2010-08-29 14:38:36\n\nThe patch implements this.  I left the old code (using ellztopoint) for curves over QQ though the new code (using ellwp) works fine too, since the the output of many doctests would have changed (in insignificant bits), especially in heegner.py.\n\nI also documented a couple of functions in period_lattice.py which were not, so that file now has 100% coverage.",
    "created_at": "2010-08-29T14:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80822",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8820-elliptic-exp.patch](tarball://root/attachments/some-uuid/ticket8820/trac_8820-elliptic-exp.patch) by @JohnCremona created at 2010-08-29 14:38:36

The patch implements this.  I left the old code (using ellztopoint) for curves over QQ though the new code (using ellwp) works fine too, since the the output of many doctests would have changed (in insignificant bits), especially in heegner.py.

I also documented a couple of functions in period_lattice.py which were not, so that file now has 100% coverage.



---

archive/issue_comments_080823.json:
```json
{
    "body": "I get doctest failures, like the typical case below. It should be considered numerical noise, but somehow it is not a very good example then. I think a point (1,1) would give a more convincing example.\n\n\n```\nFile \"/local/pmzcw/prog/sage-4.5/devel/sage-test/sage/schemes/elliptic_curves/period_lattice.py\", line 1424:\n    sage: Li[0].elliptic_exponential(zi[0])\nExpected:\n    (2.17701177381006e-16 + 2.21973923391111e-16*I : 1.11022302462516e-16 - 2.21990394816407e-16*I : 1.00000000000000)\nGot:\n    (2.17818031662168e-16 + 2.22022549601564e-16*I : 1.11022302462516e-16 - 2.22044604925031e-16*I : 1.00000000000000)\n```\n\n\nThe lines that fail are 1424, 1426, 1428, 1440, 1450, 1452.",
    "created_at": "2010-09-23T19:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80823",
    "user": "https://github.com/categorie"
}
```

I get doctest failures, like the typical case below. It should be considered numerical noise, but somehow it is not a very good example then. I think a point (1,1) would give a more convincing example.


```
File "/local/pmzcw/prog/sage-4.5/devel/sage-test/sage/schemes/elliptic_curves/period_lattice.py", line 1424:
    sage: Li[0].elliptic_exponential(zi[0])
Expected:
    (2.17701177381006e-16 + 2.21973923391111e-16*I : 1.11022302462516e-16 - 2.21990394816407e-16*I : 1.00000000000000)
Got:
    (2.17818031662168e-16 + 2.22022549601564e-16*I : 1.11022302462516e-16 - 2.22044604925031e-16*I : 1.00000000000000)
```


The lines that fail are 1424, 1426, 1428, 1440, 1450, 1452.



---

archive/issue_comments_080824.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T19:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80824",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080825.json:
```json
{
    "body": "Replying to [comment:5 wuthrich]:\n> I get doctest failures, like the typical case below. It should be considered numerical noise, but somehow it is not a very good example then. I think a point (1,1) would give a more convincing example.\n> \n> {{{\n> File \"/local/pmzcw/prog/sage-4.5/devel/sage-test/sage/schemes/elliptic_curves/period_lattice.py\", line 1424:\n>     sage: Li[0].elliptic_exponential(zi[0])\n> Expected:\n>     (2.17701177381006e-16 + 2.21973923391111e-16*I : 1.11022302462516e-16 - 2.21990394816407e-16*I : 1.00000000000000)\n> Got:\n>     (2.17818031662168e-16 + 2.22022549601564e-16*I : 1.11022302462516e-16 - 2.22044604925031e-16*I : 1.00000000000000)\n> }}}\n> \n> The lines that fail are 1424, 1426, 1428, 1440, 1450, 1452.\n\nWhich version is that?  The patch says 4.5!",
    "created_at": "2010-09-23T21:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80825",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 wuthrich]:
> I get doctest failures, like the typical case below. It should be considered numerical noise, but somehow it is not a very good example then. I think a point (1,1) would give a more convincing example.
> 
> {{{
> File "/local/pmzcw/prog/sage-4.5/devel/sage-test/sage/schemes/elliptic_curves/period_lattice.py", line 1424:
>     sage: Li[0].elliptic_exponential(zi[0])
> Expected:
>     (2.17701177381006e-16 + 2.21973923391111e-16*I : 1.11022302462516e-16 - 2.21990394816407e-16*I : 1.00000000000000)
> Got:
>     (2.17818031662168e-16 + 2.22022549601564e-16*I : 1.11022302462516e-16 - 2.22044604925031e-16*I : 1.00000000000000)
> }}}
> 
> The lines that fail are 1424, 1426, 1428, 1440, 1450, 1452.

Which version is that?  The patch says 4.5!



---

archive/issue_comments_080826.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n\n\n> Which version is that?  The patch says 4.5!\n\nSorry, I meant \"path\".",
    "created_at": "2010-09-23T21:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80826",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:6 cremona]:


> Which version is that?  The patch says 4.5!

Sorry, I meant "path".



---

archive/issue_comments_080827.json:
```json
{
    "body": "It is 4.5.3 on my office computer. \n\nNot that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.\n\nAm I too picky ?\n\nChris.",
    "created_at": "2010-09-24T18:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80827",
    "user": "https://github.com/categorie"
}
```

It is 4.5.3 on my office computer. 

Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.

Am I too picky ?

Chris.



---

archive/issue_comments_080828.json:
```json
{
    "body": "Replying to [comment:8 wuthrich]:\n> It is 4.5.3 on my office computer. \n> \n> Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.\n> \n> Am I too picky ?\n\nNo, not at all -- using points which do not have 0 as a coordinate is a good idea!  But I was confused since the test which fails does not appear to exist on my 4.6.alpha1.\n\n> \n> Chris.",
    "created_at": "2010-09-24T19:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80828",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:8 wuthrich]:
> It is 4.5.3 on my office computer. 
> 
> Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.
> 
> Am I too picky ?

No, not at all -- using points which do not have 0 as a coordinate is a good idea!  But I was confused since the test which fails does not appear to exist on my 4.6.alpha1.

> 
> Chris.



---

archive/issue_comments_080829.json:
```json
{
    "body": "Replying to [comment:9 cremona]:\n> Replying to [comment:8 wuthrich]:\n> > It is 4.5.3 on my office computer. \n> > \n> > Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.\n> > \n> > Am I too picky ?\n> \n> No, not at all -- using points which do not have 0 as a coordinate is a good idea!  But I was confused since the test which fails does not appear to exist on my 4.6.alpha1.\n\nSorry, I am being completely stupid -- of course the failing test is in the patch and I was looking at unpatched files!  But now I find that the patch does not apply to 4.6.alpha1 so I will have to rebase it.  When I do that I will try to use better examples.\n\n> \n> > \n> > Chris.",
    "created_at": "2010-09-24T19:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80829",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:9 cremona]:
> Replying to [comment:8 wuthrich]:
> > It is 4.5.3 on my office computer. 
> > 
> > Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.
> > 
> > Am I too picky ?
> 
> No, not at all -- using points which do not have 0 as a coordinate is a good idea!  But I was confused since the test which fails does not appear to exist on my 4.6.alpha1.

Sorry, I am being completely stupid -- of course the failing test is in the patch and I was looking at unpatched files!  But now I find that the patch does not apply to 4.6.alpha1 so I will have to rebase it.  When I do that I will try to use better examples.

> 
> > 
> > Chris.



---

archive/issue_comments_080830.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-24T20:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80830",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080831.json:
```json
{
    "body": "Please try the rebased patch.  I changes the point (0,0) to (-1,-1) in the bad example, but that was enough since the approximate imaginary parts were not exactly 0 -- which I got around by taking real parts where necessary.  A little crude, but it avoids the fuzz.",
    "created_at": "2010-09-24T20:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80831",
    "user": "https://github.com/JohnCremona"
}
```

Please try the rebased patch.  I changes the point (0,0) to (-1,-1) in the bad example, but that was enough since the approximate imaginary parts were not exactly 0 -- which I got around by taking real parts where necessary.  A little crude, but it avoids the fuzz.



---

archive/issue_comments_080832.json:
```json
{
    "body": "John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)\n\nAlso: you should use \"PARI\" instead of \"Pari\".",
    "created_at": "2010-09-25T17:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80832",
    "user": "https://github.com/jdemeyer"
}
```

John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)

Also: you should use "PARI" instead of "Pari".



---

archive/issue_comments_080833.json:
```json
{
    "body": "Replying to [comment:12 jdemeyer]:\n> John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)\n> \n> Also: you should use \"PARI\" instead of \"Pari\".\n\nyes, alpha1",
    "created_at": "2010-09-25T17:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80833",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:12 jdemeyer]:
> John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)
> 
> Also: you should use "PARI" instead of "Pari".

yes, alpha1



---

archive/issue_comments_080834.json:
```json
{
    "body": "Replying to [comment:13 cremona]:\n> Replying to [comment:12 jdemeyer]:\n> > John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)\n> > \n> > Also: you should use \"PARI\" instead of \"Pari\".\n> \n> yes, alpha1\n\nI have now fixed all the offending \"Pari\" and \"pari\" in the patch, and all the files in  elliptic_curves!",
    "created_at": "2010-09-26T16:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80834",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:13 cremona]:
> Replying to [comment:12 jdemeyer]:
> > John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)
> > 
> > Also: you should use "PARI" instead of "Pari".
> 
> yes, alpha1

I have now fixed all the offending "Pari" and "pari" in the patch, and all the files in  elliptic_curves!



---

archive/issue_comments_080835.json:
```json
{
    "body": "Attachment [trac_8820-elliptic-exp-rebase.patch](tarball://root/attachments/some-uuid/ticket8820/trac_8820-elliptic-exp-rebase.patch) by @JohnCremona created at 2010-09-26 16:46:50\n\napplies to 4.6.alpha1",
    "created_at": "2010-09-26T16:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80835",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8820-elliptic-exp-rebase.patch](tarball://root/attachments/some-uuid/ticket8820/trac_8820-elliptic-exp-rebase.patch) by @JohnCremona created at 2010-09-26 16:46:50

applies to 4.6.alpha1



---

archive/issue_comments_080836.json:
```json
{
    "body": "John, I have rebased your patch such that it can be applied after the positively-reviewed #9931 (there were several conflicts).  I also made some very small changes to the docstring of the `cardinality` function in `ell_finite_field.py`",
    "created_at": "2010-09-26T18:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80836",
    "user": "https://github.com/jdemeyer"
}
```

John, I have rebased your patch such that it can be applied after the positively-reviewed #9931 (there were several conflicts).  I also made some very small changes to the docstring of the `cardinality` function in `ell_finite_field.py`



---

archive/issue_comments_080837.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> John, I have rebased your patch such that it can be applied after the positively-reviewed #9931 (there were several conflicts).  I also made some very small changes to the docstring of the `cardinality` function in `ell_finite_field.py`\n\nOK, I'm not sure what the issues were there but the new patch applies fine after #9931;  I am currently testing it.  Meanwhile:  the latest patch's header is\n\n```\n...\n# User Jeroen Demeyer <jdemeyer@cage.ugent.be>\n...\n[mq]: 8820_rebase_after_9931\n```\n\nand I think protocol would leave me as author (and have a better one-line description) ;)",
    "created_at": "2010-09-26T20:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80837",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:15 jdemeyer]:
> John, I have rebased your patch such that it can be applied after the positively-reviewed #9931 (there were several conflicts).  I also made some very small changes to the docstring of the `cardinality` function in `ell_finite_field.py`

OK, I'm not sure what the issues were there but the new patch applies fine after #9931;  I am currently testing it.  Meanwhile:  the latest patch's header is

```
...
# User Jeroen Demeyer <jdemeyer@cage.ugent.be>
...
[mq]: 8820_rebase_after_9931
```

and I think protocol would leave me as author (and have a better one-line description) ;)



---

archive/issue_comments_080838.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-26T20:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80838",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080839.json:
```json
{
    "body": "Replying to [comment:16 cremona]:\n> # User Jeroen Demeyer <jdemeyer`@`cage.ugent.be>\n> ...\n> [mq]: 8820_rebase_after_9931\n> }}}\n> and I think protocol would leave me as author (and have a better one-line description) ;)\n\nOK, I just copy-pasted the header from your patch.",
    "created_at": "2010-09-26T21:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80839",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:16 cremona]:
> # User Jeroen Demeyer <jdemeyer`@`cage.ugent.be>
> ...
> [mq]: 8820_rebase_after_9931
> }}}
> and I think protocol would leave me as author (and have a better one-line description) ;)

OK, I just copy-pasted the header from your patch.



---

archive/issue_comments_080840.json:
```json
{
    "body": "John's patch rebased to be applied on top of #9931 (and some small additional changes)",
    "created_at": "2010-09-26T21:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80840",
    "user": "https://github.com/jdemeyer"
}
```

John's patch rebased to be applied on top of #9931 (and some small additional changes)



---

archive/issue_comments_080841.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-26T21:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80841",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_080842.json:
```json
{
    "body": "Attachment [8820_rebase_after_9931.patch](tarball://root/attachments/some-uuid/ticket8820/8820_rebase_after_9931.patch) by @JohnCremona created at 2010-09-26 21:42:19\n\nReplying to [comment:17 jdemeyer]:\n> Replying to [comment:16 cremona]:\n> > # User Jeroen Demeyer <jdemeyer`@`cage.ugent.be>\n> > ...\n> > [mq]: 8820_rebase_after_9931\n> > }}}\n> > and I think protocol would leave me as author (and have a better one-line description) ;)\n> \n> OK, I just copy-pasted the header from your patch.\n\nThanks -- I added your name as reviewer and marked the ticket Positive Review.  If you want, you can add your name as author (and mine as reviewer) -- I appreciate your attention to detail.\n\nRelease manager:  apply only the last patch 8820_rebase_after_9931.patch, after the patch at #9931.",
    "created_at": "2010-09-26T21:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80842",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8820_rebase_after_9931.patch](tarball://root/attachments/some-uuid/ticket8820/8820_rebase_after_9931.patch) by @JohnCremona created at 2010-09-26 21:42:19

Replying to [comment:17 jdemeyer]:
> Replying to [comment:16 cremona]:
> > # User Jeroen Demeyer <jdemeyer`@`cage.ugent.be>
> > ...
> > [mq]: 8820_rebase_after_9931
> > }}}
> > and I think protocol would leave me as author (and have a better one-line description) ;)
> 
> OK, I just copy-pasted the header from your patch.

Thanks -- I added your name as reviewer and marked the ticket Positive Review.  If you want, you can add your name as author (and mine as reviewer) -- I appreciate your attention to detail.

Release manager:  apply only the last patch 8820_rebase_after_9931.patch, after the patch at #9931.



---

archive/issue_comments_080843.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-26T22:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80843",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_080844.json:
```json
{
    "body": "I'm sorry John, but I did not review your patch, I just made a few small comments.  In any case, I think it is strange for the author of a patch to set his ticket to positive_review (no offense though).  I can probably review your patch later (not tonight).",
    "created_at": "2010-09-26T22:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80844",
    "user": "https://github.com/jdemeyer"
}
```

I'm sorry John, but I did not review your patch, I just made a few small comments.  In any case, I think it is strange for the author of a patch to set his ticket to positive_review (no offense though).  I can probably review your patch later (not tonight).



---

archive/issue_comments_080845.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-26T22:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80845",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080846.json:
```json
{
    "body": "Replying to [comment:19 jdemeyer]:\n> I'm sorry John, but I did not review your patch, I just made a few small comments.  In any case, I think it is strange for the author of a patch to set his ticket to positive_review (no offense though).  I can probably review your patch later (not tonight).\n\nNo problem -- I misunderstood, and also forgot that the original doctest failures were not from you but from Chris Wuthrich.\n\nOf course I would not positively review my own work!  I have now added Chris to the list of reviewers, and hope that he'll be able to take another look at it.  Needs review!",
    "created_at": "2010-09-26T22:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80846",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:19 jdemeyer]:
> I'm sorry John, but I did not review your patch, I just made a few small comments.  In any case, I think it is strange for the author of a patch to set his ticket to positive_review (no offense though).  I can probably review your patch later (not tonight).

No problem -- I misunderstood, and also forgot that the original doctest failures were not from you but from Chris Wuthrich.

Of course I would not positively review my own work!  I have now added Chris to the list of reviewers, and hope that he'll be able to take another look at it.  Needs review!



---

archive/issue_comments_080847.json:
```json
{
    "body": "A few comments:\n\n* I think the help for `elliptic_exponential` (lines 1379--1385) is not so well written.  I would write something like\n\n```\nOUTPUT:\n\n- If ``to_curve`` is False, a 2-tuple of real or complex numbers\nrepresenting the point `(x,y) = (\\wp(z),\\wp'(z))` where `\\wp` denotes the Weierstrass\n`\\wp`-function with respect to this lattice.\n\n- If ``to_curve`` is True, the point `(x-b_2/12,y-(a_1(x-b_2/12)-a_3)/2)`\nas a point in `E(\\RR)` or `E(\\CC)`, with `(x,y) = (\\wp(z),\\wp'(z))` as above.\n\nIf the lattice is real...\n```\n\n\n* The comment\n\n```\n       # the next lines compute [P(w), P'(w)] when flag=1\n       # or [x:y:1] in E(C) when flag=2\n```\n\n seems to refer to old code.\n\n* Is there a good reason to distinguish between QQ and general number fields?  The number-field code seems simpler, so you could consider removing the special-case code for QQ.\n\n* lines 1503 and 1530: `C(t.real().python(),t.imag().python())` can be simplified as `C(t)`.\n\n* it doesn't work for the point at infinity (and there should be a doctest for that case anyway):\n\n```\nsage: E = EllipticCurve([1,1,1,-8,6])\nsage: L = E.period_lattice()\nsage: L.elliptic_exponential(0)\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n\n/usr/local/src/pari/src/<ipython console> in <module>()\n\n/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.pyc in elliptic_exponential(self, z, to_curve)\n   1476         if self.coordinates(z) == self.coordinates(z, rounding='round'):\n   1477             if to_curve:\n-> 1478                 return E.change_ring(C)(0)\n   1479             return (C('+infinity'),C('+infinity'))\n   1480\n\nUnboundLocalError: local variable 'E' referenced before assignment\n```\n",
    "created_at": "2010-09-30T09:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80847",
    "user": "https://github.com/jdemeyer"
}
```

A few comments:

* I think the help for `elliptic_exponential` (lines 1379--1385) is not so well written.  I would write something like

```
OUTPUT:

- If ``to_curve`` is False, a 2-tuple of real or complex numbers
representing the point `(x,y) = (\wp(z),\wp'(z))` where `\wp` denotes the Weierstrass
`\wp`-function with respect to this lattice.

- If ``to_curve`` is True, the point `(x-b_2/12,y-(a_1(x-b_2/12)-a_3)/2)`
as a point in `E(\RR)` or `E(\CC)`, with `(x,y) = (\wp(z),\wp'(z))` as above.

If the lattice is real...
```


* The comment

```
       # the next lines compute [P(w), P'(w)] when flag=1
       # or [x:y:1] in E(C) when flag=2
```

 seems to refer to old code.

* Is there a good reason to distinguish between QQ and general number fields?  The number-field code seems simpler, so you could consider removing the special-case code for QQ.

* lines 1503 and 1530: `C(t.real().python(),t.imag().python())` can be simplified as `C(t)`.

* it doesn't work for the point at infinity (and there should be a doctest for that case anyway):

```
sage: E = EllipticCurve([1,1,1,-8,6])
sage: L = E.period_lattice()
sage: L.elliptic_exponential(0)
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/usr/local/src/pari/src/<ipython console> in <module>()

/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.pyc in elliptic_exponential(self, z, to_curve)
   1476         if self.coordinates(z) == self.coordinates(z, rounding='round'):
   1477             if to_curve:
-> 1478                 return E.change_ring(C)(0)
   1479             return (C('+infinity'),C('+infinity'))
   1480

UnboundLocalError: local variable 'E' referenced before assignment
```




---

archive/issue_comments_080848.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-30T09:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80848",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080849.json:
```json
{
    "body": "Also, there is trouble with points which are very close to the point af infinity:\n\n```\nsage: K.<a> = QuadraticField(-1)\nsage: E = EllipticCurve([0,0,0,a,0])\nsage: L = E.period_lattice(K.complex_embeddings()[0])\nsage: L.elliptic_exponential(1e-100)\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n\n/home/jdemeyer/<ipython console> in <module>()\n\n/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.pyc in elliptic_exponential(self, z, to_curve)\n   1527         # the same precision as the input.\n   1528\n-> 1529         x,y = pari(self.basis(prec=prec)).ellwp(w,flag=1)\n   1530         x,y = [C(t) for t in (x,y)]\n   1531\n\n/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:45047)()\n\nPariError: division by zero (27)\n```\n",
    "created_at": "2010-09-30T09:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80849",
    "user": "https://github.com/jdemeyer"
}
```

Also, there is trouble with points which are very close to the point af infinity:

```
sage: K.<a> = QuadraticField(-1)
sage: E = EllipticCurve([0,0,0,a,0])
sage: L = E.period_lattice(K.complex_embeddings()[0])
sage: L.elliptic_exponential(1e-100)
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/jdemeyer/<ipython console> in <module>()

/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.pyc in elliptic_exponential(self, z, to_curve)
   1527         # the same precision as the input.
   1528
-> 1529         x,y = pari(self.basis(prec=prec)).ellwp(w,flag=1)
   1530         x,y = [C(t) for t in (x,y)]
   1531

/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:45047)()

PariError: division by zero (27)
```




---

archive/issue_comments_080850.json:
```json
{
    "body": "Thanks for the comments, I will revise the patch accordingly.  The very last point (evaluation when z is very small but not zero) will not be easy though.  I think that I left in the special code for QQ since it was faster, but I may be mixing this up with the (harder!) elliptic logarithm.",
    "created_at": "2010-09-30T10:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80850",
    "user": "https://github.com/JohnCremona"
}
```

Thanks for the comments, I will revise the patch accordingly.  The very last point (evaluation when z is very small but not zero) will not be easy though.  I think that I left in the special code for QQ since it was faster, but I may be mixing this up with the (harder!) elliptic logarithm.



---

archive/issue_comments_080851.json:
```json
{
    "body": "Replying to [comment:25 cremona]:\n> Thanks for the comments, I will revise the patch accordingly.  The very last point (evaluation when z is very small but not zero) will not be easy though.\n\nYou could use `try:`/`except PariError:` for this.  The only problem is that currently, you cannot easily check in Python whether a PariError is a division by zero or something else.",
    "created_at": "2010-09-30T15:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80851",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:25 cremona]:
> Thanks for the comments, I will revise the patch accordingly.  The very last point (evaluation when z is very small but not zero) will not be easy though.

You could use `try:`/`except PariError:` for this.  The only problem is that currently, you cannot easily check in Python whether a PariError is a division by zero or something else.



---

archive/issue_comments_080852.json:
```json
{
    "body": "It's ok, I have fixed it and the only reason I have not yet upadted the patch is that I am getting lots of failures in heegner.py -- not for the first time.  Several of the doctests there are not very well designed, so I may complain to Robert Bradshaw if I cannot fix them all!",
    "created_at": "2010-09-30T16:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80852",
    "user": "https://github.com/JohnCremona"
}
```

It's ok, I have fixed it and the only reason I have not yet upadted the patch is that I am getting lots of failures in heegner.py -- not for the first time.  Several of the doctests there are not very well designed, so I may complain to Robert Bradshaw if I cannot fix them all!



---

archive/issue_comments_080853.json:
```json
{
    "body": "8820_rebase_after_9931-new.patch adresses the doctest failures in heegner.py.  I did this quite carefully (even refining a little the code which does the modular parametrization).  I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero;  but when the output is an approximate integral Heegner point one cannot easily change the point.  I hope reviewer(s) do not object to the various ways I found  around this -- with very little use of ... and none (I think) of #random.\n\nNote that these Heegner examples are often going to be problematical since in many cases the point computed is approximately (0:1:0), i.e. the z in CC is approximately a period.  In such examples it might be better just to output E.period_lattice().coordinates(z) rather than E.elliptic_exponential(z).  However, I have adjusted the test for being integral (i.e. for z to b in the period lattice) in a way that I hope is a reasonable compromise:   namely that the coordinates w.r.t. the lattice basis should be approximately integral in the sense that their fractional part is at most `2^(0.8*prec)`.",
    "created_at": "2010-10-03T12:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80853",
    "user": "https://github.com/JohnCremona"
}
```

8820_rebase_after_9931-new.patch adresses the doctest failures in heegner.py.  I did this quite carefully (even refining a little the code which does the modular parametrization).  I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero;  but when the output is an approximate integral Heegner point one cannot easily change the point.  I hope reviewer(s) do not object to the various ways I found  around this -- with very little use of ... and none (I think) of #random.

Note that these Heegner examples are often going to be problematical since in many cases the point computed is approximately (0:1:0), i.e. the z in CC is approximately a period.  In such examples it might be better just to output E.period_lattice().coordinates(z) rather than E.elliptic_exponential(z).  However, I have adjusted the test for being integral (i.e. for z to b in the period lattice) in a way that I hope is a reasonable compromise:   namely that the coordinates w.r.t. the lattice basis should be approximately integral in the sense that their fractional part is at most `2^(0.8*prec)`.



---

archive/issue_comments_080854.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-03T12:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80854",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080855.json:
```json
{
    "body": "Replying to [comment:28 cremona]:\n> However, I have adjusted the test for being integral (i.e. for z to b in the period lattice) in a way that I hope is a reasonable compromise:   namely that the coordinates w.r.t. the lattice basis should be approximately integral in the sense that their fractional part is at most `2^(0.8*prec)`.\n\nI like this solution. The `elliptic_exponential()` code looks fine to me.  However, I would like somebody else to review the heegner stuff.\n\nOne small suggestion: the doctest for `elliptic_exponential()` is quite long, so I would separate it in an `EXAMPLES` part and a `TESTS` part.",
    "created_at": "2010-10-03T15:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80855",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:28 cremona]:
> However, I have adjusted the test for being integral (i.e. for z to b in the period lattice) in a way that I hope is a reasonable compromise:   namely that the coordinates w.r.t. the lattice basis should be approximately integral in the sense that their fractional part is at most `2^(0.8*prec)`.

I like this solution. The `elliptic_exponential()` code looks fine to me.  However, I would like somebody else to review the heegner stuff.

One small suggestion: the doctest for `elliptic_exponential()` is quite long, so I would separate it in an `EXAMPLES` part and a `TESTS` part.



---

archive/issue_comments_080856.json:
```json
{
    "body": "Replying to [comment:28 cremona]:\n> I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero\n\nWell, my **personal opinion** on this differs a bit.  I think we should remember that doctests not only serve as tests, but also as documentation.  I think it is always a difficult excercise to balance these two.  For me personally, the balance always goes in favour of documentation.  When needed, one can still add true tests in a `TESTS` section of a doctest.",
    "created_at": "2010-10-03T16:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80856",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:28 cremona]:
> I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero

Well, my **personal opinion** on this differs a bit.  I think we should remember that doctests not only serve as tests, but also as documentation.  I think it is always a difficult excercise to balance these two.  For me personally, the balance always goes in favour of documentation.  When needed, one can still add true tests in a `TESTS` section of a doctest.



---

archive/issue_comments_080857.json:
```json
{
    "body": "Replying to [comment:30 jdemeyer]:\n> Replying to [comment:28 cremona]:\n> > I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero\n> \n> Well, my **personal opinion** on this differs a bit.  I think we should remember that doctests not only serve as tests, but also as documentation.  I think it is always a difficult excercise to balance these two.  For me personally, the balance always goes in favour of documentation.  When needed, one can still add true tests in a `TESTS` section of a doctest.\n\nFair enough.  In the heegner file, which I did not write any of, I did not want to re-think documentation/tests from scratch, although that might be a good idea;  I just wanted to get things to work!  (And I would not have had to do anything, I think, if I had not followed the suggestion to eliminate the specific QQ code from elliptic_exponential.)",
    "created_at": "2010-10-03T16:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80857",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:30 jdemeyer]:
> Replying to [comment:28 cremona]:
> > I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero
> 
> Well, my **personal opinion** on this differs a bit.  I think we should remember that doctests not only serve as tests, but also as documentation.  I think it is always a difficult excercise to balance these two.  For me personally, the balance always goes in favour of documentation.  When needed, one can still add true tests in a `TESTS` section of a doctest.

Fair enough.  In the heegner file, which I did not write any of, I did not want to re-think documentation/tests from scratch, although that might be a good idea;  I just wanted to get things to work!  (And I would not have had to do anything, I think, if I had not followed the suggestion to eliminate the specific QQ code from elliptic_exponential.)



---

archive/issue_comments_080858.json:
```json
{
    "body": "I give all the changes to heegner.py in the patch \"8820_rebase_after_9931-new.patch\" a positive review.",
    "created_at": "2010-10-04T23:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80858",
    "user": "https://github.com/williamstein"
}
```

I give all the changes to heegner.py in the patch "8820_rebase_after_9931-new.patch" a positive review.



---

archive/issue_comments_080859.json:
```json
{
    "body": "You beat me to it :). Looks fine by me too.",
    "created_at": "2010-10-05T04:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80859",
    "user": "https://github.com/robertwb"
}
```

You beat me to it :). Looks fine by me too.



---

archive/issue_comments_080860.json:
```json
{
    "body": "There is a doctest failure on a 32-bit machine:\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/heegner.py\"\n**********************************************************************\nFile \"/Users/jdemeyer/sage-4.6.alpha2/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 3048:\n    sage: P = E.heegner_point(-19); y = P._trace_numerical_conductor_1(); [c.real() for c in y]\nExpected:\n    [-1.26165722088693e-16, -1.00000000000000, 1.00000000000000]\nGot:\n    [-1.26126537554300e-16, -1.00000000000000, 1.00000000000000]\n**********************************************************************\n```\n\n\nWhen this is fixed (just write -1.261...), this ticket can finally gets its positive_review.",
    "created_at": "2010-10-05T07:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80860",
    "user": "https://github.com/jdemeyer"
}
```

There is a doctest failure on a 32-bit machine:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/Users/jdemeyer/sage-4.6.alpha2/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 3048:
    sage: P = E.heegner_point(-19); y = P._trace_numerical_conductor_1(); [c.real() for c in y]
Expected:
    [-1.26165722088693e-16, -1.00000000000000, 1.00000000000000]
Got:
    [-1.26126537554300e-16, -1.00000000000000, 1.00000000000000]
**********************************************************************
```


When this is fixed (just write -1.261...), this ticket can finally gets its positive_review.



---

archive/issue_comments_080861.json:
```json
{
    "body": "replaces previous",
    "created_at": "2010-10-05T08:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80861",
    "user": "https://github.com/JohnCremona"
}
```

replaces previous



---

archive/issue_comments_080862.json:
```json
{
    "body": "Attachment [8820_rebase_after_9931-new.patch](tarball://root/attachments/some-uuid/ticket8820/8820_rebase_after_9931-new.patch) by @JohnCremona created at 2010-10-05 08:30:57\n\nThanks to all, and apologies for missing that one.  I have changed the patch as suggested and just tested it on a 32-bit machine as well as a 64-bit.\n\nThat failing test is exactly the kind of thing it would be nice to avoid altogether in doctests, since the \"true\" value of the x-coordinate is 0, so all nonzero digits, and the sign, are completely spurious.\n\nJeroen, if you are happy with this now could you mark it as \"positive review\"?  Thanks.\n\nRelease manager: only the last patch is to be applied.",
    "created_at": "2010-10-05T08:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80862",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8820_rebase_after_9931-new.patch](tarball://root/attachments/some-uuid/ticket8820/8820_rebase_after_9931-new.patch) by @JohnCremona created at 2010-10-05 08:30:57

Thanks to all, and apologies for missing that one.  I have changed the patch as suggested and just tested it on a 32-bit machine as well as a 64-bit.

That failing test is exactly the kind of thing it would be nice to avoid altogether in doctests, since the "true" value of the x-coordinate is 0, so all nonzero digits, and the sign, are completely spurious.

Jeroen, if you are happy with this now could you mark it as "positive review"?  Thanks.

Release manager: only the last patch is to be applied.



---

archive/issue_comments_080863.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-05T20:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80863",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-06T03:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8820#issuecomment-80864",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008985.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-10-06T03:17:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8820",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8820#event-8985"
}
```
