# Issue 8139: Can not compute (very) high power of WordMorphism

Issue created by migration from https://trac.sagemath.org/ticket/8139

Original creator: vdelecroix

Original creation time: 2010-01-31 19:49:56

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



---

Comment by slabbe created at 2010-04-12 09:19:31

I am adding a comment so that I will see it in the list of ticket I am involved (I was not seeing it before).


---

Comment by mjo created at 2012-01-09 03:41:59

The example morphism,


```
sage: m = WordMorphism('a->ab,b->ba')
```


doubles the length of its input on every application. So,


```
sage: m^31
```


will double the length of 'a' 31 times. That's just enough so that the length of the result overflows a signed integer, and thus it complains, "Stop argument for islice() must be a non-negative integer..."
