import locale
locale.setlocale(locale.LC_NUMERIC, "pt_BR")

num=1255.56
num2=1254564

num3=locale.format_string("%.2f",num)
print(str(num).replace(".", ","))
print(num3)

