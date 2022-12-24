# Issue 7587: improve multi_polynomial_libsingular exponent method

archive/issues_007587.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  simonking\n\nThe returned result is a list of ETuples, but for people interested in maximum speed it would be useful to provide an option to return plain tuples.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7587\n\n",
    "created_at": "2009-12-02T22:11:10Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "improve multi_polynomial_libsingular exponent method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7587",
    "user": "ylchapuy"
}
```
Assignee: AlexGhitza

CC:  simonking

The returned result is a list of ETuples, but for people interested in maximum speed it would be useful to provide an option to return plain tuples.

Issue created by migration from https://trac.sagemath.org/ticket/7587





---

archive/issue_comments_064685.json:
```json
{
    "body": "Attachment [trac_7587-multi_polynomial_libsingular_exponents.patch](tarball://root/attachments/some-uuid/ticket7587/trac_7587-multi_polynomial_libsingular_exponents.patch) by ylchapuy created at 2009-12-02 22:17:36\n\nbased on 4.3.alpha0",
    "created_at": "2009-12-02T22:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64685",
    "user": "ylchapuy"
}
```

Attachment [trac_7587-multi_polynomial_libsingular_exponents.patch](tarball://root/attachments/some-uuid/ticket7587/trac_7587-multi_polynomial_libsingular_exponents.patch) by ylchapuy created at 2009-12-02 22:17:36

based on 4.3.alpha0



---

archive/issue_comments_064686.json:
```json
{
    "body": "For the record:\n\n\n```\nsage: R = PolynomialRing(QQ,100,'x') \nsage: p = R.random_element(degree=50,terms=50)\nsage: timeit('p.exponents()')\n625 loops, best of 3: 1.02 ms per loop\nsage: timeit('p.exponents(as_ETuples=False)')\n625 loops, best of 3: 110 \u00b5s per loop\n```\n",
    "created_at": "2009-12-02T22:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64686",
    "user": "ylchapuy"
}
```

For the record:


```
sage: R = PolynomialRing(QQ,100,'x') 
sage: p = R.random_element(degree=50,terms=50)
sage: timeit('p.exponents()')
625 loops, best of 3: 1.02 ms per loop
sage: timeit('p.exponents(as_ETuples=False)')
625 loops, best of 3: 110 µs per loop
```




---

archive/issue_comments_064687.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-02T22:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64687",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064688.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-03T14:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64688",
    "user": "SimonKing"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064689.json:
```json
{
    "body": "Hi Yann!\n\nFirst good new: The patch cleanly applies to sage-4.3.alpha0.\n\nSecond good news: Using regular expressions (as explained [here](http://groups.google.com/group/sage-devel/browse_thread/thread/20e0fc8f5c5be582)) seem to still be faster in my applications:\n\n```\nsage: Vars = ['x_'+str(n) for n in range(50)]+['y'+str(n) for n in range(50)]\nsage: R = PolynomialRing(QQ,Vars)\nsage: RE = re.compile('([a-zA-Z0-9]+)_([0-9]+)\\^?([0-9]*)')\nsage: p = R.random_element()\nsage: p *= R.random_element()\nsage: p *= R.random_element()\nsage: p *= R.random_element()\nsage: p *= R.random_element()\nsage: p *= R.random_element()\nsage: L = [(Vars[i],e) for i,e in enumerate(p.lm().exponents(as_ETuples=False)[0][:50]) if e]\nsage: L\n[('x_0', 1),\n ('x_2', 1),\n ('x_4', 1),\n ('x_5', 2),\n ('x_10', 1),\n ('x_42', 1),\n ('x_47', 1)]\nsage: RE.findall(str(p.lm()))\n[('x', '0', ''),\n ('x', '2', ''),\n ('x', '4', ''),\n ('x', '5', '2'),\n ('x', '10', ''),\n ('x', '42', ''),\n ('x', '47', '')]\nsage: timeit('L = RE.findall(str(p.lm()))')\n625 loops, best of 3: 25.1 \u00b5s per loop\nsage: timeit('L = [(Vars[i],e) for i,e in enumerate(p.lm().exponents(as_ETuples=False)[0][:50]) if e] ')\n625 loops, best of 3: 11.2 \u00b5s per loop\n```\n\n\nI can also confirm that the computation time with the `as_ETuples=False` option is reduced by 90%. So, I can give it a positive review.",
    "created_at": "2009-12-03T14:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64689",
    "user": "SimonKing"
}
```

Hi Yann!

First good new: The patch cleanly applies to sage-4.3.alpha0.

Second good news: Using regular expressions (as explained [here](http://groups.google.com/group/sage-devel/browse_thread/thread/20e0fc8f5c5be582)) seem to still be faster in my applications:

```
sage: Vars = ['x_'+str(n) for n in range(50)]+['y'+str(n) for n in range(50)]
sage: R = PolynomialRing(QQ,Vars)
sage: RE = re.compile('([a-zA-Z0-9]+)_([0-9]+)\^?([0-9]*)')
sage: p = R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: L = [(Vars[i],e) for i,e in enumerate(p.lm().exponents(as_ETuples=False)[0][:50]) if e]
sage: L
[('x_0', 1),
 ('x_2', 1),
 ('x_4', 1),
 ('x_5', 2),
 ('x_10', 1),
 ('x_42', 1),
 ('x_47', 1)]
