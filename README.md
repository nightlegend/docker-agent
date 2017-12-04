# docker-agent

### A docker daemon api develop by python3


####API Information example

* create client

    URL :
    
    ``localhost:8000/create_client``

    POST JSON DATA :
    
    ``{
        "docker_daemon_url": "http://localhost:2375",
        "client_id": "${client_id}"
    }``
    
    RETURN:
    
    ``100: create failed``
    
    ``200: create success``

* show client information
    
    URL:
    
    ``localhost:8000/show_docker_client_info/${client_id}``
    
    RETURN:
    >Return a json format data
   
