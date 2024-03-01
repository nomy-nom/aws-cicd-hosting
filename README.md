GitHub Repo Link: https://github.com/nomy-nom/aws-cicd-hosting

Hi there! Thanks for visiting my page. Here's a a quick overview of the project:

Main components to this site:
1) CICD: Code changes are pushed and reflected in  CICD progress
2) API: This readme page is pulled on the website dynamically using API Gateway and Lambda 
3) Frontend: covered by HTML/CSS, Javascript, and GitHub API. Hosted with Cloudfront and Route53

   
    Github folder: /frontend
5) IaC: AWS resources written only with Terraform
    Github file: /main.tf
6) Containerzation: Utilizes docker image for node.js (FROM node:20)
    Github file: /Dockerfile


![Alt Text](https://github.com/nomy-nom/aws-cicd-hosting/blob/main/imges/overview.png?raw=true)


