def fc_principal():
    print("! Executando a Função Principal!")

    def fc_interna_abc():
        print("! Executando a Função Interna ABC!")
    
    def fc_interna_xyz():
        print("! Executando a Função Interna XYZ!")
    
    fc_interna_xyz()
    fc_interna_abc()

fc_principal()