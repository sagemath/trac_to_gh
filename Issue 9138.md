# Issue 9138: Introspection is failing on polynomial rings

archive/issues_009138.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat robertwb\n\nKeywords: introspection\n\nExample:\n\n```\nsage: R.<x> = QQ[] \nsage: R.su<tab> \nR.sum                               R.summation \nR.summation_from_element_class_add \nsage: R.sum? \nObject `R.sum` not found. \nsage: R.sum() \n--------------------------------------------------------------------------- \nAttributeError                            Traceback (most recent call last) \n```\n\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/4780192a11a8b591 for more discussion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9138\n\n",
    "created_at": "2010-06-04T13:43:04Z",
    "labels": [
        "categories",
        "major",
        "bug"
    ],
    "title": "Introspection is failing on polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9138",
    "user": "jbandlow"
}
```
Assignee: nthiery

CC:  sage-combinat robertwb

Keywords: introspection

Example:

```
sage: R.<x> = QQ[] 
sage: R.su<tab> 
R.sum                               R.summation 
R.summation_from_element_class_add 
sage: R.sum? 
Object `R.sum` not found. 
sage: R.sum() 
--------------------------------------------------------------------------- 
AttributeError                            Traceback (most recent call last) 
```


See http://groups.google.com/group/sage-devel/browse_thread/thread/4780192a11a8b591 for more discussion.

Issue created by migration from https://trac.sagemath.org/ticket/9138





---

archive/issue_comments_085169.json:
```json
{
    "body": "Changing keywords from \"introspection\" to \"introspection, categories\".",
    "created_at": "2010-06-05T15:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85169",
    "user": "nthiery"
}
```

Changing keywords from "introspection" to "introspection, categories".



---

archive/issue_comments_085170.json:
```json
{
    "body": "This ticket seems to be a duplicate of #8613.",
    "created_at": "2010-06-05T19:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85170",
    "user": "mmezzarobba"
}
```

This ticket seems to be a duplicate of #8613.



---

archive/issue_comments_085171.json:
```json
{
    "body": "Replying to [comment:2 mmezzarobba]:\n> This ticket seems to be a duplicate of #8613.\n\nIndeed. This should have ringed a bell to me!\n\nSince I have already recycled this ticket to \"Categories for\npolynomial ring\", I leave the two tickets as is. Once this ticket will\nbe closed, it should be possible to close #8613 as well.",
    "created_at": "2010-06-07T07:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85171",
    "user": "nthiery"
}
```

Replying to [comment:2 mmezzarobba]:
> This ticket seems to be a duplicate of #8613.

Indeed. This should have ringed a bell to me!

Since I have already recycled this ticket to "Categories for
polynomial ring", I leave the two tickets as is. Once this ticket will
be closed, it should be possible to close #8613 as well.



---

archive/issue_comments_085172.json:
```json
{
    "body": "This ticket is just about a single kind of parent classes. Rather than going through a long list of parent classes one by one and inserting the missing pieces: Wouldn't it be a more thorough approach to provide a *default* implementation for the attributes needed in the category framework, in cases where it makes sense? \n\nHere is an example:\n\n```\nsage: R.<x,y> = QQ[]\nsage: 'element_class' in dir(R)\nTrue\nsage: hasattr(R,'element_class')\nFalse\n```\n\n\nIf I am not mistaken, \"element_class\" should be implemented by providing the attribute \"Element\". \n\nBut is there a reason why element_class is a dynamic meta-class and not a regular method? Since any parent class has a \"an_element\" method, it seems to me that the following default implementation makes sense (and it solves the problem in my example above):\n\n```\n    def element_class(self):\n        try:\n            return self.Element\n        except AttributeError:\n            return self.an_element().__class__\n```\n\n\nIt seems to me that providing reasonable default implementations would, on the long run, be easier than going through any single parent class. But certainly other people know more about the \"how-to\" of categories.",
    "created_at": "2010-08-01T11:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85172",
    "user": "SimonKing"
}
```

This ticket is just about a single kind of parent classes. Rather than going through a long list of parent classes one by one and inserting the missing pieces: Wouldn't it be a more thorough approach to provide a *default* implementation for the attributes needed in the category framework, in cases where it makes sense? 

Here is an example:

```
sage: R.<x,y> = QQ[]
sage: 'element_class' in dir(R)
True
sage: hasattr(R,'element_class')
False
```


If I am not mistaken, "element_class" should be implemented by providing the attribute "Element". 

But is there a reason why element_class is a dynamic meta-class and not a regular method? Since any parent class has a "an_element" method, it seems to me that the following default implementation makes sense (and it solves the problem in my example above):

```
    def element_class(self):
        try:
            return self.Element
        except AttributeError:
            return self.an_element().__class__
```


It seems to me that providing reasonable default implementations would, on the long run, be easier than going through any single parent class. But certainly other people know more about the "how-to" of categories.



---

archive/issue_comments_085173.json:
```json
{
    "body": "Replying to [comment:4 SimonKing]:\n> But is there a reason why element_class is a dynamic meta-class and not a regular method?\n\nSorry, I just noticed that \"element_class\" is not a method at all: I assumed that it should be used like `R.element_class()`, but sadly it is `R.element_class` without calling the attribute. So, one attribute (element_class) is implemented by providing another attribute (Element).\n\nAnyway, if there shall be a default implementation for element_class then unfortunately it must be in `__getattr__`.",
    "created_at": "2010-08-01T12:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85173",
    "user": "SimonKing"
}
```

Replying to [comment:4 SimonKing]:
> But is there a reason why element_class is a dynamic meta-class and not a regular method?

Sorry, I just noticed that "element_class" is not a method at all: I assumed that it should be used like `R.element_class()`, but sadly it is `R.element_class` without calling the attribute. So, one attribute (element_class) is implemented by providing another attribute (Element).

Anyway, if there shall be a default implementation for element_class then unfortunately it must be in `__getattr__`.



---

archive/issue_comments_085174.json:
```json
{
    "body": "Replying to [comment:5 SimonKing]:\n> Replying to [comment:4 SimonKing]:\n> > But is there a reason why element_class is a dynamic meta-class and not a regular method?\n> \n> Sorry, I just noticed that \"element_class\" is not a method at all...\n\nAgain wrong. I found in sage.structure.parent that there is indeed a *method* element_class -- with a lazy_attribute decorator. I am still confused by that programming style, so, better I shut up.\n\nAnyway, changing the element_class method so that an_element is used (rather than raising an `AttributeError`) did not help. Can you explain why this does not work?",
    "created_at": "2010-08-01T12:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85174",
    "user": "SimonKing"
}
```

Replying to [comment:5 SimonKing]:
> Replying to [comment:4 SimonKing]:
> > But is there a reason why element_class is a dynamic meta-class and not a regular method?
> 
> Sorry, I just noticed that "element_class" is not a method at all...

Again wrong. I found in sage.structure.parent that there is indeed a *method* element_class -- with a lazy_attribute decorator. I am still confused by that programming style, so, better I shut up.

Anyway, changing the element_class method so that an_element is used (rather than raising an `AttributeError`) did not help. Can you explain why this does not work?



---

archive/issue_comments_085175.json:
```json
{
    "body": "Question: Is it OK to broaden the scope of this ticket, namely to use the category framework for everything that comes from sage/rings/ring.pyx? Or shall it be restricted to polynomial rings.",
    "created_at": "2011-03-29T08:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85175",
    "user": "SimonKing"
}
```

Question: Is it OK to broaden the scope of this ticket, namely to use the category framework for everything that comes from sage/rings/ring.pyx? Or shall it be restricted to polynomial rings.



---

archive/issue_comments_085176.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-29T13:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85176",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085177.json:
```json
{
    "body": "Since #9944 almost has a positive review but does not entirely fix the bug reported here, I'm posting my patch here, building on top of that.\n\nExamples:\n\nWith the patches from #9944:\n\n```\nsage: QQ['x'].category()        # why not additionally an algebra?\nCategory of euclidean domains\nsage: QQ['x','y'].category()    # why not an algebra?\nCategory of commutative rings\nsage: SteenrodAlgebra(2)['x'].category()  # this is wrong\nCategory of commutative rings\nsage: QQ['x','y'].sum([1,1])\nTraceback (most recent call last):\n...\nAttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular' object has no attribute 'sum'\n```\n\n\nAdding my (not yet submitted) patch, I get:\n\n```\nsage: QQ['x'].category()\nJoin of Category of euclidean domains and Category of commutative algebras over Rational Field\nsage: QQ['x','y'].category()\nCategory of commutative algebras over Rational Field\nsage: SteenrodAlgebra(2)['x'].category()\nCategory of algebras over mod 2 Steenrod algebra\nsage: QQ['x','y'].sum([1,1])\n2\n```\n\n\nSo, I think the bug reported here is fixed. For me, all doctests pass.\n\nDepends on #9944",
    "created_at": "2011-03-29T13:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85177",
    "user": "SimonKing"
}
```

Since #9944 almost has a positive review but does not entirely fix the bug reported here, I'm posting my patch here, building on top of that.

Examples:

With the patches from #9944:

```
sage: QQ['x'].category()        # why not additionally an algebra?
Category of euclidean domains
sage: QQ['x','y'].category()    # why not an algebra?
Category of commutative rings
sage: SteenrodAlgebra(2)['x'].category()  # this is wrong
Category of commutative rings
sage: QQ['x','y'].sum([1,1])
Traceback (most recent call last):
...
AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular' object has no attribute 'sum'
```


Adding my (not yet submitted) patch, I get:

```
sage: QQ['x'].category()
Join of Category of euclidean domains and Category of commutative algebras over Rational Field
sage: QQ['x','y'].category()
Category of commutative algebras over Rational Field
sage: SteenrodAlgebra(2)['x'].category()
Category of algebras over mod 2 Steenrod algebra
sage: QQ['x','y'].sum([1,1])
2
```


So, I think the bug reported here is fixed. For me, all doctests pass.

Depends on #9944



---

archive/issue_comments_085178.json:
```json
{
    "body": "Replying to [comment:8 SimonKing]:\n> Adding my (not yet submitted) patch, ...\n\nOops, I meant: That's with the patch that I *have* submitted...",
    "created_at": "2011-03-29T15:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85178",
    "user": "SimonKing"
}
```

Replying to [comment:8 SimonKing]:
> Adding my (not yet submitted) patch, ...

Oops, I meant: That's with the patch that I *have* submitted...



---

archive/issue_comments_085179.json:
```json
{
    "body": "Hi Simon,\n\nI haven't been following all the details of this, but thanks for the patch!  One question I have is whether there is a performance penalty for this, and if so, to what degree is that acceptable. On my machine, I noticed about a 10% slow-down for\n\n```\n    sage: R.<x> = QQ['x']\n    sage: timeit('f = x^2 + 1')\n```\n\nafter applying the patches at #9944 and here. I did not do any rigorous testing so this may be spurious, but I'm not sure this should be given a positive review unless this issue has at least been considered.\n\nIf this has already happened and I missed the discussion, then I apologize. Just point me to it and I'll shut up and go away. :)",
    "created_at": "2011-03-29T16:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85179",
    "user": "jbandlow"
}
```

Hi Simon,

I haven't been following all the details of this, but thanks for the patch!  One question I have is whether there is a performance penalty for this, and if so, to what degree is that acceptable. On my machine, I noticed about a 10% slow-down for

```
    sage: R.<x> = QQ['x']
    sage: timeit('f = x^2 + 1')
```

after applying the patches at #9944 and here. I did not do any rigorous testing so this may be spurious, but I'm not sure this should be given a positive review unless this issue has at least been considered.

If this has already happened and I missed the discussion, then I apologize. Just point me to it and I'll shut up and go away. :)



---

archive/issue_comments_085180.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-03-29T16:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85180",
    "user": "jbandlow"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_085181.json:
```json
{
    "body": "Hi Jason,\n\nReplying to [comment:10 jbandlow]:\n> I did not do any rigorous testing so this may be spurious, but I'm not sure this should be given a positive review unless this issue has at least been considered.\n\nYou are right, things like this should be considered. However, I wonder where a slow-down might come from.\n\n> If this has already happened and I missed the discussion, then I apologize. Just point me to it and I'll shut up and go away. :)\n\nNo, I wasn't testing the performance. Aparently I work in cycles: Recently I had several patches that considerably increased performance, and perhaps I am now in a slow mood again...\n\nAnyway, I'll do some tests now.",
    "created_at": "2011-03-29T16:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85181",
    "user": "SimonKing"
}
```

Hi Jason,

Replying to [comment:10 jbandlow]:
> I did not do any rigorous testing so this may be spurious, but I'm not sure this should be given a positive review unless this issue has at least been considered.

You are right, things like this should be considered. However, I wonder where a slow-down might come from.

> If this has already happened and I missed the discussion, then I apologize. Just point me to it and I'll shut up and go away. :)

No, I wasn't testing the performance. Aparently I work in cycles: Recently I had several patches that considerably increased performance, and perhaps I am now in a slow mood again...

Anyway, I'll do some tests now.



---

archive/issue_comments_085182.json:
```json
{
    "body": "Here are the test results:\n\nWithout all patches:\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 22.5 \u00c2\u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 24.5 \u00c2\u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 87.7 \u00c2\u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 114 \u00c2\u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 21.9 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 40 \u00c2\u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 26.3 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 239 \u00c2\u00b5s per loop\n```\n\n\nWith the patches from #9944:\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 25.6 \u00c2\u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 26.7 \u00c2\u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 109 \u00c2\u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 121 \u00c2\u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 31.4 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 40 \u00c2\u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 26.8 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 250 \u00c2\u00b5s per loop\n```\n\n\nWith the patches from #9944 and the patch from here:\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 25.7 \u00c2\u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 28.3 \u00c2\u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 115 \u00c2\u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 125 \u00c2\u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 31 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 17.5 \u00c2\u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 25.1 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 256 \u00c2\u00b5s per loop\n```\n\n\nNote, however, that the numbers arent't very stable\n\n```\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 20.9 \u00c2\u00b5s per loop\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 20.8 \u00c2\u00b5s per loop\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 22.6 \u00c2\u00b5s per loop\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 37.9 \u00c2\u00b5s per loop\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 15.4 \u00c2\u00b5s per loop\n```\n\n\nBut there is a tendency: Things tend to be slower, both with #9944 and with my patch.\n\nSo, it should be worth while to analyse the arithmetic with prun.",
    "created_at": "2011-03-29T16:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85182",
    "user": "SimonKing"
}
```

Here are the test results:

Without all patches:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 22.5 Âµs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 24.5 Âµs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 87.7 Âµs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 114 Âµs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 21.9 Âµs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 40 Âµs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 26.3 Âµs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 239 Âµs per loop
```


With the patches from #9944:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 25.6 Âµs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 26.7 Âµs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 109 Âµs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 121 Âµs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 31.4 Âµs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 40 Âµs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 26.8 Âµs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 250 Âµs per loop
```


With the patches from #9944 and the patch from here:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 25.7 Âµs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 28.3 Âµs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 115 Âµs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 125 Âµs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 31 Âµs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 17.5 Âµs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 25.1 Âµs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 256 Âµs per loop
```


Note, however, that the numbers arent't very stable

```
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 20.9 Âµs per loop
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 20.8 Âµs per loop
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 22.6 Âµs per loop
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 37.9 Âµs per loop
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 15.4 Âµs per loop
```


But there is a tendency: Things tend to be slower, both with #9944 and with my patch.

So, it should be worth while to analyse the arithmetic with prun.



---

archive/issue_comments_085183.json:
```json
{
    "body": "By the way, I think we should add doctests of the type\n\n```\nsage: TestSuite(QQ['x']).run()\nsage: TestSuite(QQ['x','y']).run()\nsage: TestSuite(QQ['x','y']['t']).run()\nsage: TestSuite(GF(3)['t']).run()\nsage: TestSuite(ZZ['t']).run()\n```\n\n\nIf I understand the ticket description, this used to fail.",
    "created_at": "2011-03-29T17:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85183",
    "user": "SimonKing"
}
```

By the way, I think we should add doctests of the type

```
sage: TestSuite(QQ['x']).run()
sage: TestSuite(QQ['x','y']).run()
sage: TestSuite(QQ['x','y']['t']).run()
sage: TestSuite(GF(3)['t']).run()
sage: TestSuite(ZZ['t']).run()
```


If I understand the ticket description, this used to fail.



---

archive/issue_comments_085184.json:
```json
{
    "body": "Idea: Could it be that the length of the method resolution order is responsible for the slow-down?\n\nWith all patches:\n\n```\nsage: len(type(QQ['x']).mro())\n47\nsage: len(type(QQ['x','y']).mro())\n11\nsage: len(type(GF(3)['x','y']).mro())\n11\nsage: len(type(GF(3)['x']).mro())\n49\nsage: len(type(ZZ['x']).mro())\n41\nsage: len(type(ZZ['x']['t']).mro())\n41\nsage: len(type(QQ['x'].gen()).mro())\n9\nsage: len(type(QQ['x','y'].gen()).mro())\n8\nsage: len(type(GF(3)['x','y'].gen()).mro())\n8\nsage: len(type(GF(3)['x'].gen()).mro())\n10\nsage: len(type(ZZ['x'].gen()).mro())\n9\nsage: len(type(ZZ['x']['t'].gen()).mro())\n9\n```\n\n\nWith only the patches from #9944:\n\n```\nsage: len(type(QQ['x']).mro())\n39\nsage: len(type(QQ['x','y']).mro())\n11\nsage: len(type(GF(3)['x','y']).mro())\n11\nsage: len(type(GF(3)['x']).mro())\n41\nsage: len(type(ZZ['x']).mro())\n34\nsage: len(type(ZZ['x']['t']).mro())\n34\nsage: len(type(QQ['x'].gen()).mro())\n9\nsage: len(type(QQ['x','y'].gen()).mro())\n8\nsage: len(type(GF(3)['x','y'].gen()).mro())\n8\nsage: len(type(GF(3)['x'].gen()).mro())\n10\nsage: len(type(ZZ['x'].gen()).mro())\n9\nsage: len(type(ZZ['x']['t'].gen()).mro())\n9\n```\n\n\nWithout these patches:\n\n```\nsage: len(type(QQ['x']).mro())\n18\nsage: len(type(QQ['x','y']).mro())\n11\nsage: len(type(GF(3)['x','y']).mro())\n11\nsage: len(type(GF(3)['x']).mro())\n20\nsage: len(type(ZZ['x']).mro())\n15\nsage: len(type(ZZ['x']['t']).mro())\n15\nsage: len(type(QQ['x'].gen()).mro())\n9\nsage: len(type(QQ['x','y'].gen()).mro())\n8\nsage: len(type(GF(3)['x','y'].gen()).mro())\n8\nsage: len(type(GF(3)['x'].gen()).mro())\n10\nsage: len(type(ZZ['x'].gen()).mro())\n9\nsage: len(type(ZZ['x']['t'].gen()).mro())\n9\n```\n\n\nSo, the mro of the rings becomes much longer. Could it be that, as a consequence, it takes longer to find common and frequently used methods such as `R.parent()` and `R.base_ring()`?",
    "created_at": "2011-03-29T17:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85184",
    "user": "SimonKing"
}
```

Idea: Could it be that the length of the method resolution order is responsible for the slow-down?

