StackSync API module
--------------------


1) Install StackSync REST API.

    $ sudo python setup.py install


2) Edit your proxy-server.conf pipeline to enable the StackSync API module.

    [pipeline:main]
    pipeline = healthcheck cache authtoken keystone stacksync-api proxy-server

3) And add the WSGI filter below:

    [filter:stacksync-api]
    use = egg:stacksync-api-swift#stacksync_api
    stacksync_host = 167.88.36.138
    stacksync_port = 61234

4) Restart the proxy:

    $ swift-init proxy restart

You can see the API specifications [here](https://github.com/stacksync/swift-API/blob/master/StackSync_API_Specifications.md)
