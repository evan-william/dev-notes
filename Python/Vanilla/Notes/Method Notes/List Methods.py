# Python List Methods Notes and Examples

# Daftar awal
menu = ['🍔', '🍟', '🍔', '🍟', '🍔']

# append
menu1 = menu.copy()
menu1.append('🍔')
print("append('🍔') ->", menu1)

# clear
menu2 = menu.copy()
menu2.clear()
print("clear() ->", menu2)

# count
print("count('🍔') ->", menu.count('🍔'))

# copy
menu3 = menu.copy()
print("copy() ->", menu3)

# index
print("index('🍟') ->", menu.index('🍟'))

# insert
menu4 = menu.copy()
menu4.insert(1, '🥤')
print("insert(1, '🥤') ->", menu4)

# pop
menu5 = menu.copy()
menu5.pop(3)
print("pop(3) ->", menu5)

# remove
menu6 = menu.copy()
menu6.remove('🍟')
print("remove('🍟') ->", menu6)

# reverse
menu7 = menu.copy()
menu7.reverse()
print("reverse() ->", menu7)
