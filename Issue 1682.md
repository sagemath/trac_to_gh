# Issue 1682: Turn on implicit multiplication per default

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-04 18:13:41

Assignee: was

This is the second patch from #1576 which turns on implicit multiplication per default. We will wait to merge this past 2.9.2.

Cheers,

Michael


---

Attachment

patch by was


---

Comment by was created at 2008-01-09 04:18:34

I just want to commment that this afternoon somebody came up to me at the Sage booth and really really wanted implicit multiplication by default, and was quite happy when I demoed it for them. 

I'll ask Robert to referee this patch "turning it on".  He might want to do something
a little more sophisticated, though I would be very reluctant to support that (e.g., adjusting the level -- which is dangerous since library code could also use the preparser and may depend on the default level). 

William


---

Comment by robertwb created at 2008-01-09 04:43:56

I think the default level is the right one (hence the default). I would be happy to see this patch go in, but will add more documentation first...


---

Attachment


---

Comment by zimmerma created at 2008-01-09 14:05:57

Sorry if I come late in this discussion, but I want to warn about possible implications of this
change. Firstly the fact that "a b" is parsed as "a*b" is the reason which forced Mathematica to
introduce a different kind of parenthesis for function calls, like Sin[x] instead of Sin(x),
because Sin (x) could be parsed as Sin * (x). You will say that if Sin is a functional operator,
then Sin (x) should be parsed as Sin(x). But what about f (g), where f and g are both
functional operators? Should it be parsed as the composition of f and g, or as f*g? 
What about t [1]? Should it be parsed as the element of index 1 of the list t, or as the 
multiplication of each element of [1] by t? Note that Mathematica had to introduce t{{1}} to
access indices of arrays or lists for the same reason.

In understand that parsing "a b" as "a*b" might be very attractive for interactive usage, but
it will lead to some ambiguities, some of which are explained above, and maybe some others I'm
not yet aware of. Those ambiguities might force to change back, or to make fundamental changes
in the language syntax. Therefore I strongly recommend to consider all possible implications 
before doing that fundamental change.

If you want to count people which are happy without implicit multiplication, I am! Why not
letting the user decide in his/her init.sage file to enable implicit multiplication?


---

Comment by robertwb created at 2008-01-09 20:36:37

The implicit multiplication code is very conservative. It doesn't mangle any valid python, so something like "sin(x)" won't be touched at all. The places implicit multiplication is inserted are (default level 5):


```
        code  -- the code with missing *'s
        level -- how agressive to be in placing *'s
                   0) Do nothing
                   1) numeric followed by alphanumeric
                   2) closing parentheses followed by alphanumeric
                   3) Spaces between alphanumeric
                  10) Adjacent parentheses (may mangle call statements)
                   
    EXAMPLES: 
        sage: from sage.misc.preparser import implicit_mul
        sage: implicit_mul('(2x^2-4x+3)a0')
        '(2*x^2-4*x+3)*a0'
        sage: implicit_mul('a b c in L')
        'a*b*c in L'
        sage: implicit_mul('1r + 1e3 + 5exp(2)')
        '1r + 1e3 + 5*exp(2)'
        sage: implicit_mul('f(a)(b)', level=10)
        'f(a)*(b)'
```


For me personally, I don't mind typing "a*b" instead of "a b", but being able to do stuff like "2x^3-3x+1" is really nice.


---

Comment by robertwb created at 2008-01-09 20:37:32

Sorry, `2x^2-3x+1`.


---

Comment by dmharvey created at 2008-01-10 02:46:41

Gosh. I really don't like this at all.

By all means, go ahead and merge it --- I can see your arguments for enabling it --- but I think it's finally come to the day where I switch off the preparser in my copy of sage altogether.


---

Comment by mabshoff created at 2008-01-10 03:01:40

I tend to agree with Paul on this, that the implicit multiplication leads to ambiguities. While it might be convenient for some people and a much requested feature you should consider that once it is activated per default you cannot push toothpaste back in the tube once you have pushed it out.

