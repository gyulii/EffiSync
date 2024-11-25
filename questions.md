# Questions and thoughts
- Right now in the Record time frame, the 3 settings are: Project, Topic, and Booking text.
  - On the recorded times frame, we only see Project out of these three. Is there any reason for the other 2?
  - If so, shouldn't we have them in the database schema as well?
- On the recorded times frame, there are columns for start time and end time
  - However, we discussed that in the database any day+project combination should be unique
  - Will we scrap those columns long-term?
  - (This is important because when loading the data from the database, there won't be anything corresponding to this, but there will be one column for the day)

- In the long term:
  - When a manager wants to export the timetables, what will be the filters?