# Class 008 - String Formatting and Interpolation 
# (f-string) and (.format) string formatting
name = 'Albert Einstein'
height = 1.75
weight = 73
imc = weight / (height ** 2)
print(name, 'tem', height, 'm de altura, ', weight, 'kg e seu IMC é', imc)
# fomatação de strings f-strings
print(f'{name} tem {height}m de altura, {weight}kg e seu IMC é {imc:.2f}')
# formatação de strings .format
print('{} tem {}m de altura, {}kg e seu IMC é {:.2f}'.format(name, height, weight, imc))