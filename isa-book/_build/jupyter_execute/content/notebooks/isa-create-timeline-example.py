# Isa Create Mode


from isatools.model import *
from isatools.create.models import *
from isatools.create.models import StudyCell


# Treatments
Here we will try to create a few treatments:

NAME = 'name'
treatment_0_conf = dict(TYPE=INTERVENTIONS['CHEMICAL'], FACTORS_0_VALUE='nitroglycerin',FACTORS_1_VALUE=5, FACTORS_1_UNIT='kg/m^3', 
                            FACTORS_2_VALUE=100.0, FACTORS_2_UNIT = 's')
treatment_1_conf = dict(TYPE=INTERVENTIONS['CHEMICAL'], FACTORS_0_VALUE='aether',FACTORS_1_VALUE=1.25, FACTORS_1_UNIT='g', 
                            FACTORS_2_VALUE=60000.0, FACTORS_2_UNIT = 's')
treatment_2_conf = dict(TYPE=INTERVENTIONS['RADIOLOGICAL'], FACTORS_0_VALUE='gamma ray',FACTORS_1_VALUE=10, FACTORS_1_UNIT='gy', 
                            FACTORS_2_VALUE=60000.0, FACTORS_2_UNIT = 's')
treatment_3_conf = dict(TYPE=INTERVENTIONS['DIET'], FACTORS_0_VALUE='glucose',FACTORS_1_VALUE=0.25, FACTORS_1_UNIT='kg', 
                            FACTORS_2_VALUE=30, FACTORS_2_UNIT = 'day')

treatment_3_conf.keys()

Treatment(treatment_3_conf.get('TYPE', None))

Treatment(treatment_3_conf['TYPE']).treatment_type


treatment_3_conf.items()

treatments = [Treatment(treatment_type=conf.get('TYPE',None), factor_values=(
    FactorValue(factor_name=StudyFactor(name=BASE_FACTORS_[0]['name']), value=conf['FACTORS_0_VALUE']),
    FactorValue(factor_name=StudyFactor(BASE_FACTORS_[1]['name']), value=conf['FACTORS_1_VALUE'], unit=conf['FACTORS_1_UNIT']),
    FactorValue(factor_name=StudyFactor(BASE_FACTORS_[2]['name']), value=conf['FACTORS_2_VALUE'], unit=conf['FACTORS_2_UNIT'])
)) for conf in [treatment_0_conf, treatment_1_conf, treatment_2_conf, treatment_3_conf]]


treatments

## Study Epochs:
Here we will create three epochs. The central epoch will have two concomitant treatments.

sample_plan = SampleAssayPlan()

sample_plan

epoch_0 = StudyCell(name='first', elements=[treatments[0]])
epoch_1 = StudyCell(name='second', elements=(treatments[1], treatments[2]))
epoch_2 = StudyCell(name='third', elements=(treatments[2], treatments[2]))

epoch_0

epoch_1

epoch_2

# Study Design
Here we compose a study design with the three study epochs

study_design =  StudyDesign()

# Study Design Factory
Here we use a `StudyDesignFactory` class to generate study designs:

factory = StudyDesignFactory(treatments, sample_plan)

factory

crossover_design = factory.compute_crossover_design(screen=True, follow_up=True)
parallel_design = factory.compute_parallel_design(screen=True, follow_up=True)

crossover_design

study_design = StudyDesign(crossover_design)

study_design

