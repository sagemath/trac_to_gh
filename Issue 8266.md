# Issue 8266: Improve documentation for word objects

Issue created by migration from https://trac.sagemath.org/ticket/8266

Original creator: slabbe

Original creation time: 2010-02-14 22:35:51

Assignee: slabbe

CC:  abmasse

Documentation of words and word objects contains only pickle tests and lacks good examples :


```
sage: words?
...
Docstring:
    
        A class consisting of constructors for several famous words.
        
        TESTS::
    
            sage: from sage.combinat.words.word_generators import WordGenerator
            sage: MyWordBank = WordGenerator()
            sage: type(loads(dumps(MyWordBank)))
            <class 'sage.combinat.words.word_generators.WordGenerator'>
```

    
        

```
sage: w = Word(range(5))
sage: w?
...
Docstring:
    
        TESTS::
    
            sage: w = Word([0,1,1,0])
            sage: w == loads(dumps(w))
            True
```

        




---

Attachment

Depends on #7619.


---

Comment by slabbe created at 2010-02-14 22:39:55

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-03-02 10:19:37

#7619 now have a positive review... so this patch can now get reviewed


---

Comment by abmasse created at 2010-03-03 21:11:37

Looked at the patch. Since it is a documentation-only patch, all tests passed. I made sure that the patch of ticket #7619 was applied first. I still made a few minor changes.

1. I replaced "pyhon" by "Python" everywhere I found it.

2. I added ":" after a NOTE block that was not appearing in the documentation.

3. I replaced strange unicode characters by " at the end of Sébastien's patch.

4. I replaced the latex output of "w." by a code-font "w."

If Sébastien agrees with my changes, I allow him to set the ticket to "positive review".


---

Attachment

Doc fixes -- apply on top of Sébastien's patch


---

Comment by slabbe created at 2010-03-03 23:32:30

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2010-03-03 23:32:30

Thanks for the review Alex. I don't know where those strange characters came from... I added one patch to fix two of those characters (I really wanted ```` not ").

Since I my patch fix only two characters in the doc and because I agree with your changes and because your gave a positive review to my first patch, I think I can change the status of this ticket to positive review.


---

Attachment

Applies over the two precedent patches.


---

Comment by mhansen created at 2010-03-06 08:30:51

Resolution: fixed