With all patches:

```
sage: len(type(QQ['x']).mro())
47
sage: len(type(QQ['x','y']).mro())
11
sage: len(type(GF(3)['x','y']).mro())
11
sage: len(type(GF(3)['x']).mro())
49
sage: len(type(ZZ['x']).mro())
41
sage: len(type(ZZ['x']['t']).mro())
41
sage: len(type(QQ['x'].gen()).mro())
9
sage: len(type(QQ['x','y'].gen()).mro())
8
sage: len(type(GF(3)['x','y'].gen()).mro())
8
sage: len(type(GF(3)['x'].gen()).mro())
10
sage: len(type(ZZ['x'].gen()).mro())
9
sage: len(type(ZZ['x']['t'].gen()).mro())
9
```


With only the patches from #9944:

```
sage: len(type(QQ['x']).mro())
39
sage: len(type(QQ['x','y']).mro())
11
sage: len(type(GF(3)['x','y']).mro())
11
sage: len(type(GF(3)['x']).mro())
41
sage: len(type(ZZ['x']).mro())
34
sage: len(type(ZZ['x']['t']).mro())
34
sage: len(type(QQ['x'].gen()).mro())
9
sage: len(type(QQ['x','y'].gen()).mro())
8
sage: len(type(GF(3)['x','y'].gen()).mro())
8
sage: len(type(GF(3)['x'].gen()).mro())
10
sage: len(type(ZZ['x'].gen()).mro())
9
sage: len(type(ZZ['x']['t'].gen()).mro())
9
```


Without these patches:

```
sage: len(type(QQ['x']).mro())
18
sage: len(type(QQ['x','y']).mro())
11
sage: len(type(GF(3)['x','y']).mro())
11
sage: len(type(GF(3)['x']).mro())
20
sage: len(type(ZZ['x']).mro())
15
sage: len(type(ZZ['x']['t']).mro())
15
sage: len(type(QQ['x'].gen()).mro())
9
sage: len(type(QQ['x','y'].gen()).mro())
8
sage: len(type(GF(3)['x','y'].gen()).mro())
8
sage: len(type(GF(3)['x'].gen()).mro())
10
sage: len(type(ZZ['x'].gen()).mro())
9
sage: len(type(ZZ['x']['t'].gen()).mro())
9
```


So, the mro of the rings becomes much longer. Could it be that, as a consequence, it takes longer to find common and frequently used methods such as `R.parent()` and `R.base_ring()`?



---

archive/issue_comments_085185.json:
```json
{
    "body": "Here are times for basic methods (i.e., methods that require to walk up much of the mro):\n\nWithout patches\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 253 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 447 ns per loop\nsage: R.<x> = QQ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 249 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 508 ns per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 262 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 555 ns per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 249 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 446 ns per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 240 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 286 ns per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 240 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 282 ns per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 245 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 284 ns per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 266 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 413 ns per loop\n```\n\n\nWith all patches\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 539 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 476 ns per loop\nsage: R.<x> = QQ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 247 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 652 ns per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 670 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\nsage: R.<x> = QQ['t'][]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 254 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 496 ns per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 583 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 297 ns per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 237 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 307 ns per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 237 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 294 ns per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('x.parent()',number=10^5)\n100000 loops, best of 3: 277 ns per loop\nsage: timeit('R.base_ring()',number=10^5)\n100000 loops, best of 3: 477 ns per loop\n```\n\n\nSo, there seems to be some slow-down in accessing basic methods.",
    "created_at": "2011-03-29T18:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85185",
    "user": "SimonKing"
}
```

Here are times for basic methods (i.e., methods that require to walk up much of the mro):

Without patches

```
sage: R.<x> = ZZ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 253 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 447 ns per loop
sage: R.<x> = QQ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 249 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 508 ns per loop
sage: R.<x> = GF(3)[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 262 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 555 ns per loop
sage: R.<x> = QQ['t'][]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 249 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 446 ns per loop
sage: R.<x,y> = ZZ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 240 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 286 ns per loop
sage: R.<x,y> = QQ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 240 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 282 ns per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 245 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 284 ns per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 266 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 413 ns per loop
```


With all patches

```
sage: R.<x> = ZZ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 539 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 476 ns per loop
sage: R.<x> = QQ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 247 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 652 ns per loop
sage: R.<x> = GF(3)[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 670 ns per loop
sage: timeit('R.base_ring()',number=10^5)
sage: R.<x> = QQ['t'][]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 254 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 496 ns per loop
sage: R.<x,y> = ZZ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 583 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 297 ns per loop
sage: R.<x,y> = QQ[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 237 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 307 ns per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 237 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 294 ns per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('x.parent()',number=10^5)
100000 loops, best of 3: 277 ns per loop
sage: timeit('R.base_ring()',number=10^5)
100000 loops, best of 3: 477 ns per loop
```


So, there seems to be some slow-down in accessing basic methods.



---

archive/issue_comments_085186.json:
```json
{
    "body": "But apparently one *can* work around the mro:\n\n```\nsage: timeit('R.base_ring()',number=10^6)\n1000000 loops, best of 3: 470 ns per loop\nsage: timeit('Parent.base_ring(R)',number=10^6)\n1000000 loops, best of 3: 352 ns per loop\n```\n\n\nSo, if speed matters, it might be worth while to use the idiom above to speed things up. I'll ask on sage-devel whether there is a more elegant/pythonic way to cope with a long mro.",
    "created_at": "2011-03-29T18:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85186",
    "user": "SimonKing"
}
```

But apparently one *can* work around the mro:

```
sage: timeit('R.base_ring()',number=10^6)
1000000 loops, best of 3: 470 ns per loop
sage: timeit('Parent.base_ring(R)',number=10^6)
1000000 loops, best of 3: 352 ns per loop
```


So, if speed matters, it might be worth while to use the idiom above to speed things up. I'll ask on sage-devel whether there is a more elegant/pythonic way to cope with a long mro.



---

archive/issue_comments_085187.json:
```json
{
    "body": "I had to rebase my patch since it \n\nDepends on #9944",
    "created_at": "2011-03-30T14:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85187",
    "user": "SimonKing"
}
```

I had to rebase my patch since it 

Depends on #9944



---

archive/issue_comments_085188.json:
```json
{
    "body": "With the latest patches, I obtain the following timings:\n\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 25.8 \u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 27.8 \u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 112 \u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 124 \u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 12.7 \u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 15.7 \u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 10.3 \u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 148 \u00b5s per loop\n```\n\n\nWithout these patches:\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 22.7 \u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 24.2 \u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 87 \u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 113 \u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 13 \u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 16.3 \u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 10.5 \u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 237 \u00b5s per loop\n```\n\n\nIn other words, there is a mild deceleration in the univariate case and a mild (and in one case considerable) *acceleration* in the multivariate case.\n\nI don't understand why. But perhaps a reviewer has an idea, and can also state his or her opinion how bad the deceleration is compared with the acceleration?",
    "created_at": "2011-03-30T14:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85188",
    "user": "SimonKing"
}
```

With the latest patches, I obtain the following timings:


```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 25.8 µs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 27.8 µs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 112 µs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 124 µs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 12.7 µs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 15.7 µs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 10.3 µs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 148 µs per loop
```


Without these patches:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 22.7 µs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 24.2 µs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 87 µs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 113 µs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 13 µs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 16.3 µs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 10.5 µs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 237 µs per loop
```


In other words, there is a mild deceleration in the univariate case and a mild (and in one case considerable) *acceleration* in the multivariate case.

I don't understand why. But perhaps a reviewer has an idea, and can also state his or her opinion how bad the deceleration is compared with the acceleration?



---

archive/issue_comments_085189.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-03-30T14:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85189",
    "user": "SimonKing"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_085190.json:
```json
{
    "body": "The patch is rebased again.\n\nNote that meanwhile #9944 does not mean a slow down but a speed up! The patch from here, unfortunately, makes things slightly slower, again. But compared with unpatched Sage, it is not significantly slower in any case, but still much faster in some cases (and in two cases even faster than with #9944 alone).\n\nHere are the latest timings.\n\nUnpatched:\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 23.4 \u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 24.6 \u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 87.9 \u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 113 \u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 13 \u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 16.6 \u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 10.8 \u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 238 \u00b5s per loop\nsage: R.<x,y> = Qp(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 511 \u00b5s per loop\nsage: R.<x> = Qp(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 1.06 ms per loop\n```\n\n\nWith #9944 and #9138:\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 8.95 \u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 8.33 \u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 76.7 \u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 82.7 \u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 13.2 \u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 16.4 \u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 11 \u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 106 \u00b5s per loop\nsage: R.<x,y> = Qp(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 421 \u00b5s per loop\nsage: R.<x> = Qp(3)[]\nsage: timeit('(2*x-1)^2+5', number=10^4)\n10000 loops, best of 3: 1.1 ms per loop\n```\n\n\nSo, I hope it can be reviewed.\n\nFor the patch bot:\n\nDepends on #9944",
    "created_at": "2011-03-31T11:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85190",
    "user": "SimonKing"
}
```

The patch is rebased again.

Note that meanwhile #9944 does not mean a slow down but a speed up! The patch from here, unfortunately, makes things slightly slower, again. But compared with unpatched Sage, it is not significantly slower in any case, but still much faster in some cases (and in two cases even faster than with #9944 alone).

Here are the latest timings.

Unpatched:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 23.4 µs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 24.6 µs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 87.9 µs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 113 µs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 13 µs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 16.6 µs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 10.8 µs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 238 µs per loop
sage: R.<x,y> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 511 µs per loop
sage: R.<x> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 1.06 ms per loop
```


With #9944 and #9138:

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 8.95 µs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 8.33 µs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 76.7 µs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 82.7 µs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 13.2 µs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 16.4 µs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 11 µs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 106 µs per loop
sage: R.<x,y> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 421 µs per loop
sage: R.<x> = Qp(3)[]
sage: timeit('(2*x-1)^2+5', number=10^4)
10000 loops, best of 3: 1.1 ms per loop
```


So, I hope it can be reviewed.

For the patch bot:

Depends on #9944



---

archive/issue_comments_085191.json:
```json
{
    "body": "Not good. Many doctests fail. First analysis: When I implemented the improved base ring conversion for polynomial rings, I noticed that `_lmul_` for p-adics returns None (quite a bug). I thought that I had worked around that bug, as the doc tests pass with the patches from #9944.\n\nBut apparently it hit me here...",
    "created_at": "2011-03-31T13:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85191",
    "user": "SimonKing"
}
```

Not good. Many doctests fail. First analysis: When I implemented the improved base ring conversion for polynomial rings, I noticed that `_lmul_` for p-adics returns None (quite a bug). I thought that I had worked around that bug, as the doc tests pass with the patches from #9944.

But apparently it hit me here...



---

archive/issue_comments_085192.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-31T13:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85192",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085193.json:
```json
{
    "body": "Changing keywords from \"introspection, categories\" to \"introspection, categories for rings\".",
    "created_at": "2011-04-01T10:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85193",
    "user": "SimonKing"
}
```

Changing keywords from "introspection, categories" to "introspection, categories for rings".



---

archive/issue_comments_085194.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-01T10:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85194",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085195.json:
```json
{
    "body": "I think now we are ready for review.\n\nLong tests passed for me.\n\nBy the way, the long tests made me fix another bug. Namely, in the `__setstate__` method of `CategoryObject`, the existing category was overridden by the value found in the pickle. If you do so for the ration field, than afterwards its category is not the category of quotient fields but of rings. Result: The pickle jar broke.\n\nSolution: If the category in the pickle is None, then `self._category` will be preserved. Otherwise, it will be the join of `self._category` (if not None) with the category found in the pickle.\n\nI don't know whether you agree with the second part of that solution. But I think the first part should be clear.\n\nAlso, I added some `TestSuite` tests for various flavours of polynomial rings.\n\nFor the patch bot:\n\nDepends on #9944",
    "created_at": "2011-04-01T10:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85195",
    "user": "SimonKing"
}
```

I think now we are ready for review.

Long tests passed for me.

By the way, the long tests made me fix another bug. Namely, in the `__setstate__` method of `CategoryObject`, the existing category was overridden by the value found in the pickle. If you do so for the ration field, than afterwards its category is not the category of quotient fields but of rings. Result: The pickle jar broke.

Solution: If the category in the pickle is None, then `self._category` will be preserved. Otherwise, it will be the join of `self._category` (if not None) with the category found in the pickle.

I don't know whether you agree with the second part of that solution. But I think the first part should be clear.

Also, I added some `TestSuite` tests for various flavours of polynomial rings.

For the patch bot:

Depends on #9944



---

archive/issue_comments_085196.json:
```json
{
    "body": "Replying to [comment:20 SimonKing]:\n> Not good. Many doctests fail. First analysis: When I implemented the improved base ring conversion for polynomial rings, I noticed that `_lmul_` for p-adics returns None (quite a bug).\n\nFor the record: this *might* be intentional. The coercion protocle\ndoes specify that the arithmetic operation may return None\nunder certain circumstances to state that, after all, they can't\nhandle that operation, and some other approach should be tried.\n\nCheers,\n\t\t\tNicolas",
    "created_at": "2011-04-01T15:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85196",
    "user": "nthiery"
}
```

Replying to [comment:20 SimonKing]:
> Not good. Many doctests fail. First analysis: When I implemented the improved base ring conversion for polynomial rings, I noticed that `_lmul_` for p-adics returns None (quite a bug).

For the record: this *might* be intentional. The coercion protocle
does specify that the arithmetic operation may return None
under certain circumstances to state that, after all, they can't
handle that operation, and some other approach should be tried.

Cheers,
			Nicolas



---

archive/issue_comments_085197.json:
```json
{
    "body": "Replying to [comment:22 nthiery]:\n> Replying to [comment:20 SimonKing]:\n> > Not good. Many doctests fail. First analysis: When I implemented the improved base ring conversion for polynomial rings, I noticed that `_lmul_` for p-adics returns None (quite a bug).\n> \n> For the record: this *might* be intentional. \n\nOK, but really just for the record -- because I did not change it. Instead, I test what `_lmul_` does, and if it returns None then it will not be used in the base ring conversion.",
    "created_at": "2011-04-01T15:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85197",
    "user": "SimonKing"
}
```

Replying to [comment:22 nthiery]:
> Replying to [comment:20 SimonKing]:
> > Not good. Many doctests fail. First analysis: When I implemented the improved base ring conversion for polynomial rings, I noticed that `_lmul_` for p-adics returns None (quite a bug).
> 
> For the record: this *might* be intentional. 

OK, but really just for the record -- because I did not change it. Instead, I test what `_lmul_` does, and if it returns None then it will not be used in the base ring conversion.



---

archive/issue_comments_085198.json:
```json
{
    "body": "Sorry, apparently I had not applied the patch when I was running the long doc tests. There were a couple of errors. So, needs work...",
    "created_at": "2011-04-02T10:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85198",
    "user": "SimonKing"
}
```

Sorry, apparently I had not applied the patch when I was running the long doc tests. There were a couple of errors. So, needs work...



---

archive/issue_comments_085199.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-02T10:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85199",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085200.json:
```json
{
    "body": "I think I just fixed it, and it can be reviewed.\n\nDepends on #9944",
    "created_at": "2011-04-02T14:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85200",
    "user": "SimonKing"
}
```

I think I just fixed it, and it can be reviewed.

Depends on #9944



---

archive/issue_comments_085201.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-02T14:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85201",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085202.json:
```json
{
    "body": "FWIW, long tests pass for me.",
    "created_at": "2011-04-02T17:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85202",
    "user": "SimonKing"
}
```

FWIW, long tests pass for me.



---

archive/issue_comments_085203.json:
```json
{
    "body": "But there is one point that I don't like: \n\nWith the patches from #9944), I get\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\"\n\t [26.9 s]\n```\n\nwhich is about the same as without these patches. So, there is no speed loss.\n\nBut when I also apply the patch from here, I get\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\"\n         [30.3 s]\n```\n\n\nA similar slow down is visible for the tests from heegner.py.\n\nWhat could be the reason? What arithmetic operations are dominant?\n\nMy original impression was that it is operations in large integer quotient rings. But that isn't the problem according to these tests:\n\n\n```\nsage: R = Integers(3814697265625)\nsage: a = R(1021573325796)\nsage: b = R(2884990864521)\nsage: timeit('a+b',number=10^6)\n1000000 loops, best of 3: 297 ns per loop\nsage: timeit('a*b',number=10^6)\n1000000 loops, best of 3: 397 ns per loop\nsage: timeit('a+2',number=10^6)\n1000000 loops, best of 3: 1.24 \u00b5s per loop\nsage: timeit('a*2',number=10^6)\n1000000 loops, best of 3: 1.4 \u00b5s per loop\nsage: timeit('a.sqrt()')\n625 loops, best of 3: 146 \u00b5s per loop\n```\n\n\nI get more or less the same timings with or without the patch.\n\nAny idea?",
    "created_at": "2011-04-11T16:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85203",
    "user": "SimonKing"
}
```

But there is one point that I don't like: 

With the patches from #9944), I get

```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"
	 [26.9 s]
```

which is about the same as without these patches. So, there is no speed loss.

But when I also apply the patch from here, I get

```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"
         [30.3 s]
```


A similar slow down is visible for the tests from heegner.py.

What could be the reason? What arithmetic operations are dominant?

My original impression was that it is operations in large integer quotient rings. But that isn't the problem according to these tests:


```
sage: R = Integers(3814697265625)
sage: a = R(1021573325796)
sage: b = R(2884990864521)
sage: timeit('a+b',number=10^6)
1000000 loops, best of 3: 297 ns per loop
sage: timeit('a*b',number=10^6)
1000000 loops, best of 3: 397 ns per loop
sage: timeit('a+2',number=10^6)
1000000 loops, best of 3: 1.24 µs per loop
sage: timeit('a*2',number=10^6)
1000000 loops, best of 3: 1.4 µs per loop
sage: timeit('a.sqrt()')
625 loops, best of 3: 146 µs per loop
```


I get more or less the same timings with or without the patch.

Any idea?



---

archive/issue_comments_085204.json:
```json
{
    "body": "I see that there is a lot of slow-down in the Monsky-Washnitzer code, namely arithmetic in `SpecialCubicQuotientRing`:\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: x, T = R.gens()\nsage: x\n(0) + (1)*x + (0)*x^2\nsage: T\n(T) + (0)*x + (0)*x^2\n```\n\nIn vanilla sage-4.6.2, I get\nsage: timeit('x*T')\n625 loops, best of 3: 491 \u00b5s per loop\n}}}\nWith the patches, I get\n\n```\nsage: timeit('x*T')\n625 loops, best of 3: 612 \u00b5s per loop\n```\n\n\nSo, there is your problem!",
    "created_at": "2011-04-11T16:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85204",
    "user": "SimonKing"
}
```

I see that there is a lot of slow-down in the Monsky-Washnitzer code, namely arithmetic in `SpecialCubicQuotientRing`:

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: x, T = R.gens()
sage: x
(0) + (1)*x + (0)*x^2
sage: T
(T) + (0)*x + (0)*x^2
```

In vanilla sage-4.6.2, I get
sage: timeit('x*T')
625 loops, best of 3: 491 µs per loop
}}}
With the patches, I get

