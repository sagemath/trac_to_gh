# Issue 7850: spherical plot

archive/issues_007850.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: spherical,plot\n\nI've made a clone of Mathematicas SphericalPlot3d . Only that the 3d seemed redundant to me.\n\nThe code is\n\n```\nvar('phi,theta')\ndef spherical_plot(f,phiran=(phi,0,2*pi),thetaran=(theta,0,pi),**kwds):\n   phi=phiran[0]\n   phi0=phiran[1]\n   phif=phiran[2]\n   theta=thetaran[0]\n   theta0=thetaran[1]\n   thetaf=thetaran[2]\n   Rho=(f*cos(phi)*sin(theta),f*sin(phi)*sin(theta),f*cos(theta))\n   return parametric_plot3d(Rho,(phi,phi0,phif),(theta,theta0,thetaf),**kwds) \n```\n\n\nSeveral examples can be found in [http://www.sagenb.org/pub/1319/](http://www.sagenb.org/pub/1319/)\n\nI've been suggested to eliminate the dependence on the 'phi' and 'theta' variables. I quite agree that that would be good, but I can't figure how to do it.\n\nAlso, I think I might generalize this into any sort of transform plot. But let's first see how this works out. Especially the variable dependency\n\nIssue created by migration from https://trac.sagemath.org/ticket/7850\n\n",
    "created_at": "2010-01-05T18:06:16Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "spherical plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7850",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: @williamstein

Keywords: spherical,plot

I've made a clone of Mathematicas SphericalPlot3d . Only that the 3d seemed redundant to me.

The code is

```
var('phi,theta')
def spherical_plot(f,phiran=(phi,0,2*pi),thetaran=(theta,0,pi),**kwds):
   phi=phiran[0]
   phi0=phiran[1]
   phif=phiran[2]
   theta=thetaran[0]
   theta0=thetaran[1]
   thetaf=thetaran[2]
   Rho=(f*cos(phi)*sin(theta),f*sin(phi)*sin(theta),f*cos(theta))
   return parametric_plot3d(Rho,(phi,phi0,phif),(theta,theta0,thetaf),**kwds) 
```


Several examples can be found in [http://www.sagenb.org/pub/1319/](http://www.sagenb.org/pub/1319/)

I've been suggested to eliminate the dependence on the 'phi' and 'theta' variables. I quite agree that that would be good, but I can't figure how to do it.

Also, I think I might generalize this into any sort of transform plot. But let's first see how this works out. Especially the variable dependency

Issue created by migration from https://trac.sagemath.org/ticket/7850





---

archive/issue_comments_067878.json:
```json
{
    "body": "Here is a rough cut of a generic function: http://sagenb.org/home/pub/1322/\n\n\n```\n# TODO: figure out a way to determine if f is an expression or callable symbolic function for the if statement.\n\ndef make_coordinate_plot3d(transformation, function_variable,parameter_variables):\n   def new_plot(f, var1_range, var2_range,**kwds):\n       f_is_expression=True\n       \n       if f_is_expression:\n           # if f is an expression, then we can use .subs.  This is faster, because parametric_plot3d\n           # can then use fast_float\n           if len(var1_range)==3:\n               vars=[var1_range[0], var2_range[0]]\n           else:\n               vars=sage.symbolic.ring.var('v1,v2')\n           plot_func=[t.subs({function_variable:f, parameter_variables[0]:vars[0], parameter_variables[1]:vars[1]})\n                       for t in transformation]\n       else:\n           # if f is not a symbolic expression or function, use the following\n           # We could make this faster by using fast_float on the components of transformation\n           # We need to do the function and map instead of just a list comprehension because\n           # of python scoping; see http://lackingrhoticity.blogspot.com/2009/04/python-variable-binding-semantics-part.html\n           def subs_func(t):\n               return lambda x,y: t.subs({function_variable:f(x,y), parameter_variables[0]:x, parameter_variables[1]:y})\n           plot_func=map(subs_func,transformation)\n\n       return parametric_plot3d(plot_func, var1_range, var2_range,**kwds)\n   return new_plot \n\n \t\nvar('r,t,p') \njason_spherical_plot3d=make_coordinate_plot3d([r*cos(t)*sin(p), r*sin(t)*sin(p), r*cos(p)], function_variable=r, parameter_variables=[t,p]) \n\n```\n",
    "created_at": "2010-01-05T22:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67878",
    "user": "https://github.com/jasongrout"
}
```

Here is a rough cut of a generic function: http://sagenb.org/home/pub/1322/


```
# TODO: figure out a way to determine if f is an expression or callable symbolic function for the if statement.

