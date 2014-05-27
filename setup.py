try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'vero'
]
requires = ['requests==1.2.3', 'mock==1.0.1']

setup(
    name='vero',
    description='Python wrapper for Vero API',
    long_description=open('README.rst').read(),
    version='1.1.3',
    author=open('AUTHORS.rst').read(),
    author_email='opensource@waveaccounting.com',
    url='https://github.com/waveaccounting/vero-python',
    packages=packages,
    package_data={'': ['LICENSE.rst', 'AUTHORS.rst', 'README.rst']},
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    license=open('LICENSE.rst').read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
)
