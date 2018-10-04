# oxd Python Demo site

This is a demo Python Flask app to show how to use oxd-python to perform authentication with an OpenID Provider and fetch user information.

## Deployment

### Prerequisites

1. **Client Server**

    * Python 2.7 with pip installed
    * oxd-server running in the background. [Install oxd server](https://gluu.org/docs/oxd/install/)

2. **OpenID Provider**

     * An OpenID provider like Gluu Server. [Install Gluu Server](https://gluu.org/docs/ce/3.1.1/)

### Testing OpenID Connect with the demo site

* Install oxd-python in the Client server:

```bash
git clone https://github.com/GluuFederation/oxd-python.git
cd oxd-python
python setup.py install
```

* Switch to the demosite folder

```bash
cd examples/flask_app
```

* Edit the `demosite.cfg` file. Add the URI of the OpenID Provider (OP) in the `op_host` field, e.g. `https://idp.example.com`. If `op_host` was configured during installation, this step can be skipped.
  
* Edit `/etc/hosts` and point `client.example.com` at the IP Address of the server where the demo app is installed, e.g. `100.100.100.100 client.example.com`

* Run the demo server

```bash
pip install flask
pip install pyOpenSSL
python demosite.py
```

Enable **basic** script on your gluu-server: Maganage Custom Scripts -> Person Authentication -> basic

Now the demosite can be accessed at [https://client.example.com:8080](https://client.example.com:8080)

