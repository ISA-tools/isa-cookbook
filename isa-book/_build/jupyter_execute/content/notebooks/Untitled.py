import isatools
import os
import sys
from isatools import isatab

my_json_report_bii_i_1 = isatab.validate(open(os.path.join('./BII-I-1/', 'i_investigation.txt')))

with open(os.path.join('./BII-S-3', 'i_gilbert.txt')) as fp:
            ISA = isatab.load(fp)

ISA.studies[0].description

my_json_report_bii_s_3 = isatab.validate(open(os.path.join('./BII-S-3/', 'i_gilbert.txt')))

my_json_report_bii_s_4 = isatab.validate(open(os.path.join('./BII-S-4/', 'i_investigation.txt')))

my_json_report_bii_s_5 = isatab.validate(open(os.path.join('./BII-S-5/', 'i_investigation.txt')))

my_json_report_bii_s_7 = isatab.validate(open(os.path.join('./BII-S-7/', 'i_matteo.txt')))

my_json_report_bii_s_7

