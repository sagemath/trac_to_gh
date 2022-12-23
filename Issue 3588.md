# Issue 3588: Divison may involve lengthy calculations

archive/issues_003588.json:
```json
{
    "body": "Assignee: robertwb\n\n\n```\nsage: p = random_prime(2^1000, proof=False)\n\nsage: r = Integers(p)(2)\n\nsage: time 1/r\nCPU times: user 8.33 s, sys: 0.04 s, total: 8.37 s\nWall time: 8.38 s\n 3499526081536621642679042248089160305431650460015592790597504050874839449753564641181241694531732168529968232075793871659087004627036430097798051425534663680136477216778245568521334956231031996455409743133009480089945324001250066901998383114487031466512725971538453941363837544198631115493811447198845\n```\n\n\nThe generic fraction_field() call does primality testing here, takes too long. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3588\n\n",
    "created_at": "2008-07-07T20:23:11Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "Divison may involve lengthy calculations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3588",
    "user": "robertwb"
}
```
Assignee: robertwb


```
sage: p = random_prime(2^1000, proof=False)

sage: r = Integers(p)(2)

sage: time 1/r
CPU times: user 8.33 s, sys: 0.04 s, total: 8.37 s
Wall time: 8.38 s
 3499526081536621642679042248089160305431650460015592790597504050874839449753564641181241694531732168529968232075793871659087004627036430097798051425534663680136477216778245568521334956231031996455409743133009480089945324001250066901998383114487031466512725971538453941363837544198631115493811447198845
```


The generic fraction_field() call does primality testing here, takes too long. 

Issue created by migration from https://trac.sagemath.org/ticket/3588





---

archive/issue_comments_025352.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-07T21:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25352",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025353.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-07T21:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25353",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_025354.json:
```json
{
    "body": "This is 3.0.5 material, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-11T17:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25354",
    "user": "mabshoff"
}
```

This is 3.0.5 material, too.

Cheers,

Michael



---

archive/issue_comments_025355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-11T18:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25355",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_025356.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-07-11T18:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25356",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_025357.json:
```json
{
    "body": "A doctest failed in infinity.py.  I've posted a quick fix here.  Robert could easily have a better fix, so this is reopened.",
    "created_at": "2008-07-11T18:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25357",
    "user": "was"
}
```

A doctest failed in infinity.py.  I've posted a quick fix here.  Robert could easily have a better fix, so this is reopened.



---

archive/issue_comments_025358.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-07-11T18:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25358",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_025359.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-11T18:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25359",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_025360.json:
```json
{
    "body": "Are these patches still needed?  In 3.1.1:\n\n\n```\nsage: p = random_prime(2^1000, proof=False)\nsage: r = Integers(p)(2)                   \nsage: time 1/r\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n4182378068297747496347619509094946589859242110649682753826323779912818104926185222329257414498084527466823768975174201208996376519370243477775194265315260528263826200480626844830896267031936271294686269384932307195051185481109989133791723199020928430708397791147367704717745601696690836602407579616974\nsage: %timeit 1/r\n100000 loops, best of 3: 5.21 \u00b5s per loop\nsage: %timeit 1/Integers(p)(2)\n100000 loops, best of 3: 16.8 \u00b5s per loop\n```\n",
    "created_at": "2008-08-24T17:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25360",
    "user": "cremona"
}
```

Are these patches still needed?  In 3.1.1:


```
sage: p = random_prime(2^1000, proof=False)
sage: r = Integers(p)(2)                   
sage: time 1/r
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4182378068297747496347619509094946589859242110649682753826323779912818104926185222329257414498084527466823768975174201208996376519370243477775194265315260528263826200480626844830896267031936271294686269384932307195051185481109989133791723199020928430708397791147367704717745601696690836602407579616974
sage: %timeit 1/r
100000 loops, best of 3: 5.21 µs per loop
sage: %timeit 1/Integers(p)(2)
100000 loops, best of 3: 16.8 µs per loop
```




---

archive/issue_comments_025361.json:
```json
{
    "body": "This patch was merged in Sage 3.0.6, so I am closing it. The issue it caused to appear was related to weak references and Cython. Thanks for finding this John.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-24T17:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25361",
    "user": "mabshoff"
}
```

This patch was merged in Sage 3.0.6, so I am closing it. The issue it caused to appear was related to weak references and Cython. Thanks for finding this John.

Cheers,

Michael



---

archive/issue_comments_025362.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-24T17:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3588",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3588#issuecomment-25362",
    "user": "mabshoff"
}
```

Resolution: fixed
