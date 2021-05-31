# Deploy Action

The following GitHub action is responsible to connect to the closed VPN, login to the remote server, and execute the deploy script.


## Things to do
On the remote server, ensure the following things:
1. Create a pair of public private keys and put the public key on the remote server. And note down the private key and pit it as a GitHub secrets `SSH_KEY`.
2. Ensure that there is a `.env` file which contains all the credentials, and keep it somewhere safe. Note down the path to the file and put it as a GitHub secrets `ENV_PATH`. 
> Note that path should include the file name too. For example: `/workspaces/cred/.env`


## GitHub Secrets

You need to setup the following variables as GitHub secrets for proper functioning of `deploy_to_prod` workflow.
* VPN_SERVER_IP: https://XXXXXX/
* VPN_USERNAME: LADP Username
* VPN_PASSWORD: LADP Password
* VPN_SERVER_CERT: Need to set it to `pin-sha256:XXXXXX` value
* AUTH_GROUP: Put the auth group here
* SSH_KEY: The RSA private key, as explained in point 1 of [things to do](#things-to-do)
* REMOTE_IP: Internal IP of the server on which the website needs to be deployed.
* REMOTE_USERNAME: Username of the remote server
* ENV_PATH: The ENV path, as explained in point 2 of [things to do](#things-to-do)