```
sage: timeit('x*T')
625 loops, best of 3: 612 µs per loop
```


So, there is your problem!



---

archive/issue_comments_085205.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-11T16:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85205",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085206.json:
```json
{
    "body": "Closing in...\n\nWith patches\n\n```\nsage: %prun L=[x*T for _ in xrange(1000)]\n         392002 function calls in 0.766 CPU seconds\n\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n   384000    0.371    0.000    0.371    0.000 polynomial_ring.py:1836(modulus)\n     1000    0.367    0.000    0.724    0.001 monsky_washnitzer.py:553(_mul_)\n        1    0.017    0.017    0.766    0.766 <string>:1(<module>)\n     2000    0.006    0.000    0.006    0.000 integer_mod_ring.py:726(_repr_)\n     1000    0.003    0.000    0.004    0.000 monsky_washnitzer.py:325(__init__)\n     2000    0.001    0.000    0.001    0.000 {isinstance}\n     2000    0.000    0.000    0.000    0.000 {method 'parent' of 'sage.structure.element.Element' objects}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n```\n\n\nWithout patches:\n\n```\nsage: %prun L=[x*T for _ in xrange(1000)]\n         404602 function calls in 0.684 CPU seconds\n\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n     1000    0.366    0.000    0.651    0.001 monsky_washnitzer.py:553(_mul_)\n   384600    0.234    0.000    0.234    0.000 polynomial_ring.py:1797(modulus)\n     2000    0.047    0.000    0.061    0.000 polynomial_ring.py:212(_element_constructor_)\n        1    0.018    0.018    0.684    0.684 <string>:1(<module>)\n     2000    0.007    0.000    0.007    0.000 integer_mod_ring.py:726(_repr_)\n     2000    0.005    0.000    0.006    0.000 integer_mod_ring.py:911(__cmp__)\n     1000    0.003    0.000    0.004    0.000 monsky_washnitzer.py:325(__init__)\n     4000    0.003    0.000    0.003    0.000 {isinstance}\n     4000    0.001    0.000    0.001    0.000 {method 'parent' of 'sage.structure.element.Element' objects}\n     2000    0.001    0.000    0.001    0.000 {cmp}\n     2000    0.000    0.000    0.000    0.000 {method 'base_ring' of 'sage.structure.category_object.CategoryObject' objects}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n```\n\n\nIn other words: The biggest loss is the call to `modulus()`. That should be possible to fix.",
    "created_at": "2011-04-11T17:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85206",
    "user": "SimonKing"
}
```

Closing in...

With patches

```
sage: %prun L=[x*T for _ in xrange(1000)]
         392002 function calls in 0.766 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   384000    0.371    0.000    0.371    0.000 polynomial_ring.py:1836(modulus)
     1000    0.367    0.000    0.724    0.001 monsky_washnitzer.py:553(_mul_)
        1    0.017    0.017    0.766    0.766 <string>:1(<module>)
     2000    0.006    0.000    0.006    0.000 integer_mod_ring.py:726(_repr_)
     1000    0.003    0.000    0.004    0.000 monsky_washnitzer.py:325(__init__)
     2000    0.001    0.000    0.001    0.000 {isinstance}
     2000    0.000    0.000    0.000    0.000 {method 'parent' of 'sage.structure.element.Element' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


Without patches:

```
sage: %prun L=[x*T for _ in xrange(1000)]
         404602 function calls in 0.684 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.366    0.000    0.651    0.001 monsky_washnitzer.py:553(_mul_)
   384600    0.234    0.000    0.234    0.000 polynomial_ring.py:1797(modulus)
     2000    0.047    0.000    0.061    0.000 polynomial_ring.py:212(_element_constructor_)
        1    0.018    0.018    0.684    0.684 <string>:1(<module>)
     2000    0.007    0.000    0.007    0.000 integer_mod_ring.py:726(_repr_)
     2000    0.005    0.000    0.006    0.000 integer_mod_ring.py:911(__cmp__)
     1000    0.003    0.000    0.004    0.000 monsky_washnitzer.py:325(__init__)
     4000    0.003    0.000    0.003    0.000 {isinstance}
     4000    0.001    0.000    0.001    0.000 {method 'parent' of 'sage.structure.element.Element' objects}
     2000    0.001    0.000    0.001    0.000 {cmp}
     2000    0.000    0.000    0.000    0.000 {method 'base_ring' of 'sage.structure.category_object.CategoryObject' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


In other words: The biggest loss is the call to `modulus()`. That should be possible to fix.



---

archive/issue_comments_085207.json:
```json
{
    "body": "Possible reason:\n\n```\nsage: P = R.poly_ring()\nsage: len(P.__class__.mro())\n14    # without patch\n35    # with patch\n```\n\n\nApparently that makes attribute access slower.",
    "created_at": "2011-04-11T18:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85207",
    "user": "SimonKing"
}
```

Possible reason:

```
sage: P = R.poly_ring()
sage: len(P.__class__.mro())
14    # without patch
35    # with patch
```


Apparently that makes attribute access slower.



---

archive/issue_comments_085208.json:
```json
{
    "body": "I just found that the problem with `modulus` is an excellent use case for the improved cached methods provided by #11115!\n\nNamely, instead of caching the modulus in a Python attribute `__modulus` and have `self.modulus()` return `self.__modulus`, I define `self.modulus()` as a cached method -- and that is a lot faster:\n\nWith the patches:\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: P = R.poly_ring()\nsage: timeit('P.modulus()',number=10^6)\n1000000 loops, best of 3: 226 ns per loop\nsage: x, T = R.gens()\nsage: timeit('x*T')\n625 loops, best of 3: 234 \u00c2\u00b5s per loop\n```\n\n\nWithout the patches (and without the quick cached methods):\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: P = R.poly_ring()\nsage: timeit('P.modulus()',number=10^6)\n1000000 loops, best of 3: 647 ns per loop\nsage: x, T = R.gens()\nsage: timeit('x*T')\n625 loops, best of 3: 495 \u00c2\u00b5s per loop\n```\n\n\nSo, the slow-down turned into a speed-up. I don't know if the doc tests will all pass, but I put it as \"needs review\".\n\nDepends on #9944 #11115 #9976",
    "created_at": "2011-04-11T18:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85208",
    "user": "SimonKing"
}
```

I just found that the problem with `modulus` is an excellent use case for the improved cached methods provided by #11115!

Namely, instead of caching the modulus in a Python attribute `__modulus` and have `self.modulus()` return `self.__modulus`, I define `self.modulus()` as a cached method -- and that is a lot faster:

With the patches:

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: P = R.poly_ring()
sage: timeit('P.modulus()',number=10^6)
1000000 loops, best of 3: 226 ns per loop
sage: x, T = R.gens()
sage: timeit('x*T')
625 loops, best of 3: 234 Âµs per loop
```


Without the patches (and without the quick cached methods):

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: P = R.poly_ring()
sage: timeit('P.modulus()',number=10^6)
1000000 loops, best of 3: 647 ns per loop
sage: x, T = R.gens()
sage: timeit('x*T')
625 loops, best of 3: 495 Âµs per loop
```


So, the slow-down turned into a speed-up. I don't know if the doc tests will all pass, but I put it as "needs review".

Depends on #9944 #11115 #9976



---

archive/issue_comments_085209.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-11T18:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85209",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085210.json:
```json
{
    "body": "Note, however, that `sage -t  \"devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\"` is not up to speed, yet, but not as slow as with the old patch.",
    "created_at": "2011-04-11T19:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85210",
    "user": "SimonKing"
}
```

Note, however, that `sage -t  "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"` is not up to speed, yet, but not as slow as with the old patch.



---

archive/issue_comments_085211.json:
```json
{
    "body": "It could actually be that I there is no regression in Monsky-Washnitzer at all.\n\nI just took the tests from sage/schemes/elliptic_curves/monsky_washnitzer.py and timed each test individually (using timeit). In all cases, the tests went *faster* with my patches - even though \"sage -t\" took 50% longer than without the patches.\n\nMy next guess was that there is a problem with the startup time. Indeed, starting sage without the patches feels \"snappier\".\n\nUsing \"sage -startuptime\", I found with the patches:\n\n```\n## Slowest (including children)\n1.623 sage.all (None)\n0.356 sage.schemes.all (sage.all)\n0.225 elliptic_curves.all (sage.schemes.all)\n0.222 ell_rational_field (elliptic_curves.all)\n0.216 sage.rings.all (sage.all)\n0.214 sage.misc.all (sage.all)\n0.173 sage.algebras.all (sage.all)\n0.153 ell_number_field (ell_rational_field)\n```\n\n\nWithout patch:\n\n```\n## Slowest (including children)\n1.196 sage.all (None)\n0.312 sage.schemes.all (sage.all)\n0.190 twisted.persisted.styles (sage.all)\n0.176 elliptic_curves.all (sage.schemes.all)\n0.172 ell_rational_field (elliptic_curves.all)\n0.172 sage.misc.all (sage.all)\n0.151 ell_number_field (ell_rational_field)\n0.150 ell_field (ell_number_field)\n...\n0.087 sage.rings.all (sage.all)\n...\n0.035 sage.algebras.all (sage.all)\n```\n",
    "created_at": "2011-04-12T07:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85211",
    "user": "SimonKing"
}
```

It could actually be that I there is no regression in Monsky-Washnitzer at all.

I just took the tests from sage/schemes/elliptic_curves/monsky_washnitzer.py and timed each test individually (using timeit). In all cases, the tests went *faster* with my patches - even though "sage -t" took 50% longer than without the patches.

My next guess was that there is a problem with the startup time. Indeed, starting sage without the patches feels "snappier".

Using "sage -startuptime", I found with the patches:

```
## Slowest (including children)
1.623 sage.all (None)
0.356 sage.schemes.all (sage.all)
0.225 elliptic_curves.all (sage.schemes.all)
0.222 ell_rational_field (elliptic_curves.all)
0.216 sage.rings.all (sage.all)
0.214 sage.misc.all (sage.all)
0.173 sage.algebras.all (sage.all)
0.153 ell_number_field (ell_rational_field)
```


Without patch:

```
## Slowest (including children)
1.196 sage.all (None)
0.312 sage.schemes.all (sage.all)
0.190 twisted.persisted.styles (sage.all)
0.176 elliptic_curves.all (sage.schemes.all)
0.172 ell_rational_field (elliptic_curves.all)
0.172 sage.misc.all (sage.all)
0.151 ell_number_field (ell_rational_field)
0.150 ell_field (ell_number_field)
...
0.087 sage.rings.all (sage.all)
...
0.035 sage.algebras.all (sage.all)
```




---

archive/issue_comments_085212.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-12T07:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85212",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085213.json:
```json
{
    "body": "It turns out that the measuring of the startup time is by far too flaky. Without the patches, the startup time varies from \"1.008 sage.all (None)\" to \"1.518 sage.all (None)\". There seems to be a regression, though.",
    "created_at": "2011-04-12T07:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85213",
    "user": "SimonKing"
}
```

It turns out that the measuring of the startup time is by far too flaky. Without the patches, the startup time varies from "1.008 sage.all (None)" to "1.518 sage.all (None)". There seems to be a regression, though.



---

archive/issue_comments_085214.json:
```json
{
    "body": "Replying to [comment:35 SimonKing]:\n> It turns out that the measuring of the startup time is by far too flaky. Without the patches, the startup time varies from \"1.008 sage.all (None)\" to \"1.518 sage.all (None)\". There seems to be a regression, though.\n\nI have to correct myself.\n\nIt turned out that both the slow-down in the startup time *and* the slow-down in the Monsky-Washnitzer code are caused by #11115. So, I suggest that I prepare a new patch that is not based on #11115.",
    "created_at": "2011-04-13T12:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85214",
    "user": "SimonKing"
}
```

Replying to [comment:35 SimonKing]:
> It turns out that the measuring of the startup time is by far too flaky. Without the patches, the startup time varies from "1.008 sage.all (None)" to "1.518 sage.all (None)". There seems to be a regression, though.

I have to correct myself.

It turned out that both the slow-down in the startup time *and* the slow-down in the Monsky-Washnitzer code are caused by #11115. So, I suggest that I prepare a new patch that is not based on #11115.



---

archive/issue_comments_085215.json:
```json
{
    "body": "I rebased the patch on top of sage-4.7.alpha5. It is independent of #11115. Now I need to rebuild and do some tests, but I am confident enough to ask for a review, again...\n\nDepends on #9944",
    "created_at": "2011-04-13T13:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85215",
    "user": "SimonKing"
}
```

I rebased the patch on top of sage-4.7.alpha5. It is independent of #11115. Now I need to rebuild and do some tests, but I am confident enough to ask for a review, again...

Depends on #9944



---

archive/issue_comments_085216.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-13T13:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85216",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085217.json:
```json
{
    "body": "For the record: Both `sage -startuptime` and the Monsky-Washnitzer example do not report a significant slow-down. It is not a speed-up either, but I think that speeding things up shall be the job of #11115, eventually.",
    "created_at": "2011-04-13T13:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85217",
    "user": "SimonKing"
}
```

For the record: Both `sage -startuptime` and the Monsky-Washnitzer example do not report a significant slow-down. It is not a speed-up either, but I think that speeding things up shall be the job of #11115, eventually.



---

archive/issue_comments_085218.json:
```json
{
    "body": "I noticed that the patched contained one change that would fit better into a patch for #11115 (adding `@`cached-method to the modulus method of polynomial rings). I think that this change is reasonable, but should better be put into #11115.",
    "created_at": "2011-04-15T13:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85218",
    "user": "SimonKing"
}
```

I noticed that the patched contained one change that would fit better into a patch for #11115 (adding `@`cached-method to the modulus method of polynomial rings). I think that this change is reasonable, but should better be put into #11115.



---

archive/issue_comments_085219.json:
```json
{
    "body": "To be on the safe side, I repeated timings with the latest patch from here, applied only on top of #9944:\n\n```\n$ ./sage -startuptime\n...\n## Slowest (including children)\n1.396 sage.all (None)\n0.398 sage.misc.all (sage.all)\n0.285 functional (sage.misc.all)\n0.282 sage.schemes.all (sage.all)\n0.271 sage.rings.complex_double (functional)\n...\n```\n\nand\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: P = R.poly_ring()\nsage: x, T = R.gens()\nsage: timeit('x*T')\n625 loops, best of 3: 869 \u00b5s per loop\n```\n\n\nWithout all these patches, I get\n\n```\n$ ./sage -startuptime\n...\n## Slowest (including children)\n1.282 sage.all (None)\n0.284 sage.schemes.all (sage.all)\n0.241 sage.misc.all (sage.all)\n0.184 twisted.persisted.styles (sage.all)\n0.165 elliptic_curves.all (sage.schemes.all)\n...\n```\n\nand\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: P = R.poly_ring()\nsage: x, T = R.gens()\nsage: timeit('x*T')\n625 loops, best of 3: 501 \u00b5s per loop\n```\n\n\nI think the timing of the startup time is within the error margin. But there is a slow-down of the Monsky-Washnitzer code. I have shown how to solve the latter problem, based on #11115.\n\nI leave the decision to the reviewer whether or not #11115, together with a patch that puts a cached_method decorator in front of the modulus method, should be a dependency for this ticket.",
    "created_at": "2011-04-15T14:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85219",
    "user": "SimonKing"
}
```

To be on the safe side, I repeated timings with the latest patch from here, applied only on top of #9944:

```
$ ./sage -startuptime
...
## Slowest (including children)
1.396 sage.all (None)
0.398 sage.misc.all (sage.all)
0.285 functional (sage.misc.all)
0.282 sage.schemes.all (sage.all)
0.271 sage.rings.complex_double (functional)
...
```

and

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: P = R.poly_ring()
sage: x, T = R.gens()
sage: timeit('x*T')
625 loops, best of 3: 869 µs per loop
```


Without all these patches, I get

```
$ ./sage -startuptime
...
## Slowest (including children)
1.282 sage.all (None)
0.284 sage.schemes.all (sage.all)
0.241 sage.misc.all (sage.all)
0.184 twisted.persisted.styles (sage.all)
0.165 elliptic_curves.all (sage.schemes.all)
...
```

and

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: P = R.poly_ring()
sage: x, T = R.gens()
sage: timeit('x*T')
625 loops, best of 3: 501 µs per loop
```


I think the timing of the startup time is within the error margin. But there is a slow-down of the Monsky-Washnitzer code. I have shown how to solve the latter problem, based on #11115.

I leave the decision to the reviewer whether or not #11115, together with a patch that puts a cached_method decorator in front of the modulus method, should be a dependency for this ticket.



---

archive/issue_comments_085220.json:
```json
{
    "body": "Replying to [comment:40 SimonKing]:\n> I leave the decision to the reviewer whether or not #11115, together with a patch that puts a cached_method decorator in front of the modulus method, should be a dependency for this ticket.\n\nApparently there is no reviewer :(\n\nAnyway. I modified the patch so that now `modulus()` becomes a cached method. This provides a speed-up even without #11115. And once #11115 is merged as well, the speed-up will increase.\n\nWithout #11115, but with the patches from #9944 and from here:\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: P = R.poly_ring()\nsage: x, T = R.gens()\n# Without patches, the following was 495 \u00c2\u00b5s per loop\nsage: timeit('x*T')\n625 loops, best of 3: 472 \u00b5s per loop\nsage: %prun L=[x*T for _ in xrange(1000)]\n         392002 function calls in 0.590 CPU seconds\n\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n     1000    0.385    0.000    0.560    0.001 monsky_washnitzer.py:553(_mul_)\n   384000    0.177    0.000    0.177    0.000 cachefunc.py:505(__call__)\n        1    0.019    0.019    0.590    0.590 <string>:1(<module>)\n     2000    0.006    0.000    0.006    0.000 integer_mod_ring.py:726(_repr_)\n     1000    0.003    0.000    0.004    0.000 monsky_washnitzer.py:325(__init__)\n     2000    0.001    0.000    0.001    0.000 {isinstance}\n     2000    0.000    0.000    0.000    0.000 {method 'parent' of 'sage.structure.element.Element' objects}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n```\n\n\nThat's better than with an unpatched Sage and thus good enough.",
    "created_at": "2011-04-19T08:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85220",
    "user": "SimonKing"
}
```

Replying to [comment:40 SimonKing]:
> I leave the decision to the reviewer whether or not #11115, together with a patch that puts a cached_method decorator in front of the modulus method, should be a dependency for this ticket.

Apparently there is no reviewer :(

Anyway. I modified the patch so that now `modulus()` becomes a cached method. This provides a speed-up even without #11115. And once #11115 is merged as well, the speed-up will increase.

Without #11115, but with the patches from #9944 and from here:

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: P = R.poly_ring()
sage: x, T = R.gens()
# Without patches, the following was 495 Âµs per loop
sage: timeit('x*T')
625 loops, best of 3: 472 µs per loop
sage: %prun L=[x*T for _ in xrange(1000)]
         392002 function calls in 0.590 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.385    0.000    0.560    0.001 monsky_washnitzer.py:553(_mul_)
   384000    0.177    0.000    0.177    0.000 cachefunc.py:505(__call__)
        1    0.019    0.019    0.590    0.590 <string>:1(<module>)
     2000    0.006    0.000    0.006    0.000 integer_mod_ring.py:726(_repr_)
     1000    0.003    0.000    0.004    0.000 monsky_washnitzer.py:325(__init__)
     2000    0.001    0.000    0.001    0.000 {isinstance}
     2000    0.000    0.000    0.000    0.000 {method 'parent' of 'sage.structure.element.Element' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```


