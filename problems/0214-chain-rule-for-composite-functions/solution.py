import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    decompose = [None] * len(functions)   # decompose[k] = input of functions[k]
    val = x
    for k in range(len(functions)-1, -1, -1):
        decompose[k] = val                # was: append
        if functions[k] == 'square':
            val = val * val
        elif functions[k] == 'sin':
            val = np.sin(val)
        elif functions[k] == 'exp':
            val = np.exp(val)
        elif functions[k] == 'log':
            val = np.log(val)

    ans = 1.0                             # was: ans = x
    for i in range(len(functions)-1, -1, -1):
        if functions[i] == 'square':
            ans *= 2 * decompose[i]       # was: ans = ...
        elif functions[i] == 'sin':
            ans *= np.cos(decompose[i])
        elif functions[i] == 'exp':
            ans *= np.exp(decompose[i])
        elif functions[i] == 'log':
            ans *= 1 / decompose[i]

    return ans