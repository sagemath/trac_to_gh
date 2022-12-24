# Issue 8133: changing the string representation of Dirichlet charachters

archive/issues_008133.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  was\n\nKeywords: dirichlet characters\n\nThe current representation of Dirichlet characters as something like `[1,zeta6,-1]` is not very helpful, especially because it is not even clear what generator we are taling about in (Z/N)*.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8133\n\n",
    "created_at": "2010-01-31T01:33:06Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "changing the string representation of Dirichlet charachters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8133",
    "user": "wuthrich"
}
```
Assignee: craigcitro

CC:  was

Keywords: dirichlet characters

The current representation of Dirichlet characters as something like `[1,zeta6,-1]` is not very helpful, especially because it is not even clear what generator we are taling about in (Z/N)*.

Issue created by migration from https://trac.sagemath.org/ticket/8133





---

archive/issue_comments_071513.json:
```json
{
    "body": "I put this in the component 'modular forms' since the relevant file dirichlet.py is there. But I think it is a bit odd that this file is there; it should be with number fields, I believe. \n\nThe attached patch changes the string representation of a Dirichlet character to \n\n\n```\nsage: G = DirichletGroup(12)\nsage: chi = G.0\nsage: chi\nDirichlet character modulo 12 of conductor 4 mapping the generators to {5: 1, 7: -1}\n```\n\n\nI have also created a shorter representation that is used in other _repr_ like in\n\n\n```\nsage: ModularForms(chi,7)\nModular Forms space of dimension 14, character {5: 1, 7: -1} and weight 7 over Rational Field\n```\n",
    "created_at": "2010-01-31T01:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71513",
    "user": "wuthrich"
}
```

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

archive/issue_comments_071514.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-31T01:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71514",
    "user": "wuthrich"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071515.json:
```json
{
    "body": "sorry, this is not ready for review ! I fail to see some tests.",
    "created_at": "2010-01-31T01:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71515",
    "user": "wuthrich"
}
```

sorry, this is not ready for review ! I fail to see some tests.



---

archive/issue_comments_071516.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-31T01:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71516",
    "user": "wuthrich"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071517.json:
```json
{
    "body": "Hmmm .... I should also modify book_stein_modform.py.\n\nI guess this requires the authorisation of the author. Of course, this patch would not change the answers or the useability of the code in the book, but it would make the output look somewhat prettier.\n\nWilliam, what is the verdict on such a change ?",
    "created_at": "2010-01-31T03:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71517",
    "user": "wuthrich"
}
```

Hmmm .... I should also modify book_stein_modform.py.

I guess this requires the authorisation of the author. Of course, this patch would not change the answers or the useability of the code in the book, but it would make the output look somewhat prettier.

William, what is the verdict on such a change ?



---

archive/issue_comments_071518.json:
```json
{
    "body": "Replying to [ticket:8133 wuthrich]:\n> The current representation of Dirichlet characters as something like `[1,zeta6,-1]` is not very helpful, especially because it is not even clear what generator we are talking about in (Z/N)*. \n> \n\nI have concerns:\n\n1. First, you can easily get the generators of the Dirichlet group.   I do not think they have to be given explicitly in the print representation (just like the basis for a vector space doesn't have to be given in a matrix).   See below -- just use the `unit_gens()` method to find out the gens that are being mapped. \n\n```\nsage: G.<a,b,c> = DirichletGroup(40)\nsage: b\n[1, -1, 1]\nsage: a\n[-1, 1, 1]\nsage: c\n[1, 1, zeta4]\nsage: G.unit_gens()\n[31, 21, 17]\n```\n\n \n2. There are potential issues with your suggested change:\n\n```\nDirichlet character modulo 12 of conductor 4 mapping the generators to {5: 1, 7: -1}\n```\n\nThe problem is that it literally makes no sense to read it.  The generators don't get mapped to a Python dictionary.   It's like a mixed metaphor.   Moreover, if you use Python dictionary notation, maybe you really have a dictionary there, so the keys can come in random order, which is bad. \n\n3. If we're going to make some big change, it would be better to make it consistent with ring homomorphisms, which all do print in the same way:\n\n```\nsage: R.<x,y> = QQ[]}}} \nsage: phi = R.hom([y^3,x-3]); phi\nRing endomorphism of Multivariate Polynomial Ring in x, y over Rational Field\n  Defn: x |--> y^3\n        y |--> x - 3\n```\n\nHowever, this notation is definitely too heavy as is for Dirichlet characters.  \n\n\nI'm not going to suggest a change, since I actually like how Dirichlet characters are currently printed.",
    "created_at": "2010-02-01T01:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71518",
    "user": "was"
}
```

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

archive/issue_comments_071519.json:
```json
{
    "body": "Thanks a lot for the valuable comments. Sorry to insist a bit more on this change. I have been using Dirichlet characters quite a lot recently for p-adic L-functions (of elliptic curves and for zeta functions) and I thought the current printing was not useful.\n\nReplying to [comment:6 was]:\n> 1. First, you can easily get the generators of the Dirichlet group.   I do not think they have to be given explicitly in the print representation (just like the basis for a vector space doesn't have to be given in a matrix).   See below -- just use the `unit_gens()` method to find out the gens that are being mapped. \n\nI almost agree with you, only with a few minor points :\n\n* The group (Z/N)* is not a vector space, for instance for N=16, we have Z/2 + Z/4 and so the two generators have different order and it would be great to recognise that immediately in the string representation. \n\n* Usually, in a vector space the elements do not have canonical names as the residue classes in Z/N have. \n\n* There is no need to have it, of course; but I think it would improve the user-friendliness of sage. It is completely counter-intuitive for a new user to ask for a Dirichlet character, which is a map from ZZ to R, and to be given back a list of values in R.\n\n* There is no place in sage where a Dirichlet character is treated as a list of values, apart from the _repr_. So I do not see the advantage of the list representation. \n\n* I think it is advantage when the _repr_ tells what sort of type we are dealing with. Seeing a list, one is tempted to do things like `chi[0]`.\n\n> 2. There are potential issues with your suggested change:\n> [...]\n> The problem is that it literally makes no sense to read it.  The generators don't get mapped to a Python dictionary.   It's like a mixed metaphor.   Moreover, if you use Python dictionary notation, maybe you really have a dictionary there, so the keys can come in random order, which is bad. \n\nTotally agree with you on this one. My English is bad and it should read \"mapping 5 |--> 1, 7 |--> -1\" instead. Yes I did put a dictionary there and I agree that it is not good, exactly because of what I said earlier.\n\n> 3. If we're going to make some big change, it would be better to make it consistent with ring homomorphisms, [...]\n> However, this notation is definitely too heavy as is for Dirichlet characters.  \n\nYes, I agree with both. So as a second attempt I would propose a long representation of the form\n\n\n```\nsage: chi\nDirichlet character modulo 12 of conductor 4 mapping 5 |--> 1, 7  |--> -1\n```\n\n\nor maybe one could print the order, too.\nAnd a short representation as in \n\n\n```\nsage: ModularForms(chi,7)\nModular Forms space of dimension 14, character 5 |--> 1, 7 |--> -1 and weight 7 over Rational Field\n```\n\n\nor maybe with () around it. Or we could leave it there as values_on_gens().\n\n> I'm not going to suggest a change, since I actually like how Dirichlet characters are currently printed. \n\n... this is of course a valid poitn of taste about which I won't argue about at all.",
    "created_at": "2010-02-01T16:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71519",
    "user": "wuthrich"
}
```

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

archive/issue_comments_071520.json:
```json
{
    "body": "Attachment [trac_8133.patch](tarball://root/attachments/some-uuid/ticket8133/trac_8133.patch) by wuthrich created at 2010-03-27 21:08:47\n\nexported against 4.3.4",
    "created_at": "2010-03-27T21:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71520",
    "user": "wuthrich"
}
```

Attachment [trac_8133.patch](tarball://root/attachments/some-uuid/ticket8133/trac_8133.patch) by wuthrich created at 2010-03-27 21:08:47

exported against 4.3.4



---

archive/issue_comments_071521.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-27T21:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71521",
    "user": "wuthrich"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071522.json:
```json
{
    "body": "So, here is a new version of the patch. This one is ready to be reviewed. It changes the string representation of a Dirichlet character to \n\n\n```\nsage: chi\nDirichlet character modulo 12 of conductor 4 mapping 5 |--> 1, 7  |--> -1\n```\n\n\nbut leaves the usual representation within modular form etc, like \n\n\n```\nsage: ModularForms(chi,7)\nModular Forms space of dimension 14, character [1,-1] and weight 7 over Rational Field\n```\n\n\nIf this change is not approved by some, I would propose to make a vote on sage-nt.",
    "created_at": "2010-03-27T21:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71522",
    "user": "wuthrich"
}
```

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

archive/issue_comments_071523.json:
```json
{
    "body": "I like the new output format.  But I can see that William might be attached to the old one, being used to (and also responsible for) it.\n\nTesting now...",
    "created_at": "2010-04-03T11:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71523",
    "user": "cremona"
}
```

I like the new output format.  But I can see that William might be attached to the old one, being used to (and also responsible for) it.

Testing now...



---

archive/issue_comments_071524.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T12:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71524",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071525.json:
```json
{
    "body": "...all tests pass, so I am giving this a positive review --but would not mind opening the discussion up, so will post on sage-nt also).",
    "created_at": "2010-04-03T12:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71525",
    "user": "cremona"
}
```

...all tests pass, so I am giving this a positive review --but would not mind opening the discussion up, so will post on sage-nt also).



---

archive/issue_comments_071526.json:
```json
{
    "body": "After 4 days, there were two responses on sage-nt:  a positive one from William, and a suggestion for a few further changes from Robert Bradshaw (see http://groups.google.co.uk/group/sage-nt/browse_thread/thread/be56e6f0e29b44e8).\n\n```\nI certainly like the new representation better. Perhaps the _latex_   \nmethod should use \\mapsto rather than the ASCII art |-->, but it   \nshould certainly produce \\zeta_{n}^{k} rather than returning just   \nplain _repr_. Another alternative short representation would be   \nsomething like \n(31, 41, 37) |--> (1, 1, zeta4) \n- Robert \n```\n",
    "created_at": "2010-04-07T21:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71526",
    "user": "cremona"
}
```

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

archive/issue_comments_071527.json:
```json
{
    "body": "Latexing of Dirichlet characters is being tracked at #8584. I have uploaded a new patch there which implements Robert's suggestions (using `\\mapsto` and the latex representation of roots of unity). \n\nFor what it's worth, I'm also in favour of the change.",
    "created_at": "2010-04-08T10:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71527",
    "user": "davidloeffler"
}
```

Latexing of Dirichlet characters is being tracked at #8584. I have uploaded a new patch there which implements Robert's suggestions (using `\mapsto` and the latex representation of roots of unity). 

For what it's worth, I'm also in favour of the change.



---

archive/issue_comments_071528.json:
```json
{
    "body": "I was just about to submit an additional patch (equal to the new one in #8584), because I completely agree with changing the LaTeX representation as well. Thanks David, I will review yours.",
    "created_at": "2010-04-08T11:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71528",
    "user": "wuthrich"
}
```

I was just about to submit an additional patch (equal to the new one in #8584), because I completely agree with changing the LaTeX representation as well. Thanks David, I will review yours.



---

archive/issue_comments_071529.json:
```json
{
    "body": "Merged \"trac_8133.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-15T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71529",
    "user": "jhpalmieri"
}
```

Merged "trac_8133.patch" in 4.4.alpha0.



---

archive/issue_comments_071530.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8133#issuecomment-71530",
    "user": "jhpalmieri"
}
```

Resolution: fixed