That's better than with an unpatched Sage and thus good enough.



---

archive/issue_comments_085221.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-20T08:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85221",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085222.json:
```json
{
    "body": "While working on #11115, I found that there are still some rings that do neither use the new coercion framework nor properly initialize their category. That includes quotient rings and free algebras. The problem is that, even though they inherit from sage.rings.ring.Ring, they do not call the appropriate `__init__`.\n\nI was wondering whether that should be done here or on #11115, but after all I think it should better be here.",
    "created_at": "2011-04-20T08:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85222",
    "user": "SimonKing"
}
```

While working on #11115, I found that there are still some rings that do neither use the new coercion framework nor properly initialize their category. That includes quotient rings and free algebras. The problem is that, even though they inherit from sage.rings.ring.Ring, they do not call the appropriate `__init__`.

I was wondering whether that should be done here or on #11115, but after all I think it should better be here.



---

archive/issue_comments_085223.json:
```json
{
    "body": "Replying to [comment:42 SimonKing]:\n> While working on #11115, I found that there are still some rings that do neither use the new coercion framework nor properly initialize their category. That includes quotient rings and free algebras. The problem is that, even though they inherit from sage.rings.ring.Ring, they do not call the appropriate `__init__`.\n> \n> I was wondering whether that should be done here or on #11115, but after all I think it should better be here.\n\nBoth routes look fine. Please pick up whichever is more practical to you.",
    "created_at": "2011-04-20T08:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85223",
    "user": "nthiery"
}
```

Replying to [comment:42 SimonKing]:
> While working on #11115, I found that there are still some rings that do neither use the new coercion framework nor properly initialize their category. That includes quotient rings and free algebras. The problem is that, even though they inherit from sage.rings.ring.Ring, they do not call the appropriate `__init__`.
> 
> I was wondering whether that should be done here or on #11115, but after all I think it should better be here.

Both routes look fine. Please pick up whichever is more practical to you.



---

archive/issue_comments_085224.json:
```json
{
    "body": "It is rather frustrating. I try to fit `BooleanPolynomialRing` into the new coercion model, defining _element_constructor_ and _coerce_map_from_ -- and now, suddenly Sage is complaining that it is still using the old coercion model! I found that the reason for the complaint is the existence of _element_constructor. But that should be the *new* model, shouldn't it??\n\nTime to call it a day...",
    "created_at": "2011-04-20T16:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85224",
    "user": "SimonKing"
}
```

It is rather frustrating. I try to fit `BooleanPolynomialRing` into the new coercion model, defining _element_constructor_ and _coerce_map_from_ -- and now, suddenly Sage is complaining that it is still using the old coercion model! I found that the reason for the complaint is the existence of _element_constructor. But that should be the *new* model, shouldn't it??

Time to call it a day...



---

archive/issue_comments_085225.json:
```json
{
    "body": "It turned out that the notion of \"coercion\" was not used in the proper way, in sage.rings.polynomial.pbori. Namely, `_coerce_` was used to *convert* a boolean set into a boolean polynomial. That can not be called a coercion, since boolean sets have no parent (at least no parent that would allow for a coercion map). The old coercion model did not mind, but the new coercion model complains about those things.\n\nMoreover, there was a custom call method that first tried to call `self._coerce_(x)`. When one renames that call method to `_element_contructor_` (for the new coercion model) then one obtains an infinite recursion, because you need to evaluate the element constructor for constructing the `_coerce_` method.\n\nIn other words, one needs to replace `P._coerce_(...)` and `P.coerce(...)` by either `P(...)` or by a direct call to `P._coerce_c_impl(...)`. This is what I'm trying now.",
    "created_at": "2011-04-21T11:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85225",
    "user": "SimonKing"
}
```

It turned out that the notion of "coercion" was not used in the proper way, in sage.rings.polynomial.pbori. Namely, `_coerce_` was used to *convert* a boolean set into a boolean polynomial. That can not be called a coercion, since boolean sets have no parent (at least no parent that would allow for a coercion map). The old coercion model did not mind, but the new coercion model complains about those things.

Moreover, there was a custom call method that first tried to call `self._coerce_(x)`. When one renames that call method to `_element_contructor_` (for the new coercion model) then one obtains an infinite recursion, because you need to evaluate the element constructor for constructing the `_coerce_` method.

In other words, one needs to replace `P._coerce_(...)` and `P.coerce(...)` by either `P(...)` or by a direct call to `P._coerce_c_impl(...)`. This is what I'm trying now.



---

archive/issue_comments_085226.json:
```json
{
    "body": "Good news: I managed to implement pickling for boolean monomial monoids and boolean monomials, to fit everything into the new coercion model and to make `TestSuite(...).run()` work on boolean polynomial rings and boolean monomial monoids.\n\nI am not updating my patch yet, though, since there are further issues to fix.",
    "created_at": "2011-04-21T19:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85226",
    "user": "SimonKing"
}
```

Good news: I managed to implement pickling for boolean monomial monoids and boolean monomials, to fit everything into the new coercion model and to make `TestSuite(...).run()` work on boolean polynomial rings and boolean monomial monoids.

I am not updating my patch yet, though, since there are further issues to fix.



---

archive/issue_comments_085227.json:
```json
{
    "body": "I just found a problem with the category of quotients:\n\n\n```\nsage: EuclideanDomains().Quotients()\nJoin of Category of euclidean domains and Category of subquotients of monoids and Category of quotients of semigroups\n```\n\n\nThat's plain wrong. Think of the ring of integers mod 16, which is certainly not a euclidean domain (not even integral domain), but should belong to the category of quotients of euclidean domains.\n\nI'll try to analyse the problem. I noticed it when I tried to provide `Integers(n)` with an appropriate category.",
    "created_at": "2011-04-21T21:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85227",
    "user": "SimonKing"
}
```

I just found a problem with the category of quotients:


```
sage: EuclideanDomains().Quotients()
Join of Category of euclidean domains and Category of subquotients of monoids and Category of quotients of semigroups
```


That's plain wrong. Think of the ring of integers mod 16, which is certainly not a euclidean domain (not even integral domain), but should belong to the category of quotients of euclidean domains.

I'll try to analyse the problem. I noticed it when I tried to provide `Integers(n)` with an appropriate category.



---

archive/issue_comments_085228.json:
```json
{
    "body": "Wow!! I found that the wrong result is actually doctested in sage.categores.quotients!\n\nThat has to change.",
    "created_at": "2011-04-21T21:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85228",
    "user": "SimonKing"
}
```

Wow!! I found that the wrong result is actually doctested in sage.categores.quotients!

That has to change.



---

archive/issue_comments_085229.json:
```json
{
    "body": "From the doc:\n\n```\n    Given a concrete category ``As()`` (i.e. a subcategory of\n    ``Sets()``), ``As().Quotients()`` returns the category of objects\n    of ``As()`` endowed with a distinguished description as\n    quotient of some other object of ``As()``.\n```\n\n\nIntMod16 is *not* a quotient of ZZ by a morphism of *euclidean domains*. So it is not in EuclideanDomains().Quotients().",
    "created_at": "2011-04-21T21:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85229",
    "user": "nthiery"
}
```

From the doc:

```
    Given a concrete category ``As()`` (i.e. a subcategory of
    ``Sets()``), ``As().Quotients()`` returns the category of objects
    of ``As()`` endowed with a distinguished description as
    quotient of some other object of ``As()``.
```


IntMod16 is *not* a quotient of ZZ by a morphism of *euclidean domains*. So it is not in EuclideanDomains().Quotients().



---

archive/issue_comments_085230.json:
```json
{
    "body": "Replying to [comment:49 nthiery]:\n> From the doc:\n> {{{\n>     Given a concrete category ``As()`` (i.e. a subcategory of\n>     ``Sets()``), ``As().Quotients()`` returns the category of objects\n>     of ``As()`` endowed with a distinguished description as\n>     quotient of some other object of ``As()``.\n> }}}\n> \n> IntMod16 is *not* a quotient of ZZ by a morphism of *euclidean domains*. So it is not in EuclideanDomains().Quotients().\n\nI see. So, I can not provide `QuotientRing` with the category of quotients of the category of the ambient ring.",
    "created_at": "2011-04-21T22:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85230",
    "user": "SimonKing"
}
```

Replying to [comment:49 nthiery]:
> From the doc:
> {{{
>     Given a concrete category ``As()`` (i.e. a subcategory of
>     ``Sets()``), ``As().Quotients()`` returns the category of objects
>     of ``As()`` endowed with a distinguished description as
>     quotient of some other object of ``As()``.
> }}}
> 
> IntMod16 is *not* a quotient of ZZ by a morphism of *euclidean domains*. So it is not in EuclideanDomains().Quotients().

I see. So, I can not provide `QuotientRing` with the category of quotients of the category of the ambient ring.



---

archive/issue_comments_085231.json:
```json
{
    "body": "Replying to [comment:50 SimonKing]:\n> I see. So, I can not provide `QuotientRing` with the category of quotients of the category of the ambient ring.\n\nYup. E.g. the quotient of an algebra A by a vector space I is just a vector space. But if I is an ideal, more can be said. So the logic to determine this piece of mathematical information is non trivial, and often one is better off just specifying it explicitly.",
    "created_at": "2011-04-21T22:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85231",
    "user": "nthiery"
}
```

Replying to [comment:50 SimonKing]:
> I see. So, I can not provide `QuotientRing` with the category of quotients of the category of the ambient ring.

Yup. E.g. the quotient of an algebra A by a vector space I is just a vector space. But if I is an ideal, more can be said. So the logic to determine this piece of mathematical information is non trivial, and often one is better off just specifying it explicitly.



---

archive/issue_comments_085232.json:
```json
{
    "body": "The first patch did not cover all rings - it turned out that many classes derived from sage.rings.ring.Ring do in fact *not* call the `__init__`  method of rings. Hence, in these cases, the category stuff was not present.\n\nThe second patch takes care of some of these cases - I think I shouldn't vouch for completeness, though. Moreover, I implemented the new coercion model for some more classes of rings, such as free algebras, quotient rings, and boolean polynomial rings.\n\nConcerning quotient rings: I hope that the category of this quotient ring is correctly chosen:\n\n```\nsage: P.<x,y> = QQ[]\nsage: Q = P.quo(P*[x^2+y^2])\nsage: Q.category()\nJoin of Category of commutative rings and Category of subquotients of monoids and Category of quotients of semigroups\n```\n\n\nWhat do you think: Should it perhaps better be \"join of Category of commutative algebras over Rational Field and Category of subquotients ...\"? After all, P belongs to the category of commutative algebras over the rational field.\n\nBut apart from that, it seems ready for review now.",
    "created_at": "2011-04-25T07:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85232",
    "user": "SimonKing"
}
```

The first patch did not cover all rings - it turned out that many classes derived from sage.rings.ring.Ring do in fact *not* call the `__init__`  method of rings. Hence, in these cases, the category stuff was not present.

The second patch takes care of some of these cases - I think I shouldn't vouch for completeness, though. Moreover, I implemented the new coercion model for some more classes of rings, such as free algebras, quotient rings, and boolean polynomial rings.

Concerning quotient rings: I hope that the category of this quotient ring is correctly chosen:

```
sage: P.<x,y> = QQ[]
sage: Q = P.quo(P*[x^2+y^2])
sage: Q.category()
Join of Category of commutative rings and Category of subquotients of monoids and Category of quotients of semigroups
```


What do you think: Should it perhaps better be "join of Category of commutative algebras over Rational Field and Category of subquotients ..."? After all, P belongs to the category of commutative algebras over the rational field.

But apart from that, it seems ready for review now.



---

archive/issue_comments_085233.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-25T07:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85233",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085234.json:
```json
{
    "body": "Replying to [comment:52 SimonKing]:\n> The first patch did not cover all rings - it turned out that many classes derived from sage.rings.ring.Ring do in fact *not* call the `__init__`  method of rings. Hence, in these cases, the category stuff was not present.\n> \n> The second patch takes care of some of these cases - I think I shouldn't vouch for completeness, though. Moreover, I implemented the new coercion model for some more classes of rings, such as free algebras, quotient rings, and boolean polynomial rings.\n\nCool!\n\n> Concerning quotient rings: I hope that the category of this quotient ring is correctly chosen:\n> {{{\n> sage: P.<x,y> = QQ[]\n> sage: Q = P.quo(P*[x<sup>2+y</sup>2])\n> sage: Q.category()\n> Join of Category of commutative rings and Category of subquotients of monoids and Category of quotients of semigroups\n> }}}\n> \n> What do you think: Should it perhaps better be \"join of Category of commutative algebras over Rational Field and Category of subquotients ...\"?\n> After all, P belongs to the category of commutative algebras over the rational field.\n\nIf multiplication by elements of QQ are implemented (and I assume they\nare), then yes I definitely would go for commutative algebras.\n\n> But apart from that, it seems ready for review now.\n\nNice! I'll work on that in the coming weeks, but can't promise when\nwith the upcoming Sage days. Please anyone beat me to it!\n\nCheers,\n\t\t\t\t\tNicolas",
    "created_at": "2011-04-25T11:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85234",
    "user": "nthiery"
}
```

Replying to [comment:52 SimonKing]:
> The first patch did not cover all rings - it turned out that many classes derived from sage.rings.ring.Ring do in fact *not* call the `__init__`  method of rings. Hence, in these cases, the category stuff was not present.
> 
> The second patch takes care of some of these cases - I think I shouldn't vouch for completeness, though. Moreover, I implemented the new coercion model for some more classes of rings, such as free algebras, quotient rings, and boolean polynomial rings.

Cool!

> Concerning quotient rings: I hope that the category of this quotient ring is correctly chosen:
> {{{
> sage: P.<x,y> = QQ[]
> sage: Q = P.quo(P*[x<sup>2+y</sup>2])
> sage: Q.category()
> Join of Category of commutative rings and Category of subquotients of monoids and Category of quotients of semigroups
> }}}
> 
> What do you think: Should it perhaps better be "join of Category of commutative algebras over Rational Field and Category of subquotients ..."?
> After all, P belongs to the category of commutative algebras over the rational field.

If multiplication by elements of QQ are implemented (and I assume they
are), then yes I definitely would go for commutative algebras.

> But apart from that, it seems ready for review now.

Nice! I'll work on that in the coming weeks, but can't promise when
with the upcoming Sage days. Please anyone beat me to it!

Cheers,
					Nicolas



---

archive/issue_comments_085235.json:
```json
{
    "body": "I just noticed: \n\nThe patch not only depends on #9944 but is based on sage-4.7.alpha5. I don't know which other patches are responsible for that, but the part of the patch that concerns the polybori code fails to apply with sage-4.6.\n\nReplying to [comment:53 nthiery]:\n> > What do you think: Should it perhaps better be \"join of Category of commutative algebras over Rational Field and Category of subquotients ...\"?\n> > After all, P belongs to the category of commutative algebras over the rational field.\n> \n> If multiplication by elements of QQ are implemented (and I assume they\n> are), then yes I definitely would go for commutative algebras.\n\nI looked at the code, and it seems that at least operation of the base ring exists. But I think one should also implement an `_rmul_` and `_lmul_` for quotient ring elements - it is missing, so far.\n\nBest regards,\nSimon",
    "created_at": "2011-04-25T12:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85235",
    "user": "SimonKing"
}
```

I just noticed: 

The patch not only depends on #9944 but is based on sage-4.7.alpha5. I don't know which other patches are responsible for that, but the part of the patch that concerns the polybori code fails to apply with sage-4.6.

Replying to [comment:53 nthiery]:
> > What do you think: Should it perhaps better be "join of Category of commutative algebras over Rational Field and Category of subquotients ..."?
> > After all, P belongs to the category of commutative algebras over the rational field.
> 
> If multiplication by elements of QQ are implemented (and I assume they
> are), then yes I definitely would go for commutative algebras.

I looked at the code, and it seems that at least operation of the base ring exists. But I think one should also implement an `_rmul_` and `_lmul_` for quotient ring elements - it is missing, so far.

Best regards,
Simon



---

archive/issue_comments_085236.json:
```json
{
    "body": "I think I found what patch caused the polybori incompatibility:\n\nDepends on #9944 #10797",
    "created_at": "2011-04-25T12:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85236",
    "user": "SimonKing"
}
```

I think I found what patch caused the polybori incompatibility:

Depends on #9944 #10797



---

archive/issue_comments_085237.json:
```json
{
    "body": "It seems that there are more dependencies, as there are also some failures when applying the patch to pushout.py. So, let's try again...\n\nDepends on #10797 #8800 #9944 #11019",
    "created_at": "2011-04-25T17:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85237",
    "user": "SimonKing"
}
```

It seems that there are more dependencies, as there are also some failures when applying the patch to pushout.py. So, let's try again...

Depends on #10797 #8800 #9944 #11019



---

archive/issue_comments_085238.json:
```json
{
    "body": "The patchbot keeps complaining. I don't know why. Anyway, applied on top of sage-4.7.alpha5, it works for me.",
    "created_at": "2011-04-27T10:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85238",
    "user": "SimonKing"
}
```

The patchbot keeps complaining. I don't know why. Anyway, applied on top of sage-4.7.alpha5, it works for me.



---

archive/issue_comments_085239.json:
```json
{
    "body": "Apparently the patches need to be rebased: I just tried to apply it on top of my patch queue (including some other relevant tickets), and 8 hunks did not apply for the first of the two patches. Needs work.",
    "created_at": "2011-05-23T14:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85239",
    "user": "SimonKing"
}
```

Apparently the patches need to be rebased: I just tried to apply it on top of my patch queue (including some other relevant tickets), and 8 hunks did not apply for the first of the two patches. Needs work.



---

archive/issue_comments_085240.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-23T14:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85240",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085241.json:
```json
{
    "body": "The patches are updated.\n\nMy patch queue to this ticket, starting with sage-4.7.rc2, is: #11268 (merged), #11139 (merged), #9976 (merged), #9944 (positive review), #11269 (positive review)\n\nHence:\n\nDepends on #11268, #11139, #9976, #9944, #11269\n\nI did not run tests, yet, but will do now.",
    "created_at": "2011-05-23T14:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85241",
    "user": "SimonKing"
}
```

The patches are updated.

My patch queue to this ticket, starting with sage-4.7.rc2, is: #11268 (merged), #11139 (merged), #9976 (merged), #9944 (positive review), #11269 (positive review)

Hence:

Depends on #11268, #11139, #9976, #9944, #11269

I did not run tests, yet, but will do now.



---

archive/issue_comments_085242.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-05-23T14:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85242",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085243.json:
```json
{
    "body": "FWIW, all (short) tests pass for me.",
    "created_at": "2011-05-23T16:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85243",
    "user": "SimonKing"
}
```

FWIW, all (short) tests pass for me.



---

