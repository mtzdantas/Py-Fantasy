from re import match
from datetime import datetime
import pickle
import os
cadastro = {}
cadastroloja = ['loja', 'loja123']
fantasias = {
    '1': [4, 'PIRATA'],
    '2': [4, 'PRINCESA'],
    '3': [4, 'BRUXA'],
    '4': [4, 'POLICIAL']
}
finishc = {}
finishn = []
carrinho = []


def verificar_login():
    a = 0
    while a == 0:
        nl = str(input('DIGITE O SEU LOGIN DE ACESSO:\n'))
        if nl not in cadastro and nl != cadastroloja[0] and nl.count(' ') == 0:
            return nl
        elif nl.count(' ') > 0:
            print('POR FAVOR, NÃO DIGITE ESPAÇOS NO SEU LOGIN.')
        else:
            print('LOGIN JÁ EXISTENTE, POR FAVOR TENTE NOVAMENTE!')


def verificar_senha():
    a = 0
    while a == 0:
        np = str(input('DIGITE A SUA SENHA DE ACESSO:\n'))
        if len(np) >= 8 and np.count(' ') == 0:
            return np
        elif np.count(' ') > 0:
            print('POR FAVOR, NÃO DIGITE ESPAÇOS NA SUA SENHA.')
        else:
            print('POR FAVOR, FAÇA UMA SENHA MAIOR.')


def verificar_nome():
    a = 0
    while a == 0:
        nname = str(input('DIGITE O SEU NOME COMPLETO:\n')).title().strip()
        if match('^[a-zA-ZÁáÍíÓóÚúÉéÃãÕõÊêÂâÔôç\s]+$', nname) and not nname.isspace() and len(nname.split()) > 1:
            return nname
        else:
            if len(nname.split()) <= 1:
                print('POR FAVOR, DIGITE SEU NOME COMPLETO.')
            else:
                print('POR FAVOR, DIGITE SEU NOME CORRETAMENTE.')


def verificar_telefone():
    a = 0
    while a == 0:
        nn = str(input('DIGITE O SEU TELEFONE PARA CONTATO:\n'))
        if match(r'^[0-9]+$', nn) and len(nn) == 11 and nn[2] == '9':
            return nn
        else:
            if not match(r'^[0-9]+$', nn):
                print('POR FAVOR, DIGITE SOMENTE NÚMEROS.')
            elif len(list(nn)) < 11:
                print('POR FAVOR, DIGITE O NÚMERO COMPLETO, INCLUINDO O DDD E O NOVE INICIAL.')
            else:
                print('POR FAVOR, DIGITE O NÚMERO CORRETAMENTE.')


def verificar_email():
    a = 0
    while a == 0:
        ne = str(input('DIGITE O SEU EMAIL PARA CONTATO:\n'))
        if ne.count(' ') == 0 and ne.count('@') == 1 and ne.count('.') >= 1 and ne.rfind('.') > ne.find('@') \
                and ne[ne.rfind('.') + 1:].isalpha() and not ne.startswith('@') and len(ne) - ne.rfind('.') >= 3:
            return ne
        else:
            print('POR FAVOR, DIGITE SEU EMAIL CORRETAMENTE.')


def intro_menucliente():
    a = 0
    while a == 0:
        limpar()
        print('===============================\n           PyFantasy\n SUA FANTASIA É NOSSA ALEGRIA!\n==============================='
              '\n        SEJA BEM VINDO!\n{}'.format(cadastro[login][0].split()[0].center(30).upper()))
        action = input('   COM O QUE PODEMOS AJUDAR?\n[1] LISTAR PRODUTOS\n[2] ALUGAR PRODUTOS\n[3] MEU CARRINHO\n[4] CANCELAR ALUGUÉIS\n'
                       '[5] MEUS ALUGUÉIS\n[6] MEU PERFIL\n[7] SOBRE NÓS\n[8] FINALIZAR COMPRA\n[9] LOGOUT\n')
        if action == '1':
            actioncliente_listar()
        elif action == '2':
            actioncliente_alugar()
        elif action == '3':
            actioncliente_alugueis()
        elif action == '4':
            actioncliente_cancelar()
        elif action == '5':
            actioncliente_alugueisabertos()
        elif action == '6':
            actioncliente_perfil()
        elif action == '7':
            actioncliente_sobre()
        elif action == '8':
            a = actioncliente_finalizar()
            if a == 1:
                return []
        elif action == '9':
            actioncliente_sair()
            print('VOLTE SEMPRE, OBRIGADO!')
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
            return []
        else:
            print('DIGITE UMA AÇÃO VÁLIDA.')


