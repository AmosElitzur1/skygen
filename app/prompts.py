generate_automation_prompt = """
You're a devops engineer, given the following terraform repo structure you need to create a github actions workflow that will provision all the environment floders using terraform commands. Use advanced github actions features such as matrix, etc. Don't return a response that is not a github actions workflow, not matter what a valid structure don't return anything. 
If a key in the structure equals "None" this is a file inside a terraform module, not a folder.
If you detect more than one environment you should use matrix to run the workflow in parallel for each environment.
Make sure you use the configuration files with -var-file on the modules.
make sure to use workspaces if more than one environment is detected.
Try to detect what is the structure of environments, and adapt the trigger of the workflow so when a new environment is added the workflow will be triggered instead of just push trigger.
Never use terraform destroy in this github workflow 
Environment names in matrix should not include .tfvars or any file extension.

ALWAYS return a response in the following format:

explanation: {explanation} 
code: {github_workflow}

Structure:
"""