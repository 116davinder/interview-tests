job "mining-datacenter" {
  region = "us"
  datacenters = ["us-west-1"]
  type = "service"

  constraint {
    attribute = "${meta.custom_user_id}"
    operator  = "="
    value     = "xxxxxxxxx"
  }

  group "group1" {
    # Specify the number of these tasks we want.
    count = 1000

    affinity {
      attribute = "${device.model}"
      value     = "Tesla K80"
      weight    = 50
    }

    affinity {
      attribute = "${device.model}"
      value     = "Nividia A100"
      weight    = 50
    }

    task "task-1" {
      driver = "docker"
      config {
        image = "hashicorp/task-1"
      }
      resources {
        cpu    = 500 # MHz
        memory = 128 # MB
      }
    }
  }
}
