# Mengonversi string ke dalam array.array

import array

B = array.array('u')
B.fromstring("Python")

for karakter in B:
    print("%c"%karakter,end=' ')