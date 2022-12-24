# Issue 8139: Can not compute (very) high power of WordMorphism

archive/issues_008139.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  slabbe fsaliola mjo\n\nWhen taking a power greater than 30 of a WordMorphism I (we?) get a ugly backtrace of a ValueError\n\n\n\n```\nsage: m = WordMorphism('a->ab,b->ba')\nsage: m^30\nMorphism from Words over Ordered Alphabet ['a', 'b'] to Words over Ordered Alphabet ['a', 'b']\nsage: m^31\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/usr/local/sage-4.3.1/devel/sage-test/<ipython console> in <module>()\n\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __pow__(self, exp)\n    698             res = (self * self) ** nexp\n    699             if over == 1:\n--> 700                 res *= self\n    701             return res\n    702             \n\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __mul__(self, other)\n    642         #TODO : Est-ce que c'est le comportement que l'on veut pour le produit \n    643         #par le morphisme vide? Voir lignes ci-haut.\n--> 644         return WordMorphism(dict((key, self(w)) for (key, w) in other._morph.iteritems()), codomain=self.codomain())\n    645     \n    646     def __pow__(self, exp):\n\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in <genexpr>((key, w))\n    642         #TODO : Est-ce que c'est le comportement que l'on veut pour le produit \n    643         #par le morphisme vide? Voir lignes ci-haut.\n--> 644         return WordMorphism(dict((key, self(w)) for (key, w) in other._morph.iteritems()), codomain=self.codomain())\n    645     \n    646     def __pow__(self, exp):\n\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __call__(self, w, order, datatype)\n    580             if isinstance(w, FiniteWord_class):\n    581                 length = sum(self._morph[a].length() * b for (a,b) in w.evaluation_dict().iteritems())\n--> 582                 return self.codomain()((x for y in w for x in self._morph[y]), length=length, datatype=datatype)\n    583             else:\n    584                 return self.codomain()((x for y in w for x in self._morph[y]), length=Infinity, datatype='iter')\n\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/words.pyc in __call__(self, data, length, datatype, **kwds)\n    269 \n    270         # The function _construct_word handles the construction of the words.\n--> 271         w = self._construct_word(**kwds)\n    272         self._check(w)\n    273         return w\n\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/words.pyc in _construct_word(self, data, length, datatype, caching)\n    471                 else:\n    472                     raise ValueError, \"not a correct value for length (%s)\" % length\n--> 473             w = cls(parent=self,iter=data,length=length)\n    474         else:\n    475             raise ValueError, \"Not known datatype\"\n\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/word_infinite_datatypes.pyc in __init__(self, parent, iter, length)\n    857             8\n    858         \"\"\"\n--> 859         super(WordDatatype_iter_with_caching,self).__init__(parent,iter,length)\n    860         # we use self._data for returning an iterator through __iter__;\n    861         # we use self._gen for caching\n/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/word_infinite_datatypes.pyc in __init__(self, parent, iter, length)\n    558         else:\n    559             self._len = length\n--> 560             self._data = itertools.islice(iter, length)\n    561 \n    562         self._parent = parent\n\nValueError: Stop argument for islice() must be a non-negative integer or None.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8139\n\n",
    "created_at": "2010-01-31T19:49:56Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Can not compute (very) high power of WordMorphism",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8139",
    "user": "vdelecroix"
}
```
Assignee: sage-combinat

CC:  slabbe fsaliola mjo

When taking a power greater than 30 of a WordMorphism I (we?) get a ugly backtrace of a ValueError



```
sage: m = WordMorphism('a->ab,b->ba')
sage: m^30
Morphism from Words over Ordered Alphabet ['a', 'b'] to Words over Ordered Alphabet ['a', 'b']
sage: m^31
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/usr/local/sage-4.3.1/devel/sage-test/<ipython console> in <module>()

/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __pow__(self, exp)
    698             res = (self * self) ** nexp
    699             if over == 1:
--> 700                 res *= self
    701             return res
    702             

/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __mul__(self, other)
    642         #TODO : Est-ce que c'est le comportement que l'on veut pour le produit 
    643         #par le morphisme vide? Voir lignes ci-haut.
--> 644         return WordMorphism(dict((key, self(w)) for (key, w) in other._morph.iteritems()), codomain=self.codomain())
    645     
    646     def __pow__(self, exp):

/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in <genexpr>((key, w))
    642         #TODO : Est-ce que c'est le comportement que l'on veut pour le produit 
    643         #par le morphisme vide? Voir lignes ci-haut.
--> 644         return WordMorphism(dict((key, self(w)) for (key, w) in other._morph.iteritems()), codomain=self.codomain())
    645     
    646     def __pow__(self, exp):

/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/morphism.pyc in __call__(self, w, order, datatype)
    580             if isinstance(w, FiniteWord_class):
    581                 length = sum(self._morph[a].length() * b for (a,b) in w.evaluation_dict().iteritems())
--> 582                 return self.codomain()((x for y in w for x in self._morph[y]), length=length, datatype=datatype)
    583             else:
    584                 return self.codomain()((x for y in w for x in self._morph[y]), length=Infinity, datatype='iter')

/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/words.pyc in __call__(self, data, length, datatype, **kwds)
    269 
    270         # The function _construct_word handles the construction of the words.
--> 271         w = self._construct_word(**kwds)
    272         self._check(w)
    273         return w

/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/words.pyc in _construct_word(self, data, length, datatype, caching)
    471                 else:
    472                     raise ValueError, "not a correct value for length (%s)" % length
--> 473             w = cls(parent=self,iter=data,length=length)
    474         else:
    475             raise ValueError, "Not known datatype"

/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/word_infinite_datatypes.pyc in __init__(self, parent, iter, length)
    857             8
    858         """
--> 859         super(WordDatatype_iter_with_caching,self).__init__(parent,iter,length)
    860         # we use self._data for returning an iterator through __iter__;
    861         # we use self._gen for caching
/usr/local/sage-4.3.1/local/lib/python2.6/site-packages/sage/combinat/words/word_infinite_datatypes.pyc in __init__(self, parent, iter, length)
    558         else:
    559             self._len = length
--> 560             self._data = itertools.islice(iter, length)
    561 
    562         self._parent = parent

ValueError: Stop argument for islice() must be a non-negative integer or None.
```


Issue created by migration from https://trac.sagemath.org/ticket/8139





---

archive/issue_comments_071567.json:
```json
{
    "body": "I am adding a comment so that I will see it in the list of ticket I am involved (I was not seeing it before).",
    "created_at": "2010-04-12T09:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8139#issuecomment-71567",
    "user": "slabbe"
}
```

I am adding a comment so that I will see it in the list of ticket I am involved (I was not seeing it before).



---

archive/issue_comments_071568.json:
```json
{
    "body": "The example morphism,\n\n\n```\nsage: m = WordMorphism('a->ab,b->ba')\n```\n\n\ndoubles the length of its input on every application. So,\n\n\n```\nsage: m^31\n```\n\n\nwill double the length of 'a' 31 times. That's just enough so that the length of the result overflows a signed integer, and thus it complains, \"Stop argument for islice() must be a non-negative integer...\"",
    "created_at": "2012-01-09T03:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8139#issuecomment-71568",
    "user": "mjo"
}
```

The example morphism,


```
sage: m = WordMorphism('a->ab,b->ba')
```


doubles the length of its input on every application. So,


```
sage: m^31
```


will double the length of 'a' 31 times. That's just enough so that the length of the result overflows a signed integer, and thus it complains, "Stop argument for islice() must be a non-negative integer..."
