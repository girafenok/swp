CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/swp/etc',
    #'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=16',
        '--timeout=60',
        'hello:hello_app',
    ),
}
