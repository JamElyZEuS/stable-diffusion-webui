from pyngrok import ngrok, conf, exception


def connect(token, port):
    conf.get_default().auth_token = token
    try:
        public_url = ngrok.connect(port).public_url
    except exception:
        print(f'Invalid ngrok authtoken, ngrok connection aborted.\n'
              f'Your token: {token}, get the right one on https://dashboard.ngrok.com/get-started/your-authtoken')
    else:
        print(f'ngrok connected to localhost:{port}! URL: {public_url}')