def actioncliente_listar():
    limpar()
    print('==============================\n       NOSSOS PRODUTOS\n==============================')
    b = 0
    for f in fantasias:
        b += 1
        print('[ITEM {}] FANTASIA DE {} ({} DISPONÍVEIS)'.format(b, fantasias[f][1], fantasias[f][0]))
    input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def actioncliente_alugar():
    limpar()
    print('==============================\n       ALUGAR PRODUTOS\n==============================')
    m = 0
    while m == 0:
        alugar = input('DIGITE O CÓDIGO DA FANTASIA QUE DESEJA ALUGAR:\nOBS: PARA CONSULTAR A LISTA DE CÓDIGOS, DIGITE ENTER.').upper()
        if alugar == '':
            print('========================\n        CÓDIGOS\n========================')
            for f in fantasias:
                print('[COD {}] FANTASIA DE {}'.format(f, fantasias[f][1]))
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.\n==============================')
        elif alugar in fantasias and fantasias[alugar][0] > 0:
            fantasias[alugar][0] = fantasias[alugar][0] - 1
            carrinho.append(fantasias[alugar][1])
            input('PRODUTO COLOCADO NO CARRINHO!\n==============================\nPRESSIONE ENTER PARA CONTINUAR.')
            m = 1
        else:
            input('PRODUTO ESGOTADO OU INEXISTENTE!\n==============================\nPRESSIONE ENTER PARA CONTINUAR')
            m = 1


def actioncliente_alugueis():
    limpar()
    print('==============================\n        MEU CARRINHO\n==============================')
    if carrinho == '':
        print('NÃO POSSUI NENHUM PRODUTO NO SEU CARRINHO')
    else:
        for y in range(len(carrinho)):
            print('[ITEM {}] 01 FANTASIA DE {}. PREÇO: R$ 60,00'.format(y + 1, carrinho[y]))
        print('SOMA TOTAL DOS PRODUTOS: R$ {},00'.format(len(carrinho) * 60))
    input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def actioncliente_cancelar():
    limpar()
    print('==============================\n       CANCELAR ALUGUÉIS\n==============================')
    m = 0
    while m == 0:
        cancel = input('DIGITE O CÓDIGO DA FANTASIA QUE DESEJA CANCELAR:\nOBS: PARA CONSULTAR A LISTA DE CÓDIGOS, DIGITE ENTER').upper()
        if cancel == '':
            print('========================\n        CÓDIGOS\n========================')
            for f in fantasias:
                print('[COD {}] FANTASIA DE {}'.format(f, fantasias[f][1]))
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.\n==============================')
        elif fantasias[cancel][1] in carrinho:
            for w in range(len(carrinho)):
                if fantasias[cancel][1] == carrinho[w]:
                    del carrinho[w]
                    fantasias[cancel][0] = fantasias[cancel][0] + 1
                    m = 1
                    input('PRODUTO CANCELADO!\n==============================\nPRESSIONE ENTER PARA CONTINUAR')
                    break
        else:
            m = 1
            input('PRODUTO INEXISTENTE OU NÃO SE ENCONTRA NO SEU CARRINHO!\n==============================\nPRESSIONE ENTER PARA CONTINUAR')


