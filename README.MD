 # To collect EDP data:
  "emon -collect-edp > emon.dat" or
  "emon -collect-edp [edp_file=<edp-events-file>] > emon.dat  (Use edp_file optional option to provide custom events file)"
 # To process data using EDP Ruby script: 
  "emon -process-edp /path/to/edp_config.txt  (requires python xlsxwriter library to generate Excel summary sheet on Linux)"
