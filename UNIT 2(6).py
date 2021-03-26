import re
text = "PYTHON Exercises"
print("Original Text: ",text)
redata = re.compile(re.escape('python'), re.IGNORECASE)
new_text = redata.sub('python', 'PYTHON Exercises')
print("Using 'python' replace PYTHON") 
print("New Text: ",new_text)
