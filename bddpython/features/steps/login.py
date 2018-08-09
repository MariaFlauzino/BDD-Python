from behave import given, then
from modules.loginPage import loginPage

@given(u'que eu acessei o formulário de Login "{link}"')
def acessa_login(context, link):
    context.browser.get(link)


@when(u'preencho o campo email com "{email}" e "{password}"')
def execute_logar(context,email,password):
    loginPage.logar(email,password)

# @then(u'sou logado com sucesso')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then sou logado com sucesso')


# @then(u'sou redirecionado para o painel de tarefas com a mensagem "Olá, Maria"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then sou redirecionado para o painel de tarefas com a mensagem "Olá, Maria"')


# @when(u'preencho o campo email com "eu@papito.io" e "xpt123"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When preencho o campo email com "eu@papito.io" e "xpt123"')


# @then(u'devo ver a mensagem de alerta "Senha inválida."')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo ver a mensagem de alerta "Senha inválida."')


# @when(u'preencho o campo email com "padre.kevedo@noekzite.com" e "123456"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When preencho o campo email com "padre.kevedo@noekzite.com" e "123456"')


# @then(u'devo ver a mensagem de alerta "Usuário não cadastrado."')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo ver a mensagem de alerta "Usuário não cadastrado."')


# @when(u'preencho o campo email com "maria%noekzite.com" e "123456"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When preencho o campo email com "maria%noekzite.com" e "123456"')



# @then(u'devo ver a mensagem de alerta "Email incorreto ou ausente."')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then devo ver a mensagem de alerta "Email incorreto ou ausente."')


# @when(u'preencho o campo email com "" e "123456"')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When preencho o campo email com "" e "123456"')