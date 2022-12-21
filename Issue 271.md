# Issue 271: defining classes in the notebook with examples

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-02-20 22:09:04

Assignee: was

Executable examples in comments seem to interfere with the creation of class definitions in the notebook:

We define a class in a notebook cell without executable example:

```
class test1():
  """
  doc here
  """

  def __init__(self):
    """
    EXAMPLES:
      asage: print "there you are!"
      there you are!
    """
    print "here I am!"
```


We test it and successfully create the class:

```
A=test1()
///
here I am!
```


Same example, but now the example is executable. Note that we get the result from the example.

```
class test2():
  """
  doc here
  """

  def __init__(self):
    """
    EXAMPLES:
      sage: print "there you are!"
      there you are!
    """
    print "here I am!"
///
there you are!
```


But creating an instance of this class now fails:

```
B=test2()
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/sage/nobody/sage_notebook/worksheets/test/code/20.py", line 4, in <module>
    exec compile(ur'B=test2()' + '\n', '', 'single')
  File "/usr/local/sage/nobody/", line 1, in <module>
    
NameError: name 'test2' is not defined
```




---

Comment by TimothyClemans created at 2007-03-01 01:59:10

Same as ticket #228


---

Comment by TimothyClemans created at 2007-03-26 03:35:47

Resolution: duplicate


---

Comment by kohel created at 2007-03-26 05:48:06

Changing status from closed to reopened.


---

Comment by kohel created at 2007-03-26 05:48:06

Resolution changed from duplicate to 


---

Comment by kohel created at 2007-03-26 05:48:06

Changing component from packages to user interface.


---

Comment by TimothyClemans created at 2007-04-03 06:18:14

Resolution: fixed