So I would suggest just as Paul said that people can activate this in the sage.ini file or wherever.  Make it a prominent part of the tutorial so that people know about it. That might be a compromise for now and let's reevaluate this down the road. I don't think I will change my opinion, mostly because I have discussed the same issue in the CoCoA language where `f (g)` and `f(g)` can mean different things. And the backward compatibility hell that this causes for a CoCoA 5 parser is quite a pain, so my vote is negative on merging this patch now.

*If* this gets merged it shouldn't have some knob to turn, since this will very likely cause us to investigate the knob value for bug reports on sage-support.

Cheers,

Michael


---

Comment by was created at 2008-01-10 03:29:11

> I tend to agree with Paul on this, that the implicit 
> multiplication leads to ambiguities.

No it doesn't.  

> While it might be convenient for some people and 
> a much requested feature you should consider that 
> once it is activated per default you cannot push 
> toothpaste back in the tube once you have pushed it out.

Yes we can.   If it turns out to really be a problem
we can change or eliminate it.  

> So I would suggest just as Paul said that people 
> can activate this in the sage.ini file or wherever. 
> Make it a prominent part of the tutorial so that
>  people know about it.

I disagree with this.  Sage should make clear choices
instead of having tons of complicated configuration 
options.  

> That might be a compromise for now and let's 
> reevaluate this down the road. I don't think
> I will change my opinion, mostly because I have
> discussed the same issue in the CoCoA language
> where f (g) and f(g) can mean different things.

You do understand that the Sage implicit multiplication
does not apply at all in the above cases, since it doesn't
do anything with adjacent parenthesis.  In fact the
implicit multiplication code only has any effect at all
on expressions that would otherwise be syntax errors. 

> *If* this gets merged it shouldn't have some knob to 
> turn, since this will very likely cause us to 
> investigate the knob value for bug reports on sage-support.

I disagree.  We should enable it and if it turns out
that people do make syntax error that suddenly become
valid and this results in actual confusion, then we revisit
this question.   

William


>  And the backward compatibility hell that this causes for a CoCoA 5 parser is quite a pain, so my vote is negative on merging this patch now.


---

Comment by was created at 2008-01-10 03:39:23

From Paul:

> Sorry if I come late in this discussion, but I want to warn about 
> possible implications of this change. Firstly the fact that "a b" 
> is parsed as "a*b" is the reason which forced Mathematica to
>  introduce a different kind of parenthesis for function calls,

That's not true unless you mean a and b to be completely general expressions.

> like Sin[x] instead of Sin(x), because Sin (x) could be parsed as 
> Sin * (x). You will say that if Sin is a functional operator, then 
> Sin (x) should be parsed as Sin(x).

No.

>  But what about f (g), where f and g are both functional operators? 

The implicit multiplication that Robert implemented does *nothing* 
in that case.  It's much more minimal -- it never ever changes anything
unless it would have been a syntax error in Python. 

> Should it be parsed as the composition of f and g, or as f*g? 

A composition, since it is as valid python.

> What about t [1]? Should it be parsed as the element of
> index 1 of the list t, or as the multiplication of each 
> element of [1] by t? Note that Mathematica had to
>  introduce t{{1}} to access indices of arrays or lists for the same reason.

Again t [1] is valid Python so it is not touched. 

> In understand that parsing "a b" as "a*b" might be very 
> attractive for interactive usage,

It is very useful for interactive use so long as one is careful
about what is meant by a and b above. 

>  but it will lead to some ambiguities, 

I can't think of any ambiguities at all in what Robert proposes. 

> some of which are explained above, and maybe 
> some others I'm not yet aware of. Those ambiguities might 
> force to change back, or to make fundamental changes in

