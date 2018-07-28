# ------------------------------------------------
#                   IMPORTS
# ------------------------------------------------
import discord
import asyncio
import os
# ------------------------------------------------
#                  VARIAVEIS
# ------------------------------------------------

client = discord.Client()
email = "lamanu@loketa.com"
senha = "00000000"

lista_de_membros_final = []


limite = 1
tempo = 60

ver_se_pode_executar_envios = False
contador = 0

mensagemd = "**Oi bb's, venho aqui oferecer meu servidor, o The Light!" \
            "\n\nTemos eventos diários, salas de jogos, sorteios, campeonatos e muito mais!" \
            "\n\nAlém do evento SexClub rsrs.. :smiling_imp: :smiling_imp:\n\nConto com sua presença!**"


@client.event
async def on_ready():
    print("SELF BOT .")
    print("SELF BOT ...")
    print("SELF BOT .....")
    print("SELF BOT .......")
    print("SELF BOT .........")
    print("SELF BOT ...........")
    print("Olá, sou seu SELFBOT. Meu nome é {}, já este é meu ID {}\nEstou conectado(a) em {} servidores.\n".format(
        client.user.name, client.user.id, len(client.servers)))
    # await client.change_presence(game=discord.Game(name='League of Legends', type=1, url='https://www.twitch.tv/bblindadamamae'),status='streaming')
    await client.change_presence(game=discord.Game(name='League of Legends'))

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        await client.send_message(message.channel, "YES")

@client.event
async def on_member_join(member):
    # Adicionar o membro na lista de verificação de ID
    ver_se_esta_na_lista = []
    ver_se_esta_na_lista.append(member)

    verificacao = (list(set(ver_se_esta_na_lista) & set(lista_de_membros_final)))
    if bool(verificacao) == False:
        lista_de_membros_final.append(member)
        print("{} foi adicionado na lista, atualmente temos {} usuários na lista. [{}]\n".format(member.name, len(lista_de_membros_final), member.server.name))

    if ver_se_pode_executar_envios == False:
        await executar_envios(lista_de_membros_final, member)


async def executar_envios(lista_de_membros_final, member):
    # Variáveis globais
    global ver_se_pode_executar_envios
    global contador

    if len(lista_de_membros_final) >= limite and ver_se_pode_executar_envios == False:
        ver_se_pode_executar_envios = True
        while contador < limite and len(lista_de_membros_final) >= 1:
            contador += 1
            try:
                embed = discord.Embed(description='{}'.format(mensagemd), color=0xFF1493)
                embed.set_footer(text='ME ABRAÇA 💓💓', icon_url=client.user.avatar_url)
                embed.set_author(name="The Light", url='https://discord.gg/HWFQ86G', icon_url=client.user.avatar_url)
                embed.set_thumbnail(url=client.user.avatar_url)
                await client.send_message(lista_de_membros_final[0], embed=embed)
                await client.send_message(lista_de_membros_final[0], '🎫 https://discord.gg/HWFQ86G')
                print("Enviado >> {}\n".format(lista_de_membros_final[0].name))
                del lista_de_membros_final[0]
            except discord.errors.Forbidden as msg_erro:
                if str(msg_erro) == str("FORBIDDEN (status code: 403): Cannot send messages to this user"):
                    print("Este usuário falhou: {}. Ele saiu do servidor ou foi bloqueado. Erro: {}\n".format(lista_de_membros_final[0].name, msg_erro))
                    contador -= 1
                    del lista_de_membros_final[0]
                    if contador == limite and len(lista_de_membros_final) >= 1:
                        embed = discord.Embed(description='{}'.format(mensagemd), color=0xFF1493)
                        embed.set_footer(text='ME ABRAÇA 💓💓', icon_url=client.user.avatar_url)
                        embed.set_author(name="The Light", url='https://discord.gg/HWFQ86G', icon_url=client.user.avatar_url)
                        embed.set_thumbnail(url=client.user.avatar_url)
                        await client.send_message(lista_de_membros_final[0], embed=embed)
                        await client.send_message(lista_de_membros_final[0], '🎫 https://discord.gg/HWFQ86G')
                        print("Enviado >> {}\n".format(lista_de_membros_final[0].name))
                        del lista_de_membros_final[0]
                    pass

                if str(msg_erro) == str("FORBIDDEN (status code: 403): You are opening direct messages too fast."):
                    print("Envio de mensagens cancelados. \nMotivo: {}\n".format(msg_erro))
                    contador = limite

            except NameError as msg_error:
                print("Código pausado pra manutenção, envios não serão efetuados por 3 minutos.\nMensagem de exceção: {}\n".format(msg_erro))
                contador = limite

        if contador == limite and ver_se_pode_executar_envios == True or len(lista_de_membros_final) < limite and ver_se_pode_executar_envios == True:
            print("Esperando o delay de {} minutos.\n".format(int(tempo/60)))
            await asyncio.sleep(tempo)
            print("Delay finalizado, pronto para enviar mensagens.\n")
            ver_se_pode_executar_envios = False
            contador = 0
            if len(lista_de_membros_final) >= limite:
                await executar_envios(lista_de_membros_final, member)

client.run(str(os.environ.get('EMAIL')), str(os.environ.get('SENHA')))