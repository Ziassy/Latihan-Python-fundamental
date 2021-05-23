# upper() dan lower(), rstrip(), lstrip(), strip()
# mengecek boolean dari sebuah string isupper(), islower(), isalpha(), isalnum(), isdecimal(),
convert = 'Pauziah'
upper = convert.upper()
lower = convert.lower()

print(upper)
print(lower)

print('    with white    space')
print('Delete whitespace from right side    '.rstrip()) # hapus whiteSpace dari kanan
print('    Delete whitespace from left side'.lstrip()) # hapus whiteSpace dari kiri
print('    delete both side whitespace   '.strip()) # hapus whitespace ke dua sisi

kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code')) # delete setiap kata Code

# join() menggabungkan string
print(' '.join(['Dicoding', 'Indonesia', '!']))

# split()
# memisahkan substring berdasarkan delimiter tertentu
print('Dicoding Indonesia !'.split()) #['Dicoding', 'Indonesia', '!']

multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""
print(multi_line)