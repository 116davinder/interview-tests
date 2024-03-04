job "layman" {
  region = "us"
  datacenters = ["us-west-1"]
  type = "service"

    constraint {
        attribute = "${device.model}"
        operator  = "="
        value     = "Nivida RTX 3090"
    }

    constraint {
        attribute = "${meta.custom_user_id}"
        operator  = "="
        value     = "xxxxxxxxx"
    }

  group "group1" {
    # Specify the number of these tasks we want.
    count = 5
    task "task-1" {
      driver = "docker"
      config {
        image = "hashicorp/user-task-1"
      }
      resources {
        cpu    = 500 # MHz
        memory = 128 # MB
      }
    }
  }
}
