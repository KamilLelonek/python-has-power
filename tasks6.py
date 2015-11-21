# TASK 6.1
def all_attributes(obj): return dir(obj)
    
print(all_attributes(1))
print(all_attributes(""))

# TASK 6.2
def all_iterable_attributes(obj):
    return [attr for attr in all_attributes(obj) if callable(attr)]
    
print(all_attributes(1))
print(all_attributes(""))

# TASK 6.3
def attributes_docstring(obj):
    return [getattr(obj, attr) for attr in all_attributes(obj)]

print(all_attributes(1))
print(all_attributes(""))
