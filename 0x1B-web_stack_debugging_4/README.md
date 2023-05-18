Task 0
How to improve performance of a webserver...
- Run Apache Bench after installation of apache bench
- With this command: ab -c 100 -n 2000 localhost/ 
- This will send 2000 requests, 100 at a time
- Check online what the problem might be then check discripancies with default nginx config file and
- What we have in the sandbox then change and restart then run ab -c 100 -n 2000 localhost/
-  to check if it is fix
