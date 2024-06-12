import sys

geek_var = "Geek"
print(sys.getrefcount(geek_var))

string_gfg = geek_var
print(sys.getrefcount(string_gfg))
