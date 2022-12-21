# Issue 5220: Weird or non-appearance of default in input_box in interact

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-02-09 15:35:45

Assignee: boothby

From sage-support:


```
On sagenb.org, try making an interact with an input box explicitly 
defined, e.g. 
`@`interact 
def plotfunction(f=input_box(x^2)): 
    P=plot(f,0,1) 
    show(P) 
It works fine in the sense that whatever you type in does what it 
should.  But what's up with how the input box appears?  It's even 
worse on my box (PPC OSX.4) - the initial input does not show up *at 
all* in the box, though again the plot is fine and once you type 
something in it behaves normally. 
```




```
I'm able to reproduce this on sagenb.org on a Mac with FF3. 
```




---

Comment by kcrisman created at 2009-02-09 16:33:02

Behavior seems to be unrelated to #4524, though that is a possibility.  

Using default=x^2 still creates graph, doesn't put anything in input box.  Using default="x^2" or default='x^2' puts something in input box, but then yields an "invalid literal for float(): x^2" error when actually plotting.


---

Comment by kcrisman created at 2009-02-09 16:35:25

Replying to [comment:1 kcrisman]:
> Behavior seems to be unrelated to #4524, though that is a possibility.  
> 
> 
Using 

```
default=x^2 
```

still creates graph, doesn't put anything in input box.  Using 

```
default="x^2"
```

or

```
default='x^2'
}}} 
puts something in input box, but then yields an 
{{{
"invalid literal for float(): x^2"
}}} 
error when actually plotting.


---

Comment by jason created at 2009-02-09 20:20:41

The problem is a str versus repr call in the interact code.  I've attached a patch which fixes the issue, but it changes how interact is needs to be used.  Personally, I think the behavior with the patch should be the correct behavior.


---

Attachment

Note that the attached patch changes two other doctests in the affected function.  This should be discussed, as this changes how interacts work, I believe.


---

Comment by jason created at 2009-03-05 02:10:01

See the mailing list discussion at http://groups.google.com/group/sage-support/browse_thread/thread/c01b61836bc53339/00cebbec4da5304c for how interact changes after this patch.  Basically, doing:


```
`@`interact
def plotfunction(f=input_box('x^2')):
     print f 
```


used to make an input box with x^2 in it.  Now it literally puts the string 'x^2' (with quote marks) in the input box.  In order to make an input box with x^2 in it after the patch, you need to do:


```
`@`interact
def plotfunction(f=input_box(x^2)):
     print f 
```


or even


```
`@`interact
def plotfunction(f=x^2):
     print f 
```



---

Comment by jason created at 2009-03-05 02:16:26

P.S. I can see why having


```
`@`interact
def plotfunction(f=input_box('x^2')):
     print f 
```


produce x^2 in the input box would be good too, though.  There are lots of types in Sage for which repr does not give you back a string that can be used to reconstruct the object.  For example, I believe that after the patch, 

```
`@`interact
def plotfunction(f=input_box(RIF(3.2,3.4))):
     print f 
```


will produce an input box that has "3.3?" in it (without quotation marks).  Of course, this is nonsense.  For that reason, I can see changing how default values are handled to allow:


```
`@`interact
def plotfunction(f=input_box('RIF(3.2,3.4)')):
     print f 
```


to produce an input box with "RIF(3.2,3.4)" (without quotation marks) in it.  This means that to make an input box containing a string (with quotation marks), you'll have to do something like:


```
`@`interact
def plotfunction(f=input_box("'my string'")):
     print f 
```

(i.e., double-quote your string).


---

Attachment


---

Comment by was created at 2009-03-05 05:22:48

I reviewed the patch, noticed it broke a doctest from #4524, fixed that, and in so doing I think I implemented exactly what Jason suggests above in the comment 3 hours ago.


---

Comment by jason created at 2009-03-05 05:43:15

The changes was made look good.  I haven't applied it or tested it, but it's exactly what I was thinking of in my comments above.


Gee, William, I wish you had a nick that didn't make my grammar look so bad!


---

Comment by mabshoff created at 2009-03-08 06:49:19

Merged both patches in Sage 3.4.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-08 06:49:19

Resolution: fixed
