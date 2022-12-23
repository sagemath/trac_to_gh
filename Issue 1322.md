# Issue 1322: interactive widgets in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/1322

Original creator: jason

Original creation time: 2007-11-28 20:16:45

Assignee: mhansen

CC:  jason-sage@creativetrax.com mhansen timothyclemans

Keywords: graphs

See mailing list discussions at 

[http://groups.google.com/group/sage-devel/browse_thread/thread/f0119a34ca55e95f/65bf86aef687c6d2?lnk=gst&q=interactive#65bf86aef687c6d2](http://groups.google.com/group/sage-devel/browse_thread/thread/f0119a34ca55e95f/65bf86aef687c6d2?lnk=gst&q=interactive#65bf86aef687c6d2)

and 
[http://groups.google.com/group/sage-devel/browse_thread/thread/db30b40ab36aa51c/2157c72c6cc50dfe?lnk=gst&q=Manipulate#2157c72c6cc50dfe](http://groups.google.com/group/sage-devel/browse_thread/thread/db30b40ab36aa51c/2157c72c6cc50dfe?lnk=gst&q=Manipulate#2157c72c6cc50dfe)

Also, from Robert Miller (to Jason Grout):


```
> I was brainstorming about something like widgets a while ago, before
> the notebook underwent its sea change. We (>= you and I) should make
> this a coding sprint at SD7.
```



---

Comment by jason created at 2007-11-30 01:06:00

Test to see if CC feature is working.


---

Comment by jason created at 2007-11-30 20:14:34

See also the thread:

[http://groups.google.com/group/sage-devel/browse_thread/thread/9bc46be5632fe3f1/a86393f145b72f31#a86393f145b72f31](http://groups.google.com/group/sage-devel/browse_thread/thread/9bc46be5632fe3f1/a86393f145b72f31#a86393f145b72f31)


---

Attachment

Extremely rough cut of initial functionality for interactive widgets in the notebook.


---

Comment by jason created at 2007-12-01 06:52:11

There are several problems with the way things are done in menu-widget.patch:

 * We rely on a complete hack of sending an AJAX request with an invalid cell id (-1).  The webserver complains ("Warning -- cell -1 no longer exists"), but the code is still executed and everything seems fine.  So it'd be great if we could remove the warning and call it a feature :).
 * The variable is not set initially.  You have to select a value before using the variable.  The variable is not set initially because I couldn't figure out how to set a global variable from within the menu.__init__ function.  We could probably look into the polynomial ring stuff and figure out how to inject variables into the global namespace.  I have a rough cython file written that attempts to define an "inject_global" function that injects a variable into the global namespace, but when this function is called from menu.__init__, it doesn't inject into the global namespace.
 * When a value is updated via the menu, it doesn't change or reevaluate any cells in the notebook.  It would be very nice to automatically evaluate other cells in the notebook to get real-time dynamic feedback from picking new values from the menu.
 * When manually reevaluating cells, it seems to display the old value first and then update to the new value.  This is very annoying and takes time and looks bad.
 * There should be some sort of caching eventually implemented to make things faster.  Maybe something like a directive "%depends_on(x)" to say that a cell's output only depends on x.  In other words, if x is the same, then we can spit out a cached copy of the cell's output instead of having to reevaluate the cell.

The menu select box is the tip of the iceberg here.  It'd be nice to have fancy sliders and things like that using javascript.


---

Comment by jason created at 2007-12-01 06:54:45

Oh, and one more thing: we currently have to import the function:


```
sage: from sage.server.notebook.widgets.menu import menu
sage: menu('f',[sin,cos,tan]).show()

(a menu is shown.  pick a value for f)

sage: plot(f(x),0,2*pi).show()

(the plot of f(x) (with the selected f) is shown.)

```



---

Comment by jason created at 2007-12-01 07:12:42

Changing component from combinatorics to notebook.


---

Comment by jason created at 2007-12-01 07:12:42

Changing keywords from "graphs" to "".


---

Comment by jason created at 2007-12-01 07:12:42

Changing assignee from mhansen to boothby.


---

Comment by jason created at 2007-12-01 08:01:32

It appears that the warning about a nonexistant cell comes from the line 


```
            s = encode_list([cell.next_id(), 'no_new_cell', str(id)])
```


in sage/server/notebook/twisted.py


---

Comment by jason created at 2007-12-01 19:01:48

In addition to applying the first patch above, you need to create an empty __init__.py file in sage/server/notebook/widgets/


---

Comment by was created at 2008-02-07 07:29:08

See also #1613....


---

Comment by was created at 2008-02-07 07:30:30

Here is a trivial example.  You *must* change 155 to an actual
existing blank output cell. 


```
def manipulate():
    print r""" 
    <html>
<script>
function manip(id, cmd) {
   var cell_input = get_cell(id);
   cell_input.value = cmd;
   cell_input.style.display = "none";
   evaluate_cell(id, 0);
}
</script>
    <input type="button" value="sin(x)" onclick="manip(155, 'plot(sin,-1,1)')">
    <input type="button" value="cos(x)" onclick="manip(155, 'plot(cos,-1,1)')">
    <input type="button" value="tan(x)" onclick="manip(155, 'plot(tan,-1,1)')">
    <input type="button" value="sin(x^2)" onclick="manip(155, 'plot(sin(x^2),-1,1)')">
    </html>
"""
```



---

Comment by jason created at 2008-02-07 09:46:55

More stuff:


```
print r"""
<html>
<script>
function manip(id,cmd, variable, value) {
    var cell_input = get_cell(id);
    cell_input.value = variable+"="+value+"\n"+cmd;
    cell_input.style.display = "none";
    evaluate_cell(id, 0);
}
</script>
</html>
"""
```


and 


```
def menu(cmd, variable, options):
    ret = """<select name='' onchange='manip(%d,"%s", "%s", this.options[this.selectedIndex].value)'>"""%(__SAGE_NOTEBOOK_CELL_ID__+1,cmd,variable)
    for option in options:
        ret += "<option value='%s'>%s</option>"%(repr(option), repr(option))
    ret += "</select>"
    return ret

def manipulate(cmd, variables):
    controls=''
    for key,val in variables.items():
        controls += menu(cmd, key, val)
    print "<html>"+controls+"</html>"
```


and 


```
manipulate('plot(f(x),(x,0,3))', {'f':[sin,cos,tan]})
```



---

Comment by jason created at 2008-02-13 20:35:28

with "manipulate.patch", here is a trivial example.  You *must* change the CELL_ID to the id of an existing cell.  That cell will be overwritten.

manipulate("factor(y)", {'y': TextBox(100)}, CELL_ID)

manipulate("factor(y)", {'y': Menu([2, 4, 6, 8])}, CELL_ID)

manipulate("factor(y)", {'y': ButtonGroup([2, 4, 6, 8])}, CELL_ID)

manipulate("factor(y)", {'y': CheckBox(checked=10, unchecked=20)}, CELL_ID)

manipulate("factor(p*y)", {'p': TextBox(100), 'y': Menu([(x-1),x^2-2*x+1])}, CELL_ID)
 

(Note to self: fix the bug of printing the menu using str instead of repr, so x^2 looks like 2x)


---

Comment by jason created at 2008-02-13 20:36:19

A different very rough cut of functionality.


---

Attachment

Wow, this is a lot of fun!

Here's another, more interesting example.  (This uses a CELL_ID of zero, so the first cell in your notebook will be overwritten.)

```
x = polygen(ZZ)
coeff_range = ButtonGroup([-4,-3,-2,-1,0,1,2,3,4])
manipulate("p = a*x^4 + b*x^3 + c*x^2 + d*x + e; show(plot(p, -4, 4)); show(p); p.roots(ring=RR)", 
           {'a': coeff_range,
            'b': coeff_range,
            'c': coeff_range,
            'd': coeff_range,
            'e': coeff_range}, 0)
```


Just judging from the functionality, I'd be willing to give a positive review once these two issues were addressed.  (I haven't read the code yet, though.)

1. Having to specify a CELL_ID is lame.

2. The API of specifying a dictionary is bad.  In the above example, the controls don't appear in the expected order (a,b,c,d,e); but that can't be fixed in manipulate, because it doesn't know what order you used when you typed the dictionary literal.  Instead, manipulate should take a list of pairs.

Wishlist items:

1. Slider bars would be nice.

2. Widgets should be labeled with the variable name they control.

3. The syntax is pretty ugly.  I haven't thought of a way to fix that without some sort of preparser; here's a first suggestion for a preparser-based syntax:

```
%manipulate
x : Menu([2,4,6,8])
y : Menu([1,10,100,1000])
--
x^y
```

For extra bonus points, this could work in conjunction with %pari/%magma/etc.


---

Attachment

this is independent of the patches above -- it's standalone -- see comments below for how to use.


---

Comment by was created at 2008-03-01 10:32:44

This patch manipulate-take3.patch is a completely totally different approach to the whole manipulate thing.  It is just a prototype!!! It's not supposed to work perfectly, in particular, you must enter a number first and press return to see anything.
Anyway, here are some example inputs (each should be entered in its own cell):


```
@manipulate
def myfactor(n):
    print jsmath(factor(n))


@manipulate
def polys(m):
    R = QQ['x']
    f = R.random_element(m)
    print "f = ", jsmath(f)
    print "real roots = ", f.real_roots()
    show(plot(f))



@manipulate
def ellcurve(label):
    E = EllipticCurve(label)
    show(E)
    show("E conductor = %s"%E.conductor())
    show(E.q_eigenform(7))
    show(plot(E))



@manipulate
def pl(n):
    var('x,y')
    show(x^n-y^n)
    show(plot3d(x^n-y^n, (x,-2,2), (y,-2,2)))

```



---

Comment by TimothyClemans created at 2008-03-02 01:09:00

I love the new code by William.

Here is my first example using it:

```
@manipulate
def gcd_steps(numbers):
    a, b = numbers
    w = a
    y = b
    while True:
        x, z = divmod(w, y)
        print '%d = %d * %d + %d' % (w, x, y, z)
        if not z:
            break
        w = y
        y = z
```



---

Attachment

part 2 of manipulate with decorators; this is usable again (probably) better docs; but there are several things to do soon and I'm too tired.


---

Comment by was created at 2008-03-02 15:31:47

Here is the patch that adds full jquery and uijquery support to sage.  apply
it against the extcode repo.

http://sage.math.washington.edu/home/was/patches/extcode-add_jquery_support.patch


---

Comment by was created at 2008-03-02 15:33:39

Examples of how to use the version as of now:

```
@manipulate
def foo(f=text_box("sin(x)"), L=slider(-5,0), U=slider(0,5)):
    return plot(f,L,U)
```



```
@manipulate
def bar(a,b=slider([1..10])):
    return a+b
```



```
@manipulate
def ec(a,b):
    E = EllipticCurve([a,b])
    html("<h1>Data about an Elliptic Curve</h1>")
    print E.cremona_label()
    show(E)
    show(plot(E))
    show(E.q_eigenform(30))
    show(E.torsion_order())
```



---

Attachment

this requires that you also install the extcode patch that gives jquery support.


---

Comment by was created at 2008-03-03 02:09:26

Examples as of manipulate_take3_part3.patch

```
@manipulate
def factor_example(n=range(2,1000)):
    F = factor(n)
    html("<h1 align=center><font color='darkblue' size=+4>factor(%s) = %s</font></h1>"%(n, F))



@manipulate
def foo(f, xmax=[0,0.1,..20]):
    show(f)
    show(plot(f, -1, xmax))

@manipulate
def pl(n=[0..30], xmin=[-5..0], xmax=[0..10]):
    print n, xmin, xmax
    f = sin(n*x); g = cos(n*x)
    show(plot(f,xmin,xmax) + plot(g,xmin,xmax,color='red'), figsize=[5,2], xmin=xmin, xmax=xmax)


@manipulate
def pl(n=[100,200,..,10^4]):
    html("<h1 align=center>Primes up to %s</h1>"%n)
    show(plot(prime_pi, 1, n) + plot(x/(log(x)-1), 0.1, n, color='red'))


@manipulate
def a3dplot(a=[1..10], b=[1..10]):
    var('x,y')
    f = x^a + y^b
    show(f)
    show(plot3d(f, (x,-2,2), (y,-2,2)))

```



---

Comment by was created at 2008-03-03 04:26:39

HI: I've put a bundle at 

    http://sage.math.washington.edu/home/was/patches/manipulate.hg

since people were having trouble applying the plain text patches. 

William


---

Comment by was created at 2008-03-03 04:46:14

To get this to work, install jquery as follows:

Get 

http://sage.math.washington.edu/home/was/patches/jquery.tar.bz2 

and unpack it in SAGE_ROOT


---

Comment by was created at 2008-03-03 04:47:28

Oops, actually extract 

http://sage.math.washington.edu/home/was/patches/jquery.tar.bz2

in SAGE_ROOT/data/

Sorry for all the trouble.


---

Attachment


---

Attachment

this is a new better version


---

Comment by was created at 2008-03-07 18:50:42

I am now posting the hg bundle for people who want to try this out here:

http://sage.math.washington.edu/home/was/patches/interact.hg


---

Comment by was created at 2008-03-07 18:50:42

Changing status from new to assigned.


---

Comment by was created at 2008-03-07 18:50:42

Changing assignee from boothby to was.


---

Comment by was created at 2008-03-09 23:46:43

Resolution: duplicate
