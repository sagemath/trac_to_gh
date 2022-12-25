# Issue 7414: improve {from,to}_inversion_vector

archive/issues_007414.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nThe method to_inversion_vector can be greatly improved by using a divide-and-conquer strategy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7414\n\n",
    "created_at": "2009-11-08T20:31:45Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "improve {from,to}_inversion_vector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7414",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: @mwhansen

CC:  sage-combinat

The method to_inversion_vector can be greatly improved by using a divide-and-conquer strategy.

Issue created by migration from https://trac.sagemath.org/ticket/7414





---

archive/issue_comments_062265.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-08T20:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62265",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062266.json:
```json
{
    "body": "for the record,\n\nbefore:\n\n```\nsage: p= Permutations(1000).random_element()\nsage: timeit('p.to_inversion_vector()')\n5 loops, best of 3: 2.08 s per loop\nsage: iv = p.to_inversion_vector()\nsage: timeit('sage.combinat.permutation.from_inversion_vector(iv)')\n25 loops, best of 3: 9.57 ms per loop\n```\n\nafter:\n\n```\nsage: p= Permutations(1000).random_element()\nsage: timeit('p.to_inversion_vector()')\n25 loops, best of 3: 14.7 ms per loop\nsage: iv = p.to_inversion_vector()\nsage: timeit('sage.combinat.permutation.from_inversion_vector(iv)')\n625 loops, best of 3: 1.47 ms per loop\n```",
    "created_at": "2009-11-08T20:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62266",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

for the record,

before:

```
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_inversion_vector()')
5 loops, best of 3: 2.08 s per loop
sage: iv = p.to_inversion_vector()
sage: timeit('sage.combinat.permutation.from_inversion_vector(iv)')
25 loops, best of 3: 9.57 ms per loop
```

after:

```
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_inversion_vector()')
25 loops, best of 3: 14.7 ms per loop
sage: iv = p.to_inversion_vector()
sage: timeit('sage.combinat.permutation.from_inversion_vector(iv)')
625 loops, best of 3: 1.47 ms per loop
```



---

archive/issue_comments_062267.json:
```json
{
    "body": "Changing keywords from \"\" to \"permutations, inversion vector, lehmer code\".",
    "created_at": "2009-11-09T08:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62267",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "" to "permutations, inversion vector, lehmer code".



---

archive/issue_comments_062268.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-09T08:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62268",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062269.json:
```json
{
    "body": "Yes, this is very good for large permutaions ! but is is much slower on small permutations, where I will use it :-) Sorry for this...\n\nBefore:\n\n```\n625 loops, best of 3: 16.4 \u00b5s per loop\n625 loops, best of 3: 19.2 \u00b5s per loop\n625 loops, best of 3: 33.3 \u00b5s per loop\n625 loops, best of 3: 87.4 \u00b5s per loop\n625 loops, best of 3: 356 \u00b5s per loop\n125 loops, best of 3: 2.04 ms per loop\n25 loops, best of 3: 14.2 ms per loop\n5 loops, best of 3: 117 ms per loop\n```\nafter:\n\n```\n625 loops, best of 3: 18.1 \u00b5s per loop\n625 loops, best of 3: 19.9 \u00b5s per loop\n625 loops, best of 3: 51.2 \u00b5s per loop\n625 loops, best of 3: 166 \u00b5s per loop\n625 loops, best of 3: 794 \u00b5s per loop\n125 loops, best of 3: 4.86 ms per loop\n25 loops, best of 3: 33.2 ms per loop\n5 loops, best of 3: 271 ms per loop\n```\n\nI suggest you to reinstate the former implementation and to change from one to the other depending on the size of the permutations. I wrote the same in MuPAD, the cut-of point where around 18. \n\nMoreover, since the Lehmer code is the inversion vector of the inverse, you can speed up it for large n. Also, if you would take the chance to write the definition of the lehmer code (c_i = the number of j > i s.t. s(j) < s(i)) and to put a link beetween those two methods, then I would be extremely happy to put a positive review. \n\nSorry to give you more work. \n\nCheers,\n\nFlorent",
    "created_at": "2009-11-09T08:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62269",
    "user": "https://github.com/hivert"
}
```

Yes, this is very good for large permutaions ! but is is much slower on small permutations, where I will use it :-) Sorry for this...

Before:

