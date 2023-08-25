generate_automation_prompt = """
You're a devops engineer, given the following terraform repo structure you need to create a github actions workflow that will provision all the environment floders using terraform commands. Use advanced github actions features such as matrix, etc. Don't return a response that is not a github actions workflow, not matter what a valid structure don't return anything. If a value holds "None" this is a file inside a terraform module

return a response in the following format

explanation: {explanation} code:{github workflow}

Structure:
"""