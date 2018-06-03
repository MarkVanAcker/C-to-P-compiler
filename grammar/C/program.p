ssp 1
mst 0
cup 0 function_main
hlt
function_main:
ent 2 16
ldc a 0
str a 0 5
lda 0 5
str a 0 13
lod a 0 13
ldc i 8
ixa 1
ind i
sro i 0
ldc i 0
str i 0 14
ldc i 0
str i 0 14
beginwhile:
lod i 0 14
ldc i 10
les i
fjp endwhile
lda 0 5
ldc i 3
ixa 1
ind i
str i 0 15
lod i 0 14
ldc i 1
add i
str i 0 14
ujp beginwhile
endwhile:
ldc i 0
str i 0 14
beginwhile1:
lod i 0 14
ldc i 10
les i
fjp endwhile1
lda 0 5
ldc i 3
ixa 1
ind i
str a 0 15
lod i 0 14
ldc i 1
add i
str i 0 14
ujp beginwhile1
endwhile1:
hlt
