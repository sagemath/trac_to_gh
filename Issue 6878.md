# Issue 6878: [with patch, needs review] allow the exclusion of points from the plot range

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-09-03 13:27:41

Assignee: was

Keywords: plot

The attached patch adds a new option 'exclude' to the plot command
which allows to exclude points from the plot.

This is useful if there are discontinuities in the function you are plotting.


```
sage: plot(floor(x), (x, 1, 10), exclude = [1..10])
```



---

Comment by jason created at 2009-09-15 09:10:04

Very nice!

This line:


```
points = [e.right() for e in exclude.solve(v) if e.left() == v] 
```


should also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.


---

Comment by whuss created at 2009-09-28 12:51:16

Replying to [comment:1 jason]:
> Very nice!
> 
> This line:
> 
> {{{
> points = [e.right() for e in exclude.solve(v) if e.left() == v] 
> }}}
> 
> should also check that v is not in the right side.  Alternatively, you could use the solution_dict parameter to make sure you get a solution.

The new version of the patch includes your suggestion.


---

Comment by jason created at 2009-10-01 04:57:45

Some more comments after examining things more carefully:

 * Use "is not None" rather than "!= None", as the "is not None" is way, way faster (it's a pointer comparison)

 * If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.

 * Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.

Those are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).


---

Attachment

Replying to [comment:3 jason]:
> Some more comments after examining things more carefully:
> 
>  * Use "is not None" rather than "!= None", as the "is not None" is way, way faster (it's a pointer comparison)

Done
 
>  * If I have just a few excluded points, but lots more poles, won't the break during the calculation of the exclusions also jump out of the loop that deals with detecting poles?  That means my poles past the last exclusion point are ignored.

You are right. I have fixed this.

>  * Can you put a brief comment in about `(x0 < exclusion_point <= x1 or x0 <= exclusion_point < x1)`?  It may be just that it's too late, but this is confusing me a bit.

I don't know anymore why I have written it that way. I have changed it to

`(x0 <= exclusion_point <= x1)`
 
> Those are the only issues I find; the code other than that works fine.  I have not tested the output (nice doctests, though!).


---

Comment by whuss created at 2009-10-16 15:52:20

Changing status from needs_work to needs_review.


---

Comment by whuss created at 2009-12-20 10:20:59

Changing assignee from was to whuss.


---

Comment by rossk created at 2010-01-31 03:39:57

Works as advertised with the caveat that if the exclusion points are less than xmin or greater than xmax then the plot range is extended (beyond either xmin and xmax). Statements below demonstrate this. 

(IMHO, I think this is new functionality that works and its easy to specify an exclude range that is inside xmin..xmax to get the plot range you want so it should go in the next milestone release - so Im giving it a positive review).


```
sage: plot(floor(x), xmin=0, xmax=10)              

sage: plot(floor(x), xmin=0, xmax=10, exclude = [1..15])

sage: plot(floor(x), xmin=0, xmax=10, exclude = [1..10])

sage: plot(floor(x), xmin=0, xmax=10, exclude = [5..10])
```


(I guess if we dont want the exclusion points to modify the plot range - which is ideal - this should be in a new ticket)


---

Comment by rossk created at 2010-01-31 03:39:57

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 15:29:52

The commit string is not sufficiently descriptive.  I've refreshed it to

```
#6878: Allow the exclusion of points from the plot range
```


in the queue for 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 10:15:58

Please remember to update the relevant ticket fields --- the release managers use an automated script to generate lists of merged tickets.


---

Comment by mpatel created at 2010-02-11 14:59:20

Resolution: fixed
