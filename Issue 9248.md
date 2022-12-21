# Issue 9248: docstring for factorial doesn't say that it accepts non-integer, non-symbolic input

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-06-16 01:55:29

Assignee: mvngu

At comment:2:ticket:9240, we see someone get confused about the docstring for `factorial`, which claims it takes as input an integer or symbolic expression. However, it takes non-integer, non-SR inputs:

```
sage: x = 1.5; parent(x)
Real Field with 53 bits of precision
sage: factorial(x)
1.32934038817914
sage: x = 3/2; parent(x)
Rational Field
sage: factorial(x)      
3/4*sqrt(pi)
sage: x = CC(1+I); parent(x)
Complex Field with 53 bits of precision
sage: factorial(x)
0.652965496420167 + 0.343065839816545*I
```

I understand that there is coercion going on, but we should specify that the function takes pretty much any complex number (except of course negative integers) and evaluates (something akin to) gamma(1+x).

However, it doesn't exactly do gamma(1+x):

```
sage: x = I; parent(x)  
Symbolic Ring
sage: factorial(x)    
0.498015668118356 - 0.154949828301811*I
sage: gamma(x+1)      
gamma(I + 1)
sage: parent(factorial(x))  
Symbolic Ring
sage: gamma(x+1).n() 
0.498015668118356 - 0.154949828301811*I
sage: parent(gamma(x+1).n())
Complex Field with 53 bits of precision
```

The factorial function clearly is not simply calling gamma(x+1) when x is not an integer.


---

Comment by ddrake created at 2010-06-16 05:13:13

Changing assignee from mvngu to ddrake.


---

Comment by ddrake created at 2010-06-16 05:13:13

Also, factorial doesn't seem to accept the algorithm keyword anymore, even though the docstring says it does! I see that factorial() is just a wrapper around GiNaC's factorial; how does GiNaC compute factorials?


---

Comment by kcrisman created at 2010-12-02 02:27:51

Notice also that factorial does not accept all sorts of input, which leads to problems in [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/119eafbfe3b69500).


---

Comment by kcrisman created at 2010-12-02 02:28:18

Replying to [comment:2 kcrisman]:
> Notice also that factorial does not accept all sorts of input, which leads to problems in [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/119eafbfe3b69500).  
Which for some reason I still posted even after realizing this is just #9240. Sorry for the noise.


---

Comment by rws created at 2014-12-13 08:16:52

Replying to [comment:1 ddrake]:
> Also, factorial doesn't seem to accept the algorithm keyword anymore, even though the docstring says it does!
Wrong doc read. The problem is fixed in #17489.


---

Comment by rws created at 2014-12-13 08:19:56

It appears the originally described issue was fixed in #12286 (misleading title).


---

Comment by rws created at 2014-12-13 08:19:56

Changing status from new to needs_review.


---

Comment by ncohen created at 2014-12-31 10:46:02

please change the status of a ticket to 'positive review' when you flag it as wontfix.


---

Comment by ncohen created at 2014-12-31 10:46:02

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2015-01-01 02:38:07

The same person should not both set it to wontfix and give it a positive review as it skips the review process.


---

Comment by jdemeyer created at 2015-01-02 09:59:15

On the other hand, closing a ticket without review is much less bad than merging a branch without review. And essentially _nobody_ reviews sage-duplicate/invalid/wontfix tickets.


---

Comment by kcrisman created at 2015-01-03 21:50:41

> The same person should not both set it to wontfix and give it a positive review as it skips the review process.
But the invalid and duplicate I think this is okay for.  I often give a positive review to dups or obviously now-functioning tickets.
> And essentially nobody reviews sage-duplicate/invalid/wontfix tickets.
Yeah, probably also true.

I do have to say that perhaps we should have a separate wontfix that would require _two_ reviewers, maybe?  I have occasionally set some notebook tickets to wontfix but that is a fairly unusual situation.


---

Comment by vbraun created at 2015-01-13 01:16:55

Resolution: fixed
