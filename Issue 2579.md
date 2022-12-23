# Issue 2579: Inconsistency in integer quotient

Issue created by migration from https://trac.sagemath.org/ticket/2579

Original creator: rishi

Original creation time: 2008-03-18 01:29:11

Assignee: somebody

sage: a=-17
sage: a//4
-5
sage: a.div(4)
-4
sage: a.mod(4)
3


I recommend we redefine

def div(self, other):
    q,_ = self.quo_rem(other)
    return q


---

Comment by rishi created at 2008-03-18 01:34:42

sage: a=-17 

sage: a//4 

-5 

sage: a.div(4)

-4 

sage: a.mod(4)

3

I recommend we redefine

def div(self, other):

    q,_ = self.quo_rem(other) 

    return q


---

Comment by cwitty created at 2008-03-18 02:21:48

If we want a.div(b) to be floor(a/b) (which I agree we probably do, if we want the method to exist at all), the correct fix is to change from mpz_tdiv_qr to mpz_fdiv_q.


---

Comment by rishi created at 2008-03-18 03:00:49

I think the basis logic should be as below. Since this will make the remainder always positive.


```
if mpz_sgn(_other.value) == 1:
            mpz_fdiv_q(q.value, _self.value, _other.value)        
else:
            mpz_cdiv_q(q.value, _self.value, _other.value)
```



---

Attachment


---

Comment by rishi created at 2008-03-19 17:03:18

I used quo_rem to redefine div. I would have essentially copied and pasted quo_rem otherwise.


---

Comment by mhansen created at 2008-03-19 20:31:56

Looks good to me.


---

Comment by mabshoff created at 2008-03-20 00:18:51

Merged in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-20 00:18:51

Resolution: fixed
