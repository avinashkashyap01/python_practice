
from datetime import datetime

# While Loop

a = datetime.now().second
print(a)


wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    print('still waiting')
print(f'we are at {wait_until} second!')


wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    1 + 1
print(f'we are at {wait_until} second!')


# Pass
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    pass
print(f'we are at {wait_until} second!')


# Break
wait_until = datetime.now().second + 2
while True:
    if datetime.now().second == wait_until:
        print(f'we are at {wait_until} second!')
        break


# Continue

wait_until = datetime.now().second + 2
while True:
    if datetime.now().second < wait_until:
        continue
    break
print(f'we are at {wait_until} second!')
