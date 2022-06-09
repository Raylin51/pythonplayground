import random
from unittest import result

avada_probability = range(1, 1 + 436)
crucio_probability = range(437, 437 + 436)
dumbledore_probability = range(437 + 436, 437 + 436 + 367)
weasley_probability = range(437 + 436 + 367, 437 + 436 + 367 + 239)
blasting_probability = range(437 + 436 + 367 + 239, 437 + 436 + 367 + 239 + 239)
prior_probability = range(437 + 436 + 367 + 239 + 239, 437 + 436 + 367 + 239 + 239 + 239)
inflating_probability = range(437 + 436 + 367 + 239 + 239 + 239, 437 + 436 + 367 + 239 + 239 + 239 + 1405)

print(avada_probability)
print(crucio_probability)
print(dumbledore_probability)
print(weasley_probability)
print(blasting_probability)
print(prior_probability)
print(inflating_probability)

round = 1
total = 0

for n in range(0, round):
  cards = []
  for i in range(0, 10):
    if len(cards) >= 5:
      total += 1
      print('成功了', total, '次')
      break
    print('开始用第', i + 1, '张券')
    for j in range(0, 5):
      # result = random.randint(1, 100000)
      result = 3000
      print(result)
      if result in avada_probability:
        print('抽到阿瓦达索命')
        if 'avada' in cards: 
          continue
        else:
          cards.append('avada')
      elif result in crucio_probability:
        print('抽到钻心剜骨')
        if 'crucio' in cards: 
          continue
        else:
          cards.append('crucio')
      elif result in dumbledore_probability:
        print('抽到邓布利多')
        if 'dumbledore' in cards: 
          continue
        else:
          cards.append('dumbledore')
      elif result in weasley_probability:
        print('抽到韦斯莱烟花')
        if 'weasley' in cards: 
          continue
        else:
          cards.append('weasley')
      elif result in blasting_probability:
        print('抽到霹雳爆炸')
        if 'blasting' in cards: 
          continue
        else:
          cards.append('blasting')
      elif result in prior_probability:
        print('抽到闪回咒')
        if 'prior' in cards: 
          continue
        else:
          cards.append('prior')
      elif result in inflating_probability:
        print('抽到充气咒')
        if 'inflating' in cards: 
          continue
        else:
          cards.append('inflating')
      else:
        print('啥也没抽到')
    
print(total)
print('本次实验概率是', total / round * 100, '%')