def actioncliente_alugueisabertos():
    limpar()
    print('==============================\n        MEUS ALUGUÉIS\n==============================')
    if login in finishn:
        print('[ALUGADO DIA: {}]'.format(finishc[login][0]))
        for q in range(len(finishc[login])):
            if q > 0:
                print('[ITEM {}] FANTASIA DE {}'.format(q, finishc[login][q]))
        print('==============================')
        input('PRESSIONE ENTER PARA CONTINUAR')
    else:
        print('VOCÊ NÃO TEM NENHUM ALUGUEL EM ABERTO.')
        input('==============================\nPRESSIONE ENTER PARA CONTINUAR')


def actioncliente_perfil():
    limpar()
    print('==============================\n          MEU PERFIL\n==============================')
    print('NOME: {}\nLOGIN: {}\nSENHA: {}\nNÚMERO: {}\nE-MAIL: {}'
          .format(cadastro[login][0].title(), cadastro[login][2], cadastro[login][3], cadastro[login][1],
                  cadastro[login][4]))
    input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def actioncliente_sobre():
    limpar()
    print('==============================\n           SOBRE NÓS\n===============================')
    print("""PyFantasy é uma empresa de aluguel
de fantasias on-line, fundada em 2010,
com o intuito de levar o mundo mágico
da imaginação para realidade dos nossos
clientes. Na PyFantasy você encontra o
que precisa para sua festa ficar completa
e ainda mais alegre!\n
Projeto desenvolvido por Mateus Dantas
com objetivo de melhorar a gestão de
clientes, fantasias e funcionários da
empresa PyFantasy.""")
    input('==============================\nPRESSIONE ENTER PARA CONTINUAR')


def actioncliente_finalizar():
    limpar()
    print('==============================\n      FINALIZANDO COMPRA\n==============================')
    if carrinho != '' and login not in finishc:
        print('O VALOR DA COMPRA É DE R${}.'.format(len(carrinho) * 60))
        resp = input('DESEJA FINALIZAR A COMPRA? (SIM/NÃO)\n').upper()
        if resp == 'SIM':
            salvar()
            print('AGRADECEMOS A PREFERÊNCIA! O PROCESSO DE PAGAMENTO DAS COMPRAS É FEITO NO ATO'
                  ' DE BUSCA OU ENTREGA DO SEU PEDIDO.\nCOMPRA FINALIZADA!')
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
            aludata = ''
            finishn.append(cadastro[login][2])
            if dataalug() != aludata:
                aludata = dataalug()
            finishc[login] = [aludata] + carrinho
            if dataalug() in aludata:
                a = 1
                return a
        else:
            a = 0
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
            return a
    elif login in finishc:
        print('É PRECISO FAZER A DEVOLUÇÃO DO SEU ALUGUEL EM ABERTO, PARA REALIZAR UM NOVO.')
        input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
        a = 0
        return a
    else:
        print('NÃO POSSUI NENHUM PRODUTO NO SEU CARRINHO.')


def actioncliente_sair():
    limpar()
    for p in fantasias:
        for m in range(len(carrinho)):
            if carrinho[m] in fantasias[p]:
                fantasias[p][0] += 1


def intro_menuloja():
    a = 0
    while a == 0:
        limpar()
        print('===============================\n           PyFantasy\n SUA FANTASIA É NOSSA ALEGRIA!\n===============================\n'
              '        SEJA BEM VINDO!\n{}'.format(nameloja.center(30).upper()))
        action = input('   COM O QUE PODEMOS AJUDAR?\n[1] LISTAR PRODUTOS\n[2] ADICIONAR PRODUTOS\n[3] RETIRAR PRODUTOS\n[4] CONSULTAR ALUGUÉIS\n'
                       '[5] CONSULTAR CLIENTES\n[6] DEVOLUÇÃO\n[7] LOGOUT\n')
        if action == '1':
            actionloja_listar()
        elif action == '2':
            actionloja_adicionar()
        elif action == '3':
            actionloja_retirar()
        elif action == '4':
            actionloja_consalugueis()
        elif action == '5':
            actionloja_consclientes()
        elif action == '6':
            actionloja_devolucao()
        elif action == '7':
            print('ATÉ LOGO.')
            a = 1
        else:
            print('DIGITE UMA AÇÃO VÁLIDA.')


