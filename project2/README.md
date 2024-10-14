# web client and server 2.0

## Added Files

* `index.html`: temporary homepage if connecting to root

* `file1.txt`: test file for proper 'text/plain' responses

* `file2.html`: test file for proper 'text/html' responses

## Running

For webclient.py Commandline:

* `python3 webclient.py -w domain_name -p port_number` Domain name is required. Port number is optional. Default is 80

For webserver.py Commandline:

* `python3 webserver.py -p port_number` Port number is required. 

## Function Hierarchy

* `main`: driver function
	* `create_response`: Takes a filename, including extension, and creates a web response with it
	
## Notes

* `No update to the webclient. 

* `webclient was used for debugging purposes.

* `Only supports html and txt extensions currently.

* `If files don't exist in directory, 404 error is sent

* `Other types of files will result in nothing getting sent and the connection closing