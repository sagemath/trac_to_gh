# Issue 2693: Sage should have generic resultant implementation for multivariate polynomials

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-28 02:21:37

Assignee: was

CC:  tscrim vdelecroix vklein

Consider this example, which fails:

```
R.<x,y> = RR[]
p = x + y
q = x*y
p.resultant(q)
```

(as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/1d6289cead33d063#)

This is because multivariate resultants are implemented using the Singular pexpect interface, which does not support RR.

A workaround for this particular problem (and a possible basis for an improved version) is:

```
p.polynomial(x).resultant(q.polynomial(x)) 
```

That is, fall back to univariate resultants, which are implemented using Pari and are somewhat more generic.  (This is still not truly generic, though, since there are Sage rings which have no Pari equivalent.)


---

Comment by mmarco created at 2014-08-25 08:28:43

In fact, singular resultants are slow compared to other methods, so it would really be a good idea to write specific sage code for resultants.

See #16749 and #12174 for ideas about it.

Just something like:


```
def resultant(self, other, variable):
    m = self.sylvester_matrix(other, variable)
    return m.determinant()
```


Would be both general for any polynomial ring, and faster than the current implementation. And of course, there could be a lot of cases where things can be done much faster, using specific backends where they are better.


---

Comment by chapoton created at 2019-05-01 14:49:17

Changing keywords from "" to "resultant".


---

Comment by chapoton created at 2019-05-01 15:04:51

New commits:


---

Comment by chapoton created at 2019-05-01 15:04:51

Changing status from new to needs_review.


---

Comment by chapoton created at 2019-05-01 18:26:32

green bot, please review


---

Comment by chapoton created at 2019-05-02 06:51:51

hmm, the second doctest is more about univariate polynomials. Maybe it should go there ?


---

Comment by git created at 2019-05-06 15:46:25

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by chapoton created at 2019-05-06 15:47:41

ok, test is now at the right place.


---

Comment by chapoton created at 2019-05-06 17:53:46

and the bot is green.


---

Comment by tscrim created at 2019-05-07 00:56:30

LGTM.


---

Comment by tscrim created at 2019-05-07 00:56:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2019-05-12 21:34:19

Resolution: fixed
