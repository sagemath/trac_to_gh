# Issue 5963: 3.4.2.a0: prime_pi returns wrong results on some platforms for large input

Issue created by migration from https://trac.sagemath.org/ticket/5963

Original creator: mabshoff

Original creation time: 2009-05-02 20:15:21

Assignee: was

Alex reports: 

I can't get this to segfault. I tried on sage.math and on my laptop (macbook running 32-bit archlinux). The problem is that the two machines get different answers after a while (I hope the table is clear -- the last column is a function that's "known" to be a good approximation to prime_pi):

```
x     prime_pi(x) on sage.math     prime_pi(x) on my laptop     Li(x)-Li(sqrt(x))/2
2^46   2280998753949                2280998753949               2.28099863535e+12
2^47   4461632979717                4454203917918               4.46163280359e+12
2^48   8731188863470                8612800813048               8.73118897751e+12
2^49  17094432576778               15793194017311               1.70944327138e+13
2^50  33483379603407               21969300962685               3.34833795774e+13
```

So it seems that the problem starts somewhere between 2^46 and 2^47, and that the sage.math output is most likely correct.


---

Comment by mabshoff created at 2009-05-03 00:17:51

As discussed toward the end in https://groups.google.com/group/sage-devel/t/776d8e0a25735dca 

```
On May 2, 3:52 pm, William Stein <wst...@gmail.com> wrote: 
<SNIP>
> Andrew looked into this whole issue a while ago, and told me that the
> prime_pi he implemented *should* only work up to about 2^40, and the
> algorithm would take far too long above there.   I thought he had
> included an error message if the input exceeds 2^40, but I guess not.
>    So +1 to your suggestion above, but with a smaller bound that 2^48.

Cool.

> He told me Mathematica can go up to about 2^45 or so, but not beyond.

At least for MMA 6.0 on linux x86-64 the limit seems to be around
2^47:

         MMA        Sage

2^44:   18.04      110.88   (597116381732)
2^45:   29.98      207.61   (1166746786182)
2^46:   47.59      389.98   (2280998753949)
2^47:   89.25      728.84   (4461632979717)
2^48:   NA :)      about an hour - correct?

According to Alex's numbers at least on his laptop 2^46 was correct on
32 bits, but given the length of the test (~6 minutes on sage.math
this isn't really doctestable).

> The algorithm in Mathematica is completely different (and better) than
> what Andrew implemented for Sage.   As far as I know the situation for
> computing pi(X) using general purpose math software is thus:

>    * Mathematica -- has the best implementation available

>    * Sage -- now has the second best implementation available

Yep, the old implementation was about 1000 times slower than Andrew's
which is about 5 times slower than MMA 6.0 - so great job from
catching us up from 5000 times to only 5 times :).

>    * Pari, Maple, Matlab -- "stupid" implementations, which all simply
> enumerate all primes up to x and see how many there are.  Useless, and
> can't come close to what Sage or Mathematica do.

Well, what should we pick as upper bound? 2^40 seems to be what Andrew
suggests, but maybe 2^42 or 2^43? In that range we can actually add
#long doctests and I would be much more comfortable that we would at
least catch potential issues.

>  -- William

Cheers,

Michael 
```



---

Attachment

The attached patch caps the allowed input to `2^40` for now and adds a long doctest to verify the correct value of all n in (30..40) for prime_pi(2**n). The upper allowable limit should be reviewed post Sage 3.4.2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 06:21:47

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2009-05-04 06:21:59

Changing status from new to assigned.


---

Comment by roed created at 2009-05-04 08:37:09

Looks good to me.  Michael says that the values in the doctest agree with those from Mathematica.


---

Comment by mabshoff created at 2009-05-04 09:31:39

Resolution: fixed


---

Comment by mabshoff created at 2009-05-04 09:31:39

Merged in Sage 3.4.2.final.

Cheers,

Michael
