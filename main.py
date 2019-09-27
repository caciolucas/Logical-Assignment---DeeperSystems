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
    for mensagem in locals()['usuario_%s' %usuario]:
        horario=float(mensagem['ts'])
        horarioemminutos=horario/60
        ts=float(mensagem['ts'])
        if locals()['usuario_%s' %usuario][0] == mensagem:
            horarioatual=horario
            limite=horarioemminutos+2
            locals()['dicionario_%s' %usuario][ts]=[]
            locals()['dicionario_%s' %usuario][ts].append(mensagem)
        else:      
            if horarioemminutos>limite and locals()['dicionario_%s' %usuario].keys():
                locals()['dicionario_%s' %usuario][ts]=[]
                horarioatual=horario
                limite=horarioatual+2
                locals()['dicionario_%s' %usuario][horarioatual].append(mensagem)
            else:
                locals()['dicionario_%s' %usuario][horarioatual].append(mensagem)
                
        
for usuario in usuarios:
    with open('%s.json'%usuario, 'w') as json_file:
        json.dump(locals()['dicionario_%s' %usuario], json_file, indent=2)
        
        




    
        

