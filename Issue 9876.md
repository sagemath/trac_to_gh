# Issue 9876: Add is_sturmian_factor, is_tangent methods for finite words

Issue created by migration from https://trac.sagemath.org/ticket/9877

Original creator: tmonteil

Original creation time: 2010-09-08 21:05:26

Assignee: tmonteil

CC:  sage-combinat abmasse slabbe

Add 3 methods to the `sage/combinat/words/finite_word.py`:

 1. sturmian_desubstitute_as_possible
 1. is_sturmian_factor
 1. is_tangent


```
sage: w = Word('01110110110111011101',alphabet='01')
sage: w.is_tangent()                  
True
```



---

Comment by tmonteil created at 2010-09-24 16:17:26

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-10-01 18:31:44

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-10-01 18:31:44

I'm testing your patch in the next two hours. Before testing it explicitly, just some comments:

 1. Could you add a reference where one can find the proof that a word is finite sturmian if and only if you can desubstitute it to the empy word?
 1. As I told you when you were in Montreal, I think I prefer the name `is_finite_sturmian` (or just `is_sturmian`) over the name  `is_sturmian_factor`. I feel that the last one implies an argument like in `w.is_sturmian_factor(u)` and it seems to be used in many articles (just googling it, you find a big list).
 1. Not very important, but there are two comment `# print <something>` that should be removed from the code in the function `is_sturmian_factor`.

I'm waiting for sage-combinat to install and I'll test and look more thoroughly at your code.


---

Comment by abmasse created at 2010-10-01 19:59:05

There is another problem with your function:

```
TypeError: Your word must be defined on a binary alphabet
sage: 
sage: 
sage: Word('ababab', alphabet='ab').is_sturmian_factor()
True
sage: Word('ababab').is_sturmian_factor()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/alexandre/Applications/sage/devel/sage-combinat/sage/combinat/words/<ipython console> in <module>()

/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/words/finite_word.pyc in is_sturmian_factor(self)
   4197         - Thierry Monteil
   4198         """
-> 4199         return self.sturmian_desubstitute_as_possible().is_empty()
   4200 
   4201 

/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/words/finite_word.pyc in sturmian_desubstitute_as_possible(self)
   4086         W = self.parent()
   4087         if (W.size_of_alphabet() != 2):
-> 4088             raise TypeError, 'Your word must be defined on a binary alphabet'
   4089         alphabet = W.alphabet()
   4090         if self.is_empty():

TypeError: Your word must be defined on a binary alphabet
```


I think this shouldn't be the case. In fact, this is interesting, because it raises another problem I had when working on another patch. What I suggest is that you could first verify if the parent has size 2 and, if it's not the case, you check if its *real* alphabet has size 2 by using the expression
len(set(self)) == 2

I think the clean solution would be to replace the deprecated function `alphabet()` by a new one that would compute the *real alphabet* in question, so that there would be two kinds of alphabet:

 1. The one corresponding to the parent of the word (for instance `aaab` might be a word defined on the alphabet `{a,b,c}`).
 2. The one corresponding to the alphabet realized by the word `Alph(aaab) = {a,b}`

The first one is called by `w.parent().alphabet()` while the second one would be obtained from `w.alphabet()`. But this is for another ticket.

What I suggest is that you simply add the `len(set(w)) == 2` condition to your code and we'll clean it eventually.


---

Comment by abmasse created at 2010-10-01 20:32:00

I might be wrong, but it seems that the code for the `desubstitute_as_possible` is long and should be cut into smaller functions that maybe already exist in Sage. Could you provide me the pseudocode of the function?


---

Comment by tmonteil created at 2010-10-01 22:53:03

Replying to [comment:2 abmasse]:
>  1. Could you add a reference where one can find the proof that a word is finite sturmian if and only if you can desubstitute it to the empy word?

Sure. This is a well known result (though there are many variants of this idea, i do not know whether this exact one is written somewhere), but i will add at least in the Arnoux chapter of the Pytheas Fogg book. I guess i will also add a reference to a recent article of Smillie and Ulcigrai which explains this in a nice way.


---

Comment by tmonteil created at 2010-10-01 22:56:10

Replying to [comment:2 abmasse]:
>  2. Not very important, but there are two comment `# print <something>` that should be removed from the code in the function `is_sturmian_factor`.

ok.


---

Comment by tmonteil created at 2010-10-01 23:21:59