archive/issue_comments_085244.json:
```json
{
    "body": "The dependencies of this patch are stated in the corresponding form field. For the following timings, I additionally have #11298, #11267 and, in particular, #11115.\n\nIn some cases, there is quite an improvement, compared with the timings that are stated in previous comments! Note that the times per loop change, depending on whether one lets timeit run `10^4` loops (as in #9944) or one simply does `timeit` without any specification.\n\nFirst series of timings: I guess most of the speedup is due to #9944\n\n```\nsage: R.<x> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 20.9 \u00b5s per loop\n# unpatched 625 loops, best of 3: 22.5 \u00c2\u00b5s per loop\nsage: R.<x> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 21.3 \u00b5s per loop\n# unpatched 625 loops, best of 3: 24.5 \u00c2\u00b5s per loop\nsage: R.<x> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 19.2 \u00b5s per loop\n# unpatched 625 loops, best of 3: 87.7 \u00c2\u00b5s per loop\nsage: R.<x> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 75.4 \u00b5s per loop\n# unpatched 625 loops, best of 3: 114 \u00c2\u00b5s per loop\nsage: R.<x,y> = ZZ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 19.7 \u00b5s per loop\n# unpatched 625 loops, best of 3: 21.9 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 18.2 \u00b5s per loop\n# unpatched 625 loops, best of 3: 40 \u00c2\u00b5s per loop\nsage: R.<x,y> = GF(3)[]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 15.8 \u00b5s per loop\n# unpatched 625 loops, best of 3: 26.3 \u00c2\u00b5s per loop\nsage: R.<x,y> = QQ['t'][]\nsage: timeit('(2*x-1)^2+5')\n625 loops, best of 3: 162 \u00b5s per loop\n# unpatched 625 loops, best of 3: 239 \u00c2\u00b5s per loop\n```\n\n\nTimings for some \"schemes\" tests.\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\"\n\t [29.5 s]\n```\n\nI have not the faintest idea where that slow-down might come from. Namely, the underlying arithmetic has drastically improved:\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: x, T = R.gens()\nsage: timeit('x*T')\n625 loops, best of 3: 179 \u00b5s per loop\n# unpatched: 625 loops, best of 3: 612 \u00b5s per loop\n```\n\nand\n\n```\nsage: B.<t> = PolynomialRing(Integers(125))\nsage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))\nsage: P = R.poly_ring()\nsage: timeit('P.modulus()',number=10^6)\n1000000 loops, best of 3: 161 ns per loop\n# unpatched: 1000000 loops, best of 3: 647 ns per loop\nsage: x, T = R.gens()\nsage: timeit('x*T')\n625 loops, best of 3: 177 \u00b5s per loop\n# unpatched: 625 loops, best of 3: 495 \u00c2\u00b5s per loop\n```\n\n\nAnd the startup time (which is also relevant for doctests:\n\n```\n1.326 sage.all (None)\n0.324 sage.schemes.all (sage.all)\n0.184 sage.misc.all (sage.all)\n0.160 hyperelliptic_curves.all (sage.schemes.all)\n```\n\n\nI'd appreciate if someone could explain why the doctest time in sage.schemes increased, while the underlying arithmetics became faster.\n\nOverall, I think that the performance is quite good, and of course the main point of this ticket (namely to implement the category framework for rings) was successfully addressed.\n\nReview, anyone?",
    "created_at": "2011-05-24T16:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85244",
    "user": "SimonKing"
}
```

The dependencies of this patch are stated in the corresponding form field. For the following timings, I additionally have #11298, #11267 and, in particular, #11115.

In some cases, there is quite an improvement, compared with the timings that are stated in previous comments! Note that the times per loop change, depending on whether one lets timeit run `10^4` loops (as in #9944) or one simply does `timeit` without any specification.

First series of timings: I guess most of the speedup is due to #9944

```
sage: R.<x> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 20.9 µs per loop
# unpatched 625 loops, best of 3: 22.5 Âµs per loop
sage: R.<x> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 21.3 µs per loop
# unpatched 625 loops, best of 3: 24.5 Âµs per loop
sage: R.<x> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 19.2 µs per loop
# unpatched 625 loops, best of 3: 87.7 Âµs per loop
sage: R.<x> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 75.4 µs per loop
# unpatched 625 loops, best of 3: 114 Âµs per loop
sage: R.<x,y> = ZZ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 19.7 µs per loop
# unpatched 625 loops, best of 3: 21.9 Âµs per loop
sage: R.<x,y> = QQ[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 18.2 µs per loop
# unpatched 625 loops, best of 3: 40 Âµs per loop
sage: R.<x,y> = GF(3)[]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 15.8 µs per loop
# unpatched 625 loops, best of 3: 26.3 Âµs per loop
sage: R.<x,y> = QQ['t'][]
sage: timeit('(2*x-1)^2+5')
625 loops, best of 3: 162 µs per loop
# unpatched 625 loops, best of 3: 239 Âµs per loop
```


Timings for some "schemes" tests.

```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"
	 [29.5 s]
```

I have not the faintest idea where that slow-down might come from. Namely, the underlying arithmetic has drastically improved:

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: x, T = R.gens()
sage: timeit('x*T')
625 loops, best of 3: 179 µs per loop
# unpatched: 625 loops, best of 3: 612 µs per loop
```

and

```
sage: B.<t> = PolynomialRing(Integers(125))
sage: R = monsky_washnitzer.SpecialCubicQuotientRing(t^3 - t + B(1/4))
sage: P = R.poly_ring()
sage: timeit('P.modulus()',number=10^6)
1000000 loops, best of 3: 161 ns per loop
# unpatched: 1000000 loops, best of 3: 647 ns per loop
sage: x, T = R.gens()
sage: timeit('x*T')
625 loops, best of 3: 177 µs per loop
# unpatched: 625 loops, best of 3: 495 Âµs per loop
```


And the startup time (which is also relevant for doctests:

```
1.326 sage.all (None)
0.324 sage.schemes.all (sage.all)
0.184 sage.misc.all (sage.all)
0.160 hyperelliptic_curves.all (sage.schemes.all)
```


I'd appreciate if someone could explain why the doctest time in sage.schemes increased, while the underlying arithmetics became faster.

Overall, I think that the performance is quite good, and of course the main point of this ticket (namely to implement the category framework for rings) was successfully addressed.

Review, anyone?



---

archive/issue_comments_085245.json:
```json
{
    "body": "rebased Simon's patch to 4.7.1.alpha1",
    "created_at": "2011-06-07T21:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85245",
    "user": "burcin"
}
```

rebased Simon's patch to 4.7.1.alpha1



---

archive/issue_comments_085246.json:
```json
{
    "body": "Attachment [trac9138_categories_for_more_rings.rebase4.7.1.a1.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138_categories_for_more_rings.rebase4.7.1.a1.patch) by burcin created at 2011-06-07 21:37:25",
    "created_at": "2011-06-07T21:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85246",
    "user": "burcin"
}
```

Attachment [trac9138_categories_for_more_rings.rebase4.7.1.a1.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138_categories_for_more_rings.rebase4.7.1.a1.patch) by burcin created at 2011-06-07 21:37:25



---

archive/issue_comments_085247.json:
```json
{
    "body": "Thank you, Burcin!\n\nFor the patchbot:\n\nApply trac9138-categories_for_rings.patch, trac9138_categories_for_more_rings.rebase4.7.1.a1.patch",
    "created_at": "2011-06-08T06:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85247",
    "user": "SimonKing"
}
```

Thank you, Burcin!

For the patchbot:

Apply trac9138-categories_for_rings.patch, trac9138_categories_for_more_rings.rebase4.7.1.a1.patch



---

archive/issue_comments_085248.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-02T16:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85248",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085249.json:
```json
{
    "body": "It seems that there is a problem with doctests for the Steenrod algebra. When I apply the patch on top of sage-4.7.1.rc1, I obtain\n\n```\n    sage: SteenrodAlgebra(2)['x'].category()\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[12]>\", line 1, in <module>\n        SteenrodAlgebra(Integer(2))['x'].category()###line 114:\n    sage: SteenrodAlgebra(2)['x'].category()\n      File \"/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/algebras/steenrod/steenrod_algebra.py\", line 1037, in homogeneous_component\n        basis = self._basis_fcn(n)\n      File \"cachefunc.pyx\", line 531, in sage.misc.cachefunc.CachedFunction.__call__ (sage/misc/cachefunc.c:2227)\n      File \"/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/algebras/steenrod/steenrod_algebra_bases.py\", line 368, in steenrod_algebra_basis_\n        if n < 0 or int(n) != n:\n    ValueError: invalid literal for int() with base 10: 'x'\n```\n\n\nSo, back to the drawing board...",
    "created_at": "2011-08-02T16:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85249",
    "user": "SimonKing"
}
```

It seems that there is a problem with doctests for the Steenrod algebra. When I apply the patch on top of sage-4.7.1.rc1, I obtain

```
    sage: SteenrodAlgebra(2)['x'].category()
Exception raised:
    Traceback (most recent call last):
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[12]>", line 1, in <module>
        SteenrodAlgebra(Integer(2))['x'].category()###line 114:
    sage: SteenrodAlgebra(2)['x'].category()
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/algebras/steenrod/steenrod_algebra.py", line 1037, in homogeneous_component
        basis = self._basis_fcn(n)
      File "cachefunc.pyx", line 531, in sage.misc.cachefunc.CachedFunction.__call__ (sage/misc/cachefunc.c:2227)
      File "/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python/site-packages/sage/algebras/steenrod/steenrod_algebra_bases.py", line 368, in steenrod_algebra_basis_
        if n < 0 or int(n) != n:
    ValueError: invalid literal for int() with base 10: 'x'
```


So, back to the drawing board...



---

archive/issue_comments_085250.json:
```json
{
    "body": "I wonder if the Steenrod algebra problem is due to #10052, which was merged in 4.7.1.alpha3.",
    "created_at": "2011-08-02T17:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85250",
    "user": "jhpalmieri"
}
```

I wonder if the Steenrod algebra problem is due to #10052, which was merged in 4.7.1.alpha3.



---

archive/issue_comments_085251.json:
```json
{
    "body": "Replying to [comment:66 jhpalmieri]:\n> I wonder if the Steenrod algebra problem is due to #10052, which was merged in 4.7.1.alpha3.\n\nI wouldn't say \"due to\", since the critical tests (perhaps introduced by #10052) pass with sage-4.7.1.rc1. In fact, I already found out that [attachment:trac9138-categories_for_rings.patch] is to blame. But I don't know yet what went wrong.",
    "created_at": "2011-08-02T17:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85251",
    "user": "SimonKing"
}
```

Replying to [comment:66 jhpalmieri]:
> I wonder if the Steenrod algebra problem is due to #10052, which was merged in 4.7.1.alpha3.

I wouldn't say "due to", since the critical tests (perhaps introduced by #10052) pass with sage-4.7.1.rc1. In fact, I already found out that [attachment:trac9138-categories_for_rings.patch] is to blame. But I don't know yet what went wrong.



---

archive/issue_comments_085252.json:
```json
{
    "body": "Replying to [comment:67 SimonKing]:\n> I wouldn't say \"due to\"\n\nI guess I meant due to the interactions between the patch here and the changes in #10052.",
    "created_at": "2011-08-02T17:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85252",
    "user": "jhpalmieri"
}
```

Replying to [comment:67 SimonKing]:
> I wouldn't say "due to"

I guess I meant due to the interactions between the patch here and the changes in #10052.



---

archive/issue_comments_085253.json:
```json
{
    "body": "In my first patch, I had introduced the test\n\n```\nsage: SteenrodAlgebra(2)['x'].category() \nCategory of algebras over mod 2 Steenrod algebra\n```\n\n\nIt was supposed to be a test for a polynomial ring over a non-commutative ring. But by your patch from #10052, the `__getitem__` method of a Steenrod algebra got a different meaning.\n\nI think the easiest solution (and probably the best solution as well would be to replace that test by a polynomial ring over a different non-commutative algebra, perhaps a matrix algebra.",
    "created_at": "2011-08-02T20:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85253",
    "user": "SimonKing"
}
```

In my first patch, I had introduced the test

```
sage: SteenrodAlgebra(2)['x'].category() 
Category of algebras over mod 2 Steenrod algebra
```


It was supposed to be a test for a polynomial ring over a non-commutative ring. But by your patch from #10052, the `__getitem__` method of a Steenrod algebra got a different meaning.

I think the easiest solution (and probably the best solution as well would be to replace that test by a polynomial ring over a different non-commutative algebra, perhaps a matrix algebra.



---

archive/issue_comments_085254.json:
```json
{
    "body": "Replying to [comment:69 SimonKing]:\n> I think the easiest solution (and probably the best solution as well would be to replace that test by a polynomial ring over a different non-commutative algebra, perhaps a matrix algebra.\n\nHel\u00e0s.\n\nMatrix spaces have their custom `__getitem__` as well. But it would be possible to construct the polynomial ring by using the polynomial ring constructor:\n\n```\nsage: PolynomialRing(MatrixSpace(QQ,2),'x').category()\nCategory of algebras over Full MatrixSpace of 2 by 2 dense matrices over Rational Field\nsage: PolynomialRing(SteenrodAlgebra(2),'x').category()\nCategory of algebras over mod 2 Steenrod algebra, milnor basis\n```\n\n\nThe other problem is in sage/algebras/steenrod/steenrod_algebra.py.: With the patch from here,\n\n```\n            sage: A1 = SteenrodAlgebra(profile=[2,1])\n            sage: A1(3)  # map integer into A1\n```\n\nreturns 3 and not 1!\n\nThat behaviour boils down to\n\n```\nsage: A1._from_dict({():3})\n3\n```\n\nHere, one should have\n\n```\nsage: A1._from_dict({():3},coerce=True)\n1\n```\n\n\nI don't know, though, how my patch has changed the question whether there is a conversion or not: The word `coerce` occurs precisely twice in my first patch, but that is certainly unrelated with \"coerce=True\" versus \"coerce=False\". Strange.",
    "created_at": "2011-08-02T20:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85254",
    "user": "SimonKing"
}
```

Replying to [comment:69 SimonKing]:
> I think the easiest solution (and probably the best solution as well would be to replace that test by a polynomial ring over a different non-commutative algebra, perhaps a matrix algebra.

Helàs.

Matrix spaces have their custom `__getitem__` as well. But it would be possible to construct the polynomial ring by using the polynomial ring constructor:

```
sage: PolynomialRing(MatrixSpace(QQ,2),'x').category()
Category of algebras over Full MatrixSpace of 2 by 2 dense matrices over Rational Field
sage: PolynomialRing(SteenrodAlgebra(2),'x').category()
Category of algebras over mod 2 Steenrod algebra, milnor basis
```


The other problem is in sage/algebras/steenrod/steenrod_algebra.py.: With the patch from here,

```
            sage: A1 = SteenrodAlgebra(profile=[2,1])
            sage: A1(3)  # map integer into A1
```

returns 3 and not 1!

That behaviour boils down to

```
sage: A1._from_dict({():3})
3
```

Here, one should have

```
sage: A1._from_dict({():3},coerce=True)
1
```


I don't know, though, how my patch has changed the question whether there is a conversion or not: The word `coerce` occurs precisely twice in my first patch, but that is certainly unrelated with "coerce=True" versus "coerce=False". Strange.



---

archive/issue_comments_085255.json:
```json
{
    "body": "It seems that the problem is deeper. With the first patch, I obtain\n\n```\nsage: A1 = SteenrodAlgebra(profile=[2,1])\nsage: A1.coerce_map_from(ZZ)\nConversion map:\n  From: Integer Ring\n  To:   sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]\n```\n\n\nWithout the patch, I obtain\n\n```\nsage: A1 = SteenrodAlgebra(profile=[2,1])\nsage: A1.coerce_map_from(ZZ)\nComposite map:\n  From: Integer Ring\n  To:   sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]\n  Defn:   Natural morphism:\n          From: Integer Ring\n          To:   Finite Field of size 2\n        then\n          Generic morphism:\n          From: Finite Field of size 2\n          To:   sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]\n```\n\n\nBy consequence, when doing `A1(3)` with my patch, a direct conversion is attempted from `ZZ` to `A1`, but the auxiliary methods involved in the conversion assume that the argument 3 has already been converted into the base ring, `GF(2)`.\n\nPerhaps a \"register_coercion\" during initialisation could help.",
    "created_at": "2011-08-03T08:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85255",
    "user": "SimonKing"
}
```

It seems that the problem is deeper. With the first patch, I obtain

```
sage: A1 = SteenrodAlgebra(profile=[2,1])
sage: A1.coerce_map_from(ZZ)
Conversion map:
  From: Integer Ring
  To:   sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]
```


Without the patch, I obtain

```
sage: A1 = SteenrodAlgebra(profile=[2,1])
sage: A1.coerce_map_from(ZZ)
Composite map:
  From: Integer Ring
  To:   sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]
  Defn:   Natural morphism:
          From: Integer Ring
          To:   Finite Field of size 2
        then
          Generic morphism:
          From: Finite Field of size 2
          To:   sub-Hopf algebra of mod 2 Steenrod algebra, milnor basis, profile function [2, 1]