def make_coordinate_plot3d(transformation, function_variable,parameter_variables):
   def new_plot(f, var1_range, var2_range,**kwds):
       f_is_expression=True
       
       if f_is_expression:
           # if f is an expression, then we can use .subs.  This is faster, because parametric_plot3d
           # can then use fast_float
           if len(var1_range)==3:
               vars=[var1_range[0], var2_range[0]]
           else:
               vars=sage.symbolic.ring.var('v1,v2')
           plot_func=[t.subs({function_variable:f, parameter_variables[0]:vars[0], parameter_variables[1]:vars[1]})
                       for t in transformation]
       else:
           # if f is not a symbolic expression or function, use the following
           # We could make this faster by using fast_float on the components of transformation
           # We need to do the function and map instead of just a list comprehension because
           # of python scoping; see http://lackingrhoticity.blogspot.com/2009/04/python-variable-binding-semantics-part.html
           def subs_func(t):
               return lambda x,y: t.subs({function_variable:f(x,y), parameter_variables[0]:x, parameter_variables[1]:y})
           plot_func=map(subs_func,transformation)

       return parametric_plot3d(plot_func, var1_range, var2_range,**kwds)
   return new_plot 

 	
var('r,t,p') 
jason_spherical_plot3d=make_coordinate_plot3d([r*cos(t)*sin(p), r*sin(t)*sin(p), r*cos(p)], function_variable=r, parameter_variables=[t,p]) 

```




---

archive/issue_comments_067879.json:
```json
{
    "body": "Here's the relevant sage-devel thread: http://groups.google.com/group/sage-devel/browse_thread/thread/8e38cdd8048eb39c\n\nThanks again for working on this!\n\nHere are some comments about the implementation up at http://www.sagenb.org/home/pub/1323/, just based on reading the code.\n\n1. To be consistent with the plotting functions, it would also need to support something like:\n\n\n```\nspherical_plot3d(lambda x,y: x+y, (0,2*pi), (0,pi))\n```\n\n\nThat's the purpose behind the convoluted second half of the make_coordinate_plot3d function (because symbolic functions can't be multiplied by lambda functions).\n\n2. It's better to use \"zran is None\" rather than \"zran==None\".  It's a much faster test.\n\n3. There is still some dependence on variable names if the variable name is not specified.  This should give an error, or at least a deprecation warning, as it is no longer a supported syntax for plotting:\n\n\n```\nspherical_plot3d(phi*theta, (0,2*pi),(0,pi))\n```\n\n\n(note that the expression has two variables, but I haven't said which variable corresponds to which range.  This is particularly confusing with spherical plots, since there are two opposite conventions.\n\n4. except statements should catch specific exceptions (e.g., \"except ValueError\"), instead of just triggering on any error.\n\n5. I'm not sure there's any difference between the transform_plot3d and just plainly calling parametric_plot3d.  transform_plot3d seems to just basically be a rename of parametric_plot3d.",
    "created_at": "2010-01-06T07:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67879",
    "user": "https://github.com/jasongrout"
}
```

Here's the relevant sage-devel thread: http://groups.google.com/group/sage-devel/browse_thread/thread/8e38cdd8048eb39c

Thanks again for working on this!

Here are some comments about the implementation up at http://www.sagenb.org/home/pub/1323/, just based on reading the code.

1. To be consistent with the plotting functions, it would also need to support something like:


```
spherical_plot3d(lambda x,y: x+y, (0,2*pi), (0,pi))
```


That's the purpose behind the convoluted second half of the make_coordinate_plot3d function (because symbolic functions can't be multiplied by lambda functions).

2. It's better to use "zran is None" rather than "zran==None".  It's a much faster test.

3. There is still some dependence on variable names if the variable name is not specified.  This should give an error, or at least a deprecation warning, as it is no longer a supported syntax for plotting:


```
spherical_plot3d(phi*theta, (0,2*pi),(0,pi))
```


(note that the expression has two variables, but I haven't said which variable corresponds to which range.  This is particularly confusing with spherical plots, since there are two opposite conventions.

4. except statements should catch specific exceptions (e.g., "except ValueError"), instead of just triggering on any error.

5. I'm not sure there's any difference between the transform_plot3d and just plainly calling parametric_plot3d.  transform_plot3d seems to just basically be a rename of parametric_plot3d.



---

archive/issue_comments_067880.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-07T19:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67880",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067881.json:
```json
{
    "body": "Changing assignee from @williamstein to olazo.",
    "created_at": "2010-01-07T19:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67881",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing assignee from @williamstein to olazo.



---

archive/issue_comments_067882.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-07T19:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67882",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067883.json:
```json
{
    "body": "See also #7850 for a cylindrical plotting function",
    "created_at": "2010-01-07T19:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67883",
    "user": "https://github.com/jasongrout"
}
```

See also #7850 for a cylindrical plotting function



---

archive/issue_comments_067884.json:
```json
{
    "body": "a proposal for a docstring",
    "created_at": "2010-01-13T01:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67884",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

a proposal for a docstring



---

archive/issue_events_008065.json:
```json
{
    "actor": "olazo",
    "created_at": "2010-01-24T19:35:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7850#event-8065"
}
```



---

archive/issue_comments_067885.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-24T19:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67885",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Resolution: invalid



---

archive/issue_comments_067886.json:
```json
{
    "body": "Attachment [docstring](tarball://root/attachments/some-uuid/ticket7850/docstring) by olazo created at 2010-01-24 19:35:42",
    "created_at": "2010-01-24T19:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7850#issuecomment-67886",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Attachment [docstring](tarball://root/attachments/some-uuid/ticket7850/docstring) by olazo created at 2010-01-24 19:35:42
