"""
stack-empty(S)
    if S.top == 0
        return True
    else
        return False

push(S, x)
    S.top = S.top + 1
    S[S.top] = x

pop(S)
    if stack-empty(S)
        error 'underflow'
    else
        S.top = S.top - 1
        return S[S.top + 1]
"""