```


By consequence, when doing `A1(3)` with my patch, a direct conversion is attempted from `ZZ` to `A1`, but the auxiliary methods involved in the conversion assume that the argument 3 has already been converted into the base ring, `GF(2)`.

Perhaps a "register_coercion" during initialisation could help.



---

archive/issue_comments_085256.json:
```json
{
    "body": "Replying to [comment:71 SimonKing]:\n> Perhaps a \"register_coercion\" during initialisation could help.\n\nActually, that registration should take place in the `__init_extra__` method that is defined in `sage.categories.algebras`. Without my patch, the rather generic coercion from the base ring is registered no matter what, which means that it could result in a very slow coerce map from the base ring.\n\nTherefore, my patch modifies `__init_extra__` so that the generic coercion is only registered if no \"better\" coercion has been registered before. It could be that that is a problem for Steenrod algebras.",
    "created_at": "2011-08-03T08:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85256",
    "user": "SimonKing"
}
```

Replying to [comment:71 SimonKing]:
> Perhaps a "register_coercion" during initialisation could help.

Actually, that registration should take place in the `__init_extra__` method that is defined in `sage.categories.algebras`. Without my patch, the rather generic coercion from the base ring is registered no matter what, which means that it could result in a very slow coerce map from the base ring.

Therefore, my patch modifies `__init_extra__` so that the generic coercion is only registered if no "better" coercion has been registered before. It could be that that is a problem for Steenrod algebras.



---

archive/issue_comments_085257.json:
```json
{
    "body": "By inserting print statements into my new init_extra method, I found out that when it is called, the \"one\" of the Steenrod algebra is not available, yet. Therefore, the generic method (\"multiply the given element of the base ring with the multiplicative unit of the algebra\") is not available at that time.\n\nWithout my patch, a different method is used for coercion, namely \n\n```\nSetMorphism(function = self.from_base_ring, parent = Hom(self.base_ring(), self, Rings()))\n```\n\n\nThe reason for changing it was the fact that normally  `self.one()._lmul_(r)` is a pretty fast way to convert a base ring element r into self. But I guess that the old `from_base_ring` should be used if the unit is not available during initialisation.",
    "created_at": "2011-08-03T08:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85257",
    "user": "SimonKing"
}
```

By inserting print statements into my new init_extra method, I found out that when it is called, the "one" of the Steenrod algebra is not available, yet. Therefore, the generic method ("multiply the given element of the base ring with the multiplicative unit of the algebra") is not available at that time.

Without my patch, a different method is used for coercion, namely 

```
SetMorphism(function = self.from_base_ring, parent = Hom(self.base_ring(), self, Rings()))
```


The reason for changing it was the fact that normally  `self.one()._lmul_(r)` is a pretty fast way to convert a base ring element r into self. But I guess that the old `from_base_ring` should be used if the unit is not available during initialisation.



---

archive/issue_comments_085258.json:
```json
{
    "body": "That said: The generic from_base_ring does exactly the same as my new approach -- but it constructs the unit again and again and again. Therefore, if the unit is available during initialisation, then my approach is faster.",
    "created_at": "2011-08-03T08:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85258",
    "user": "SimonKing"
}
```

That said: The generic from_base_ring does exactly the same as my new approach -- but it constructs the unit again and again and again. Therefore, if the unit is available during initialisation, then my approach is faster.



---

archive/issue_comments_085259.json:
```json
{
    "body": "I am now fighting against some doc test failures, that are apparently due to the fact that many tests in `sage.rings.polynomial.multi_polynomial_ring` do not use the cache of polynomial rings, in order to demonstrate features of ring classes that would otherwise hardly be used.\n\nProblem: If there is a ring in the cache, together with a coerce map from its base ring, then the coerce map is cached as well. Later, if one constructs an isomorphic ring that is *not* in the cache of rings, then the ring will evaluate equal to the previously constructed ring, and thus looking up the coerce map yields a map with the wrong codomain.\n\nDifficult.",
    "created_at": "2011-08-03T09:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85259",
    "user": "SimonKing"
}
```

I am now fighting against some doc test failures, that are apparently due to the fact that many tests in `sage.rings.polynomial.multi_polynomial_ring` do not use the cache of polynomial rings, in order to demonstrate features of ring classes that would otherwise hardly be used.

Problem: If there is a ring in the cache, together with a coerce map from its base ring, then the coerce map is cached as well. Later, if one constructs an isomorphic ring that is *not* in the cache of rings, then the ring will evaluate equal to the previously constructed ring, and thus looking up the coerce map yields a map with the wrong codomain.

Difficult.



---

archive/issue_comments_085260.json:
```json
{
    "body": "The problem was that some doc tests in sage/rings violate the unique parent assumption on purpose. But homsets will try to be unique even if domain and codomain are not unique. That's bad.\n\nTherefore, I made the following change for my first patch: If `Hom(X,Y,category)` is able to find a hom set H for the given data in cache, then it is first tested that `H.domain() is X` and `H.codomain() is Y`. If it isn't, then a new hom set is constructed, and put into the cache.\n\nHence, we have (as a new doctest):\n\n```\n    By trac ticket #9138, we abandon the uniqueness of hom sets, if the domain or\n    codomain break uniqueness::\n\n        sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain\n        sage: P.<x,y,z>=MPolynomialRing_polydict_domain(QQ, 3, order='degrevlex')\n        sage: Q.<x,y,z>=MPolynomialRing_polydict_domain(QQ, 3, order='degrevlex')\n        sage: P == Q\n        True\n        sage: P is Q\n        False\n\n    Hence, P and Q are not unique parents. By consequence, the following homsets\n    aren't either::\n\n        sage: H1 = Hom(QQ,P)\n        sage: H2 = Hom(QQ,Q)\n        sage: H1 == H2\n        True\n        sage: H1 is H2\n        False\n\n    It is always the most recently constructed hom set that remains in the cache::\n\n        sage: H2 is Hom(QQ,Q)\n        True\n```\n\n\nThe second patch still applies on top of the first. I did the doc tests in sage/rings and sage/categories with the first patch, but full doc tests should be run with both patches, of course.\n\nApply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.rebase4.7.1.a1.patch",
    "created_at": "2011-08-03T10:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85260",
    "user": "SimonKing"
}
```

The problem was that some doc tests in sage/rings violate the unique parent assumption on purpose. But homsets will try to be unique even if domain and codomain are not unique. That's bad.

Therefore, I made the following change for my first patch: If `Hom(X,Y,category)` is able to find a hom set H for the given data in cache, then it is first tested that `H.domain() is X` and `H.codomain() is Y`. If it isn't, then a new hom set is constructed, and put into the cache.

Hence, we have (as a new doctest):

```
    By trac ticket #9138, we abandon the uniqueness of hom sets, if the domain or
    codomain break uniqueness::

        sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
        sage: P.<x,y,z>=MPolynomialRing_polydict_domain(QQ, 3, order='degrevlex')
        sage: Q.<x,y,z>=MPolynomialRing_polydict_domain(QQ, 3, order='degrevlex')
        sage: P == Q
        True
        sage: P is Q
        False

    Hence, P and Q are not unique parents. By consequence, the following homsets
    aren't either::

        sage: H1 = Hom(QQ,P)
        sage: H2 = Hom(QQ,Q)
        sage: H1 == H2
        True
        sage: H1 is H2
        False

    It is always the most recently constructed hom set that remains in the cache::

        sage: H2 is Hom(QQ,Q)
        True
```


The second patch still applies on top of the first. I did the doc tests in sage/rings and sage/categories with the first patch, but full doc tests should be run with both patches, of course.

Apply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.rebase4.7.1.a1.patch



---

archive/issue_comments_085261.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-03T10:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85261",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085262.json:
```json
{
    "body": "Too bad. There are numerous errors for the tests in sage/doc.",
    "created_at": "2011-08-03T10:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85262",
    "user": "SimonKing"
}
```

Too bad. There are numerous errors for the tests in sage/doc.



---

archive/issue_comments_085263.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-03T10:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85263",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085264.json:
```json
{
    "body": "Replying to [comment:77 SimonKing]:\n> Too bad. There are numerous errors for the tests in sage/doc.\n\nTo be precise: The errors seem to come from elliptic curves. Not for the first time...",
    "created_at": "2011-08-03T10:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85264",
    "user": "SimonKing"
}
```

Replying to [comment:77 SimonKing]:
> Too bad. There are numerous errors for the tests in sage/doc.

To be precise: The errors seem to come from elliptic curves. Not for the first time...



---

archive/issue_comments_085265.json:
```json
{
    "body": "For example, I get\n\n```\nsage: L = EllipticCurve('11a').padic_lseries(5)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/king/<ipython console> in <module>()\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padics.pyc in padic_lseries(self, p, normalize, use_eclib)\n    157     if self.ap(p) % p != 0:\n    158         Lp = plseries.pAdicLseriesOrdinary(self, p,\n--> 159                               normalize = normalize, use_eclib=use_eclib)\n    160     else:\n    161         Lp = plseries.pAdicLseriesSupersingular(self, p, \n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in __init__(self, E, p, use_eclib, normalize)\n    197             print \"Warning : Curve outside Cremona's table. Computations of modular symbol space might take very long !\"\n    198             \n--> 199         self._modular_symbol = E.modular_symbol(sign=+1, use_eclib = use_eclib, normalize=normalize)\n    200 \n    201     def __add_negative_space(self):\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in modular_symbol(self, sign, use_eclib, normalize)\n   1241             M = ell_modular_symbols.ModularSymbolECLIB(self, sign, normalize=normalize)\n   1242         else :\n-> 1243             M = ell_modular_symbols.ModularSymbolSage(self, sign, normalize=normalize)\n   1244         self.__modular_symbol[typ] = M\n   1245         return M\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_modular_symbols.pyc in __init__(self, E, sign, normalize)\n    621         self._use_eclib = False\n    622         self._normalize = normalize\n--> 623         self._modsym = E.modular_symbol_space(sign=self._sign)\n    624         self._base_ring = self._modsym.base_ring()\n    625         self._ambient_modsym = self._modsym.ambient_module()\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in modular_symbol_space(self, sign, base_ring, bound)\n   1111         except KeyError:\n   1112             pass\n-> 1113         M = ell_modular_symbols.modular_symbol_space(self, sign, base_ring, bound=bound)\n   1114         self.__modular_symbol_space[typ] = M\n   1115         return M\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_modular_symbols.pyc in modular_symbol_space(E, sign, base_ring, bound)\n    110         t = V.T(p)\n    111         ap = E.ap(p)\n--> 112         V = (t - ap).kernel()\n    113         p = next_prime(p)\n    114             \n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:12234)()\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6463)()\n\n/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7862)()\n\nRuntimeError: BUG in map, returned None -2 <type 'sage.categories.map.FormalCompositeMap'> Composite map:\n  From: Integer Ring\n  To:   Full Hecke algebra acting on Modular Symbols space of dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field\n  Defn:   Natural morphism:\n          From: Integer Ring\n          To:   Rational Field\n        then\n          Generic morphism:\n          From: Rational Field\n          To:   Full Hecke algebra acting on Modular Symbols space of dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field\n```\n\nwith the latest patches.",
    "created_at": "2011-08-03T11:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85265",
    "user": "SimonKing"
}
```

For example, I get

```
sage: L = EllipticCurve('11a').padic_lseries(5)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/king/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padics.pyc in padic_lseries(self, p, normalize, use_eclib)
    157     if self.ap(p) % p != 0:
    158         Lp = plseries.pAdicLseriesOrdinary(self, p,
--> 159                               normalize = normalize, use_eclib=use_eclib)
    160     else:
    161         Lp = plseries.pAdicLseriesSupersingular(self, p, 

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in __init__(self, E, p, use_eclib, normalize)
    197             print "Warning : Curve outside Cremona's table. Computations of modular symbol space might take very long !"
    198             
--> 199         self._modular_symbol = E.modular_symbol(sign=+1, use_eclib = use_eclib, normalize=normalize)
    200 
    201     def __add_negative_space(self):

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in modular_symbol(self, sign, use_eclib, normalize)
   1241             M = ell_modular_symbols.ModularSymbolECLIB(self, sign, normalize=normalize)
   1242         else :
-> 1243             M = ell_modular_symbols.ModularSymbolSage(self, sign, normalize=normalize)
   1244         self.__modular_symbol[typ] = M
   1245         return M

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_modular_symbols.pyc in __init__(self, E, sign, normalize)
    621         self._use_eclib = False
    622         self._normalize = normalize
--> 623         self._modsym = E.modular_symbol_space(sign=self._sign)
    624         self._base_ring = self._modsym.base_ring()
    625         self._ambient_modsym = self._modsym.ambient_module()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in modular_symbol_space(self, sign, base_ring, bound)
   1111         except KeyError:
   1112             pass
-> 1113         M = ell_modular_symbols.modular_symbol_space(self, sign, base_ring, bound=bound)
   1114         self.__modular_symbol_space[typ] = M
   1115         return M

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_modular_symbols.pyc in modular_symbol_space(E, sign, base_ring, bound)
    110         t = V.T(p)
    111         ap = E.ap(p)
--> 112         V = (t - ap).kernel()
    113         p = next_prime(p)
    114             

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__sub__ (sage/structure/element.c:12234)()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6463)()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7862)()

RuntimeError: BUG in map, returned None -2 <type 'sage.categories.map.FormalCompositeMap'> Composite map:
  From: Integer Ring
  To:   Full Hecke algebra acting on Modular Symbols space of dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field
  Defn:   Natural morphism:
          From: Integer Ring
          To:   Rational Field
        then
          Generic morphism:
          From: Rational Field
          To:   Full Hecke algebra acting on Modular Symbols space of dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field
```

with the latest patches.



---

archive/issue_comments_085266.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-03T15:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85266",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085267.json:
```json
{
    "body": "At last it seems to work! With the new first patch together with the second patch, all doc tests (both sage/ and doc/) pass (at least for me)!\n\nHere is the problem and its solution.\n\n__First Problem__\n\nHecke algebras: _lmul_ for its elements returns None. The previous patch version would thus register `from_base_ring` for coercion. However, in that case, a default implementation of `from_base_ring` would be used, which fails if _lmul_ returns None. Hence, it must not be registered as coercion.\n\nSolution: Use from_base_ring if it is a custom implementation , i.e., if `self.from_base_ring` is not obtained from `self.category().parent_class.from_base_ring`. If it is clear that the default implementation won't work, then do not register from_base_ring as coercion.\n\nAdditional advantage: If the user provides a fast custom `from_base_ring` then it will be picked up.\n\n__Second problem__\n\n`SpecialCubicQuotientRing`: Here, self.one() had not been available during initialisation\nof coercion from the base ring. Hence, in the previous patch version, from_base_ring\nhad been registered.\n\nHowever, _lmul_ is returning None, again. Additional complication:\nThe initialisation of a `SpecialCubicQuotientRing` as a commutative algebra happened\ntoo early, namely *before* its hash was available. Hence, the attempt to construct\na hom set containing the coercion from the base ring had failed.\n\nSolution: Move `CommutativeAlgebra.__init__` nearer to the end of `SpecialCubicQuotientRing.__init__`,\nnamely to a point where both self.one() and the hash are available.\n\n__Conclusion__\n\nReady for Review!\n\nApply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.rebase4.7.1.a1.patch",
    "created_at": "2011-08-03T15:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85267",
    "user": "SimonKing"
}
```

At last it seems to work! With the new first patch together with the second patch, all doc tests (both sage/ and doc/) pass (at least for me)!

Here is the problem and its solution.

__First Problem__

Hecke algebras: _lmul_ for its elements returns None. The previous patch version would thus register `from_base_ring` for coercion. However, in that case, a default implementation of `from_base_ring` would be used, which fails if _lmul_ returns None. Hence, it must not be registered as coercion.

Solution: Use from_base_ring if it is a custom implementation , i.e., if `self.from_base_ring` is not obtained from `self.category().parent_class.from_base_ring`. If it is clear that the default implementation won't work, then do not register from_base_ring as coercion.

Additional advantage: If the user provides a fast custom `from_base_ring` then it will be picked up.

__Second problem__

`SpecialCubicQuotientRing`: Here, self.one() had not been available during initialisation
of coercion from the base ring. Hence, in the previous patch version, from_base_ring
had been registered.

However, _lmul_ is returning None, again. Additional complication:
The initialisation of a `SpecialCubicQuotientRing` as a commutative algebra happened
too early, namely *before* its hash was available. Hence, the attempt to construct
a hom set containing the coercion from the base ring had failed.

Solution: Move `CommutativeAlgebra.__init__` nearer to the end of `SpecialCubicQuotientRing.__init__`,
namely to a point where both self.one() and the hash are available.

__Conclusion__

Ready for Review!

Apply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.rebase4.7.1.a1.patch



---

archive/issue_comments_085268.json:
```json
{
    "body": "PS: It seems that the patch bot has a problem, because it doesn't understand that one of the patches of #9976 is for the devel/sagenb repository, not for devel/sage. Too bad...",
    "created_at": "2011-08-03T15:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85268",
    "user": "SimonKing"
}
```

PS: It seems that the patch bot has a problem, because it doesn't understand that one of the patches of #9976 is for the devel/sagenb repository, not for devel/sage. Too bad...



---

archive/issue_comments_085269.json:
```json
{
    "body": "I am currently getting doctest failures with my patches, when I start with sage-4.7.1.rc2 and some other patches.\n\nI seems likely that the errors come from [attachment:trac9138-categories_for_rings.patch], but it needs further investigation. For the moment, it needs work.",
    "created_at": "2011-08-14T12:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85269",
    "user": "SimonKing"
}
```

I am currently getting doctest failures with my patches, when I start with sage-4.7.1.rc2 and some other patches.

I seems likely that the errors come from [attachment:trac9138-categories_for_rings.patch], but it needs further investigation. For the moment, it needs work.



---

archive/issue_comments_085270.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-14T12:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85270",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085271.json:
```json
{
    "body": "I added another dependency, namely #11316 (weighted degree term orders), that already has a positive review. But it still needs work, and because of the new dependency the first patch will require to be rebased.",
    "created_at": "2011-08-14T15:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85271",
    "user": "SimonKing"
}
```

I added another dependency, namely #11316 (weighted degree term orders), that already has a positive review. But it still needs work, and because of the new dependency the first patch will require to be rebased.



---

archive/issue_comments_085272.json:
```json
{
    "body": "The first patch needs to be rebased because of #11316, but it does not yield doctest errors.\n\nHowever, the second patch introduces errors in devel/sage-main/sage/crypto/boolean_function.pyx and devel/sage-main/sage/rings/polynomial/pbori.pyx; in each case, 14 tests fail.\n\nSo, back to the drawing board...",
    "created_at": "2011-08-14T16:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85272",
    "user": "SimonKing"
}
```

The first patch needs to be rebased because of #11316, but it does not yield doctest errors.

However, the second patch introduces errors in devel/sage-main/sage/crypto/boolean_function.pyx and devel/sage-main/sage/rings/polynomial/pbori.pyx; in each case, 14 tests fail.

So, back to the drawing board...



---

archive/issue_comments_085273.json:
```json
{
    "body": "Snap diagnose: #11316 changed when the term order is created, and I changed the order of things as well. In consequence, variable names are assigned twice, which yields an error. Example:\n\n\n```\nsage: from polybori import *\nsage: declare_ring([Block('x',2),Block('y',3)],globals())\nTraceback (most recent call last)\n...\nValueError: variable names cannot be changed after object creation.\n```\n",
    "created_at": "2011-08-14T16:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85273",
    "user": "SimonKing"
}
```

Snap diagnose: #11316 changed when the term order is created, and I changed the order of things as well. In consequence, variable names are assigned twice, which yields an error. Example:


```
sage: from polybori import *
sage: declare_ring([Block('x',2),Block('y',3)],globals())
Traceback (most recent call last)
...
ValueError: variable names cannot be changed after object creation.
```




---

archive/issue_comments_085274.json:
```json
{
    "body": "Replying to [comment:85 SimonKing]:\n> Snap diagnose: #11316 changed when the term order is created, and I changed the order of things as well. In consequence, variable names are assigned twice, which yields an error.\n\nI don't know what other ticket was creating the conflict (it has not been #11316, sorry for that). Anyway, the problem is that `MPolynomialRing_generic.__init__` was calling `ParentWithGens.__init__` first, and then `Ring.__init__`. By consequence, name assignment is tried *twice* - which is not allowed.\n\nI am currently running the doc tests (the two tests that previously failed are now fine), and if it succeeds then I'll update both patches.",
    "created_at": "2011-08-14T17:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85274",
    "user": "SimonKing"
}
```

Replying to [comment:85 SimonKing]:
> Snap diagnose: #11316 changed when the term order is created, and I changed the order of things as well. In consequence, variable names are assigned twice, which yields an error.

I don't know what other ticket was creating the conflict (it has not been #11316, sorry for that). Anyway, the problem is that `MPolynomialRing_generic.__init__` was calling `ParentWithGens.__init__` first, and then `Ring.__init__`. By consequence, name assignment is tried *twice* - which is not allowed.

I am currently running the doc tests (the two tests that previously failed are now fine), and if it succeeds then I'll update both patches.



---

archive/issue_comments_085275.json:
```json
{
    "body": "Attachment [trac9138-categories_for_rings.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138-categories_for_rings.patch) by SimonKing created at 2011-08-14 17:46:01\n\nUse category framework for rings",
    "created_at": "2011-08-14T17:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85275",
    "user": "SimonKing"
}
```

Attachment [trac9138-categories_for_rings.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138-categories_for_rings.patch) by SimonKing created at 2011-08-14 17:46:01

Use category framework for rings



---

archive/issue_comments_085276.json:
```json
{
    "body": "Both patches are updated: The first since it is rebased against #11316, the second since a rogue initialisation of a `ParentWithGens` occured.\n\nFor me, all tests pass, with sage-4.7.1.rc2 plus #11316 plus both patches from here. Thus, needs review again.\n\nApply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.patch",
    "created_at": "2011-08-14T17:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85276",
    "user": "SimonKing"
}
```

Both patches are updated: The first since it is rebased against #11316, the second since a rogue initialisation of a `ParentWithGens` occured.

For me, all tests pass, with sage-4.7.1.rc2 plus #11316 plus both patches from here. Thus, needs review again.

Apply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.patch



---

archive/issue_comments_085277.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-14T17:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85277",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085278.json:
```json
{
    "body": "I tested against sage-4.7.2.alpha1 . I didn't add any dependancys because their descriptions all say they are merged in that version already. Almost all test pass except some tests in pbori.pyx .\n\n\n```\nmderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage$ ../../sage -t --long sage/rings/polynomial/pbori.pyx\nsage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage-main/sage/rings/polynomial/pbori.pyx\", line 843:\n    sage: P(p)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[23]>\", line 1, in <module>\n        P(p)###line 843:\n    sage: P(p)\n      File \"parent.pyx\", line 945, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7108)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)\n      File \"pbori.pyx\", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)\n    IndexError: list index out of range\n**********************************************************************\nFile \"/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage-main/sage/rings/polynomial/pbori.pyx\", line 563:\n    sage: ZZ['a'].gen() + c\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[16]>\", line 1, in <module>\n        ZZ['a'].gen() + c###line 563:\n    sage: ZZ['a'].gen() + c\n      File \"element.pyx\", line 1309, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11532)\n      File \"coerce.pyx\", line 713, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6420)\n      File \"coerce.pyx\", line 827, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7682)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)\n      File \"pbori.pyx\", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)\n    IndexError: list index out of range\n**********************************************************************\n2 items had failures:\n   1 of  25 in __main__.example_10\n   1 of  18 in __main__.example_8\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/mderickx/.sage//tmp/.doctest_pbori.py\n\t [6.1 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\nTotal time for all tests: 6.1 seconds\n```\n\n\nA little sanity check that #11316 was really merged in 4.7.2.alpha1\n\n\n```\nmderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage$ ../../sage -hg log sage/rings/polynomial/pbori.pyx |head -n 20\nchangeset:   15995:f3369d315c96\ntag:         qtip\ntag:         tip\ntag:         trac9138_categories_for_more_rings.patch\nuser:        Simon King <simon.king@uni-jena.de>\ndate:        Sun Apr 24 15:28:28 2011 +0200\nsummary:     #9138: Provide the category framework for quotient rings and free algebras.\n\nchangeset:   15990:cf06a8bb75f4\nuser:        Kwankyu Lee <ekwankyu@gmail.com>\ndate:        Tue May 10 16:58:20 2011 +0900\nsummary:     Trac #11316: #11316: added weighted degree term orders\n\n\n```\n",
    "created_at": "2011-08-29T01:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85278",
    "user": "mderickx"
}
```

I tested against sage-4.7.2.alpha1 . I didn't add any dependancys because their descriptions all say they are merged in that version already. Almost all test pass except some tests in pbori.pyx .


```
mderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage$ ../../sage -t --long sage/rings/polynomial/pbori.pyx
sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
**********************************************************************
File "/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage-main/sage/rings/polynomial/pbori.pyx", line 843:
    sage: P(p)
