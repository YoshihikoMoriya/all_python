import re

line = "the gohst that says boo haunts the loo"

m = re.findall(".oo", line)
print(m)