If there are any (I don't think there are), then changing back
would not be the end of the work. 

>  the language syntax. Therefore I strongly recommend to 
> consider all possible implications before doing that 
> fundamental change.

> If you want to count people which are happy without implicit
> multiplication, I am! Why not letting the user decide in his/her
>  init.sage file to enable implicit multiplication?

You can simply ignore it.  You'll never know it is there. 
Why make customization complicated when it's not necessary
to do so.  Sage isn't emacs. 

 -- William


---

Comment by was created at 2008-01-10 08:19:39

There is one BUG with this:

{{
sage: time 2+2
------------------------------------------------------------
   File "<timed exec>", line 1
     *Integer(2)+Integer(2)
     ^
<type 'exceptions.SyntaxError'>: invalid syntax
}}}


```

sage: time v=5
------------------------------------------------------------
   File "<timed exec>", line 1
     *v=Integer(5)
     ^
<type 'exceptions.SyntaxError'>: invalid syntax

```



---

Comment by robertwb created at 2008-01-10 08:44:41

Wow, there are a lot of people that don't like the idea of having implicit multiplication available! On the other hand, there are several people (including some I ran into at the AMS booth) who were very enthusiastic about the idea. I think this is especially important for reaching out to the high school-undergrad calculus audience. 

If we were to have an option then it should be on by default (as those most likely to want it are not probably going to be the least likely to know how to change the settings, and also so that code from both [non-implicit-mul] and [implicit-mul] folks would run in plan-vanilla Sage). That being said, I think lots of configuration options is a bad idea when it can be avoided. 

As far as the concerns that this makes the parser more complicated, the entire thing is implemented in 24 lines of code, and (in my opinion) one of the most understandable chunks of the preparser (assuming one knows a little bit about regular expressions). 

For those of you who are against this patch, I would like you to do `from sage.misc.preparser import implicit_mul` and please find examples where it either

(1) does the wrong thing 

or 

(2) would get in your way.


---

Attachment

fix "time ..." bug


---

Comment by dmharvey created at 2008-01-10 13:40:12

Replying to [comment:14 robertwb]:
> For those of you who are against this patch, I would like you to do `from sage.misc.preparser import implicit_mul` and please find examples where it either
> 
> (1) does the wrong thing 
> 
> or 
> 
> (2) would get in your way. 

No, this isn't the problem for me. It's not implicit multiplication in particular. It's the whole preparser thing in general.

For me this is the straw that broke the camel's back: I have finally switched off the preparser in my sage installation, we'll see how long I last. Maybe I've gone to heaven, maybe to hell, we'll see.

Do you know, when I first ran into sage (when there was a *lot* less crud in the preparser), the preparser was probably the single most difficult thing for me to get my head around. I was basically learning python and sage at the same time, and a lot of things totally didn't make sense for a while. Like what the hell is R.<x>? (Is that a member of R? Are variable names even allowed to start with < in python? Is that some weird python syntax for adding members to an object? *Is* it even python syntax at all? I better go look that up.)

I still bash my head against the wall every time I'm writing library code and forget to replace the caret by **, or forget that when I divide an integer by an integer I need to (sometimes) wrap them with Integer calls. You call it a convenience, but do I ever make those kind of mistakes when programming in C? No: in C, literals have clear and predictable semantics, and I like that, because it saves me needing to think. In Sage, the meaning of a literal changes depending on who is reading the code, and I hate that. I need to do extra thinking *every time I write down an integer*.

Whenever I make this complaint, William always comes back with "well just run the preparser on your code before you put it in the library". If I'm editing library code, am I supposed to copy it back out to the sage prompt, edit it there, then re-run the preparser, copy it back to the library (and then delete all the extraneous Integer calls which slow it down)? Surely not. And apart from that solution producing ugly code and being impractical (William, do you really use the preparser this way?), it's completely missing the point: the problem is that it's infected my brainspace. I'm learning two different languages which are *very* similar, which is much harder than learning two totally different languages. It's made me much less confident in the Sage language, i.e. if I want to convince myself that a piece of code does what I think it does, I have to work much harder. I've really noticed that when I write C code, I strive for it to be "correct", but when I write code in Sage (library or otherwise), I only go for "mostly correct", mainly because of flakiness like this.

