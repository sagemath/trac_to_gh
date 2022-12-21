# Issue 1660: maxima interface bug caused by bad use of file when evaluating large input

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-02 21:07:38

Assignee: was


```
> That's weird.  Can you post the _exact_ input
> and output from a complete session where you get
> sage1 as the output from maxima.eval('...')?  Thanks.
>

This is it:
lwdrob`@`lwdrob-comp:~/Disertatie$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9.1, Release Date: 2007-12-24                       |
| Type notebook() for the GUI, and license() for information.        |
sage:
maxima.eval('plot2d([-7.5/-0.5*(x-0.5)+8,-7.5/7.5*(x-0.5)+8,-6.5/-0.5*(x-0.5)+8,-6.5/7.5*(x-0.5)+8,-5.5/-0.5*(x-0.5)+8,'+
\
....:
'-5.5/7.5*(x-0.5)+8,-4.5/-0.5*(x-0.5)+8,-4.5/7.5*(x-0.5)+8,-3.5/-0.5*(x-0.5)+8,-3.5/7.5*(x-0.5)+8,-2.5/-0.5*(x-0.5)+8,'+
\
....:
'-2.5/7.5*(x-0.5)+8,-1.5/-0.5*(x-0.5)+8,-1.5/7.5*(x-0.5)+8,-0.5/-0.5*(x-0.5)+8,-0.5/7.5*(x-0.5)+8],'+
\
....: '[x,0,n],[plot_format,gnuplot_pipes],[y, 0, 8],[ylabel,"y"],
[gnuplot_preamble, "set grid xtics ytics"],[legend,false])')
'sage0'
sage:

There is a tmp file containing the above cmd:
$cat /home/lwdrob/.sage/temp/lwdrob_comp/7280/interface/tmp
sage0 :
plot2d([-7.5/-0.5*(x-0.5)+8,-7.5/7.5*(x-0.5)+8,-6.5/-0.5*(x-0.5)+8,-6.5/7.5*(x-0.5)+8,-5.5/-0.5*(x-0.5)+8,
-5.5/7.5*(x-0.5)+8,-4.5/-0.5*(x-0.5)+8,-4.5/7.5*(x-0.5)+8,-3.5/-0.5*(x-0.5)+8,-3.5/7.5*(x-0.5)+8,-2.5/-0.5*(x-0.5)+8,
-2.5/7.5*(x-0.5)+8,-1.5/-0.5*(x-0.5)+8,-1.5/7.5*(x-0.5)+8,-0.5/-0.5*(x-0.5)+8,-0.5/7.5*(x-0.5)+8],
[x,0,n], [plot_format,gnuplot_pipes], [y,0,8],[ylabel,"y"],
[gnuplot_preamble, "set grid xtics ytics"],[legend,false])$

Best regards,
```


The problem is that the maxima interface should not be assigning to a variable when using a file to evaluate a large input. 

William
