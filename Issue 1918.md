# Issue 1918: Matrices that are printed are not aligned

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-01-25 01:27:06

Assignee: was

CC:  hivert nthiery

The rows of matrices in a list right now do not line up when printed, even though carriage returns are inserted as if they should line up.  That means all the matrices look *very* messed up when printing a list of matrices.

In the command line:


```
sage: list(MatrixSpace(GF(2),2))

[[0 0]
[0 0],
 [1 0]
[0 0],
 [0 1]
[0 0],
 [0 0]
[1 0],
 [0 0]
[0 1],
 [1 1]
[0 0],
 [1 0]
[1 0],
 [1 0]
[0 1],
 [0 1]
[1 0],
 [0 1]
[0 1],
 [0 0]
[1 1],
 [1 1]
[1 0],
 [1 1]
[0 1],
 [1 0]
[1 1],
 [0 1]
[1 1],
 [1 1]
[1 1]]
```


In the notebook, it's worse.  Each matrix is chopped in half and continues at the start of the next line.  This gives the appearance of matrices that are not part of the list (one row of one matrix and another row from a different matrix).


```
[[0 0]
[0 0], [1 0]
[0 0], [0 1]
[0 0], [0 0]
[1 0], [0 0]
[0 1], [1 1]
[0 0], [1 0]
[1 0], [1 0]
[0 1], [0 1]
[1 0], [0 1]
[0 1], [0 0]
[1 1], [1 1]
[1 0], [1 1]
[0 1], [1 0]
[1 1], [0 1]
[1 1], [1 1]
[1 1]]
```


An example of better output would be:


```
sage: list(MatrixSpace(GF(2),2))

[
[0 0]
[0 0],

[1 0]
[0 0],

[0 1]
[0 0],

[0 0]
[1 0],

[0 0]
[0 1],

[1 1]
[0 0],

[1 0]
[1 0],

[1 0]
[0 1],

[0 1]
[1 0],

[0 1]
[0 1],

[0 0]
[1 1],

[1 1]
[1 0],

[1 1]
[0 1],

[1 0]
[1 1],

[0 1]
[1 1],

[1 1]
[1 1]]
```


Or even better:

```
[
[0 0]  [1 0]  [0 1]  [0 0]  [0 0]  [1 1]  
[0 0], [0 0], [0 0], [1 0], [0 1], [0 0], 

[1 0]  [1 0]  [0 1]  [0 1]  [0 0]  [1 1]
[1 0], [0 1], [1 0], [0 1], [1 1], [1 0],

[1 1]  [1 0]  [0 1]  [1 1]
[0 1], [1 1], [1 1], [1 1]
]
```




---

Comment by was created at 2008-01-25 02:05:35

This is another example of something that can probably only ? be addressed
by changing the Python displayhook thing.  That's completely reasonable.

William


---

Comment by malb created at 2009-01-22 22:35:41

Changing type from defect to enhancement.


---

Comment by wcauchois created at 2009-08-05 01:39:41

I did some work to alleviate this issue, including implementing a new displayhook. The displayhook looks at every list, and if any object's repr spans multiple lines it prints the whole list out in a special format. See for yourself:


```
sage: list(MatrixSpace(GF(2),2))
[
[0 0]  [1 0]  [0 1]  [0 0]  [0 0]  [1 1]  [1 0]  [1 0]  [0 1]  [0 1]
[0 0], [0 0], [0 0], [1 0], [0 1], [0 0], [1 0], [0 1], [1 0], [0 1],

[0 0]  [1 1]  [1 1]  [1 0]  [0 1]  [1 1]
[1 1], [1 0], [0 1], [1 1], [1 1], [1 1]
]
```


I discovered that IPython has a separate displayhook mechanism -- however, the Sage instance spawned for the notebook does not use IPython. Hence, my code has two separate paths. I tried to ensure that the behavior of the default displayhook would be maintained in any case. I do hope it doesn't break anything :).


---

Comment by jason created at 2009-09-17 09:49:09

This looks very, *very* nice.  It also leads to huge numbers of failures in doctests in the matrix directory, which would need to be cleaned up by someone in another patch on this ticket.


---

Comment by flawrence created at 2009-10-06 07:27:30

The patch doesn't just lead to doctest failures in the matrix directory - on my machine it seems to lead to the failure of every single doctest that produces output!  e.g.

```
File "/Applications/sage/devel/sage-1918/sage/algebras/algebra.py", line 29:
    sage: is_Algebra(R)
Expected:
    True
Got nothing
```

When running a test manually (i.e. typing it into a sage console), everything works as intended - the output matches the expected doctest result exactly.  So the patch seems to break the doctesting mechanism in some way.  I note that all of the output-producing tests in the new file displayhook.py pass their output through DH.print_obj() or similar.


---

Attachment

based on sage 4.2.1


---

Attachment

based on sage 4.3.alpha0; apply only this patch


---

Comment by wcauchois created at 2009-12-02 08:46:12

I think this is ready for review! The only doctest failure now is from sage/interfaces/maxima.py, but I'm pretty sure that has nothing to do with this patch (I saw it in the main branch of 4.3.alpha0 as well).


---

Comment by wcauchois created at 2009-12-02 08:46:12

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2009-12-02 17:26:06

Replying to [comment:6 wcauchois]:
> I think this is ready for review! The only doctest failure now is from sage/interfaces/maxima.py, but I'm pretty sure that has nothing to do with this patch (I saw it in the main branch of 4.3.alpha0 as well).