It says on the main page "You work with SAGE using the highly regarded scripting language Python instead of an obscure language designed for a particular mathematics program". Yeah right. Not any more, guys.

This implicit multiplication thing is a part of a general trend in Sage that I've noticed: it's aiming to cater more and more to "the dummies" (apologies for the political incorrectness). You're adding crud to the preparser so that people can type "2x + 3" instead of "2*x + 3", because that's what they are used to writing on paper. Well you're basically separating your audience into two pieces: some people who don't have any idea about python and preparsers and probably even programming in general, and the rest of us poor sods who do understand these things. You know what's going to happen. As soon as Sage starts getting more users, you're going to get a flood of emails to sage-support like "why does 2x+3 work but (x+3)(x+4) gives me x+7 in sage?" How do you reply to that? Explain the preparser to them? "Fix" the preparser even more, running straight into the ambiguities Paul brought up? Tell them "well in Sage we try to make things easy for you by making 2x work, but we can't quite make the second example work, so you'll just have to use the multiplication operator anyway"? Is that harder or easier than just using * in the first place?

Another example of this creeping audience thing: I hate that "sqrt" and "floor" and all those sorts of functions have been hijacked by the calculus package, and have become ludicrously slow. Now I have to constantly track down the right version of these functions which will run at an acceptable speed.

Okay I might leave my rant there. It seems like Sage is heading towards a different audience, an audience that doesn't include me, but maybe if we want be a "viable alternative to Mathematica, Maple, and MATLAB", then that's what we gotta do. But I've switched off my preparser.

david

p.s. I'm interested to hear Nick Alexander's take on this issue.


---

Comment by robertwb created at 2008-01-10 18:52:05

I'm running off to the airport, so this may be hasty, but I had to  
respond to this (very valid) criticism.

>  No, this isn't the problem for me. It's not implicit  
> multiplication in
>  particular. It's the whole preparser thing in general.
>
>  For me this is the straw that broke the camel's back: I have finally
>  switched off the preparser in my sage installation, we'll see how  
> long I
>  last. Maybe I've gone to heaven, maybe to hell, we'll see.

I'm very curious, but I know where I'd be :-).

>  Do you know, when I first ran into sage (when there was a *lot*  
> less crud
>  in the preparser), the preparser was probably the single most  
> difficult
>  thing for me to get my head around. I was basically learning  
> python and
>  sage at the same time, and a lot of things totally didn't make  
> sense for a
>  while. Like what the hell is R.<x>? (Is that a member of R? Are  
> variable
>  names even allowed to start with < in python? Is that some weird  
> python
>  syntax for adding members to an object? *Is* it even python syntax  
> at all?
>  I better go look that up.)
>
>  I still bash my head against the wall every time I'm writing  
> library code
>  and forget to replace the caret by **, or forget that when I  
> divide an
>  integer by an integer I need to (sometimes) wrap them with Integer  
> calls.
>  You call it a convenience, but do I ever make those kind of  
> mistakes when
>  programming in C? No: in C, literals have clear and predictable  
> semantics,
>  and I like that, because it saves me needing to think. In Sage, the
>  meaning of a literal changes depending on who is reading the code,  
> and I
>  hate that. I need to do extra thinking *every time I write down an
>  integer*.

I know I made these kind of mistakes in programing languages long  
before I used Sage, and this kind of syntactic sugar is what makes  
"Python" usable as a CAS language. Having to write Integer(3) *every time I want to use an integer* is unacceptable as well.

>  Whenever I make this complaint, William always comes back with  
> "well just
>  run the preparser on your code before you put it in the library".  
> If I'm
>  editing library code...

I don't know anyone who does this except perhaps when they're first  
starting out (when it is a very useful technique).

