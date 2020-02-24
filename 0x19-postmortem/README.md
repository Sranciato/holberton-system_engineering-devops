# Postmortem
## Issue Summary
From 4:00PM to 5:30pm on February 23 2020, AirBnB flask api could not import flask. When trying to curl the flask api, an error notifying us that we are unable import flask affecting all users. The root cause was the route for the status of the api.
## Timeline
* 4:00PM - Added route for status of api.
* 4:01PM - Could no longer curl flask api.
* 4:45PM - Inspected the status function with the route.
* 5:03PM - Imported flask differently.
* 5:10PM - Reponsibility for fix was assigned to Stephen Ranciato.
* 5:30PM - Stephen landed a double backflip while simultaneously changing the path in the route for the status method, resolving all issues.
## Root Cause
The issue was a direct cause of assigning the wrong path to the status route. The issue was fixed by adding the correct path to the status route.
## Corrective Measures
* Next time be sure that the correct path is added to the status route before pushing the code.
* Testing should be done before every change is implemented.
* Read documentation regarding app.route().
* Log all changes in order to make future bugs easier to discover.
###
![](image.jpg)
