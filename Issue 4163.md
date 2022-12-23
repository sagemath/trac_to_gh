# Issue 4163: tut -- improve factorial / valuation example

Issue created by migration from https://trac.sagemath.org/ticket/4163

Original creator: was

Original creation time: 2008-09-21 14:00:40

Assignee: tba

CC:  cremona


```
That's a good point.

2008/9/20 pong <wypong00>:
>
> This is not a bug report. But I'm not sure where to post a suggestion.
>
> In the SAGE tutorial, http://www.sagemath.org/doc/tut/node27.html
>
> there is an example:
>
> sage: c = factorial(25); c
> 15511210043330985984000000
> sage: [valuation(c,p) for p in prime_range(2,23)]
> [22, 10, 6, 3, 2, 1, 1, 1]
>
> Since prime_range(2,23) does not include 23 itself, maybe it's better
> to change it to prime_range(2,25). In that case, the product of primes
> to the corresponding powers will actually give the factorial of 25.

I would also include
sage: c.factor()
2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
(which would be helpful to people who might know know this meaning of
"valuation", standard in number theory), and even perhaps
sage: list(c.factor())
[(2, 22), (3, 10), (5, 6), (7, 3), (11, 2), (13, 1), (17, 1), (19, 1), (23, 1)]

John Cremona
```



---

Attachment

doc patch


---

Comment by AlexGhitza created at 2008-09-23 08:06:51

see the attached doc patch (made on 3.1.3.alpha0).


---

Comment by mabshoff created at 2008-09-23 08:33:00

Looks good to me. You did not add c.factor(), so I am not sure what to do in that regard.

John: Do you have a preference here?

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-09-23 08:36:46

i thought that it would be preferrable not to clutter the example too much, but i don't have strong feelings about this.  i can easily add that in if people think it's a good idea.


---

Comment by cremona created at 2008-09-23 08:50:39

Replying to [comment:3 AlexGhitza]:
> i thought that it would be preferrable not to clutter the example too much, but i don't have strong feelings about this.  i can easily add that in if people think it's a good idea.

I'm happy with it the way it is.  John


---

Comment by mabshoff created at 2008-09-23 09:41:33

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 09:41:33

Resolution: fixed
