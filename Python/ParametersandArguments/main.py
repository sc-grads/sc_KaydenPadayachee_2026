def greet(name: str):
    print(f"Hello {name}!")

greet('Mario')
greet('James')
greet('Sophia')

#new

def greet(name: str, language: str, default: str= 'Hello'):
    if language == 'it':
        print(f'Ciao, {name}!')
    else:
        print(f'{default}, {name}!')

greet(name='Mario',language= 'it')
#or you can do like this, greet('Mario','it','Hello')
greet(name='Mario',language= 'it',default= 'Hola')


#return functions

def get_length(text: str) -> int:
    print(f'Getting the length of "{text}"...')
    return len(text)

name: str = 'Mario'
length: int = get_length(name)
print(length)

#new

def make_upper(text: str) -> str:
    return text.upper()
print(make_upper('hello'))


