from kubernetes import client, config


class K8sInfo:
    def __init__(self, ns='Default', status='Default'):
        self.ns = ns
        self.status = status

    def get_pod_info(self):
        config.load_kube_config()
        k8s_api = client.CoreV1Api()
        # If no parameters are specified, view all problem pods
        if self.ns == "Default" and self.status == "Default":
            field_selector = "status.phase!=Running,status.phase!=Completed"
            try:
                pod_list = k8s_api.list_pod_for_all_namespaces(field_selector=field_selector).items
                for pod in pod_list:
                    print("Pod {} in namespace {} is in {} phase.".format(pod.metadata.name, pod.metadata.namespace,
                                                                          pod.status.phase))
            except client.exceptions.ApiException as e:
                print("Error reading pod list: {}".format(e))
        else:
            if self.status != "Default" and self.ns == "Default" :
                field_selector = "status.phase!={}".format(self.status)
                pod_list = k8s_api.list_namespaced_pod(field_selector=field_selector).items
            elif self.ns != "Default" and self.status == "Default":
                k8s_ns = self.ns
                pod_list = k8s_api.list_namespaced_pod(namespace=k8s_ns).items
            else:
                field_selector = "status.phase!={}".format(self.status)
                k8s_ns = self.ns
                pod_list = k8s_api.list_namespaced_pod(namespace=k8s_ns, field_selector=field_selector).items
            try:
                pod_list = k8s_api.list_pod_for_all_namespaces(field_selector=field_selector).items
                for pod in pod_list:
                    print("Pod {} in namespace {} is in {} phase.".format(pod.metadata.name, pod.metadata.namespace,
                                                                          pod.status.phase))
            except client.exceptions.ApiException as e:
                print("Error reading pod list: {}".format(e))