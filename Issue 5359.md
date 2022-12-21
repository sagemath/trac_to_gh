# Issue 5359: Block matrix viewing is broken

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-02-24 17:55:14

Assignee: cwitty

From sage-support:

Viewing block matrices "nicely" seems to be difficult in Sage. 

```
sage: A=matrix([This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro)) 
sage: B=matrix([This is the Trac macro *2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2-macro)) 
sage: C=matrix([This is the Trac macro *3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3-macro)) 
sage: D=matrix([This is the Trac macro *4* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#4-macro)) 
sage: BM=block_matrix([A,B,C,D]) 
sage: BM 
[1|2] 
[-+-] 
[3|4] 
```

Okay, this is fine but a little clunky.  Let's try something nicer: 

```
sage: show(BM) 
```

Upon which a dvi viewer opens up, unfortunately not a very nice one... 
and shows the block matrix with only a vertical dividing line, not a 
horizontal one! 
Okay, let's try the notebook: 


```
A=matrix([This is the Trac macro *1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1-macro)) 
B=matrix([This is the Trac macro *2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2-macro)) 
C=matrix([This is the Trac macro *3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3-macro)) 
D=matrix([This is the Trac macro *4* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#4-macro)) 

BM=block_matrix([A,B,C,D]);BM 

[1|2] 
[-+-] 
[3|4] 
}}} 

So far so good, but when I click "Typeset" to get a LaTeXed matrix... 
{{{
BM=block_matrix([A,B,C,D]);BM 

<html><span class="math">\left(\begin{array}{r|r} 
1 & 2 \\ 
3 & 4 
\end{array}\right)</span></html> 
}}} 
Which as you can see does NOT have any "blockiness" to it at all. 
Very pretty, but not a block matrix, at least not identifiably so. 


---

Comment by jhpalmieri created at 2009-02-24 19:48:32

I think this is partly a bug and partly a defect in jsmath: the `_latex_` method for matrices completely ignores any subdivisions in the rows, and this is a bug. The right way to do this would be to add `\hline` between the rows where you want lines, but jsmath doesn't seem to support this command.  It also seems to ignore the vertical line specifier in the array argument.

So I know how to fix this so that it works from the command line, but not from the notebook.  I'll attach a patch.

Any ideas on what to do in the notebook?


---

Attachment

(will have to be rebased against sage 3.4)


---

Comment by kcrisman created at 2009-02-25 01:41:56

I won't be able to review this in the near future but if it works this seems appropriate.  

According to the jsmath future features page, [http://www.math.union.edu/~dpvc/jsMath/future.html](http://www.math.union.edu/~dpvc/jsMath/future.html), one of the future goals is 

```
Add more control over entries in arrays and matrices (something like the array option control provided by WebTeX)
```

so perhaps this ticket should be closed once the command line piece is given a positive review, and then a new ticket opened and/or a report sent to the jsmath author.  In any case we should at least have Sage as one of the sites using jsmath on his gallery!  

There _is_ an example of a pseudo-block matrix in his examples section, [http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html](http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html) Exercise 18.42.  I don't know if that would be a satisfactory solution, though.


---

Comment by jhpalmieri created at 2009-02-25 20:31:34

Replying to [comment:2 kcrisman]:

> There _is_ an example of a pseudo-block matrix in his examples section, 
> [http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html](http://www.math.union.edu/~dpvc/jsMath/examples/TeXbook18x.html) Exercise 18.42.  I 
> don't know if that would be a satisfactory solution, though.

I don't know if it is satisfactory, either, but I couldn't come up with anything better, so I've implemented this for the notebook version.  This ignores repeated subdivisions, because I couldn't come up with a good way to display them: in the notebook, if you do

```
B = matrix(2,2)
B.subdivide([1], [])
C = matrix(2,2)
C.subdivide([1,1], [])
```

then B and C will be typeset identically.  The command-line versions look different, though.


---

Comment by jhpalmieri created at 2009-03-05 20:59:02

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-03-05 20:59:02

Changing assignee from cwitty to jhpalmieri.


---

Comment by jhpalmieri created at 2009-03-12 21:49:56

rebased against 3.4; apply only this patch


---

Attachment

I think your solution for block matrices in the notebook is a good idea, at least until jsmath supports the standard way.


---

Comment by mabshoff created at 2009-03-25 08:43:40

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 08:43:40

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
