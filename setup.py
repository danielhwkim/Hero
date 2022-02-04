from distutils.core import setup
setup(
  name = 'hero',
  packages = ['hero'],
  version = '0.1',
  license='MIT',
  description = 'Hero',
  author = 'Hoewon Kim',
  author_email = 'hoewon.kim@gmail.com',
  url = 'https://github.com/danielhwkim/Hero',
  download_url = 'https://github.com/danielhwkim/Hero/archive/refs/tags/v_0_1.tar.gz',
  keywords = ['hero'],
  install_requires=[
          'argparse',
          'logging',
          'zeroconf',
          'threading',
          'typing',
          'time',
          'socket'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
