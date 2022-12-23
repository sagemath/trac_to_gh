# Issue 6887: Implement elliptic curve isogenies (continued)

Issue created by migration from https://trac.sagemath.org/ticket/6887

Original creator: cremona

Original creation time: 2009-09-04 11:59:29

Assignee: davidloeffler

CC:  was wuthrich shumow kohel jcooley

Keywords: elliptic curve isogeny

Thanks mainly to Dan Shumow, 4.1.1 has some very useful code for constructing elliptic curve isogenies.  Together with a summer student Jenny Cooley, I am implementing the following:

   1. For `l=2,3,5,7,13` over any field, find all `l`-isogenies of a given elliptic curve. (These are the `l` for which `X_0(l)` has genus 0).

   2. For the remaining `l` for which `l`-isogenies exist over QQ, similarly.

   3. Given an elliptic curve over QQ, find the whole isogeny class (this currently exists by wrapping some eclib code, but that it not very robust -- what we are writing will be!)

   4. Testing if two curves are isogenous (at least over QQ;  we can do something over other number fields but I am still working out how to make it rigorous.)

At the moment I am not planning anything over finite fields, where the situation is very different, though the generic code for `l=2,3,5,7,13` will work (as it is right now, only as long as the characteristic is not 2, 3 or `l`, but eventually that will change).

Some of the methods we are implementing were worked out by  Mark Watkins and me in an unfinished preprint c.2005.

As one major test of the code for curves over QQ, we are intending to check that the databases are closed under isogeny (as they should be!  at least my own should be).


---

Comment by davidloeffler created at 2009-10-09 09:08:48

Remove assignee davidloeffler.


---

Attachment

poster by Jenny for an exhibition at U of Warwick


---

Comment by cremona created at 2009-11-09 09:25:27

Apologies for taking so long to get the patch up here -- it has been a busy term.  To make up for that I have attached here the poster Jenny made for the local URSS (= Undergraduate Research Scholarship Scheme) exhibition, for which she received a certificate!


---

Comment by was created at 2009-11-09 17:22:19

"Mathematicians may continue to use the curves in the database without fear!"


---

Comment by cremona created at 2009-11-19 22:32:56

Changing status from new to needs_review.


---

Comment by cremona created at 2009-11-19 22:32:56

Here's the patch, ready for review. There's more to be done but this is a useful step in the right direction, I hope.  We did test the code over QQ against *all* curves in the database and it did fine.


---

Comment by wuthrich created at 2009-11-27 17:34:14

I got the following when I tried to apply the patch to 4.3.alpha0. Am I doing something wrong ?


```
sage: hg_sage.apply('trac_6887-isogeny.patch')
...
/usr/bin/patch: **** malformed patch at line 121: diff -r 465d8fc11bf5 -r ef97f71cd70b doc/en/introspect/__init__.py</pre>

abort: patch command failed: exited with status 2
```



---

Comment by cremona created at 2009-11-27 20:39:30

Replying to [comment:5 wuthrich]:
> I got the following when I tried to apply the patch to 4.3.alpha0. Am I doing something wrong ?
> 
> {{{
> sage: hg_sage.apply('trac_6887-isogeny.patch')
> ...
> /usr/bin/patch: **** malformed patch at line 121: diff -r 465d8fc11bf5 -r ef97f71cd70b doc/en/introspect/__init__.py</pre>
> 
> abort: patch command failed: exited with status 2
> }}}

How weird -- I did not edit any "introspect" files.  I will try to edit the patch, and try the result myself against 4.3.alpha0, and repost it.


---

Attachment

applies to 4.3.alpha0


---

Comment by cremona created at 2009-11-27 20:45:34

Please try the new version.  Thanks!  John


---

Comment by wuthrich created at 2009-12-03 23:19:54

