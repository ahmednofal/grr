from setuptools import setup, find_packages

requires = [
    'tornado',
    'jsonrpc',
    'python-keycloak',
    'werkzeug',
    'http',
    'json',

    # 'tornado-sqlalchemy',
    # 'psycopg2',
]

setup(
    name='tornado_todo',
    version='0.0',
    description='Access Control Authority to offer mediation between grr server and grr client',
    author='Ahmed Nofal',
    author_email='ahmednofal@aucegypt.edu',
    keywords='ACAuthority',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'serve_app = todo:main',
        ],
    },
)
