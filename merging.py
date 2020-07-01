import pandas as pd
import xarray as xr

merged_variable = []
file = open('filename.txt')#read the filename and filename must be in correct order
for i in file:
  d1 = i.strip('\n')
  d = xr.open_dataset(d1)
  variables = d['var130'][:,35,:,:]
  merged_variable.append(variables)

data1 = xr.concat(merged_variable,dim='time')
data1.to_netcdf('newfile.nc',format='NETCDF4')
