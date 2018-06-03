ssp 1
mst 0
cup 0 function_main
hlt
function_faculty:
ent 3 6
lod i 0 5
ldc i 2
equ i
fjp falseif
ldc i 2
str i 0 0
retf
falseif:
lod i 0 5
mst 1
lod i 0 5
ldc i 1
sub i
cup 1 function_faculty
mul i
str i 0 0
retf
hlt
function_main:
ent 1 6
mst 1
ldc i 10
cup 1 function_faculty
str i 0 5
lod i 0 5
out i
hlt