Sorry for being so slow in reviewing this. This is a very good and long patch, so I will allow myself a bit more time to look at it. So far I only spotted a few minor issues. 

 * Coverage issue which should be easy to fix :

   {{{
   ell_curve_isogeny.py
   SCORE ell_curve_isogeny.py: 98% (79 of 80)

   Missing doctests:
         * _isogeny_machine(Ew, f, ker, a, iso=None, E=None):


   Possibly wrong (function name doesn't occur in doctests):
         * unfill_isogeny_matrix(M):
   }}}

 * The patch applies fine and the first few tests I did pass. But when you deleted the top part of the patch you (=John) probably deleted a little bit too much, the presentation here is missing something in the beginning. I don't think that it harms the patch though.

 * Naming : Do you want to call it l_isogenies ? I agree that prime_degree_isogenies is a bit long, but would have the advantage of being clear about what l can be and about the possible confusion with 1 and I (depending on the font). Or isogenies_of_prime_degree that would make the function appear in .isog<tab>. 

 * In line 1266 of ell_number_field.py, docstring of is_isogenous, you write
     _If ``True``, this test should be followed by a rigorous test (not fully implemented)._
   What do you mean by should ? Do you mean "this test is followed by a rigourous test if it is implemented for the given curve..." ? I think I know what goes on from the second to last example, but maybe it would be good to have a sentence or two about it.

Of course, these are very minor things. once I have played around a little with the code and read a bit more of it, I will give a positive review....

Chris.


---

Comment by cremona created at 2009-12-04 06:57:34

Many thanks, Chris.  I wil sort out the issues you mention easily.  No time for fuller reply now as I'm about to checkout of Luminy.  While here I discussed the special cases of l=5,7,13 and j=0,1728 with Mark Watkins (with whom most of the rest was developed) and see a better way to do that, without having crazy special cases such as char. 53 for (l,j)=(7,1728).  So the revised patch may have that in too.


---

Comment by cremona created at 2009-12-08 22:16:45

I have almost finished revising the patch.  I have fixed all the points raised above except (so far) changing the name l_isogenies, which I agree should have a name starting isog*.  My new patch still has the strange problem in its header, but I do not know how to fix that so if it does not prevent it being applied I may give up on that part.

In addition, I changed the code for l=5,7,13 and j=0,1728 to avoid the weird "feature" where a few random characteristics had to be excluded.  I remove my isogeny_machine function, opting instead for 6 separate functions for these 6 cases, despite some repetition of code, since it just got too complicated to write one function which handled all 6 cases plus subcases (for endomorphisms and non-endos).

Hope to finish and re-post patch on Wednesday.


---

Attachment

Replaces previous, applies to 4.3.alpha1


---

Comment by cremona created at 2009-12-09 20:24:01

I have dealt with the referee (Chris)'s points;  in addition to the things listed above, I changed "l_isogenies" to "isogenies_prime_degree" throughout.

A small further review needed, please!


---

Comment by wuthrich created at 2009-12-09 20:27:47

I will look at it.


---

Comment by wuthrich created at 2009-12-10 00:24:41

Changing status from needs_review to positive_review.


---

Comment by wuthrich created at 2009-12-10 00:24:41

All tests passed. (at least it did not have an effect on my testall results)

Also the minor issues above are all solved. I have not checked in details all the algorithms, but I am confident that they are correct. Especially because they give back the original results in the table.

When testing if the `isogeny_graph()` was not affected by this, I noticed that the graphs are now not well plotted anymore: the picture is cut off too close to the graph. Of course, this has nothing to do with the patch here. I will search tomorrow if a ticket exists already for this.

Great work, Jenny. I wish I would find summer students of that level myself !


---

Comment by was created at 2009-12-10 07:01:37

> I will search tomorrow if a ticket exists already for this. 

This is "well known".  I'm not sure whose patch broke this, but I sure as heck wish this would get fixed!


---

Comment by cremona created at 2009-12-22 17:42:05

This has been sitting with a positive review for nearly two weeks, and I just noticed that it had no milestone set.  So I set it to 4.3 (ever optimistic).  Of course it could be bumped to 4.3.1...


---

Comment by was created at 2009-12-24 07:12:37

This will be merged in first thing for 4.3.1.


---

Comment by cremona created at 2009-12-24 10:01:26

Replying to [comment:16 was]:
> This will be merged in first thing for 4.3.1.
That's fine -- thanks!


---

Comment by mhansen created at 2010-01-04 04:09:44

Resolution: fixed
