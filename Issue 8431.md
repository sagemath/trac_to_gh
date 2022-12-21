# Issue 8431: Rauzy fractal (discrete planes and broken lines)

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-03-03 23:49:21

Assignee: vdelecroix

CC:  sage-combinat slabbe abmasse tmonteil

Keywords: word morphism

Thinking about it for a long time and motivated by [#8423](http://trac.sagemath.org/sage_trac/ticket/8423&usg=AFQjCNG8_y-UlT3ON3unoD3utIEHQfTYbQ) this ticket stands for
  * the creation of WordMorphismExtension and WordMorphismExtensionDual (from [an article of Sano-Arnoux-Ito](http://iml.univ-mrs.fr/~arnoux/AISrev.pdf))
  * Have easy to use function for plotting Rauzy fractals using those algebraic tools


---

Comment by vdelecroix created at 2010-03-04 00:08:36

Changing type from defect to task.


---

Comment by slabbe created at 2010-03-08 11:20:14

I add myself in cc because I am interested.


---

Comment by tjolivet created at 2010-09-17 11:11:48

Changing keywords from "word morphism" to "word morphism unit face generalized substitution rauzy fractal".


---

Comment by tjolivet created at 2010-09-17 11:11:48

Changing assignee from vdelecroix to tjolivet.


---

Attachment


---

Comment by tjolivet created at 2010-09-17 11:12:54

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-09-17 18:16:16

I feel like `Patch`, `Face`, `E1Star` might be too domain specific to import into the global namespace.


---

Comment by slabbe created at 2010-09-17 21:38:38

Cher Timo,

Thanks a lot for your recent effort in polishing that code. I am actually needing it rigth now!! It will be of great help to me. 

I just read through the patch from my web browser and got those comments :

 1. As Mike Hanson, I think those three classes should not be in the global namespace. To create a E1Star, I recommand to add a method in the `WordMorphism` class.
 1. Add the file to the documentation. To do this you must edit the file sage-your-branch/doc/en/reference/combinat.rst
 1. Each sage block must be preceded by ::.
 1. No example using color in Face `__init__` function.
 1. Examples of all the possible drawings.
 1. Rename `_image_by_substitution` to `_apply_substitution` in Face class.
 1. Face._image_by_substitution should only accept E1Star object. If not, it should  raise an `TypeError` and not try to coerce the input to an E1Star object.
 1. Patch.translate method forgets the color of the faces.
 1. Patch.apply_substitution should only accept E1Star object. If not, it should raise an `TypeError` and not try to coerce the input to an E1Star object.
 1. `_M` and `_inv_M` should become `lazy_attributes`
 1. `_inv_M` should be computed from _M
 1. For the matrix method of E1Star, should `_inv_M` be the "matrix associated with self" more than `_M` ?
 1. When I used these classes last week, I needed the method `__eq__` for Patch. Here is my code :


```
    def __eq__(self, other):
        r"""
        EXAMPLES::

            TODO!!

        """
        return (isinstance(other, Patch) and
                set(self) == set(other) )
```


I am going to download, apply and use the patch real soon...and I guess I will have more comments...


---

Comment by slabbe created at 2010-09-17 21:38:38

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2010-09-18 17:36:54

I suggest to add this example for the method `__eq__` for Patch class :


```
    def __eq__(self, other):
        r"""
        EXAMPLES::
            
            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: x = WordMorphism('0->02,1->012,2->2')
            sage: y = WordMorphism('0->012,1->12,2->2')
            sage: p = Patch([Face((0,0,0),1), Face((0,0,0),2), Face((0,0,0),3)])
            sage: E1Star(x) (p) == E1Star(y) (p)
            False
            sage: E1Star(x * y) (p) == E1Star(y) (E1Star(x) (p))
            True

        """
        return (isinstance(other, Patch) and
                set(self) == set(other) )

```


I also suggest to add a `__len__` method and change the `__repr__` to behave like Graphs (Graph of 45 vertices).


```
    def __repr__(self):
        r"""
        String representation of a patch.

        EXAMPLES:

            sage: x = [Face((0,0,0),t) for t in [1,2,3]]
            sage: P = Patch(x)
            sage: P
            Patch of 3 faces
        """
        return "Patch of %s faces"%len(self)

    def __len__(self):
        r"""
        Returns the number of faces.

        EXAMPLES::

            sage: x = [Face((0,0,0),t) for t in [1,2,3]]
            sage: P = Patch(x)
            sage: len(P)       #indirect doctest
            3
        """
        return len(self._faces)
```



---

Comment by slabbe created at 2010-09-18 17:52:56

The method `__call__` of E1Star should pass the possible kwds to `apply_substitution method` : 


```
    def __call__(self, patch, **kwds):
        r"""
        EXAMPLES:

            sage: p = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: sigma = WordMorphism('1->12,2->13,3->1')
            sage: E = E1Star(sigma)
            sage: E(p)
            Patch: [[(1, 0, -1), 1]*, [(0, 1, -1), 2]*, [(0, 0, 0), 3]*, [(0, 0, 0), 1]*, [(0, 0, 0), 2]*]
        """
        patch = Patch(patch)
        patch.apply_substitution(self, **kwds)
        return patch
```



---

Comment by slabbe created at 2010-09-18 20:52:17

The last lines of plot_tikz should be : 


```
        s += '\\end{tikzpicture}\n'
        return LatexExpr(s)
```


Make sure to add the following line in the beginning of the file :


```
from sage.misc.latex import LatexExpr
```


This is to avoid `latex(a_patch.plot_tikz())` be edited wrongly.


---

Comment by slabbe created at 2010-09-18 20:56:31

The function `plot_tikz` should be renamed `_latex_`.

A graph in Sage has methods `plot`, `plot3d` and `_latex_` and I think we can follow the same behavior.


---

Comment by tjolivet created at 2010-09-19 12:08:27

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-09-23 19:06:43

> *EDIT (2010-09-19):* a new version of the patch is attached (`trac_8431_e_one_star.patch`), taking into account the suggestions given in the comments. Documentation compiles fine, except for the following warning, which I don't think comes from an error in `e_one_star.py`:
> 
>   `/home/timo/sage-4.5.3/local/lib/python2.6/site-packages/sage/combinat/e_one_star.py:docstring of sage.combinat.e_one_star:56: (WARNING/2) Literal block expected; none found.`

Actually, it does. If you don't write a sage block after the line `EXAMPLES:`, then you must write only one colon:


```
EXAMPLES:

We start by drawing a simple three-face patch::
```


instead of


```
EXAMPLES::

We start by drawing a simple three-face patch::
```


One more detail about ReST :


```
This module implements the `E_1^*(\sigma)` substitution
associated with a one-dimensional substitution `\sigma`,
that acts on unit faces of dimension `(d-1)` in `\mathbb R^d`.
```


The macro `\RR`, as well as `\ZZ` and `\QQ` is defined to get the doc more readable in the terminal, so the following should work : ``\RR^d``.


---

Attachment

Okay, thanks again for the useful comments!

I've updated the patch.


---

Comment by slabbe created at 2010-09-24 00:57:26

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2010-09-24 00:57:26

I just uploaded a patch which fixes some syntax stuff but I did a little bit more than that. More importantly, I :
 
  - moved `Face._apply_substitution` to the method `E1Star._call_on_face` because that is where that code belongs.
  - reworked `Patch.apply_substitution` and moved the code that was repainting the faces to a method called `Patch.repaint`
  - moved the code of `Patch.apply_substitution` to `E1Star.__call__` because it *was* creating a copy anyway. `Patch.apply_substitution` works as before. `E1Star.__call__` works twice as fast as before because it doesn't do two copies but only one.
  - added some cached method and lazy attributes in `E1Star` class

I still see one possible problem before giving a positive review, but didn't have time enough to test/fix it. The attribute `E1Star._base_iter` seems to assume some conditions on the values of faces types. That they are integer for instance. Haven't tested it. 

For the tikz output code, I think the `\newcommand` in the code is not compatible with sagetex package. If I am not mistaken, `\newcommand` are not possible in an input file.

Timo, now that I uploaded a new patch, you will have to create a new separate patch that applies over yours and mine if you want to modify anything.


---

Attachment

Applies over the trac_8431_e_one_star.patch


---

Comment by slabbe created at 2010-09-24 20:08:10

Okay, I just re-uploaded my review patch. The faces type is now considered as an arbitrary object. It can be any hashable object. Doing this, the code is more readable (e.g. the method `_base_iter`)  and more versatile (no such `type + 1` assuming type is an integer).

In order to do so, I changed the way `E1Star._base_iter` behave. It now returns a dict.

And now, the domain alphabet of the substitution used must correspond to the type of faces. No more '1' -> rank('1') = 0 -> + 1 -> 1 = type of a face. The type of faces iff domain alphabet. If one wants to use integer type of faces, he must define a substitution on integers which is possible using dictionary.

I also moved `orig_coords` to an attribute of Patch called `face_contour`. Code gets cleaner that way also. `face_contour` now gets assigned at the creation of a Patch.

I also added `#not tested` to many plot test so that the time of testing for that file is decreased from 24s to 7s on my computer. I kept some plot tested at minimum.

My very last concern about the actual state of the ticket is about the methods outputting tikz code. I want to make sure that they work well. I will do more test later (I'm done for the day). The necessity of `\newcommand` needs to be studied.

Sorry Timo, I am very serious on the review. But I think it is better and easier to do changes now than after inclusion in Sage.

Cheers,


---

Comment by tjolivet created at 2010-09-24 23:26:29

Okay I'll continue working on it! Thanks again for all you advices and improvements!

I'll do the remaining things we talked about and upload a new patch.

As for the tikz code, I am sure that it compiles fine (with a normal texlive installation). The \newcommand is nice because then one face is reprensented by a small line instead of three bulky ones. It could be _two_ lines, but in tikz there is no other way to specify an RGB color than using \definecolor, which takes one more line. (Something similar to `black!30!green` for RGB would be the great...)


---

Comment by abmasse created at 2010-09-25 02:17:30

Hello, Timo and Sébastien !

Replying to [comment:18 tjolivet]:
> As for the tikz code, I am sure that it compiles fine (with a normal texlive installation). The \newcommand is nice because then one face is reprensented by a small line instead of three bulky ones. It could be _two_ lines, but in tikz there is no other way to specify an RGB color than using \definecolor, which takes one more line. (Something similar to `black!30!green` for RGB would be the great...)

I agree with you that the `\newcommand` makes the output much lighter. On the other hand, it doesn't compile correctly... I tried it with a normal Latex distribution, but I had to move the three `\newcommand` statements outside the tikzpicture environment.

I might have a solution that would avoid using them, but which is not as neat. You could use

```
\foreach \x / \y / \z / \c1 / \c2 / \c3 in {...}
```

and replace the `...` by the appropriate very long list of parameters for each face and then put in the body of the `\foreach` command the 3-lines Latex statement that draws the face with these parameters.

What do you say? Do you understand what I'm talking about (I don't feel my explanation is very clear)?


---

Comment by tjolivet created at 2010-09-25 12:03:02

Replying to [abmasse](http://trac.sagemath.org/search/opensearch?q=comment%3A19):


> I agree with you that the `\newcommand`  makes the output much lighter. On the other hand, it doesn't compile  correctly... I tried it with a normal Latex distribution, but I had to  move the three `\newcommand` statements outside the tikzpicture environment. I might have a solution that would avoid using them, but which is not as neat. You could use !` \foreach \x / \y / \z / \c1 / \c2 / \c3 in {...} ` and replace the `...` by the appropriate very long list of parameters for each face and then put in the body of the `\foreach` command the 3-lines Latex statement that draws the face with these parameters. What do you say? Do you understand what I'm talking about (I don't feel my explanation is very clear)?

Yes, you made yourself  clear, and it seems like a  good idea. I'll try it on  big instances, and if it works, I'll make it that way in the new patch. Otherwise, moving the \newcommand outside the tikzpicture is not a problem at all (it should have been that way, I probably made a !``typo!''...).


---

Comment by abmasse created at 2010-09-25 12:15:44

Replying to [comment:20 tjolivet]:
> Replying to [abmasse](http://trac.sagemath.org/search/opensearch?q=comment%3A19):
> 
> Yes, you made yourself  clear, and it seems like a  good idea. I'll try it on  big instances, and if it works, I'll make it that way in the new patch. Otherwise, moving the \newcommand outside the tikzpicture is not a problem at all (it should have been that way, I probably made a !``typo!''...).

The problem is that if you use the `tikz_plot` twice in the document with `sagetex` there will be a compilation problem (since you can't use `\newcommand` on an already define command (you need local variables!).

There might be another solution, using `\def\loza#1#2#3#4#5#6` (which is local when included in a `tikzpicture` environment), but I haven't tried it out.


---

Comment by tjolivet created at 2010-09-25 12:30:50

Replying to [abmasse](http://trac.sagemath.org/search/opensearch?q=comment%3A21):



> The problem is that if you use the `tikz_plot` twice in the document with `sagetex` there will be a compilation problem (since you can't use `\newcommand` on an already define command (you need local variables!). There might be another solution, using `\def\loza#1#2#3#4#5#6` (which is local when included in a `tikzpicture` environment), but I haven't tried it out.

Okay, so I'll get rid of the `\newcommand` in any case, and  use either the `\foreach` or the `\def` solution; I admit I also like the idea of outputing a `tikzpicture` that works !``out of the box!''. Thanks for the suggestions and comments.


---

Comment by tjolivet created at 2010-09-28 12:25:43

Hello, I uploaded a new patch (that applies over !``e_one_star and !`` and !``review-sl!``).

 * It changes the `plot_tikz` function. There are no more `\newcommand`'s, but only `\def`'s that are inside the `tikzpicture` environment. (No more global annoyance, and it should work fine with `sagetex` now.) Also, RGB colors a printed with two decimals only.

 * In response to "the domain alphabet of the substitution used must correspond to the type of faces": now, every substitution defining an `E1Star` object is converted to an equivalent substitution on alphabet `'1'`, ..., `'d'`. The type of a face can be specified by a positive integer or a string representing a positive integer, and is converted to a string when the `Face` object is created. This allows us to assume that the type of a face in 3D is in {`'1'`, `'2'`, `'3'`}, which is very useful for plotting functions.

 * An option to color face according to their type has been added.

 * It is possible to choose whether to (or not to) print the `tikzpicture` environment definition, and the `\def` macros.

 * Some other minor fixes, and small documentation fixes.


---

Comment by slabbe created at 2010-09-29 14:14:01

Salut Timo,

I look at the patch and still have comments. 

>  * It changes the `plot_tikz` function. There are no more `\newcommand`'s,
>  but only `\def`'s that are inside the `tikzpicture` environment. (No more
>  global annoyance, and it should work fine with `sagetex` now.) Also, RGB
>  colors a printed with two decimals only.

Great for the `\def` instead of `\newcommand`. 

>  * In response to "the domain alphabet of the substitution used must
>  correspond to the type of faces": 

When I wrote that comment, I was meaning that I fixed it in my patch. In fact, I removed the coercion of the face type into the integer ring which allows the user to use the type of object he wants for the face types.

> now, every substitution defining an `E1Star` object is converted to an
> equivalent substitution on alphabet `'1'`, ..., `'d'`. The type of a face can
> be specified by a positive integer or a string representing a positive
> integer, and is converted to a string when the `Face` object is created. 

I do not agree with this. I do not want the type face to be converted to an integer nor to a str. I want it to stays as it is given by the user. I want the correspondance between the faces type and the domain alphabet of the morphism to be clean. I do not want the correspondance appear by coincidence. Here are three examples to clarify my point :

GOOD (integer faces type with integers for the domain of the substitution) :

```
    sage: from sage.combinat.e_one_star import E1Star, Face, Patch
    sage: x = [Face((0,0,0),1), Face((0,0,0),2), Face((0,0,0),3)]
    sage: P = Patch(x)
    sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
    sage: E = E1Star(sigma)
    sage: E(P)
    Patch: [[(1, 0, -1), 1]*, [(0, 1, -1), 2]*, [(0, 0, 0), 3]*, [(0, 0, 0), 1]*, [(0, 0, 0), 2]*]
```


GOOD (str faces type with str for the domain of the substitution) :

```
    sage: from sage.combinat.e_one_star import E1Star, Face, Patch
    sage: x = [Face((0,0,0),'1'), Face((0,0,0),'2'), Face((0,0,0),'3')]
    sage: P = Patch(x)
    sage: sigma = WordMorphism('1->12,2->13,3->1')
    sage: E = E1Star(sigma)
    sage: E(P)
    Patch: [[(1, 0, -1), 1]*, [(0, 1, -1), 2]*, [(0, 0, 0), 3]*, [(0, 0, 0), 1]*, [(0, 0, 0), 2]*]
```


BAD (integer faces type with str for the domain of the substitution). Correspondance is lost. If the following is suppported, it makes the code less usable for potential future uses by others.

```
    sage: from sage.combinat.e_one_star import E1Star, Face, Patch
    sage: x = [Face((0,0,0),1), Face((0,0,0),2), Face((0,0,0),3)]
    sage: P = Patch(x)
    sage: sigma = WordMorphism('1->12,2->13,3->1')
    sage: E = E1Star(sigma)
    sage: E(P)
    Patch: [[(1, 0, -1), 1]*, [(0, 1, -1), 2]*, [(0, 0, 0), 3]*, [(0, 0, 0), 1]*, [(0, 0, 0), 2]*]
```


The reason is that the code we write is *always* used differently by the others. And the coercion of the face type to a str object is an unneccessary restriction. Do you agree with me?

> This allows us to assume that the type of a face in 3D is in {`'1'`, `'2'`,
> `'3'`}, which is very useful for plotting functions.

Can you explain me why it is useful for plotting functions? Is it because digits can not be used in a definition like `\def\loz1{...}` ? But then, I don't understand why `'1'` is better than `1`. I am sure we can find a solution for the plotting problem that will not restrict the usability of the code.

>  * An option to color face according to their type has been added.

Thanks for fixing this in the `__call__` method. Small suggestions : coloring='color_from_type' is redundant. I suggest that the following 


```
-  ``color_from_type`` - boolean (default: False). Colors the faces 
     according to their type. 
```


becomes 


```
-  ``'face_type'`` - boolean (default: False). Colors the faces 
     according to their type. 
```


For the `repaint` method. I dislike the addition of a new argument to the function. The reason is that the user should never use the argument `cmap` at the same time as the argument `color_from_type`. Hence, inconstencies in the arguments can happen and should be considered. This tells us that it should be only one argument that plays the role for either one or the other. Python is great for that because it is not a typed language. Moreover, I was disappointed that it is not possible for the user to specify which color he can give to each faces type. Hence, I suggest to do the following which should fix all the problems I mention::


```
    def repaint(self, cmap='hsv'):
        r"""
        Repaint all the faces of self from the given color map.

        This changes self.

        INPUT:

        -  ``cmap`` - color map (default: 'hsv'). It can be one of the
           following :
           
	   - string - A color map. For available color map names type: ``import
	     matplotlib.cm; matplotlib.cm.datad.keys()``. Each face will be
             given a color according to their rank in the patch.
	   - list - a list of color to assign to the faces in order.
	   - dict - a dict of faces type mapped to colors.
	   - ``{}``, the empty dict - the dict ``{'1':'red', '2':'green', '3':'blue'}``              is used.
```


>  * It is possible to choose whether to (or not to) print the `tikzpicture`
>  environment definition, and the `\def` macros.

Ok. And by default, they are printed : great.

>  * Some other minor fixes, and small documentation fixes.

Great.

Finally, lines like


```
if print_macros == True: 
```


should be replaced by


```
if print_macros:
```


That is it for now.

If you rework on it, you can reload your last patch or add a new one. It is as you wish. I do not have any local modifications.

Cheers!


---

Attachment

Hi Sébastien and the others,

_[We had a long discussion on skype with Sébastien regarding his last reply.]_

I just uploaded a new version of the last patch. The face types are now integers, and only integers (from 1 to d), and the [WordMorphism](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMorphism) associated with an E1Star object is also defined on integers.

Some other things I changed:

 * I removed the `coloring` option in `apply_substitution`. Why? Because we can use `repaint`, and it is better that all the "color business" is taken care of by `repaint`. The colors of a face in an image by a substitution is automatically the color of its preimage (which enables to get the interesting coloring given by the substitution). If we want to change the color of a patch obtained by iteration, `repaint`!

 * I took care of the above remarks concerning `color_from_preimage`, and used the clever solution suggested by Sébastien: dictionaries `{types:colors}`.

 * Some small fixes.

*Now, a last and important remark*. Writing


```
sigma = WordMorphism('1->12,2->13,3->1')
```

is less painful than writing


```
sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
```

Since all the face types are integers and the [WordMorphism](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMorphism) defining an `E1Star` must be on integers, we are supposed to use the latter way to define `sigma`. However, I find it very inconvenient, so we allow the user to give a `sigma` defined on an *arbitrary* alphabet. When `E1Star` is defined, it is converted and stored as a substitution on the alphabet `[1, ..., d]` (so that there is a correspondence between the types of the faces and the alphabet of the substitutions). It really makes the definitions much more convenient and I don't think that it harms `sage` so much.

Also, I don't think that it would be useful to allow the user to specify an arbitrary alphabet for the faces, since they are not used as the letters of a word, but as three-dimensional objects, which we _call_ of type `1`, `2` or `3`. (This is why all the types are represented by integers.) It corresponds to the mathematical definition of the object.

I strongly insist on this last remark!


---

Comment by abmasse created at 2010-10-01 19:28:00

Hi, Timo and Sébastien !

Replying to [comment:25 tjolivet]:
> Hi Sébastien and the others,
> 
> *Now, a last and important remark*. Writing
> 
> {{{
> sigma = WordMorphism('1->12,2->13,3->1')
> }}}
> is less painful than writing
> 
> {{{
> sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
> }}}

I agree with you on that one. This is something I've noticed too when using `WordMorphism`'s. The thing is: the problem comes from the object WordMorphism, and it's where it should be solved, in my opinion, and not in the class `E1Star`.

> Since all the face types are integers and the [WordMorphism](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMorphism) defining an `E1Star` must be on integers, we are supposed to use the latter way to define `sigma`. However, I find it very inconvenient, so we allow the user to give a `sigma` defined on an *arbitrary* alphabet. When `E1Star` is defined, it is converted and stored as a substitution on the alphabet `[1, ..., d]` (so that there is a correspondence between the types of the faces and the alphabet of the substitutions). It really makes the definitions much more convenient and I don't think that it harms `sage` so much.
> 
> Also, I don't think that it would be useful to allow the user to specify an arbitrary alphabet for the faces, since they are not used as the letters of a word, but as three-dimensional objects, which we _call_ of type `1`, `2` or `3`. (This is why all the types are represented by integers.) It corresponds to the mathematical definition of the object.
> 

I disagree. If I'm not mistaken, the integer meaning of 1, 2, 3 is never used in the construction of patches and discrete plane. I mean, we could use a,b,c and everything would work the same, there is no gain from encoding it with integers, since no additive group structure is used (correct me if I'm wrong, though, that could be a good argument).

In fact, I think it's quite the opposite. It would be better to allow the user to have any alphabet, so that he can use any structure he wants (additive group, for instance, or any other operation that might encode interesting discrete plane construction).

> I strongly insist on this last remark!

What I propose you is that either Sébastien or I work on the improvement of the construction of `WordMorphism` in order to offer something like

```
sigma = WordMorphism('1->12,2->13,3->1', type='integer')
```


Does that seem reasonable?

P.S. I'm following your discussion and I see the progress... Keep the good work!


---

Comment by tjolivet created at 2010-10-01 20:07:13

Thanks for you answer and hello!

Replying to [comment:26 abmasse]:

> I disagree. If I'm not mistaken, the integer meaning of 1, 2, 3 is never used in the construction of patches and discrete plane. I mean, we could use a,b,c and everything would work the same, there is no gain from encoding it with integers, since no additive group structure is used (correct me if I'm wrong, though, that could be a good argument). In fact, I think it's quite the opposite. It would be better to allow the user to have any alphabet, so that he can use any structure he wants (additive group, for instance, or any other operation that might encode interesting discrete plane construction).

Yes, the types are just names, so anything else could be used. But I'm not sure that it would be very useful, it's not comparable to allowing any choice of letters for words, for example. If you (or anybody else) want to implement it, it's OK, but please make sure that if integer faces are given, it works as in the current patch by default (to make it "easy-usable").

> What I propose you is that either Sébastien or I work on the improvement of the construction of `WordMorphism` in order to offer something like ` sigma = WordMorphism('1->12,2->13,3->1', type='integer') ` Does that seem reasonable? P.S. I'm following your discussion and I see the progress... Keep the good work!

This a  good idea, even with respect to [WordMorphism](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMorphism) only. I'm just a bit saddened that we will have to add "`type='integer'`") when specifying a substitution to work with the default integers, but I can live with it!

---

I think that apart from the possible option to leave the choice of the alphabet, and the "`type='integer'`" feature to be added to [WordMorphism](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMorphism), the work on this patch is over. Do you agree? I leave these two last points up to you.

Thanks for all your help, work and comments on this (it's my first patch, as you know), I'm learning a lot. And I'm ready to work more if there is something more that I forgot!


---

Comment by slabbe created at 2010-10-01 20:13:50

Hi Timo,

>  * I removed the `coloring` option in `apply_substitution`. Why? Because we
>  can use `repaint`, and it is better that all the "color business" is taken
>  care of by `repaint`. The colors of a face in an image by a substitution is
>  automatically the color of its preimage (which enables to get the
>  interesting coloring given by the substitution). If we want to change the
>  color of a patch obtained by iteration, `repaint`!

Great idea! Very very good. That is really upgrading the quality of the code. The design is converging!

>  * I took care of the above remarks concerning `color_from_preimage`, and
>  used the clever solution suggested by Sébastien: dictionaries
>  `{types:colors}`.

Great. I am just wondering if we could avoid to use a list of one color to change the color of every faces. If their is no intersection between the list of available color and the list of available color map, then simply a color string could be used for coloring every faces the same color.

> *Now, a last and important remark*. Writing
> 
> {{{
> sigma = WordMorphism('1->12,2->13,3->1')
> }}}
> is less painful than writing
> 
> {{{
> sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
> }}}

I agree.

> Since all the face types are integers and the [WordMorphism](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMorphism) defining an `E1Star` must be on integers, we are supposed to use the latter way to define `sigma`. However, I find it very inconvenient, so we allow the user to give a `sigma` defined on an *arbitrary* alphabet. When `E1Star` is defined, it is converted and stored as a substitution on the alphabet `[1, ..., d]` (so that there is a correspondence between the types of the faces and the alphabet of the substitutions). It really makes the definitions much more convenient and I don't think that it harms `sage` so much.
> 
> Also, I don't think that it would be useful to allow the user to specify an arbitrary alphabet for the faces, since they are not used as the letters of a word, but as three-dimensional objects, which we _call_ of type `1`, `2` or `3`. (This is why all the types are represented by integers.) It corresponds to the mathematical definition of the object.
> 
> I strongly insist on this last remark!

One solution is to allow face type '1', '2' and '3' which would work easily with such expressions : `WordMorphism('1->12,2->13,3->1')`. But I know you don't like this solution.

On the other side, as I already explained, I dislike the solution you propose because (1) it is getting the code less efficient for those who specify a WordMorphism already defined on integers, (2) because those translation of object gets the code less versatile and reusable by others and (3) it may leads to conceptual problems for the user when letters gets translated not in the way he expected.

Personnaly, I can not give a positive review with this translation of alphabet.

I think Alexandre's ideas for improving the definition of `WordMorphism` might be a good compromise.



Moreover, in the code of `plot_tikz`, I suggest to use the following ideas :


```
sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
sage: d = P._face_contour
sage: ' -- '.join(map(str, d[1])) + ' -- cycle;\n'
'(0, 0, 0) -- (0, 1, 0) -- (0, 1, 1) -- (0, 0, 1) -- cycle;\n'
```


rather than hardcoding the face contour points:


```
        if print_macros:
            s += '\\def\\loza#1#2#3#4#5#6{\n'
            s += '  \\definecolor{facecolor}{rgb}{#4,#5,#6}\n'
            s += '  \\fill[fill=facecolor, draw=black, shift={(#1, #2, #3)}]\n'
            s += '  (0,0,0) -- (0,1,0) -- (0,1,1) -- (0,0,1) -- cycle;\n'
            s += '}\n'
```



---

Comment by slabbe created at 2010-10-01 23:09:46

Just added a patch that improves the color map manipulations and tikz code. I removed the `Face._plot_tikz` method that was not really usable on its own and moved its code into the `Patch.plot_tikz`.

Patches apply in this order :

 1. trac_8431_e_one_star.patch 
 1. trac_8431_review-sl.patch 
 1. trac_8431_might_be_final_tj.patch
 1. trac_8431_colors_tikz-sl.patch 

Earlier, I wrote :

> Great. I am just wondering if we could avoid to use a list of one color to change the color of every faces. If their is no intersection between the list of available color and the list of available color map, then simply a color string could be used for coloring every faces the same color. 

Forget about that, I was wrong. I like the way it is.


---

Attachment

Applies over the precedent 3 patches


---

Comment by slabbe created at 2010-10-01 23:40:25

So, now, I can say that I give a positive review to this ticket if the following 5 lines of `E1Star.__init__` are removed.


```
        # changing the alphabet of sigma to [1, ..., d]
        A = sigma.domain().alphabet()
        change_alphabet = WordMorphism(dict([(A[i], [Integer(i+1)]) for i in range(len(A))]))
        D = dict([(change_alphabet(a)[0], list(change_alphabet(sigma(a)))) for a in A])
        sigma = WordMorphism(D)
```


Of course, my two patches also have to get a positive review by Timo or Alexandre (preferably both) before the ticket be ready to be merged into Sage.


---

Comment by tjolivet created at 2010-10-02 13:17:02

OK, I uploaded a last patch to fix the type of the [WordMorphism](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMorphism). The `__init__` method of `E1Star` accepts only integer substitutions. I have changed the doc accordingly. I hope that the `type='integer'` option of [WordMosphim](http://trac.sagemath.org/sage_trac/search/opensearch?q=wiki%3AWordMosphim) will be available soon!

The patch seems to be ready. How do we give positive review of an individual patch, and not to the whole ticket? How long will it take before it is integrated to sage?

To recap, the patches apply in this order:

 1. trac_8431_e_one_star.patch
 1. trac_8431_review-sl.patch
 1. trac_8431_might_be_final_tj.patch
 1. trac_8431_colors_tikz-sl.patch
 1. trac_8431_sigma_type_fix.patch

(Can we remove the useless trac_8431_E1Star.patch patch?)


---

Comment by tjolivet created at 2010-10-02 13:21:13

sigma type fix


---

Attachment


---

Comment by abmasse created at 2010-10-03 05:49:01

Replying to [comment:31 tjolivet]:
> The patch seems to be ready. How do we give positive review of an individual patch, and not to the whole ticket? How long will it take before it is integrated to sage?
>
Normally, when two people work on the same ticket and both of them provide patches, the last person cannot make the final positive review, so in that case, it's Sébastien that should do it. However, I will probably do it this week since both you and Sébastien worked on it. This way, it will give a different point of view.
 
The patch probably won't be merged in sage-4.6 as it is already in its alpha stage, but should be included in the next version. 

> To recap, the patches apply in this order:
> 
>  1. trac_8431_e_one_star.patch
>  1. trac_8431_review-sl.patch
>  1. trac_8431_might_be_final_tj.patch
>  1. trac_8431_colors_tikz-sl.patch
>  1. trac_8431_sigma_type_fix.patch
> 
> (Can we remove the useless trac_8431_E1Star.patch patch?)

Unfortunately, you can't.


---

Comment by slabbe created at 2010-10-05 00:34:48

Applies over the precedent 5 patches


---

Attachment

Just added a new patch that adds two methods that might be useful : `E1Star.__mul__` and `WordMorphism.dual_map`.

Patches need to be applied in this order:

   1. trac_8431_e_one_star.patch
   1. trac_8431_review-sl.patch
   1. trac_8431_might_be_final_tj.patch
   1. trac_8431_colors_tikz-sl.patch
   1. trac_8431_sigma_type_fix.patch 
   1. trac_8431-wordmorphism-sl.patch


---

Comment by slabbe created at 2010-10-05 00:39:40

Changing status from needs_work to needs_review.


---

Comment by tjolivet created at 2010-11-04 16:38:09

small fixes


---

Attachment

Hi,

This patch (trac_8431-smallfixes-tj.patch) corrects three bugs and adds three minor features:

 * in `.plot_tikz`, the option `edgecolor='facecolor'` didnt't work
 * in `.plot_tikz`, the option `print_tikz_env=False` caused an error message
 * in `.plot3d`, the plot was rotated uselessly (it was confusing)
 * patches can now be added (which gives their union)
 * `E1Star` morphisms can now be multiplied (according to the rule _E1Star(s*t) = E1Star(t)*E1Star(s)_)

Patches need to be applied in this order:

 1. trac_8431_e_one_star.patch
 1. trac_8431_review-sl.patch
 1. trac_8431_might_be_final_tj.patch
 1. trac_8431_colors_tikz-sl.patch
 1. trac_8431_sigma_type_fix.patch
 1. trac_8431-wordmorphism-sl.patch
 1. trac_8431-smallfixes-tj.patch


---

Comment by tjolivet created at 2010-11-05 11:31:36

Replying to [tjolivet](http://trac.sagemath.org/sage_trac/search/opensearch?q=comment%3A36):

> * in `.plot3d`, the plot was rotated uselessly (it was confusing)

A precision about the `.plot3d` fix, the removal of these two lines:

`911 P.aspect_ratio((1,1,1))`
`912 P = P.rotateY(pi/2).rotateX(pi/2)`

The first line doesn't change anything. The only way to control the aspect ratio of the rendered object in Jmol is to include it into a cube that contains everything, because Jmol will automatically take the smallest 3D rectangle that contains the object, and deform it to a cube (hence changing the aspect ratio). If a cube bounds everything, we get an actual aspect ratio of (1,1,1).

The second line was initally written to "turn" the patch so that it faces the viewer when Jmol opens. The problem is that `rotate` does not change the point of view, but rotates the object itself, which is very confusing when we want to plot something else with the Patch (normal vectors or contracting planes, for example).


---

Attachment


---

Comment by tjolivet created at 2010-11-10 15:25:08

I just added a new patch (trac_8431-alphaset-tj.patch) that applies over the previous ones, and that allows to set the `alpha` parameter in the `.plot` method. It is useful if we want to plot fractals without seeing the unit cube edges.


---

Comment by abmasse created at 2010-11-12 17:03:54

Hi, Timo !

I tried applying the various patches on a sage-4.6 clone and the patch trac_8431-smallfixes-tj.patch fails. Here's what I get.


```
labo [~/Applications/sage/devel/sage-t8431/sage/combinat]
 $ hg qseries
trac_8431_e_one_star.patch
trac_8431_review-sl.patch
trac_8431_might_be_final_tj.patch
trac_8431_colors_tikz-sl.patch
trac_8431_sigma_type_fix.patch
trac_8431-wordmorphism-sl.patch
trac_8431-smallfixes-tj.patch

labo [~/Applications/sage/devel/sage-t8431/sage/combinat]
 $ hg qtop
trac_8431-smallfixes-tj.patch

labo [~/Applications/sage/devel/sage-t8431/sage/combinat]
 $ hg qpop
now at: trac_8431-wordmorphism-sl.patch

labo [~/Applications/sage/devel/sage-t8431/sage/combinat]
 $ hg qpush
applying trac_8431-smallfixes-tj.patch
patching file sage/combinat/e_one_star.py
Hunk #6 FAILED at 1337
1 out of 7 hunks FAILED -- saving rejects to file sage/combinat/e_one_star.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8431-smallfixes-tj.patch
```


Could you please fix it? Or is it because the order is not correct? Here's the output for the rejected hunk:


```
labo [~/Applications/sage/devel/sage-t8431/sage/combinat]
 $ cat e_one_star.py.rej 
--- e_one_star.py
+++ e_one_star.py
`@``@` -1230,49 +1338,6 `@``@`
                 X[letter].append((v, k))
         return X
 
-    def __call__(self, patch, iterations=1):
-        r"""
-        Apply a generalized substitution to a Patch; this returns a new
-        object.
-        
-        The color of every new face in the image is given the same color as its preimage.
-
-        INPUT:
-
-        - ``patch`` - a patch
-        - ``iterations`` - integer (optional, default: 1) number of iterations
-
-        OUTPUT:
-            
-            a patch
-
-        EXAMPLES::
-
-            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
-            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
-            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
-            sage: E = E1Star(sigma)
-            sage: R = E(P)
-            sage: len(R)
-            5
-
-        ::
-
-            sage: x = (0,0,0)
-            sage: p = Patch([Face(x, 1, 'red'), Face(x, 2, 'yellow'), Face(x, 3, 'green')])
-            sage: p = E(p, iterations=4)
-            sage: p
-            Patch of 31 faces
-        """
-        old_faces = patch
-        for i in xrange(iterations):
-            new_faces = []
-            for f in old_faces:
-                new_faces.extend(self._call_on_face(f, color=f.color()))
-            old_faces = new_faces
-
-        return Patch(new_faces)
-
     def _call_on_face(self, face, color=None):
         r"""
         Returns an iterator of faces obtained by applying self on the face.
```



---

Comment by tjolivet created at 2010-11-12 22:37:38

Hi !

Well, that's very strange: I just compiled 4.6, made a fresh clone, and I could apply all the patches without any problem:


```
timo`@`ukko:~/sage-4.6/devel/sage-haha$ ../../sage -hg qseries
trac_8431_e_one_star.patch
trac_8431_review-sl.patch
trac_8431_might_be_final_tj.patch
trac_8431_colors_tikz-sl.patch
trac_8431_sigma_type_fix.patch
trac_8431-wordmorphism-sl.patch
trac_8431-smallfixes-tj.patch
trac_8431-alphaset-tj.patch
timo`@`ukko:~/sage-4.6/devel/sage-haha$ ../../sage -hg qtop
trac_8431-alphaset-tj.patch
timo`@`ukko:~/sage-4.6/devel/sage-haha$ ../../sage -hg qpop
now at: trac_8431-smallfixes-tj.patch
timo`@`ukko:~/sage-4.6/devel/sage-haha$ ../../sage -hg qpop
now at: trac_8431-wordmorphism-sl.patch
timo`@`ukko:~/sage-4.6/devel/sage-haha$ ../../sage -hg qpush
applying trac_8431-smallfixes-tj.patch
now at: trac_8431-smallfixes-tj.patch
timo`@`ukko:~/sage-4.6/devel/sage-haha$ ../../sage -hg qpush
applying trac_8431-alphaset-tj.patch
now at: trac_8431-alphaset-tj.patch
```

Could you try it again? There's no reason that it works for me but not for you!

(And don't forget the last patch `trac_8431-alphaset-tj.patch` !)

To recap, the order is:

 1. trac_8431_e_one_star.patch
 1. trac_8431_review-sl.patch
 1. trac_8431_might_be_final_tj.patch
 1. trac_8431_colors_tikz-sl.patch
 1. trac_8431_sigma_type_fix.patch
 1. trac_8431-wordmorphism-sl.patch
 1. trac_8431-smallfixes-tj.patch
 1. trac_8431-alphaset-tj.patch

[BTW, a question: when I need to apply such a sequence of patches, do I have to do "`import, qpush, import, qpush, import, qpush, ...`", with an `import` and a `qpush` for each patch ?]


---

Attachment

Hi. Sorry, this error message was because of a manipulation error from my part. (I misapplied the wordmorphism-sl patch, and my two last patches were based on this misapplying.)

I made a new patch that applies correctly over wordmorphism-sl, and that takes into account my two last patches (which should now be ignored; it's a shame that we can't delete patches from the ticket!).

Patches should be applied in this order:

 1. trac_8431_e_one_star.patch
 1. trac_8431_review-sl.patch
 1. trac_8431_might_be_final_tj.patch
 1. trac_8431_colors_tikz-sl.patch
 1. trac_8431_sigma_type_fix.patch
 1. trac_8431-wordmorphism-sl.patch
 1. trac_new-fixes-final-tj.patch

(Sorry for misnaming the last patch, I forgot "8431"... And sorry if this made you lose some time!)


---

Attachment


---

Comment by tjolivet created at 2010-11-13 16:46:51

Thanks for you final remarks. The last patch is trac_8431_typos-docfix-tj.patch, and the sequence is:

 1. trac_8431_e_one_star.patch
 1. trac_8431_review-sl.patch
 1. trac_8431_might_be_final_tj.patch
 1. trac_8431_colors_tikz-sl.patch
 1. trac_8431_sigma_type_fix.patch
 1. trac_8431-wordmorphism-sl.patch
 1. trac_new-fixes-final-tj.patch
 1. trac_8431_typos-docfix-tj.patch


---

Comment by abmasse created at 2010-11-13 17:08:49

Apply on top of preceding patches


---

Attachment

Hi Timo and Sébastien !

I just uploaded a (I hope last) patch that fixes a minor doctest failure (decimal number, on my computer but not Timo's).

I tested all of it on sage-4.6. I'm satisfied with the code and the documentation looks good (no warning neither).

Before setting this ticket to "positive review", I want to know if Sébastien is ok with it, since he reviewed big parts, and if Timo agrees with my last patch (Timo, just make sure it still passes on your machine).


---

Comment by tjolivet created at 2010-11-13 18:02:00

Yes, the patch applies fine, and the doctest passes. Everything seems to be fine now.

Just a recap:

 1. trac_8431_e_one_star.patch
 1. trac_8431_review-sl.patch
 1. trac_8431_might_be_final_tj.patch
 1. trac_8431_colors_tikz-sl.patch
 1. trac_8431_sigma_type_fix.patch
 1. trac_8431-wordmorphism-sl.patch
 1. trac_new-fixes-final-tj.patch
 1. trac_8431_typos-docfix-tj.patch
 1. trac_8431_doctest_fix-abm.patch


---

Comment by slabbe created at 2010-11-14 01:17:31

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2010-11-14 01:17:31

> Before setting this ticket to "positive review", I want to know if Sébastien is ok with it, since he reviewed big parts, and if Timo agrees with my last patch (Timo, just make sure it still passes on your machine).

All test pass on my machine. Coverage is 100%. Documentation builds fine. Positive review!

I just folded the 9 patches into one : trac_8431_folded.patch. It might be easier for the release manager.

Great work!


---

Comment by jdemeyer created at 2010-11-15 12:34:59

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-11-15 12:34:59

1) Please update the commit message of the folded patch (use `hg qrefresh -e` for that).  Make sure the first line contains the ticket number and a short summary of the whole patch.  The next lines can contain a longer description.

2) The copyright message in the files MUST be changed to state

```
#  Distributed under the terms of the GNU General Public License (GPL) 
#  as published by the Free Software Foundation; either version 2 of 
#  the License, or (at your option) any later version.  
#                  http://www.gnu.org/licenses/  
#***************************************************************************** 
```



---

Comment by slabbe created at 2010-11-15 14:12:43

Folded all the 9 appropriate patches.


---

Attachment

I just re-uploaded the folded patch.

> 1) Please update the commit message of the folded patch (use `hg qrefresh -e` for that).

Done.

> 2) The copyright message in the files MUST be changed to state

Done. I did not know the copyright message changed.

Needs review.


---

Comment by slabbe created at 2010-11-15 14:15:31

Changing status from needs_work to needs_review.


---

Comment by abmasse created at 2010-11-15 14:53:03

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-11-15 14:53:03

I just checked that the fixes required by the release manager have indeed been done.

All tests still pass.

Positive review.


---

Comment by jdemeyer created at 2010-11-19 07:53:54

Resolution: fixed
