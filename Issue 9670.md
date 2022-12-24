# Issue 9670: Bring probability/random_variable.py to 100% coverage

archive/issues_009670.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  kohel pelegm pang\n\nCurrently, this file is pretty woeful.\n\n```\nprobability/random_variable.py: 3% (1 of 29)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9670\n\n",
    "created_at": "2010-08-02T19:55:09Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Bring probability/random_variable.py to 100% coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9670",
    "user": "kcrisman"
}
```
Assignee: mvngu

CC:  kohel pelegm pang

Currently, this file is pretty woeful.

```
probability/random_variable.py: 3% (1 of 29)
```


Issue created by migration from https://trac.sagemath.org/ticket/9670





---

archive/issue_comments_093925.json:
```json
{
    "body": "The only thread about this I can find on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/533249e757f61636/00289c1374494e4d?lnk=gst&q=Discrete+probability+space#) seems relevant but short on examples.\n\nThere are also some minor bugs in checking for errors, which apparently have never occurred.  There is also some use of multiple inheritance, but it's not clear why (see [here](http://docs.python.org/release/1.5.1p1/tut/multiple.html) for the official view on this), although see the above thread for another view.\n\nI'm posting a partial patch, but before I spend more time on this, I'd like to know if the original author has any comments - particularly as to what sort of examples were expected with `RandomVariable`, since there weren't any in the original.  Also as to whether the doc upgrades thus far are on track.",
    "created_at": "2010-08-02T20:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93925",
    "user": "kcrisman"
}
```

The only thread about this I can find on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/533249e757f61636/00289c1374494e4d?lnk=gst&q=Discrete+probability+space#) seems relevant but short on examples.

There are also some minor bugs in checking for errors, which apparently have never occurred.  There is also some use of multiple inheritance, but it's not clear why (see [here](http://docs.python.org/release/1.5.1p1/tut/multiple.html) for the official view on this), although see the above thread for another view.

I'm posting a partial patch, but before I spend more time on this, I'd like to know if the original author has any comments - particularly as to what sort of examples were expected with `RandomVariable`, since there weren't any in the original.  Also as to whether the doc upgrades thus far are on track.



---

archive/issue_comments_093926.json:
```json
{
    "body": "Attachment [trac_9670-prelim.patch](tarball://root/attachments/some-uuid/ticket9670/trac_9670-prelim.patch) by kcrisman created at 2010-08-02 20:04:14",
    "created_at": "2010-08-02T20:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93926",
    "user": "kcrisman"
}
```

