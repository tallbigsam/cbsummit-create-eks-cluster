ATTEMPTS=10
WAIT_SEC=120
DNS="se-couchbasedemos.com"

#===============================
#	VPC Information
#===============================
VPC_STACK_NAME="neur-devday-stack"
VPC_TEMPLATE="https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-12-10/amazon-eks-vpc-sample.yaml"

#===============================
#	EKS Cluster
#===============================
EKS_CLUSTER_NAME="neur-devday-cluster"
EKS_ROLE_ARN="arn:aws:iam::669678783832:role/cbd-eks-role"

#===============================
#	EKS Worker Nodes
#===============================
EKS_NODES_TEMPLATE="https://amazon-eks.s3-us-west-2.amazonaws.com/cloudformation/2018-12-10/amazon-eks-nodegroup.yaml"
EKS_NODES_STACK_NAME="neur-devday-cluster-nodes"
EKS_NODE_GROUP_NAME="neur-devday-cluster-eks-nodes"
EKS_NODE_AS_GROUP_MIN="3"
EKS_NODE_AS_GROUP_MAX="3"
EKS_NODE_AS_GROUP_DESIRED="3"

#Amazon instance type - Refer to Amazon Documentation for available values
EKS_NODE_INSTANCE_TYPE="m4.4xlarge"

#Amazon Image Id - Refer to https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html for full list.  The region is important for AMI to use.  The below is for eu-west-1 v1.18
EKS_IMAGE_ID="ami-0316939d36d601217"

#The IAM Key to use
EKS_KEY_NAME="cb-day-se"

EKS_NODE_VOLUME_SIZE="20"

#===============================
#	Secondary User
#===============================
AWS_SECOND_USER_ARN="arn:aws:iam::669678783832:user/cb-day-participant"
AWS_SECOND_USER_NAME="cb-day-participant"
