## Part 1 Question 1
Write an ansible playbook for installing nginx, docker, logrotate.

Ensure nginx container is running on port 8080 on host and log rotation is cleaning the logs of stdout of nginx container once it reaches 100mb.

(Separate roles should be created for the tasks mentioned inline)


### Requirements
* Linux based system is supported (Ubuntu Only)
* `ansible` package installed on your local system.
* you must have `sudo`/`root` access to the local system and test system.
* `vagrant` and `virtualbox` packages if want to run in local system.

### Tested System
* `Ubuntu 20.04`
* `Ansible` Version
```bash
$ ansible --version
ansible [core 2.12.5]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/davinderpal/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/davinderpal/.local/lib/python3.10/site-packages/ansible
  ansible collection location = /home/davinderpal/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0]
  jinja version = 3.1.2
  libyaml = True
```
### Notes*
* I am also assuming that you basic knowledge of `ansible`/`vagrant`/`virtualbox`.
* Since the Question is a bit vague in terms of nginx usage.
I am assuming that Local Nginx can be used as well and may want to run nginx inside
a container both options are available via variables.

### Create Test Infrastructure with Vagrant
```bash
$ cd part-1
$ vagrant up
Bringing machine 'worker' up with 'virtualbox' provider...
==> worker: Importing base box 'ubuntu/bionic64'...
==> worker: Matching MAC address for NAT networking...
==> worker: Checking if box 'ubuntu/bionic64' version '20220506.0.0' is up to date...
==> worker: Setting the name of the VM: part-1_worker_1652106034426_12339
==> worker: Clearing any previously set network interfaces...
==> worker: Available bridged network interfaces:
1) wlp59s0
2) docker0
==> worker: When choosing an interface, it is usually the one that is
==> worker: being used to connect to the internet.
==> worker:
    worker: Which interface should the network bridge to? 1
==> worker: Preparing network interfaces based on configuration...
    worker: Adapter 1: nat
    worker: Adapter 2: bridged
==> worker: Forwarding ports...
    worker: 22 (guest) => 2222 (host) (adapter 1)
==> worker: Running 'pre-boot' VM customizations...
==> worker: Booting VM...
==> worker: Waiting for machine to boot. This may take a few minutes...
    worker: SSH address: 127.0.0.1:2222
    worker: SSH username: vagrant
    worker: SSH auth method: private key
    worker: Warning: Connection reset. Retrying...
    worker: Warning: Remote connection disconnect. Retrying...
==> worker: Machine booted and ready!
.....
    worker:
    worker: Guest Additions Version: 5.2.42
    worker: VirtualBox Version: 6.1
==> worker: Configuring and enabling network interfaces...
==> worker: Mounting shared folders...
    worker: /vagrant => xxxxx
```

### Usage of playbook
* create inventory file similar to `inventories/dev/hosts` if `vargrant` is not used for test system
* Run Playbook

