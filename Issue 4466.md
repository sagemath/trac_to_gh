# Issue 4466: fix det in linbox case to fail if proof=False isn't also set

archive/issues_004466.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee below:\n\n```\n\n\nOn Fri, Nov 7, 2008 at 4:26 PM, Clement Pernet <clement.pernet@gmail.com> wrote:\n> Hi all,\n>\n> After checking, the default algorithm called in LinBox for det over Z\n> with dense matrices is the naive Chinese Remainder Theorem, with an\n> early termination (if det stabilizes after 4 iterations in a row, then\n> you stop picking random primes).\n>\n> So yes, it is probabilistic, Monte Carlo, and definitely not the fastest\n> way to go (on my box, Sage's implementation, using IML's p-adic solver,\n> is always faster).\n>\n> There is a p-adic implementation, with several additional tricks that\n> Ana Urbanska and J-G Dumas have done, which was supposedely the fastest\n> (btw I like the docstring in sage!!!).\n>\n> So far, I remember, removing it as a default option since it had some\n> leaks, or bugs, and I was waiting for them to polish up the prototypical\n> code. Another line in the v2.0 TODO list, I guess!\n>\n>\n>\n> William Stein a \u00e9crit :\n>> Hi Clement,\n>>\n>> I tried this in Sage:\n>>\n>> time d = random_matrix(ZZ,n).det(proof=True)\n>> time d = random_matrix(ZZ,n).det(algorithm='linbox')\n>>\n>> for various n (say around 200 - 500, etc.,) then linbox is dramatically faster\n>> than Sage.  However, if I do\n>>\n>> time d = random_matrix(ZZ,n).det(proof=False)\n>>\n>> then Sage is similar in speed to linbox (actually about twice as fast on OS X,\n>> and close on sage.math).\n>>\n>> This strongly suggests to me that the following code in Linbox is actually\n>> *not* proving its result.   Could you clarify?\n>>\n>>  void linbox_integer_dense_det(mpz_t ans, mpz_t** matrix, size_t nrows,\n>>                                size_t ncols) {\n>>    commentator.setMaxDetailLevel(0);\n>>    commentator.setMaxDepth (0);\n>>\n>>    DenseMatrix<Integers> A(new_matrix_integers(matrix, nrows, ncols));\n>>    Integers::Element d;\n>>    det(d, A);\n>>    mpz_set(ans, spy.get_mpz(d));\n>> }\n>>\n>>\n>> William\n>>\n>>\n>\n>\n\n\n\n-- \nWilliam Stein\nAssociate Professor of Mathematics\nUniversity of Washington\nhttp://wstein.org\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4466\n\n",
    "created_at": "2008-11-08T03:52:23Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "fix det in linbox case to fail if proof=False isn't also set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4466",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

See below:

```


On Fri, Nov 7, 2008 at 4:26 PM, Clement Pernet <clement.pernet@gmail.com> wrote:
> Hi all,
>
> After checking, the default algorithm called in LinBox for det over Z
> with dense matrices is the naive Chinese Remainder Theorem, with an
> early termination (if det stabilizes after 4 iterations in a row, then
> you stop picking random primes).
>
> So yes, it is probabilistic, Monte Carlo, and definitely not the fastest
> way to go (on my box, Sage's implementation, using IML's p-adic solver,
> is always faster).
>
> There is a p-adic implementation, with several additional tricks that
> Ana Urbanska and J-G Dumas have done, which was supposedely the fastest
> (btw I like the docstring in sage!!!).
>
> So far, I remember, removing it as a default option since it had some
> leaks, or bugs, and I was waiting for them to polish up the prototypical
> code. Another line in the v2.0 TODO list, I guess!
>
>
>
> William Stein a écrit :
>> Hi Clement,
>>
>> I tried this in Sage:
>>
>> time d = random_matrix(ZZ,n).det(proof=True)
>> time d = random_matrix(ZZ,n).det(algorithm='linbox')
>>
>> for various n (say around 200 - 500, etc.,) then linbox is dramatically faster
>> than Sage.  However, if I do
>>
>> time d = random_matrix(ZZ,n).det(proof=False)
>>
>> then Sage is similar in speed to linbox (actually about twice as fast on OS X,
>> and close on sage.math).
>>
>> This strongly suggests to me that the following code in Linbox is actually
>> *not* proving its result.   Could you clarify?
>>
>>  void linbox_integer_dense_det(mpz_t ans, mpz_t** matrix, size_t nrows,
>>                                size_t ncols) {
>>    commentator.setMaxDetailLevel(0);
>>    commentator.setMaxDepth (0);
>>
>>    DenseMatrix<Integers> A(new_matrix_integers(matrix, nrows, ncols));
>>    Integers::Element d;
>>    det(d, A);
>>    mpz_set(ans, spy.get_mpz(d));
>> }
>>
>>
>> William
>>
>>
>
>



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org

```

Issue created by migration from https://trac.sagemath.org/ticket/4466





---

archive/issue_comments_032913.json:
```json
{
    "body": "Attachment [sage-4466.patch](tarball://root/attachments/some-uuid/ticket4466/sage-4466.patch) by @robertwb created at 2008-11-13 22:53:27",
    "created_at": "2008-11-13T22:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4466#issuecomment-32913",
    "user": "https://github.com/robertwb"
}
```

Attachment [sage-4466.patch](tarball://root/attachments/some-uuid/ticket4466/sage-4466.patch) by @robertwb created at 2008-11-13 22:53:27



---

archive/issue_comments_032914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T05:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4466#issuecomment-32914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010092.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-14T05:24:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4466",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4466#event-10092"
}
```



---

archive/issue_comments_032915.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-14T05:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4466#issuecomment-32915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_events_010093.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-14T05:24:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4466",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4466#event-10093"
}
```
