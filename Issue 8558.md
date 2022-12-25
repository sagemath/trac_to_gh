# Issue 8558: Make gcd use pari for univariate polynomial rings over number fields

archive/issues_008558.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @slel\n\nKeywords: gcd, pari, number field\n\nQuestion arised here,\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/0f5b029970e1a4e2/fcec7d0e35474fbd#fcec7d0e35474fbd\n\nunivariate gcd is performed using euclidean algorithm, which causes explosion of coefficients and is slow but for trivial examples. Instead we should use pari that performs better.\n\n1.- Add a _pari_ function for absolute number fields taht work\n\n2.- Add gcd using pari for absolute number fields\n\n3.- For relative number fields, pass to an absolute representation. This may be slow. But for the cases where this is slow the current implementation may be unfeasible.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8558\n\n",
    "created_at": "2010-03-18T17:14:43Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Make gcd use pari for univariate polynomial rings over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8558",
    "user": "https://github.com/lftabera"
}
```
Assignee: @aghitza

CC:  @slel

Keywords: gcd, pari, number field

Question arised here,

http://groups.google.com/group/sage-devel/browse_thread/thread/0f5b029970e1a4e2/fcec7d0e35474fbd#fcec7d0e35474fbd

univariate gcd is performed using euclidean algorithm, which causes explosion of coefficients and is slow but for trivial examples. Instead we should use pari that performs better.

1.- Add a _pari_ function for absolute number fields taht work

2.- Add gcd using pari for absolute number fields

3.- For relative number fields, pass to an absolute representation. This may be slow. But for the cases where this is slow the current implementation may be unfeasible.

Issue created by migration from https://trac.sagemath.org/ticket/8558





---

archive/issue_comments_077296.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-18T17:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77296",
    "user": "https://github.com/lftabera"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_077297.json:
```json
{
    "body": "Changing keywords from \"gcd, pari, number field\" to \"gcd, pari, ntl, number field\".",
    "created_at": "2010-03-27T19:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77297",
    "user": "https://github.com/lftabera"
}
```

Changing keywords from "gcd, pari, number field" to "gcd, pari, ntl, number field".



---

archive/issue_comments_077298.json:
```json
{
    "body": "Attachment [13911.patch](tarball://root/attachments/some-uuid/ticket8558/13911.patch) by @lftabera created at 2010-03-27 19:15:04\n\nThe pari algorithm is not fast enough. I have implemented a modular algorithm using ntl.\n\nThe patch needs doctest and integration in sage (it is, right now, a separate function).\n\nIt adds a new function modular_gcd\n\nTo test it, apply the patch and\n\nfrom sage.rings.polynomial.polynomial_absolute_number_field import modular_gcd\n\nSome timmings: (800 Mhz i386 linux, 1Gb ram)\n\n\n```\nsage: N.<a>=NumberField(x^3 -123)         \nsage: K.<t>=N[]                           \nsage: f=K.random_element(degree=2)        \nsage: g1=K.random_element(degree=15)      \nsage: g2=K.random_element(degree=15)      \nsage: h1=f*g1                             \nsage: h2=f*g2                             \nsage: %time modular_gcd(h1,h2,'pari')     \nCPU times: user 0.30 s, sys: 0.00 s, total: 0.30 s\nWall time: 0.31 s                                 \nt^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203\nsage: %time modular_gcd(h1,h2)                                                                                \nCPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s                                                            \nWall time: 0.12 s                                                                                             \nt^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203\nsage: %time modular_gcd(h1,h2,'euclidean')                                                                    \nCPU times: user 11.28 s, sys: 0.05 s, total: 11.33 s                                                          \nWall time: 12.21 s                                                                                            \nt^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203\n```\n\n\n\n```\nsage: N.<a>=NumberField(x^10 - 123)\nsage: K.<t>=N[]\nsage: f=K.random_element(degree=2)\nsage: g1=K.random_element(degree=15)\nsage: g2=K.random_element(degree=15)\nsage: h1=f*g1\nsage: h2=f*g2\nsage: %time l=modular_gcd(h1,h2,'pari')\nCPU times: user 30.06 s, sys: 0.02 s, total: 30.07 s\nWall time: 32.15 s\nsage: %time l=modular_gcd(h1,h2,'modular')\nCPU times: user 0.43 s, sys: 0.00 s, total: 0.43 s\nWall time: 0.47 s\n```\n",
    "created_at": "2010-03-27T19:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77298",
    "user": "https://github.com/lftabera"
}
```

Attachment [13911.patch](tarball://root/attachments/some-uuid/ticket8558/13911.patch) by @lftabera created at 2010-03-27 19:15:04

The pari algorithm is not fast enough. I have implemented a modular algorithm using ntl.

The patch needs doctest and integration in sage (it is, right now, a separate function).

It adds a new function modular_gcd

To test it, apply the patch and

from sage.rings.polynomial.polynomial_absolute_number_field import modular_gcd

Some timmings: (800 Mhz i386 linux, 1Gb ram)


```
sage: N.<a>=NumberField(x^3 -123)         
sage: K.<t>=N[]                           
sage: f=K.random_element(degree=2)        
sage: g1=K.random_element(degree=15)      
sage: g2=K.random_element(degree=15)      
sage: h1=f*g1                             
sage: h2=f*g2                             
sage: %time modular_gcd(h1,h2,'pari')     
CPU times: user 0.30 s, sys: 0.00 s, total: 0.30 s
Wall time: 0.31 s                                 
t^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203
sage: %time modular_gcd(h1,h2)                                                                                
CPU times: user 0.10 s, sys: 0.00 s, total: 0.10 s                                                            
Wall time: 0.12 s                                                                                             
t^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203
sage: %time modular_gcd(h1,h2,'euclidean')                                                                    
CPU times: user 11.28 s, sys: 0.05 s, total: 11.33 s                                                          
Wall time: 12.21 s                                                                                            
t^2 + (-35396/663609*a^2 + 92498/663609*a + 1750733/663609)*t - 1312/663609*a^2 + 3026/221203*a + 66060/221203
```



```
sage: N.<a>=NumberField(x^10 - 123)
sage: K.<t>=N[]
sage: f=K.random_element(degree=2)
sage: g1=K.random_element(degree=15)
sage: g2=K.random_element(degree=15)
sage: h1=f*g1
sage: h2=f*g2
sage: %time l=modular_gcd(h1,h2,'pari')
CPU times: user 30.06 s, sys: 0.02 s, total: 30.07 s
Wall time: 32.15 s
sage: %time l=modular_gcd(h1,h2,'modular')
CPU times: user 0.43 s, sys: 0.00 s, total: 0.43 s
Wall time: 0.47 s
```




---

archive/issue_comments_077299.json:
```json
{
    "body": "Here there is a cleaner patch.\n\nThe patch adds a new class of univariate polynomials whose ground field is an absolute number field. There is a new _gcd method for this class. It actually implements several approaches to the modular gcd algorithm:\n\nLangemyr-McCallum algorithm\nEncarnacion\na mixture of the two previous (default)\n\nmoreover, a call to pari method and the old Euclidean method.\n\nI think that there should be only one modular algorithm, but, as usual, there are cases in which any of them beats the others. So suggestions are welcome. It should probably be Encarnacion or the mixture of boths\n\nsome timmings for harder problems:\n\n\n\n```\nsage: N = NumberField(ZZ[x].random_element(15).monic(),'a')    \nsage: K = N[x]\nsage: f = K.random_element(100)\nsage: g1 = K.random_element(100)\nsage: g2 = K.random_element(100)\nsage: g1 *= f\nsage: g2 *= f\nsage: %time _=gcd(g1,g2)\nCPU times: user 7.32 s, sys: 0.02 s, total: 7.34 s\nWall time: 7.42 s\n```\n\n\nThis example with the old implementation or even pari is unfeasible.",
    "created_at": "2010-06-22T15:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77299",
    "user": "https://github.com/lftabera"
}
```

Here there is a cleaner patch.

The patch adds a new class of univariate polynomials whose ground field is an absolute number field. There is a new _gcd method for this class. It actually implements several approaches to the modular gcd algorithm:

Langemyr-McCallum algorithm
Encarnacion
a mixture of the two previous (default)

moreover, a call to pari method and the old Euclidean method.

I think that there should be only one modular algorithm, but, as usual, there are cases in which any of them beats the others. So suggestions are welcome. It should probably be Encarnacion or the mixture of boths

some timmings for harder problems:



```
sage: N = NumberField(ZZ[x].random_element(15).monic(),'a')    
sage: K = N[x]
sage: f = K.random_element(100)
sage: g1 = K.random_element(100)
sage: g2 = K.random_element(100)
sage: g1 *= f
sage: g2 *= f
sage: %time _=gcd(g1,g2)
CPU times: user 7.32 s, sys: 0.02 s, total: 7.34 s
Wall time: 7.42 s
```


This example with the old implementation or even pari is unfeasible.



---

archive/issue_comments_077300.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-22T15:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77300",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077301.json:
```json
{
    "body": "- Improved documentation\n- Eliminated an improvement in a function that hos nothing to do with the ticket",
    "created_at": "2010-06-24T14:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77301",
    "user": "https://github.com/lftabera"
}
```

- Improved documentation
- Eliminated an improvement in a function that hos nothing to do with the ticket



---

archive/issue_comments_077302.json:
```json
{
    "body": "Added the method also for number fields of degree 1 using Flint in this special case",
    "created_at": "2010-06-26T10:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77302",
    "user": "https://github.com/lftabera"
}
```

Added the method also for number fields of degree 1 using Flint in this special case



---

archive/issue_comments_077303.json:
```json
{
    "body": "Attachment [14371.patch](tarball://root/attachments/some-uuid/ticket8558/14371.patch) by @lftabera created at 2010-09-14 13:20:27\n\nNow that #4000 has possitive review, I raise the priority of this one.\n\nUpdated patch to work in 4.5.3\n\nNow, it works also for relative number fields, passing to an absolute representation and performing there the computations. This is not optimal but it is usable.\n\nIf the extension of the field is one, then the gcd of QQ[x] is used wich is faster.",
    "created_at": "2010-09-14T13:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77303",
    "user": "https://github.com/lftabera"
}
```

Attachment [14371.patch](tarball://root/attachments/some-uuid/ticket8558/14371.patch) by @lftabera created at 2010-09-14 13:20:27

Now that #4000 has possitive review, I raise the priority of this one.

Updated patch to work in 4.5.3

Now, it works also for relative number fields, passing to an absolute representation and performing there the computations. This is not optimal but it is usable.

If the extension of the field is one, then the gcd of QQ[x] is used wich is faster.



---

archive/issue_comments_077304.json:
```json
{
    "body": "Attachment [trac-5885.patch](tarball://root/attachments/some-uuid/ticket8558/trac-5885.patch) by @JohnCremona created at 2010-10-29 19:37:24\n\nI can confirm that the patch applies fine to 4.6.rc0 and all tests (including long) pass.\n\nThere are some minor problems with the documentation (just punctuation) -- now I am studying the code, since this looks like very useful functionality!",
    "created_at": "2010-10-29T19:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77304",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac-5885.patch](tarball://root/attachments/some-uuid/ticket8558/trac-5885.patch) by @JohnCremona created at 2010-10-29 19:37:24

I can confirm that the patch applies fine to 4.6.rc0 and all tests (including long) pass.

There are some minor problems with the documentation (just punctuation) -- now I am studying the code, since this looks like very useful functionality!



---

archive/issue_comments_077305.json:
```json
{
    "body": "Some clean in the documentation, reorder of the methods (methods after the classes of the file) and a couple of small bugs (honor the method option for relative fields and duplicated code for degree 1 extensions). Rename correctly the patch.\n\nApply: trac-8558.patch\n\nTry new buildbot  :)",
    "created_at": "2010-12-04T12:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77305",
    "user": "https://github.com/lftabera"
}
```

Some clean in the documentation, reorder of the methods (methods after the classes of the file) and a couple of small bugs (honor the method option for relative fields and duplicated code for degree 1 extensions). Rename correctly the patch.

Apply: trac-8558.patch

Try new buildbot  :)



