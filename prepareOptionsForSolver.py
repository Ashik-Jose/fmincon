def prepareOptionsForSolver(options,solverName):
    if isinstance(options,'dict'):
        if options.get('TolFun') and options.get('TolFunValue')==None:
            options['TolFunValue']=options['TolFun']
