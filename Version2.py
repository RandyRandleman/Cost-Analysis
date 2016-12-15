target.write("How large of email pst was analyzed? \n")
x1 = raw_input("How big was the email dump?: ")
target.write(x1 + "\n")

target.write("How many devices were imaged? \n")
acquisition_imaging = raw_input("How many devices were imaged?: ")
target.write(acquisition_imaging + "\n")
acquisition_imaging = int(acquisition_imaging)

target.write("How many hours did you spend analyzing? \n")
analysis_hours = raw_input("How many hours did you spend analyzing?: ")
target.write(analysis_hours + "\n")
analysis_hours = int(analysis_hours)

target.write("How many mobile apps were analyzed? \n")
x4 = raw_input("how many mobile apps were analyzed?:  ")
target.write(x4 + "\n")

target.write("How many hours were spent consulting? \n")
consulting_hours = raw_input("How many hours were spent consulting: ")
target.write(consulting_hours + "\n")
consulting_hours = int(consulting_hours)

target.write("How large were the reports in GB? \n")
x6 = raw_input("How large were the reports in GB?: ")
target.write(x6 + "\n")

#This is where the magic happens
def vendor_costs(consulting_hours, analysis_hours, consulting_rate, analysis_rate, acquisition_rate):
	return (consulting_hours*consulting_rate) + (analysis_hours*analysis_rate) + (acquisition_rate)

companies = {'EY': {'consulting_rate': 400, 'analysis_rate': 300, 'acquisition_rate': 500}, 
'Newberry': {'consulting_rate': 295, 'analysis_rate': 295}, 
'Kroll': {'consulting_rate': 190, 'analysis_rate': 295}}

for company, information in companies.items():
	estimated_cost = vendor_costs(consulting_hours, analysis_hours, information['consulting_rate'], information['analysis_rate'], information['acquisition_rate'])
	print 'Estimated Cost for {} is {}'.format(company,estimated_cost)
	target.write('Estimated Cost for {} is {}'.format(company,estimated_cost))