Exception raised:
    Traceback (most recent call last):
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[23]>", line 1, in <module>
        P(p)###line 843:
    sage: P(p)
      File "parent.pyx", line 945, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7108)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)
      File "pbori.pyx", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)
    IndexError: list index out of range
**********************************************************************
File "/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage-main/sage/rings/polynomial/pbori.pyx", line 563:
    sage: ZZ['a'].gen() + c
Exception raised:
    Traceback (most recent call last):
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[16]>", line 1, in <module>
        ZZ['a'].gen() + c###line 563:
    sage: ZZ['a'].gen() + c
      File "element.pyx", line 1309, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11532)
      File "coerce.pyx", line 713, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6420)
      File "coerce.pyx", line 827, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7682)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)
      File "pbori.pyx", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)
    IndexError: list index out of range
**********************************************************************
2 items had failures:
   1 of  25 in __main__.example_10
   1 of  18 in __main__.example_8
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mderickx/.sage//tmp/.doctest_pbori.py
	 [6.1 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
Total time for all tests: 6.1 seconds
```


A little sanity check that #11316 was really merged in 4.7.2.alpha1


```
mderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha1/devel/sage$ ../../sage -hg log sage/rings/polynomial/pbori.pyx |head -n 20
changeset:   15995:f3369d315c96
tag:         qtip
tag:         tip
tag:         trac9138_categories_for_more_rings.patch
user:        Simon King <simon.king@uni-jena.de>
date:        Sun Apr 24 15:28:28 2011 +0200
summary:     #9138: Provide the category framework for quotient rings and free algebras.

changeset:   15990:cf06a8bb75f4
user:        Kwankyu Lee <ekwankyu@gmail.com>
date:        Tue May 10 16:58:20 2011 +0900
summary:     Trac #11316: #11316: added weighted degree term orders


```




---

archive/issue_comments_085279.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-29T01:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85279",
    "user": "mderickx"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085280.json:
```json
{
    "body": "Strange. With sage-4.7.2.alpha2, I do not get that error.\n\n```\n$ ../../sage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\nsage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\n\t [4.8 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.8 seconds\n```\n\n\nBut I installed an updated version of polybori, perhaps that is the reason. So, I should try with vanilla sage-4.7.2.alpha1 and try to replicate the error you get.",
    "created_at": "2011-08-29T06:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85280",
    "user": "SimonKing"
}
```

Strange. With sage-4.7.2.alpha2, I do not get that error.

```
$ ../../sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
	 [4.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.8 seconds
```


But I installed an updated version of polybori, perhaps that is the reason. So, I should try with vanilla sage-4.7.2.alpha1 and try to replicate the error you get.



---

archive/issue_comments_085281.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-29T09:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85281",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085282.json:
```json
{
    "body": "I can definitely not confirm the error that you got.\n\nI built sage-4.7.2.alpha2 (not alpha1, if that should make a difference). Then I qimported the two patches:\n\n```\n$ hg qapplied\ntrac9138-categories_for_rings.patch\ntrac9138_categories_for_more_rings.patch\n```\n\nfollowed by `sage -b`.\n\nAnd still I have\n\n```\n$ ../../sage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\nsage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\n\t [7.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 7.8 seconds\n```\n",
    "created_at": "2011-08-29T09:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85282",
    "user": "SimonKing"
}
```

I can definitely not confirm the error that you got.

I built sage-4.7.2.alpha2 (not alpha1, if that should make a difference). Then I qimported the two patches:

```
$ hg qapplied
trac9138-categories_for_rings.patch
trac9138_categories_for_more_rings.patch
```

followed by `sage -b`.

And still I have

```
$ ../../sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
	 [7.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.8 seconds
```




---

archive/issue_comments_085283.json:
```json
{
    "body": "Very very strange. Ok what I did is on sage.math.washington.edu:\n\nI downloaded: http://boxen.math.washington.edu/home/release/sage-4.7.2.alpha2/sage-4.7.2.alpha2.tar\nExtracted the file and did\nmake build\nusing environment variables MAKE=make -j20 and SAGE_SPKG_PARALLEL_BUILD=yes.\nAfter having made this clean build (located in /mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2) I got:\n\n\n```\nmderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2$ ./sage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\nsage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\n\t [7.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 7.0 seconds\n```\n\nThen I qimported and applied your two patches and did\n\n```\nmderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2/devel/sage$ ../../sage -bt --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n...whole load of buiding output\nsage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2/devel/sage-main/sage/rings/polynomial/pbori.pyx\", line 843:\n    sage: P(p)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[23]>\", line 1, in <module>\n        P(p)###line 843:\n    sage: P(p)\n      File \"parent.pyx\", line 945, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7108)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)\n      File \"pbori.pyx\", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)\n        \n    IndexError: list index out of range\n**********************************************************************\nFile \"/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2/devel/sage-main/sage/rings/polynomial/pbori.pyx\", line 563:\n    sage: ZZ['a'].gen() + c\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mderickx/.sage/tmp/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[16]>\", line 1, in <module>\n        ZZ['a'].gen() + c###line 563:\n    sage: ZZ['a'].gen() + c\n      File \"element.pyx\", line 1309, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11532)\n      File \"coerce.pyx\", line 742, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6577)\n      File \"coerce.pyx\", line 856, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7818)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)\n      File \"pbori.pyx\", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)\n        \n    IndexError: list index out of range\n**********************************************************************\n2 items had failures:\n   1 of  25 in __main__.example_10\n   1 of  18 in __main__.example_8\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/mderickx/.sage//tmp/.doctest_pbori.py\n\t [6.1 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t --long \"devel/sage-main/sage/rings/polynomial/pbori.pyx\"\nTotal time for all tests: 6.1 seconds\n```\n\n\nSo I seem to not be able to reproduce your passing the doctest.\nDid you also use sage.math. I can give you acces to the created folder on sage.math so you can fiddle around with it.",
    "created_at": "2011-08-29T22:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85283",
    "user": "mderickx"
}
```

Very very strange. Ok what I did is on sage.math.washington.edu:

I downloaded: http://boxen.math.washington.edu/home/release/sage-4.7.2.alpha2/sage-4.7.2.alpha2.tar
Extracted the file and did
make build
using environment variables MAKE=make -j20 and SAGE_SPKG_PARALLEL_BUILD=yes.
After having made this clean build (located in /mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2) I got:


```
mderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2$ ./sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
	 [7.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.0 seconds
```

Then I qimported and applied your two patches and did

```
mderickx@sage:/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2/devel/sage$ ../../sage -bt --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"

----------------------------------------------------------
sage: Building and installing modified Sage library files.
...whole load of buiding output
sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
**********************************************************************
File "/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2/devel/sage-main/sage/rings/polynomial/pbori.pyx", line 843:
    sage: P(p)
Exception raised:
    Traceback (most recent call last):
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[23]>", line 1, in <module>
        P(p)###line 843:
    sage: P(p)
      File "parent.pyx", line 945, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7108)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)
      File "pbori.pyx", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)
        
    IndexError: list index out of range
**********************************************************************
File "/mnt/usb1/scratch/mderickx/sage-4.7.2.alpha2/devel/sage-main/sage/rings/polynomial/pbori.pyx", line 563:
    sage: ZZ['a'].gen() + c
Exception raised:
    Traceback (most recent call last):
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mderickx/.sage/tmp/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[16]>", line 1, in <module>
        ZZ['a'].gen() + c###line 563:
    sage: ZZ['a'].gen() + c
      File "element.pyx", line 1309, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11532)
      File "coerce.pyx", line 742, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6577)
      File "coerce.pyx", line 856, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7818)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3256)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3159)
      File "pbori.pyx", line 896, in sage.rings.polynomial.pbori.BooleanPolynomialRing._element_constructor_ (sage/rings/polynomial/pbori.cpp:8488)
        
    IndexError: list index out of range
