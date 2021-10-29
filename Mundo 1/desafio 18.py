import math
ângulo = float(input('Qual o seu ângulo ?'))
sen = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tag = math.tan(math.radians(ângulo))
print(f'O seno é:{sen:.1f}\no cosseno:{cos:.1f}\na tangente:{tag:.1f}')