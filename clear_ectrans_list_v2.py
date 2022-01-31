"""
run on ECMWF-Server: python clear_ectrans_list_v2.py

package requirements: subprocess (pip install subprocess)

original author: A. Plach, updated by K. Baier

"""

from subprocess import check_output#, run
import subprocess
# write output of ecaccess-ectrans-list to a variable, but transfer it
# to a string (from bytes format) and split at newline

out = str(check_output(['ecaccess-ectrans-list'])).split('\n')

for i,line in enumerate(out):
    line_tmp = line.split()
    procID = line_tmp[0]
    try:
         subprocess.check_call(['ecaccess-ectrans-delete', str(procID)])
         print(str(procID))
    except TypeError as e:
        print(e)
