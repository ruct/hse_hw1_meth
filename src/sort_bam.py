# Сортировка bam-файла

import os, subprocess
def sort_bam(bam_file, sorted_version):
  os.system(f'samtools sort {bam_file} -o {sorted_version} && samtools index {sorted_version}')