```
$ ansible-playbook -i inventories/dev/hosts main.yml

PLAY [dev] ********************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Docker | Install prequisites] **********************************************************************************************************************************************************************
included: /home/davinderpal/projects/personal/zeta/part-1/roles/docker/tasks/prepare.yml for 127.0.0.1

TASK [docker : Docker | Prepare | Install system dependency (Ubuntu)] *********************************************************************************************************************************************
ok: [127.0.0.1] => (item=ca-certificates)
ok: [127.0.0.1] => (item=curl)
ok: [127.0.0.1] => (item=gnupg)
ok: [127.0.0.1] => (item=lsb-release)
ok: [127.0.0.1] => (item=software-properties-common)
changed: [127.0.0.1] => (item=apt-transport-https)
changed: [127.0.0.1] => (item=virtualenv)
changed: [127.0.0.1] => (item=python3-pip)
ok: [127.0.0.1] => (item=python3-setuptools)

TASK [docker : Docker | Install Docker] ***************************************************************************************************************************************************************************
included: /home/davinderpal/projects/personal/zeta/part-1/roles/docker/tasks/install.yml for 127.0.0.1

TASK [docker : Docker | Install | Add Docker Gpg Key (Ubuntu)] ****************************************************************************************************************************************************
changed: [127.0.0.1]

TASK [docker : Docker | Install | Add repo (Ubuntu)] **************************************************************************************************************************************************************
changed: [127.0.0.1]

TASK [docker : Docker | Install | install docker-ce (Ubuntu)] *****************************************************************************************************************************************************
changed: [127.0.0.1] => (item=docker-ce)
ok: [127.0.0.1] => (item=docker-ce-cli)
ok: [127.0.0.1] => (item=containerd.io)
changed: [127.0.0.1] => (item=docker-compose-plugin)

TASK [docker : Docker | Post Installation] ************************************************************************************************************************************************************************
included: /home/davinderpal/projects/personal/zeta/part-1/roles/docker/tasks/post-install.yml for 127.0.0.1

TASK [docker : Docker | Post-Install | Add Users to Docker Group] *************************************************************************************************************************************************
changed: [127.0.0.1] => (item=vagrant)

TASK [docker : Docker | Post-Install | Install docker package via pip] ********************************************************************************************************************************************
changed: [127.0.0.1]

TASK [docker : Docker  | Post-Install | Make Sure docker service is running] **************************************************************************************************************************************
ok: [127.0.0.1]

TASK [nginx : Nginx | Install prequisites] ************************************************************************************************************************************************************************
included: /home/davinderpal/projects/personal/zeta/part-1/roles/nginx/tasks/prepare.yml for 127.0.0.1

TASK [nginx : Nginx | Prepare | Install system dependency (Ubuntu)] ***********************************************************************************************************************************************
ok: [127.0.0.1] => (item=ca-certificates)
ok: [127.0.0.1] => (item=apt-transport-https)
ok: [127.0.0.1] => (item=gpg-agent)

TASK [nginx : Nginx | Install Nginx] ******************************************************************************************************************************************************************************
included: /home/davinderpal/projects/personal/zeta/part-1/roles/nginx/tasks/install.yml for 127.0.0.1

TASK [nginx : Nginx | Install | Add Nginx Gpg Key (Ubuntu)] *******************************************************************************************************************************************************
............
TASK [nginx : Nginx | Start Nginx via Container] ******************************************************************************************************************************************************************
changed: [127.0.0.1]

TASK [logrotate : Logrotate | Install] ****************************************************************************************************************************************************************************
included: /home/davinderpal/projects/personal/zeta/part-1/roles/logrotate/tasks/install.yml for 127.0.0.1

TASK [logrotate : Logrotate | Install | install logrotate package] ************************************************************************************************************************************************
ok: [127.0.0.1] => (item=logrotate)

TASK [logrotate : Logrotate | Configure] **************************************************************************************************************************************************************************
included: /home/davinderpal/projects/personal/zeta/part-1/roles/logrotate/tasks/configure.yml for 127.0.0.1

TASK [logrotate : Logrotate | Configure | upload logrotate confs from variables] **********************************************************************************************************************************
changed: [127.0.0.1] => (item={'dest': '/etc/logrotate.d/docker-container', 'backup': False, 'content': '/var/lib/docker/containers/*/*.log {\n  size 100M\n  rotate 7\n  hourly\n  compress\n  missingok\n  delaycompress\n  copytruncate\n}\n'})

TASK [logrotate : Logrotate | Configure | find logrotate cron file] ***********************************************************************************************************************************************
ok: [127.0.0.1]

TASK [logrotate : Logrotate | Configure | set logrotate script path] **********************************************************************************************************************************************
ok: [127.0.0.1]

TASK [logrotate : Logrotate | Configure | Copy Logrotate to hourly Cron] ******************************************************************************************************************************************
changed: [127.0.0.1]

PLAY RECAP ********************************************************************************************************************************************************************************************************
127.0.0.1                  : ok=31   changed=14   unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

* Run Test Playbook

```bash
$ ansible-playbook -i inventories/dev/hosts test.yml

PLAY [dev] ********************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [127.0.0.1]

TASK [Test | Gather the package facts] ****************************************************************************************************************************************************************************
ok: [127.0.0.1]

TASK [Test | Check if Docker Community package is installed] ******************************************************************************************************************************************************
ok: [127.0.0.1] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [Test | Check if Nginx package is installed] *****************************************************************************************************************************************************************
ok: [127.0.0.1] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [Test | Check if Logrotate package is installed] *************************************************************************************************************************************************************
ok: [127.0.0.1] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [Test | Fetch data from Nginx Port] **************************************************************************************************************************************************************************
ok: [127.0.0.1]

TASK [Test | Check if Nginx Return Correct Page] ******************************************************************************************************************************************************************
ok: [127.0.0.1] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP ********************************************************************************************************************************************************************************************************
127.0.0.1                  : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
