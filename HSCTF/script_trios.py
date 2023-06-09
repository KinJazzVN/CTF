chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

res = [] 
data = ''
with open('data.txt', 'r') as f:
    data = f.read()
    handle = data.replace('{',' ').replace('}','').replace('.', '').replace(',', '').split(' ')
    # print(data)

    for i in range(len(handle)):
        tmp = len(handle[i])
        c = 0 
        if tmp % 3 != 0:
            c = 1 
            while c < len(handle[i]):
                res.append(handle[i][c : c + 3]) 
                c += 3 
        else:
            while c < len(handle[i]):
                res.append(handle[i][c : c + 3]) 
                c += 3
    # print(res)

keyboard_chars = [chr(i) for i in range(97, 123)]
# print(keyboard_chars)

# dic = {'f': '8wn', 'l': 'APR', 'a': '2sv', 'g': 'yje'}
# print(list(set(res)))

dic = {char: term for char, term in zip(keyboard_chars, list(set(res)))}
# print(dic)

data_dec = data
for i in dic.keys():
    data_dec = data_dec.replace(dic[i], i)

print(data_dec)   

# -> use Mono-alphabetic Substitution in dcode and get flag :D 