#!/usr/bin/env python3

import connexion


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


def post_full_greeting(name: str, sir_name: str) -> str:
    return 'Hello {name} {sir_name}'.format(name=name, sir_name=sir_name)

app = connexion.FlaskApp(__name__, port=9090, specification_dir='openapi/')
app.add_api('helloworld-api.yaml', arguments={'title': 'Hello World Example'})
application = app.app

