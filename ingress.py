import json
from kubernetes import client
from kubernetes.client import ApiClient
import yaml
from os import path
from kubernetes.client.rest import ApiException
import json,base64,yaml


def __get_kubernetes_networkv1client(bearer_token,api_server_endpoint):
    try:
        #corev1api=("pod","node","config_map","secret","service","namespace","resource")
        configuration = client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        client_api = client.NetworkingV1Api()
        return client_api
    except Exception as e:
        print("Error getting kubernetes client \n{}".format(e))
        return None


def update_ingress(cluster_details,k8s_object_name=None,yaml_body=None,namespace="default"):
    try:
        client_api= __get_kubernetes_networkv1client(
                bearer_token=cluster_details["bearer_token"],
                api_server_endpoint=cluster_details["api_server_endpoint"],
            )

        yaml_data=open("ingress-update.yml", "rb").read().decode('utf-8')
        yaml_body=yaml.safe_load(yaml_data)

        resp=client_api.patch_namespaced_ingress(
            name=k8s_object_name,body=yaml_body, namespace="{}".format(namespace))
        data=__format_data_for_create_ingress(resp)
        print("Ingress updated: {}".format(data))

    except ApiException as e:
        print("ERROR IN create_deployment:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))
        return __format_data_for_create_ingress(e.body)

def delete_ingress(cluster_details,k8s_object_name=None,namespace="default"):
    try:
        client_api= __get_kubernetes_networkv1client(
                bearer_token=cluster_details["bearer_token"],
                api_server_endpoint=cluster_details["api_server_endpoint"],
            )

        resp=client_api.delete_namespaced_ingress(
            name=k8s_object_name,
            namespace="{}".format(namespace),
            body=client.V1DeleteOptions(
            propagation_policy="Foreground", grace_period_seconds=5
        ))
        data=__format_data_for_create_ingress(resp)
        print("Ingress deleted: {}".format(data))

    except ApiException as e:
        print("ERROR IN create_deployment:\n{}".format(e.body))
        print("TYPE :{}".format(type(e)))
        return __format_data_for_create_ingress(e.body)


if __name__ == '__main__':
    cluster_details={
        "bearer_token":"GKE-Bearer-Token",
        "api_server_endpoint":"Ip-k8s-control-plane"
    }
    
    # update_ingress(cluster_details,k8s_object_name="minimal-ingress")
    # delete_ingress(cluster_details,k8s_object_name="minimal-ingress")