---

archive/issue_comments_077306.json:
```json
{
    "body": "Apply trac-8558.patch\n\n(I think such messages have to come *after* the patch is uploaded)",
    "created_at": "2011-01-19T16:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77306",
    "user": "https://github.com/loefflerd"
}
```

Apply trac-8558.patch

(I think such messages have to come *after* the patch is uploaded)



---

archive/issue_comments_077307.json:
```json
{
    "body": "avoid next_prime, better exceptions",
    "created_at": "2011-03-28T10:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77307",
    "user": "https://github.com/lftabera"
}
```

avoid next_prime, better exceptions



---

archive/issue_comments_077308.json:
```json
{
    "body": "Attachment [trac-8558.patch](tarball://root/attachments/some-uuid/ticket8558/trac-8558.patch) by @lftabera created at 2011-03-28 10:46:13",
    "created_at": "2011-03-28T10:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77308",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac-8558.patch](tarball://root/attachments/some-uuid/ticket8558/trac-8558.patch) by @lftabera created at 2011-03-28 10:46:13



---

archive/issue_comments_077309.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-04-29T13:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77309",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_077310.json:
```json
{
    "body": "Hi, I don't know much about fast computation in polynomial rings over number fields. However, I'm wondering why you have this bias towards functions as opposed to methods? For example, `lift_pm` looks like it should be a method on `p` instead of a function? Perhaps the same applies to the gcd functions? Or am I missing something?",
    "created_at": "2011-04-29T13:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77310",
    "user": "https://github.com/malb"
}
```

Hi, I don't know much about fast computation in polynomial rings over number fields. However, I'm wondering why you have this bias towards functions as opposed to methods? For example, `lift_pm` looks like it should be a method on `p` instead of a function? Perhaps the same applies to the gcd functions? Or am I missing something?



---

archive/issue_comments_077311.json:
```json
{
    "body": "No bias intended. lift_pm can be a method and probably in more classes than polynomials in NTL.\n\nI am reading again the code and it looks awful now. I think there are too many gcd alternatives with little gainamong them.\n\nI will update the code.",
    "created_at": "2011-05-12T11:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77311",
    "user": "https://github.com/lftabera"
}
```

No bias intended. lift_pm can be a method and probably in more classes than polynomials in NTL.

I am reading again the code and it looks awful now. I think there are too many gcd alternatives with little gainamong them.

I will update the code.



---

archive/issue_comments_077312.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-06-10T11:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77312",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_077313.json:
```json
{
    "body": "Now the functions are methods.\n\nlift_to_poly_ZZ and lift_to_poly_QQ are methods of ntl_ZZ_pEX\n\nlift_pm is a method of ntl_ZZ_p\n\nStill, I have left a lift_pm function in sage.rings.arith I think it is good for educational purposes in modular algorithms.\n\nI have eliminated pure Encarnacion and pure Langemyr_McCallum methods. There is no real benefit compared to the extra code they add.",
    "created_at": "2011-06-10T11:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77313",
    "user": "https://github.com/lftabera"
}
```

Now the functions are methods.

lift_to_poly_ZZ and lift_to_poly_QQ are methods of ntl_ZZ_pEX

lift_pm is a method of ntl_ZZ_p

Still, I have left a lift_pm function in sage.rings.arith I think it is good for educational purposes in modular algorithms.

I have eliminated pure Encarnacion and pure Langemyr_McCallum methods. There is no real benefit compared to the extra code they add.



---

archive/issue_comments_077314.json:
```json
{
    "body": "Apply: trac-8558.2.patch",
    "created_at": "2011-06-10T11:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77314",
    "user": "https://github.com/lftabera"
}
```

Apply: trac-8558.2.patch



---

archive/issue_comments_077315.json:
```json
{
    "body": "rebase against 4.7.1",
    "created_at": "2011-08-24T17:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77315",
    "user": "https://github.com/lftabera"
}
```

rebase against 4.7.1



---

archive/issue_comments_077316.json:
```json
{
    "body": "Apply: trac-8558.2.patch",
    "created_at": "2011-08-25T09:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77316",
    "user": "https://github.com/lftabera"
}
```

Apply: trac-8558.2.patch



---

archive/issue_comments_077317.json:
```json
{
    "body": "Several comments:\n1. Why the name `lift_pm()`?  In PARI, this function is called `centerlift()` which is more understandable in my opinion.  On the other hand, having the name *begin* with `lift` is more friendly for TAB-completion, so why not `lift_centered` or something?\n2. A special class for polynomials over number fields looks like a good idea, but please put it in a separate file `polynomial_number_field.pyx` instead of adding to `polynomial_element_generic.pyx`.\n3. I have a hard time understand the text below. What is `c`? What is `n`? Probably \"reduction\" is a better word than \"project\". And I also think the name `K` for a polynomial ring is badly chosen:\n\n```\n    def lift_to_poly_QQ(self,K):\n        \"\"\"\n        Compute a lift of poly to K.\n            \n        INPUT:\n    \n        - K: an univariate polynomial ring over an absolute number field QQ[a].\n        In order to make sense of this algorithm, the minimum polynomial of 'a'\n        should project onto `c` modulo `m`.\n      \n        OUTPUT:\n    \n        -A polynomial in QQ[a] such that its projection coefficientwise is poly.\n        This algorithm uses rational reconstruction, so it may fail.\n```\n\n4. Why `_gcd()` instead of `gcd()`?\n5. Add some tests using the global `gcd()` function instead of always calling your `_gcd()` method.\n6. Thanks to #11904, the line\n {{{\n h1 = pari([coeff._pari_('y') for coeff in self.list()]).Polrev() \n }}}\n can be changed to\n {{{\n h1 = pari(self)\n }}}\n7. This looks very fishy:\n {{{\n #Experimental bound IMPROVE\n }}}\n8. With\n {{{\n p = p.next_prime(False)\n }}}\n do you mean\n {{{\n p = p.next_prime(proof=False)\n }}}\n which is much clearer?\n9. I believe the keyword argument `algoritm=` is usually used instead of `method =` (note also the spacing!).",
    "created_at": "2011-10-15T12:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77317",
    "user": "https://github.com/jdemeyer"
}
```

Several comments:
1. Why the name `lift_pm()`?  In PARI, this function is called `centerlift()` which is more understandable in my opinion.  On the other hand, having the name *begin* with `lift` is more friendly for TAB-completion, so why not `lift_centered` or something?
2. A special class for polynomials over number fields looks like a good idea, but please put it in a separate file `polynomial_number_field.pyx` instead of adding to `polynomial_element_generic.pyx`.
3. I have a hard time understand the text below. What is `c`? What is `n`? Probably "reduction" is a better word than "project". And I also think the name `K` for a polynomial ring is badly chosen:

```
    def lift_to_poly_QQ(self,K):
        """
        Compute a lift of poly to K.
            
        INPUT:
    
        - K: an univariate polynomial ring over an absolute number field QQ[a].
        In order to make sense of this algorithm, the minimum polynomial of 'a'
        should project onto `c` modulo `m`.
      
        OUTPUT:
    
        -A polynomial in QQ[a] such that its projection coefficientwise is poly.
        This algorithm uses rational reconstruction, so it may fail.
```

4. Why `_gcd()` instead of `gcd()`?
5. Add some tests using the global `gcd()` function instead of always calling your `_gcd()` method.
6. Thanks to #11904, the line
 {{{
 h1 = pari([coeff._pari_('y') for coeff in self.list()]).Polrev() 
 }}}
 can be changed to
 {{{
 h1 = pari(self)
 }}}
7. This looks very fishy:
 {{{
 #Experimental bound IMPROVE
 }}}
8. With
 {{{
 p = p.next_prime(False)
 }}}
 do you mean
 {{{
 p = p.next_prime(proof=False)
 }}}
 which is much clearer?
9. I believe the keyword argument `algoritm=` is usually used instead of `method =` (note also the spacing!).



---

archive/issue_comments_077318.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-15T12:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77318",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077319.json:
```json
{
    "body": "rebase 4.7.2 still needs work",
    "created_at": "2011-11-10T17:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77319",
    "user": "https://github.com/lftabera"
}
```

rebase 4.7.2 still needs work



---

archive/issue_comments_077320.json:
```json
{
    "body": "Back to business.\n\nI have updated the patch with Jeroen's suggestions. Still I have to do something with \n\n\n```\n#Experimental bound IMPROVE\np = ZZ(3+min(2**255, (max(map(abs,Bound.list())).n()**(0.4)).floor())).next_prime(proof=False)\n```\n\n\np is the first prime to perform a modular gcd. If p=2, we will have to use a lot of primes and will be inefficient. On the other hand, if p is too big, we lose the advantages of modular gcd. So we have to give a sane, intermediate default.\n\nThe prime above is based on some experiments I made two years ago, the idea is to use a prime such that we will have to use few modular gcd, but limiting our stating prime to the interval `[3, 2^255]`.\n\nIdeas welcomed.",
    "created_at": "2013-02-24T13:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77320",
    "user": "https://github.com/lftabera"
}
```

Back to business.

I have updated the patch with Jeroen's suggestions. Still I have to do something with 


```
#Experimental bound IMPROVE
p = ZZ(3+min(2**255, (max(map(abs,Bound.list())).n()**(0.4)).floor())).next_prime(proof=False)
```


p is the first prime to perform a modular gcd. If p=2, we will have to use a lot of primes and will be inefficient. On the other hand, if p is too big, we lose the advantages of modular gcd. So we have to give a sane, intermediate default.

The prime above is based on some experiments I made two years ago, the idea is to use a prime such that we will have to use few modular gcd, but limiting our stating prime to the interval `[3, 2^255]`.

Ideas welcomed.



---

archive/issue_comments_077321.json:
```json
{
    "body": "Apply trac-8558.2.patch",
    "created_at": "2013-02-24T18:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77321",
    "user": "https://github.com/lftabera"
}
```

Apply trac-8558.2.patch



---

archive/issue_comments_077322.json:
```json
{
    "body": "Still, we have to look for a sensible default starting prime p, but the rest of the ticket can be reviewed.\n\nFurther improvements for other tickets and for big degree polynomials (different tickets) could be\n\n* add a half-gcd algorithm for ntl_ZZ_p_EX class, ntl libraries do not provide one.\n* Improve a lot the test of having a gcd, remainder algorithm is slow.\n\nApply: trac-8558.2.patch",
    "created_at": "2013-03-02T15:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77322",
    "user": "https://github.com/lftabera"
}
```

Still, we have to look for a sensible default starting prime p, but the rest of the ticket can be reviewed.

Further improvements for other tickets and for big degree polynomials (different tickets) could be

* add a half-gcd algorithm for ntl_ZZ_p_EX class, ntl libraries do not provide one.
* Improve a lot the test of having a gcd, remainder algorithm is slow.

Apply: trac-8558.2.patch



---

archive/issue_comments_077323.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-03-02T15:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77323",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077324.json:
```json
{
    "body": "The patchbot wants to apply too many patches\n\nApply: trac-8558.2.patch",
    "created_at": "2013-03-02T17:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77324",
    "user": "https://github.com/lftabera"
}
```

The patchbot wants to apply too many patches

Apply: trac-8558.2.patch



---

archive/issue_comments_077325.json:
```json
{
    "body": "rebase to 5.8.beta2",
    "created_at": "2013-03-03T19:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77325",
    "user": "https://github.com/lftabera"
}
```

rebase to 5.8.beta2



---

archive/issue_comments_077326.json:
```json
{
    "body": "Attachment [trac-8558.2.patch](tarball://root/attachments/some-uuid/ticket8558/trac-8558.2.patch) by @lftabera created at 2013-03-03 20:02:49\n\nApply: trac-8558.2.patch",
    "created_at": "2013-03-03T20:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77326",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac-8558.2.patch](tarball://root/attachments/some-uuid/ticket8558/trac-8558.2.patch) by @lftabera created at 2013-03-03 20:02:49

Apply: trac-8558.2.patch



---

archive/issue_comments_077327.json:
```json
{
    "body": "Apply: trac-8558.2.2.patch",
    "created_at": "2013-03-08T20:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77327",
    "user": "https://github.com/lftabera"
}
```

Apply: trac-8558.2.2.patch



---

archive/issue_comments_077328.json:
```json
{
    "body": "Some quick comments:\n1. `_sig_on` and `_sig_off` are very deprecated and should be changed to `sig_on()` and `sig_off()` (#10115).\n2. The change \"somewhat\" -> \"somewha\" clearly is a mistake.\n3. [Documentation](http://sagemath.org/doc/developer/conventions.html#documentation-strings) and [library](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files) formatting must be fixed.\n4. Could you replace `centerlift` by `lift_centered` in `sage/rings/finite_rings/integer_mod.pyx` for consistency?\n5. As I already mentioned, replace `method =` by `algorithm=`\n6. Since `QQ` is a unique parent, replace `base_ring != QQ` by `base_ring is not QQ`.\n6. Remove `# There has to be a better way to do this, self.change_ring()` does not work.  I don't see any problem with that code.\n6. It is better to use a `**kwds` argument for `sparse` and `implementation` in\n\n```\ndef __init__(self, base_ring, name=\"x\", sparse=False, element_class=None, implementation=None)\n```\n",
    "created_at": "2013-03-13T14:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77328",
    "user": "https://github.com/jdemeyer"
}
```

Some quick comments:
1. `_sig_on` and `_sig_off` are very deprecated and should be changed to `sig_on()` and `sig_off()` (#10115).
2. The change "somewhat" -> "somewha" clearly is a mistake.
3. [Documentation](http://sagemath.org/doc/developer/conventions.html#documentation-strings) and [library](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files) formatting must be fixed.
4. Could you replace `centerlift` by `lift_centered` in `sage/rings/finite_rings/integer_mod.pyx` for consistency?
5. As I already mentioned, replace `method =` by `algorithm=`
6. Since `QQ` is a unique parent, replace `base_ring != QQ` by `base_ring is not QQ`.
6. Remove `# There has to be a better way to do this, self.change_ring()` does not work.  I don't see any problem with that code.
6. It is better to use a `**kwds` argument for `sparse` and `implementation` in

```
def __init__(self, base_ring, name="x", sparse=False, element_class=None, implementation=None)
```




---

archive/issue_comments_077329.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-03-16T22:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77329",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077330.json:
```json
{
    "body": "I have taken into acoount the suggestions. I have deprecated integer_mod.centerlift and have eliminated the PolynomialRing new classes, since they only differed from PolynomialRing_field in the element_class and ignored the sparse option.",
    "created_at": "2013-05-10T14:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77330",
    "user": "https://github.com/lftabera"
}
```

I have taken into acoount the suggestions. I have deprecated integer_mod.centerlift and have eliminated the PolynomialRing new classes, since they only differed from PolynomialRing_field in the element_class and ignored the sparse option.



---

archive/issue_comments_077331.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-05-10T14:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77331",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_020621.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20621"
}
```



---

archive/issue_comments_077332.json:
```json
{
    "body": "Attachment [trac-8558.2.2.patch](tarball://root/attachments/some-uuid/ticket8558/trac-8558.2.2.patch) by @lftabera created at 2013-12-20 12:28:14\n\nrebase to 5.13",
    "created_at": "2013-12-20T12:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77332",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac-8558.2.2.patch](tarball://root/attachments/some-uuid/ticket8558/trac-8558.2.2.patch) by @lftabera created at 2013-12-20 12:28:14

rebase to 5.13



---

archive/issue_comments_077333.json:
```json
{
    "body": "Apply: trac-8558.2.2.patch\u200b",
    "created_at": "2013-12-20T12:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77333",
    "user": "https://github.com/lftabera"
}
```

Apply: trac-8558.2.2.patch​



---

archive/issue_comments_077334.json:
```json
{
    "body": "Certainly looks in much better shape than it used to be, but I'm afraid I don't know enough NTL to completely review this. Why not split up this ticket in two? The first which adds the new classes and implements `gcd` via PARI and the second which implements the modular algorithm.",
    "created_at": "2014-01-06T16:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77334",
    "user": "https://github.com/jdemeyer"
}
```

Certainly looks in much better shape than it used to be, but I'm afraid I don't know enough NTL to completely review this. Why not split up this ticket in two? The first which adds the new classes and implements `gcd` via PARI and the second which implements the modular algorithm.



---

archive/issue_events_020622.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20622"
}
```



---

archive/issue_events_020623.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20623"
}
```



---

archive/issue_comments_077335.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-02-10T15:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77335",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077336.json:
```json
{
    "body": "I have split the ticket into three tickets for easier reviewer and to allow partial merging.",
    "created_at": "2014-02-10T16:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77336",
    "user": "https://github.com/lftabera"
}
```

I have split the ticket into three tickets for easier reviewer and to allow partial merging.



---

archive/issue_events_020624.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20624"
}
```



---

archive/issue_events_020625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20625"
}
```



---

archive/issue_comments_077337.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-07T14:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77337",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077338.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-08T10:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77338",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077339.json:
```json
{
    "body": "(I'm not sure if the merge conflict was caused by this ticket or one of its dependencies; I just reported what the patchbot told me.)\n\nI don't really have time to review any of this at the moment, but I agree with earlier reviewers that this looks like a very nice addition.  I was just wondering whether it would make sense to do this via a `NumberField._gcd_univariate_polynomial()` method as introduced by #13442.  On the one hand, this would mean you didn't have to introduce new classes (potentially many of them: we have absolute and relative number fields, quadratic fields, cyclotomic fields, sparse and dense polynomials, who knows what other distinctions we'll have in the future).  On the other hand, the code of this ticket has already been written and #13442 is still at `needs_work`, so it probably isn't worth the effort for now.",
    "created_at": "2014-05-08T14:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77339",
    "user": "https://github.com/pjbruin"
}
```

(I'm not sure if the merge conflict was caused by this ticket or one of its dependencies; I just reported what the patchbot told me.)

I don't really have time to review any of this at the moment, but I agree with earlier reviewers that this looks like a very nice addition.  I was just wondering whether it would make sense to do this via a `NumberField._gcd_univariate_polynomial()` method as introduced by #13442.  On the one hand, this would mean you didn't have to introduce new classes (potentially many of them: we have absolute and relative number fields, quadratic fields, cyclotomic fields, sparse and dense polynomials, who knows what other distinctions we'll have in the future).  On the other hand, the code of this ticket has already been written and #13442 is still at `needs_work`, so it probably isn't worth the effort for now.



---

archive/issue_comments_077340.json:
```json
{
    "body": "Thanks anyway, this made me update my local branches :)\n\nThe code is ok, but the branch of patches is a little mess due to my poor \"git-fu\". As of now I think that it is more important to get the dependencies merged, they are much simpler and would allow to prepare cleaner patches for this ticket.\n\nConcerning #13442, I had in mind an implementation of these rings as in ticket #10591, so it would be better to have different classes for polynomials over number fields. The long term goal would be to have nice multiple extensions without the need of computing a primitive element for basic arithmetic, IMO it would be faster than using singular (cf. #9541).",
    "created_at": "2014-05-09T07:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77340",
    "user": "https://github.com/lftabera"
}
```

Thanks anyway, this made me update my local branches :)

The code is ok, but the branch of patches is a little mess due to my poor "git-fu". As of now I think that it is more important to get the dependencies merged, they are much simpler and would allow to prepare cleaner patches for this ticket.

Concerning #13442, I had in mind an implementation of these rings as in ticket #10591, so it would be better to have different classes for polynomials over number fields. The long term goal would be to have nice multiple extensions without the need of computing a primitive element for basic arithmetic, IMO it would be faster than using singular (cf. #9541).



---

archive/issue_events_020626.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20626"
}
```



---

archive/issue_events_020627.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20627"
}
```



---

archive/issue_comments_077341.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-16T16:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77341",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077342.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-21T12:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77342",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077343.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-05-22T10:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77343",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077344.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-12-03T17:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77344",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077345.json:
```json
{
    "body": "After so much time, I want to check if the code needs refactoring.",
    "created_at": "2015-12-03T17:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77345",
    "user": "https://github.com/lftabera"
}
```

After so much time, I want to check if the code needs refactoring.



---

archive/issue_comments_077346.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-02-23T15:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77346",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077347.json:
```json
{
    "body": "It works again with latest beta",
    "created_at": "2016-02-23T15:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77347",
    "user": "https://github.com/lftabera"
}
```

It works again with latest beta



---

archive/issue_comments_077348.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-02-23T15:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77348",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077349.json:
```json
{
    "body": "- `.. NOTE:` -> `.. NOTE::`\n\n- In the docstring of \"lift_to_poly_QQ\" it is written that \"it may fail with a ``ValueError`` exception.\". But there is only an example which gives an \"ArithmeticError\". So either fix the note or add a doctest.\n\n- you should do more typing in Cython file (with `cdef`). For example, `cdef list lifted = []`. It will help cython to speed up loops including the loops. And if I am not mistaken, this syntax `for 0 <= i < r` is equivalent to `for i in range(r)` which is more Python friendly.\n\n- the name `lift_to_poly_QQ` looks strange to me. What does the `QQ` stands for?\n\n- Could you provide more examples why the situation is it better with this new algorithm?",
    "created_at": "2016-03-16T13:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77349",
    "user": "https://github.com/videlec"
}
```

- `.. NOTE:` -> `.. NOTE::`

- In the docstring of "lift_to_poly_QQ" it is written that "it may fail with a ``ValueError`` exception.". But there is only an example which gives an "ArithmeticError". So either fix the note or add a doctest.

- you should do more typing in Cython file (with `cdef`). For example, `cdef list lifted = []`. It will help cython to speed up loops including the loops. And if I am not mistaken, this syntax `for 0 <= i < r` is equivalent to `for i in range(r)` which is more Python friendly.

- the name `lift_to_poly_QQ` looks strange to me. What does the `QQ` stands for?

- Could you provide more examples why the situation is it better with this new algorithm?



---

archive/issue_comments_077350.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-15T08:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77350",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077351.json:
```json
{
    "body": "- I have added mor cdef, however, I cannot do that in polynomial_number_field since the class inherist from a python class. I was not able to cdef, rings or number field elements. The latter has at least two classes and I was not able to cdef the common parent.\n- I have fixed types, more verbose method names, clean unusued variables.\n- modular method can be further improved for high degree using half-gcd algorithms in ntl.\n\n- Some more examples:\n\nPari seems to use either Euclid or some subresultant variation. I would expect pari to perform better when the gcd is big with respect to the degree of the inputs. Or, when the input has small degree.\n\nThe polynomials are generated with K.random_element() so small coefficients. This benefits pari.\n\nSmall extension, not impressing except for huge polynomials\n\n\n```\nsage: K=QQ[I]['x']\n```\n\n\n\n```\ndeg f, deg g, deg gcd, timeit pari, timeit modular\n2, 2, 0, 111 \u00b5s, 176 \u00b5s\n2, 2, 1, 173 \u00b5s, 360 \u00b5s\n2, 2, 2, 185 \u00b5s, 466 \u00b5s\n\n100, 100, 0, 30.6 ms, 7.06 ms\n100, 100, 50, 22.5 ms, 34.7 ms\n100, 100, 100, 4.82 ms, 6.58 ms\n\n300, 300, 0, 1.8 s, 45.1 ms\n300, 300, 150, 534 ms, 201 ms\n300, 300, 300, 13.3 ms, 11.3 ms\n\n1000, 1000, 100, 2min 52s, 2.07 s\n```\n\n\nA degree 3, easy extension\n\n\n```\nsage: R=NumberField(x^3-2,'a')['x']\n```\n\n\n\n```\ndeg f, deg g, deg gcd, timeit pari, timeit modular\n2, 2, 0, 163 \u00b5s, 243 \u00b5s\n2, 2, 1, 239 \u00b5s, 597 \u00b5s\n2, 2, 2, 257 \u00b5s, 587 \u00b5s\n\n100, 100, 0, 19 s, 11.2 ms (1000x faster)\n100, 100, 50, 8.6 s, 47.3 ms (100x faster)\n100, 100, 100, 6.57 ms, 11.9 ms (2x slower)\n\n300, 300, 150, > 600 s, 403 ms\n```\n\n\nTu support my claim that big coefficients benefits modular\n\n\n```\nsage: K=QQ[I]['x']\nsage: f=K.random_element(2,10**10)\n```\n\n\n\n```\n100, 100, 0, 282 ms, 6.92 ms\n100, 100, 50, 117 ms, 15.4 ms\n100, 100, 100, 4.69 ms, 5.01 ms\n```\n",
    "created_at": "2016-07-15T11:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77351",
    "user": "https://github.com/lftabera"
}
```

- I have added mor cdef, however, I cannot do that in polynomial_number_field since the class inherist from a python class. I was not able to cdef, rings or number field elements. The latter has at least two classes and I was not able to cdef the common parent.
- I have fixed types, more verbose method names, clean unusued variables.
- modular method can be further improved for high degree using half-gcd algorithms in ntl.

- Some more examples:

Pari seems to use either Euclid or some subresultant variation. I would expect pari to perform better when the gcd is big with respect to the degree of the inputs. Or, when the input has small degree.

The polynomials are generated with K.random_element() so small coefficients. This benefits pari.

Small extension, not impressing except for huge polynomials


```
sage: K=QQ[I]['x']
```



```
deg f, deg g, deg gcd, timeit pari, timeit modular
2, 2, 0, 111 µs, 176 µs
2, 2, 1, 173 µs, 360 µs
2, 2, 2, 185 µs, 466 µs

100, 100, 0, 30.6 ms, 7.06 ms
100, 100, 50, 22.5 ms, 34.7 ms
100, 100, 100, 4.82 ms, 6.58 ms

300, 300, 0, 1.8 s, 45.1 ms
300, 300, 150, 534 ms, 201 ms
300, 300, 300, 13.3 ms, 11.3 ms

1000, 1000, 100, 2min 52s, 2.07 s
```


A degree 3, easy extension


```
sage: R=NumberField(x^3-2,'a')['x']
```



```
deg f, deg g, deg gcd, timeit pari, timeit modular
2, 2, 0, 163 µs, 243 µs
2, 2, 1, 239 µs, 597 µs
2, 2, 2, 257 µs, 587 µs

100, 100, 0, 19 s, 11.2 ms (1000x faster)
100, 100, 50, 8.6 s, 47.3 ms (100x faster)
100, 100, 100, 6.57 ms, 11.9 ms (2x slower)

300, 300, 150, > 600 s, 403 ms
```


Tu support my claim that big coefficients benefits modular


```
sage: K=QQ[I]['x']
sage: f=K.random_element(2,10**10)
```



```
100, 100, 0, 282 ms, 6.92 ms
100, 100, 50, 117 ms, 15.4 ms
100, 100, 100, 4.69 ms, 5.01 ms
```




---

archive/issue_comments_077352.json:
```json
{
    "body": "lift methods still need better documentation according to #18",
    "created_at": "2016-07-15T11:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77352",
    "user": "https://github.com/lftabera"
}
```

lift methods still need better documentation according to #18



---

archive/issue_comments_077353.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-07-15T11:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77353",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_077354.json:
```json
{
    "body": "If I were a pari developer reasing this, I would ask:  why not implement the algorithm in pari itself, rather than in Sage?",
    "created_at": "2016-07-15T12:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77354",
    "user": "https://github.com/JohnCremona"
}
```

If I were a pari developer reasing this, I would ask:  why not implement the algorithm in pari itself, rather than in Sage?



---

archive/issue_comments_077355.json:
```json
{
    "body": "I am not a pari developer, it would certainly benefit more people than an implementation in Sage. I thought about an implementation in ntl, but I do not touch C++ since 15 years ago. Flint would also be a good place to put a similar code.\n\nAccording to the documentation:\n\ngcd uses:\n\n* integers: use modified right-shift binary (\"plus-minus\" variant).\n\n* univariate polynomials with coefficients in the same number field (in particular rational): use modular gcd algorithm.\n\n* general polynomials: use the subresultant algorithm if coefficient explosion is likely (non modular coefficients).\n\nSo, it may be the case that we are not translating polynomials to the correct pari setting and so I get bad timings? It may be the case, in order not to compute the discriminant of the number field we are dealing with...",
    "created_at": "2016-07-15T13:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77355",
    "user": "https://github.com/lftabera"
}
```

I am not a pari developer, it would certainly benefit more people than an implementation in Sage. I thought about an implementation in ntl, but I do not touch C++ since 15 years ago. Flint would also be a good place to put a similar code.

According to the documentation:

gcd uses:

* integers: use modified right-shift binary ("plus-minus" variant).

* univariate polynomials with coefficients in the same number field (in particular rational): use modular gcd algorithm.

* general polynomials: use the subresultant algorithm if coefficient explosion is likely (non modular coefficients).

So, it may be the case that we are not translating polynomials to the correct pari setting and so I get bad timings? It may be the case, in order not to compute the discriminant of the number field we are dealing with...



---

archive/issue_comments_077356.json:
```json
{
    "body": "One thing to watch when comparing timings with pari is that when Sage calls pari to compute class number s and units in a number field, unless Proof=False it assumes no hypothesis (like GRH) so is often a lot slower than the same thing done in pari, where the default is to assume everything (and you can ask for certification later).  This should be as issue if you only do basic number field arithmetic, but if you do anything which requires knowing the units or class group it can be quite significant.  You might want to try setting Proof=False in Sage and seeing if your timings change.",
    "created_at": "2016-07-15T13:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77356",
    "user": "https://github.com/JohnCremona"
}
```

One thing to watch when comparing timings with pari is that when Sage calls pari to compute class number s and units in a number field, unless Proof=False it assumes no hypothesis (like GRH) so is often a lot slower than the same thing done in pari, where the default is to assume everything (and you can ask for certification later).  This should be as issue if you only do basic number field arithmetic, but if you do anything which requires knowing the units or class group it can be quite significant.  You might want to try setting Proof=False in Sage and seeing if your timings change.



---

archive/issue_comments_077357.json:
```json
{
    "body": "It it is not that, I only need basic arithmetic, at most, pari could be interested in the  discriminant, but I am working in QQ[I] in my examples. Which should be easy. \n\nI have tried to write polynomials in pure gp as\n\n`f= Mod(3*y,y<sup>2-1)*x</sup>2+Mod(1,y<sup>2-1)*x+Mod(y,y</sup>2-1)`\n\nor as \n\n\n```\nw=quadgen(-4)\nf= 3*w*x^2+1*x+w\n```\n\n\nin both cases I get bad timing. Reading the documentation now to see how to deal with polynomials with number field coefficients in pari...",
    "created_at": "2016-07-15T14:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77357",
    "user": "https://github.com/lftabera"
}
```

It it is not that, I only need basic arithmetic, at most, pari could be interested in the  discriminant, but I am working in QQ[I] in my examples. Which should be easy. 

I have tried to write polynomials in pure gp as

`f= Mod(3*y,y<sup>2-1)*x</sup>2+Mod(1,y<sup>2-1)*x+Mod(y,y</sup>2-1)`

or as 


```
w=quadgen(-4)
f= 3*w*x^2+1*x+w
```


in both cases I get bad timing. Reading the documentation now to see how to deal with polynomials with number field coefficients in pari...



---

archive/issue_comments_077358.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-18T10:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77358",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077359.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-07-18T10:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77359",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077360.json:
```json
{
    "body": "It looks that Pari is not really using a modular algorithm...\n\nIn any case, I have fixed the documentation, I have also fixed some heuristic assumptions about the primes. Do not use proof=False and be more conservative about the size of the primes. In principle, with proof=False we could try a composite number such that the gcd in the residue ring success but some prime factors are good and some are bad. Not sure if this is possible. Also, chinese remainder could potentially fail, in this case I think that can only happens if the gcd is already unfeasible by any method. But let's be conservative and use only failproof methods.",
    "created_at": "2016-07-18T10:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77360",
    "user": "https://github.com/lftabera"
}
```

It looks that Pari is not really using a modular algorithm...

In any case, I have fixed the documentation, I have also fixed some heuristic assumptions about the primes. Do not use proof=False and be more conservative about the size of the primes. In principle, with proof=False we could try a composite number such that the gcd in the residue ring success but some prime factors are good and some are bad. Not sure if this is possible. Also, chinese remainder could potentially fail, in this case I think that can only happens if the gcd is already unfeasible by any method. But let's be conservative and use only failproof methods.



---

archive/issue_comments_077361.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-03-09T16:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77361",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077362.json:
```json
{
    "body": "Changing keywords from \"gcd, pari, ntl, number field\" to \"gcd, pari, ntl, number field, days94\".",
    "created_at": "2018-06-28T09:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77362",
    "user": "https://github.com/lftabera"
}
```

Changing keywords from "gcd, pari, ntl, number field" to "gcd, pari, ntl, number field, days94".



---

archive/issue_comments_077363.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-06-28T16:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77363",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077364.json:
```json
{
    "body": "This code uses ntl ZZ_pEX while it should use the faster lzz_pEX for word-sized primes.",
    "created_at": "2018-07-07T23:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77364",
    "user": "https://github.com/lftabera"
}
```

This code uses ntl ZZ_pEX while it should use the faster lzz_pEX for word-sized primes.



---

archive/issue_comments_077365.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2018-07-07T23:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77365",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_020628.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2019-01-13T14:35:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20628"
}
```



---

archive/issue_events_020629.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2019-01-13T14:35:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20629"
}
```



---

archive/issue_events_020630.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-03-25T10:56:15Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20630"
}
```



---

archive/issue_events_020631.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-03-25T10:56:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20631"
}
```



---

archive/issue_comments_077366.json:
```json
{
    "body": "Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)",
    "created_at": "2019-03-25T10:56:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77366",
    "user": "https://github.com/embray"
}
```

Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)



---

archive/issue_comments_077367.json:
```json
{
    "body": "Tickets still needing working or clarification should be moved to the next release milestone at the soonest (please feel free to revert if you think the ticket is close to being resolved).",
    "created_at": "2019-06-14T14:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77367",
    "user": "https://github.com/embray"
}
```

Tickets still needing working or clarification should be moved to the next release milestone at the soonest (please feel free to revert if you think the ticket is close to being resolved).



---

archive/issue_events_020632.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-06-14T14:50:27Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20632"
}
```



---

archive/issue_events_020633.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-06-14T14:50:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20633"
}
```



---

archive/issue_comments_077368.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2019-06-26T11:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77368",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077369.json:
```json
{
    "body": "lzz_pEX is not interfaced in Sage, so that should be a different ticket.\n\nStill, with latest ntl library the code should be even much faster since the modular gcds are subquadratic for these types.\n\ndevelop merged.",
    "created_at": "2019-06-26T11:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77369",
    "user": "https://github.com/lftabera"
}
```

lzz_pEX is not interfaced in Sage, so that should be a different ticket.

Still, with latest ntl library the code should be even much faster since the modular gcds are subquadratic for these types.

develop merged.



---

archive/issue_comments_077370.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2019-06-26T11:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77370",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_077371.json:
```json
{
    "body": "Replying to [comment:69 lftabera]:\n> lzz_pEX is not interfaced in Sage, so that should be a different ticket.\n\nThere is #8109 for that.",
    "created_at": "2019-06-30T12:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77371",
    "user": "https://github.com/slel"
}
```

Replying to [comment:69 lftabera]:
> lzz_pEX is not interfaced in Sage, so that should be a different ticket.

There is #8109 for that.



---

archive/issue_comments_077372.json:
```json
{
    "body": "Ticket retargeted after milestone closed",
    "created_at": "2019-12-30T14:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77372",
    "user": "https://github.com/embray"
}
```

Ticket retargeted after milestone closed



---

archive/issue_events_020634.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-12-30T14:48:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20634"
}
```



---

archive/issue_events_020635.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-12-30T14:48:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20635"
}
```



---

archive/issue_events_020636.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-04-14T19:41:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20636"
}
```



---

archive/issue_events_020637.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-04-14T19:41:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20637"
}
```



---

archive/issue_comments_077373.json:
```json
{
    "body": "Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.",
    "created_at": "2020-04-14T19:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77373",
    "user": "https://github.com/mkoeppe"
}
```

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.



---

archive/issue_comments_077374.json:
```json
{
    "body": "The branch has conflict with the sage develop branch since at least 9.1.beta7 according to the patchbot reports.",
    "created_at": "2020-08-15T13:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77374",
    "user": "https://github.com/seblabbe"
}
```

The branch has conflict with the sage develop branch since at least 9.1.beta7 according to the patchbot reports.



---

archive/issue_comments_077375.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2020-08-15T13:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77375",
    "user": "https://github.com/seblabbe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_020638.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-09-05T19:21:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20638"
}
```



---

archive/issue_events_020639.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-09-05T19:21:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20639"
}
```



---

archive/issue_events_020640.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-02-13T20:51:01Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20640"
}
```



---

archive/issue_events_020641.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-02-13T20:51:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20641"
}
```



---

archive/issue_comments_077376.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77376",
    "user": "https://github.com/mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_events_020642.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-19T00:44:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20642"
}
```



---

archive/issue_events_020643.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-19T00:44:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20643"
}
```



---

archive/issue_comments_077377.json:
```json
{
    "body": "Setting a new milestone for this ticket based on a cursory review.",
    "created_at": "2021-07-19T00:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77377",
    "user": "https://github.com/mkoeppe"
}
```

Setting a new milestone for this ticket based on a cursory review.



---

archive/issue_comments_077378.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-07-20T10:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8558#issuecomment-77378",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_020644.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:24:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20644"
}
```



---

archive/issue_events_020645.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:24:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20645"
}
```



---

archive/issue_events_020646.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-02T20:27:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20646"
}
```



---

archive/issue_events_020647.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-02T20:27:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20647"
}
```



---

archive/issue_events_020648.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-09-19T18:58:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20648"
}
```



---

archive/issue_events_020649.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-09-19T18:58:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8558",
    "milestone": "sage-9.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8558#event-20649"
}
```