This is some very good piece of work ! However, I'm soory to say that but I think it is not general enough. In combinatorics, we have a lot of 2d objects (Ferrers diagram, Young tableau). Right now it is hardcoded in the patch that this hook only apply for a list of matrices. should'nt we add some plugin saying that a particular kind of objects are printed by a 2d diagram. Or maybe should we apply the hook allways ? Or for any objects whose __repr__ string contains a newline ? 

But maybe we should keep the for another patch. 

By the way and as a consequence, I don't think this has to do with linear algebra. 

Cheers,

Florent


---

Comment by hivert created at 2009-12-02 17:36:34

To be more specific, I'd like to be able to write thing like that

```
sage: class bla(): 
....:     def __init__(self, str): self.str=str
....:     def __repr__(self): return self.str
}}} 
And without patching displayhook, to get
{{{
sage: sage.misc.displayhook._check_tall_list_and_print(sys.stdout, [a,b])
[
       dsf
werew  sdf
sdfd , sf 
]
}}}
instead of...
{{{
sage: [bla("werew\nsdfd"), bla("dsf\nsdf\nsf")]
[werew
sdfd, dsf
sdf
sf]
}}}
I'm not sure what is the correct mechanism of plugin. should we add in the class a method called say `_repr_use2d_` ? 

Florent


---

Comment by jason created at 2009-12-02 17:40:01

Replying to [comment:7 hivert]:

> But maybe we should keep the for another patch. 

I agree.  Furthermore, this will let us shake out any unintended consequences or bugs in a narrow case before expanding to lots of combinatorics objects.

The patch has already waited a long time.  Unless the change you suggest is trivial (but it sounds like already there are questions about the design of your suggestion), I'd say if the patch is ready to go in, let it go in.


---

Comment by wcauchois created at 2009-12-02 20:21:00

Replying to [comment:7 hivert]:

I agree that there are many more cases where this type of list formatting could be useful, and indeed the code is general enough to work with any type of object whose repr spans multiple lines. The issue is simply choosing which lists to format specially (in print_obj()).

In one of my earlier iterations of the displayhook, I applied the special list formatting to every "tall" list. But when I ran testall I found that some objects just didn't work well with the formatting. So I think that applying the hook always is a mistake, and besides would introduce many more doctest headaches. Having objects "opt-in" by including a special field or method that tells the displayhook to use the special list formatting sounds like a good idea though.

This kind of work should definitely be done, but in another ticket. We will have to come to an agreement about these design issues. For now, let's get this patch into Sage.


---

Comment by hivert created at 2009-12-02 20:53:29

Replying to [comment:10 wcauchois]:
> In one of my earlier iterations of the displayhook, I applied the special list formatting to every "tall" list. But when I ran testall I found that some objects just didn't work well with the formatting. So I think that applying the hook always is a mistake, and besides would introduce many more doctest headaches. Having objects "opt-in" by including a special field or method that tells the displayhook to use the special list formatting sounds like a good idea though.

I even tried to apply it on **all** lists ! I can tell you that there are much more output that looks better with your modification than without. (see e.g. in  `sage/modular/arithgroup/`... I'm not sure doing it systematically is a mistake... But some objects have to adapt their output, and the way you decide to break a line or not is not always optimal (see e.g. the output of ` TabularUnifiedsage/modular/modsym/relation_matrix.py` in your patch.

 
> This kind of work should definitely be done, but in another ticket. We will have to come to an agreement about these design issues. For now, let's get this patch into Sage.

Agreed, this show that they are a lot of possible improvement in sage output routine. Thanks a lot for showing us how to do that. 

I'm waiting for the results of the tests to give you a positive review...


---

Comment by hivert created at 2009-12-02 20:56:56

Everything is ok ! Positive review. (This is my 11th review for 4.3 :-)


---

Comment by hivert created at 2009-12-02 20:58:55

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-12-03 21:19:09

I've a request concerning this ticket: You manage to hijack ipython's printer but not python's one.

```
sage: [matrix(2,2)] * 3
[
[0 0]  [0 0]  [0 0]
[0 0], [0 0], [0 0]
]
sage: print([matrix(2,2)] * 3)
[[0 0]
[0 0], [0 0]
[0 0], [0 0]
[0 0]]
```

Is it trivial to solve this ? Or should I open a new ticket ?

Cheers,

Florent


---

Comment by wcauchois created at 2009-12-04 03:07:17

Replying to [comment:14 hivert]:
> I've a request concerning this ticket: You manage to hijack ipython's printer but not python's one.
> {{{
> sage: [matrix(2,2)] * 3
> [
> [0 0]  [0 0]  [0 0]
> [0 0], [0 0], [0 0]
> ]
> sage: print([matrix(2,2)] * 3)
> [[0 0]
> [0 0], [0 0]
> [0 0], [0 0]
> [0 0]]
> }}}
> Is it trivial to solve this ? Or should I open a new ticket ?

You raise an interesting point Florent. The problem here is that Python's displayhook mechanism only affects the output from the interpreter, not the behavior of the print statement. In fact, the displayhook uses the print statement to output values, so if the print statement used the displayhook it would be bad.

AFAIK, there is no way to hook into the print statement. All it does is write the object's repr to sys.stdout. And now we run into the limitation that drove us to use a displayhook in the first place: you can't change the way repr behaves for lists.

The only thing I can suggest is to add a function, say, `format_list_of_matrices()` to the matrix library so that your code becomes:

```
sage: print format_list_of_matrices([matrix(2,2) * 3])
```

But I feel like such a facility would be not at all obvious for end-users. Unless they notice how crappy a list of matrices looks when its `print`ed and root around the documentation for answers.


---

Comment by mhansen created at 2009-12-06 09:20:03

Resolution: fixed
