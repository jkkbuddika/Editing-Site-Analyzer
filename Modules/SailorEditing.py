import os
import glob
import yaml
import subprocess as sp
import ColorTextWriter

class SailorEditing():

    def __init__(self, input_dir, sailor_path, genome_fasta, snp_file, extensions):
        self.input_dir = input_dir
        self.sailor_path = sailor_path
        self.genome_fasta = genome_fasta
        self.snp_file = snp_file
        self.extensions = extensions

    def editing_prediction(self):

        bam_files = sorted(glob.glob(self.input_dir + '*.bam'))

        ctw = ColorTextWriter.ColorTextWriter()

        for i in bam_files:
            if i.endswith(self.extensions[4]):

                print('\n' + ctw.CRED + 'Seraching for A-to-I editing sites: ' + ctw.CBLUE + os.path.basename(i) + ctw.CRED + ' ...' + ctw.CEND + '\n')

                ## Write the .yaml file

                kv_pair = {'input_bam': {'class': 'File', 'path': i},
                           'reference': {'class': 'File', 'path': self.genome_fasta},
                           'known_snp': {'class': 'File', 'path': self.snp_file}}

                yml_file = os.path.basename(i).split('.fastq')[0] + '.yml'

                with open(yml_file, 'w') as f:
                    yaml.dump(kv_pair, f, default_flow_style=False)

                ## Running Sailor with default settings

                command = [
                    'module load singularity;', self.sailor_path, yml_file
                ]

                command = ' '.join(command)
                sp.check_call(command, shell=True)

                ## Move results to "sailor" directory and remove .yml files

                sp.call(['mv', i, os.path.dirname(self.sailor_path) + '/'])
                sp.call('rm -r ' + yml_file, shell=True)

        print(ctw.CBEIGE + ctw.CBOLD + 'A-to-I Editing Site Identification Completed!!!' + ctw.CEND)