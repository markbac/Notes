

a VEN can have multiple profiles associated to it. 

For every VEN there can be Multiple ESA's associated to it.

(VEN = OpenADR Virtual End Node, ESA = Energy Smart Appliance)

Assocaited with a profile are
 - Order
   -  The order can be MS, LD, IO or a numeric 0-999
 - Interval
   - 0-999
 - Frequency response capability
   - 0-10
- ESA IS
  - string

The profiles are identified by the Order. 

For each profile there will be a set of start times, duration and power

E.g 
start_time,duration,power
2023-02-01 11:43:18.451195+00:00,0 days 01:00:00,10000.0
2023-02-01 12:43:18.451195+00:00,0 days 01:00:00,500.0



For each ESA 1 or more profiles (identidified by Order) can be asocciated to it.
Profiles can be updated 

i.e the above data could be replaced with

start_time,duration,power
2023-02-01 11:43:18.451195+00:00,0 days 01:00:00,3000.0
2023-02-01 12:43:18.451195+00:00,0 days 03:00:00,0.0
2023-02-01 15:43:18.451195+00:00,0 days 01:00:00,10000.0
2023-02-01 16:43:18.451195+00:00,0 days 01:00:00,500.0

Note: Only the first start time is mandatory, so teh following is valid
start_time,duration,power
2023-02-01 11:43:18.451195+00:00,0 days 01:00:00,3000.0
,0 days 03:00:00,0.0
,0 days 01:00:00,10000.0
,0 days 01:00:00,500.0

This is because the other start times can be worked out from the initial start time and duration.
