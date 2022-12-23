# Issue 4189: hmm documentation buglet

Issue created by migration from https://trac.sagemath.org/ticket/4189

Original creator: mabshoff

Original creation time: 2008-09-24 10:56:05

Assignee: was

mapb reported in http://groups.google.com/group/sage-devel/t/8109b386f0e94251

```
The fourth argument in the following routine is called 
"emission_symbols", while the INPUTS section reports "emission_state". 
hmm.DiscreteHiddenMarkovModel(A, B, pi=None, emission_symbols=None, 
name=None, normalize=True) 
n 
    INPUTS: 
        A  -- square matrix of doubles; the state change probabilities 
        B  -- matrix of doubles; emission probabilities 
        pi -- list of floats; probabilities for each initial state 
        emission_state -- list of B.ncols() symbols (just used for 
printing) 
        name -- (optional) name of the model 
        normalize -- (optional; default=True) whether or not to 
normalize 
                     the model so the probabilities add to 1 
```



---

Attachment


---

Comment by mabshoff created at 2008-09-24 23:31:58

Looks good to me, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-25 00:14:25

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-25 00:14:25

Resolution: fixed
