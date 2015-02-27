# inlinesas #

Call SAS from within a Python script. Pass your SAS code as a string to the call_SAS function. 

Usage:
=======================================

    from inlinesas import call_SAS

    sascode = 'your SAS code as a string'
    result = call_SAS(sascode)

    # You can also specify a location (using absolute path) for the logfile.
    #
    # If no logfile location is specified, no logfile will be created.

    result = call_SAS(sascode, log_location='/path/to/file.log')


You can access the returncode, stdout, and stderr of your SAS run:

`result.returncode`

`result.stdout`

`result.stderr`

