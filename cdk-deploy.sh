#!/bin/bash
cd ~/SageMaker/SDonEKS-Deploy/stable-diffusion-on-eks
npm install
cdk bootstrap
cdk deploy --all