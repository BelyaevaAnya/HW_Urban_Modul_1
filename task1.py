example = 'Бесконечность не предел!'
print(example[0])                     # =>Б
print(example[-1])                    # =>!
print(example[len(example)//2:])      # => ь не предел!
print(''.join(reversed(example)))     # => !ледерп ен ьтсонченоксеБ
print(example[1::2])                  # => екнчот епее!