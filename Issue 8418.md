# Issue 8418: Reduced Rauzy graph

archive/issues_008418.json:
```json
{
    "body": "Assignee: jleroy\n\nCC:  abmasse slabbe\n\nAdding the function reduced_rauzy_graph in word.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/8418\n\n",
    "created_at": "2010-03-02T13:06:20Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Reduced Rauzy graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8418",
    "user": "jleroy"
}
```
Assignee: jleroy

CC:  abmasse slabbe

Adding the function reduced_rauzy_graph in word.py

Issue created by migration from https://trac.sagemath.org/ticket/8418





---

archive/issue_comments_075433.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-03T13:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75433",
    "user": "jleroy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075434.json:
```json
{
    "body": "Hello Julien ! Thanks for this new function that will be really helpful ! I have some minor comments, though.\n\n1. When using the notation `u[i,j]` with Latex formatting, it is better not to put `[i,j]` in index position.\n\n2. There is a typo in IMPUT.\n\n3. Since the output is a directed graph, I would put \"digraph\" instead of \"a graph\". The \"a\" is not necessary and \"digraph\" is more precise.\n\n4. You should put some text between your example blocks, to explain what you're doing and what you want to show. For instance, between blocks 1 and 2, you could write \"For the Fibonacci word...\" and between blocks 2 and 3, something like \"It works also for periodic words.\". Note that this is optional, it just helps the user to understand how you would use the function.\n\nShort of that, your code looks good. Next time will probably be a positive review !",
    "created_at": "2010-03-03T14:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75434",
    "user": "abmasse"
}
```

Hello Julien ! Thanks for this new function that will be really helpful ! I have some minor comments, though.

1. When using the notation `u[i,j]` with Latex formatting, it is better not to put `[i,j]` in index position.

2. There is a typo in IMPUT.

3. Since the output is a directed graph, I would put "digraph" instead of "a graph". The "a" is not necessary and "digraph" is more precise.

4. You should put some text between your example blocks, to explain what you're doing and what you want to show. For instance, between blocks 1 and 2, you could write "For the Fibonacci word..." and between blocks 2 and 3, something like "It works also for periodic words.". Note that this is optional, it just helps the user to understand how you would use the function.

Short of that, your code looks good. Next time will probably be a positive review !



---

archive/issue_comments_075435.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-03T14:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75435",
    "user": "abmasse"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075436.json:
```json
{
    "body": "I am adding some more comments :\n\n5. There is two blankline after EXAMPLES:: (one is enough).\n\n6. The last :: is not necessary.\n\n7. I would replace the UNICODE characters in references by simple ascii characters.\n\n8. I would put the line \"# In this case, the Rauzy graph is simply a cycle.\" on the line after inside the indentation.\n\n9. I would try to remove the utilisation of the function \"Word\" inside of the function. This creates a dependance that we want to avoid.\n\nS\u00e9bastien",
    "created_at": "2010-03-03T14:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75436",
    "user": "slabbe"
}
```

I am adding some more comments :

5. There is two blankline after EXAMPLES:: (one is enough).

6. The last :: is not necessary.

7. I would replace the UNICODE characters in references by simple ascii characters.

8. I would put the line "# In this case, the Rauzy graph is simply a cycle." on the line after inside the indentation.

9. I would try to remove the utilisation of the function "Word" inside of the function. This creates a dependance that we want to avoid.

Sébastien



---

archive/issue_comments_075437.json:
```json
{
    "body": "10. \n\nThe following result seem broken. There should be 3 edges :\n\n\n```\nsage: w = words.FibonacciWord()[:100]\nsage: h = w.reduced_rauzy_graph(9)\nsage: for e in h.edges(): print e\n(word: 001010010, word: 010010100, word: 010100)\n(word: 010010100, word: 001010010, word: 10)\n```\n\n\nOnce it is fixed. This example should be added to the documentation.",
    "created_at": "2010-03-03T15:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75437",
    "user": "slabbe"
}
```

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

archive/issue_comments_075438.json:
```json
{
    "body": "Adds reduced rauzy graph function",
    "created_at": "2010-03-03T16:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75438",
    "user": "jleroy"
}
```

Adds reduced rauzy graph function



---

archive/issue_comments_075439.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-03T16:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75439",
    "user": "jleroy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075440.json:
```json
{
    "body": "Attachment [trac_8418_reduced_rauzy_graph-jl.patch](tarball://root/attachments/some-uuid/ticket8418/trac_8418_reduced_rauzy_graph-jl.patch) by jleroy created at 2010-03-03 16:43:40",
    "created_at": "2010-03-03T16:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75440",
    "user": "jleroy"
}
```

