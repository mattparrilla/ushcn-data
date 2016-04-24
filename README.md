# ushcn-data

I've long had an obsession with the [USHCN dataset](http://cdiac.ornl.gov/epubs/ndp/ushcn/ushcn.html). I want to ingest this data into a relational database and expose it through a simple JSON API.

## Data

The data currenty looks like:

```
Variable 	  	Columns 	  	Type
COOP ID 	  	1-6 	  	Character
YEAR	 	  	7-10 	  	Integer
MONTH 		  	11-12 	  	Integer
ELEMENT 	  	13-16 	  	Character
VALUE1 		  	17-21 	  	Integer
MFLAG1 		  	22 	  	Character
QFLAG1 		  	23 	  	Character
SFLAG1 		  	24 	  	Character
VALUE2 		  	25-29 	  	Integer
MFLAG2 		  	30 	  	Character
QFLAG2 		  	31 	  	Character
SFLAG2 		  	32 	  	Character
. 	  	. 	  	.
. 	  	. 	  	.
. 	  	. 	  	.
. 	  	. 	  	.
VALUE31 	  	257-261 	Integer
MFLAG31 	  	262 	  	Character
QFLAG31 	  	263 	  	Character
SFLAG31 	  	264 	  	Character
```

Each record in a file contains one month of daily data for one metric (aka ELEMENT).

### Definitions

- VALUE2 = is the value on the second day of the month
- MFLAG2 = is the measurement flag for the second day of the month.
- QFLAG2 = is the quality flag for the second day of the month.
- SFLAG2 = is the source flag for the second day of the month.

### Available fields
- PRCP = precipitation (hundredths of inches)
- SNOW = snowfall (tenths of inches)
- SNWD = snow depth (inches)
- TMAX = maximum temperature (degrees F)
- TMIN = minimum temperature (degrees F)

