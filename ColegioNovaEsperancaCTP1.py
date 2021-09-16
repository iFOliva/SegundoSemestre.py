dadosAluno = {}
criarEcontarHistorias = [1,2,3,4,5,6,7,8,9]
teatroLuzCameraEAcao = []
aLinguaDeSinais = []
expresaoArtistica = []
soletrando = []
leituraDramatica = []
oCorpoFala = []
oMundoDaImaginacao = []
leituraDinamica = []
criandoERecriandoEmojis = []
todosEventos = []
segundaSerie = ["Criar e Contar Histórias", "A língua de sinais", "O mundo da imaginação", "Criando e recriando com emojis"]
terceiraSerie = ["Criar e Contar Histórias", "Teatro: Luz, Câmera e Ação", "A língua de sinais", "O corpo fala"]
quartaSerie = ["Teatro: Luz, Câmera e Ação", "A língua de sinais", "Expressão Artística", "Leitura dramática"]
quintaSerie = ["A língua de sinais", "Expressão Artística", "Soletrando", "Leitura dinâmica"]
listarRM = []
listarNome = []
listarSerie = []
j = 0
key = 0
menuOpcoes = ["1 - Cadastrar Alunos","2 - Fazer Inscrições","3 - Listar Inscrições","4 - Sair"]
print("-" *20, "Bem vindo ao","-"*20)
print(" " *15, "Colégio Nova Esperança")
print("-" *54)

