from subprocess import check_output, run

# write output of ecaccess-ectrans-list to a variable, but transfer it
# to a string (from bytes format) and split at newline
out = str(check_output(['ecaccess-ectrans-list'])).split('\\n')

for line in out:
    line_tmp = line.split()
    procID = line_tmp[0]
    print(procID)
    try:
        run(['ecaccess-ectrans-delete', str(procID)])
    except TypeError as e:
        print(e)
