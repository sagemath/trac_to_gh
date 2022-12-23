# Issue 7488: plot3d? doesn't document some important options, which causes confusion

Issue created by migration from https://trac.sagemath.org/ticket/7488

Original creator: was

Original creation time: 2009-11-18 17:32:44

Assignee: was


```


On Wed, Nov 18, 2009 at 9:16 AM, Laurent <> wrote:
> Hi.
>
> I'm writing the following code in order to plot sin(x^2+x^2) :
>
> var('x,y')
> g(x,y)=sin(x**2+y**2)
> plot3d(g(x,y),(x,-5,5),(y,-5,5))
>
> My problem is that the result is quite bad because of the sampling : all
> the points with x^2+y^2=pi/2 are not taken, so that I don't get
> beautiful circles.
>
> How can I ask for a finer sampling, or to compute more intermediate points ?

Use the plot_points option.  Type "parametric_plot3d?" for more details:

        -  ``plot_points`` - (default: "automatic", which is
           75 for curves and [40,40] for surfaces) initial number of sample
           points in each parameter; an integer for a curve, and a pair of
           integers for a surface.
        
Note that the documentation output by "plot3d?" doesn't even mention the plot_points option, which is why you're confused.  

William



 -- William

> I'm sure there is an option to add, but I don't see in the documentation
> which one. (I'm reading the Sage reference manual, version 4.1.1, Agust
> 14 2009).


---

Attachment


---

Comment by was created at 2009-11-18 18:08:57

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-18 18:10:49

Looks good to me.


---

Comment by mhansen created at 2009-11-18 18:10:49

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-19 10:16:13

Resolution: fixed
