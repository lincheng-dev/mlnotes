
# coding: utf-8

# # Note of "Python for Data Analysis"

# 1 $\textbf{Global Interpreter Lock}$: A mechanism that prevents the interpreter from executing more than one Python instruction at a time. Bottleneck for Python concurrency performance. Can call C function to realize concurrency.

# 2 Books for Python: Python Cookbook; Fluent Python; Effective Python

# 3 Run a Python file: %run in IPython/Jupyter; %run -i allow existing variable visible; %load will import the file

# 4 ? show information of obj or function; ?? show function source code as well. Another usage is np.*load*? for wildcard search

# 5 Some useful magic functions: %quickref, %magic, %reset

# 6 Type related commands

# In[10]:


a = 5
print(type(a))
print(isinstance(a, (int, float)))


# 7 Reflection: access object/attributes by name. $\textbf{getattr/hasattr/setattr}$

# 8 $\textbf{is}$ and $\textbf{is not}$ are useful for checking reference equality. We can also write a is None to check equivalence to None since there is only one instance of None.

# 9 String is immutable object. In Python3, it is Unicode by default instead of byte, can encode to others and decode back to Unicode.

# 10 Datetime handling: datetime/timedelta/strftime/strptime

# In[39]:


get_ipython().run_cell_magic('timeit', '', 'numsum = 0\nfor i in range(1000):\n    if i % 3==0 or i%5==0:\n        numsum+=i')


# In[40]:


get_ipython().run_cell_magic('timeit', '', 'newsum = sum([i for i in range(1000) if (i%3==0 or i%5==0)])')


# 11 Tuple unpacking

# In[41]:


thetup = 1,2,3,4,5
a,b,*theothers = thetup
print(a)
print(b)
print(theothers)

