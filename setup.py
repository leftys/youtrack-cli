from distutils.core import setup



setup(
    name='youtrack-cli',
    version='1.0',
    author='Jan Skoda',
    author_email='skoda@jskoda.cz',
    scripts=['yt'],
    url='http:/github.com/lefty/youtrack-cli',
    license='GNU/GPLv3',
    description='Command line tool for manipulating issues on YouTrack',
    requires = {
        'youtrack' : ['youtrack>=0.12.1,<1'],
        'click': ['click>=7.0,<8'],
    },
)