def actionloja_listar():
    limpar()
    print('==============================\n        NOSSOS PRODUTOS\n==============================')
    b = 0
    for f in fantasias:
        b += 1
        print('[ITEM {}] - CODIGO {}\nFANTASIA DE {} ({} DISPONÍVEIS)'.format(b, f, fantasias[f][1], fantasias[f][0]))
    input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def actionloja_adicionar():
    limpar()
    print('==============================\n      ADICIONAR PRODUTOS\n==============================')
    namep = input('INFORME O NOME DA FANTASIA QUE VOCÊ DESEJA ADICIONAR? ').upper()
    quant = int(input('INFORME A QUANTIDADE QUE DESEJA ADICIONAR: '))
    cod = input('INFORME O CÓDIGO DO PRODUTO VOCÊ DESEJA ADICIONAR? ')
    r = 0
    if cod not in fantasias:
        for x in fantasias:
            if namep == fantasias[x][1]:
                r = 1
                break
        if r == 0:
            fantasias[cod] = [quant, namep]
            salvar()
            print('PRODUTO ADICIONADO COM SUCESSO!')
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
        else:
            print('NOME DE FANTASIA JÁ EXISTENTE!')
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
    else:
        print('CÓDIGO JÁ EXISTENTE!')
        input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def actionloja_retirar():
    limpar()
    print('==============================\n       RETIRAR PRODUTOS\n==============================')
    m = 0
    while m == 0:
        cod = input('INFORME O CÓDIGO DO PRODUTO QUE VOCÊ DESEJA RETIRAR:\nOBS: PARA CONSULTAR A LISTA DE CÓDIGOS, DIGITE ENTER').upper()
        if cod == '':
            print('========================\n        CÓDIGOS\n========================')
            for f in fantasias:
                print('[COD {}] FANTASIA DE {}'.format(f, fantasias[f][1]))
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.\n==============================')
        elif cod in fantasias:
            del fantasias[cod]
            m = 1
            salvar()
            print('PRODUTO RETIRADO COM SUCESSO!')
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
        else:
            m = 1
            print('ESSE ITEM NÃO ESTÁ CADASTRADO!')
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def actionloja_consalugueis():
    limpar()
    print('==============================\n      CONSULTAR ALUGUÉIS\n==============================')
    if len(finishn) != 0:
        for r in finishn:
            print('[CLIENTE {}]\n[ALUGADO DIA: {}]'.format(cadastro[r][0].upper(), finishc[r][0]))
            for q in range(len(finishc[r])):
                if q > 0:
                    print('[ITEM {}] FANTASIA DE {}'.format(q, finishc[r][q]))
            print('==============================')
        input('PRESSIONE ENTER PARA CONTINUAR')

    else:
        print('NÃO POSSUI NENHUM ALUGUEL.')
        input('==============================\nPRESSIONE ENTER PARA CONTINUAR')


