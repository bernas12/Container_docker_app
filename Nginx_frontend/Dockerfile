FROM nginx:latest

#Copy the conf file
COPY frontend.conf /etc/nginx/conf.d/default.conf

#Copy the index.html file
COPY index.html /usr/share/nginx/html/

#Expose the same port as in the conf file
EXPOSE 80