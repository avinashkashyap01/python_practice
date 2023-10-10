
# Variables as Functions

x = 5
def x():
    return 5

# Viewinf Function data with _code_

print(x.__code__.co_varnames)
print(x.__code__.co_code)


# Text processing in python
text = '''
Beautiful is batter then ugly.
Explicit is batter then implicit.
Simple is batter then complex.
Complex is batter then complicated
Flat is batter then nested.
Sparse is batter then dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicity silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferable only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is batter then never.
Although never is often batter then *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

def lowercase(text):
    return text.lower()

def removepunctuation(text):
    punctuation =['.','-',',','*']
    for punctuation in punctuation:
        text = text.replace(punctuation, '')
    return text

def removenewlines(text):
    text = text.replace('\n',' ')
    return text

def removeshortwords(text):
    return ' '.join([word for word in text.split() if len(word) > 3])

def removelongwords(text):
    return ' '.join([word for word in text.split() if len(word) < 6])


processingfunction = [lowercase,removepunctuation,removenewlines]

for func in processingfunction:
    text = func(text)

print(text)



# Lambda Functions

a = 2 + 3
print(a)

b = (lambda x : x + 3)(5)
print(b)

mylist = [5,4,3,2,1]
print(sorted(mylist))

mylist = [{'num':3},{'num':2},{'num':1}]
print(sorted(mylist, key=lambda x: x['num']))
