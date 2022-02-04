from distutils.core import setup
setup(
  name = 'hero',
  packages = ['hero'],
  version = '0.1',
  license='MIT',
  description = 'Hero',
  author = 'Hoewon Kim',
  author_email = 'hoewon.kim@gmail.com',
  url = 'https://github.com/danielhwkim/Hero',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/danielhwkim/Hero/archive/hero-0_1.tar.gz',    # I explain this later on
  keywords = ['hero'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'argparse',
          'logging',
          'zeroconf',
          'threading',
          'typing',
          'time',
          'socket'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
