ssp 2
ldc r 7.0
str r 0 0
ldc r 6.0
lod r 0 0
add r
str r 0 1
mst 0
cup 0 function_main
hlt
function_main:
ent 3 7
ldc i 9
str i 0 5
lod i 0 5
lod i 0 5
ldc i 7
mul i
add i
str i 0 6
ldc r 8.9
str r 1 1
lod r 1 1
out r
ldc i 0
retf
hlt
