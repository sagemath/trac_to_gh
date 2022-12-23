# Issue 3836: notebook interact -- make it so one control can depend on others

Issue created by migration from https://trac.sagemath.org/ticket/3836

Original creator: was

Original creation time: 2008-08-13 16:12:38

Assignee: boothby

CC:  timdumol mpatel jason


```

I really like the @interact functionality! I'm trying to do something
like this:

@interact
def _(p=5,q=range(p)):
   ...

So I'd like the range of q to depend on the current value of p. This
doesn't seem to be possible. Is there any way to make it work?
```



---

Comment by TimothyClemans created at 2008-09-09 19:23:45

Changing component from notebook to interact.


---

Comment by TimothyClemans created at 2008-09-09 19:23:45

Changing assignee from boothby to itolkov.


---

Comment by kcrisman created at 2009-10-21 15:21:40

Here is another request from [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/a0292dca53c3be16/682f8ae33df29761?show_docid=682f8ae33df29761) which seems very similar.

I want to know if there is any way to "create" new buttons while 
already in execution. 

This is a testing code i wrote (of course, just for testing 
purposes :P) 

```
@interact 
def _(n1=input_box(0,label='Testing', type=int),a=selector([1,2,7], 
buttons=True), n2=input_box(1,label='Testing2',type=int), 
juega=input_box(0,label='Testing3',type=int)): 
    if(n1>0): 
        print 'hi' 
        another_function() 
def another_function(t1=input_box(0,label='Testing123')): 
    print 'hola' 
```

Thing is, when i run it, i can get it to print 'Hola' but no input_box 
is created again. I've managed to "make" one using html, but i can't 
get to "interact" with it. 

What i'm thinking on doing is a program that has several options using 
a selector, e.g. if you choose 1 then it should appear a grid so that 
when u enter matrix values it does some calcs, if you choose 2 then it 
should appear an input box, and so on...


---

Comment by kcrisman created at 2012-01-17 23:27:52

Turns out that this is going to be available once it makes its way back from the single-cell server code!  See [this ask.sagemath.org question](http://ask.sagemath.org/question/1061/), in particular Jason's answer.


---

Comment by jdemeyer created at 2017-03-21 11:17:22

This can be done in Jupyter, using traitlets links.
