from setuptools import setup

setup(name='persephone',
      version='0.3.2',
      description='A tool for developing automatic phoneme transcription models',
      long_description=open('README.rst').read(),
      url='https://github.com/oadams/persephone',
      author='Oliver Adams',
      author_email='oliver.adams@gmail.com',
      license='GPLv3',
      packages=['persephone', 'persephone.datasets', 'persephone.preprocess'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='speech-recognition machine-learning acoustic-models artificial-intelligence neural-networks',
      install_requires=[
           'ipython==6.2.1',
           'GitPython==2.1.8',
           'nltk==3.2.5',
           'numpy==1.15.0',
           'python-speech-features==0.6',
           'keras==2.2.2',
           'scipy==1.1.0',
           'tensorflow==1.10.0',
           'scikit-learn==0.19.1',
           'pympi-ling==1.69',
           'pydub==0.20.0',
           'pint==0.8.1',
      ],
      include_package_data = True,
)
