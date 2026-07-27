#25341a05l1 vinay
import keyword

# printing soft keywords
print("Soft Keywords:")
for word in keyword.softkwlist:
    print(word)

print()

# printing hard keywords
print("Hard Keywords:")
for word in keyword.kwlist:
    if word not in keyword.softkwlist:
        print(word)

        ''' output
        Soft Keywords:
_
case
match
type

Hard Keywords:
False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
'''