#### Python client for the kubernetes API

#  ingress

we can use the client module to interact with the resources. 

`Resources:` kubectl get commands are used to create ingress using yaml files in a cluster for eg:

To create the ingress in the cluster, we fire following kubectl command:

```kubectl apply -f ingress.yaml``` 

Get the list of all ingress

`kubectl get ingress`

But In Python, we instantiate NetworkingV1Api class from client module:

`client_api = client.NetworkingV1Api()`         

Here I've created the client with it's respective class NetworkingV1Api
and storing in a var named as client_api. so furture we can use it.

`KubeConfig:` to pass the on local cluster e.g minikube we use bellowcommand: 

`config. load_kube_config()`

#### Authenticating to the Kubernetes API server

But what if you want to list all the automated ingress of a GKE Cluster, you must need to authenticate the configuration

`configuration.api_key = {"authorization": "Bearer" + bearer_token}` 

I've used Bearer Token which enable requests to authenticate using an access key.

### create and get ingress:

refer to my other ingress template

#### update ingress:

Call the funcation update_ingress(cluster_details,k8s_object_name="minimal-ingress")

NOTE: You can't update the metadata name of existing ingress.

And run following command:

`python3 ingress.py`

#### get the list of all ingress:

call the funcation delete_ingress(cluster_details,k8s_object_name="minimal-ingress")

`python3 ingress.py`
