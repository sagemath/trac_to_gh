# Issue 9108: Mark long doctests in rings/polynomial/symmetric_ideal

Issue created by migration from https://trac.sagemath.org/ticket/9108

Original creator: leif

Original creation time: 2010-06-01 15:16:01

Assignee: malb

CC:  simonking cremona

Keywords: time-out, doctest, symmetric ideal, symmetric_ideal

Two doctests/examples in `sage/rings/polynomial/symmetric_ideal.py` tend to time out on older/slower machines (and take a large amount of the overall test time of that module).


---

Comment by SimonKing created at 2010-06-01 15:19:47

Replying to [ticket:9108 leif]:
> Two doctests/examples in `sage/rings/polynomial/symmetric_ideal.py` tend to time out on older/slower machines (and take a large amount of the overall test time of that module).


---

Comment by leif created at 2010-06-01 15:20:03

Marks the offending lines with `# long time`. Based on 4.4.3.alpha0.


---

Attachment

Simon, you're too fast... ;-)

I've just uploaded a patch that reduces the module test time on a Pentium 4 (Prescott, 3.2 GHz) from 238.7 seconds to 33.1 seconds.


---

Comment by leif created at 2010-06-01 15:23:32

Changing status from new to needs_review.


---

Comment by leif created at 2010-06-01 15:28:54

Perhaps you could add less demanding tests. ;-)

Also, some docstring lines are "too long". (I personally don't mind source code that exceeds 80 columns, but the help output should perhaps be limited to 80 characters in width.)


---

Comment by cremona created at 2010-06-01 16:22:36

Before applying the patch to 4.4.3.alpha0:

```
jec@selmer%sage -t sage/rings/polynomial/symmetric_ideal.py 
sage -t  "sage/rings/polynomial/symmetric_ideal.py"         
	 [110.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 110.8 seconds
jec@selmer%sage -t -long sage/rings/polynomial/symmetric_ideal.py 
sage -t -long "sage/rings/polynomial/symmetric_ideal.py"    
	 [109.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 109.8 seconds
```

and after:

```
jec@selmer%sage -t sage/rings/polynomial/symmetric_ideal.py sage -t  "sage/rings/polynomial/symmetric_ideal.py"         
	 [16.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 16.5 seconds
jec@selmer%sage -t -long sage/rings/polynomial/symmetric_ideal.py sage -t -long "sage/rings/polynomial/symmetric_ideal.py"    
	 [108.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 108.2 seconds
```


Interesting to note that it is essentially just one test which takes the time!


---

Comment by cremona created at 2010-06-01 16:22:36

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2010-06-01 16:41:11

Replying to [comment:5 cremona]:
> Interesting to note that it is essentially just one test which takes the time!

Off list, Leif just sent me some timings: 

There is one symmetric Groebner basis computation that takes 73 seconds, but most of the time is actually spent for testing whether all variable permutations of all basis elements do indeed have symmetric reduction zero modulo the symmetric Groebner basis: 130 s.

I see two ways to proceed, depending on how soon the next release is due:

 1. Leif's patch could go in, as John gave it a positive review, and it is certainly harmless and solves the problem. 
 2. I could try to find a solution for the one offending doc test. For example, the long Groebner basis computation could be replaced by something else, such us the following, of course without the timings that I just inserted for demonstration:
 {{{
sage: R.<x,y> = InfinitePolynomialRing(GF(5),order='degrevlex')
sage: I = [2*x[4]*x[3]*y[4] - 2*y[0]^3]*R
sage: %time G = I.groebner_basis()
CPU times: user 1.70 s, sys: 0.01 s, total: 1.71 s
Wall time: 1.71 s
sage: G
[x_2*x_1*y_1 - y_0^3, x_2*x_1*y_2 - y_0^3, y_2*y_0^3 - y_1*y_0^3]
sage: %time [[(p^P).reduce(G) for p in G] for P in Permutations(Integer(3))]
CPU times: user 1.38 s, sys: 0.00 s, total: 1.38 s
Wall time: 1.38 s
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
 }}}

I think this example would actually be a good one, as it shows: 

 * Even a "principal" symmetric ideal may have a reduced symmetric Groebner basis formed by more than one element.
 * The test whether the elements still reduce to zero after variable permutation is easier, since the maximal variable index can be smaller (3 instead of 4; it should be bigger than the maximal index 2 that occurs in the symmetric Groebner basis).

So, if the next release will be soon, I suggest to take Leif's patch as it is. But I think in the long run, a new example (like the one above) is needed.

Concerning line lengths: Does this only concern the first line of the doc strings? I know that my first lines tend to be rather lengthy, as I learnt that the basic description of the functionality should be given in the first line of the doc string (this is why I don't do a line wrap).


---

Comment by leif created at 2010-06-01 16:43:19

Replying to [comment:5 cremona]:
> [...]
> Interesting to note that it is essentially just one test which takes the time!

Actually two lines/tests take very long:

```
line#  walltime statement (preparsed)
[0116  72.980s] J=I.groebner_basis()
[0135 130.070s] [[(p**P).reduce(J) for p in J] for P in Permutations(Integer(4))]
```

(of a total of ~240s on that system)

Note that line numbers slightly change after applying the patch.


---

Comment by SimonKing created at 2010-06-01 16:47:01

Replying to [comment:6 SimonKing]:
> I think this example would actually be a good one, as it shows: 

Or perhaps not _that_ good...

The generator is not minimally chosen in its orbit, and I don't like that the second summand has index zero. But I recently did a series of random examples in order to test how large a symmetric Groebner basis of a symmetric ideal generated by a single small polynomial can actually be, so, it is likely that I'll find a better one.


---

Comment by leif created at 2010-06-01 16:56:23

Replying to [comment:6 SimonKing]:
> So, if the next release will be soon, I suggest to take Leif's patch as it is. But I think in the long run, a new example (like the one above) is needed.

Feel free to add additional (short) tests... ;-)

Perhaps on another ticket?


> Concerning line lengths: Does this only concern the first line of the doc strings? I know that my first lines tend to be rather lengthy, as I learnt that the basic description of the functionality should be given in the first line of the doc string (this is why I don't do a line wrap).

I just noticed that e.g. some parameter description lines are wider (net width).

Also, some are "marked" `(optional)`; the current practice seems to be repeating the default value from the function definition, too, i.e.

```
    ``param`` -- (type, default: some_value) further description...
```



---

Comment by SimonKing created at 2010-06-01 17:00:34

Replying to [comment:9 leif]:
> Replying to [comment:6 SimonKing]:
> > So, if the next release will be soon, I suggest to take Leif's patch as it is. But I think in the long run, a new example (like the one above) is needed.
> 
> Feel free to add additional (short) tests... ;-)
> 
> Perhaps on another ticket?

Seems reasonable. So, for now, the solution is to skip the long test unless it is wanted, and on a different ticket, I'll try to replace the offensive example (not _add_ an example) and will also deal with the line length etc. 

Thank you for your patch!


---

Comment by cremona created at 2010-06-01 19:12:12

I am quite happy with the the conclusion to this discussion! John


---

Comment by SimonKing created at 2010-06-02 11:06:18

I created a new ticket #9114 (ready for review) that replaces the offensive test by something better, and also improves the formatting of the documentation of "infinite polynomial rings and friends".

Since Leif's patch already has a positive review, I based #9114 on it.


---

Comment by mhansen created at 2010-06-06 08:26:59

Resolution: fixed