>  the problem is that it's infected my
>  brainspace. I'm learning two different languages which are *very*  
> similar,
>  which is much harder than learning two totally different  
> languages. It's
>  made me much less confident in the Sage language, i.e. if I want to
>  convince myself that a piece of code does what I think it does, I  
> have to
>  work much harder. I've really noticed that when I write C code, I  
> strive
>  for it to be "correct", but when I write code in Sage (library or
>  otherwise), I only go for "mostly correct", mainly because of  
> flakiness
>  like this.

Personally, I find jumping Sage <--> Python (<--> Cython) to be not  
that difficult. The preparser is similar (in purpose) to the  
notebook, it gives and easier interface to the computational engine  
underneath. Of course, you're not a notebook guy either...

>  It says on the main page "You work with SAGE using the highly  
> regarded
>  scripting language Python instead of an obscure language designed  
> for a
>  particular mathematics program". Yeah right. Not any more, guys.

Compared to any other system, I think this is true. You can use pure  
Python if you want, but if you're lazy (like me) Sage can do some CAS- 
specific things for you too.

>  This implicit multiplication thing is a part of a general trend in  
> Sage
>  that I've noticed: it's aiming to cater more and more to "the  
> dummies"
>  (apologies for the political incorrectness).

Yes, and I think this is a good thing. The center of balance is  
changing because things are getting added to the "lower" end of the  
scale, not because the "upper" end is getting smaller. If things are  
introduced that truly make it worse for the "experts" then that would  
be a harder thing to justify, but here I think it is beneficial  
across the board. In fact I wouldn't be surprised there are a lot of  
old-time mathematicians who would find having to insert the * in "2x"  
more counter-intuitive than the rising generation of computer- 
literate calc students.

>  As soon as Sage starts getting more users, you're
>  going to get a flood of emails to sage-support like "why does 2x+3  
> work
>  but (x+3)(x+4) gives me x+7 in sage?" How do you reply to that?  
> Explain
>  the preparser to them? "Fix" the preparser even more, running  
> straight
>  into the ambiguities Paul brought up?

No.

> Tell them "well in Sage we try to
>  make things easy for you by making 2x work, but we can't quite  
> make the
>  second example work, so you'll just have to use the multiplication
>  operator anyway"?

Yes, this is the kind of thing for a FAQ.

> Is that harder or easier than just using * in the first
>  place?

Yes.

>  Another example of this creeping audience thing: I hate that  
> "sqrt" and
>  "floor" and all those sorts of functions have been hijacked by the
>  calculus package, and have become ludicrously slow. Now I have to
>  constantly track down the right version of these functions which  
> will run
>  at an acceptable speed.

I agree with you here! Not sure what the best solution is for this  
though.

>  Okay I might leave my rant there. It seems like Sage is heading  
> towards a
>  different audience, an audience that doesn't include me, but maybe  
> if we
>  want be a "viable alternative to Mathematica, Maple, and MATLAB",  
> then
>  that's what we gotta do. But I've switched off my preparser.

I think the audience is getting bigger, but not excluding people like  
us.

It seems like with the preparser your sensibilities as a programmer  
are more offended than your sensibilities as a mathematician, right?  
(Of course, to use Sage more than causally one has to be both.)

- Robert


---

Comment by was created at 2008-01-14 13:53:46

EXECUTIVE SUMMARY:

I have decided *not* to have implicit multiplication on by default.  It should be an easy-to-turn on option for those who really need it.  

The reasons:
  1. "import this" outputs "Explicit is better than implicit."
  
  2. We should use the preparser only when strictly necessary.

  3. There have only ever been two requests for this functionality, but more than two people spoke up against it. 

  4. If the target audience of Sage doesn't solidly include David Harvey, then it doesn't include me either, and we have completely lost our way.  We can't let that happen.


---

Attachment

The above patch makes this optional via an `implicit_multiplication(...)` function. All patches should be applied.


---

Comment by mabshoff created at 2008-01-15 06:05:25

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 06:05:25

All four patches applied to Sage 2.10.alpha3
