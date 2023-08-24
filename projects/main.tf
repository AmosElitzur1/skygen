resource "null_resource" "test" {
  provisioner "local-exec" {
    command = "echo 'hello from ${var.name}'" 
  }
}

variable "name" {
  type        = string
  default     = ""
}
