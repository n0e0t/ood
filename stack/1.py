values = input('Enter Input : ')
count = {'(':0,')':0,'[':0,']':0}
err = 0
for i in values:
    if i in count:
        count[i] += 1
    else:
        err = 1

if count['('] == count[')'] and err == 0 and count['('] >0 and count['['] == count[']'] and count['[']>0:
    print('Parentheses : Matched ! ! !')
else:
    print('Parentheses : Unmatched ! ! !')