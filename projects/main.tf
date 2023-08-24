resource "null_resource" "test" {
  provisioner "local-exec" {
    command = "echo 'hello form ${var.name}'" 
  }
}

variable "name" {
  type        = string
  default     = ""
}
