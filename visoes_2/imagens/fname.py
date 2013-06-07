def get_fname(self):
    """
    Devolve o nome do ficheiro sem sufixo.
    """
    if self.imFileName == None:
        return 'Imagem'
    else:
        start_full_name = self.imFileName.rfind('/')
        start_ftype = self.imFileName.rfind('.')
        return self.imFileName[start_full_name+1:start_ftype]
    
    
