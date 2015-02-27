import subprocess, os, tempfile

class SASReturnObject(object):
    def __init__(self, returncode, stdout, stderr):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        message = 'Call returned code ' + str(self.returncode) + '.\n'
        message += 'stdout: ' + self.stdout + '\n'
        message += 'stderr: ' + self.stderr + '\n'
        return message

def call_SAS(code_as_str, log_location=None):
    """ 
    Call SAS from within a Python script. 

    Usage:
    =======================================

    from inlinesas import call_SAS

    sascode = 'your SAS code as a string'
    result = call_SAS(sascode)
    
    # You can also specify a location (using absolute path) for the logfile.
    #
    # If no logfile location is specified, no logfile will be created.

    result = call_SAS(sascode, log_location='/path/to/file.log')

    =======================================

    You can access the returncode, stdout, and stderr of your SAS run:

    result.returncode
    result.stdout
    result.stderr
    
    """
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(code_as_str)
    f.close() 

    invocation = ['sas', '-sysin', f.name]

    if log_location:
        invocation = invocation + ['-log', log_location]
    else:
        invocation.append('-nolog')

    r = subprocess.Popen(invocation, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = r.communicate()
    
    os.unlink(f.name) # Remove the temporary SAS file

    return SASReturnObject(r.returncode, stdout, stderr)
    