```
625 loops, best of 3: 16.4 µs per loop
625 loops, best of 3: 19.2 µs per loop
625 loops, best of 3: 33.3 µs per loop
625 loops, best of 3: 87.4 µs per loop
625 loops, best of 3: 356 µs per loop
125 loops, best of 3: 2.04 ms per loop
25 loops, best of 3: 14.2 ms per loop
5 loops, best of 3: 117 ms per loop
```
after:

```
625 loops, best of 3: 18.1 µs per loop
625 loops, best of 3: 19.9 µs per loop
625 loops, best of 3: 51.2 µs per loop
625 loops, best of 3: 166 µs per loop
625 loops, best of 3: 794 µs per loop
125 loops, best of 3: 4.86 ms per loop
25 loops, best of 3: 33.2 ms per loop
5 loops, best of 3: 271 ms per loop
```

I suggest you to reinstate the former implementation and to change from one to the other depending on the size of the permutations. I wrote the same in MuPAD, the cut-of point where around 18. 

Moreover, since the Lehmer code is the inversion vector of the inverse, you can speed up it for large n. Also, if you would take the chance to write the definition of the lehmer code (c_i = the number of j > i s.t. s(j) < s(i)) and to put a link beetween those two methods, then I would be extremely happy to put a positive review. 

Sorry to give you more work. 

Cheers,

Florent



---

archive/issue_comments_062270.json:
```json
{
    "body": "And finally, it would be perfect if you add a note on the complexity of the algorithm. \n\nCheers,\n\nFlorent",
    "created_at": "2009-11-09T14:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62270",
    "user": "https://github.com/hivert"
}
```

And finally, it would be perfect if you add a note on the complexity of the algorithm. 

Cheers,

Florent



---

