def separate_optim_struct(FUN):
    FUN=FUN['FUN']
    X=FUN['X']
    if 'A' in FUN:
        A=FUN['A']  
    else:
        A=[]
    if 'B' in FUN:
        B=FUN['B']
    else:
        B=[]
    if 'Aeq' in FUN:
        Aeq=FUN['Aeq']
    else:
        Aeq=[]
    if 'Beq' in FUN:
        Beq=FUN['Beq']
    else:
        Beq=[]
    if 'LB' in FUN:
        LB=FUN['LB']
    else:
        LB=[]
    if 'UB' in FUN:
        UB=FUN['UB']
    else:
        UB=[]
    if 'NONLCON' in FUN:
        NONLCON=FUN['NONLCON']
    else:
        NONLCON=[]
    if 'options' in FUN:
        options=FUN['options']
    else:
        options=[]
    return FUN, X, A, B, Aeq, Beq, LB, UB, NONLCON, options