Replying to [comment:2 abmasse]:
>  2. As I told you when you were in Montreal, I think I prefer the name `is_finite_sturmian` (or just `is_sturmian`) over the name `is_sturmian_factor`. I feel that the last one implies an argument like in `w.is_sturmian_factor(u)` and it seems to be used in many articles (just googling it, you find a big list).

Actually, those words are the balanced one, but the method `is_balanced` already exists with a slower (quadratic complexity) implementation (that implements the definition of the balanced word). The first name of my method was `is_factor_of_a_sturmian_word`, which describes precisely the method but is too long.

I do not really like `is_finite_sturmian`, and i am completely opposed to the name `is_sturmian` because the word Sturmian is reserved for infinite words (and this is not the role of sage to change historical notations). Also `is_finite_sturmian` will not be well positioned in the automatic completion.

Another possibility could be to add a parameter `algorithm` with values `default`, `desubstitution` or `definition` and merge this method into the existing slow method `is_balanced` (with the `desubstitution` algorithm only applying for 1-balanced words).


---

Comment by abmasse created at 2010-10-01 23:38:25

Replying to [comment:7 tmonteil]:

> 
> Another possibility could be to add a parameter `algorithm` with values `default`, `desubstitution` or `definition` and merge this method into the existing slow method `is_balanced` (with the `desubstitution` algorithm only applying for 1-balanced words).

This is a very good idea. I think you should do it.


---

Comment by tmonteil created at 2010-10-02 00:32:28

Replying to [comment:3 abmasse]:
> There is another problem with your function:

```
[cut]
TypeError: Your word must be defined on a binary alphabet
```

> 
> I think this shouldn't be the case. In fact, this is interesting, because it raises another problem I had when working on another patch. What I suggest is that you could first verify if the parent has size 2 and, if it's not the case, you check if its *real* alphabet has size 2 by using the expression
> len(set(self)) == 2
> 
> I think the clean solution would be to replace the deprecated function `alphabet()` by a new one that would compute the *real alphabet* in question, so that there would be two kinds of alphabet:
> 
>  1. The one corresponding to the parent of the word (for instance `aaab` might be a word defined on the alphabet `{a,b,c}`).
>  2. The one corresponding to the alphabet realized by the word `Alph(aaab) = {a,b}`
> 
> The first one is called by `w.parent().alphabet()` while the second one would be obtained from `w.alphabet()`. But this is for another ticket.
> 
> What I suggest is that you simply add the `len(set(w)) == 2` condition to your code and we'll clean it eventually.


Since it is explained in the documentation, this is not a bug but a feature ;)

I was thinking about this alphabet problem, and i am willing to write a ticket about that issue. I think that such a decision should be made for the whole word directory, with its whole community. Here are some bits.

If i start to do such tests in such a method, then almost every method of the FiniteWords class will have to do it as well, and the faster parent().alphabet() method will become useless. So there is a problem of code replication.

Another problem is that a test like `len(set(w)) == 2` takes probably a linear time whereas `size_of_alphabet` is just looking into the parent, which is constant time. 

Some programmer (user) should know where his/her words are living and should be warned if not. Making "friendly code" does not mean to pass over dirty programmer's inconsistencies, because then it won't detect the clean programmer's mistakes anymore. Fore those lazy ways of programming, we can imagine a global option which tells how the methods should care about the alphabet, so that both kinds of behavior are possible.

As for me, this may look Bourbachist (in particular not `bash`-ist ;), but i would like the empty word defined on a 2-letter alphabet to be recognized as a factor of a Sturmian word and not necessarily the empty word defined on a three letter alphabet (or at least to be warned if i do so). This may be, a contrario, an argument to make a difference between `is_sturmian_factor` (or `is_finite_sturmian`) and `is_balanced(1)`.


If in some very few occasion, the user will indeed need to use such a method on some words defined on some non-two-letter alphabet, but then there should be some general coerce methods like `redefine_alphabet` or `minimize_alphabet_to_actually_used_letters` that s-he can use in his/her code.

Another example of why the alphabet question deals with the whole `word` directory, and why there should be an overall policy is the following:


```
sage: words.LowerMechanicalWord(1/sqrt(2)).parent()
Words
sage: words.CharacteristicSturmianWord(1/sqrt(2)).parent()
Words over Ordered Alphabet [0, 1]
```



---

