# Issue 8728: Incorrect integral from Maxima

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-04-20 16:22:21

Assignee: burcin

From #sage-devel:


```
Boulemans left the chat room. (Read error: Connection reset by peer)
[11:58am] Boule joined the chat room.
[11:58am] Boule: (laptop shutdown due to power supply)
[11:59am] Boule: e, T, w = var("e T w"); assume(1 = e^2)>0; integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi) should give -2*pi e cos w/(1-e^2)^3/2 instead of 0
[11:59am] Boule: can someone help?
[12:00pm] wjp: yeah, sage seems to have some trouble with this integral. You could try http://groups.google.com/group/sage-support since the right people don't seem to be here currently
[12:00pm] Boule: ok, thanx
[12:08pm] kcrisman: By the way, I just tried this and get a hang in Maxima.  Can you type the exact commands which lead to an answer of 0?
[12:08pm] kcrisman: If I plug something (.5, .75) in for e in Maxima in Sage, I do get zero as an output.
[12:12pm] Boule: don't know maxima, but with numerical values for e and w at wolfram-alfa, it gives something different than 0
[12:13pm] wjp: *nod* maple gives non-zeros too
[12:13pm] kcrisman: Can you give the *exact* sequence of commands which yield zero in Sage itself? 
[12:14pm] Boule: e = var('e')
[12:14pm] Boule: T = var('T')
[12:14pm] Boule: w = var('w')
[12:14pm] baali1 joined the chat room.
[12:14pm] baali left the chat room. (Quit: Leaving.)
[12:15pm] Boule: assume(1-e^2>0)
[12:15pm] Boule:  integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)
[12:15pm] kcrisman: Okay, that's what I thought.
[12:16pm] kcrisman: Okay, it takes a while but I do get 0.
```



---

Comment by jason created at 2010-04-20 16:42:29

I wonder if this is another manifestation of this bug:


```
sage: integrate(sqrt(sin(x)^2+cos(x)^2), x,0,2*pi)
pi
```



---

Comment by jason created at 2010-04-20 16:53:38

#8729 may point to a solution.


---

Comment by kcrisman created at 2010-04-20 16:56:26

Hmm, I forgot about this, and it's true it never got implemented, did it?


---

Comment by jason created at 2010-04-20 17:22:58

It was fixed about two weeks ago in maxima.  There was a new release of maxima a few days ago---I'm trying to make an spkg right now.


---

Comment by kcrisman created at 2010-04-20 17:31:48

Sweet.  I haven't been keeping up on the Maxima list lately, thanks.


---

Comment by jason created at 2010-04-20 19:27:09

Replying to [comment:1 jason]:
> I wonder if this is another manifestation of this bug:
> 
> {{{
> sage: integrate(sqrt(sin(x)<sup>2+cos(x)</sup>2), x,0,2*pi)
> pi
> }}}

I just checked; this ticket isn't the same bug.


---

Comment by jason created at 2010-05-13 04:38:20

The upgrade to maxima 5.21.1 does not fix this.  After #8731:


```
sage: e, T, w = var("e T w")    
sage: assume(1-e^2>0)
sage: integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)                                           
0
```



---

Comment by kcrisman created at 2011-03-14 20:38:35

Maxima 5.23.2 still has this, and we still haven't reported it. 

```
Maxima 5.23.2 http://maxima.sourceforge.net
using Lisp SBCL 1.0.24
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) assume(1-e^2>0);
                                     2
(%o1)                              [e  < 1]
(%i3) integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*%pi);
(%o3)                                  0
```

This is now Maxima bug 3211975.


---

Comment by kcrisman created at 2011-03-30 15:16:20