sage: RE.findall(str(p.lm()))
[('x', '0', ''),
 ('x', '2', ''),
 ('x', '4', ''),
 ('x', '5', '2'),
 ('x', '10', ''),
 ('x', '42', ''),
 ('x', '47', '')]
sage: timeit('L = RE.findall(str(p.lm()))')
625 loops, best of 3: 25.1 µs per loop
sage: timeit('L = [(Vars[i],e) for i,e in enumerate(p.lm().exponents(as_ETuples=False)[0][:50]) if e] ')
625 loops, best of 3: 11.2 µs per loop
```


I can also confirm that the computation time with the `as_ETuples=False` option is reduced by 90%. So, I can give it a positive review.



---

archive/issue_comments_064690.json:
```json
{
    "body": "Thanks for the review.\n\nI don't understand why 25.1 \u00b5s is better than 11.2 \u00b5s though, but I might miss something.",
    "created_at": "2009-12-03T14:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64690",
    "user": "ylchapuy"
}
```

Thanks for the review.

I don't understand why 25.1 µs is better than 11.2 µs though, but I might miss something.



---

archive/issue_comments_064691.json:
```json
{
    "body": "Replying to [comment:3 ylchapuy]:\n> Thanks for the review.\n> \n> I don't understand why 25.1 \u00b5s is better than 11.2 \u00b5s though, but I might miss something.\n\nThe 25.1 \u00b5s is for using regular expressions, the 11.2 \u00b5s is for using `exponents()`. 11.2 \u00b5s is certainly better than 25.1 \u00b5s!\n\nIn other words: With your patch, I can finally avoid the use of regular expressions!\n\nCheers,\nSimon",
    "created_at": "2009-12-03T15:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64691",
    "user": "SimonKing"
}
```

Replying to [comment:3 ylchapuy]:
> Thanks for the review.
> 
> I don't understand why 25.1 µs is better than 11.2 µs though, but I might miss something.

The 25.1 µs is for using regular expressions, the 11.2 µs is for using `exponents()`. 11.2 µs is certainly better than 25.1 µs!

In other words: With your patch, I can finally avoid the use of regular expressions!

Cheers,
Simon



---

archive/issue_comments_064692.json:
```json
{
    "body": "Replying to [comment:3 ylchapuy]:\n> I don't understand why 25.1 \u00b5s is better than 11.2 \u00b5s though, but I might miss something.\n\nAfter reading what I wrote in comment 2, I see that I must apologize. I started to write the comment when I had just used exponents *without* the `as_ETuples=False` option --- which was still slower than the regular expression. When I repeated it *with* the option, it was finally beating the regular expression --- but I forgot to edit the sentence on top of the example.\n\nSorry for the noise...",
    "created_at": "2009-12-03T21:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64692",
    "user": "SimonKing"
}
```

Replying to [comment:3 ylchapuy]:
> I don't understand why 25.1 µs is better than 11.2 µs though, but I might miss something.

After reading what I wrote in comment 2, I see that I must apologize. I started to write the comment when I had just used exponents *without* the `as_ETuples=False` option --- which was still slower than the regular expression. When I repeated it *with* the option, it was finally beating the regular expression --- but I forgot to edit the sentence on top of the example.

Sorry for the noise...



---

archive/issue_comments_064693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-04T05:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7587#issuecomment-64693",
    "user": "mhansen"
}
```

Resolution: fixed
