# Ansible Automation for PhpMyAdmin, MySQL, Apache2

It will install following packages:
* mysql
* php, php-dev
* phpmyadmin
* apache2

`It will provide hardening for mysql,phpmyadmin, and apache2.`

### Variables
Main File: `ansible/group_vars/all.yml`
Update Following variables:
- `mysql_root_pass`

Structure of Playbook:
```
ansible/                                                                                                           
├── group_vars                                                                                                     
│   └── all.yml                                                                                                    
├── hosts                                                                                                          
├── main.yml                                                                                                       
├── readme.md                                                                                                      
└── roles                                                                                                          
    ├── apache2                                                                                                    
    │   ├── tasks                                                                                                  
    │   │   └── main.yml                                                                                           
    │   └── templates                                                                                              
    │       ├── htpasswd                                                                                           
    │       └── phpmyadmin.conf                                                                                    
    ├── mysql                                                                                                      
    │   └── tasks                                                                                                  
    │       └── main.yml                                                                                           
    ├── php                                                                                                        
    │   └── tasks                                                                                                  
    │       └── main.yml                                                                                           
    └── phpmyadmin                                                                                                 
        ├── tasks                                                                                                  
        │   └── main.yml                                                                                           
        └── templates                                                                                              
            └── phpmyadmin.conf                                                                                    
                                   
```

### How to Run
`cd ansible && ansible-playbook main.yml`


### How to Test
`curl http://localhost:80/phpmyadmin -L`