According to [the bug report](http://sourceforge.net/tracker/?func=detail&aid=3211975&group_id=4933&atid=104933), this is now fixed.  However, some examples may still throw a Lisp error, so we should check out whether that will affect us before saying we're totally fixed when we upgrade.


---

Comment by kcrisman created at 2012-08-14 01:14:52

Maxima 5.28 is now out.


---

Comment by kcrisman created at 2013-01-20 01:37:49

See #13973 where this should (?) be fixed, just need a doctest here?


---

Comment by pbruin created at 2014-05-21 20:36:20

In Maxima 5.33.0 (see #13973):

```
(%i1) assume(e^2<1);
                                     2
(%o1)                              [e  < 1]
(%i2) integrate(cos(w+T)/(1+e*cos(T))^2, T, 0, 2*%pi);
                      2
Is abs(e) - sqrt(1 - e ) - 1 positive, negative or zero?

negative;
   !          2     !
Is !sqrt(1 - e ) - 1! - abs(e) positive, negative or zero?

negative;
                                             2
                           2 %pi e sqrt(1 - e ) cos(w)
(%o2)                    - ---------------------------
                                   4      2
                                  e  - 2 e  + 1
```

This appears to be the correct answer.  Note that the answers to both questions are "negative" for all _e_ with -1 < _e_ < 1, so it would be nice if Maxima didn't ask those questions.


---

Comment by kcrisman created at 2014-10-20 13:32:24

> In Maxima 5.33.0 (see #13973):
> This appears to be the correct answer.  Note that the answers to both questions are "negative" for all _e_ with -1 < _e_ < 1, so it would be nice if Maxima didn't ask those questions.
The thing noted in the message upstream when they closed their ticket

```
sage: integrate(cos(w+T)/(1+.5*cos(T))^2,T,0,2*pi)
<boom>
```

does still happen, but I think that is a different issue tracked elsewhere here (the usual keepfloat thing).

So... do we have a reasonable test case to add here to confirm this is fixed and close it?


---

Comment by rws created at 2015-02-01 13:54:55

Here's the doctest:

```
sage: assume(1-e^2>0)
sage: assume(abs(e)-sqrt(1-e^2)-1>0)
sage: assume(abs(sqrt(1-e^2)-1)-abs(e)>0)
sage: integrate(cos(w+T)/(1+e*cos(T))^2,T,0,2*pi)
2*pi*sqrt(-e^2 + 1)*e*cos(w)/(e^4 - 2*e^2 + 1)
```



---

Comment by rws created at 2015-02-02 13:54:03

New commits:


---

Comment by rws created at 2015-02-02 13:54:03

Changing status from new to needs_review.


---

Comment by pbruin created at 2015-02-02 14:11:45

Changing status from needs_review to needs_work.


---

Comment by pbruin created at 2015-02-02 14:11:45

Your assumptions are contradictory: the first assumption (`1 - e^2 > 0`) implies the negation of the other two assumptions (see also comment:15).

A fortiori, the other two assumptions (after negating) are actually redundant.  It is annoying that we have to add them; ideally, we would only declare this integral to be "fixed" if Maxima did not need the extra two assumptions...


---

Comment by rws created at 2016-08-05 13:44:08

Changing status from needs_work to needs_review.


---

Comment by rws created at 2016-08-05 13:44:08

New commits:


---

Comment by tscrim created at 2016-08-05 15:52:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-08-07 20:01:30

Resolution: fixed


---

Comment by pbruin created at 2016-08-11 08:41:23

I noticed just now that this ticket has been closed; it seems comment:15 and comment:22 were ignored...


---

Comment by rws created at 2016-08-11 09:09:50

That would seem so. I think you are asking for a feature (redundancy of additional assumptions) in Maxima that would warrant a separate ticket. I apologize for not answering earlier.


---

Comment by pbruin created at 2016-08-11 09:21:58

Replying to [comment:28 rws]:
> I think you are asking for a feature (redundancy of additional assumptions) in Maxima that would warrant a separate ticket.
That too, but more importantly I meant the fact that the assumptions that are currently made in the doctest are mutually inconsistent:

```
assume(1-c^2 > 0)
assume(abs(c) - sqrt(1-c^2) - 1 > 0)
assume(abs(sqrt(1-c^2)-1) - abs(c) > 0)
```

Namely, the first assumption is equivalent to `-1 < c < 1`, and on this domain the functions `abs(c) - sqrt(1-c^2) - 1` and `abs(sqrt(1-c^2)-1) - abs(c)` are strictly negative.

There is already some functionality for detecting inconsistent assumptions (e.g. `assume(x > 0); assume(x < 0)` raises an error), but it doesn't detect this case.
