# Issue 9670: Bring probability/random_variable.py to 100% coverage

Issue created by migration from https://trac.sagemath.org/ticket/9670

Original creator: kcrisman

Original creation time: 2010-08-02 19:55:09

Assignee: mvngu

CC:  kohel pelegm pang

Currently, this file is pretty woeful.

```
probability/random_variable.py: 3% (1 of 29)
```



---

Comment by kcrisman created at 2010-08-02 20:03:00

The only thread about this I can find on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/533249e757f61636/00289c1374494e4d?lnk=gst&q=Discrete+probability+space#) seems relevant but short on examples.

There are also some minor bugs in checking for errors, which apparently have never occurred.  There is also some use of multiple inheritance, but it's not clear why (see [here](http://docs.python.org/release/1.5.1p1/tut/multiple.html) for the official view on this), although see the above thread for another view.

I'm posting a partial patch, but before I spend more time on this, I'd like to know if the original author has any comments - particularly as to what sort of examples were expected with `RandomVariable`, since there weren't any in the original.  Also as to whether the doc upgrades thus far are on track.


---

Attachment


---

Comment by was created at 2012-01-26 19:42:19

Changing type from enhancement to defect.


---

Comment by was created at 2012-01-26 19:42:19

This file is a great example of "if it isn't tested, it's totally broken!"  I've never used any of this code before just now when I grad student walked into my office and asked how to use it.  He (fortunately) couldn't even get started because typing `DiscreteProbabilitySpace?` in the notebook provides absolutely no help at all (strangely, in the command line, it does).   So I looked at the code and came up with the first trivial example:


```
sage: n=6; P = dict([(i,1/n) for i in [1..n]])
sage: X = DiscreteProbabilitySpace(P.keys(), P)
sage: X
Discrete probability space defined by {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
sage: X.expectation()
0.166666666666667
```


Literally, the first thing I tried came out completely wrong!  That's sure as hell not the expectation, which should be sum i*1/n = n*(n+1)/2/n = (n+1)/2 = 7/2.    

I then looked at the code for expectation.  It's obviously got not test (and don't worry kcrisman -- you didn't add any), and the code itself is just wrong:

```
    def expectation(self):
        r"""
        The expectation of the discrete random variable, namely
        `\sum_{x \in S} p(x) X[x]`, where `X` = self and
        `S` is the probability space of `X`.
        """
        E = 0
        Omega = self.probability_space()
        for x in self._function.keys():
            E += Omega(x) * self(x)
        return E
```


I don't know why it does Omega=..., since self.probability_space() is self is True.
I don't know why this doesn't use a single list comprehension line.  

Here self._function is the dictionary: `{1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6`}.
So the code should be:

```
def expectation(self):
    return sum(x*self(x) for x in self._function.keys())
```

right?  

Indeed,

```
sage: self=X;  sum(x*self(x) for x in self._function.keys())
3.50000000000000
```


But that said, what's up with the floating point numbers?  Shouldn't the answer be exact?

```
sage: type(self(1))
<type 'sage.rings.real_mpfr.RealNumber'>
```


There is a way to deal with this:

```
sage: X = DiscreteProbabilitySpace(P.keys(), P, codomain=QQ)
sage: self=X;  sum(x*self(x) for x in self._function.keys())
7/2
```

But shouldn't the default codomain depend on the dictionary P?   It should take the values and find a common parent for them (e.g., using Sequence), then take the fraction field of that.  

In defense of the original code, David K. wrote it before Sequence existed, and we were just figuring out how to use Python at the time.... and didn't know if Sage would have more than 3 users. 

Anyway, this code as is scary and needs massive, massive reworking.  

And since I'm reporting a specific bug, I am changing this to a defect.


---

Comment by kohel created at 2012-01-26 22:20:06

I agree the code (among the first I wrote) should be improved or rewritten.

Also note that "discrete" should be "finite" -- I never implemented any code  for infinite discrete probability spaces and the finiteness of X a rather heavy assumption.

That said, despite the lack of documentation, I assert that the above output  is correct.  The idea of the discrete or finite probability spaces is that  the underlying set S of X can be anything:


```
sage: n = 6 sage: S = list('abcdef') 
sage: P = dict([(S[i],1/n) for i in [1..n]]) 
sage: X = DiscreteProbabilitySpace(S, P) 
sage: X.expectation() 
0.166666666666667
```


It so happens that a probability function IS a random variable so that  one can ask for its expectation.  Thus probability space inherits from  random variables which generalize them.

With S so defined, it should be clear that it certainly doesn't make  sense to form \sum_{x \in S} x p(x), since S need not be contained in  a module over the reals for which this sum makes sense.  Rather for a  probability space, the expectation is \sum p(x)<sup>2.</sup>

