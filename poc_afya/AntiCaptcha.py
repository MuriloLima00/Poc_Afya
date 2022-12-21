from anticaptchaofficial.recaptchav2proxyless import *

def captchaSolver(link,chave_captcha):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key('96c0546d6b117e6808ec6326fc98df0d')
    solver.set_website_url(link)
    solver.set_website_key(chave_captcha)

    resposta = solver.solve_and_return_solution()

    if(resposta != 0):
        return resposta
    else:
        print(solver.err_string)