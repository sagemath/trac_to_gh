# Issue 1046: speed regression in mq.SR.polynomial_system()  due to new coercion code?

archive/issues_001046.json:
```json
{
    "body": "Assignee: robertwb\n\nTry to run this code:\n\n\n```\nsage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)\nsage: F,s = sr.polynomial_system()\n```\n\n\nand wait for it to terminate (~17s on my 2.33Ghz system) in a fresh SAGE session. The second run takes only 2s.\n\n\nI profiled this with hotshot like this:\n\n\n```\nsage: import hotshot\nsage: filename = \"pythongrind.prof\"\nsage: prof = hotshot.Profile(filename, lineevents=1)\nsage: prof.run(\"sr.polynomial_system()\")\n<hotshot.Profile instance at 0x414c11ec>\nsage: prof.close()\n```\n\n\nand converted the result to cachegrind/calltree format\n\n\n```\nhotshot2calltree -o cachegrind.out.42 pythongrind.prof\n```\n\n\nto inspect the result with kcachegrind. Apparently, both `sr.round_polynomials` and `sr.key_schedule_polynomials` call `MatrixSpace.get_action_impl` which in turn calls `pushout` which calls `construction_tower`. `construction_tower` creates *7164* polynomial rings and this ring construction takes up 85% of the entire runtime. \n\nSo apparently the most time is spent in coercion (which also explains the better runtime for the second run) and I believe this is due to a bug.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1046\n\n",
    "created_at": "2007-10-31T23:57:30Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "speed regression in mq.SR.polynomial_system()  due to new coercion code?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1046",
    "user": "malb"
}
```
Assignee: robertwb

Try to run this code:


```
sage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)
sage: F,s = sr.polynomial_system()
```


and wait for it to terminate (~17s on my 2.33Ghz system) in a fresh SAGE session. The second run takes only 2s.


I profiled this with hotshot like this:


```
sage: import hotshot
sage: filename = "pythongrind.prof"
sage: prof = hotshot.Profile(filename, lineevents=1)
sage: prof.run("sr.polynomial_system()")
<hotshot.Profile instance at 0x414c11ec>
sage: prof.close()
```


and converted the result to cachegrind/calltree format


```
hotshot2calltree -o cachegrind.out.42 pythongrind.prof
```


to inspect the result with kcachegrind. Apparently, both `sr.round_polynomials` and `sr.key_schedule_polynomials` call `MatrixSpace.get_action_impl` which in turn calls `pushout` which calls `construction_tower`. `construction_tower` creates *7164* polynomial rings and this ring construction takes up 85% of the entire runtime. 

So apparently the most time is spent in coercion (which also explains the better runtime for the second run) and I believe this is due to a bug.


Issue created by migration from https://trac.sagemath.org/ticket/1046





---

archive/issue_comments_006363.json:
```json
{
    "body": "I tracked this down a bit more:\n\n\n```\nsage: n = 296\nsage: P = PolynomialRing(GF(2),n,'x')\nsage: v = vector(P,100)\nsage: A = matrix(P,100,100)\n\n# this time depends on $n$ above\n\nsage: %time _ = A*v\nCPU times: user 0.53 s, sys: 0.00 s, total: 0.53 s\nWall time: 0.53\n\nsage: %time _ = A*v\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n```\n",
    "created_at": "2007-11-01T11:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6363",
    "user": "malb"
}
```

I tracked this down a bit more:


```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = vector(P,100)
sage: A = matrix(P,100,100)

# this time depends on $n$ above

sage: %time _ = A*v
CPU times: user 0.53 s, sys: 0.00 s, total: 0.53 s
Wall time: 0.53

