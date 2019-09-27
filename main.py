import json
##from datetime import timedelta
##from datetime import datetime



dados = open('source.json').read()

mensagens = json.loads(dados)
usuarios=[]

array_final=[]

for mensagem in mensagens:
    if mensagem['user'] not in usuarios:
        usuarios.append(mensagem['user'])
        locals()['usuario_%s' %mensagem['user']]=[]
        locals()['json_usuario_%s' %mensagem['user']]=[]
        

for mensagem in mensagens:
    for usuario in usuarios:
        if mensagem['user'] == usuario:
            locals()['usuario_%s' %mensagem['user']].append(mensagem)

for usuario in usuarios:
    locals()['dicionario_%s' %usuario]={}
    limite = 0
    for mensagem in locals()['usuario_%s' %usuario]:
        horario=float(mensagem['ts'])
        horarioemminutos=horario/60

        if horarioemminutos>limite:
            locals()['dicionario_%s' %usuario][horario]=[]
            locals()['dicionario_%s' %usuario][horario].append(mensagem)
            horarioant = horario=float(mensagem['ts'])
            limite=horarioemminutos+2
        else:
            locals()['dicionario_%s' %usuario][horarioant].append(mensagem)


        
##        horario=float(mensagem['ts'])
##        horarioemminutos=horario/60
##
##        if horarioemminutos>limite:
##            locals()['dicionario_%s' %usuario][horario]=[]
##            locals()['dicionario_%s' %usuario][horario].append(mensagem)
##            horarioant = horario=float(mensagem['ts'])
##            limite=horarioemminutos+2
##        else:
##            if x==0:
##                locals()['dicionario_%s' %usuario][horario]=[]
##                horarioant = float(mensagem['ts'])
##                limite=horarioemminutos+2
##                x+=1
##            locals()['dicionario_%s' %usuario][horarioant].append(mensagem)


for usuario in usuarios:
    with open('%s.json'%usuario, 'w') as json_file:
        json.dump(locals()['dicionario_%s' %usuario], json_file, indent=2)
        
        




    
        

