#!/bin/bash
git clone --recurse-submodules https://PRIVATE_TOKEN@github.com/bnusunny/stable-diffusion-on-eks.git
cd ~/SageMaker/SDonEKS-Deploy/stable-diffusion-on-eks
npm install
cdk bootstrap
cdk deploy --all —no-rollback