while True:
    print("Menu de Opções")
    for i in menuOpcoes:
        print(i)
    opcao = int(input(">>>"))
    if opcao == 1 and key == 0:
        while True:
            print("Digite o RM do aluno")
            rmAluno = int(input(">>>"))
            if rmAluno == 0:
                key = 1
                menuOpcoes.remove("1 - Cadastrar Alunos")
                break
            while rmAluno in dadosAluno.keys():
                print("Esse aluno já foi cadastrado, digite novamente!")
                rmAluno = int(input(">>>"))
            print("Digite o nome do aluno")
            nomeAluno = input(">>>")
            print("Digite a série do aluno")
            serieAluno = int(input(">>>"))
            dadosAluno[rmAluno] = [serieAluno], [nomeAluno]
            #print(dadosAluno)
            while serieAluno < 2 or serieAluno > 5:
                print("Digite uma série válida!")
                serieAluno = int(input(">>>"))
    if opcao == 2:
        print("Por favor, digite o RM do aluno")
        buscaRM = int(input(">>>"))

        if buscaRM in dadosAluno:
            if dadosAluno.get(buscaRM).__contains__([2]):
                todosEventos = criarEcontarHistorias + aLinguaDeSinais + oMundoDaImaginacao + criandoERecriandoEmojis
                if todosEventos.count(buscaRM) >= 3:
                    print("O aluno já excedeu o limite de inscrições!")
                else:
                    print("Inscrições realizadas pelo aluno até o momento: ",todosEventos.count(buscaRM),"\n")
                    if len(criarEcontarHistorias) > 9 and segundaSerie.__contains__("Criar e Contar Histórias"):
                        segundaSerie.remove("Criar e Contar Histórias")
                    if len(aLinguaDeSinais) > 9 and segundaSerie.__contains__("A língua de sinais"):
                        segundaSerie.remove("A língua de sinais")
                    if len(oMundoDaImaginacao) > 9 and segundaSerie.__contains__("O mundo da imaginação"):
                        segundaSerie.remove("O mundo da imaginação")
                    if len(criandoERecriandoEmojis) > 9 and segundaSerie.__contains__("Criando e recriando com emojis"):
                        segundaSerie.remove("Criando e recriando com emojis")
                    while j < len(segundaSerie):
                        if segundaSerie[j] == "Criar e Contar Histórias":
                            print(j+1,"-",segundaSerie[j]," | Alunos cadastrados:",len(criarEcontarHistorias))
                        elif segundaSerie[j] == "A língua de sinais":
                            print(j+1,"-",segundaSerie[j]," | Alunos cadastrados:",len(aLinguaDeSinais))
                        elif segundaSerie[j] == "O mundo da imaginação":
                            print(j+1,"-",segundaSerie[j]," | Alunos cadastrados:", len(oMundoDaImaginacao))
                        elif segundaSerie[j] == "Criando e recriando com emojis":
                            print(j+1,"-",segundaSerie[j]," | Alunos cadastrados:",len(criandoERecriandoEmojis))
                        j = j + 1
                    j = 0
                    escolha = int(input(">>>"))

                    while escolha < 1 or escolha > len(segundaSerie):
                        print("Por favor, digite uma opção válida!")
                        escolha = int(input(">>>"))
                    if segundaSerie[escolha-1] == "Criar e Contar Histórias":
                        if criarEcontarHistorias.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            criarEcontarHistorias.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif segundaSerie[escolha-1] == "A língua de sinais":
                        if aLinguaDeSinais.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            aLinguaDeSinais.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif segundaSerie[escolha-1] == "O mundo da imaginação":
                        if oMundoDaImaginacao.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            oMundoDaImaginacao.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif segundaSerie[escolha-1] == "Criando e recriando com emojis":
                        if criandoERecriandoEmojis.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            criandoERecriandoEmojis.append(buscaRM)
                            print("Cadastrado com sucesso!")
            if dadosAluno.get(buscaRM).__contains__([3]):
                todosEventos = criarEcontarHistorias + teatroLuzCameraEAcao + aLinguaDeSinais + oCorpoFala
                if todosEventos.count(buscaRM) >= 3:
                    print("O aluno já excedeu o limite de inscrições!")
                else:
                    print("Inscrições realizadas pelo aluno até o momento: ", todosEventos.count(buscaRM), "\n")
                    if len(criarEcontarHistorias) > 9 and terceiraSerie.__contains__("Criar e Contar Histórias"):
                        terceiraSerie.remove("Criar e Contar Histórias")
                    if len(teatroLuzCameraEAcao) > 9 and terceiraSerie.__contains__("Teatro: Luz, Câmera e Ação"):
                        terceiraSerie.remove("Teatro: Luz, Câmera e Ação")
                    if len(aLinguaDeSinais) > 9 and terceiraSerie.__contains__("A língua de sinais"):
                        terceiraSerie.remove("A língua de sinais")
                    if len(oCorpoFala) > 9 and terceiraSerie.__contains__("O corpo fala"):
                        terceiraSerie.remove("O corpo fala")
                    while j < len(terceiraSerie):
                        if terceiraSerie[j] == "Criar e Contar Histórias":
                            print(j + 1, "-", terceiraSerie[j], " | Alunos cadastrados:", len(criarEcontarHistorias))
                        elif terceiraSerie[j] == "Teatro: Luz, Câmera e Ação":
                            print(j + 1, "-", terceiraSerie[j], " | Alunos cadastrados:", len(teatroLuzCameraEAcao))
                        elif terceiraSerie[j] == "A língua de sinais":
                            print(j + 1, "-", terceiraSerie[j], " | Alunos cadastrados:", len(aLinguaDeSinais))
                        elif terceiraSerie[j] == "O corpo fala":
                            print(j + 1, "-", terceiraSerie[j], " | Alunos cadastrados:", len(oCorpoFala))
                        j = j + 1
                    j = 0
                    escolha = int(input(">>>"))

                    while escolha < 1 or escolha > len(terceiraSerie):
                        print("Por favor, digite uma opção válida!")
                        escolha = int(input(">>>"))
                    if terceiraSerie[escolha - 1] == "Criar e Contar Histórias":
                        if criarEcontarHistorias.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            criarEcontarHistorias.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif terceiraSerie[escolha - 1] == "Teatro: Luz, Câmera e Ação":
                        if teatroLuzCameraEAcao.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            teatroLuzCameraEAcao.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif terceiraSerie[escolha - 1] == "A língua de sinais":
                        if aLinguaDeSinais.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            aLinguaDeSinais.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif terceiraSerie[escolha - 1] == "O corpo fala":
                        if oCorpoFala.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            oCorpoFala.append(buscaRM)
                            print("Cadastrado com sucesso!")
            if dadosAluno.get(buscaRM).__contains__([4]):
                todosEventos = teatroLuzCameraEAcao + aLinguaDeSinais + expresaoArtistica + leituraDramatica
                if todosEventos.count(buscaRM) >= 3:
                    print("O aluno já excedeu o limite de inscrições!")
                else:
                    print("Inscrições realizadas pelo aluno até o momento: ", todosEventos.count(buscaRM), "\n")
                    if len(teatroLuzCameraEAcao) > 9 and segundaSerie.__contains__("Teatro: Luz, Câmera e Ação"):
                        quartaSerie.remove("Teatro: Luz, Câmera e Ação")
                    if len(aLinguaDeSinais) > 9 and segundaSerie.__contains__("A língua de sinais"):
                        quartaSerie.remove("A língua de sinais")
                    if len(expresaoArtistica) > 9 and segundaSerie.__contains__("Expressão Artística"):
                        quartaSerie.remove("Expressão Artística")
                    if len(leituraDramatica) > 9 and segundaSerie.__contains__("Leitura dramática"):
                        quartaSerie.remove("Leitura dramática")
                    while j < len(quartaSerie):
                        if quartaSerie[j] == "Teatro: Luz, Câmera e Ação":
                            print(j + 1, "-", quartaSerie[j], " | Alunos cadastrados:", len(teatroLuzCameraEAcao))
                        elif quartaSerie[j] == "A língua de sinais":
                            print(j + 1, "-", quartaSerie[j], " | Alunos cadastrados:", len(aLinguaDeSinais))
                        elif quartaSerie[j] == "Expressão Artística":
                            print(j + 1, "-", quartaSerie[j], " | Alunos cadastrados:", len(expresaoArtistica))
                        elif quartaSerie[j] == "Leitura dramática":
                            print(j + 1, "-", quartaSerie[j], " | Alunos cadastrados:", len(leituraDramatica))
                        j = j + 1
                    j = 0
                    escolha = int(input(">>>"))

                    while escolha < 1 or escolha > len(quartaSerie):
                        print("Por favor, digite uma opção válida!")
                        escolha = int(input(">>>"))
                    if quartaSerie[escolha - 1] == "Teatro: Luz, Câmera e Ação":
                        if teatroLuzCameraEAcao.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            teatroLuzCameraEAcao.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif quartaSerie[escolha - 1] == "A língua de sinais":
                        if aLinguaDeSinais.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            aLinguaDeSinais.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif quartaSerie[escolha - 1] == "Expressão Artística":
                        if expresaoArtistica.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            expresaoArtistica.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif quartaSerie[escolha - 1] == "Leitura dramática":
                        if leituraDramatica.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            leituraDramatica.append(buscaRM)
                            print("Cadastrado com sucesso!")
            if dadosAluno.get(buscaRM).__contains__([5]):
                todosEventos = aLinguaDeSinais + expresaoArtistica + soletrando + leituraDinamica
                if todosEventos.count(buscaRM) >= 3:
                    print("O aluno já excedeu o limite de inscrições!")
                else:
                    print("Inscrições realizadas pelo aluno até o momento: ", todosEventos.count(buscaRM), "\n")
                    if len(aLinguaDeSinais) > 9 and segundaSerie.__contains__("A língua de sinais"):
                        quintaSerie.remove("A língua de sinais")
                    if len(expresaoArtistica) > 9 and segundaSerie.__contains__("Expressão Artística"):
                        quintaSerie.remove("Expressão Artística")
                    if len(soletrando) > 9 and segundaSerie.__contains__("Soletrando"):
                        quintaSerie.remove("Soletrando")
                    if len(leituraDinamica) > 9 and segundaSerie.__contains__("Leitura dinâmica"):
                        quintaSerie.remove("Leitura dinâmica")
                    while j < len(quintaSerie):
                        if quintaSerie[j] == "A língua de sinais":
                            print(j + 1, "-", quintaSerie[j], " | Alunos cadastrados:", len(aLinguaDeSinais))
                        elif quintaSerie[j] == "Expressão Artística":
                            print(j + 1, "-", quintaSerie[j], " | Alunos cadastrados:", len(expresaoArtistica))
                        elif quintaSerie[j] == "Soletrando":
                            print(j + 1, "-", quintaSerie[j], " | Alunos cadastrados:", len(soletrando))
                        elif quintaSerie[j] == "Leitura dinâmica":
                            print(j + 1, "-", quintaSerie[j], " | Alunos cadastrados:", len(leituraDinamica))
                        j = j + 1
                    j = 0
                    escolha = int(input(">>>"))

                    while escolha < 1 or escolha > len(quintaSerie):
                        print("Por favor, digite uma opção válida!")
                        escolha = int(input(">>>"))
                    if quintaSerie[escolha - 1] == "A língua de sinais":
                        if aLinguaDeSinais.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            aLinguaDeSinais.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif quintaSerie[escolha - 1] == "Expressão Artística":
                        if expresaoArtistica.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            expresaoArtistica.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif quintaSerie[escolha - 1] == "Soletrando":
                        if soletrando.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            soletrando.append(buscaRM)
                            print("Cadastrado com sucesso!")
                    elif quintaSerie[escolha - 1] == "Leitura dinâmica":
                        if leituraDinamica.__contains__(buscaRM):
                            print("Este aluno já está cadastrado neste evento!")
                        else:
                            leituraDinamica.append(buscaRM)
                            print("Cadastrado com sucesso!")
        else:
             print("Aluno não cadastrado.Favor procurar a coordenação do Fundamental I")
    if opcao == 3:
        print("Menu listar opções")
        print("1 - Listar por aluno\n2 - Listar por oficina")
        opcao3 = int(input(">>>"))
        if opcao3 == 1:
            print("***** Alunos inscritos - Ordem: Alfabética (nome) *****")
            # listarNome = dados[]
            # for rm, nome in dadosAluno.items():
            for dados in dadosAluno.items():
                print("ss")




