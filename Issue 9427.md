# Issue 9427: implement fricas integrator

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2010-07-05 08:48:40

Assignee: burcin

CC:  hemmecke

Keywords: integrate, fricas

The attached patch adds the option algorithm="fricas" to the integrate
command.


---

Comment by whuss created at 2010-07-05 08:51:37

Changing status from new to needs_review.


---

Attachment


---

Comment by burcin created at 2010-07-05 09:07:20

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-07-05 09:07:20

This looks great. Thanks for the quick patch!

I have a few minor comments:
 * the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:
 {{{
sage: infinity._fricas_init_()
"%plusInfinity"
}}}
 and we can just do af = a._fricas_().
 * Similarly, I suggest moving the code for converting the result back to the `_sage_()` method of the fricas interface.


---

Attachment

Replying to [comment:2 burcin]:
>  * the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:
>  {{{
> sage: infinity._fricas_init_()
> "%plusInfinity"
> }}}

I tried this (see fricas_infinity.patch), but for some reason that I don't understand the output of
_fricas_init_() changes into something which is not a valid fricas expression.


```
sage: oo._fricas_init_()
'%plusInfinity'
```


but


```
sage: oo._fricas_()
+ infinity
```


I have no idea what is going on here.


---

Comment by drkirkby created at 2010-07-06 23:34:10

Is "algorithm" the most appropiate word here? To me, Fricas, Aximom, Maxima etc are software packages, not algorithms. They implement many differerent algorithms.

I'm not a mathmatician, but certainly my mathematical training would never have suggested that Fricas was an algorithm. 

I would have thought something like


```
integrate(f(x), x, use="fricas") 
integrate(f(x), x, software="fricas") 
integrate(f(x), x, method="fricas") 
```


would be better than 


```
integrate(f(x), x, algorithm="fricas") 
```


I don't claim any of my choices are optimal, but I think all of them are better than "algorithm". 

Dave


---

Comment by whuss created at 2010-07-07 07:40:01

Replying to [comment:4 drkirkby]:

If I do


```
sage: search_def('algorithm=')
```


I get *150* results. So the 'algorithm' convention is widely
used in Sage, I don't think it makes sense to change this
at this point.


---

Comment by burcin created at 2011-05-10 17:21:09

Replying to [comment:3 whuss]:
> Replying to [comment:2 burcin]:
> >  * the conversion of different infinities on line 95-103 should be moved to the `_fricas_init_()` method of the corresponding classes. Then this would work:
  {{{
 sage: infinity._fricas_init_()
 "%plusInfinity"
 }}}
> 
> I tried this (see fricas_infinity.patch), but for some reason that I don't understand the output of
> _fricas_init_() changes into something which is not a valid fricas expression.
> 
 {{{
 sage: oo._fricas_init_()
 '%plusInfinity'
 }}}
> 
> but
> 
> {{{
> sage: oo._fricas_()
> + infinity
> }}}
> 
> I have no idea what is going on here.

This seems to be how fricas prints `%plusInfinity`. Ralf, can you help us with this?


---

Comment by hemmecke created at 2011-05-10 18:08:51

Well, not quite right, as http://axiom-wiki.newsynthesis.org/PerCent shows. I've added

```
)set output algebra on
```

in order to also show the ascii output. Otherwise mathaction renders tex output of axiom. These things starting with a percent sign are only used for input. What exactly gets printed depends on the ')set output' settings.


---

Comment by hemmecke created at 2011-05-10 18:20:18

Also look at the exports of OrderedCompletion.
https://github.com/hemmecke/fricas-svn/blob/master/src/algebra/complet.spad.pamphlet#L20
Obviously also 'plusInfinity()' and 'minusInfinity()' could be used as input.

The output is constructed in
https://github.com/hemmecke/fricas-svn/blob/master/src/algebra/complet.spad.pamphlet#L59
How the symbol infinity appears is hidden inside OutputForm and probably deeper.

```
)set output tex on
(1) -> plusInfinity()      

   (1)   + infinity
$$
+\infty 
\leqno(1)
$$

                                             Type: OrderedCompletion(Integer)
```



---

Comment by burcin created at 2011-05-10 18:33:06

So the ascii output for plusInfinity is "+ infinity" and the `_fricas_init_()` method in attachment:fricas_infinity.patch works as intended.

Wilfried, will you have time to revise the patch? Note that when #9880 is merged (almost) all symbolics patches will need to be rebased.


---

Comment by vdelecroix created at 2014-12-07 12:04:07

Replying to [comment:4 drkirkby]:
> Is "algorithm" the most appropiate word here? To me, Fricas, Aximom, Maxima etc are software packages, not algorithms. They implement many differerent algorithms.
> 
> I'm not a mathmatician, but certainly my mathematical training would never have suggested that Fricas was an algorithm. 
> 
> I would have thought something like
> 
> {{{
> integrate(f(x), x, use="fricas") 
> integrate(f(x), x, software="fricas") 
> integrate(f(x), x, method="fricas") 
> }}}
> 
> would be better than 
> 
> {{{
> integrate(f(x), x, algorithm="fricas") 
> }}}
> 
> I don't claim any of my choices are optimal, but I think all of them are better than "algorithm". 

+1 for `use`, `software` or `library`
Moreover, in some situation, when we call the software (fricas, maxima, ...) we might want to feed it with an option `algorithm`.

Vincent


---

Comment by chapoton created at 2014-12-07 17:00:27

I have made a git branch with the attached files, rebased on 6.5.b2
----
New commits:


---

Comment by rws created at 2015-02-02 09:56:11

Replying to [comment:14 vdelecroix]:
> Moreover, in some situation, when we call the software (fricas, maxima, ...) we might want to feed it with an option `algorithm`.
First I agreed with this, but now I think it would be easy to allow something like `algorithm=fricas-risch`, and this would then be more convenient than `software=fricas,algorithm=risch`. Whereas changing `algorithm` to `software` would be annoying as hell.


---

Comment by rws created at 2015-02-02 10:08:11

Replying to [comment:2 burcin]:
>  * Similarly, I suggest moving the code for converting the result back to the `_sage_()` method of the fricas interface.
I know this is how Sympy does it but I think such a decision is up to the Fricas developers.


---

Comment by git created at 2015-02-02 10:38:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2015-02-02 10:41:46

This looks good and tests OK in `symbolic` and `rings`.


---

Comment by rws created at 2015-02-02 10:41:46

Changing status from needs_work to needs_review.


---

Comment by rws created at 2015-02-02 10:42:06

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-02-17 19:28:27

Resolution: fixed