sage: %time _ = A*v
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
```




---

archive/issue_comments_006364.json:
```json
{
    "body": "Some more hints:\n\nFirst try:\n\n\n```\nsage: n = 296\nsage: P = PolynomialRing(GF(2),n,'x')\nsage: v = matrix(P,100,1)\nsage: A = matrix(P,100,100)\nsage: time _ = A*v\nCPU times: user 0.69 s, sys: 0.03 s, total: 0.72 s\nWall time: 0.75\n```\n\n\nthen restart Sage and try:\n\n\n```\nsage: n = 296\nsage: P = PolynomialRing(GF(2),n,'x')\nsage: v = matrix(P,100,1)\nsage: A = matrix(P,100,100)\nsage: time _ = A._multiply_classical(v)\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\n```\n",
    "created_at": "2007-11-01T11:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6364",
    "user": "malb"
}
```

Some more hints:

First try:


```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = matrix(P,100,1)
sage: A = matrix(P,100,100)
sage: time _ = A*v
CPU times: user 0.69 s, sys: 0.03 s, total: 0.72 s
Wall time: 0.75
```


then restart Sage and try:


```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = matrix(P,100,1)
sage: A = matrix(P,100,100)
sage: time _ = A._multiply_classical(v)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
```




---

archive/issue_comments_006365.json:
```json
{
    "body": "I am pretty sure this is because the coercion model tries to compute the construction tower and \"pushout\" one-variable at a time. This is to support stuff like\n\n\n```\nsage: ZZ['x,y,z'].gen(1) + QQ['y'].gen(0)\n2*y\n```\n\n\nOf course it is bad when you have multi-variate polynomials in 100's of variables...",
    "created_at": "2007-11-09T22:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6365",
    "user": "robertwb"
}
```

I am pretty sure this is because the coercion model tries to compute the construction tower and "pushout" one-variable at a time. This is to support stuff like


```
sage: ZZ['x,y,z'].gen(1) + QQ['y'].gen(0)
2*y
```


Of course it is bad when you have multi-variate polynomials in 100's of variables...



---

archive/issue_comments_006366.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-26T20:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6366",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006367.json:
```json
{
    "body": "This has been fixed--but it may be difficult to pull out of the massive coercion changes that David Roe and I are in the middle of doing. \n\nSee #1283",
    "created_at": "2007-11-26T20:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6367",
    "user": "robertwb"
}
```

This has been fixed--but it may be difficult to pull out of the massive coercion changes that David Roe and I are in the middle of doing. 

See #1283



---

archive/issue_comments_006368.json:
```json
{
    "body": "This bug is still present in Sage 3.1.1.:\n\n\n```\nsage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)\nsage: time F,s = sr.polynomial_system()\nCPU times: user 53.67 s, sys: 1.30 s, total: 54.97 s\nWall time: 54.94 s\nsage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)\nsage: time F,s = sr.polynomial_system()\nCPU times: user 8.53 s, sys: 0.29 s, total: 8.82 s\nWall time: 8.81 s\n```\n\n\nThe times were obtained on sage.math.",
    "created_at": "2008-08-18T16:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6368",
    "user": "malb"
}
```

This bug is still present in Sage 3.1.1.:


```
sage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)
sage: time F,s = sr.polynomial_system()
CPU times: user 53.67 s, sys: 1.30 s, total: 54.97 s
Wall time: 54.94 s
sage: sr = mq.SR(4,4,4,8, aes_mode=True, star=True, allow_zero_inversions=True)
sage: time F,s = sr.polynomial_system()
CPU times: user 8.53 s, sys: 0.29 s, total: 8.82 s
Wall time: 8.81 s
```


The times were obtained on sage.math.



---

archive/issue_comments_006369.json:
```json
{
    "body": "This is because the whole of the coercion branch was not merged over, just the core. I'll put merging this in up on the priority queue now that 3.1 has the underlying model.",
    "created_at": "2008-08-18T16:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6369",
    "user": "robertwb"
}
```

This is because the whole of the coercion branch was not merged over, just the core. I'll put merging this in up on the priority queue now that 3.1 has the underlying model.



---

archive/issue_comments_006370.json:
```json
{
    "body": "Attachment [1046-mpoly-coerce-speed.patch](tarball://root/attachments/some-uuid/ticket1046/1046-mpoly-coerce-speed.patch) by robertwb created at 2008-10-16 20:39:35\n\nThe attached patch should resolve this issue.",
    "created_at": "2008-10-16T20:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6370",
    "user": "robertwb"
}
```

Attachment [1046-mpoly-coerce-speed.patch](tarball://root/attachments/some-uuid/ticket1046/1046-mpoly-coerce-speed.patch) by robertwb created at 2008-10-16 20:39:35

The attached patch should resolve this issue.



---

archive/issue_comments_006371.json:
```json
{
    "body": "It improves the doctest run from 1100 seconds to\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0$ ./sage -t -long devel/sage/sage/crypto/mq/sr.py\nsage -t -long devel/sage/sage/crypto/mq/sr.py                \n\t [684.8 s]\n```\n\nI am doctesting with this patch applied. \n\nCheers,\n\nMichael",
    "created_at": "2008-10-17T20:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6371",
    "user": "mabshoff"
}
```

It improves the doctest run from 1100 seconds to

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha0$ ./sage -t -long devel/sage/sage/crypto/mq/sr.py
sage -t -long devel/sage/sage/crypto/mq/sr.py                
	 [684.8 s]
```

I am doctesting with this patch applied. 

Cheers,

Michael



---

