# Issue 4466: fix det in linbox case to fail if proof=False isn't also set

Issue created by migration from https://trac.sagemath.org/ticket/4466

Original creator: was

Original creation time: 2008-11-08 03:52:23

Assignee: was

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



---

Attachment


---

Comment by mabshoff created at 2008-11-14 05:24:43

Resolution: fixed


---

Comment by mabshoff created at 2008-11-14 05:24:43

Merged in Sage 3.2.rc1
