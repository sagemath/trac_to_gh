# Issue 190: fractional matrix indices are allowed ?

Issue created by migration from https://trac.sagemath.org/ticket/190

Original creator: was

Original creation time: 2007-01-13 09:05:16

Assignee: was

Bug reported by Andrey Novoseltsev

This is disturbing.


```
a=matrix(2,2,[1,2,3,4]); a
///
[1 2]
[3 4]
```



```
a.row(1.5)
///
(3, 4)
```



```
a[1.5]
///
(3, 4)
```



```
a[1]
///
(3, 4)
```



```
a[1.4, 0.8]
///
3
```



```
a[1,0]
///
3
```


The unfortunate thing is that SageX converts things to Py_ssize_t without
any type checking.  Maybe this is way faster ...  Anyway, it should be possible
to instead call whatever C library function __getitem__ uses, which would then
have the right behavior. 




---

Comment by was created at 2007-08-18 17:51:37

Changing component from algebraic geometry to linear algebra.


---

Comment by was created at 2007-08-18 17:51:37

Conclusion: call __index__


```
[10:28] <william> what do people think aabout #190?
[10:28] <william> The issue is that detecting fractional matrix indices will slow matrix indexing down.
[10:28] <dmharvey> that's pretty funny
[10:28] <mabshoff> Not sure yet.
[10:29] <william> Maybe a[0.5] could be the average of rows 0 and 1 ??  :-)
[10:29] <mabshoff> I am checking if the patch for #226 still applies.
[10:29] <robert457965> well, if it were a 0 by 0 matrix, you could just call iszero()
[10:29] <dmharvey> where is the code for that indexing method?
[10:29] <william> matrix/matrix0.pyx
[10:29] <william> around line 538
[10:30] <william> by the way, when people fix things, if you give them to me somehow, I can post them so
[10:30] <william> everybody else can get them with hg_sage.pull().
[10:30] <mabshoff> re #226 (with slight editing to account for pyrex->Cython:
[10:30] <mabshoff> patching file Cython/Compiler/ExprNodes.py
[10:30] <mabshoff> Hunk #1 succeeded at 2823 with fuzz 1 (offset 229 lines).
[10:31] <mabshoff> I will rebuild cython and then sage-2.8
[10:31] <william> does the bug still happen?
[10:32] <william> are you sure the patch is needed?
[10:32] <mabshoff> you mean: is it fixed without applying the patch?
[10:32] <william> yes
[10:32] <mabshoff> Not yet, but I will test with the original cython.
[10:32] <william> what's your test input?
[10:32] <william> i'll just wait..
[10:33] <mabshoff> There is a regression.pyx attached to the ticket. Give me a minute to sort it all out.
[10:34] <william> ok.
[10:34] <william> dmharvey -- are you looking at #190?
[10:34] <dmharvey> #190: do matrix subclasses generally override the getitem/setitme methods?
[10:34] <william> one bad thing is:  return self.row(int(key))
[10:35] <mabshoff> [mabshoff@m940 sage-2.8.1]$ cython regression.pyx
[10:35] <mabshoff> [mabshoff@m940 sage-2.8.1]$
[10:35] <william> no, they enver do.
[10:35] <mabshoff> That is without the patch.
[10:35] <dmharvey> ok
[10:35] <william> (regarding #190)
[10:35] <mabshoff> So #226 can be closed then.
[10:35] <william> not until i have the patch and have tested it too :-)
[10:36] <mabshoff> It was the original cython without the patch applied.
[10:36] <dmharvey> #190: so I guess the real question is: if someone tries to index on something like a Rational, which happens to be an integer, should that be allowed?
[10:36] <william> it's a simple patch.
[10:36] <william> ok.
[10:36] <william> #226 - oh -- it already works -- no patch needed?
[10:36] <mabshoff> Yes.
[10:36] <william> #190: yes.
[10:37] <william> #226: where is regression.pyx
[10:37] <mabshoff> The report for #226 was for pyrex 0.9.4.1, roughly 7 months old.
[10:37] <william> ok. mabshoff - you can have the honors of closing the bug.
[10:37] <mabshoff> attached to the ticket.
[10:38] <dmharvey> #190: well then it's tricky.... at some point you need to just trying to coerce to an integer index. But floats get rounded when you do that.
[10:38] <mabshoff> Mmh, I have to remember my trac password.
[10:38] <william> #190: what does magma do?
[10:39] <mabshoff> re #226: Reported by:  was
[10:39] <dmharvey> #190: actually there are two separate issues. One is speed; we could make the pathway faster by adding special code to test for Integer/int index. Second is sanity; are fractional indices allowed.
[10:39] <dmharvey> #190: let me check on magma; never done matrices before so gimme a few minutes
[10:39] <william> you are convincing me that we should just give an error if the input isn't int,long,Integer.
[10:39] <william> wait -- can't we have a fast version, and if that doesn't work, have a slow version?
[10:40] <mabshoff> william: How should we handle fixed bugs?
[10:40] <mabshoff> Add some text (in this case) stating: Was fixed in a previous release of cython.
[10:40] <william> for the sage library, make them available to me in any way, and I'll (1) put them in the official
[10:40] <mabshoff> cython regressioin.pyx works.
[10:40] <william> hg repository; for other things, I'll put them in /home/was/bug/
[10:41] <william> oh -- and post verbosely to trac!
[10:41] --> ncalexan has joined this channel (n=user@d207-216-25-207.bchsia.telus.net).
[10:41] <william> hi nick.
[10:41] <william> where you at?
[10:41] <ncalexan> Hi folks... I can't stay long, relaxing with the family, but thought I'd see how things were.
[10:41] <ncalexan> Victoria, BC.
[10:41] <dmharvey> #190: magma raises an error "Runtime error in '[]': Bad argument types"
[10:41] <ncalexan> You?
[10:41] <william> i wonder what nick things.
[10:41] <william> nick thinks.
[10:42] <william> nick, if a is a matrix, and n = QQ(5), should a[n,n] be an error or not?
[10:42] <dmharvey> #190: my preference is to allow only int/long/Integer
[10:42] <dmharvey> hi nick
[10:42] --> paulolivier_sage has joined this channel (i=8143024e@gateway/web/cgi-irc/ircatwork.com/x-f7a7e0b894111559).
[10:42] <william> wait!
[10:42] <-- paulolivier_sage has left this server (Client Quit).
[10:42] <william> we should do whatever python lists do, shouldn't we?
[10:42] <ncalexan> Yes.  That's a reasonable answer.
[10:43] <william> also, we should look at what numpy arrays and matrices do.
[10:43] <dmharvey> sure
[10:43] <ncalexan> That probably means calling __int__ or something similar, no?
[10:43] <william> python lists have an __index__ protocol as of python 2.5.
[10:43] --> pauloliviersage has joined this channel (i=8143024e@gateway/web/cgi-irc/ircatwork.com/x-539b7d4cf887a650).
[10:43] <william> NO.
[10:43] <ncalexan> Yeah, I think we best stick with that then.
[10:43] <ncalexan> ?
[10:43] <william> #190: A python list will call __index__ and if that works, use it. otherwise fail.
[10:44] <william> So anybody can make their own new class that can index into lists, etc., if they want.
[10:44] <dmharvey> #190: ah that explains why you can index on an Integer
[10:44] <william> I used to have to do this crap in the preparser: v = [1,2,3]
[10:44] <william> v[Integer(2)]
[10:44] <william> it totally sucked.
[10:44] <william> We don't want to make SAGE users who make new classes suffer that way.
[10:44] <william> #190 -- where?
[10:45] <dmharvey> #190: sorry, I mean for a python list
[10:45] <william> there must be a python/c api call to get foo.__index__()
[10:45] <dmharvey> #190, i.e. v[Integer(2)] works, but v[2.5] doesn't
[10:45] <ncalexan> Why was it bad?
[10:45] <william> #190: yep, that's good.
[10:45] <william> but if somebody wanted to make their own "2.5" and define an index method on it, then it would work.
[10:45] <william> That's the best way to go.
[10:45] <mabshoff> Ok, I close #226
[10:45] <mabshoff> +d
[10:46] <william> thanks!
[10:46] <william> 3 down.
[10:46] <ncalexan> Ah, so it was too slow?
[10:46] <mabshoff> But I think I found a bug in cython.
[10:46] <william> 33 to go.
[10:46] <william> report the cython bug to track
[10:46] <mabshoff> cython -v doesn't work as expected.
[10:46] <dmharvey> #190: so conclusion is that Matrix.__getitem__ should use call __index__? instead of coercing to int?
[10:46] <william> #190: no -- the problem was that it wasn't meaningful
[10:46] <mabshoff> It just prints the standard help text.
[10:46] <william> #190 http://www.sagemath.org:9002/sage_trac/ticket/190
[10:47] <william> mabshoff -- agreed.  report it.
[10:47] <william> #190: use.
[10:47] <william> #190: dmharvey -- yes.
[10:47] <dmharvey> #190: ok I will try to code thisup
[10:48] <william> thanks!!
[10:48] <william> i'm pasting this part of the transcript from irc into trac, since it explains the decision well.
```



---

Attachment

partial fix for bug


---

Comment by dmharvey created at 2007-08-18 18:52:40

I just attached a partial fix: this addresses the `M[1.5]` problem, but still doesn't deal with `M.row(1.5)` --- robertwb has proposed a cython language change to deal with this (changing `size_t` conversions to go via `__index__`)


---

Comment by dmharvey created at 2007-08-18 18:57:20

see also #440, regarding speed of indexing off Integer objects


---

Comment by was created at 2007-08-18 20:58:29

fixed with the attached patch and improvements to cython.


---

Comment by was created at 2007-08-18 20:58:29

Resolution: fixed


---

Comment by robertwb created at 2007-08-19 00:47:59

Replying to [comment:2 dmharvey]:
> I just attached a partial fix: this addresses the `M[1.5]` problem, but still doesn't deal with `M.row(1.5)` --- robertwb has proposed a cython language change to deal with this (changing `size_t` conversions to go via `__index__`)

This has now been fixed in Cython.