For reasons of avoiding coefficient blowup in the rationals, the default  uses a real ring. This is a design decision which is perhaps questionable, but avoids problems with undergraduate teaching. If you want the  probability space with value ring in the rationals, then explicitly set  the codomain:


```
sage: X = DiscreteProbabilitySpace(S, P, codomain = QQ) 
sage: X.expectation() 
1/6
```


To get the random variable you intended, you need to first create the  probability space as above, then define the random variable with respect  to this:


```
sage: f = dict([(S[i],i+1) for i in range(n)]) 
sage: F = DiscreteRandomVariable(X,f) 
sage: F.expectation() 
3.50000000000000
```


Again, for exact values, set the codomain:


```
sage: F = DiscreteRandomVariable(X,f,codomain = QQ) 
sage: F.expectation() 
7/2
```


This two-step creation for a random variable is a bit awkward  if all you want is the uniform probability function. Since this  occurs quite often in practice (for a finite probability space), it might be practical to have a shortcut which defines the  uniform probability space by default.  In that case the syntax  might be changed from (X,f,codomain) to (f,X,codomain), or  without change, just letting X be a list or finite set and  setting up the uniform probability on it.  This is NOT implemented, but would be a more intuitive construction for what you intended:


```
sage: S = list('abcdef') 
sage: F = DiscreteRandomVariable(S,dict([(S[i],i+1) for i in range(n)])) 
sage: X = F.probability_space(); X 
Discrete probability space defined by {'a': 1/6, 'c': 1/6, 'b': 1/6, 'e': 1/6, 'd': 1/6, 'f': 1/6}
```


At the time of writing this (and maybe still true) there was no class of finite sets and morphisms of sets, which would provide  a more natural input to the constructors for probability space  and random variables.  It would be a cleaner construction to  have the codomain attached to the function f or probability  function p, and have some general mechanism for checking that  the domains of f and p agree and that codomain of f is a module  over the codomain of p. Python dictionaries were the closest  I could come (without implementing a category of sets) to the  datastructure for morphism of sets.

Currently the domain of a random variable is assumed to be some  real ring or subring but vector-valued random variables would  make sense in a number of settings.


---

Comment by was created at 2012-01-26 22:31:38

David -- many thanks for the clarification.  I obviously completely misunderstood how your code was supposed to work.  I've changed this ticket back to "enhancement".  Thanks also for the hints about how to improve the code.


---

Comment by was created at 2012-01-26 22:31:38

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2012-01-27 01:33:57

Thanks for the discussion here.  I just want to point out that #10770 fell afoul of this as well, and that [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8febda1b92330c85/9cea7249b186d8e5) and #11572 also had some issues because of wondering where the binomial distribution belonged, which seems somehow related. ?


---

Comment by was created at 2012-01-27 05:24:39

Some remarks from Tvrtko Tadic, a UW grad student in probability:

```
I don't think discrete probability
space needs to have an expectation (as a function).
It could be
for example that a kid gets an apple with probability 1/2,
and a orange with probability 1/2. We can't sum
half an apple and half an orange.

So I don't think the class DiscreteProbabilitySpace should
have an expectation method at all.
It could be that somebody started an expectation
method in the wrong class and the forgot about it.

I tried the expectation for DiscreteRandomVariable, and it works
fine. (Random variables take values in real numbers,
and the expectation is defined for them not for
probability spaces.)

EXAMPLE (DICE):

P=dict([(i,1/6) for i in [1..6]])
Omega=[1..6]

PS=DiscreteProbabilitySpace(Omega,P)

f=dict([(i,i) for i in [1..6]])
X=DiscreteRandomVariable(PS,f)

X.expectation()# (it should be 7/2)
X.variance() # (it should be 35/12)

It works!

I will take a look at the other packages Sage has
for probability (and related areas) that you mentioned.

Best,
Tvrtko

---

> Thanks - the original author of the code posted a long message to that
> ticket -- please look again.
I see, I still think that the expectation function
in the class probability space is confusing, it
will only confuse people.

I have also noticed that in these classes
you can't add  add or multiply random variables
either by another random variable or by an number.
All of these operations give a random variable,
and it seems that this could easily be done.

I could, maybe do something like this for the final project,
make my class by adding new methods
to the one existing
and then we could see
what could be added to the class in Sage.

>Mind if I post your remarks there?
You can post my remarks.
```



---

Comment by kohel created at 2012-01-27 09:19:59