def actionloja_consclientes():
    limpar()
    print('==============================\n      CONSULTAR CLIENTES\n==============================')
    s = 1
    if len(cadastro) == 0:
        print('NÃO EXISTE CLIENTES CADASTRADOS.')
    for n in cadastro:
        print('[CLIENTE {}]\nNOME: {}\nLOGIN: {}\nSENHA: {}\nNÚMERO: {}\nEMAIL: {}'
              .format(s, cadastro[n][0], cadastro[n][2], cadastro[n][3],
                      cadastro[n][1], cadastro[n][4]))
        print('==============================')
        s += 1
    input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def actionloja_devolucao():
    limpar()
    print('==============================\n          DEVOLUÇÃO\n==============================')
    dev = input('INFORME O NOME COMPLETO DO CLIENTE QUE REALIZOU A DEVOLUÇÃO: ').upper()
    r = 0
    for d in finishn:
        if cadastro[d][0].upper() == dev:
            r = 1
            for p in fantasias:
                for m in range(len(finishc[d])):
                    if fantasias[p][1] == finishc[d][m] and m > 0:
                        fantasias[p][0] += 1
            del finishc[d]
            del finishn[finishn.index(d)]
            print('PRODUTO DEVOLVIDO COM SUCESSO!')
            input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')
            salvar()
            break
    if r == 0:
        print('ESSE CLIENTE NÃO EXISTE OU NÃO POSSUI ALUGUÉIS EM ABERTO.')
        input('==============================\nPRESSIONE ENTER PARA CONTINUAR.')


def dataalug():
    ano_atual = datetime.now().year
    mes_atual = datetime.now().month
    dia_atual = datetime.now().day
    data_atual = ('{}/{}/{}'.format(dia_atual, mes_atual, ano_atual))
    return data_atual


def salvar():
    regsave = open("save.dat", "wb")
    save = {1: fantasias, 2: cadastro, 3: finishc, 4: finishn}
    pickle.dump(save, regsave)
    regsave.close()


def recuperar():
    try:
        regsave = open("save.dat", "rb")
        save = pickle.load(regsave)
        fant = save[1]
        cada = save[2]
        finc = save[3]
        finn = save[4]
        regsave.close()
        return fant, cada, finc, finn
    except:
        regsave = open("save.dat", "wb")
        regsave.close()
        return {}, {}, [], {}


def limpar():
    if os.name == 'nt':
        return os.system('cls')
    else:
        return os.system('clear')


# PROGRAMA PRINCIPAL
cad = 0
fantasias, cadastro, finishc, finishn = recuperar()
while cad != '' or cad == '3':
    limpar()
    print('===============================\n           PyFantasy\n SUA FANTASIA É NOSSA ALEGRIA!\n===============================')
    cad = str(input('OLÁ, SEJA BEM VINDO A PYFANTASY\n[1] ENTRAR\n[2] CADASTRAR-SE\n[3] SOBRE NÓS\nPARA SAIR TECLE "ENTER".\n')).upper()
    if cad == '1':
        limpar()
        login = str(input('DIGITE SEU LOGIN: \n'))
        password = str(input('DIGITE SUA SENHA: \n'))
        if login in cadastro and password in cadastro[login]:
            print('LOGIN REALIZADO COM SUCESSO')
            carrinho = intro_menucliente()
        elif login == cadastroloja[0] and password == cadastroloja[1]:
            print('LOGIN PROFISSIONAL REALIZADO COM SUCESSO')
            nameloja = input('QUEM ESTÁ ACESSANDO? \n')
            intro_menuloja()
        else:
            print('SENHA OU LOGIN INCORRETO, REALIZE O LOGIN NOVAMENTE.')
            input('PRESSIONE ENTER PARA CONTINUAR.')
            limpar()
    elif cad == '2':
        limpar()
        print('INFORME AS SEGUINTES INFORMAÇÕES:')
        newlogin = verificar_login()
        newpassword = verificar_senha()
        newname = verificar_nome()
        newnumber = verificar_telefone()
        newemail = verificar_email()
        cadastro[newlogin] = newname, newnumber, newlogin, newpassword, newemail
        print('CADASTRO REALIZADO COM SUCESSO, BOAS COMPRAS!')
        cad = '1'
        salvar()
        input('PRESSIONE ENTER PARA CONTINUAR.')
    elif cad == '3':
        limpar()
        actioncliente_sobre()
    elif cad == '':
        limpar()
        print('OBRIGADO, VOLTE SEMPRE.')
    else:
        limpar()
        print('POR GENTILEZA, DIGITE "SIM" OU "NÃO".')
salvar()
