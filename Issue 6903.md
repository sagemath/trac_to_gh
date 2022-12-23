# Issue 6903: Function Word currently prevent the inheritance of Words_over_OrderedAlphabet

Issue created by migration from https://trac.sagemath.org/ticket/6903

Original creator: slabbe

Original creation time: 2009-09-07 22:44:17

Assignee: mhansen

CC:  saliola

Let


```
sage: W = Words('ab')
```


In the state of sage-4.1.1, the function `W.__call__` uses the function `Word`....but it should be the inverse. In fact, the code of the function `Word` contains code like :


```
[...]

    # Construct the word
    if datatype == 'list':
        w = FiniteWord_list(parent=parent,data=data)
    elif datatype == 'str':
        w = FiniteWord_str(parent=parent,data=data)
    elif datatype == 'tuple':
        w = FiniteWord_tuple(parent=parent,data=data)
    elif datatype == 'callable':
        if caching:
            if length is None or length is Infinity:
                cls = InfiniteWord_callable_with_caching
            else:
                cls = FiniteWord_callable_with_caching
        else:
            if length is None or length is Infinity:
                cls = InfiniteWord_callable
            else:
                cls = FiniteWord_callable
        w = cls(parent=parent,callable=data,length=length)

[...]
```


The problems come when someone wants to inherits the class `Words_over_OrderedAlphabet` to create, let say, a combinatorial classes of all paths (see #5038). Below, we would like the `__call__` function of `WordPaths_all` to creates words paths instances and not the usual words instances. I don't want to rewrite the `__call__` function for `WordPaths_all` since it could be the exact same thing as the one of `Words_over_OrderedAlphabet`.


```
class WordPaths_all(Words_over_OrderedAlphabet):
    r"""
    The combinatorial class of all paths, i.e of all words over
    an alphabet where each letter is mapped to a step (a vector).
    """
    def __init__(self, alphabet, steps):
        r"""
        INPUT:

        - ``alphabet`` - an ordered alphabet 

        - ``steps`` - an iterable (of same length as alphabet) of ordered vectors

        EXAMPLES::

[...]
```


One solution is that the current code of `Word` goes to `Words.__call__` and that the function `Word` simply creates the parent from the input alphabet and delegates the creation to the parent.


---

Comment by slabbe created at 2009-09-07 22:53:14

I just posted a patch which corresponds to the work around I recently was using. Something better could be done.

Dear Franco, I would like to discuss with you about it, and I could then implement something better.


---

Comment by slabbe created at 2009-09-13 12:48:34

Changing status from new to assigned.


---

Comment by slabbe created at 2009-09-13 12:48:34

Changing assignee from mhansen to slabbe.


---

Attachment

I just posted a patch which correspond to something better. All test pass in sage/combinat/words. I also tested the pickle jar using (from http://www.sagemath.org/doc/reference/sage/structure/sage_object.html) :


```
sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
```


I keep the 'needs work' label, because there is still something I want to check. In fact, the code that changes the class of a word from `Word_class` to `FiniteWord_class` when it reaches the end of the word might be updated as well here, but I can't figure out where is that code!!! Franco should remember that.


---

Comment by saliola created at 2009-09-16 20:55:55

I am including two patches here.

In `trac_6903_reviewer_patch_1.patch`, I made the following changes:

 1. I fixed the code that changes the class of a word `FiniteWord_class` when it reaches the end of the iterator.

 2. I changed `_classetype` to `_element_classes` since the method defines the classes of the elements of the parent.

 3. I also cleaned up the code for `_element_classes`.

 4. Both `Words_all.__call__` and `Words_all._construct_word` run `self._check`, so I am deleting the occurrence in `Words_all._construct_word`.

In `trac_6903_reviewer_patch_2.patch`, I changed the method `_element_classes` into an attribute (a `lazy_attribute`, actually). So it *is* the dictionary instead of returning the dictionary. I think it is a bad idea to re-create that dictionary every time a word is created.


---

Comment by saliola created at 2009-09-16 20:56:45

Apply on top of trac_6903_word_improve_constructor-sl.patch


---

Attachment

Apply on top of trac_6903_reviewer_patch_2.patch


---

Attachment

Modulo the changes in the reviewer patches, I give a positive review to Sébastien's patch.

Sébastien, can you review my patches?


---

Attachment

Applies over the precedent 3 patches.


---

Comment by slabbe created at 2009-09-17 18:07:40

I just added a patch that removes two lines now useless after Franco's changes.

All test passed in sage/combinat/words directory. Documentation builds w/o warnings. I am giving a positive review to Franco's changes. I let Franco change the status of the ticket since I posted the last patch.


---

Comment by saliola created at 2009-09-17 19:56:04

Thanks for catching those two lines Sébastien. Positive review.


---

Comment by mvngu created at 2009-09-18 02:50:06

Resolution: fixed


---

Comment by mvngu created at 2009-09-18 02:50:06

Merged patches in this order:

 1. `trac_6903_word_improve_constructor-sl.patch`
 1. `trac_6903_reviewer_patch_1.patch`
 1. `trac_6903_reviewer_patch_2.patch`
 1. `trac_6903_review_3-sl.patch`