Comment by slabbe created at 2010-10-15 22:15:00

> The first one is called by `w.parent().alphabet()` while the second one would be obtained from `w.alphabet()`. But this is for another ticket.
> 
> What I suggest is that you simply add the `len(set(w)) == 2` condition to your code and we'll clean it eventually.

I think this is a very good suggestion.

Sébastien


---

Comment by abmasse created at 2010-11-13 16:07:59

Hi, Thierry !

Sorry if I haven't been available lately (busy, you know, the usual justification...).

If I'm not mistaken, there were last minor issues with your ticket that haven't been completely solved. To recap:

  1. Cleaning some commented code.
  1. Adding the `len(set(w)) == 2` condition. I understand your point of view that this should be done by many other functions in Sage, but for now, it will be cleaner if we do so.
  1. Finally, I agree with you about keeping the name `is_sturmian_factor`.
  1. Providing a reference for the theorem that desubstituting as possible to the empty word is equivalent to being Sturmian.
 
This is pretty much it!


---

Comment by tmonteil created at 2010-12-29 15:58:44

We were on strike my friend.


---

Comment by tmonteil created at 2010-12-29 16:02:29

Tested on Sage 4.6


---

Attachment

Hi Alexandre,

i started to work back on this ticket. This new patch is supposed to solve your four points. 

Since the `is_tangent()` method can now be applied to a word with more than 2 letters, i added a protection in the `FiniteWordPath_all` class into the file `paths.py` so that `is_tangent()` could not be applied for such word paths. Indeed, there is an extended definition for them, which is not yet written (see the paper).

Also, concerning a previous comment on using existing sage code, i looked for some "run" method and the only similar code i found was the `_delta_iterator()` method in the `Word_class` class. I tried to use it, but it seems that the use of the `groupby` itertool followed by `len` makes a slower code:


```
from itertools import groupby

def runs_groupby(self):
    for letter, run in groupby(self):
        yield letter, len(list(run))

def runs_homemade(self):
    try:
        previous_letter = self[0]
    except IndexError:
        return
    current_run_length = 0
    for i in self:
        if i == previous_letter:
            current_run_length += 1
        else:
            yield previous_letter , current_run_length
            current_run_length = 1
            previous_letter = i
    yield previous_letter , current_run_length

timeit('for i in runs_groupby(words.FibonacciWord()[:1000]):\n    print i')

timeit('for i in runs_homemade(words.FibonacciWord()[:1000]):\n    print i')

```


The first takes 28.6 ms per loop whereas the second takes 18.2 ms per loop. The problem is that the first method, though more low-level, is like passing twice on the word, which seems to be slower than the second (high-level) one-pass method.

Ciao,
Thierry


---

Comment by tmonteil created at 2010-12-29 16:56:11

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2011-01-27 12:13:14

Please fix the *5 test errors*. Four of them are the same :

AttributeError: 'WordGenerator' object has no attribute 'KolakoskiWord'

See the report of the patchbot.


---

Comment by slabbe created at 2011-01-28 15:00:26

Salut Thierry,

1.

> Since the `is_tangent()` method can now be applied to a word with more than 2 letters, i added a protection in the `FiniteWordPath_all` class into the file `paths.py` so that `is_tangent()` could not be applied for such word paths. Indeed, there is an extended definition for them, which is not yet written (see the paper).

Why? Can you explain more? I don't think the protection is needed.

2. 

The patch is having the following lines::


```
w_isolated = W(l_isolated,datatype='letter') #the word associated to the isolated letter
w_running = W(l_running,datatype='letter') #the word associated to the running letter
```


I remember I suggested you to use datatype = 'letter'. But I realized today that this was supported only for the old sage words objects saved in the pickle jar. So, by introducing it now in this patch, we would have to keep it. So we need to make a decision if we keep it or not. If we don't keep it, you can do the following instead:


```
w_isolated = W([l_isolated]) #the word associated to the isolated letter
w_running = W([l_running]) #the word associated to the running letter
```


3. I think we should redefine the function alphabet for finite words and return the letter occuring in the word and caching the result (I can post a patch for this). And so, the function `is_tangent` could look if this method return a two letter alphabet when the parent don't.


---

Comment by slabbe created at 2011-01-28 15:00:26

Changing status from needs_review to needs_info.


---

Comment by slabbe created at 2011-03-16 18:55:30

I get the following error while building the documentation :