**********************************************************************
2 items had failures:
   1 of  25 in __main__.example_10
   1 of  18 in __main__.example_8
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mderickx/.sage//tmp/.doctest_pbori.py
	 [6.1 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --long "devel/sage-main/sage/rings/polynomial/pbori.pyx"
Total time for all tests: 6.1 seconds
```


So I seem to not be able to reproduce your passing the doctest.
Did you also use sage.math. I can give you acces to the created folder on sage.math so you can fiddle around with it.



---

archive/issue_comments_085284.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-08-29T22:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85284",
    "user": "mderickx"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085285.json:
```json
{
    "body": "Is the update of pbory also on another ticket? Maybe we should list it as a dependancy?",
    "created_at": "2011-08-29T22:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85285",
    "user": "mderickx"
}
```

Is the update of pbory also on another ticket? Maybe we should list it as a dependancy?



---

archive/issue_comments_085286.json:
```json
{
    "body": "Replying to [comment:92 mderickx]:\n> Is the update of pbory also on another ticket? Maybe we should list it as a dependancy?\n\nNo. I did not install the new pbory spkg. Also I didn't try yet to install my patches on sage.math. So, probably that's the next step.",
    "created_at": "2011-08-30T05:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85286",
    "user": "SimonKing"
}
```

Replying to [comment:92 mderickx]:
> Is the update of pbory also on another ticket? Maybe we should list it as a dependancy?

No. I did not install the new pbory spkg. Also I didn't try yet to install my patches on sage.math. So, probably that's the next step.



---

archive/issue_comments_085287.json:
```json
{
    "body": "What I now did was as follows:\n\n* Copy and open the pre-built sage-4.7.2.alpha2.tar.gz for sage.math (saves a lot of time...)\n* qimport and apply the first patch, do `sage -b` and find that pbori.pyx still passes the tests.\n* qimport and apply the second patch, do `sage -b` and confirm the error that you observed.\n\nAt least, now there is a chance for me to debug it...",
    "created_at": "2011-08-30T06:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85287",
    "user": "SimonKing"
}
```

What I now did was as follows:

* Copy and open the pre-built sage-4.7.2.alpha2.tar.gz for sage.math (saves a lot of time...)
* qimport and apply the first patch, do `sage -b` and find that pbori.pyx still passes the tests.
* qimport and apply the second patch, do `sage -b` and confirm the error that you observed.

At least, now there is a chance for me to debug it...



---

archive/issue_comments_085288.json:
```json
{
    "body": "I got it!!\n\nThe problem was a misprint. I use the letter j where it should be the number zero. Apparently, on my machine, j became initialised as zero, so, things worked. But (as I found by printing its value) on sage.math it became initialised as one, hence, resulting in an index error.\n\nI updated the patch, and with it, I find\n\n```\nSimonKing@sage:~/SAGE/sage-4.7.2.alpha2-sage.math.washington.edu-x86_64-Linux$ ./sage -t devel/sage/sage/rings/polynomial/pbori.pyx\nsage -t  \"devel/sage/sage/rings/polynomial/pbori.pyx\"       \n         [6.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 6.0 seconds\n```\n\n\nSo, that was easy... Back to \"needs review\"!",
    "created_at": "2011-08-30T08:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85288",
    "user": "SimonKing"
}
```

I got it!!

The problem was a misprint. I use the letter j where it should be the number zero. Apparently, on my machine, j became initialised as zero, so, things worked. But (as I found by printing its value) on sage.math it became initialised as one, hence, resulting in an index error.

I updated the patch, and with it, I find

```
SimonKing@sage:~/SAGE/sage-4.7.2.alpha2-sage.math.washington.edu-x86_64-Linux$ ./sage -t devel/sage/sage/rings/polynomial/pbori.pyx
sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"       
         [6.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.0 seconds
```


So, that was easy... Back to "needs review"!



---

archive/issue_comments_085289.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-08-30T08:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85289",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085290.json:
```json
{
    "body": "It turns out that, when combining this ticket with #11342, then one test fails (because some category stuff is initialised that on #11342 is expected to be non-initialised).\n\nHow to proceed? Both tickets are not positively reviewed yet.",
    "created_at": "2011-09-07T10:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85290",
    "user": "SimonKing"
}
```

It turns out that, when combining this ticket with #11342, then one test fails (because some category stuff is initialised that on #11342 is expected to be non-initialised).

How to proceed? Both tickets are not positively reviewed yet.



---

archive/issue_comments_085291.json:
```json
{
    "body": "I see you are the author of both so I guess it depends on wich ticket you want to get merged first. You should rebase one of the two tickets to apply cleanly after the other and add the corresponding dependency in the dependencies field. And maybe also add a note in the description for possible reviewers that it is wiser to first review the ticket on wich it depends.\n\nPersonally I would want this ticket to be merged before the other. The main reason is that this ticket really cleans up a lot of rings stuff, and the other ticket just makes things faster. And in general I prefer to do things right first and then make them fast ;). The other reason is that I expect that this ticket will cause more conflicts with other tickets. I would try to get this one in as fast as possible so there are less patches merged depending on doing things the old \"wrong\" way. \n\nOr an even smarter thing to do would be to make both tickets apply cleanly on their own and passing all doctest in such a way that the can also be applied at the same time (but maybe not passing all doctests) . Then create a third patch wich is fixes the conflict between these tickets. This patch can then be added on wathever ticket gets reviewed/merged last. In this way none of the two tickets can delay the merging of the other.",
    "created_at": "2011-09-07T14:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85291",
    "user": "mderickx"
}
```

I see you are the author of both so I guess it depends on wich ticket you want to get merged first. You should rebase one of the two tickets to apply cleanly after the other and add the corresponding dependency in the dependencies field. And maybe also add a note in the description for possible reviewers that it is wiser to first review the ticket on wich it depends.

Personally I would want this ticket to be merged before the other. The main reason is that this ticket really cleans up a lot of rings stuff, and the other ticket just makes things faster. And in general I prefer to do things right first and then make them fast ;). The other reason is that I expect that this ticket will cause more conflicts with other tickets. I would try to get this one in as fast as possible so there are less patches merged depending on doing things the old "wrong" way. 

Or an even smarter thing to do would be to make both tickets apply cleanly on their own and passing all doctest in such a way that the can also be applied at the same time (but maybe not passing all doctests) . Then create a third patch wich is fixes the conflict between these tickets. This patch can then be added on wathever ticket gets reviewed/merged last. In this way none of the two tickets can delay the merging of the other.



---

archive/issue_comments_085292.json:
```json
{
    "body": "I've reviewed #11342 before reading Maarten's comment, so how about we can merge #11342 first and #9138 afterwards.\n\nIn `pbori.pyx`, can you clean up the comparison? E.g. remove `__richcmp__` completely and fix the `_cmp_` docstring.\n\nIn `sage/structure/element.pyx`, the following is stated:\n\n```\n    # For a derived Cython class, you **must** put the following in\n    # your subclasses, in order for it to take advantage of the\n    # above generic comparison code.  You must also define\n    # either _cmp_c_impl (if your subclass is totally ordered),\n    # _richcmp_c_impl (if your subclass is partially ordered), or both\n    # (if your class has both a total order and a partial order;\n    # then the total order will be available with cmp(), and the partial\n    # order will be available with the relation operators; in this case\n    # you must also define __cmp__ in your subclass).\n```\n\nNow this info might be outdated, and I admit that I don't have a good understanding of how comparison is supposed to be implemented in the new coercion model, but your `_cmp_` method  does not follow that comment.",
    "created_at": "2011-09-07T14:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85292",
    "user": "vbraun"
}
```

I've reviewed #11342 before reading Maarten's comment, so how about we can merge #11342 first and #9138 afterwards.

In `pbori.pyx`, can you clean up the comparison? E.g. remove `__richcmp__` completely and fix the `_cmp_` docstring.

In `sage/structure/element.pyx`, the following is stated:

```
    # For a derived Cython class, you **must** put the following in
    # your subclasses, in order for it to take advantage of the
    # above generic comparison code.  You must also define
    # either _cmp_c_impl (if your subclass is totally ordered),
    # _richcmp_c_impl (if your subclass is partially ordered), or both
    # (if your class has both a total order and a partial order;
    # then the total order will be available with cmp(), and the partial
    # order will be available with the relation operators; in this case
    # you must also define __cmp__ in your subclass).
```

Now this info might be outdated, and I admit that I don't have a good understanding of how comparison is supposed to be implemented in the new coercion model, but your `_cmp_` method  does not follow that comment.



---

archive/issue_comments_085293.json:
```json
{
    "body": "Replying to [comment:98 vbraun]:\n> I've reviewed #11342 before reading Maarten's comment, so how about we can merge #11342 first and #9138 afterwards.\n\nMakes sense now...\n\nSo, I'll attach a new patch here. The old patch does apply, it is just that one must change the expected output (namely the name of a class) in one test.\n\n> In `pbori.pyx`, can you clean up the comparison? E.g. remove `__richcmp__` completely and fix the `_cmp_` docstring.\n\nOK. Sometimes I like to keep the old code in a comment, so that one can see how and why things have changed. Fixing the `_cmp_` docstring is certainly needed.\n\n> In `sage/structure/element.pyx`, the following is stated:\n> {{{\n>     # For a derived Cython class, you **must** put the following in\n>     # your subclasses, in order for it to take advantage of the\n>     # above generic comparison code.\n> ...\n> Now this info might be outdated, and I admit that I don't have a good understanding of how comparison is supposed to be implemented in the new coercion model, but your `_cmp_` method  does not follow that comment.\n\nWhat you cite is for elements (and not outdated), but my code is for parents. I am afraid I have no reference. But I think I remember that for parents written in Cython one should provide a (single underscore) `_cmp_` method. I might ask on sage-devel, though.",
    "created_at": "2011-09-07T15:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85293",
    "user": "SimonKing"
}
```

Replying to [comment:98 vbraun]:
> I've reviewed #11342 before reading Maarten's comment, so how about we can merge #11342 first and #9138 afterwards.

Makes sense now...

So, I'll attach a new patch here. The old patch does apply, it is just that one must change the expected output (namely the name of a class) in one test.

> In `pbori.pyx`, can you clean up the comparison? E.g. remove `__richcmp__` completely and fix the `_cmp_` docstring.

OK. Sometimes I like to keep the old code in a comment, so that one can see how and why things have changed. Fixing the `_cmp_` docstring is certainly needed.

> In `sage/structure/element.pyx`, the following is stated:
> {{{
>     # For a derived Cython class, you **must** put the following in
>     # your subclasses, in order for it to take advantage of the
>     # above generic comparison code.
> ...
> Now this info might be outdated, and I admit that I don't have a good understanding of how comparison is supposed to be implemented in the new coercion model, but your `_cmp_` method  does not follow that comment.

What you cite is for elements (and not outdated), but my code is for parents. I am afraid I have no reference. But I think I remember that for parents written in Cython one should provide a (single underscore) `_cmp_` method. I might ask on sage-devel, though.



---

archive/issue_comments_085294.json:
```json
{
    "body": "Actually the comparison code should be completely removed: Boolean polynomial rings are unique parents, and thus they are equal if and only if they are identical.\n\nSo, I will submit a new patch, that removes both _cmp_ and `__richcmp__` completely (but perhaps moving the old tests to a new place) and fixes the doc test error that occurs in combination with #11342.",
    "created_at": "2011-09-07T15:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85294",
    "user": "SimonKing"
}
```

Actually the comparison code should be completely removed: Boolean polynomial rings are unique parents, and thus they are equal if and only if they are identical.

So, I will submit a new patch, that removes both _cmp_ and `__richcmp__` completely (but perhaps moving the old tests to a new place) and fixes the doc test error that occurs in combination with #11342.



---

archive/issue_comments_085295.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-09-07T15:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85295",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085296.json:
```json
{
    "body": "Attachment [trac9138_categories_for_more_rings.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138_categories_for_more_rings.patch) by SimonKing created at 2011-09-07 20:38:54\n\nCategory framework for quotient rings and free algebras; new coercion framework for boolean polynomial rings; conversion from univariate polynomial rings to boolean polynomial rings",
    "created_at": "2011-09-07T20:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85296",
    "user": "SimonKing"
}
```

Attachment [trac9138_categories_for_more_rings.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138_categories_for_more_rings.patch) by SimonKing created at 2011-09-07 20:38:54

Category framework for quotient rings and free algebras; new coercion framework for boolean polynomial rings; conversion from univariate polynomial rings to boolean polynomial rings



---

archive/issue_comments_085297.json:
```json
{
    "body": "I have updated the second patch. Since the ticket now depends on #11342, I added a fix for pari ring doctest. Also, I completely removed the `__richcmp__` and `_cmp_` code from the boolean polynomial rings, since the code is actually not needed anymore (they are unique parents, and thus `R==S`  is the same as `R is S`.\n\nFor me, the long tests pass. I hope they do for you as well?",
    "created_at": "2011-09-07T20:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85297",
    "user": "SimonKing"
}
```

I have updated the second patch. Since the ticket now depends on #11342, I added a fix for pari ring doctest. Also, I completely removed the `__richcmp__` and `_cmp_` code from the boolean polynomial rings, since the code is actually not needed anymore (they are unique parents, and thus `R==S`  is the same as `R is S`.

For me, the long tests pass. I hope they do for you as well?



---

archive/issue_comments_085298.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-07T20:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85298",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085299.json:
```json
{
    "body": "Replying to [comment:101 SimonKing]:\n> ... Also, I completely removed the `__richcmp__` and `_cmp_` code...\n\n... but I moved the old doc tests from `__richcmp__` to a different place, so that the old tests are preserved.",
    "created_at": "2011-09-07T21:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85299",
    "user": "SimonKing"
}
```

Replying to [comment:101 SimonKing]:
> ... Also, I completely removed the `__richcmp__` and `_cmp_` code...

... but I moved the old doc tests from `__richcmp__` to a different place, so that the old tests are preserved.



---

archive/issue_comments_085300.json:
```json
{
    "body": "The doctests pass for me, too. \n\nWhen I see commented-out methods lying around then I usually assume that they should be IN but for some reason we can't add the code yet, or that there is a bug in them that ought to be fixed. But right now there are various places where its just old stuff that we should actually get rid of. I would very much appreciate if you could clean that up and remove instead of just commenting out code that is not relevant any more. Realistically, if we don't remove that stuff while refactoring for newer frameworks then it'll forever clutter the source files. For those interested in the history there is always mercurial...\n\nSome comments on the first patch:\n\n* There is also a commented-out `__cmp__` in `sage/rings/polynomial/infinite_polynomial_ring.py`, I take it that should be removed as well? \n* `sage/rings/ring.pyx` l. 356-360 some commented out stuff after return? Same file, there are two `category()` methods that are just commented out.\n\nSecond patch: \n\n* `sage/algebras/free_algebra_quotient.py` the `_coerce_impl` and `__contains__` methods are also old stuff that should be snipped now that its no longer used.\n* The `_mul_(self,y)` method in `sage/monoids/free_monoid_element.py` guarantees `y` to be a `FreeModuleElement` so the commented-out isinstance check should be removed.\n* `sage/monoids/monoid.py` again superfluous `category()` method already commented out.\n* The commented-out `__reduce__` method in `sage/rings/polynomial/pbori.pyx` should go away, right?\n* The added comments in `sage/rings/quotient_ring.py` l. 153-162 aren't very helpful IMHO.",
    "created_at": "2011-09-08T03:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85300",
    "user": "vbraun"
}
```

The doctests pass for me, too. 

When I see commented-out methods lying around then I usually assume that they should be IN but for some reason we can't add the code yet, or that there is a bug in them that ought to be fixed. But right now there are various places where its just old stuff that we should actually get rid of. I would very much appreciate if you could clean that up and remove instead of just commenting out code that is not relevant any more. Realistically, if we don't remove that stuff while refactoring for newer frameworks then it'll forever clutter the source files. For those interested in the history there is always mercurial...

Some comments on the first patch:

* There is also a commented-out `__cmp__` in `sage/rings/polynomial/infinite_polynomial_ring.py`, I take it that should be removed as well? 
* `sage/rings/ring.pyx` l. 356-360 some commented out stuff after return? Same file, there are two `category()` methods that are just commented out.

Second patch: 

* `sage/algebras/free_algebra_quotient.py` the `_coerce_impl` and `__contains__` methods are also old stuff that should be snipped now that its no longer used.
* The `_mul_(self,y)` method in `sage/monoids/free_monoid_element.py` guarantees `y` to be a `FreeModuleElement` so the commented-out isinstance check should be removed.
* `sage/monoids/monoid.py` again superfluous `category()` method already commented out.
* The commented-out `__reduce__` method in `sage/rings/polynomial/pbori.pyx` should go away, right?
* The added comments in `sage/rings/quotient_ring.py` l. 153-162 aren't very helpful IMHO.



---

archive/issue_comments_085301.json:
```json
{
    "body": "Attachment [trac9138_remove_unused_code.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138_remove_unused_code.patch) by SimonKing created at 2011-09-08 08:20:24\n\nCompletely remove old unused code, rather than commenting it out",
    "created_at": "2011-09-08T08:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85301",
    "user": "SimonKing"
}
```

Attachment [trac9138_remove_unused_code.patch](tarball://root/attachments/some-uuid/ticket9138/trac9138_remove_unused_code.patch) by SimonKing created at 2011-09-08 08:20:24

Completely remove old unused code, rather than commenting it out



---

archive/issue_comments_085302.json:
```json
{
    "body": "I provided a third patch that (hopefully) addresses Volker's remarks on commented out old code that better ought to be removed. Tests still pass for me, but that's no surprise, since the new patch does not change the code nor the documentation.\n\nApply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.patch trac9138_remove_unused_code.patch",
    "created_at": "2011-09-08T08:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85302",
    "user": "SimonKing"
}
```

I provided a third patch that (hopefully) addresses Volker's remarks on commented out old code that better ought to be removed. Tests still pass for me, but that's no surprise, since the new patch does not change the code nor the documentation.

Apply trac9138-categories_for_rings.patch trac9138_categories_for_more_rings.patch trac9138_remove_unused_code.patch



---

archive/issue_comments_085303.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-08T14:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85303",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085304.json:
```json
{
    "body": "Thanks for the effort of cleaning up the rings! Positive review.",
    "created_at": "2011-09-08T14:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85304",
    "user": "vbraun"
}
```

Thanks for the effort of cleaning up the rings! Positive review.



---

archive/issue_comments_085305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-17T04:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85305",
    "user": "leif"
}
```

Resolution: fixed



---

archive/issue_comments_085306.json:
```json
{
    "body": "Simon, concercing #9138 and #11900: I am planning to unmerge #9138 in the sage-4.7.2 release series with the goal of merging them both in sage-4.7.3.alpha0.  This is because I feel that, apart from this, the sage-4.7.2 release is essentially finished.  Postponing to sage-4.7.3 will give us some more time for testing.  What do you think?",
    "created_at": "2011-10-08T09:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85306",
    "user": "jdemeyer"
}
```

Simon, concercing #9138 and #11900: I am planning to unmerge #9138 in the sage-4.7.2 release series with the goal of merging them both in sage-4.7.3.alpha0.  This is because I feel that, apart from this, the sage-4.7.2 release is essentially finished.  Postponing to sage-4.7.3 will give us some more time for testing.  What do you think?



---

archive/issue_comments_085307.json:
```json
{
    "body": "Replying to [comment:110 jdemeyer]:\n> Simon, concercing #9138 and #11900: I am planning to unmerge #9138 in the sage-4.7.2 release series with the goal of merging them both in sage-4.7.3.alpha0.  This is because I feel that, apart from this, the sage-4.7.2 release is essentially finished.  Postponing to sage-4.7.3 will give us some more time for testing.  What do you think?\n\nIt also depends on the time. The patch from #11900 is invasive, since it makes libsingular polynomial rings use the new coercion model. I think that I'll need until Tuesday or Wednesday to get my patch ready. And then we need to find a reviewer. When is the release supposed to happen?",
    "created_at": "2011-10-08T09:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85307",
    "user": "SimonKing"
}
```

Replying to [comment:110 jdemeyer]:
> Simon, concercing #9138 and #11900: I am planning to unmerge #9138 in the sage-4.7.2 release series with the goal of merging them both in sage-4.7.3.alpha0.  This is because I feel that, apart from this, the sage-4.7.2 release is essentially finished.  Postponing to sage-4.7.3 will give us some more time for testing.  What do you think?

It also depends on the time. The patch from #11900 is invasive, since it makes libsingular polynomial rings use the new coercion model. I think that I'll need until Tuesday or Wednesday to get my patch ready. And then we need to find a reviewer. When is the release supposed to happen?



---

archive/issue_comments_085308.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-10-08T10:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85308",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_085309.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-10-08T10:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85309",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_085310.json:
```json
{
    "body": "Replying to [comment:111 SimonKing]:\n> When is the release supposed to happen?\n\nWell, I think sage-4.7.2.alpha4 could be finished today or tomorrow and I would rather not merge #11900 after that, especially if the patch is invasive.  This is probably not a patch which I want to quickly squeeze in an rc0.\n\nNote that the actual release of sage-4.7.2 could easily be some weeks from now, because we need some time for testing on various platforms, fixing things in an rc, testing again,...",
    "created_at": "2011-10-08T10:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85310",
    "user": "jdemeyer"
}
```

Replying to [comment:111 SimonKing]:
> When is the release supposed to happen?

Well, I think sage-4.7.2.alpha4 could be finished today or tomorrow and I would rather not merge #11900 after that, especially if the patch is invasive.  This is probably not a patch which I want to quickly squeeze in an rc0.

Note that the actual release of sage-4.7.2 could easily be some weeks from now, because we need some time for testing on various platforms, fixing things in an rc, testing again,...



---

archive/issue_comments_085311.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-15T16:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85311",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085312.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-15T16:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85312",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085313.json:
```json
{
    "body": "Still positive review, of course modulo #11900.",
    "created_at": "2011-10-15T16:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85313",
    "user": "jdemeyer"
}
```

Still positive review, of course modulo #11900.



---

archive/issue_comments_085314.json:
```json
{
    "body": "Since the patch bot does not know which patch to apply (hence, complains on all tickets that depend on this one):\n\nApply 9138_flat.patch",
    "created_at": "2011-10-24T12:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85314",
    "user": "SimonKing"
}
```

Since the patch bot does not know which patch to apply (hence, complains on all tickets that depend on this one):

Apply 9138_flat.patch



---

archive/issue_comments_085315.json:
```json
{
    "body": "Milestone sage-4.7.3 deleted",
    "created_at": "2011-11-03T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85315",
    "user": "jdemeyer"
}
```

Milestone sage-4.7.3 deleted



---

archive/issue_comments_085316.json:
```json
{
    "body": "Since I have two ticket in sage-pending (#11575 and #4539) because of the de-merge: Will this be in 4.8.0?",
    "created_at": "2011-11-03T20:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85316",
    "user": "AlexanderDreyer"
}
```

Since I have two ticket in sage-pending (#11575 and #4539) because of the de-merge: Will this be in 4.8.0?



---

archive/issue_comments_085317.json:
```json
{
    "body": "Replying to [comment:117 AlexanderDreyer]:\n> Since I have two ticket in sage-pending (#11575 and #4539) because of the de-merge: Will this be in 4.8.0?\n\nDepends on #11900.  In any case, #9138 and #11900 will be merged together.  If #11900 gets a positive review in a reasonable time, then they will be merged.  William Stein already mentioned he might review #11900, which would be a very good thing.",
    "created_at": "2011-11-03T21:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85317",
    "user": "jdemeyer"
}
```

Replying to [comment:117 AlexanderDreyer]:
> Since I have two ticket in sage-pending (#11575 and #4539) because of the de-merge: Will this be in 4.8.0?

Depends on #11900.  In any case, #9138 and #11900 will be merged together.  If #11900 gets a positive review in a reasonable time, then they will be merged.  William Stein already mentioned he might review #11900, which would be a very good thing.



---

archive/issue_comments_085318.json:
```json
{
    "body": "Since #11761 is already merged, I was rebasing the patch relative to it. The change is trivial, though: #11761 adds the line\n\n```\n         msg = None\n```\n\ninto sage/rings/polyomial/pbori.pyx, so that one of my hunks did not apply anymore. I did test that afterwards `sage -t sage/rings/polynomial/pbori.pyx` still passes.\n\nI hope that the rebase is trivial enough, so that I can preserve the positive review.\n\nApply 9138_flat_new_cython.patch",
    "created_at": "2011-11-15T17:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85318",
    "user": "SimonKing"
}
```

Since #11761 is already merged, I was rebasing the patch relative to it. The change is trivial, though: #11761 adds the line

```
         msg = None
```

into sage/rings/polyomial/pbori.pyx, so that one of my hunks did not apply anymore. I did test that afterwards `sage -t sage/rings/polynomial/pbori.pyx` still passes.

I hope that the rebase is trivial enough, so that I can preserve the positive review.

Apply 9138_flat_new_cython.patch



---

archive/issue_comments_085319.json:
```json
{
    "body": "Replying to [comment:120 SimonKing]:\n> Since #11761 is already merged, I was rebasing the patch relative to it. The change is trivial, though: #11761 adds the line\n> {{{\n>          msg = None\n> }}}\n> into sage/rings/polyomial/pbori.pyx\n\nMy mistake: The first patch from #11761 adds that line, but the reviewer patch removes it. I forgot to apply the reviewer patch.\n\nIn other words: Rebasing was not needed! Return to the old patch.\n\nApply 9138_flat.patch",
    "created_at": "2011-11-18T11:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85319",
    "user": "SimonKing"
}
```

Replying to [comment:120 SimonKing]:
> Since #11761 is already merged, I was rebasing the patch relative to it. The change is trivial, though: #11761 adds the line
> {{{
>          msg = None
> }}}
> into sage/rings/polyomial/pbori.pyx

My mistake: The first patch from #11761 adds that line, but the reviewer patch removes it. I forgot to apply the reviewer patch.

In other words: Rebasing was not needed! Return to the old patch.

Apply 9138_flat.patch



---

archive/issue_comments_085320.json:
```json
{
    "body": "A note to the release manager: #11900 just got a positive review by Nicolas Thi\u00e9ry.",
    "created_at": "2011-12-09T14:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85320",
    "user": "SimonKing"
}
```

A note to the release manager: #11900 just got a positive review by Nicolas Thiéry.



---

archive/issue_comments_085321.json:
```json
{
    "body": "Attachment [9138_flat.patch](tarball://root/attachments/some-uuid/ticket9138/9138_flat.patch) by jdemeyer created at 2012-01-05 22:44:45\n\nAll patches together in one patch, rebased to #9958",
    "created_at": "2012-01-05T22:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85321",
    "user": "jdemeyer"
}
```

Attachment [9138_flat.patch](tarball://root/attachments/some-uuid/ticket9138/9138_flat.patch) by jdemeyer created at 2012-01-05 22:44:45

All patches together in one patch, rebased to #9958



---

archive/issue_comments_085322.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-18T08:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9138#issuecomment-85322",
    "user": "jdemeyer"
}
```

Resolution: fixed
