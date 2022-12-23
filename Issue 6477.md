# Issue 6477: notebook -- improve UNICODE handling of truncated_name function in worksheet.py

Issue created by migration from https://trac.sagemath.org/ticket/6477

Original creator: was

Original creation time: 2009-07-08 01:43:54

Assignee: boothby


```
Hello.

I use Sagemath to show the Linear Algebra problems solution.

And I am Korean.

Therefore I write the title in Korean.
```


http://nosyu.pe.kr/attach/1/5682987737.png


```
But in worksheet,  the title is broken because of truncated_name
function in worksheet.py.


def truncated_name(self, max=30):
       name = self.name()
       if len(name) > max:
           name = name[:max] + ' ...'
       return name


But Unicode is not 1 byte by character.

So Korean is broken if max is midpoint of Korean one character.

Therefore I modify the function code like this.


def truncated_name(self, max=30):
       name = unicode(self.name(), "utf-8") # name = self.name()
       if len(name) > max:
           name = name[:max] + ' ...'
       return name.encode('utf-8') # return name


Now name is encoded by unicode, then Korean one character's length is
1, not 2 or 3.

So I can see the right title.


I think there are more good choice to solve the problem.
Because I don't know about Python well and unicode also.
So I suggest this.
```



---

Comment by timdumol created at 2010-01-19 07:24:34

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 07:24:34

I'll mark this as a duplicate since #7249 subsumes this.