```
/Users/slabbe/Applications/sage-4.6.2/local/lib/python2.6/site-packages/sage/combinat/words/finite_word.
py:docstring of sage.combinat.words.finite_word.FiniteWord_class.is_sturmian_factor:47: (ERROR/3) Unexpected indentation.                                                                                      
```



---

Comment by chapoton created at 2011-06-12 07:59:28

Trying to help the build bot

Apply trac_9877_words_sturmian_desubstitution_attempt_2-tm.patch


---

Comment by vdelecroix created at 2012-03-23 23:38:37

Hello,

Some comments to motivate the author of the patch.

1) The problem with datatype=letter may be fixed by the following. At the begining of the function, create a dictionnary "word_from_letter" with keys the two letters and values as words of length 1. It is the best way to do as a call to the parent for the creation of an object is always time consuming. With that done, all tests pass on sage-5.0.beta7.

2) It would be nice to put a "reverse engineering" example (random or not) as follows:

```
sage: s1 = WordMorphism('a->ab,b->b')
sage: s2 = WordMorphism('a->ba,b->b')
sage: s3 = WordMorphism('a->a,b->ba')
sage: s4 = WordMorphism('a->a,b->ab')
sage: W=Words('ab')
sage: w=W('ab')
sage: for i in xrange(8): w = choice([s1,s2,s3,s4])(w)   
sage: w
word: aabaaabaabaaabaabaabaaabaabaabaaabaabaaa...
sage: w.is_sturmian_factor()
True
```


3) There is still the doctest problem mentionned in comment: 17

It would be great to have this patch integrated in sage-5.0!


---

Comment by vdelecroix created at 2013-02-15 17:14:13

*ping*

It would be great to have this patch integrated in sage-5.7!


---

Comment by chapoton created at 2013-02-15 20:27:04

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2013-02-15 20:27:04

I have made the necessary changes for 1) and 3). 

Should I incorporate 2) ?


---

Comment by vdelecroix created at 2013-02-15 21:01:35

Replying to [comment:21 chapoton]:
> I have made the necessary changes for 1) and 3). 
> 
> Should I incorporate 2) ?

I would. You do not like the example ?


---

Comment by chapoton created at 2013-02-15 21:11:00

Here it is. I had to change the result to

```
word: abaaabaaabaabaaabaaabaabaaabaabaaabaaaba...
```

for the doctest to pass.

Please review.


---

Comment by vdelecroix created at 2013-02-15 22:15:06

Some last docstring comments:

* for expressions that refer to Python variables or reserved names (in particular self) you may use double quotes (at some places it is ok and at some other it is not)
* line 5179: "desubstitution consist" -> "desubstitution consists"
* lines 5190, 5340, 5419: self is *not* a part of the input
* is_tangent doc: the word tangent, where it is defined, must be bold (put the word between two *). The definition is not very english, I suggest: A binary word is said to be *tangent* if it can appear in infintely many cutting sequences of a smooth curve, where each cutting sequence is observed on a progressively smaller grid.

Best,
Vincent


---

Comment by chapoton created at 2013-02-18 09:57:00

New patch, with previous points corrected. Please review.


---

Comment by chapoton created at 2013-03-05 19:30:35

Vincent, do you think that this ticket is ready to go ?


---

Comment by vdelecroix created at 2013-03-05 21:57:35

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2013-03-05 21:57:35

Changing keywords from "" to "sturmian word, tangent word".


---

Comment by vdelecroix created at 2013-03-05 21:57:35

Yes it is. Thanks Frédéric for the finalization !


---

Comment by jdemeyer created at 2013-03-07 08:07:46

Please clarify which patch(es) must be applied.


---

Comment by jdemeyer created at 2013-03-07 08:07:46

Changing status from positive_review to needs_info.


---

Comment by chapoton created at 2013-03-07 08:52:02

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2013-03-07 08:52:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-13 14:13:04

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-03-13 14:13:04

There is a problem building the documentation:

```
[combinat ] /release/merger/sage-5.9.beta0/local/lib/python2.7/site-packages/sage/combinat/words/finite_word.py:docstring of sage.combinat.words.finite_word:47: WARNING: Enumerated list ends without a blank line; unexpected unindent.
```



---

Attachment

I have corrected the doc, back to positive review


---

Comment by chapoton created at 2013-03-13 15:35:22

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-03-20 14:43:23

Resolution: fixed
