from setuptools import setup, find_packages

setup(name='camel_snake_kebab',
      version='0.3.2',
      description='A Python library for word case conversions',
      url='https://github.com/t6/camel_snake_kebab',
      author='Tobias Kortkamp',
      author_email='t@tobik.me',
      license='Eclipse Public License v1.0',
      packages=find_packages(),
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      keywords='snake_case CamelCase kebab-case',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.4'])
