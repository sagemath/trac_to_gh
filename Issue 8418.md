# Issue 8418: Reduced Rauzy graph

Issue created by migration from Trac.

Original creator: jleroy

Original creation time: 2010-03-02 13:06:20

Assignee: jleroy

CC:  abmasse slabbe

Adding the function reduced_rauzy_graph in word.py


---

Comment by jleroy created at 2010-03-03 13:51:27

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-03-03 14:34:25

Hello Julien ! Thanks for this new function that will be really helpful ! I have some minor comments, though.

1. When using the notation `u[i,j]` with Latex formatting, it is better not to put `[i,j]` in index position.

2. There is a typo in IMPUT.

3. Since the output is a directed graph, I would put "digraph" instead of "a graph". The "a" is not necessary and "digraph" is more precise.

4. You should put some text between your example blocks, to explain what you're doing and what you want to show. For instance, between blocks 1 and 2, you could write "For the Fibonacci word..." and between blocks 2 and 3, something like "It works also for periodic words.". Note that this is optional, it just helps the user to understand how you would use the function.

Short of that, your code looks good. Next time will probably be a positive review !


---

Comment by abmasse created at 2010-03-03 14:34:25

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2010-03-03 14:52:14

I am adding some more comments :

5. There is two blankline after EXAMPLES:: (one is enough).

6. The last :: is not necessary.

7. I would replace the UNICODE characters in references by simple ascii characters.

8. I would put the line "# In this case, the Rauzy graph is simply a cycle." on the line after inside the indentation.

9. I would try to remove the utilisation of the function "Word" inside of the function. This creates a dependance that we want to avoid.

Sébastien


---

Comment by slabbe created at 2010-03-03 15:21:55

10. 

The following result seem broken. There should be 3 edges :


```
sage: w = words.FibonacciWord()[:100]
sage: h = w.reduced_rauzy_graph(9)
sage: for e in h.edges(): print e
(word: 001010010, word: 010010100, word: 010100)
(word: 010010100, word: 001010010, word: 10)
```


Once it is fixed. This example should be added to the documentation.


---

Comment by jleroy created at 2010-03-03 16:42:46

Adds reduced rauzy graph function


---

Comment by jleroy created at 2010-03-03 16:43:40

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-03-03 17:44:14

I just added a patch that mainly fixes doc issues. For instance, :: are necessary before sage block (not after). I put the INPUT block higher. I fixed the NOTE block. I changed + to * for words because it is more natural (`w^2` is defined but not `w*2`) one day it is possible that + stop to be defined...

To my eye, the ticket is ready for a positive review. I let Alex do a last review and change the status to positive review if he is fine with the ticket.

Good work,

Sébastien


---

Comment by slabbe created at 2010-03-03 18:20:41

Changing priority from minor to major.


---

Comment by abmasse created at 2010-03-03 19:55:13

There is maybe a last remark I have... Sorry if I'm being over-meticulous. While I was looking at the INPUT block, I noticed that "integer" was not a precise enough explanation of the parameter `n`.

Then I tried it on the word `aba` with `n = 0` and it yielded a graph of one vertex and two edges having labels `word: a` and `word: b`. Is that what we want ?

Anyway, the last thing that needs to be done would be to be more precise about `n`. Is it a positive integer (we don't want `0`) or a non negative integer (we want `0`) ? Moreover, we need to specify what `n` means. It is the order of the reduced rauzy graph, i.e. the length of the considered factors.

Julien, if you want to make the changes, make sure you create another patch that applies on top of Sébastien's.


---

Comment by jleroy created at 2010-03-04 16:18:30

Hello Alex. 
The answer that you got is correct. In the Rauzy graph of order 'n', vertices are factors of length 'n' and edges are factors of length 'n+1'. In your case, the unique vertex corresponds to the empty word and the letters 'a' and 'b' are the only words of length 1 in the word 'aba'. This corresponds exactly to the definition of Rauzy graph and in this case, the reduced Rauzy graph is the same. Actually, it will be the case for any word if you take n=0. 

I could change this INPUT but anyone using the reduced Rauzy graph knows the definition of Rauzy graph and it is clear in this one that 'n' represents the length of the factors. Therefore it is clear that n is non negative. What do you thing about?


---

Comment by abmasse created at 2010-03-05 00:48:50

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-03-05 00:48:50

I'm all right with the ticket as it is now. I added a small patch that give more details about the input of the function.

Great work, Julien !

Positive review.


---

Comment by abmasse created at 2010-03-05 12:02:10

Precision of the input field -- apply on top of the two first patches


---

Attachment

I just added a new patch for my review. I had forgotten the word "reduced" and I gave more details about the input. Still positive review !


---

Comment by mhansen created at 2010-03-06 09:37:09

Resolution: fixed