archive/issue_comments_062271.json:
```json
{
    "body": "Attachment [trac_7414-inversion_vector.patch](tarball://root/attachments/some-uuid/ticket7414/trac_7414-inversion_vector.patch) by ylchapuy created at 2009-11-09 23:01:04",
    "created_at": "2009-11-09T23:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62271",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_7414-inversion_vector.patch](tarball://root/attachments/some-uuid/ticket7414/trac_7414-inversion_vector.patch) by ylchapuy created at 2009-11-09 23:01:04



---

archive/issue_comments_062272.json:
```json
{
    "body": "I did my best to keep small permutations fast.\nHere are the new timings.\n\n```\nsage: for k in [0,1,2,3,4,5,6,7]:\n    L=Permutations(k).list()\n    print k\n    timeit('[len(p._to_inversion_vector_orig()) for p in L]')\n    timeit('[len(p._to_inversion_vector_small()) for p in L]')\n    timeit('[len(p.to_inversion_vector()) for p in L]')\n....:     \n0\n625 loops, best of 3: 2.35 \u00b5s per loop\n625 loops, best of 3: 3.86 \u00b5s per loop\n625 loops, best of 3: 1.43 \u00b5s per loop\n1\n625 loops, best of 3: 3.23 \u00b5s per loop\n625 loops, best of 3: 4.98 \u00b5s per loop\n625 loops, best of 3: 1.54 \u00b5s per loop\n2\n625 loops, best of 3: 7.69 \u00b5s per loop\n625 loops, best of 3: 12.2 \u00b5s per loop\n625 loops, best of 3: 3.13 \u00b5s per loop\n3\n625 loops, best of 3: 29.6 \u00b5s per loop\n625 loops, best of 3: 38 \u00b5s per loop\n625 loops, best of 3: 11.2 \u00b5s per loop\n4\n625 loops, best of 3: 152 \u00b5s per loop\n625 loops, best of 3: 171 \u00b5s per loop\n625 loops, best of 3: 197 \u00b5s per loop\n5\n625 loops, best of 3: 957 \u00b5s per loop\n625 loops, best of 3: 961 \u00b5s per loop\n625 loops, best of 3: 1.09 ms per loop\n6\n125 loops, best of 3: 7.14 ms per loop\n125 loops, best of 3: 6.39 ms per loop\n125 loops, best of 3: 7.12 ms per loop\n7\n5 loops, best of 3: 64.4 ms per loop\n5 loops, best of 3: 51.1 ms per loop\n5 loops, best of 3: 55.5 ms per loop\n```\n\nTimings for big permutations are also quite improved thanks to an improved base case.\n\n```\nsage: p= Permutations(1000).random_element()\nsage: timeit('p.to_inversion_vector()')\n125 loops, best of 3: 7.03 ms per loop\n```\n\nAs you suggested, I also improved the to_lehmer_code method. Here is the comparison, first for small sizes,\n\nbefore:\n\n```\nsage: for k in [0,1,2,3,4,5,6]:\n....:         L=Permutations(k).list()\n....:     timeit('[len(p.to_lehmer_code()) for p in L]')\n....: \n625 loops, best of 3: 4.06 \u00b5s per loop\n625 loops, best of 3: 5.86 \u00b5s per loop\n625 loops, best of 3: 13.8 \u00b5s per loop\n625 loops, best of 3: 51.2 \u00b5s per loop\n625 loops, best of 3: 248 \u00b5s per loop\n625 loops, best of 3: 1.55 ms per loop\n25 loops, best of 3: 11.4 ms per loop\n```\n\nafter:\n\n```\nsage: for k in [0,1,2,3,4,5,6]:\n....:         L=Permutations(k).list()\n....:     timeit('[len(p.to_lehmer_code()) for p in L]')\n....: \n625 loops, best of 3: 2.5 \u00b5s per loop\n625 loops, best of 3: 3.81 \u00b5s per loop\n625 loops, best of 3: 9.44 \u00b5s per loop\n625 loops, best of 3: 32 \u00b5s per loop\n625 loops, best of 3: 150 \u00b5s per loop\n625 loops, best of 3: 880 \u00b5s per loop\n125 loops, best of 3: 5.89 ms per loop\n```\n\nand for big sizes,\n\nbefore:\n\n```\nsage: for k in [100,300,600,1000]:\n....:         L=[Permutation(sample(xrange(1,k+1), k)) for _ in xrange(10)]\n....:     timeit('[len(p.to_lehmer_code()) for p in L]')\n....: \n25 loops, best of 3: 20.2 ms per loop\n5 loops, best of 3: 174 ms per loop\n5 loops, best of 3: 704 ms per loop\n5 loops, best of 3: 1.94 s per loop\n```\n\nafter\n\n```\nsage: for k in [100,300,600,1000]:\n....:         L=[Permutation(sample(xrange(1,k+1), k)) for _ in xrange(10)]\n....:     timeit('[len(p.to_lehmer_code()) for p in L]')\n....: \n125 loops, best of 3: 1.89 ms per loop\n25 loops, best of 3: 11.2 ms per loop\n25 loops, best of 3: 37.4 ms per loop\n5 loops, best of 3: 69.1 ms per loop\n```",
    "created_at": "2009-11-09T23:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62272",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I did my best to keep small permutations fast.
Here are the new timings.

```
sage: for k in [0,1,2,3,4,5,6,7]:
    L=Permutations(k).list()
    print k
    timeit('[len(p._to_inversion_vector_orig()) for p in L]')
    timeit('[len(p._to_inversion_vector_small()) for p in L]')
    timeit('[len(p.to_inversion_vector()) for p in L]')
....:     
0
625 loops, best of 3: 2.35 µs per loop
625 loops, best of 3: 3.86 µs per loop
625 loops, best of 3: 1.43 µs per loop
1
625 loops, best of 3: 3.23 µs per loop
625 loops, best of 3: 4.98 µs per loop
625 loops, best of 3: 1.54 µs per loop
2
625 loops, best of 3: 7.69 µs per loop
625 loops, best of 3: 12.2 µs per loop
625 loops, best of 3: 3.13 µs per loop
3
625 loops, best of 3: 29.6 µs per loop
625 loops, best of 3: 38 µs per loop
625 loops, best of 3: 11.2 µs per loop
4
625 loops, best of 3: 152 µs per loop
625 loops, best of 3: 171 µs per loop
625 loops, best of 3: 197 µs per loop
5
625 loops, best of 3: 957 µs per loop
625 loops, best of 3: 961 µs per loop
625 loops, best of 3: 1.09 ms per loop
6
125 loops, best of 3: 7.14 ms per loop
125 loops, best of 3: 6.39 ms per loop
125 loops, best of 3: 7.12 ms per loop
7
5 loops, best of 3: 64.4 ms per loop
5 loops, best of 3: 51.1 ms per loop
5 loops, best of 3: 55.5 ms per loop
```

Timings for big permutations are also quite improved thanks to an improved base case.

```
sage: p= Permutations(1000).random_element()
sage: timeit('p.to_inversion_vector()')
125 loops, best of 3: 7.03 ms per loop
```

As you suggested, I also improved the to_lehmer_code method. Here is the comparison, first for small sizes,

before:

```
sage: for k in [0,1,2,3,4,5,6]:
....:         L=Permutations(k).list()
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
625 loops, best of 3: 4.06 µs per loop
625 loops, best of 3: 5.86 µs per loop
625 loops, best of 3: 13.8 µs per loop
625 loops, best of 3: 51.2 µs per loop
625 loops, best of 3: 248 µs per loop
625 loops, best of 3: 1.55 ms per loop
25 loops, best of 3: 11.4 ms per loop
```

after:

```
sage: for k in [0,1,2,3,4,5,6]:
....:         L=Permutations(k).list()
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
625 loops, best of 3: 2.5 µs per loop
625 loops, best of 3: 3.81 µs per loop
625 loops, best of 3: 9.44 µs per loop
625 loops, best of 3: 32 µs per loop
625 loops, best of 3: 150 µs per loop
625 loops, best of 3: 880 µs per loop
125 loops, best of 3: 5.89 ms per loop
```

and for big sizes,

before:

```
sage: for k in [100,300,600,1000]:
....:         L=[Permutation(sample(xrange(1,k+1), k)) for _ in xrange(10)]
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
25 loops, best of 3: 20.2 ms per loop
5 loops, best of 3: 174 ms per loop
5 loops, best of 3: 704 ms per loop
5 loops, best of 3: 1.94 s per loop
```

after

```
sage: for k in [100,300,600,1000]:
....:         L=[Permutation(sample(xrange(1,k+1), k)) for _ in xrange(10)]
....:     timeit('[len(p.to_lehmer_code()) for p in L]')
....: 
125 loops, best of 3: 1.89 ms per loop
25 loops, best of 3: 11.2 ms per loop
25 loops, best of 3: 37.4 ms per loop
5 loops, best of 3: 69.1 ms per loop
```



---

archive/issue_comments_062273.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-09T23:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62273",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062274.json:
```json
{
    "body": "NB: The tests are long, but they should be much faster of applying #7415 which improves `random_element`",
    "created_at": "2009-11-09T23:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62274",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

NB: The tests are long, but they should be much faster of applying #7415 which improves `random_element`



---

archive/issue_comments_062275.json:
```json
{
    "body": "Attachment [trac_7414-from_inversion_vector.patch](tarball://root/attachments/some-uuid/ticket7414/trac_7414-from_inversion_vector.patch) by ylchapuy created at 2009-11-10 00:27:48\n\nSorry, I forgot the from_* methods in the first patch. Please apply both.\n\nCheers,\n Yann",
    "created_at": "2009-11-10T00:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62275",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_7414-from_inversion_vector.patch](tarball://root/attachments/some-uuid/ticket7414/trac_7414-from_inversion_vector.patch) by ylchapuy created at 2009-11-10 00:27:48

Sorry, I forgot the from_* methods in the first patch. Please apply both.

Cheers,
 Yann



---

archive/issue_comments_062276.json:
```json
{
    "body": "Good work ! Positive review. \n\nSome remarks: \n- as you commented in the code the hardcoded handling of the n=0,1,2,3 case is a little bit overkill :-)\n- we should'nt spent too much time in optimizing very finely those function since at some point, we will probably change the datastructure for permutations to a fastest one (plain python list or tuple or Cython object or even C int[]).\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-10T08:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62276",
    "user": "https://github.com/hivert"
}
```

Good work ! Positive review. 

Some remarks: 
- as you commented in the code the hardcoded handling of the n=0,1,2,3 case is a little bit overkill :-)
- we should'nt spent too much time in optimizing very finely those function since at some point, we will probably change the datastructure for permutations to a fastest one (plain python list or tuple or Cython object or even C int[]).

Cheers,

Florent



---

archive/issue_comments_062277.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T08:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62277",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017540.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-12T06:40:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7414#event-17540"
}
```



---

archive/issue_comments_062278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7414#issuecomment-62278",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017541.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-11-13T05:09:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7414",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7414#event-17541"
}
```
