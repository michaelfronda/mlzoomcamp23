# NOTES

kind version 0.20.0

(base) michaelfronda@michaels-mbp-2 HW10 % kind create cluster
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.27.3) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Thanks for using kind! 😊

(base) michaelfronda@michaels-mbp-2 HW10 % kubectl cluster-info
Kubernetes control plane is running at https://127.0.0.1:53204
CoreDNS is running at https://127.0.0.1:53204/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.


(base) michaelfronda@michaels-mbp-2 HW10 % kubectl get service
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   7m1s


Command to upload docker image: kind load docker-image <DOCKER IMAGE NAME>
