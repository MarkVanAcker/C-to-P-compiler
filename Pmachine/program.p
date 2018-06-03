ssp 2
ldc r 7.0
str r 0 1
ldc r 6.0
lod r 0 1
add r
str r 0 2
mst 0
cup 0 function_main
hlt
function_a:
ent 1 6
ldc r 0.0
str r 0 0
retf
function_main:
ent 2 6
ldc i 9
str i 0 5
beginwhile:
lod i 0 5
ldc i 10
les i
fjp endwhile
lod i 0 5
ldc i 1
add i
str i 0 5
ujp beginwhile
endwhile:
lod i 0 5
out i
ldc i 0
str i 0 0
retf
hlt