archive/issue_comments_006372.json:
```json
{
    "body": "Robert,\n\nI guess the patch still needs some work :(\n\n```\n\tsage -t -long devel/sage/sage/structure/parent.pyx # 1 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 8 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 37 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 10 doctests failed\n\tsage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 9 doctests failed\n\tsage -t -long devel/sage/sage/modules/free_quadratic_module.py # 3 doctests failed\n\tsage -t -long devel/sage/sage/modules/free_module.py # 6 doctests failed\n\tsage -t -long devel/sage/sage/modular/modsym/space.py # 4 doctests failed\n\tsage -t -long devel/sage/sage/modular/modsym/ambient.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/modular/abvar/torsion_subgroup.py # 5 doctests failed\n\tsage -t -long devel/sage/sage/modular/abvar/cuspidal_subgroup.py # 4 doctests failed\n\tsage -t -long devel/sage/sage/modular/abvar/finite_subgroup.py # 21 doctests failed\n\tsage -t -long devel/sage/sage/modular/abvar/morphism.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed\n\tsage -t -long devel/sage/sage/matrix/matrix_real_double_dense.pyx # 3 doctests failed\n```\n\nI hope you had a good flight home from SD 10.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-17T21:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6372",
    "user": "mabshoff"
}
```

Robert,

I guess the patch still needs some work :(

```
	sage -t -long devel/sage/sage/structure/parent.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 8 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 37 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 10 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 9 doctests failed
	sage -t -long devel/sage/sage/modules/free_quadratic_module.py # 3 doctests failed
	sage -t -long devel/sage/sage/modules/free_module.py # 6 doctests failed
	sage -t -long devel/sage/sage/modular/modsym/space.py # 4 doctests failed
	sage -t -long devel/sage/sage/modular/modsym/ambient.py # 2 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/torsion_subgroup.py # 5 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/cuspidal_subgroup.py # 4 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/finite_subgroup.py # 21 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/morphism.py # 2 doctests failed
	sage -t -long devel/sage/sage/modular/abvar/abvar.py # 10 doctests failed
	sage -t -long devel/sage/sage/matrix/matrix_real_double_dense.pyx # 3 doctests failed
```

I hope you had a good flight home from SD 10.

Cheers,

Michael



---

archive/issue_comments_006373.json:
```json
{
    "body": "One more data point to the above remark malb did. With the patch applied:\n\n```\nsage: n = 296\nsage: P = PolynomialRing(GF(2),n,'x')\nsage: v = vector(P,100)\nsage: A = matrix(P,100,100)\nsage: %time _ = A*v\nCPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s\nWall time: 0.04 s\nsage: %time _ = A*v\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n```\n\nSo there is more than an order of magnitude improvement here :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-17T21:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6373",
    "user": "mabshoff"
}
```

One more data point to the above remark malb did. With the patch applied:

```
sage: n = 296
sage: P = PolynomialRing(GF(2),n,'x')
sage: v = vector(P,100)
sage: A = matrix(P,100,100)
sage: %time _ = A*v
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04 s
sage: %time _ = A*v
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```

So there is more than an order of magnitude improvement here :)

Cheers,

Michael



---

archive/issue_comments_006374.json:
```json
{
    "body": "Oh, I didn't test -t -long. I'll look into that.",
    "created_at": "2008-10-18T17:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6374",
    "user": "robertwb"
}
```

Oh, I didn't test -t -long. I'll look into that.



---

archive/issue_comments_006375.json:
```json
{
    "body": "Attachment [1046-fixes.patch](tarball://root/attachments/some-uuid/ticket1046/1046-fixes.patch) by robertwb created at 2008-10-21 17:34:42",
    "created_at": "2008-10-21T17:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6375",
    "user": "robertwb"
}
```

Attachment [1046-fixes.patch](tarball://root/attachments/some-uuid/ticket1046/1046-fixes.patch) by robertwb created at 2008-10-21 17:34:42



---

archive/issue_comments_006376.json:
```json
{
    "body": "I figured out what it was, due to some re-factoring a line got lost and that was raising a type error in the coercion discovery. Fixed.",
    "created_at": "2008-10-21T17:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6376",
    "user": "robertwb"
}
```

I figured out what it was, due to some re-factoring a line got lost and that was raising a type error in the coercion discovery. Fixed.



---

archive/issue_comments_006377.json:
```json
{
    "body": "Doctests pass, mhansen has also looked over the patch and has given it a positive review pending doctests in IRC :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-25T22:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6377",
    "user": "mabshoff"
}
```

Doctests pass, mhansen has also looked over the patch and has given it a positive review pending doctests in IRC :)

Cheers,

Michael



---

archive/issue_comments_006378.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-25T22:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6378",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006379.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-25T22:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6379",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_comments_006380.json:
```json
{
    "body": "+1 from me.",
    "created_at": "2008-10-25T22:05:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1046#issuecomment-6380",
    "user": "mhansen"
}
```

+1 from me.