Attachment [trac_9670-prelim.patch](tarball://root/attachments/some-uuid/ticket9670/trac_9670-prelim.patch) by kcrisman created at 2010-08-02 20:04:14



---

archive/issue_comments_093927.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2012-01-26T19:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93927",
    "user": "was"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_093928.json:
```json
{
    "body": "This file is a great example of \"if it isn't tested, it's totally broken!\"  I've never used any of this code before just now when I grad student walked into my office and asked how to use it.  He (fortunately) couldn't even get started because typing `DiscreteProbabilitySpace?` in the notebook provides absolutely no help at all (strangely, in the command line, it does).   So I looked at the code and came up with the first trivial example:\n\n\n```\nsage: n=6; P = dict([(i,1/n) for i in [1..n]])\nsage: X = DiscreteProbabilitySpace(P.keys(), P)\nsage: X\nDiscrete probability space defined by {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}\nsage: X.expectation()\n0.166666666666667\n```\n\n\nLiterally, the first thing I tried came out completely wrong!  That's sure as hell not the expectation, which should be sum i*1/n = n*(n+1)/2/n = (n+1)/2 = 7/2.    \n\nI then looked at the code for expectation.  It's obviously got not test (and don't worry kcrisman -- you didn't add any), and the code itself is just wrong:\n\n```\n    def expectation(self):\n        r\"\"\"\n        The expectation of the discrete random variable, namely\n        `\\sum_{x \\in S} p(x) X[x]`, where `X` = self and\n        `S` is the probability space of `X`.\n        \"\"\"\n        E = 0\n        Omega = self.probability_space()\n        for x in self._function.keys():\n            E += Omega(x) * self(x)\n        return E\n```\n\n\nI don't know why it does Omega=..., since self.probability_space() is self is True.\nI don't know why this doesn't use a single list comprehension line.  \n\nHere self._function is the dictionary: `{1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6`}.\nSo the code should be:\n\n```\ndef expectation(self):\n    return sum(x*self(x) for x in self._function.keys())\n```\n\nright?  \n\nIndeed,\n\n```\nsage: self=X;  sum(x*self(x) for x in self._function.keys())\n3.50000000000000\n```\n\n\nBut that said, what's up with the floating point numbers?  Shouldn't the answer be exact?\n\n```\nsage: type(self(1))\n<type 'sage.rings.real_mpfr.RealNumber'>\n```\n\n\nThere is a way to deal with this:\n\n```\nsage: X = DiscreteProbabilitySpace(P.keys(), P, codomain=QQ)\nsage: self=X;  sum(x*self(x) for x in self._function.keys())\n7/2\n```\n\nBut shouldn't the default codomain depend on the dictionary P?   It should take the values and find a common parent for them (e.g., using Sequence), then take the fraction field of that.  \n\nIn defense of the original code, David K. wrote it before Sequence existed, and we were just figuring out how to use Python at the time.... and didn't know if Sage would have more than 3 users. \n\nAnyway, this code as is scary and needs massive, massive reworking.  \n\nAnd since I'm reporting a specific bug, I am changing this to a defect.",
    "created_at": "2012-01-26T19:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93928",
    "user": "was"
}
```

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

archive/issue_comments_093929.json:
```json
{
    "body": "I agree the code (among the first I wrote) should be improved or rewritten.\n\nAlso note that \"discrete\" should be \"finite\" -- I never implemented any code  for infinite discrete probability spaces and the finiteness of X a rather heavy assumption.\n\nThat said, despite the lack of documentation, I assert that the above output  is correct.  The idea of the discrete or finite probability spaces is that  the underlying set S of X can be anything:\n\n\n```\nsage: n = 6 sage: S = list('abcdef') \nsage: P = dict([(S[i],1/n) for i in [1..n]]) \nsage: X = DiscreteProbabilitySpace(S, P) \nsage: X.expectation() \n0.166666666666667\n```\n\n\nIt so happens that a probability function IS a random variable so that  one can ask for its expectation.  Thus probability space inherits from  random variables which generalize them.\n\nWith S so defined, it should be clear that it certainly doesn't make  sense to form \\sum_{x \\in S} x p(x), since S need not be contained in  a module over the reals for which this sum makes sense.  Rather for a  probability space, the expectation is \\sum p(x)<sup>2.</sup>\n\nFor reasons of avoiding coefficient blowup in the rationals, the default  uses a real ring. This is a design decision which is perhaps questionable, but avoids problems with undergraduate teaching. If you want the  probability space with value ring in the rationals, then explicitly set  the codomain:\n\n\n```\nsage: X = DiscreteProbabilitySpace(S, P, codomain = QQ) \nsage: X.expectation() \n1/6\n```\n\n\nTo get the random variable you intended, you need to first create the  probability space as above, then define the random variable with respect  to this:\n\n\n```\nsage: f = dict([(S[i],i+1) for i in range(n)]) \nsage: F = DiscreteRandomVariable(X,f) \nsage: F.expectation() \n3.50000000000000\n```\n\n\nAgain, for exact values, set the codomain:\n\n\n```\nsage: F = DiscreteRandomVariable(X,f,codomain = QQ) \nsage: F.expectation() \n7/2\n```\n\n\nThis two-step creation for a random variable is a bit awkward  if all you want is the uniform probability function. Since this  occurs quite often in practice (for a finite probability space), it might be practical to have a shortcut which defines the  uniform probability space by default.  In that case the syntax  might be changed from (X,f,codomain) to (f,X,codomain), or  without change, just letting X be a list or finite set and  setting up the uniform probability on it.  This is NOT implemented, but would be a more intuitive construction for what you intended:\n\n\n```\nsage: S = list('abcdef') \nsage: F = DiscreteRandomVariable(S,dict([(S[i],i+1) for i in range(n)])) \nsage: X = F.probability_space(); X \nDiscrete probability space defined by {'a': 1/6, 'c': 1/6, 'b': 1/6, 'e': 1/6, 'd': 1/6, 'f': 1/6}\n```\n\n\nAt the time of writing this (and maybe still true) there was no class of finite sets and morphisms of sets, which would provide  a more natural input to the constructors for probability space  and random variables.  It would be a cleaner construction to  have the codomain attached to the function f or probability  function p, and have some general mechanism for checking that  the domains of f and p agree and that codomain of f is a module  over the codomain of p. Python dictionaries were the closest  I could come (without implementing a category of sets) to the  datastructure for morphism of sets.\n\nCurrently the domain of a random variable is assumed to be some  real ring or subring but vector-valued random variables would  make sense in a number of settings.",
    "created_at": "2012-01-26T22:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93929",
    "user": "kohel"
}
```

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

archive/issue_comments_093930.json:
```json
{
    "body": "David -- many thanks for the clarification.  I obviously completely misunderstood how your code was supposed to work.  I've changed this ticket back to \"enhancement\".  Thanks also for the hints about how to improve the code.",
    "created_at": "2012-01-26T22:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93930",
    "user": "was"
}
```

David -- many thanks for the clarification.  I obviously completely misunderstood how your code was supposed to work.  I've changed this ticket back to "enhancement".  Thanks also for the hints about how to improve the code.



---

archive/issue_comments_093931.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2012-01-26T22:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93931",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_093932.json:
```json
{
    "body": "Thanks for the discussion here.  I just want to point out that #10770 fell afoul of this as well, and that [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8febda1b92330c85/9cea7249b186d8e5) and #11572 also had some issues because of wondering where the binomial distribution belonged, which seems somehow related. ?",
    "created_at": "2012-01-27T01:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93932",
    "user": "kcrisman"
}
```

Thanks for the discussion here.  I just want to point out that #10770 fell afoul of this as well, and that [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8febda1b92330c85/9cea7249b186d8e5) and #11572 also had some issues because of wondering where the binomial distribution belonged, which seems somehow related. ?



---

archive/issue_comments_093933.json:
```json
{
    "body": "Some remarks from Tvrtko Tadic, a UW grad student in probability:\n\n```\nI don't think discrete probability\nspace needs to have an expectation (as a function).\nIt could be\nfor example that a kid gets an apple with probability 1/2,\nand a orange with probability 1/2. We can't sum\nhalf an apple and half an orange.\n\nSo I don't think the class DiscreteProbabilitySpace should\nhave an expectation method at all.\nIt could be that somebody started an expectation\nmethod in the wrong class and the forgot about it.\n\nI tried the expectation for DiscreteRandomVariable, and it works\nfine. (Random variables take values in real numbers,\nand the expectation is defined for them not for\nprobability spaces.)\n\nEXAMPLE (DICE):\n\nP=dict([(i,1/6) for i in [1..6]])\nOmega=[1..6]\n\nPS=DiscreteProbabilitySpace(Omega,P)\n\nf=dict([(i,i) for i in [1..6]])\nX=DiscreteRandomVariable(PS,f)\n\nX.expectation()# (it should be 7/2)\nX.variance() # (it should be 35/12)\n\nIt works!\n\nI will take a look at the other packages Sage has\nfor probability (and related areas) that you mentioned.\n\nBest,\nTvrtko\n\n---\n\n> Thanks - the original author of the code posted a long message to that\n> ticket -- please look again.\nI see, I still think that the expectation function\nin the class probability space is confusing, it\nwill only confuse people.\n\nI have also noticed that in these classes\nyou can't add  add or multiply random variables\neither by another random variable or by an number.\nAll of these operations give a random variable,\nand it seems that this could easily be done.\n\nI could, maybe do something like this for the final project,\nmake my class by adding new methods\nto the one existing\nand then we could see\nwhat could be added to the class in Sage.\n\n>Mind if I post your remarks there?\nYou can post my remarks.\n```\n",
    "created_at": "2012-01-27T05:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93933",
    "user": "was"
}
```

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

archive/issue_comments_093934.json:
```json
{
    "body": "Strictly speaking the probability space is a pair (X,p:X->RR),\nand a random variable a function F:X->RR.  Since there was no \nsuitable class of functions, the object returned by probability \nspace is essentially p, on which one can ask for the domain X \n(as Python list, for lack of better datastructure of sets). \nAs such the printing function can be a bit confusing, since it \nreports itself to be the probability space, but is implemented \nas the function.\n\nNow the probability function itself is a random variable (and \nexplicitly inherits from them), so expectation is well-defined,\nas are other functions.\n\nTo do this properly, one needs to create or identify a class of \nsets and their morphisms. Probability spaces would inherit from \nsets and random variables and the probability function from their \nmorphisms.\n\nIn order to implement non-finite discrete random variables the \nexplicit sums should be replaced by closed forms, integrals or \nsimilar computations.",
    "created_at": "2012-01-27T09:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93934",
    "user": "kohel"
}
```

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

archive/issue_comments_093935.json:
```json
{
    "body": "Kohel's examples above are a mess.  Here's something that actually works:\n\n```\nsage: n=6\nsage: S = list('abcdef')\nsage: P = dict([(S[i-1],1/n) for i in [1..n]]) \nsage: X = DiscreteProbabilitySpace(S, P)\nsage: X.expectation() \n0.166666666666667\nsage: f = dict([(S[i],i+1) for i in range(n)]) \nsage: F = DiscreteRandomVariable(X,f) \nsage: F.expectation() \n3.50000000000000\n```\n",
    "created_at": "2012-02-09T22:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93935",
    "user": "was"
}
```

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

archive/issue_comments_093936.json:
```json
{
    "body": "This is my attempt to make probability/random_variable.py better.  This patch will make it possible to  -assign probability spaces with probabilities as symbolic variables (like p, q) -assign random variables on such probability spaces with the possibility that they also can have values  in the symbolic ring -do basic operations with these random variables (like sums products..) - the ring of random variables has been added  -I have also made some changes to the way we calculate variance, and covariance  The new classes are called FiniteRandomVariable, FiniteProbabilitySpace, while the old classes (DiscreteProbabilitySpace, DiscreteRandomVariable) are still supported. (Things will work a bit differently, but I think all the things described in the manual for these classes are supported.)  Since, this is my first contribution to Sage, I am glad to hear any comments and suggestions.",
    "created_at": "2012-03-23T19:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93936",
    "user": "ttadic"
}
```

This is my attempt to make probability/random_variable.py better.  This patch will make it possible to  -assign probability spaces with probabilities as symbolic variables (like p, q) -assign random variables on such probability spaces with the possibility that they also can have values  in the symbolic ring -do basic operations with these random variables (like sums products..) - the ring of random variables has been added  -I have also made some changes to the way we calculate variance, and covariance  The new classes are called FiniteRandomVariable, FiniteProbabilitySpace, while the old classes (DiscreteProbabilitySpace, DiscreteRandomVariable) are still supported. (Things will work a bit differently, but I think all the things described in the manual for these classes are supported.)  Since, this is my first contribution to Sage, I am glad to hear any comments and suggestions.



---

archive/issue_comments_093937.json:
```json
{
    "body": "Attachment [finite_prob.patch](tarball://root/attachments/some-uuid/ticket9670/finite_prob.patch) by ttadic created at 2012-03-23 19:14:27\n\nI don't know how to change the last message, so I am writing it more clearly.\n\nThis is my attempt to make probability/random_variable.py better.  This patch will make it possible to\n\n-assign probability spaces with probabilities as symbolic variables (like p, q)\n\n-assign random variables on such probability spaces with the possibility that they also can have values  in the symbolic ring\n\n-do basic operations with these random variables (like sums products..) - the ring of random variables has been added\n\n-I have also made some changes to the way we calculate variance, and covariance\n\nThe new classes are called FiniteRandomVariable, FiniteProbabilitySpace, while the old classes (DiscreteProbabilitySpace, DiscreteRandomVariable) are still supported. (Things will work a bit differently, but I think all the things described in the manual for these classes are supported.) \n\nSince, this is my first contribution to Sage, I am glad to hear any comments and suggestions.",
    "created_at": "2012-03-23T19:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93937",
    "user": "ttadic"
}
```

Attachment [finite_prob.patch](tarball://root/attachments/some-uuid/ticket9670/finite_prob.patch) by ttadic created at 2012-03-23 19:14:27

I don't know how to change the last message, so I am writing it more clearly.

This is my attempt to make probability/random_variable.py better.  This patch will make it possible to

-assign probability spaces with probabilities as symbolic variables (like p, q)

-assign random variables on such probability spaces with the possibility that they also can have values  in the symbolic ring

-do basic operations with these random variables (like sums products..) - the ring of random variables has been added

-I have also made some changes to the way we calculate variance, and covariance

The new classes are called FiniteRandomVariable, FiniteProbabilitySpace, while the old classes (DiscreteProbabilitySpace, DiscreteRandomVariable) are still supported. (Things will work a bit differently, but I think all the things described in the manual for these classes are supported.) 

Since, this is my first contribution to Sage, I am glad to hear any comments and suggestions.



---

archive/issue_comments_093938.json:
```json
{
    "body": "A few comments to start with:\n1. the first sentence of the commit message should be short, if more info is needed add two new lines before the rest of the commit (so that there is an empty line between the first sentence and the rest of the commit message)\n2. every python function needs to have tests, even hidden functions. So for things like multiplication, add tests to make sure that A*B is what you expect it to be\n3. (not strictly necessary) for sake of readability, it would help if you had an empty line before each function definition",
    "created_at": "2013-03-18T18:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93938",
    "user": "ohanar"
}
```

A few comments to start with:
1. the first sentence of the commit message should be short, if more info is needed add two new lines before the rest of the commit (so that there is an empty line between the first sentence and the rest of the commit message)
2. every python function needs to have tests, even hidden functions. So for things like multiplication, add tests to make sure that A*B is what you expect it to be
3. (not strictly necessary) for sake of readability, it would help if you had an empty line before each function definition



---

archive/issue_comments_093939.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-18T18:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93939",
    "user": "ohanar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093940.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-03-18T18:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93940",
    "user": "ohanar"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093941.json:
```json
{
    "body": "Also, all tabs should be 4 space characters (make sure that there are no tab characters).",
    "created_at": "2013-03-18T18:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93941",
    "user": "ohanar"
}
```

Also, all tabs should be 4 space characters (make sure that there are no tab characters).



---

archive/issue_comments_093942.json:
```json
{
    "body": "Is this project now dead?\n\nThis is still a serious bug, actually; it is possible that there shouldn't be an expectation function for a probability space (but rather only for random variables), but if that's the case, the function should be removed. Currently it returns wrong values...",
    "created_at": "2017-10-31T13:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93942",
    "user": "pelegm"
}
```

Is this project now dead?

This is still a serious bug, actually; it is possible that there shouldn't be an expectation function for a probability space (but rather only for random variables), but if that's the case, the function should be removed. Currently it returns wrong values...



---

archive/issue_comments_093943.json:
```json
{
    "body": "Probably, but that doesn't mean it cannot come back zombified. With some care it probably can be restored by applying the patches. If you want to do the writing, I am willing to do as much of the review as I can.",
    "created_at": "2017-10-31T22:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93943",
    "user": "tscrim"
}
```

Probably, but that doesn't mean it cannot come back zombified. With some care it probably can be restored by applying the patches. If you want to do the writing, I am willing to do as much of the review as I can.



---

archive/issue_comments_093944.json:
```json
{
    "body": "I really want to do the writing, but I am not sure it should be based on the existing code. I hope to allow symbolics within the same framework (for example, a random variable which returns `x` w.p. 1/2 and `y` with probability 1/2, should be able to return `(x+y)/2` as its expectation), so I plan to write a new package for that, and perhaps merge it into the base code in the future.",
    "created_at": "2018-04-07T16:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93944",
    "user": "pelegm"
}
```

I really want to do the writing, but I am not sure it should be based on the existing code. I hope to allow symbolics within the same framework (for example, a random variable which returns `x` w.p. 1/2 and `y` with probability 1/2, should be able to return `(x+y)/2` as its expectation), so I plan to write a new package for that, and perhaps merge it into the base code in the future.



---

archive/issue_comments_093945.json:
```json
{
    "body": "There are many more bugs in the current implementation, which we should consider as obsolete in my opinion.\n\nCurrently is days94 this project was revived, with a couple of participants that are currently doing the thinking, with the aim of making it symbolic-friendly.\n\nIs there a way to flag a function/method in sage so that a user that uses it will be warned that it might return false results?",
    "created_at": "2018-06-30T15:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9670#issuecomment-93945",
    "user": "pelegm"
}
```

There are many more bugs in the current implementation, which we should consider as obsolete in my opinion.

Currently is days94 this project was revived, with a couple of participants that are currently doing the thinking, with the aim of making it symbolic-friendly.

Is there a way to flag a function/method in sage so that a user that uses it will be warned that it might return false results?
