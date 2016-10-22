#chapter4
#Standalone Programs
print(" this standalone program works!")#name it test1.py and type python tes1.py to see result
#command-line arguments
import sys
print('program arguments: ',sys.argv)
#modules and the import statement
#import a module
import report #report is another script named report.py
description = report.get_description()
print("today's weather: ",description)
#import a module with another name
import report as wr
description = wr.get_description()
print("tomorrow's weather: ",description )
#Import Only What You Want from a Module
from report import get_description
description = get_description()
print("tonight's weather: ",description)
#same thing with another name
from report import get_description as do_it
description = do_it()
print("morning's weather: ",description)
#module search path
import sys
for place in sys.path:
    print(place)
#packages
from sources import daily, weekly#daily,weekly located in /sources
print("daily forecast: ",daily.forecast())
print("weekly forecast: ")
for number, outlook in enumerate(weekly.forecast(),1):
    print(number,outlook)
