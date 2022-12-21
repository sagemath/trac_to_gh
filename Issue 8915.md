# Issue 8915: improve documentation on combinat.dyck_words

Issue created by migration from Trac.

Original creator: zabrocki

Original creation time: 2010-05-07 16:08:33

Assignee: mvngu

CC:  sage-combinat

Keywords: dyck_words

documentation in several functions are missing description

```
    def associated_parenthesis(self, pos):
        """
        EXAMPLES::
        
            sage: DyckWord([1, 0]).associated_parenthesis(0)
            1
```


Working on patch


---

Attachment

Documentation changes to combinat/dyck_word.py


---

Comment by zabrocki created at 2010-05-08 17:28:57

Changing assignee from mvngu to zabrocki.


---

Comment by zabrocki created at 2010-05-08 17:51:43

Changing status from new to needs_review.


---

Attachment


---

Attachment

The patch [trac8915.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8915/trac8915.2.patch) is the same as [trac8915.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8915/trac8915.patch), but with the ticket number and a commit message. Changes proposed by the reviewer patch:

 * Explain the input wherever possible.
 * Don't go over 79 characters per line wherever possible. This is in accordance with the style guide [PEP 008](http://www.python.org/dev/peps/pep-0008/).
 * Cross reference functions wherever possible.
 * Some typo fixes.
 
So only my patch needs review by anyone but me. If my reviewer patch is OK, then the whole ticket is good to go.


---

Comment by slabbe created at 2010-05-13 13:19:33

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2010-05-13 13:19:33

All tests still passed in `dyck_word.py`. Documentation coverage is still 100%. Documentation builds fine without syntax warning. ...and the documentation of the file was enhanced.

Positive review.


---

Comment by mvngu created at 2010-05-17 06:49:33

Resolution: fixed
