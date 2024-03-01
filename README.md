GitHub Repo Link: https://github.com/nomy-nom/aws-cicd-hosting

Hi there! Thanks for visiting my page. Here's a a quick overview of the project:
 
Main components to this site:
1) Continuous Integration and Continuous Deployment (CI/CD)
  
Changes made to the code are automatically pushed through a CI/CD pipeline to update the website's progress

2) API Integration

The website dynamically fetches information from a README page using API Gateway and Lambda function, with the configuration stored in /lambda_function.py file

3) Frontend Development

The frontend of the website is built using HTML, CSS, and JavaScript, along with GitHub API integration. It is hosted using CloudFront and Route 53

4) Infrastructure as Code (IaC)
  
The AWS resources are managed and provisioned using Terraform, with the configuration stored in the /main.tf file.

5) Containerization
  
The website's backend is containerized using Docker, specifically utilizing a Node.js image from Docker Hub, with the configuration stored in the /Dockerfile file


![Alt Text](https://github.com/nomy-nom/aws-cicd-hosting/blob/main/imges/overview.png?raw=true)


