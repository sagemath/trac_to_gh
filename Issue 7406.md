# Issue 7406: bug in conversion powers in to LaTeX

Issue created by migration from https://trac.sagemath.org/ticket/7406

Original creator: robert.marik

Original creation time: 2009-11-06 20:37:51

Assignee: burcin

Keywords: latex, power, jsmath

The LaTeX representation of (x<sup>pi)</sup>e is not valid TeX string and is not rendered by jsmath

```
sage: latex((x^pi)^e)
{(x)}^{\pi}^{e}
```


Burcin [suggested](http://groups.google.cz/group/sage-devel/browse_thread/thread/c49c684f1c89d0c4) how to fix this and get output like 

```
{{(x)}^{\pi}}^{e}
```



```
The code for printing
symbolic expressions is in pynac (C++). The fix can be as simple as
printing an extra set of braces around power objects.

If anybody wants to try fixing this, the relevant function is
power::do_print_latex() in power.cpp. To get to the file (using the
instructions I wrote in another message just now), go to your SAGE_ROOT
and do:

./sage -f -s spkg/standard/pynac-0.1.9.p0.spkg

cd spkg/build/pynac-0.1.9/src/ginac

Edit power.cpp. To compile and make your changes effective, go to your
SAGE_ROOT again, and do

./sage -sh
cd spkg/build/pynac-0.1.9/src
make install 
```


However a better fix would be to get 

```
{x}^{a}
```

if the base is an atom (or not power) and

```
\left({x^a}\right}^{b}
```

if the base is a power. This allows to distinguish easily between

```
x^(a^b) 
```

and 

```
(x^a)^b
```


A workaround is to remove powers of powers by simplification. For example radcan function from Maxima perfoms such simplifications

```
sage: latex(maxima((x^pi)^e).radcan().sage())
x^{\pi e}
```



---

Comment by robert.marik created at 2009-11-21 23:06:25

Changing keywords from "latex, power, jsmath" to "latex, power, jsmath, pynac".


---

Comment by robert.marik created at 2009-11-21 23:09:25

Perhaps close problem is

```
sage: latex(x*(1/(x^2)+sqrt(x^7)))
{(\sqrt{x^{7}} + \frac{1}{x^{2}})} x
```


Note missing \left and \right at outside parentheses which makes the rendering of the expression far from perfect. Should look like

```
sage: latex(x*(1/(x^2)+sqrt(x^7)))
{\left(\sqrt{x^{7}} + \frac{1}{x^{2}}\right)} x
```



---

Comment by burcin created at 2009-11-22 17:11:49

add doctests


---

Attachment

The new pynac package here

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.spkg

contains fixes for both the problem in the description and the one in comment:3.

attachment:trac_7406-power_latex.patch contains doctests for the fix.

Note that the new pynac version also contains fixes for #7508 and #7264. Tests should be run with the patches from those tickets also applied in this order:

    * #7508
    * #7264 
    * #7406 (this ticket)

This ticket now depends on #7490, #7508 and #7264.


---

Comment by burcin created at 2009-11-22 18:11:40

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-05 13:51:44

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-12-05 13:51:44

Positive review - they look great in show()!  Obviously pending #7264 or a rebase.


---

Comment by mhansen created at 2009-12-10 14:22:58

Resolution: fixed
