import separateOptimStruct
import numpy as np
def fmincon(fun,X=[], **kwargs):
    algorithm='interior-point'
    display=False
    nargin=len(kwargs)
    # algorithm = kwargs.get('algorithm', algorithm)
    # display = kwargs.get('display', display)
    A=kwargs.get('A', None)
    B=kwargs.get('B', None)
    Aeq=kwargs.get('Aeq', None)
    Beq=kwargs.get('Beq', None)
    LB=kwargs.get('LB', None)
    UB=kwargs.get('UB', None)
    NONLCON=kwargs.get('NONLCON', None)
    options=kwargs.get('options', None)
    varargin=kwargs.get('varargin', None)

    if nargin == 0 and X==[]:
        if isinstance(FUN,'dict'):
            [FUN,X,A,B,Aeq,Beq,LB,UB,NONLCON,options] = separateOptimStruct(FUN)
        else:
            print('Python:fmincon:NotEnoughInputs','Not enough input arguments.')
            return
    if len(options) ==0 :
        options = defaultopt
        optimgetflag = 'optimoptions'
    elif isinstance(options,'dict'):
        optimgetflag = 'fast'
    else:
        print('Python:fmincon:InvalidOptArg','Invalid OPT argument for FMINCON.')
    
        
    activeSet = 'active-set'
    sqp = 'sqp'
    trustRegionReflective = 'trust-region-reflective'
    interiorPoint = 'interior-point'
    sqpLegacy = 'sqp-legacy'

    xShape=X.shape
    XOUT=np.array(X)
    XOUT=XOUT.reshape(XOUT.shape[0]*XOUT.shape[1],1)

    nVar=XOUT.shape[0]*XOUT.shape[1]