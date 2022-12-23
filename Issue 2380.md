# Issue 2380: make plot give an array of plots when passed an "array" option

Issue created by migration from https://trac.sagemath.org/ticket/2380

Original creator: jason

Original creation time: 2008-03-03 22:48:12

Assignee: was

From the remains of #2350

Make it so that:

    * plot(list) does what it currently does (i.e., superimpose the plots) 

    * plot(list, array=True) does what show does in 2.10.2 (i.e., put the plots into an array).

    * change the docs to show() to more clearly reflect the purpose of the function. 
