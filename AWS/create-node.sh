eksctl create nodegroup \
  --cluster test-cluster \
  --name test-workers \
  --node-type t3.medium \
  --nodes 1 \
  --nodes-min 1 \
  --nodes-max 3 \
  --asg-access 