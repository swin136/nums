"""
Работа со словарем

"""

a_dict = {"one":1, "two":2, "three":3}
 
for key in a_dict:
    print(key)



morse_symbols = ["0", "1", "2", "3", "4", "5"]
morse_code_transl = ["-----", ".----", "..---", "...--", "....-", "....."]


morse_code = dict(zip(morse_symbols, morse_code_transl))


print(morse_code.get("4"))
print(morse_code.get("2"))
print(morse_code.get("1"))


