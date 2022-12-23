# Issue 8133: changing the string representation of Dirichlet charachters

Issue created by migration from https://trac.sagemath.org/ticket/8133

Original creator: wuthrich

Original creation time: 2010-01-31 01:33:06

Assignee: craigcitro

CC:  was

Keywords: dirichlet characters

The current representation of Dirichlet characters as something like `[1,zeta6,-1]` is not very helpful, especially because it is not even clear what generator we are taling about in (Z/N)*.


---

Comment by wuthrich created at 2010-01-31 01:39:03

I put this in the component 'modular forms' since the relevant file dirichlet.py is there. But I think it is a bit odd that this file is there; it should be with number fields, I believe. 

The attached patch changes the string representation of a Dirichlet character to 


```
sage: G = DirichletGroup(12)
sage: chi = G.0
sage: chi
Dirichlet character modulo 12 of conductor 4 mapping the generators to {5: 1, 7: -1}
```


I have also created a shorter representation that is used in other _repr_ like in


```
sage: ModularForms(chi,7)
Modular Forms space of dimension 14, character {5: 1, 7: -1} and weight 7 over Rational Field
```



---

Comment by wuthrich created at 2010-01-31 01:42:19

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-01-31 01:51:57

sorry, this is not ready for review ! I fail to see some tests.


---

Comment by wuthrich created at 2010-01-31 01:51:57

Changing status from needs_review to needs_work.


---

Comment by wuthrich created at 2010-01-31 03:12:49

Hmmm .... I should also modify book_stein_modform.py.

I guess this requires the authorisation of the author. Of course, this patch would not change the answers or the useability of the code in the book, but it would make the output look somewhat prettier.

William, what is the verdict on such a change ?


---

Comment by was created at 2010-02-01 01:23:44

Replying to [ticket:8133 wuthrich]:
> The current representation of Dirichlet characters as something like `[1,zeta6,-1]` is not very helpful, especially because it is not even clear what generator we are talking about in (Z/N)*. 
> 

I have concerns:

1. First, you can easily get the generators of the Dirichlet group.   I do not think they have to be given explicitly in the print representation (just like the basis for a vector space doesn't have to be given in a matrix).   See below -- just use the `unit_gens()` method to find out the gens that are being mapped. 

```
sage: G.<a,b,c> = DirichletGroup(40)
sage: b
[1, -1, 1]
sage: a
[-1, 1, 1]
sage: c
[1, 1, zeta4]
sage: G.unit_gens()
[31, 21, 17]
```

 
2. There are potential issues with your suggested change:

```
Dirichlet character modulo 12 of conductor 4 mapping the generators to {5: 1, 7: -1}
```

The problem is that it literally makes no sense to read it.  The generators don't get mapped to a Python dictionary.   It's like a mixed metaphor.   Moreover, if you use Python dictionary notation, maybe you really have a dictionary there, so the keys can come in random order, which is bad. 

3. If we're going to make some big change, it would be better to make it consistent with ring homomorphisms, which all do print in the same way:

```
sage: R.<x,y> = QQ[]}}} 
sage: phi = R.hom([y^3,x-3]); phi
Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
  Defn: x |--> y^3
        y |--> x - 3
```

However, this notation is definitely too heavy as is for Dirichlet characters.  


I'm not going to suggest a change, since I actually like how Dirichlet characters are currently printed.


---

Comment by wuthrich created at 2010-02-01 16:23:50

Thanks a lot for the valuable comments. Sorry to insist a bit more on this change. I have been using Dirichlet characters quite a lot recently for p-adic L-functions (of elliptic curves and for zeta functions) and I thought the current printing was not useful.

Replying to [comment:6 was]:
> 1. First, you can easily get the generators of the Dirichlet group.   I do not think they have to be given explicitly in the print representation (just like the basis for a vector space doesn't have to be given in a matrix).   See below -- just use the `unit_gens()` method to find out the gens that are being mapped. 

I almost agree with you, only with a few minor points :

 * The group (Z/N)* is not a vector space, for instance for N=16, we have Z/2 + Z/4 and so the two generators have different order and it would be great to recognise that immediately in the string representation. 

 * Usually, in a vector space the elements do not have canonical names as the residue classes in Z/N have. 

 * There is no need to have it, of course; but I think it would improve the user-friendliness of sage. It is completely counter-intuitive for a new user to ask for a Dirichlet character, which is a map from ZZ to R, and to be given back a list of values in R.

 * There is no place in sage where a Dirichlet character is treated as a list of values, apart from the _repr_. So I do not see the advantage of the list representation. 

 * I think it is advantage when the _repr_ tells what sort of type we are dealing with. Seeing a list, one is tempted to do things like `chi[0]`.

> 2. There are potential issues with your suggested change:
> [...]
> The problem is that it literally makes no sense to read it.  The generators don't get mapped to a Python dictionary.   It's like a mixed metaphor.   Moreover, if you use Python dictionary notation, maybe you really have a dictionary there, so the keys can come in random order, which is bad. 

Totally agree with you on this one. My English is bad and it should read "mapping 5 |--> 1, 7 |--> -1" instead. Yes I did put a dictionary there and I agree that it is not good, exactly because of what I said earlier.

> 3. If we're going to make some big change, it would be better to make it consistent with ring homomorphisms, [...]
> However, this notation is definitely too heavy as is for Dirichlet characters.  

Yes, I agree with both. So as a second attempt I would propose a long representation of the form


```
sage: chi
Dirichlet character modulo 12 of conductor 4 mapping 5 |--> 1, 7  |--> -1
```


or maybe one could print the order, too.
And a short representation as in 


```
sage: ModularForms(chi,7)
Modular Forms space of dimension 14, character 5 |--> 1, 7 |--> -1 and weight 7 over Rational Field
```


or maybe with () around it. Or we could leave it there as values_on_gens().

> I'm not going to suggest a change, since I actually like how Dirichlet characters are currently printed. 

... this is of course a valid poitn of taste about which I won't argue about at all.


---

Attachment

exported against 4.3.4


---

Comment by wuthrich created at 2010-03-27 21:12:30

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2010-03-27 21:12:30

So, here is a new version of the patch. This one is ready to be reviewed. It changes the string representation of a Dirichlet character to 


```
sage: chi
Dirichlet character modulo 12 of conductor 4 mapping 5 |--> 1, 7  |--> -1
```


but leaves the usual representation within modular form etc, like 


```
sage: ModularForms(chi,7)
Modular Forms space of dimension 14, character [1,-1] and weight 7 over Rational Field
```


If this change is not approved by some, I would propose to make a vote on sage-nt.


---

Comment by cremona created at 2010-04-03 11:50:55

I like the new output format.  But I can see that William might be attached to the old one, being used to (and also responsible for) it.

Testing now...


---

Comment by cremona created at 2010-04-03 12:04:05

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-03 12:04:05

...all tests pass, so I am giving this a positive review --but would not mind opening the discussion up, so will post on sage-nt also).


---

Comment by cremona created at 2010-04-07 21:26:32

After 4 days, there were two responses on sage-nt:  a positive one from William, and a suggestion for a few further changes from Robert Bradshaw (see http://groups.google.co.uk/group/sage-nt/browse_thread/thread/be56e6f0e29b44e8).

```
I certainly like the new representation better. Perhaps the _latex_   
method should use \mapsto rather than the ASCII art |-->, but it   
should certainly produce \zeta_{n}^{k} rather than returning just   
plain _repr_. Another alternative short representation would be   
something like 
(31, 41, 37) |--> (1, 1, zeta4) 
- Robert 
```



---

Comment by davidloeffler created at 2010-04-08 10:26:59

Latexing of Dirichlet characters is being tracked at #8584. I have uploaded a new patch there which implements Robert's suggestions (using `\mapsto` and the latex representation of roots of unity). 

For what it's worth, I'm also in favour of the change.


---

Comment by wuthrich created at 2010-04-08 11:21:46

I was just about to submit an additional patch (equal to the new one in #8584), because I completely agree with changing the LaTeX representation as well. Thanks David, I will review yours.


---

Comment by jhpalmieri created at 2010-04-15 23:39:49

Merged "trac_8133.patch" in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:39:49

Resolution: fixed