Attachment [trac_8418_reduced_rauzy_graph-jl.patch](tarball://root/attachments/some-uuid/ticket8418/trac_8418_reduced_rauzy_graph-jl.patch) by jleroy created at 2010-03-03 16:43:40



---

archive/issue_comments_075441.json:
```json
{
    "body": "Attachment [trac_8418_review-sl.patch](tarball://root/attachments/some-uuid/ticket8418/trac_8418_review-sl.patch) by slabbe created at 2010-03-03 17:38:50\n\nApplies over the precedent patch",
    "created_at": "2010-03-03T17:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75441",
    "user": "slabbe"
}
```

Attachment [trac_8418_review-sl.patch](tarball://root/attachments/some-uuid/ticket8418/trac_8418_review-sl.patch) by slabbe created at 2010-03-03 17:38:50

Applies over the precedent patch



---

archive/issue_comments_075442.json:
```json
{
    "body": "I just added a patch that mainly fixes doc issues. For instance, :: are necessary before sage block (not after). I put the INPUT block higher. I fixed the NOTE block. I changed + to * for words because it is more natural (`w^2` is defined but not `w*2`) one day it is possible that + stop to be defined...\n\nTo my eye, the ticket is ready for a positive review. I let Alex do a last review and change the status to positive review if he is fine with the ticket.\n\nGood work,\n\nS\u00e9bastien",
    "created_at": "2010-03-03T17:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75442",
    "user": "slabbe"
}
```

I just added a patch that mainly fixes doc issues. For instance, :: are necessary before sage block (not after). I put the INPUT block higher. I fixed the NOTE block. I changed + to * for words because it is more natural (`w^2` is defined but not `w*2`) one day it is possible that + stop to be defined...

To my eye, the ticket is ready for a positive review. I let Alex do a last review and change the status to positive review if he is fine with the ticket.

Good work,

Sébastien



---

archive/issue_comments_075443.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-03-03T18:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75443",
    "user": "slabbe"
}
```

Changing priority from minor to major.



---

archive/issue_comments_075444.json:
```json
{
    "body": "There is maybe a last remark I have... Sorry if I'm being over-meticulous. While I was looking at the INPUT block, I noticed that \"integer\" was not a precise enough explanation of the parameter `n`.\n\nThen I tried it on the word `aba` with `n = 0` and it yielded a graph of one vertex and two edges having labels `word: a` and `word: b`. Is that what we want ?\n\nAnyway, the last thing that needs to be done would be to be more precise about `n`. Is it a positive integer (we don't want `0`) or a non negative integer (we want `0`) ? Moreover, we need to specify what `n` means. It is the order of the reduced rauzy graph, i.e. the length of the considered factors.\n\nJulien, if you want to make the changes, make sure you create another patch that applies on top of S\u00e9bastien's.",
    "created_at": "2010-03-03T19:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75444",
    "user": "abmasse"
}
```

There is maybe a last remark I have... Sorry if I'm being over-meticulous. While I was looking at the INPUT block, I noticed that "integer" was not a precise enough explanation of the parameter `n`.

Then I tried it on the word `aba` with `n = 0` and it yielded a graph of one vertex and two edges having labels `word: a` and `word: b`. Is that what we want ?

Anyway, the last thing that needs to be done would be to be more precise about `n`. Is it a positive integer (we don't want `0`) or a non negative integer (we want `0`) ? Moreover, we need to specify what `n` means. It is the order of the reduced rauzy graph, i.e. the length of the considered factors.

Julien, if you want to make the changes, make sure you create another patch that applies on top of Sébastien's.



---

archive/issue_comments_075445.json:
```json
{
    "body": "Hello Alex. \nThe answer that you got is correct. In the Rauzy graph of order 'n', vertices are factors of length 'n' and edges are factors of length 'n+1'. In your case, the unique vertex corresponds to the empty word and the letters 'a' and 'b' are the only words of length 1 in the word 'aba'. This corresponds exactly to the definition of Rauzy graph and in this case, the reduced Rauzy graph is the same. Actually, it will be the case for any word if you take n=0. \n\nI could change this INPUT but anyone using the reduced Rauzy graph knows the definition of Rauzy graph and it is clear in this one that 'n' represents the length of the factors. Therefore it is clear that n is non negative. What do you thing about?",
    "created_at": "2010-03-04T16:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75445",
    "user": "jleroy"
}
```

Hello Alex. 
The answer that you got is correct. In the Rauzy graph of order 'n', vertices are factors of length 'n' and edges are factors of length 'n+1'. In your case, the unique vertex corresponds to the empty word and the letters 'a' and 'b' are the only words of length 1 in the word 'aba'. This corresponds exactly to the definition of Rauzy graph and in this case, the reduced Rauzy graph is the same. Actually, it will be the case for any word if you take n=0. 

I could change this INPUT but anyone using the reduced Rauzy graph knows the definition of Rauzy graph and it is clear in this one that 'n' represents the length of the factors. Therefore it is clear that n is non negative. What do you thing about?



---

archive/issue_comments_075446.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-05T00:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75446",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075447.json:
```json
{
    "body": "I'm all right with the ticket as it is now. I added a small patch that give more details about the input of the function.\n\nGreat work, Julien !\n\nPositive review.",
    "created_at": "2010-03-05T00:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75447",
    "user": "abmasse"
}
```

I'm all right with the ticket as it is now. I added a small patch that give more details about the input of the function.

Great work, Julien !

Positive review.



---

archive/issue_comments_075448.json:
```json
{
    "body": "Precision of the input field -- apply on top of the two first patches",
    "created_at": "2010-03-05T12:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75448",
    "user": "abmasse"
}
```

Precision of the input field -- apply on top of the two first patches



---

archive/issue_comments_075449.json:
```json
{
    "body": "Attachment [trac_8418_review-abm.patch](tarball://root/attachments/some-uuid/ticket8418/trac_8418_review-abm.patch) by abmasse created at 2010-03-05 12:03:53\n\nI just added a new patch for my review. I had forgotten the word \"reduced\" and I gave more details about the input. Still positive review !",
    "created_at": "2010-03-05T12:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75449",
    "user": "abmasse"
}
```

Attachment [trac_8418_review-abm.patch](tarball://root/attachments/some-uuid/ticket8418/trac_8418_review-abm.patch) by abmasse created at 2010-03-05 12:03:53

I just added a new patch for my review. I had forgotten the word "reduced" and I gave more details about the input. Still positive review !



---

archive/issue_comments_075450.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T09:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8418#issuecomment-75450",
    "user": "mhansen"
}
```

Resolution: fixed
