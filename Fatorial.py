class Fatorial:
    
    @staticmethod
    def fatorial(x):
        if x == 2:
            return x
        else:
            return x * Fatorial.fatorial(x-1)
