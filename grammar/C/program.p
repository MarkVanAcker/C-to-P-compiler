ssp 1
mst 0
cup 0 function_main
hlt
function_func:
ent 2 6
ldc i 4
str i 0 5
lod i 0 5
ldc i 3
equ i
fjp falseif
ldc i 0
retf
ujp endif
falseif:
ldc i 10
retf
endif:
hlt
function_main:
ent 1 6
mst 1
cup 1 function_func
str i 0 5
ldc i 1
retf
hlt
