Main ref:
http://tutorial.djangogirls.org/en/

Other refs:
http://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
http://conda.pydata.org/docs/_downloads/conda-pip-virtualenv-translator.html

--

Set anaconda to default python environment in .bash_profile

Update conda
>> sudo conda update conda

Create virtual environment:
>> conda create -n myenv python=3.5 anaconda

Load virtual environment:
>> source activate myenv
>> conda info -e

Install django into virtual environment:
>> sudo conda install -n myenv django

###################################################################
# Follow http://tutorial.djangogirls.org/en/django_start_project/ #
###################################################################
#
# N.B. 'git push' requires 'sudo git push'
#

Deactivate virtual environment:
>> source deactivate

Delete virtual environment:
>> sudo conda remove -n myenv -all