Strictly speaking the probability space is a pair (X,p:X->RR),
and a random variable a function F:X->RR.  Since there was no 
suitable class of functions, the object returned by probability 
space is essentially p, on which one can ask for the domain X 
(as Python list, for lack of better datastructure of sets). 
As such the printing function can be a bit confusing, since it 
reports itself to be the probability space, but is implemented 
as the function.

Now the probability function itself is a random variable (and 
explicitly inherits from them), so expectation is well-defined,
as are other functions.

To do this properly, one needs to create or identify a class of 
sets and their morphisms. Probability spaces would inherit from 
sets and random variables and the probability function from their 
morphisms.

In order to implement non-finite discrete random variables the 
explicit sums should be replaced by closed forms, integrals or 
similar computations.


---

Comment by was created at 2012-02-09 22:11:45

Kohel's examples above are a mess.  Here's something that actually works:

```
sage: n=6
sage: S = list('abcdef')
sage: P = dict([(S[i-1],1/n) for i in [1..n]]) 
sage: X = DiscreteProbabilitySpace(S, P)
sage: X.expectation() 
0.166666666666667
sage: f = dict([(S[i],i+1) for i in range(n)]) 
sage: F = DiscreteRandomVariable(X,f) 
sage: F.expectation() 
3.50000000000000
```



---

Comment by ttadic created at 2012-03-23 19:10:10

This is my attempt to make probability/random_variable.py better.  This patch will make it possible to  -assign probability spaces with probabilities as symbolic variables (like p, q) -assign random variables on such probability spaces with the possibility that they also can have values  in the symbolic ring -do basic operations with these random variables (like sums products..) - the ring of random variables has been added  -I have also made some changes to the way we calculate variance, and covariance  The new classes are called FiniteRandomVariable, FiniteProbabilitySpace, while the old classes (DiscreteProbabilitySpace, DiscreteRandomVariable) are still supported. (Things will work a bit differently, but I think all the things described in the manual for these classes are supported.)  Since, this is my first contribution to Sage, I am glad to hear any comments and suggestions.


---

Attachment

I don't know how to change the last message, so I am writing it more clearly.

This is my attempt to make probability/random_variable.py better.  This patch will make it possible to

-assign probability spaces with probabilities as symbolic variables (like p, q)

-assign random variables on such probability spaces with the possibility that they also can have values  in the symbolic ring

-do basic operations with these random variables (like sums products..) - the ring of random variables has been added

-I have also made some changes to the way we calculate variance, and covariance

The new classes are called FiniteRandomVariable, FiniteProbabilitySpace, while the old classes (DiscreteProbabilitySpace, DiscreteRandomVariable) are still supported. (Things will work a bit differently, but I think all the things described in the manual for these classes are supported.) 

Since, this is my first contribution to Sage, I am glad to hear any comments and suggestions.


---

Comment by ohanar created at 2013-03-18 18:49:14

A few comments to start with:
1. the first sentence of the commit message should be short, if more info is needed add two new lines before the rest of the commit (so that there is an empty line between the first sentence and the rest of the commit message)
1. every python function needs to have tests, even hidden functions. So for things like multiplication, add tests to make sure that A*B is what you expect it to be
1. (not strictly necessary) for sake of readability, it would help if you had an empty line before each function definition


---

Comment by ohanar created at 2013-03-18 18:49:14

Changing status from new to needs_review.


---

Comment by ohanar created at 2013-03-18 18:49:23

Changing status from needs_review to needs_work.


---

Comment by ohanar created at 2013-03-18 18:51:27

Also, all tabs should be 4 space characters (make sure that there are no tab characters).


---

Comment by pelegm created at 2017-10-31 13:30:34

Is this project now dead?

This is still a serious bug, actually; it is possible that there shouldn't be an expectation function for a probability space (but rather only for random variables), but if that's the case, the function should be removed. Currently it returns wrong values...


---

Comment by tscrim created at 2017-10-31 22:16:09

Probably, but that doesn't mean it cannot come back zombified. With some care it probably can be restored by applying the patches. If you want to do the writing, I am willing to do as much of the review as I can.


---

Comment by pelegm created at 2018-04-07 16:52:12

I really want to do the writing, but I am not sure it should be based on the existing code. I hope to allow symbolics within the same framework (for example, a random variable which returns `x` w.p. 1/2 and `y` with probability 1/2, should be able to return `(x+y)/2` as its expectation), so I plan to write a new package for that, and perhaps merge it into the base code in the future.


---

Comment by pelegm created at 2018-06-30 15:40:47

There are many more bugs in the current implementation, which we should consider as obsolete in my opinion.

Currently is days94 this project was revived, with a couple of participants that are currently doing the thinking, with the aim of making it symbolic-friendly.

Is there a way to flag a function/method in sage so that a user that uses it will be warned that it might return false results?
