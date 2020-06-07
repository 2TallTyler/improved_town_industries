# print statements aren't necessary, but they help see what the script is doing when it runs
# print is helpful for 'wtf?' moments
print("Python: Combining NML files")

 # this module is a good way to handle working with files that might contain unicode (e.g. translations) 
import codecs

sections = [] # create an empty list, we'll put strings in here then join them later

# get the header file and append to a list
header = codecs.open("src/header.nml",'r','utf8')
sections.append(header.read())
header.close()

farm = codecs.open("src/farm.nml",'r','utf8')
sections.append(farm.read())
farm.close()

coal_mine = codecs.open("src/coal_mine.nml",'r','utf8')
sections.append(coal_mine.read())
coal_mine.close()

power_plant = codecs.open("src/power_plant.nml",'r','utf8')
sections.append(power_plant.read())
power_plant.close()

iron_mine = codecs.open("src/iron_mine.nml",'r','utf8')
sections.append(iron_mine.read())
iron_mine.close()

steel_mill = codecs.open("src/steel_mill.nml",'r','utf8')
sections.append(steel_mill.read())
steel_mill.close()

factory = codecs.open("src/factory.nml",'r','utf8')
sections.append(factory.read())
factory.close()

sawmill = codecs.open("src/sawmill.nml",'r','utf8')
sections.append(sawmill.read())
sawmill.close()

paper_mill = codecs.open("src/paper_mill.nml",'r','utf8')
sections.append(paper_mill.read())
paper_mill.close()

oil_wells = codecs.open("src/oil_wells.nml",'r','utf8')
sections.append(oil_wells.read())
oil_wells.close()

oil_refinery = codecs.open("src/oil_refinery.nml",'r','utf8')
sections.append(oil_refinery.read())
oil_refinery.close()

print("Python: Writing combined NML file")

# create a new file on disk, which will have a name and be writable
processed_nml_file = codecs.open('nmlc/historical_industries.nml','w','utf8')

# write stuff into the file
processed_nml_file.write('\n'.join(sections)) # join the list of templated stuff with newlines, and write to a file
processed_nml_file.close() # we're done with this file now, finish with it
