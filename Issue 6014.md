# Issue 6014: hexads in S(5,6,12) and mathematical blackjack

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2009-05-10 12:56:56

Assignee: rlm

Keywords: combinatorics, coding theory

This patch implements kittens, hexads and mathematical blackjack as explained in


```
    R. Curtis, ``The Steiner system $S(5,6,12)$, the Mathieu group $M_{12}$, 
    and the kitten,'' in {\bf Computational group theory}, ed. M. Atkinson, 
    Academic Press, 1984.
    J. Conway, ``Hexacode and tetracode - MINIMOG and MOG,'' in {\bf Computational 
    group theory}, ed. M. Atkinson, Academic Press, 1984.
    J. Conway and N. Sloane, ``Lexicographic codes: error-correcting codes from 
    game theory,'' IEEE Trans. Infor. Theory32(1986)337-348.
    J. Kahane and A. Ryba, ``The hexad game,'' Electronic Journal of Combinatorics, 8 (2001) 
    http://www.combinatorics.org/Volume_8/Abstracts/v8i2r11.html
```


It is used in a book on coding theory I'm writing with Jon-Lark Kim on coding theory, which uses Sage throughout to illustrate error-correcting codes.



---

Comment by wdj created at 2009-05-10 12:58:53

applies to 3.4.2 and passes sage -testall


---

Attachment


---

Comment by dgordon created at 2009-06-01 18:46:08

After reviewing the patch I think that it looks good overall, but there is one major problem.  In setting_up() various global variables are created with information for minimog_shuffle.  The find_hexad() functions take MINIMOG as an argument, but use the minimog_shuffle global variables.  Right now this is the only minimog implemented, but if minimog_modulo11 is implemented in the future, other changes would be needed.

Instead of having the global variables separate from the minimog, why not define a class minimog, which contains all the line, cross, tet, and other information.  This would take care of the above problem, and be better programming practice.  

Also, is it really that difficult to implement minimog_modulo11?  I think the only problem is that then the minimog can't be defined as a matrix over QQ.  Since there aren't any arithmetic operations being done to the matrix elements, this shouldn't be a real impediment.  If the minimogs are implemented as classes, then a function could be added to convert minimog elements to strings that handles infinity.


---

Attachment


---

Comment by wdj created at 2009-06-03 12:22:42

This implements the referee's suggestions, passes sage -testall on 4.0.1.a0 on a 64bit ubuntu 9.04 machine(except for the problem with html.py, which was already reported as a separate issue). Also, sage -docbuild reference html worked without errors.

Both patches need to be applied.


---

Attachment

to be applied after the other two


---

Attachment


---

Comment by wdj created at 2009-06-04 02:38:38

These patches add the examples suggested by the referee.

One odd thing is that it appears that a list of elements containing infinity is sorted differently on an intel mac than on an ubuntu machine.
Because of this, I had to add a # random comment to a docstring.


---

Comment by ncalexan created at 2009-06-13 21:45:34

Resolution: fixed
