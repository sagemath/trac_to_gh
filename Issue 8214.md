# Issue 8214: add better error message when symbolic expressions are called

Issue created by migration from https://trac.sagemath.org/ticket/8214

Original creator: burcin

Original creation time: 2010-02-08 13:36:24

Assignee: burcin

From sage-devel:


```
On Sun, 7 Feb 2010 10:36:29 -0800 (PST)
Gustav Delius <gustav.delius@gmail.com> wrote:

> I wonder whether it would be possible to give a better error message
> when a user leaves out the multiplication operator in something like
> x(x+1). Perhaps somthing like: "Warning: you may have forgotten a
> multiplication operator."
> 
> Currently one gets the error message: "DeprecationWarning:
> Substitution using function-call syntax and unnamed arguments is
> deprecated and will be removed from a future release of Sage; you can
> use named arguments instead, like EXPR(x=...,y=...)". This error
> message is meaningful only to people who know the history of sage and
> know that there used to be a confusing shorthand notation that allowed
> something like x=a^2 to be interpreted as x(a)=a^2. I am glad that was
> deprecated, but I think that the deprecation warning should be
> preceeded by the warning about the possibility of a missing *.
```


Here is the thread:

http://groups.google.com/group/sage-devel/t/de97f91d548cc0ec

Incidentally, it's almost a year since this was deprecated, #5413. Maybe we can remove the deprecation message for good. :)


---

Comment by delius created at 2010-02-08 15:41:24

Burcin, I agree with your observation that the shortcut notation has now been deprecated for a long time. However the shortcut notation has not actually been disabled yet. Perhaps the warning should stay until that has happened.


---

Comment by kcrisman created at 2010-05-27 14:25:53

As to what the new message should be:

```
Maybe, but that message is not so helpful.  I guarantee you that you don't need to know the history of Sage to do

sage: f=x^2
sage: f(2)

and expect 4.  You just need to attend an insufficiently pedantic algebra or calculus lecture :)
```



---

Comment by kcrisman created at 2011-11-07 22:04:40

But definitely add some *serious* documentation in several spots people might look for why this is "wrong".  If it is ;-)

See also [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/5f2705b2b8d21593/b11079d8299a03b5), where the BDFL suggests it really is time to let it go.


---

Comment by rws created at 2015-02-01 09:32:59

duplicate of #14270


---

Comment by aapitzsch created at 2015-02-01 09:55:15

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-02-01 10:08:55

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-02-08 15:28:10

Resolution: duplicate
