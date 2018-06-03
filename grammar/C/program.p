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
ent 4 7
ldc i 0
str i 0 5
ldc c 71
out c
ldc c 101
out c
ldc c 101
out c
ldc c 102
out c
ldc c 32
out c
ldc c 104
out c
ldc c 105
out c
ldc c 101
out c
ldc c 114
out c
ldc c 32
out c
ldc c 101
out c
ldc c 101
out c
ldc c 110
out c
ldc c 32
out c
ldc c 103
out c
ldc c 101
out c
ldc c 116
out c
ldc c 97
out c
ldc c 108
out c
ldc c 32
out c
ldc c 105
out c
ldc c 110
out c
ldc c 32
out c
ldc c 119
out c
ldc c 97
out c
ldc c 97
out c
ldc c 114
out c
ldc c 118
out c
ldc c 97
out c
ldc c 110
out c
ldc c 32
out c
ldc c 117
out c
ldc c 32
out c
ldc c 100
out c
ldc c 101
out c
ldc c 32
out c
ldc c 102
out c
ldc c 97
out c
ldc c 99
out c
ldc c 117
out c
ldc c 108
out c
ldc c 116
out c
ldc c 101
out c
ldc c 105
out c
ldc c 116
out c
ldc c 32
out c
ldc c 119
out c
ldc c 105
out c
ldc c 108
out c
ldc c 116
out c
ldc c 32
out c
ldc c 98
out c
ldc c 101
out c
ldc c 114
out c
ldc c 101
out c
ldc c 107
out c
ldc c 101
out c
ldc c 110
out c
ldc c 101
out c
ldc c 110
out c
ldc c 58
out c
ldc c 32
out c
lda 0 5
in i
sto i
mst 1
lod i 0 5
cup 1 function_faculty
str i 0 6
lod i 0 5
out i
ldc c 32
out c
ldc c 102
out c
ldc c 97
out c
ldc c 99
out c
ldc c 117
out c
ldc c 108
out c
ldc c 116
out c
ldc c 101
out c
ldc c 105
out c
ldc c 116
out c
ldc c 32
out c
ldc c 105
out c
ldc c 115
out c
ldc c 32
out c
lod i 0 6
out i
hlt
