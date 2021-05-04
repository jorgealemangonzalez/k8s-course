eksctl create cluster \
 --name test-cluster \
 --without-nodegroup \ 
 --region eu-west-3 \
 --zones eu-west-3a,eu-west-3b


 eksctl create iamserviceaccount --cluster=test-cluster --namespace=kube-system --name=aws-load-balancer-controller --approve --override-existing-serviceaccounts --attach-policy-arn='arn:aws:iam::113563847585:policy/AWSLoadBalancerControllerIAMPolicy'